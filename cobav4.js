// silent-scanner-v4.js - Silent Endpoint & Secrets Scanner (bookmarklet) - UPDATED v4
// - Whitelist extensions (.html, .js, .json, .xml)
// - MIME smart detection option
// - Mode selection (smart / ext-only) before starting
// - Only fetch same-origin (local) resources (record external endpoints but do not deep-scan)
// - Concurrency 5, MAX_DEPTH 3
// - Preserve categories and UI behaviour from v3, export JSON/manual, progress overlay hides after finish
// - Detect misconfig (.env, .git, .htpasswd, config files)

/* eslint-disable no-undef */
(async function(){
  // UI (similar to v3) - but we add mode select and Start button; do not auto-start
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
    <strong style="font-size:14px">Silent Scanner (Optimized - v4)</strong>
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
    <div style="display:flex;gap:6px;align-items:center">
      <label style="font-size:12px">Mode:</label>
      <select id="scan-mode" title="Scan mode" style="padding:4px;">
        <option value="smart">Smart (MIME-aware)</option>
        <option value="ext-only">Extension only (.html, .js, .json, .xml)</option>
      </select>
      <label style="font-size:12px"><input id="same-origin-only" type="checkbox" checked style="vertical-align:middle"> Same-origin only</label>
    </div>
    <div style="margin-left:auto;display:flex;gap:6px">
      <button id="start-scan" style="padding:6px 8px;background:#0366d6;color:#fff;border:none;border-radius:4px">Start</button>
      <button id="stop-scan" style="padding:6px 8px;background:#eee;border:1px solid #ccc;border-radius:4px">Stop</button>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
    <div id="scan-status" style="font-size:12px;color:#666">Ready</div>
    <div style="flex:1;background:#f1f1f1;height:8px;border-radius:4px;overflow:hidden;margin-left:8px">
      <div id="scan-progress" style="height:8px;width:0%;background:#0366d6;transition:width 150ms linear"></div>
    </div>
  </div>

  <div id="results" style="max-height:60vh;overflow:auto;border-top:1px solid #eee;padding-top:8px"></div>

  <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:8px;flex-wrap:wrap">
    <div style="font-size:11px;color:#666;margin-right:auto" id="scan-info">Using whitelist extensions & MIME checks</div>
    <label style="font-size:12px"><input id="include-raw" type="checkbox"> Include raw secrets in export</label>
    <button id="copy-all" style="padding:6px 8px">Copy</button>
    <button id="export-txt" style="padding:6px 8px">Export .txt</button>
    <button id="export-json" style="padding:6px 8px">Export JSON</button>
    <button id="close-panel" style="padding:6px 8px">Close</button>
  </div>
  <div style="font-size:11px;color:#a00;margin-top:6px">Warning: Use only on sites you own or have explicit permission to test.</div>
  `;

  document.body.appendChild(panel);

  // UI refs
  const resultsDiv = panel.querySelector('#results');
  const filterSelect = panel.querySelector('#scan-filter');
  const detectKeysCheckbox = panel.querySelector('#detect-keys');
  const includeRawCheckbox = panel.querySelector('#include-raw');
  const scanStatus = panel.querySelector('#scan-status');
  const scanProgressBar = panel.querySelector('#scan-progress');
  const scanInfo = panel.querySelector('#scan-info');
  const startBtn = panel.querySelector('#start-scan');
  const stopBtn = panel.querySelector('#stop-scan');
  const modeSelect = panel.querySelector('#scan-mode');
  const sameOriginOnlyCheckbox = panel.querySelector('#same-origin-only');

  // config per your choices
  const MAX_DEPTH = 3;
  const CONCURRENCY = 5; // user requested
  // Whitelist extensions to *scan* (only these considered by ext-only mode)
  const SCAN_EXTENSIONS = new Set(['.html', '.htm', '.js', '.json', '.xml']);
  // Whitelist MIME types considered text for smart mode
  const TEXT_MIME = new Set(['text/html', 'application/javascript', 'application/x-javascript', 'text/javascript', 'application/json', 'application/xml', 'text/xml']);

  // preserve excludedHosts from v3 (still good to exclude known CDNs)
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
    // jsdelivr & githack intentionally not excluded
  ];

  function hostExcluded(host){
    try{ return excludedHosts.some(r=>r.test(host)); }catch(e){ return false; }
  }

  // detectors (extend v3 with misconfig patterns)
  const DET = {
    firebaseApiKey: /AIza[0-9A-Za-z\-_]{35}/g,
    firebaseDB: /(https?:\/\/[A-Za-z0-9\-]+(?:\.firebaseio\.com|\.firebasedatabase\.app))(?:[:\/\w\-\.\?\=\&]*)/gi,
    firebaseProjectId: /["'\s]projectId["']?\s*[:=]\s*["']?([a-z0-9\-]{6,})["']?/gi,
    firebaseStorage: /["'\s]storageBucket["']?\s*[:=]\s*["']?([a-z0-9\-\.]+(?:appspot\.com|storage\.googleapis\.com)?)["']?/gi,
    googleClientId: /[0-9]{1,}-[0-9A-Za-z_]+\.apps\.googleusercontent\.com/g,
    awsKey: /\b(A3T|AKIA|ASIA)[A-Z0-9]{16}\b/g,
    longHex: /(?:key|token|secret|auth|session|hash)[\s'"]{0,8}[:=]\s*['"]?([0-9a-fA-F]{32,})['"]?/gi,
    pwdParam: /(?:username|user|email|password|pwd|pass|secret|token|api[_-]?key|apikey|access[_-]?token|client_secret|private_key)\s*(?:=|:)\s*['"]?([^\s'";,<>]{4,200})/gi,
    urlWithPort: /https?:\/\/[^\s'"]+:\d{2,5}[^\s'"]*/gi,
    dbConn: /(mongodb(?:\+srv)?:\/\/[^\s'"]+|postgres(?:ql)?:\/\/[^\s'"]+|mysql:\/\/[^\s'"]+|redis:\/\/[^\s'"]+)/gi,
    smtpUrl: /(smtp:\/\/[^\s'"]+|smtp:[^\s'"]+|smtp\.[a-z0-9\.-]+\.[a-z]{2,})/gi,
    appKey: /(?:app[_-]?key|application[_-]?key|client[_-]?id|client[_-]?secret)\s*(?:=|:)\s*['"]?([A-Za-z0-9\-_]{6,200})/gi,
    emailLike: /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g,
    apiKeyNear: /(?:(?:api[_-]?key|x-?api-?key|apikey|client[_-]?id|client[_-]?secret|authorization)\s*[:=]\s*['"]?([A-Za-z0-9\-_]{10,})['"]?)/gi,
    localhost: /\b(?:localhost|127\.0\.0\.1|::1)\b/g,
    commonDbUser: /\b(?:root|admin|postgres|sa|mongo|sysadmin)\b/gi,
    base64Long: /\b[A-Za-z0-9\+\/]{40,}={0,2}\b/g,
    jwtLike: /([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)/g,
    // misconfiguration hints (filenames & common leaks)
    gitConfigPath: /(?:\.git\/HEAD|\.git\/config|\.gitignore)/i,
    envFilename: /(^|\/)(?:\.env|env\.local|env\.development|.env\.production)(?:$|\/|\?)/i,
    htpasswd: /(^|\/)(?:\.htpasswd|htpasswd)(?:$|\/|\?)/i,
    configFileNames: /(composer\.json|package\.json|web\.config|appsettings\.json|.env)/i
  };

  // result stores and caches
  const seen = new Set(); // absolute urls processed or queued
  const found = new Map(); // absUrl -> metadata
  const fetchCache = new Map(); // cache text or null
  const fetchErrors = new Map(); // absUrl -> [errors]
  const skipped = new Set();

  // helpers
  function isLocal(u){
    try{ const url = new URL(u, location.href); return url.origin === location.origin && !hostExcluded(url.host); }catch(e){ return false; }
  }

  function urlHasWhitelistExt(u){
    try{
      const pathname = new URL(u, location.href).pathname.toLowerCase();
      const lastDot = pathname.lastIndexOf('.');
      if(lastDot === -1) return false;
      const ext = pathname.substring(lastDot);
      return SCAN_EXTENSIONS.has(ext);
    }catch(e){
      return false;
    }
  }

  // decide whether to fetch a resource (HEAD/MIME or ext-only)
  async function shouldFetchResource(url, mode, preferSameOrigin){
    // preferSameOrigin = if true, skip cross-origin
    try{
      const parsed = new URL(url, location.href);
      if(preferSameOrigin && parsed.origin !== location.origin) return false;
      if(hostExcluded(parsed.host)) return false;
      // ext-only mode -> only fetch if extension in whitelist
      if(mode === 'ext-only'){
        return urlHasWhitelistExt(url);
      }
      // smart mode: if we already cached, reuse
      const abs = parsed.href;
      if(fetchCache.has(abs)) return !!fetchCache.get(abs);
      // For smart mode, try quick HEAD for same-origin OR attempt to use content-type from server
      if(parsed.origin === location.origin){
        try{
          const r = await fetch(abs, { method: 'HEAD', credentials: 'same-origin', signal: AbortSignal.timeout(2000) });
          const c = r.headers.get('content-type') || '';
          const mime = c.split(';')[0].toLowerCase();
          if(mime && TEXT_MIME.has(mime)) return true;
          // not a text mime
          return false;
        }catch(e){
          // If HEAD fails, fallback to trying to GET (but keep cautious)
          // We'll allow fetchTextQuiet to attempt GET; here return true to let it try
          registerFetchError(abs, String(e && e.message ? e.message : e));
          return true;
        }
      } else {
        // cross-origin: we cannot reliably HEAD due to CORS. Avoid fetching cross-origin bodies.
        return false;
      }
    }catch(e){
      return false;
    }
  }

  function registerFetchError(url, msg){
    try{
      const abs = new URL(url, location.href).href;
      if(!fetchErrors.has(abs)) fetchErrors.set(abs, []);
      fetchErrors.get(abs).push(msg);
    }catch(e){}
  }

  // fetch with caching (only for same-origin or permitted)
  async function fetchTextQuiet(url){
    let abs;
    try{ abs = new URL(url, location.href).href; }catch(e){ return null; }
    if(fetchCache.has(abs)) return fetchCache.get(abs);

    // only fetch same-origin by design
    try{
      const parsed = new URL(abs);
      if(parsed.origin !== location.origin){
        fetchCache.set(abs, null);
        skipped.add(abs);
        incSkipped();
        return null;
      }
    }catch(e){}

    try{
      const r = await fetch(abs, { credentials: 'same-origin', signal: AbortSignal.timeout(5000) });
      if(!r.ok){
        registerFetchError(abs, `HTTP_${r.status}`);
        fetchCache.set(abs, null);
        return null;
      }
      // check content-type to ensure it's text/json/js/xml/html
      const ctype = (r.headers.get('content-type') || '').split(';')[0].toLowerCase();
      if(ctype && !Array.from(TEXT_MIME).some(m => ctype.includes(m))) {
        // not in allowed text types
        fetchCache.set(abs, null);
        skipped.add(abs);
        incSkipped();
        return null;
      }
      const txt = await r.text();
      fetchCache.set(abs, txt);
      return txt;
    }catch(e){
      registerFetchError(abs, String(e && e.message ? e.message : e));
      fetchCache.set(abs, null);
      return null;
    }
  }

  // detectors & heuristics (similar to v3, with misconfig detection)
  function contextHasKeywords(text, index, keywords, radius=60){
    if(!text) return false;
    const start = Math.max(0, index - radius);
    const end = Math.min(text.length, index + radius);
    const snippet = text.slice(start, end).toLowerCase();
    for(const k of keywords){
      if(snippet.includes(k)) return true;
    }
    return false;
  }

  function scanSensitive(text){
    if(!text) return [];
    const res = [];
    for(const m of text.matchAll(DET.firebaseApiKey) || []) res.push({type:'firebase_api_key', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.firebaseDB) || []) res.push({type:'firebase_database_url', value:m[1], contextIndex: m.index});
    for(const m of text.matchAll(DET.firebaseProjectId) || []) res.push({type:'firebase_project_id', value:m[1], contextIndex: m.index});
    for(const m of text.matchAll(DET.firebaseStorage) || []) res.push({type:'firebase_storage_bucket', value:m[1], contextIndex: m.index});
    for(const m of text.matchAll(DET.googleClientId) || []) res.push({type:'google_client_id', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.awsKey) || []) res.push({type:'aws_key', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.longHex) || []) res.push({type:'long_hex', value:m[1] || m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.pwdParam) || []) { if(m[1] && m[1].length>0) res.push({type:'credential_like', value:m[1], contextIndex: m.index}); }
    for(const m of text.matchAll(DET.urlWithPort) || []) res.push({type:'url_with_port', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.dbConn) || []) res.push({type:'database_conn', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.smtpUrl) || []) res.push({type:'smtp_hint', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.appKey) || []) { if(m[1] && m[1].length>0) res.push({type:'app_key', value:m[1], contextIndex: m.index}); }
    for(const m of text.matchAll(DET.emailLike) || []) res.push({type:'email', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.apiKeyNear) || []) res.push({type:'api_key_like', value:m[1], contextIndex: m.index});
    for(const m of text.matchAll(DET.localhost) || []) res.push({type:'local_host_hint', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.commonDbUser) || []) res.push({type:'common_db_user_hint', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.base64Long) || []) res.push({type:'base64_long', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.jwtLike) || []) res.push({type:'jwt_like', value:m[1] || m[0], contextIndex: m.index});

    // misconfiguration file hints (if contents include .env or .git paths or config file names)
    for(const m of text.matchAll(/(?:\.env|DB_PASSWORD|DATABASE_URL|GITHUB_TOKEN|PRIVATE_KEY|BEGIN RSA PRIVATE KEY)/gi) || []) {
      res.push({type:'possible_leak', value:m[0], contextIndex: m.index});
    }
    for(const m of text.matchAll(DET.gitConfigPath) || []) res.push({type:'git_exposed', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.envFilename) || []) res.push({type:'env_filename', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.htpasswd) || []) res.push({type:'htpasswd', value:m[0], contextIndex: m.index});
    for(const m of text.matchAll(DET.configFileNames) || []) res.push({type:'config_file_hint', value:m[0], contextIndex: m.index});

    // dedupe + context heuristics
    const uniq = [], seenv = new Set();
    for(const it of res){
      const key = it.type + '|' + it.value;
      if(seenv.has(key)) continue;
      let keep = true;
      if(it.type === 'long_hex' || it.type === 'base64_long' || it.type === 'jwt_like'){
        keep = contextHasKeywords(text, it.contextIndex || 0, ['key','token','secret','auth','password','api','client','bearer','jwt','session','access','private','db','database','passwd','pass']);
      }
      if(it.type === 'email'){
        const near = contextHasKeywords(text, it.contextIndex || 0, ['user','email','password','db','database','login','account']);
        if(!near){
          const emails = (text.match(DET.emailLike) || []).length;
          if(emails > 10) keep = false;
        }
      }
      if(keep){
        seenv.add(key);
        uniq.push(it);
      }
    }
    return uniq;
  }

  // extract candidate urls/paths from text (same as v3, but keep external endpoints recorded)
  function extractCandidatesFromText(text){
    if(!text) return [];
    const s = new Set();
    const re1 = /['"]((?:https?:\/\/|\/\/|\/|\.\.\/|\.\/)[^'"]{1,800})['"]/g;
    for(const m of text.matchAll(re1)) s.add(m[1]);
    const re2 = /`([^`]{1,800})`/g;
    for(const m of text.matchAll(re2)) s.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    const ajaxRe = /(?:fetch|axios\.(?:get|post|put|delete|patch)|open|XMLHttpRequest|new\s+Request)\s*\(\s*['"`]((?:https?:\/\/|\/|\.\.\/|\.\/)[^'"`]{1,800})['"`]/g;
    for(const m of text.matchAll(ajaxRe)) s.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    const pathRe = /['"]((?:\/[a-zA-Z0-9_\-\/\.]{3,200}api[\/a-zA-Z0-9_\-\.]*)['"])/g;
    for(const m of text.matchAll(pathRe)) s.add(m[1]);
    // also capture direct references to .env, .git paths, config files
    const miscRe = /['"]((?:\/|\.\/)?(?:\.env|\.git\/config|\.git\/HEAD|\.htpasswd|appsettings\.json|web\.config|.env\.local)[^'"]*)['"]/g;
    for(const m of text.matchAll(miscRe)) s.add(m[1]);
    return Array.from(s);
  }

  // progress counters
  let totalResources = 0;
  let processedResources = 0;
  let skippedResources = 0;
  let stopRequested = false;

  function setProgress(percent){
    scanProgressBar.style.width = percent + '%';
    scanStatus.textContent = `Scanning... ${percent}%`;
    scanInfo.textContent = `Scanned ${processedResources}/${totalResources} — Skipped ${skippedResources}`;
  }

  function incProgress(){
    processedResources++;
    const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100;
    setProgress(pct);
  }

  function incSkipped(){
    skippedResources++;
    processedResources++;
    const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100;
    setProgress(pct);
  }

  // concurrency pLimit
  function pLimit(concurrency){
    const queue = [];
    let active = 0;
    const next = () => {
      if(queue.length === 0) return;
      if(active >= concurrency) return;
      active++;
      const item = queue.shift();
      const fn = item.fn;
      fn().then((v)=>{ active--; item.resolve(v); next(); }).catch(()=>{ active--; item.resolve(); next(); });
    };
    return (fn) => new Promise(res => { queue.push({fn, resolve:res}); next(); });
  }
  const limit = pLimit(CONCURRENCY);

  function addFound(url, source='detected'){
    try{
      const abs = new URL(url, location.href).href;
      if(!found.has(abs)){
        found.set(abs, { params: new Set(), sensitive: [], source, local: isLocal(abs), apiLike: isApiLike(abs), misconfig: [], fetchErrors: fetchErrors.get(abs) || [] });
      } else {
        const meta = found.get(abs);
        const errs = fetchErrors.get(abs);
        if(errs){
          meta.fetchErrors = Array.from(new Set([...(meta.fetchErrors||[]), ...errs]));
        }
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

  // improved isApiLike (from v3)
  function isApiLike(u){
    try{
      const url = new URL(u, location.href);
      const path = (url.pathname || '').toLowerCase();
      if(path.includes('/api/') || path.includes('/graphql') || /\/v\d+(\.|\/)/.test(path) || path.includes('/_next/data/')) return true;
      if(url.host.startsWith('api.') || url.pathname.match(/\/(api|graphql|services|rest|v\d+)\b/)) return true;
      return false;
    }catch(e){
      if(/\/api\//i.test(u) || /graphql/i.test(u) || /_next\/data/i.test(u) || /\/v\d+\//i.test(u)) return true;
      if(/apikey|api[_-]?key|x-?api-?key|authorization\s*[:=]\s*bearer/i.test(u)) return true;
      return false;
    }
  }

  // determine if item is sensitive
  function isSensitiveItem(meta){
    if(!meta) return false;
    if((meta.sensitive && meta.sensitive.length>0)) return true;
    if(meta.misconfig && meta.misconfig.length>0) return true;
    return false;
  }

  // main recursive processor
  async function process(url, depth=0, source='root', mode='smart', preferSameOrigin=true){
    if(stopRequested) return;
    if(depth > MAX_DEPTH) return;
    let abs;
    try{ abs = new URL(url, location.href).href; }catch(e){ return; }
    if(seen.has(abs)) return;
    seen.add(abs);

    // Check extension whitelist skipping - updated logic: if ext exists but not whitelisted, skip
    try{
      const uobj = new URL(abs);
      const path = uobj.pathname.toLowerCase();
      const lastDot = path.lastIndexOf('.');
      if(lastDot > -1){
        const ext = path.substring(lastDot);
        if(!SCAN_EXTENSIONS.has(ext)){
          skipped.add(abs);
          incSkipped();
          return;
        }
      } else {
        // no extension: in smart mode we rely on shouldFetchResource to decide via MIME
        // in ext-only mode skip resources without extension
        if(mode === 'ext-only'){
          skipped.add(abs);
          incSkipped();
          return;
        }
      }
    }catch(e){}

    addFound(abs, source);
    const params = extractParams(abs);
    for(const p of params) found.get(abs).params.add(p);

    // Only fetch same-origin bodies
    const local = isLocal(abs);
    if(!local){
      // record existence but do not fetch body
      incProgress();
      return;
    }

    // cached?
    if(fetchCache.has(abs)){
      const cachedText = fetchCache.get(abs);
      incProgress();
      if(cachedText){
        if(detectKeysCheckbox.checked){
          const sensitive = scanSensitive(cachedText);
          for(const s of sensitive){
            const idx = s.contextIndex || 0;
            const start = Math.max(0, idx - 40);
            const snippet = cachedText.slice(start, Math.min(cachedText.length, idx + 40)).replace(/\s+/g,' ');
            found.get(abs).sensitive.push(Object.assign({}, s, {context: snippet}));
          }
        }
        const cands = extractCandidatesFromText(cachedText);
        for(const c of cands){
          try{
            const resolved = new URL(c, abs).href;
            // For candidate resolution: if candidate is external, record but don't deep-scan
            addFound(resolved, abs);
            const ps = extractParams(c);
            for(const p of ps) found.get(resolved).params.add(p);
            if(isLocal(resolved) || isApiLike(c) || isApiLike(resolved)){
              await limit(()=>process(resolved, depth+1, abs, mode, preferSameOrigin));
            }
          }catch(e){}
        }
      }
      return;
    }

    // Additional check before fetching
    const shouldFetch = await shouldFetchResource(abs, mode, preferSameOrigin);
    if(!shouldFetch){
      skipped.add(abs);
      incSkipped();
      fetchCache.set(abs, null);
      return;
    }

    // fetch body
    const text = await fetchTextQuiet(abs);
    incProgress();
    if(fetchErrors.has(abs)){
      const meta = found.get(abs);
      meta.fetchErrors = Array.from(new Set([...(meta.fetchErrors||[]), ...fetchErrors.get(abs)]));
    }
    if(!text) return;

    // scanning for sensitive & misconfig
    if(detectKeysCheckbox.checked){
      const sensitive = scanSensitive(text);
      for(const s of sensitive){
        const idx = s.contextIndex || 0;
        const start = Math.max(0, idx - 40);
        const snippet = text.slice(start, Math.min(text.length, idx + 40)).replace(/\s+/g,' ');
        // misconfig types mapped to misconfig array
        if(['git_exposed','env_filename','htpasswd','config_file_hint','possible_leak'].includes(s.type)){
          found.get(abs).misconfig.push(Object.assign({}, s, {context: snippet}));
        } else {
          found.get(abs).sensitive.push(Object.assign({}, s, {context: snippet}));
          if(s.type && s.type.startsWith('firebase')) found.get(abs).firebaseMeta = found.get(abs).firebaseMeta || {};
          if(s.type && s.type.startsWith('firebase')) found.get(abs).firebaseMeta[s.type] = s.value;
        }
      }
    }

    // extract candidates from this text
    const cands = extractCandidatesFromText(text);
    for(const c of cands){
      try{
        const resolved = new URL(c, abs).href;
        // if resolved external (cross-origin), just record it (fuzzing-external category) but don't deep-scan
        addFound(resolved, abs);
        const ps = extractParams(c);
        for(const p of ps) found.get(resolved).params.add(p);
        if(isLocal(resolved) || isApiLike(c) || isApiLike(resolved)){
          // process recursively but only for local or api-like (local)
          await limit(()=>process(resolved, depth+1, abs, mode, preferSameOrigin));
        }
      }catch(e){}
    }
  }

  // gather initial resources (but do NOT include inline scripts per user instruction)
  function gatherInitialResources(mode, preferSameOrigin){
    const resources = new Set();
    try{
      performance.getEntriesByType('resource')
        .map(r=>r.name)
        .forEach(u=>resources.add(u));
    }catch(e){}
    // gather external script[src] but we will decide to fetch later based on mode
    document.querySelectorAll('script[src]').forEach(s => resources.add(s.src));
    // gather link hrefs (manifest, json, etc.)
    document.querySelectorAll('link[href]').forEach(l => resources.add(l.href));
    // gather anchors & forms as candidate endpoints
    document.querySelectorAll('a[href]').forEach(a => resources.add(a.href));
    document.querySelectorAll('form[action]').forEach(f => resources.add(f.action));
    // gather inline HTML content references (like JSON blocks in the page)
    try{
      extractCandidatesFromText(document.documentElement.outerHTML||document.body.innerHTML)
        .forEach(p=>resources.add(p));
    }catch(e){}
    return Array.from(resources);
  }

  // main entrypoint triggered by Start button
  async function startScan(){
    stopRequested = false;
    // reset counters and stores
    totalResources = 0;
    processedResources = 0;
    skippedResources = 0;
    seen.clear();
    found.clear();
    fetchCache.clear();
    fetchErrors.clear();
    skipped.clear();
    fetchCache.clear();

    resultsDiv.innerHTML = `<div style="color:#666">Scanning... please wait.</div>`;
    const mode = modeSelect.value; // 'smart' or 'ext-only'
    const preferSameOrigin = !!sameOriginOnlyCheckbox.checked;

    // gather resources
    const initial = gatherInitialResources(mode, preferSameOrigin).filter(u => !!u);
    // dedupe and normalize
    const uniqueResources = Array.from(new Set(initial.map(u => { try { return new URL(u, location.href).href } catch(e){ return u } })));
    totalResources = uniqueResources.length || 1;
    processedResources = 0;
    skippedResources = 0;
    setProgress(0);
    scanStatus.textContent = `Scanning... 0%`;

    // build tasks
    const tasks = [];
    for(const r of uniqueResources){
      // limit execution concurrency
      tasks.push(limit(()=>process(r, 0, 'resource', mode, preferSameOrigin)));
    }

    // await tasks
    await Promise.all(tasks);
    // finished
    setProgress(100);
    scanStatus.textContent = `Scan complete - Found ${found.size} endpoints`;
    scanInfo.textContent = `Scanned ${processedResources} resources — Skipped ${skippedResources}`;
    // hide progress bar (per user: progress bar disappears after finished and results appear)
    setTimeout(()=>{ scanProgressBar.style.width = '0%'; scanProgressBar.parentElement.style.visibility = 'hidden'; }, 400);
    // render results
    render();
  }

  // stop scanning gracefully
  function stopScan(){
    stopRequested = true;
    scanStatus.textContent = 'Stopping...';
  }

  // rendering similar to v3
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
        misconfig: meta.misconfig ? meta.misconfig.slice() : [],
        source: meta.source,
        local: meta.local,
        apiLike: meta.apiLike,
        firebaseMeta: Object.assign({}, meta.firebaseMeta || {}),
        fetchErrors: meta.fetchErrors || []
      });
    }
    const f = filterSelect.value;
    let filtered = list;
    if(f === 'api') filtered = list.filter(i=>i.apiLike && !isSensitiveItem(i));
    if(f === 'fuzzing') filtered = list.filter(i=>i.local && isParamBearing(i.url) && !isSensitiveItem(i));
    if(f === 'fuzzing-external') filtered = list.filter(i=>!i.local && isParamBearing(i.url) && !hostExcluded((() => { try { return new URL(i.url).host } catch(e){ return '' } })()));
    if(f === 'sensitive') filtered = list.filter(i=>isSensitiveItem(i));
    filtered.sort((a,b) => (isSensitiveItem(b)?1:0) - (isSensitiveItem(a)?1:0) || ((b.apiLike|0) - (a.apiLike|0)));
    return filtered;
  }

  function render(){
    const rows = buildList();
    if(rows.length === 0){ resultsDiv.innerHTML = `<div style="color:#666">No endpoints found.</div>`; return; }
    const html = rows.map(it => {
      const sensHtml = (it.sensitive && it.sensitive.length>0) ? `<div style="margin-top:6px;color:#900;font-weight:600">⚠ Sensitive (${it.sensitive.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.sensitive.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code title="${escapeHtml(s.context||'')}">${escapeHtml(redact(s.value))}</code>${s.context?` <span style="color:#666;font-size:11px">…${escapeHtml(redact(s.context))}</span>`:''}</li>`).join('')}</ul>` : '';
      const misHtml = (it.misconfig && it.misconfig.length>0) ? `<div style="margin-top:6px;color:#b56500;font-weight:600">⚠ Misconfiguration (${it.misconfig.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.misconfig.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code title="${escapeHtml(s.context||'')}">${escapeHtml(redact(s.value))}</code>${s.context?` <span style="color:#666;font-size:11px">…${escapeHtml(redact(s.context))}</span>`:''}</li>`).join('')}</ul>` : '';
      const fbHtml = (it.firebaseMeta && Object.keys(it.firebaseMeta).length>0) ? `<div style="margin-top:6px;color:#0366d6"><strong>Firebase hints:</strong> ${Object.entries(it.firebaseMeta).map(([k,v])=>`${escapeHtml(k)}=${escapeHtml(redact(v))}`).join(', ')}</div>` : '';
      const fetchErrHtml = (it.fetchErrors && it.fetchErrors.length>0) ? `<div style="margin-top:6px;color:#999;font-size:11px">Fetch issues: ${escapeHtml(it.fetchErrors.join('; '))}</div>` : '';
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
        ${misHtml}
        ${fbHtml}
        ${fetchErrHtml}
      </div>`;
    }).join('');
    resultsDiv.innerHTML = html;
  }

  function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

  // event handlers
  startBtn.onclick = async ()=>{
    // UI adjustments
    scanProgressBar.parentElement.style.visibility = 'visible';
    scanProgressBar.style.width = '0%';
    scanStatus.textContent = 'Initializing...';
    // start
    await startScan();
  };

  stopBtn.onclick = ()=>{
    stopScan();
  };

  filterSelect.onchange = ()=> render();
  detectKeysCheckbox.onchange = ()=> render();

  // copy action (like v3)
  panel.querySelector('#copy-all').onclick = async ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw){
      if(!confirm('You have selected to include raw secrets. This will copy sensitive data to your clipboard. Proceed?')) return;
    }
    const lines = [];
    for(const r of rows){
      const sens = r.sensitive.map(s=> includeRaw ? `${s.type}:${s.value}` : `${s.type}:[REDACTED]`).join('; ');
      const mis = r.misconfig.map(s=> includeRaw ? `${s.type}:${s.value}` : `${s.type}:[REDACTED]`).join('; ');
      const errs = (r.fetchErrors && r.fetchErrors.length) ? ` | fetchErrors: ${r.fetchErrors.join(';')}` : '';
      const extras = [];
      if(mis) extras.push(`misconfig: ${mis}`);
      lines.push(`${r.url}${r.params.length?` | params: ${r.params.join(',')}`:''}${sens?` | sensitive: ${sens}`:''}${extras.length?` | ${extras.join(' | ')}`:''}${errs}`);
    }
    const out = lines.join('\n');
    try{ await navigator.clipboard.writeText(out); alert(`Copied ${rows.length} items`); }catch(e){ const ta=document.createElement('textarea'); ta.value=out; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); alert('Copied (fallback)'); }
  };

  // export .txt
  panel.querySelector('#export-txt').onclick = ()=>{
    const f = filterSelect.value;
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw){
      if(!confirm('You have selected to include raw secrets in the export file. This will write sensitive data to disk. Proceed?')) return;
    }
    const lines = [];

    function pushItem(r){
      lines.push(`URL: ${r.url}`);
      if(r.params.length) lines.push(`Params: ${r.params.join(', ')}`);
      if(r.sensitive.length){
        lines.push('Sensitive:');
        for(const s of r.sensitive) lines.push(`  - ${s.type}: ${ includeRaw ? s.value : '[REDACTED]' } ${s.context?` (context: ${s.context})`:''}`);
      }
      if(r.misconfig.length){
        lines.push('Misconfiguration:');
        for(const s of r.misconfig) lines.push(`  - ${s.type}: ${ includeRaw ? s.value : '[REDACTED]' } ${s.context?` (context: ${s.context})`:''}`);
      }
      if(Object.keys(r.firebaseMeta||{}).length){
        lines.push('Firebase hints:');
        for(const [k,v] of Object.entries(r.firebaseMeta)) lines.push(`  - ${k}: ${ includeRaw ? v : '[REDACTED]' }`);
      }
      if(r.fetchErrors && r.fetchErrors.length) lines.push(`Fetch issues: ${r.fetchErrors.join('; ')}`);
      lines.push('');
    }

    if(f === 'all'){
      const groups = { FUZZING_LOCAL:[], FUZZING_EXTERNAL:[], API:[], SENSITIVE:[], MISCONFIG:[], ALL:[] };
      for(const r of rows){
        if(r.misconfig && r.misconfig.length) groups.MISCONFIG.push(r);
        else if(isSensitiveItem(r)) groups.SENSITIVE.push(r);
        else if(isParamBearing(r.url) && r.local) groups.FUZZING_LOCAL.push(r);
        else if(isParamBearing(r.url) && !r.local) groups.FUZZING_EXTERNAL.push(r);
        else if(r.apiLike) groups.API.push(r);
        else groups.ALL.push(r);
      }
      if(groups.FUZZING_LOCAL.length){ lines.push('=== FUZZING (LOCAL) ===',''); groups.FUZZING_LOCAL.forEach(pushItem); lines.push(''); }
      if(groups.FUZZING_EXTERNAL.length){ lines.push('=== FUZZING (EXTERNAL) ===',''); groups.FUZZING_EXTERNAL.forEach(pushItem); lines.push(''); }
      if(groups.API.length){ lines.push('=== API ===',''); groups.API.forEach(pushItem); lines.push(''); }
      if(groups.SENSITIVE.length){ lines.push('=== SENSITIVE INFORMATION ===',''); groups.SENSITIVE.forEach(pushItem); lines.push(''); }
      if(groups.MISCONFIG.length){ lines.push('=== MISCONFIGURATION ===',''); groups.MISCONFIG.forEach(pushItem); lines.push(''); }
      if(groups.ALL.length){ lines.push('=== ALL (OTHER) ===',''); groups.ALL.forEach(pushItem); lines.push(''); }
    } else {
      for(const r of rows) pushItem(r);
    }

    const blob = new Blob([lines.join('\n')], {type:'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'endpoints-v4.txt'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  // export JSON (manual)
  panel.querySelector('#export-json').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw){
      if(!confirm('You have selected to include raw secrets in the export file. This will write sensitive data to disk. Proceed?')) return;
    }
    const out = rows.map(r => ({
      url: r.url,
      params: r.params,
      sensitive: r.sensitive.map(s => includeRaw ? s : ({ type: s.type, value: '[REDACTED]', context: s.context })),
      misconfig: r.misconfig.map(s => includeRaw ? s : ({ type: s.type, value: '[REDACTED]', context: s.context })),
      source: r.source,
      local: r.local,
      apiLike: r.apiLike,
      firebaseMeta: r.firebaseMeta,
      fetchErrors: r.fetchErrors
    }));
    const blob = new Blob([JSON.stringify(out, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'result-v4.json'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  panel.querySelector('#close-panel').onclick = ()=> panel.remove();

  // util: param-bearing detection (same as v3)
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

  // initial render (empty)
  resultsDiv.innerHTML = `<div style="color:#666">Ready. Choose mode and press Start.</div>`;

  // ensure progress bar initially visible but 0
  scanProgressBar.parentElement.style.visibility = 'visible';
  scanProgressBar.style.width = '0%';

  // end of main IIFE
})();
