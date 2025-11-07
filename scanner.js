javascript:(async function(){
  const panel=document.createElement("div");
  Object.assign(panel.style,{
    position:"fixed",bottom:"0",left:"0",width:"100%",maxHeight:"70%",
    overflowY:"auto",backgroundColor:"#fff",color:"#000",padding:"10px",
    zIndex:2147483647,borderTop:"2px solid #000",fontFamily:"Arial, sans-serif",
    fontSize:"13px"
  });

  panel.innerHTML = `
  <div style="display:flex;flex-direction:column;gap:8px">
    <div style="display:flex;justify-content:space-between;align-items:center;gap:8px">
      <h4 style="margin:0">Endpoint & Secrets Scanner</h4>
      <div style="display:flex;align-items:center;gap:8px">
        <select id="scan-filter" title="Filter">
          <option value="all">All</option>
          <option value="api">API-like only</option>
          <option value="external">External only</option>
          <option value="local">Local only</option>
          <option value="sensitive">Sensitive only</option>
          <option value="firebase">Firebase only</option>
        </select>
        <label style="margin-left:8px"><input type="checkbox" id="detect-keys" checked> Detect keys</label>
        <label style="margin-left:8px"><input type="checkbox" id="include-raw"> Include raw secrets in exports</label>
        <button id="export-json">Export JSON</button>
        <button id="export-csv">Export CSV</button>
        <button id="copy-all">Copy All</button>
        <button id="close-scan">Close</button>
      </div>
    </div>
    <div id="status" style="font-size:12px;color:#333">Scanning — please wait...</div>
    <div id="results" style="max-height:56vh;overflow:auto;padding-left:6px;border-top:1px solid #eee"></div>
  </div>`;

  document.body.appendChild(panel);
  const resultsDiv = panel.querySelector("#results");
  const statusDiv = panel.querySelector("#status");
  const filterSelect = panel.querySelector("#scan-filter");
  const detectKeysCheckbox = panel.querySelector("#detect-keys");
  const includeRawCheckbox = panel.querySelector("#include-raw");

  const MAX_DEPTH = 3;
  const excludedHosts = [
    /(^|\.)googleapis\.com$/,
    /(^|\.)gstatic\.com$/,
    /(^|\.)googleusercontent\.com$/,
    /(^|\.)cloudflare\.com$/,
    /(^|\.)cdnjs\.cloudflare\.com$/
  ];

  const seenUrls = new Set();
  const found = new Map(); // url -> { params:Set, keys:Set (raw), sensitive:Array, source, local, apiLike, firebaseMeta }

  function hostExcluded(host){
    try{ return excludedHosts.some(r=>r.test(host)); }catch(e){ return false; }
  }
  function isLocal(u){
    try{ const url=new URL(u, location.href); return url.origin === location.origin && !hostExcluded(url.host); }catch(e){ return false; }
  }
  function isApiLike(u){
    try{
      const url=new URL(u, location.href);
      return url.pathname.includes('/api/') || url.host.startsWith('api.') || /\/v\d+(\.|\/)/.test(url.pathname) || /\/graphql$/.test(url.pathname);
    }catch(e){
      return /\/api\//.test(u) || /:\w+/.test(u) || /\{.+\}/.test(u);
    }
  }

  // Sensitive detectors
  const detectors = {
    firebaseApiKey: /AIza[0-9A-Za-z\-_]{35}/g,
    firebaseDatabaseUrl: /(https?:\/\/[A-Za-z0-9\-]+(?:\.firebaseio\.com|\.firebasedatabase\.app))(?:[:\/\w\-\.\?\=\&]*)/gi,
    firebaseProjectId: /["'\s]projectId["']?\s*[:=]\s*["']?([a-z0-9\-]{6,})["']?/gi,
    firebaseStorageBucket: /["'\s]storageBucket["']?\s*[:=]\s*["']?([a-z0-9\-\.]+(?:appspot\.com|storage\.googleapis\.com)?)["']?/gi,
    googleClientId: /[0-9]{1,}-[0-9A-Za-z_]+\.apps\.googleusercontent\.com/g,
    bearerJwt: /\bBearer\s+([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)\b/gi,
    jwtCompact: /\b([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)\b/g, // will be filtered further
    awsAccessKey: /\b(A3T|AKIA|ASIA)[A-Z0-9]{16}\b/g,
    longHex: /\b[0-9a-fA-F]{32,}\b/g,
    possiblePasswordParam: /(?:password|pwd|pass|secret|token|api_key|api-key|apikey|access_token|auth_token|client_secret|private_key)\s*(?:=|:)\s*['"]?([^\s'";,<>]{4,200})/gi,
    urlWithPort: /https?:\/\/[^\s/]+:\d{2,5}[^\s'"]*/gi
  };

  function extractSensitive(text, url){
    const founds = [];
    if(!text) return founds;
    // Firebase API keys
    for(const m of text.matchAll(detectors.firebaseApiKey) || []) founds.push({type:'firebase_api_key', value:m[0]});
    // Firebase DB urls
    for(const m of text.matchAll(detectors.firebaseDatabaseUrl) || []) founds.push({type:'firebase_database_url', value:m[1]});
    // projectId
    for(const m of text.matchAll(detectors.firebaseProjectId) || []) founds.push({type:'firebase_project_id', value:m[1]});
    // storage bucket
    for(const m of text.matchAll(detectors.firebaseStorageBucket) || []) founds.push({type:'firebase_storage_bucket', value:m[1]});
    // google client id
    for(const m of text.matchAll(detectors.googleClientId) || []) founds.push({type:'google_client_id', value:m[0]});
    // bearer tokens
    for(const m of text.matchAll(detectors.bearerJwt) || []) founds.push({type:'bearer_jwt', value:m[1]});
    // possible jwt compact (avoid matching common dotted numbers like version strings)
    for(const m of text.matchAll(detectors.jwtCompact) || []) {
      const v = m[1] || m[0];
      if(v.split('.').length===3 && v.length>20) founds.push({type:'jwt_like', value:v});
    }
    // aws keys
    for(const m of text.matchAll(detectors.awsAccessKey) || []) founds.push({type:'aws_key', value:m[0]});
    // long hex
    for(const m of text.matchAll(detectors.longHex) || []) founds.push({type:'long_hex', value:m[0]});
    // password-like params
    for(const m of text.matchAll(detectors.possiblePasswordParam) || []) {
      if(m[1] && m[1].length>3) founds.push({type:'param_password_like', value:m[1]});
    }
    // urls with ports
    for(const m of text.matchAll(detectors.urlWithPort) || []) founds.push({type:'url_with_port', value:m[0]});
    // dedupe by value
    const uniq = [];
    const seen = new Set();
    for(const it of founds){
      if(!seen.has(it.type+'|'+it.value)){
        seen.add(it.type+'|'+it.value);
        uniq.push(it);
      }
    }
    return uniq;
  }

  async function fetchText(url){
    try{
      const res = await fetch(url, { credentials: 'same-origin' });
      if(!res.ok) return null;
      return await res.text();
    }catch(e){
      return null;
    }
  }

  function extractCandidates(text){
    if(!text) return [];
    const set = new Set();
    const re1 = /['"]((?:https?:\/\/|\/\/|\/|\.\.\/|\.\/)[^'"]{1,800})['"]/g;
    for(const m of text.matchAll(re1)) set.add(m[1]);
    const re2 = /`([^`]{1,800})`/g;
    for(const m of text.matchAll(re2)) set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    const ajaxRe = /(?:fetch|axios\.(?:get|post|put|delete|patch)|open)\s*\(\s*['"`]((?:https?:\/\/|\/|\.\.\/|\.\/)[^'"`]{1,800})['"`]/g;
    for(const m of text.matchAll(ajaxRe)) set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    return Array.from(set);
  }

  function addFound(abs, meta = {}){
    try{
      const u = new URL(abs, location.href).href;
      if(!found.has(u)) found.set(u, {
        params: new Set(),
        keys: new Set(),
        sensitive: [],
        source: meta.source || 'detected',
        local: isLocal(u),
        apiLike: isApiLike(u),
        firebaseMeta: {}
      });
    }catch(e){}
  }

  function extractParamsFromUrlString(u){
    const params = new Set();
    try{
      (u.match(/\{([^}]+)\}/g)||[]).forEach(x=>params.add(x.replace(/[{}]/g,'')));
      (u.match(/:([a-zA-Z0-9_]+)/g)||[]).forEach(x=>params.add(x.replace(/^:/,'')));
      const parsed = new URL(u, location.href);
      for(const k of parsed.searchParams.keys()) params.add(k);
    }catch(e){}
    return params;
  }

  async function processUrl(u, depth = 0, source = 'root'){
    if(depth > MAX_DEPTH) return;
    let abs;
    try{ abs = new URL(u, location.href).href; }catch(e){ return; }
    if(seenUrls.has(abs)) return;
    seenUrls.add(abs);
    addFound(abs, {source});
    // params from url
    extractParamsFromUrlString(abs).forEach(p=>found.get(abs).params.add(p));
    // if not same-origin local, don't fetch (but still record)
    if(!isLocal(abs)) return;
    const text = await fetchText(abs);
    if(!text) return;
    if(detectKeysCheckbox.checked){
      // extract sensitive
      const sens = extractSensitive(text, abs);
      for(const s of sens){
        found.get(abs).sensitive.push(s);
        found.get(abs).keys.add(s.value);
        // firebase meta hints
        if(s.type.startsWith('firebase')) {
          found.get(abs).firebaseMeta[s.type] = s.value;
        }
      }
    }
    const candidates = extractCandidates(text);
    for(const c of candidates){
      try{
        const resolved = new URL(c, abs).href;
        addFound(resolved, {source: abs});
        extractParamsFromUrlString(c).forEach(p=>found.get(resolved).params.add(p));
        if(isLocal(resolved) || isApiLike(c) || isApiLike(resolved)) await processUrl(resolved, depth+1, abs);
      }catch(e){}
    }
  }

  // collect resources quietly
  const resources = new Set();
  try{ performance.getEntriesByType('resource').map(r=>r.name).forEach(u=>resources.add(u)); }catch(e){}
  document.querySelectorAll('script[src]').forEach(s=>resources.add(s.src));
  document.querySelectorAll('script:not([src])').forEach(s=>{
    try{ extractCandidates(s.textContent||'').forEach(p=>resources.add(p)); }catch(e){}
  });
  try{ extractCandidates(document.documentElement.outerHTML||document.body.innerHTML).forEach(p=>resources.add(p)); }catch(e){}

  // progress counter (no verbose logs)
  let processed = 0;
  const total = resources.size || 1;
  statusDiv.textContent = `Scanning ${total} resource candidates — please wait...`;

  for(const r of resources){
    await processUrl(r, 0, 'resource');
    processed++;
    // update simple status (no details)
    statusDiv.textContent = `Scanning — ${processed}/${total} resources processed...`;
  }

  // done
  statusDiv.textContent = `Scan complete — ${found.size} unique endpoints found.`;

  // build final list and UI
  function buildList(){
    const list = [];
    for(const [u, meta] of found.entries()){
      list.push({
        url: u,
        params: Array.from(meta.params),
        keys: Array.from(meta.keys),
        sensitive: meta.sensitive, // array of {type, value}
        source: meta.source,
        local: meta.local,
        apiLike: meta.apiLike,
        firebaseMeta: meta.firebaseMeta
      });
    }
    const f = filterSelect.value;
    let filtered = list;
    if(f === 'api') filtered = list.filter(i => i.apiLike);
    if(f === 'external') filtered = list.filter(i => !i.local);
    if(f === 'local') filtered = list.filter(i => i.local);
    if(f === 'sensitive') filtered = list.filter(i => i.sensitive && i.sensitive.length>0);
    if(f === 'firebase') filtered = list.filter(i => Object.keys(i.firebaseMeta).length>0 || (i.url && /firebaseio\.com|firebasedatabase\.app|firebaseapp\.com|googleapis\.com/.test(i.url)));
    filtered.sort((a,b) => (b.sensitive.length|0) - (a.sensitive.length|0) || (b.apiLike|0) - (a.apiLike|0));
    return filtered;
  }

  function redact(v){ if(!v) return ''; const s = String(v); if(s.length>40) return s.slice(0,8)+'...'+s.slice(-8); return s; }

  function render(){
    const rows = buildList();
    if(rows.length===0){
      resultsDiv.innerHTML = '<i>No endpoints found</i>';
      return;
    }
    const html = rows.map(it=>{
      const sensitiveHtml = (it.sensitive && it.sensitive.length>0) ? `<div style="margin-top:6px"><strong style="color:#b22222">Sensitive findings:</strong><ul style="margin:6px 0 0 18px">${it.sensitive.map(s=>`<li>${s.type}: <code>${escapeHtml(redact(s.value))}</code></li>`).join('')}</ul></div>` : '';
      const firebaseHtml = (it.firebaseMeta && Object.keys(it.firebaseMeta).length>0) ? `<div style="margin-top:6px"><strong style="color:#1e90ff">Firebase hints:</strong> ${Object.entries(it.firebaseMeta).map(([k,v])=>`${k}=${escapeHtml(redact(v))}`).join(', ')}</div>` : '';
      return `<div style="padding:8px;border-bottom:1px solid #eee">
        <div><a href="${it.url}" target="_blank" rel="noreferrer noopener">${escapeHtml(it.url)}</a></div>
        <div style="font-size:12px;color:#333;margin-top:6px">
          ${it.params.length?`params: ${escapeHtml(it.params.join(', '))} `:''}
          <span style="margin-left:8px">src: ${escapeHtml(it.source)}</span>
          <span style="margin-left:8px">local: ${it.local}</span>
          <span style="margin-left:8px">apiLike: ${it.apiLike}</span>
          <span style="margin-left:12px;color:#666">sensitiveCount: ${it.sensitive.length}</span>
        </div>
        ${sensitiveHtml}
        ${firebaseHtml}
      </div>`;
    }).join('');
    resultsDiv.innerHTML = html;
  }

  // helpers
  function escapeHtml(s){
    if(!s) return '';
    return String(s).replace(/[&<>"']/g, function(m){ return ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m]); });
  }

  render();
  filterSelect.onchange = render;
  panel.querySelector("#close-scan").onclick = ()=>panel.remove();

  panel.querySelector("#copy-all").onclick = async ()=>{
    const rows = buildList();
    const text = rows.map(r=>{
      const sens = r.sensitive.map(s=>`${s.type}:${s.value}`).join(';');
      return `${r.url}${r.params.length?` | params: ${r.params.join(',')}`:''}${sens?` | sensitive: ${sens}`:''} | src: ${r.source}`;
    }).join("\n");
    try{ await navigator.clipboard.writeText(text); alert(`Copied ${rows.length} items`); }
    catch(e){ const ta=document.createElement('textarea'); ta.value=text; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); alert('Copied (fallback)'); }
  };

  function downloadFile(filename, content){
    const blob = new Blob([content], {type:'application/octet-stream'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  }

  panel.querySelector('#export-json').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    const out = rows.map(r => ({
      url: r.url,
      params: r.params,
      sensitive: includeRaw ? r.sensitive : r.sensitive.map(s=>({type:s.type, value:'[REDACTED]'})),
      source: r.source,
      local: r.local,
      apiLike: r.apiLike,
      firebaseMeta: includeRaw ? r.firebaseMeta : Object.fromEntries(Object.entries(r.firebaseMeta).map(([k,v])=>[k,'[REDACTED]']))
    }));
    downloadFile('endpoints.json', JSON.stringify(out, null, 2));
  };

  panel.querySelector('#export-csv').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    const header = ['url','params','sensitive','source','local','apiLike','firebaseMeta'];
    const csv = [header.join(',')].concat(rows.map(r=>{
      const esc = v=>`"${String(v).replace(/"/g,'""')}"`;
      const sens = includeRaw ? r.sensitive.map(s=>`${s.type}:${s.value}`).join(';') : r.sensitive.map(s=>s.type).join(';');
      const fbmeta = includeRaw ? JSON.stringify(r.firebaseMeta) : JSON.stringify(Object.fromEntries(Object.keys(r.firebaseMeta).map(k=>[k,'[REDACTED]'])));
      return [esc(r.url), esc(r.params.join(';')), esc(sens), esc(r.source), r.local, r.apiLike, esc(fbmeta)].join(',');
    })).join('\n');
    downloadFile('endpoints.csv', csv);
  };

})();
