// scanner.js - Silent Endpoint & Secrets Scanner (bookmarklet) - OPTIMIZED VERSION
// - Categories: All, API, Fuzzing local, Fuzzing external, Sensitive information
// - Sensitive includes firebase, aws, database, username/password, email, smtp, app_key, etc.
// - Keeps progress bar, export behavior, copy, redact, ignore list, and previous detectors
// - OPTIMIZED: Ignores static files (.css, .jpg, .png, .ico, .mp4, .mp3, etc.) for faster scanning
(async function(){
  // UI
  const panel = document.createElement('div');
  Object.assign(panel.style, {
    position: 'fixed',
    right: '12px',
    bottom: '12px',
    width: '520px',
    maxHeight: '76vh',
    overflowY: 'auto',
    backgroundColor: '#fff',
    color: '#111',
    padding: '10px',
    zIndex: 2147483647,
    border: '1px solid #ddd',
    borderRadius: '8px',
    boxShadow: '0 6px 18px rgba(0,0,0,0.12)',
    fontFamily: 'Arial, sans-serif',
    fontSize: '13px'
  });

  panel.innerHTML = `
  <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:8px">
    <strong style="font-size:14px">Silent Scanner (Optimized)</strong>
    <div style="display:flex;gap:6px;align-items:center">
      <select id="scan-filter" title="Filter" style="padding:4px;">
        <option value="all">All</option>
        <option value="api">API</option>
        <option value="fuzzing">Fuzzing local</option>
        <option value="fuzzing-external">Fuzzing external</option>
        <option value="sensitive">Sensitive information</option>
      </select>
      <label style="font-size:12px"><input id="detect-keys" type="checkbox" checked style="vertical-align:middle"> Detect</label>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
    <div id="scan-status" style="font-size:12px;color:#666">Ready</div>
    <div style="flex:1;background:#f1f1f1;height:8px;border-radius:4px;overflow:hidden;margin-left:8px">
      <div id="scan-progress" style="height:8px;width:0%;background:#0366d6"></div>
    </div>
  </div>
  <div id="results" style="max-height:60vh;overflow:auto;border-top:1px solid #eee;padding-top:8px"></div>
  <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:8px;flex-wrap:wrap">
    <div style="font-size:11px;color:#666;margin-right:auto" id="scan-info">Ignoring static files for speed</div>
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
  const scanStatus = panel.querySelector('#scan-status');
  const scanProgressBar = panel.querySelector('#scan-progress');
  const scanInfo = panel.querySelector('#scan-info');

  // config
  const MAX_DEPTH = 3;
  
  // Static file extensions to ignore for performance optimization
  const STATIC_FILE_EXTENSIONS = new Set([
    'css', 'scss', 'sass', 'less',
    'jpg', 'jpeg', 'png', 'gif', 'webp', 'svg', 'ico', 'bmp', 'tiff',
    'mp4', 'mp3', 'avi', 'mov', 'wmv', 'flv', 'webm', 'ogg', 'wav', 'aac',
    'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
    'zip', 'rar', '7z', 'tar', 'gz',
    'ttf', 'woff', 'woff2', 'eot',
    'swf', 'fla'
  ]);

  // MIME types to ignore
  const STATIC_MIME_TYPES = new Set([
    'text/css',
    'image/jpeg', 'image/png', 'image/gif', 'image/webp', 'image/svg+xml', 'image/x-icon',
    'video/mp4', 'video/avi', 'video/quicktime', 'video/x-msvideo',
    'audio/mpeg', 'audio/wav', 'audio/ogg', 'audio/aac',
    'application/pdf', 'application/zip', 'application/x-rar-compressed',
    'font/woff', 'font/woff2', 'application/font-woff', 'application/font-woff2',
    'application/x-shockwave-flash'
  ]);

  const excludedHosts = [
    /(^|\.)googleapis\.com$/,
    /(^|\.)gstatic\.com$/,
    /(^|\.)googleusercontent\.com$/,
    /(^|\.)cloudflare\.com$/,
    /(^|\.)cdnjs\.cloudflare\.com$/,
    /(^|\.)fontawesome\.com$/,
    /(^|\.)avatars\.githubusercontent\.com$/,
    /(^|\.)unpkg\.com$/,
    /(^|\.)gravatar\.com$/
    // NOTE: jsdelivr & githack are intentionally NOT excluded
  ];

  // Helper function to check if URL points to a static file
  function isStaticFile(url) {
    try {
      const urlObj = new URL(url, location.href);
      const pathname = urlObj.pathname.toLowerCase();
      
      // Check file extension
      const lastDot = pathname.lastIndexOf('.');
      if (lastDot > -1) {
        const extension = pathname.substring(lastDot + 1);
        if (STATIC_FILE_EXTENSIONS.has(extension)) {
          return true;
        }
      }
      
      // Check for common static file patterns
      if (pathname.includes('/assets/') || 
          pathname.includes('/static/') || 
          pathname.includes('/public/') ||
          pathname.includes('/images/') ||
          pathname.includes('/img/') ||
          pathname.includes('/css/') ||
          pathname.includes('/js/') && pathname.endsWith('.js') && !pathname.includes('api')) {
        return true;
      }
      
      return false;
    } catch (e) {
      return false;
    }
  }

  // Enhanced function to check if resource should be fetched
  async function shouldFetchResource(url) {
    // Skip static files
    if (isStaticFile(url)) {
      return false;
    }
    
    // For performance, do a quick HEAD request to check content-type for same-origin resources
    if (isLocal(url)) {
      try {
        const response = await fetch(url, { 
          method: 'HEAD', 
          credentials: 'same-origin',
          signal: AbortSignal.timeout(2000) // 2 second timeout
        });
        
        const contentType = response.headers.get('content-type');
        if (contentType) {
          const mimeType = contentType.split(';')[0].toLowerCase();
          if (STATIC_MIME_TYPES.has(mimeType)) {
            return false;
          }
        }
      } catch (e) {
        // If HEAD request fails, we'll still try to process it
      }
    }
    
    return true;
  }

  // detectors (jwt detection intentionally removed)
  const DET = {
    firebaseApiKey: /AIza[0-9A-Za-z\-_]{35}/g,
    firebaseDB: /(https?:\/\/[A-Za-z0-9\-]+(?:\.firebaseio\.com|\.firebasedatabase\.app))(?:[:\/\w\-\.\?\=\&]*)/gi,
    firebaseProjectId: /["'\s]projectId["']?\s*[:=]\s*["']?([a-z0-9\-]{6,})["']?/gi,
    firebaseStorage: /["'\s]storageBucket["']?\s*[:=]\s*["']?([a-z0-9\-\.]+(?:appspot\.com|storage\.googleapis\.com)?)["']?/gi,
    googleClientId: /[0-9]{1,}-[0-9A-Za-z_]+\.apps\.googleusercontent\.com/g,
    awsKey: /\b(A3T|AKIA|ASIA)[A-Z0-9]{16}\b/g,
    longHex: /\b[0-9a-fA-F]{32,}\b/g,
    pwdParam: /(?:username|user|email|password|pwd|pass|secret|token|api[_-]?key|apikey|access[_-]?token|client_secret|private_key)\s*(?:=|:)\s*['"]?([^\s'";,<>]{4,200})/gi,
    urlWithPort: /https?:\/\/[^\s'"]+:\d{2,5}[^\s'"]*/gi,
    // added detectors for various sensitive info
    dbConn: /(mongodb(?:\+srv)?:\/\/[^\s'"]+|postgres(?:ql)?:\/\/[^\s'"]+|mysql:\/\/[^\s'"]+|redis:\/\/[^\s'"]+)/gi,
    smtpUrl: /(smtp:\/\/[^\s'"]+|smtp:[^\s'"]+|smtp\.[a-z0-9\.-]+\.[a-z]{2,})/gi,
    appKey: /(?:app[_-]?key|application[_-]?key|client[_-]?id|client[_-]?secret)\s*(?:=|:)\s*['"]?([A-Za-z0-9\-_]{6,200})/gi,
    emailLike: /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g
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

  // Fuzzing detection: parameter-bearing URL (has ?= or path params)
  function isParamBearing(u){
    try{
      const url = new URL(u, location.href);
      if(url.search && url.search.includes('=')) return true;
      if(/:\w+/.test(url.pathname) || /\{[^}]+\}/.test(url.pathname)) return true;
      return false;
    }catch(e){
      return /[?].*=/.test(u) || /:\w+/.test(u) || /\{[^}]+\}/.test(u);
    }
  }

  // results store
  const seen = new Set();
  const found = new Map();
  const skipped = new Set(); // Track skipped static files
  // found: url -> { params:Set, sensitive: [{type,value}], source, local, apiLike, firebaseMeta:{} }

  function addFound(url, source='detected'){
    try{
      const abs = new URL(url, location.href).href;
      if(!found.has(abs)){
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
      const r = await fetch(url, { 
        credentials: 'same-origin',
        signal: AbortSignal.timeout(5000) // 5 second timeout
      });
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
    for(const m of text.matchAll(DET.awsKey) || []) res.push({type:'aws_key', value:m[0]});
    for(const m of text.matchAll(DET.longHex) || []) res.push({type:'long_hex', value:m[0]});
    for(const m of text.matchAll(DET.pwdParam) || []) { if(m[1] && m[1].length>0) res.push({type:'credential_like', value:m[1]}); }
    for(const m of text.matchAll(DET.urlWithPort) || []) res.push({type:'url_with_port', value:m[0]});
    for(const m of text.matchAll(DET.dbConn) || []) res.push({type:'database_conn', value:m[0]});
    for(const m of text.matchAll(DET.smtpUrl) || []) res.push({type:'smtp_hint', value:m[0]});
    for(const m of text.matchAll(DET.appKey) || []) { if(m[1] && m[1].length>0) res.push({type:'app_key', value:m[1]}); }
    for(const m of text.matchAll(DET.emailLike) || []) res.push({type:'email', value:m[0]});
    // dedupe
    const uniq = [], seenv = new Set();
    for(const it of res){ const key = it.type + '|' + it.value; if(!seenv.has(key)){ seenv.add(key); uniq.push(it); } }
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

  // progress helpers
  let totalResources = 0;
  let processedResources = 0;
  let skippedResources = 0;
  
  function setProgress(percent){
    scanProgressBar.style.width = percent + '%';
    scanStatus.textContent = `Scanning... ${percent}%`;
    scanInfo.textContent = `Skipped ${skippedResources} static files for speed`;
  }
  
  function incProgress(){
    processedResources++;
    const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100;
    setProgress(pct);
  }

  function incSkipped(){
    skippedResources++;
    processedResources++; // Count as processed for progress calculation
    const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100;
    setProgress(pct);
  }

  async function process(url, depth=0, source='root'){
    if(depth > MAX_DEPTH) return;
    let abs;
    try{ abs = new URL(url, location.href).href; }catch(e){ return; }
    if(seen.has(abs)) return;
    seen.add(abs);
    
    // Check if this is a static file we should skip
    if(isStaticFile(abs)) {
      skipped.add(abs);
      incSkipped();
      return;
    }
    
    addFound(abs, source);
    const params = extractParams(abs);
    for(const p of params) found.get(abs).params.add(p);
    
    // Only fetch same-origin (local) resources to avoid cross-origin noise
    const local = isLocal(abs);
    if(!local){
      // we still add the resource entry (URL) but do not fetch its body
      incProgress();
      return;
    }
    
    // Additional check before fetching
    if(!(await shouldFetchResource(abs))) {
      skipped.add(abs);
      incSkipped();
      return;
    }
    
    const text = await fetchTextQuiet(abs);
    incProgress();
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
        // Don't process static files in candidates either
        if(!isStaticFile(resolved)) {
          addFound(resolved, abs);
          const ps = extractParams(c);
          for(const p of ps) found.get(resolved).params.add(p);
          if(isLocal(resolved) || isApiLike(c) || isApiLike(resolved)) {
            await process(resolved, depth+1, abs);
          }
        }
      }catch(e){}
    }
  }

  // gather resources silently - but filter out static files early
  const resources = new Set();
  try{ 
    performance.getEntriesByType('resource')
      .map(r=>r.name)
      .filter(u => !isStaticFile(u)) // Filter out static files early
      .forEach(u=>resources.add(u)); 
  }catch(e){}
  
  document.querySelectorAll('script[src]').forEach(s => {
    if(!isStaticFile(s.src)) {
      resources.add(s.src);
    }
  });
  
  document.querySelectorAll('script:not([src])').forEach(s => {
    try{ 
      extractCandidatesFromText(s.textContent||'')
        .filter(p => !isStaticFile(p))
        .forEach(p=>resources.add(p)); 
    }catch(e){}
  });
  
  try{ 
    extractCandidatesFromText(document.documentElement.outerHTML||document.body.innerHTML)
      .filter(p => !isStaticFile(p))
      .forEach(p=>resources.add(p)); 
  }catch(e){}

  // initialize progress totals
  totalResources = resources.size || 1;
  processedResources = 0;
  skippedResources = 0;
  setProgress(0);

  // process all (silent) - with optimizations
  const resourcesArray = Array.from(resources);
  for(const r of resourcesArray){ 
    await process(r, 0, 'resource'); 
  }

  // ensure progress complete
  setProgress(100);
  scanStatus.textContent = `Scan complete - Found ${found.size} endpoints`;
  scanInfo.textContent = `Optimized: Skipped ${skippedResources} static files for ${Math.round(((skippedResources)/(found.size + skippedResources))*100)}% speed boost`;

  // rendering + filter behavior
  function redact(val){
    if(!val) return '';
    const s = String(val);
    if(s.length > 44) return s.slice(0,12) + '…' + s.slice(-12);
    return s;
  }

  // helper: determine if item is "sensitive" by types we want grouped into Sensitive information
  function isSensitiveItem(meta){
    if(!meta) return false;
    if((meta.sensitive && meta.sensitive.length>0)) return true;
    // additional heuristics: firebaseMeta keys
    if(meta.firebaseMeta && Object.keys(meta.firebaseMeta).length>0) return true;
    return false;
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
    if(f === 'api') filtered = list.filter(i=>i.apiLike && !isSensitiveItem(i));
    if(f === 'fuzzing') filtered = list.filter(i=>i.local && isParamBearing(i.url) && !isSensitiveItem(i));
    if(f === 'fuzzing-external') filtered = list.filter(i=>!i.local && isParamBearing(i.url) && !hostExcluded((() => { try { return new URL(i.url).host } catch(e){ return '' } })()));
    if(f === 'sensitive') filtered = list.filter(i=>isSensitiveItem(i));
    // 'all' returns everything (no filter)
    filtered.sort((a,b) => (isSensitiveItem(b)?1:0) - (isSensitiveItem(a)?1:0) || (b.apiLike|0) - (a.apiLike|0));
    return filtered;
  }

  function render(){
    const rows = buildList();
    if(rows.length === 0){ resultsDiv.innerHTML = `<div style="color:#666">No endpoints found.</div>`; return; }
    const html = rows.map(it => {
      const sensHtml = (it.sensitive && it.sensitive.length>0) ? `<div style="margin-top:6px;color:#900;font-weight:600">⚠ Sensitive (${it.sensitive.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.sensitive.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code>${escapeHtml(redact(s.value))}</code></li>`).join('')}</ul>` : '';
      const fbHtml = (it.firebaseMeta && Object.keys(it.firebaseMeta).length>0) ? `<div style="margin-top:6px;color:#0366d6"><strong>Firebase hints:</strong> ${Object.entries(it.firebaseMeta).map(([k,v])=>`${escapeHtml(k)}=${escapeHtml(redact(v))}`).join(', ')}</div>` : '';
      return `<div style="padding:8px;border-bottom:1px solid #eee">
        <div style="word-break:break-all"><a href="${it.url}" target="_blank" rel="noreferrer noopener">${escapeHtml(it.url)}</a></div>
        <div style="font-size:12px;color:#444;margin-top:6px">
          ${it.params.length?`params: ${escapeHtml(it.params.join(', '))} `:''}
          <span style="margin-left:8px;color:#666">src: ${escapeHtml(it.source)}</span>
          <span style="margin-left:8px;color:#666">fuzzingCandidate: ${isParamBearing(it.url)}</span>
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

  // initial render
  render();

  // realtime filter change -> render
  filterSelect.onchange = render;
  detectKeysCheckbox.onchange = render;

  // copy
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

  // export .txt respects current filter and groups when filter='all' into the requested categories
  panel.querySelector('#export-txt').onclick = ()=>{
    const f = filterSelect.value;
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    const lines = [];

    function pushItem(r){
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

    if(f === 'all'){
      // group into only the allowed categories: FUZZING LOCAL, FUZZING EXTERNAL, API, SENSITIVE, ALL (catch-all)
      const groups = { FUZZING_LOCAL:[], FUZZING_EXTERNAL:[], API:[], SENSITIVE:[], ALL:[] };
      for(const r of rows){
        if(isSensitiveItem(r)) groups.SENSITIVE.push(r);
        else if(isParamBearing(r.url) && r.local) groups.FUZZING_LOCAL.push(r);
        else if(isParamBearing(r.url) && !r.local) groups.FUZZING_EXTERNAL.push(r);
        else if(r.apiLike) groups.API.push(r);
        else groups.ALL.push(r); // catch-all falls under 'All' category
      }
      if(groups.FUZZING_LOCAL.length){ lines.push('=== FUZZING (LOCAL) ===',''); groups.FUZZING_LOCAL.forEach(pushItem); lines.push(''); }
      if(groups.FUZZING_EXTERNAL.length){ lines.push('=== FUZZING (EXTERNAL) ===',''); groups.FUZZING_EXTERNAL.forEach(pushItem); lines.push(''); }
      if(groups.API.length){ lines.push('=== API ===',''); groups.API.forEach(pushItem); lines.push(''); }
      if(groups.SENSITIVE.length){ lines.push('=== SENSITIVE INFORMATION ===',''); groups.SENSITIVE.forEach(pushItem); lines.push(''); }
      if(groups.ALL.length){ lines.push('=== ALL (OTHER) ===',''); groups.ALL.forEach(pushItem); lines.push(''); }
    } else {
      for(const r of rows) pushItem(r);
    }

    const blob = new Blob([lines.join('\n')], {type:'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'endpoints-optimized.txt'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  panel.querySelector('#close-panel').onclick = ()=> panel.remove();

})();
