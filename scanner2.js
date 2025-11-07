// scanner.js - Silent Endpoint & Secrets Scanner (bookmarklet)
// - No process logs shown anywhere (silent mode)
// - Detects parameters, hidden endpoints, firebase hints, tokens/keys/password-like strings
// - UI: floating panel bottom, results only
// - Export: .txt (URL + sensitive findings). Option to include raw secrets in export.
// Usage: load via bookmarklet loader (jsDelivr raw hosted file)

(async function(){
  // --- UI ---
  const panel = document.createElement('div');
  Object.assign(panel.style, {
    position: 'fixed',
    right: '12px',
    bottom: '12px',
    width: '420px',
    maxHeight: '70vh',
    overflowY: 'auto',
    backgroundColor: '#fff',
    color: '#111',
    padding: '10px',
    zIndex: 2147483647,
    border: '1px solid #ddd',
    borderRadius: '8px',
    boxShadow: '0 6px 18px rgba(0,0,0,0.12)',
    fontFamily: 'Inter, Arial, sans-serif',
    fontSize: '13px'
  });

  panel.innerHTML = `
  <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px">
    <strong style="font-size:14px">Silent Scanner</strong>
    <div style="display:flex;gap:6px;align-items:center">
      <select id="scan-filter" title="Filter" style="padding:4px;">
        <option value="all">All</option>
        <option value="api">API-like</option>
        <option value="local">Local only</option>
        <option value="external">External only</option>
        <option value="sensitive">Sensitive only</option>
        <option value="firebase">Firebase only</option>
      </select>
      <label style="font-size:12px"><input id="detect-keys" type="checkbox" checked style="vertical-align:middle"> Detect</label>
    </div>
  </div>
  <div id="results" style="max-height:56vh;overflow:auto;border-top:1px solid #eee;padding-top:8px"></div>
  <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:8px">
    <label style="font-size:12px"><input id="include-raw" type="checkbox"> Include raw secrets in export</label>
    <button id="copy-all" style="padding:6px 8px">Copy</button>
    <button id="export-txt" style="padding:6px 8px">Export .txt</button>
    <button id="close-panel" style="padding:6px 8px">Close</button>
  </div>
  `;

  document.body.appendChild(panel);

  const resultsDiv = panel.querySelector('#results');
  const filterSelect = panel.querySelector('#scan-filter');
  const detectKeysCheckbox = panel.querySelector('#detect-keys');
  const includeRawCheckbox = panel.querySelector('#include-raw');

  // --- config ---
  const MAX_DEPTH = 3;
  const excludedHosts = [
    /(^|\.)googleapis\.com$/,
    /(^|\.)gstatic\.com$/,
    /(^|\.)googleusercontent\.com$/,
    /(^|\.)cloudflare\.com$/,
    /(^|\.)cdnjs\.cloudflare\.com$/
  ];

  // --- detectors ---
  const DET = {
    firebaseApiKey: /AIza[0-9A-Za-z\-_]{35}/g,
    firebaseDB: /(https?:\/\/[A-Za-z0-9\-]+(?:\.firebaseio\.com|\.firebasedatabase\.app))(?:[:\/\w\-\.\?\=\&]*)/gi,
    firebaseProjectId: /["'\s]projectId["']?\s*[:=]\s*["']?([a-z0-9\-]{6,})["']?/gi,
    firebaseStorage: /["'\s]storageBucket["']?\s*[:=]\s*["']?([a-z0-9\-\.]+(?:appspot\.com|storage\.googleapis\.com)?)["']?/gi,
    googleClientId: /[0-9]{1,}-[0-9A-Za-z_]+\.apps\.googleusercontent\.com/g,
    bearerJwt: /\bBearer\s+([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)\b/gi,
    jwtLike: /\b([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)\b/g,
    awsKey: /\b(A3T|AKIA|ASIA)[A-Z0-9]{16}\b/g,
    longHex: /\b[0-9a-fA-F]{32,}\b/g,
    pwdParam: /(?:password|pwd|pass|secret|token|api[_-]?key|apikey|access[_-]?token|client_secret|private_key)\s*(?:=|:)\s*['"]?([^\s'";,<>]{4,200})/gi,
    urlWithPort: /https?:\/\/[^\s'"]+:\d{2,5}[^\s'"]*/gi
  };

  function hostExcluded(host){
    try{ return excludedHosts.some(r=>r.test(host)); }catch(e){ return false; }
  }
  function isLocal(u){
    try{ const url = new URL(u, location.href); return url.origin === location.origin && !hostExcluded(url.host); }catch(e){ return false; }
  }
  function isApiLike(u){
    try{
      const url = new URL(u, location.href);
      return url.pathname.includes('/api/') || url.host.startsWith('api.') || /\/v\d+(\.|\/)/.test(url.pathname) || /\/graphql$/.test(url.pathname);
    }catch(e){
      return /\/api\//.test(u) || /:\w+/.test(u) || /\{.+\}/.test(u);
    }
  }

  // storage for results
  const seen = new Set();
  const found = new Map(); // url -> { params:Set, sensitive: Array<{type,value}>, source, local, apiLike, firebaseMeta:{} }

  function addFound(url, source='detected'){
    try{
      const abs = new URL(url, location.href).href;
      if(!found.has(abs)) {
        found.set(abs, { params: new Set(), sensitive: [], source, local: isLocal(abs), apiLike: isApiLike(abs), firebaseMeta: {} });
      }
      return abs;
    }catch(e){ return null; }
  }

  function extractParams(u){
    const params = new Set();
    try{
      (u.match(/\{([^}]+)\}/g)||[]).forEach(x=>params.add(x.replace(/[{}]/g,'')));
      (u.match(/:([a-zA-Z0-9_]+)/g)||[]).forEach(x=>params.add(x.replace(/^:/,'')));
      const parsed = new URL(u, location.href);
      for(const k of parsed.searchParams.keys()) params.add(k);
    }catch(e){}
    return params;
  }

  async function fetchTextQuiet(url){
    try{
      const r = await fetch(url, { credentials: 'same-origin' });
      if(!r.ok) return null;
      return await r.text();
    }catch(e){ return null; }
  }

  function scanSensitive(text){
    if(!text) return [];
    const res = [];
    for(const m of text.matchAll(DET.firebaseApiKey) || []) res.push({type:'firebase_api_key', value:m[0]});
    for(const m of text.matchAll(DET.firebaseDB) || []) res.push({type:'firebase_database_url', value:m[1]});
    for(const m of text.matchAll(DET.firebaseProjectId) || []) res.push({type:'firebase_project_id', value:m[1]});
    for(const m of text.matchAll(DET.firebaseStorage) || []) res.push({type:'firebase_storage_bucket', value:m[1]});
    for(const m of text.matchAll(DET.googleClientId) || []) res.push({type:'google_client_id', value:m[0]});
    for(const m of text.matchAll(DET.bearerJwt) || []) res.push({type:'bearer_jwt', value:m[1]});
    for(const m of text.matchAll(DET.jwtLike) || []) {
      const v = m[1] || m[0];
      if(v.split('.').length===3 && v.length>20) res.push({type:'jwt_like', value:v});
    }
    for(const m of text.matchAll(DET.awsKey) || []) res.push({type:'aws_key', value:m[0]});
    for(const m of text.matchAll(DET.longHex) || []) res.push({type:'long_hex', value:m[0]});
    for(const m of text.matchAll(DET.pwdParam) || []) { if(m[1] && m[1].length>3) res.push({type:'password_like', value:m[1]}); }
    for(const m of text.matchAll(DET.urlWithPort) || []) res.push({type:'url_with_port', value:m[0]});
    // dedupe
    const uniq = [], seenv = new Set();
    for(const it of res) { const key = it.type + '|' + it.value; if(!seenv.has(key)){ seenv.add(key); uniq.push(it); } }
    return uniq;
  }

  function extractCandidatesFromText(text){
    if(!text) return [];
    const s = new Set();
    const re1 = /['"]((?:https?:\/\/|\/\/|\/|\.\.\/|\.\/)[^'"]{1,800})['"]/g;
    for(const m of text.matchAll(re1)) s.add(m[1]);
    const re2 = /`([^`]{1,800})`/g;
    for(const m of text.matchAll(re2)) s.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    const ajaxRe = /(?:fetch|axios\.(?:get|post|put|delete|patch)|open)\s*\(\s*['"`]((?:https?:\/\/|\/|\.\.\/|\.\/)[^'"`]{1,800})['"`]/g;
    for(const m of text.matchAll(ajaxRe)) s.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    return Array.from(s);
  }

  async function process(url, depth=0, source='root'){
    if(depth > MAX_DEPTH) return;
    let abs;
    try { abs = new URL(url, location.href).href; } catch(e){ return; }
    if(seen.has(abs)) return;
    seen.add(abs);
    addFound(abs, source);
    const params = extractParams(abs);
    for(const p of params) found.get(abs).params.add(p);
    // if not local origin, don't fetch (just record)
    if(!isLocal(abs)) return;
    const text = await fetchTextQuiet(abs);
    if(!text) return;
    if(detectKeysCheckbox.checked){
      const sensitive = scanSensitive(text);
      for(const s of sensitive){
        found.get(abs).sensitive.push(s);
        if(s.type && s.type.startsWith('firebase')) found.get(abs).firebaseMeta[s.type] = s.value;
      }
    }
    const cands = extractCandidatesFromText(text);
    for(const c of cands){
      try{
        const resolved = new URL(c, abs).href;
        addFound(resolved, abs);
        const ps = extractParams(c);
        for(const p of ps) found.get(resolved).params.add(p);
        if(isLocal(resolved) || isApiLike(c) || isApiLike(resolved)) await process(resolved, depth+1, abs);
      }catch(e){}
    }
  }

  // gather resource candidates silently
  const resources = new Set();
  try { performance.getEntriesByType('resource').map(r=>r.name).forEach(u=>resources.add(u)); } catch(e){}
  document.querySelectorAll('script[src]').forEach(s => resources.add(s.src));
  document.querySelectorAll('script:not([src])').forEach(s => {
    try { extractCandidatesFromText(s.textContent||'').forEach(p=>resources.add(p)); } catch(e){}
  });
  try { extractCandidatesFromText(document.documentElement.outerHTML||document.body.innerHTML).forEach(p=>resources.add(p)); } catch(e){}

  // process all resources (silent)
  for(const r of resources) { await process(r, 0, 'resource'); }

  // render results (no process logs)
  function redact(val){
    if(!val) return '';
    const s = String(val);
    if(s.length > 44) return s.slice(0,12) + '…' + s.slice(-12);
    return s;
  }

  function buildList(){
    const list = [];
    for(const [u, meta] of found.entries()){
      list.push({
        url: u,
        params: Array.from(meta.params),
        sensitive: meta.sensitive.slice(),
        source: meta.source,
        local: meta.local,
        apiLike: meta.apiLike,
        firebaseMeta: Object.assign({}, meta.firebaseMeta)
      });
    }
    const f = filterSelect.value;
    let filtered = list;
    if(f === 'api') filtered = list.filter(i=>i.apiLike);
    if(f === 'local') filtered = list.filter(i=>i.local);
    if(f === 'external') filtered = list.filter(i=>!i.local);
    if(f === 'sensitive') filtered = list.filter(i=>i.sensitive && i.sensitive.length>0);
    if(f === 'firebase') filtered = list.filter(i=>Object.keys(i.firebaseMeta).length>0 || /firebaseio\.com|firebasedatabase\.app|firebaseapp\.com|storage\.googleapis\.com/.test(i.url));
    filtered.sort((a,b) => (b.sensitive.length|0) - (a.sensitive.length|0) || (b.apiLike|0) - (a.apiLike|0));
    return filtered;
  }

  function render(){
    const rows = buildList();
    if(rows.length === 0){
      resultsDiv.innerHTML = `<div style="color:#666">No endpoints found.</div>`;
      return;
    }
    const html = rows.map(it => {
      const sensHtml = (it.sensitive && it.sensitive.length>0) ? `<div style="margin-top:6px;color:#900;font-weight:600">⚠ Sensitive (${it.sensitive.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.sensitive.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code>${escapeHtml(redact(s.value))}</code></li>`).join('')}</ul>` : '';
      const fbHtml = (it.firebaseMeta && Object.keys(it.firebaseMeta).length>0) ? `<div style="margin-top:6px;color:#0366d6"><strong>Firebase:</strong> ${Object.entries(it.firebaseMeta).map(([k,v])=>`${escapeHtml(k)}=${escapeHtml(redact(v))}`).join(', ')}</div>` : '';
      return `<div style="padding:8px;border-bottom:1px solid #eee">
        <div style="word-break:break-all"><a href="${it.url}" target="_blank" rel="noreferrer noopener">${escapeHtml(it.url)}</a></div>
        <div style="font-size:12px;color:#444;margin-top:6px">
          ${it.params.length?`params: ${escapeHtml(it.params.join(', '))} `:''}
          <span style="margin-left:8px;color:#666">src: ${escapeHtml(it.source)}</span>
          <span style="margin-left:8px;color:#666">local: ${it.local}</span>
          <span style="margin-left:8px;color:#666">apiLike: ${it.apiLike}</span>
        </div>
        ${sensHtml}
        ${fbHtml}
      </div>`;
    }).join('');
    resultsDiv.innerHTML = html;
  }

  function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

  render();

  // copy all: URL + sensitive (raw values redacted unless includeRaw checked)
  panel.querySelector('#copy-all').onclick = async ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    const lines = [];
    for(const r of rows){
      const sens = r.sensitive.map(s=> includeRaw ? `${s.type}:${s.value}` : `${s.type}:[REDACTED]`).join('; ');
      lines.push(`${r.url}${r.params.length?` | params: ${r.params.join(',')}`:''}${sens?` | sensitive: ${sens}`:''}`);
    }
    const out = lines.join('\n');
    try{ await navigator.clipboard.writeText(out); alert(`Copied ${rows.length} items`); }catch(e){ const ta=document.createElement('textarea'); ta.value=out; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); alert('Copied (fallback)'); }
  };

  // export txt: URL + that sensitive block (raw if includeRaw)
  panel.querySelector('#export-txt').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    const lines = [];
    for(const r of rows){
      lines.push(`URL: ${r.url}`);
      if(r.params.length) lines.push(`Params: ${r.params.join(', ')}`);
      if(r.sensitive.length){
        lines.push('Sensitive:');
        for(const s of r.sensitive) lines.push(`  - ${s.type}: ${ includeRaw ? s.value : '[REDACTED]' }`);
      }
      if(Object.keys(r.firebaseMeta||{}).length){
        lines.push('Firebase hints:');
        for(const [k,v] of Object.entries(r.firebaseMeta)) lines.push(`  - ${k}: ${ includeRaw ? v : '[REDACTED]' }`);
      }
      lines.push(''); // separator
    }
    const blob = new Blob([lines.join('\n')], {type:'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'endpoints.txt'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  panel.querySelector('#close-panel').onclick = ()=> panel.remove();

})();
