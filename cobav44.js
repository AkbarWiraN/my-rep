// silent-scanner-v4-full.js
// Silent Scanner v4 - focused on .html, .js, .json, .xml
// - Whitelist extension: .html, .js, .json, .xml
// - Fetch only same-host bodies; external resources are recorded but not fetched
// - Modes: smart (MIME-aware permissive), ext-only (strict ext), aggressive (force-fetch whitelisted ext)
// - Concurrency: 5, MAX_DEPTH: 3, caching of fetched URLs to avoid recheck
// - Categories: All, API, Fuzzing local, Fuzzing external, Sensitive information, Misconfig
// - Export JSON manual, progress overlay, copy/export text

(async function(){
  // ---------------- UI ----------------
  const panel = document.createElement('div');
  Object.assign(panel.style, {
    position: 'fixed',
    right: '12px',
    bottom: '12px',
    width: '560px',
    maxHeight: '80vh',
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
    <strong style="font-size:14px">Silent Scanner v4 (final)</strong>
    <div style="display:flex;gap:6px;align-items:center">
      <select id="scan-filter" title="Filter" style="padding:4px;">
        <option value="all">All</option>
        <option value="api">API</option>
        <option value="fuzzing">Fuzzing local</option>
        <option value="fuzzing-external">Fuzzing external</option>
        <option value="sensitive">Sensitive information</option>
        <option value="misconfig">Misconfiguration</option>
      </select>
      <label style="font-size:12px"><input id="detect-keys" type="checkbox" checked style="vertical-align:middle"> Detect</label>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
    <div style="display:flex;gap:6px;align-items:center">
      <label style="font-size:12px">Mode:</label>
      <select id="scan-mode" style="padding:4px;">
        <option value="smart">Smart (MIME-aware)</option>
        <option value="ext-only">Ext-only</option>
        <option value="aggressive">Aggressive</option>
      </select>
      <label style="font-size:12px"><input id="same-host-only" type="checkbox" checked style="vertical-align:middle"> Same-host only</label>
    </div>
    <div style="margin-left:auto;display:flex;gap:6px">
      <button id="start-scan" style="padding:6px 10px;background:#0366d6;color:#fff;border:none;border-radius:5px">Start</button>
      <button id="stop-scan" style="padding:6px 10px;background:#eee;border:1px solid #ccc;border-radius:5px">Stop</button>
    </div>
  </div>

  <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">
    <div id="scan-status" style="font-size:12px;color:#666">Ready</div>
    <div style="flex:1;background:#f1f1f1;height:10px;border-radius:6px;overflow:hidden;margin-left:8px">
      <div id="scan-progress" style="height:10px;width:0%;background:#0366d6;transition:width 120ms linear"></div>
    </div>
  </div>

  <div id="results" style="max-height:60vh;overflow:auto;border-top:1px solid #eee;padding-top:8px"></div>

  <div style="display:flex;gap:8px;justify-content:flex-end;margin-top:8px;flex-wrap:wrap">
    <div style="font-size:11px;color:#666;margin-right:auto" id="scan-info">Whitelist ext: .html .js .json .xml — only fetch same-host; external listed only.</div>
    <label style="font-size:12px"><input id="include-raw" type="checkbox"> Include raw secrets</label>
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
  const sameHostOnlyCheckbox = panel.querySelector('#same-host-only');

  // ---------------- Config ----------------
  const MAX_DEPTH = 3;
  const CONCURRENCY = 5;
  const SCAN_EXTENSIONS = new Set(['.html', '.htm', '.js', '.json', '.xml']);
  const TEXT_MIME = new Set(['text/html','application/javascript','application/x-javascript','text/javascript','application/json','application/xml','text/xml','application/ld+json']);
  // exclude common external hosts from deep scanning (still listed)
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
  ];
  function hostExcluded(host){ try{ return excludedHosts.some(r=>r.test(host)); }catch(e){ return false; } }

  // ---------------- Detectors ----------------
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
    base64Long: /\b[A-Za-z0-9\+\/]{40,}={0,2}\b/g,
    jwtLike: /([A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+)/g,
    gitPath: /(?:\.git\/HEAD|\.git\/config|\.gitignore)/i,
    envFile: /(^|\/)(?:\.env|env\.local|env\.development|\.env\.production)(?:$|\/|\?)/i,
    htpasswd: /(^|\/)(?:\.htpasswd|htpasswd)(?:$|\/|\?)/i,
    configHints: /(composer\.json|package\.json|web\.config|appsettings\.json|\.env)/i
  };

  // ---------------- Stores ----------------
  const seen = new Set(); // URLs already processed (abs href)
  const found = new Map(); // absHref -> meta
  const fetchCache = new Map(); // absHref -> text|null
  const fetchErrors = new Map(); // absHref -> [errors]
  const skipped = new Set(); // skipped resources
  let stopRequested = false;

  // ---------------- Helpers ----------------
  function isSameHost(u){
    try{ const url = new URL(u, location.href); return url.host === location.host && !hostExcluded(url.host); }catch(e){ return false; }
  }
  function urlHasWhitelistExt(u){
    try{ const p = new URL(u, location.href).pathname.toLowerCase(); const idx = p.lastIndexOf('.'); if(idx===-1) return false; return SCAN_EXTENSIONS.has(p.substring(idx)); }catch(e){ return false; }
  }
  function registerFetchError(url, msg){
    try{ const abs = new URL(url, location.href).href; if(!fetchErrors.has(abs)) fetchErrors.set(abs, []); fetchErrors.get(abs).push(msg); }catch(e){}
  }
  function addFound(url, source='detected'){
    try{
      const abs = new URL(url, location.href).href;
      if(!found.has(abs)){
        found.set(abs, {
          params: new Set(),
          sensitive: [],
          misconfig: [],
          source,
          local: isSameHost(abs),
          apiLike: isApiLike(abs),
          firebaseMeta: {},
          fetchErrors: []
        });
      } else {
        const meta = found.get(abs);
        const errs = fetchErrors.get(abs);
        if(errs) meta.fetchErrors = Array.from(new Set([...(meta.fetchErrors||[]), ...errs]));
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
  function isApiLike(u){
    try{
      const url = new URL(u, location.href);
      const path = (url.pathname||'').toLowerCase();
      if(path.includes('/api/') || path.includes('/graphql') || /\/v\d+(\.|\/)/.test(path) || path.includes('/_next/data/')) return true;
      if(url.host.startsWith('api.') || url.pathname.match(/\/(api|graphql|services|rest|v\d+)\b/)) return true;
      return false;
    }catch(e){
      if(/\/api\//i.test(u) || /graphql/i.test(u) || /_next\/data/i.test(u)) return true;
      if(/apikey|api[_-]?key|authorization\s*[:=]\s*bearer/i.test(u)) return true;
      return false;
    }
  }

  // ---------------- Fetch policy ----------------
  // mode: 'ext-only' | 'smart' | 'aggressive'
  async function shouldFetchResource(url, mode, preferSameHost){
    try{
      const parsed = new URL(url, location.href);
      // preferSameHost means only fetch if same host
      if(preferSameHost && parsed.host !== location.host) return false;
      // if host excluded, do not fetch
      if(hostExcluded(parsed.host)) return false;

      // ext-only mode: require whitelist extension
      if(mode === 'ext-only') return urlHasWhitelistExt(url) && parsed.host === location.host;

      // aggressive: fetch any same-host resource with whitelist ext
      if(mode === 'aggressive'){
        if(parsed.host !== location.host) return false;
        const p = parsed.pathname.toLowerCase();
        if(p.endsWith('.js')||p.endsWith('.json')||p.endsWith('.xml')||p.endsWith('.html')||p.endsWith('.htm')) return true;
        return false;
      }

      // smart mode: HEAD check same-host
      if(parsed.host === location.host){
        try{
          const r = await fetch(parsed.href, { method: 'HEAD', credentials: 'same-origin', signal: AbortSignal.timeout(2500) });
          const ct = r.headers.get('content-type') || '';
          const mime = ct.split(';')[0].toLowerCase();
          if(!mime) return urlHasWhitelistExt(url); // unknown -> rely on extension
          // accept text-like and json/xml/js, deny image/video/audio
          if(Array.from(TEXT_MIME).some(m => mime.includes(m))) return true;
          if(mime.startsWith('text/')) return true;
          if(mime.startsWith('image/') || mime.startsWith('video/') || mime.startsWith('audio/')) return false;
          // otherwise allow if extension in whitelist
          return urlHasWhitelistExt(url);
        }catch(e){
          registerFetchError(parsed.href, `HEAD_ERR:${String(e && e.message ? e.message : e)}`);
          // fallback: allow GET for whitelist ext on same host
          return (parsed.host === location.host) && urlHasWhitelistExt(url);
        }
      }

      // cross-host: do not fetch body
      return false;
    }catch(e){
      return false;
    }
  }

  async function fetchTextQuiet(url){
    let abs;
    try{ abs = new URL(url, location.href).href; }catch(e){ return null; }
    if(fetchCache.has(abs)) return fetchCache.get(abs);

    // only fetch same-host bodies
    try{ const p = new URL(abs); if(p.host !== location.host){ fetchCache.set(abs, null); skipped.add(abs); return null; } }catch(e){}

    try{
      const r = await fetch(abs, { credentials: 'same-origin', signal: AbortSignal.timeout(8000) });
      if(!r.ok){
        registerFetchError(abs, `HTTP_${r.status}`);
        fetchCache.set(abs, null);
        return null;
      }
      const ct = (r.headers.get('content-type')||'').split(';')[0].toLowerCase();
      const pathname = new URL(abs).pathname.toLowerCase();
      const looksLikeJs = pathname.endsWith('.js') || pathname.match(/\.chunk\.js$/);
      const looksLikeJson = pathname.endsWith('.json');
      const looksLikeXml = pathname.endsWith('.xml');
      // if content-type exists and is clearly binary and url not explicitly js/json/xml, skip
      if(ct && !Array.from(TEXT_MIME).some(m => ct.includes(m)) && !looksLikeJs && !looksLikeJson && !looksLikeXml){
        fetchCache.set(abs, null);
        skipped.add(abs);
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

  // ---------------- Content analysis ----------------
  function contextHasKeywords(text, index, keywords, radius=60){
    if(!text) return false;
    const start = Math.max(0, index - radius);
    const end = Math.min(text.length, index + radius);
    const snippet = text.slice(start, end).toLowerCase();
    return keywords.some(k => snippet.includes(k));
  }

  function scanSensitive(text){
    if(!text) return [];
    const res = [];
    for(const m of text.matchAll(DET.firebaseApiKey) || []) res.push({ type:'firebase_api_key', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.firebaseDB) || []) res.push({ type:'firebase_database_url', value:m[1], index:m.index });
    for(const m of text.matchAll(DET.firebaseProjectId) || []) res.push({ type:'firebase_project_id', value:m[1], index:m.index });
    for(const m of text.matchAll(DET.firebaseStorage) || []) res.push({ type:'firebase_storage_bucket', value:m[1], index:m.index });
    for(const m of text.matchAll(DET.googleClientId) || []) res.push({ type:'google_client_id', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.awsKey) || []) res.push({ type:'aws_key', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.longHex) || []) res.push({ type:'long_hex', value:m[1] || m[0], index:m.index });
    for(const m of text.matchAll(DET.pwdParam) || []) if(m[1]) res.push({ type:'credential_like', value:m[1], index:m.index });
    for(const m of text.matchAll(DET.urlWithPort) || []) res.push({ type:'url_with_port', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.dbConn) || []) res.push({ type:'database_conn', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.smtpUrl) || []) res.push({ type:'smtp_hint', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.appKey) || []) if(m[1]) res.push({ type:'app_key', value:m[1], index:m.index });
    for(const m of text.matchAll(DET.emailLike) || []) res.push({ type:'email', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.base64Long) || []) res.push({ type:'base64_long', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.jwtLike) || []) res.push({ type:'jwt_like', value:m[1] || m[0], index:m.index });
    for(const m of text.matchAll(DET.gitPath) || []) res.push({ type:'git_exposed', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.envFile) || []) res.push({ type:'env_filename', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.htpasswd) || []) res.push({ type:'htpasswd', value:m[0], index:m.index });
    for(const m of text.matchAll(DET.configHints) || []) res.push({ type:'config_hint', value:m[0], index:m.index });

    // dedupe and heuristics
    const uniq = [], seenSet = new Set();
    for(const it of res){
      const key = it.type + '|' + it.value;
      if(seenSet.has(key)) continue;
      // heuristics for noisy types
      if(['long_hex','base64_long','jwt_like'].includes(it.type)){
        if(!contextHasKeywords(text, it.index, ['key','token','secret','auth','password','api','client','bearer','jwt','session','access','private','db'])) continue;
      }
      if(it.type === 'email'){
        const near = contextHasKeywords(text, it.index, ['user','email','password','db','login','account']);
        if(!near){
          const countEmails = (text.match(DET.emailLike) || []).length;
          if(countEmails > 15) continue;
        }
      }
      seenSet.add(key);
      uniq.push(it);
    }
    return uniq;
  }

  function extractCandidatesFromText(text){
    if(!text) return [];
    const set = new Set();
    // quoted urls/paths
    const re1 = /['"]((?:https?:\/\/|\/\/|\/|\.\.\/|\.\/)[^'"]{1,900})['"]/g;
    for(const m of text.matchAll(re1)) set.add(m[1]);
    // template/backtick strings
    const re2 = /`([^`]{1,900})`/g;
    for(const m of text.matchAll(re2)) set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    // AJAX/fetch/axios
    const ajaxRe = /(?:fetch|axios\.(?:get|post|put|delete|patch)|open|XMLHttpRequest|new\s+Request)\s*\(\s*['"`]((?:https?:\/\/|\/|\.\.\/|\.\/)[^'"`]{1,900})['"`]/g;
    for(const m of text.matchAll(ajaxRe)) set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    // paths that look like endpoints
    const pathRe = /['"]((?:\/[a-zA-Z0-9_\-\/\.]{3,300}(?:api|graphql)[\/a-zA-Z0-9_\-\.]*)['"])/g;
    for(const m of text.matchAll(pathRe)) set.add(m[1]);
    // bare /api/... patterns
    const bareApi = /(?:\s|:|=)(\/api\/[a-zA-Z0-9_\-\/\.\{\}]+)/g;
    for(const m of text.matchAll(bareApi)) set.add(m[1]);
    return Array.from(set);
  }

  // ---------------- Progress & concurrency ----------------
  let totalResources = 0, processedResources = 0, skippedResources = 0;
  function setProgress(pct){
    scanProgressBar.style.width = pct + '%';
    scanStatus.textContent = `Scanning... ${pct}%`;
    scanInfo.textContent = `Scanned ${processedResources}/${totalResources} — Skipped ${skippedResources}`;
  }
  function incProgress(){ processedResources++; const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100; setProgress(pct); }
  function incSkipped(){ skippedResources++; processedResources++; const pct = totalResources ? Math.min(100, Math.round((processedResources/totalResources)*100)) : 100; setProgress(pct); }

  function pLimit(concurrency){
    const queue = []; let active = 0;
    const next = () => {
      if(queue.length === 0) return;
      if(active >= concurrency) return;
      active++;
      const item = queue.shift();
      const fn = item.fn;
      fn().then(v=>{ active--; item.resolve(v); next(); }).catch(e=>{ active--; item.resolve(); next(); });
    };
    return (fn) => new Promise(res => { queue.push({fn, resolve:res}); next(); });
  }
  const limit = pLimit(CONCURRENCY);

  // ---------------- Main recursive process ----------------
  async function processResource(url, depth=0, source='root', mode='smart', preferSameHost=true){
    if(stopRequested) return;
    if(depth > MAX_DEPTH) return;
    let abs;
    try{ abs = new URL(url, location.href).href; }catch(e){ return; }
    if(seen.has(abs)) return;
    seen.add(abs);

    addFound(abs, source);
    const params = extractParams(abs);
    for(const p of params) found.get(abs).params.add(p);

    const local = isSameHost(abs);
    if(!local){
      // external: include as endpoint but don't fetch body
      incProgress();
      return;
    }

    // ext-only mode: if no whitelist ext, skip
    if(mode === 'ext-only' && !urlHasWhitelistExt(abs)){ skipped.add(abs); incSkipped(); return; }

    // check shouldFetchResource
    const doFetch = await shouldFetchResource(abs, mode, preferSameHost);
    if(!doFetch){ skipped.add(abs); incSkipped(); fetchCache.set(abs, null); return; }

    // returned from cache?
    if(fetchCache.has(abs)){
      const cached = fetchCache.get(abs);
      incProgress();
      if(cached){
        if(detectKeysCheckbox.checked){
          const sens = scanSensitive(cached);
          for(const s of sens){
            const snippet = cached.slice(Math.max(0, (s.index||0)-40), Math.min(cached.length, (s.index||0)+40)).replace(/\s+/g,' ');
            if(['git_exposed','env_filename','htpasswd','config_hint'].includes(s.type)) found.get(abs).misconfig.push(Object.assign({}, s, { context: snippet }));
            else {
              found.get(abs).sensitive.push(Object.assign({}, s, { context: snippet }));
              if(s.type && s.type.startsWith('firebase')) found.get(abs).firebaseMeta[s.type] = s.value;
            }
          }
        }
        const cands = extractCandidatesFromText(cached);
        for(const c of cands){
          try{
            const res = new URL(c, abs).href;
            addFound(res, abs);
            const ps = extractParams(c);
            for(const p of ps) found.get(res).params.add(p);
            if(isSameHost(res) || isApiLike(c) || isApiLike(res)){
              await limit(()=>processResource(res, depth+1, abs, mode, preferSameHost));
            }
          }catch(e){}
        }
      }
      return;
    }

    // perform fetch
    const text = await fetchTextQuiet(abs);
    incProgress();
    if(fetchErrors.has(abs)){
      const meta = found.get(abs);
      meta.fetchErrors = Array.from(new Set([...(meta.fetchErrors||[]), ...fetchErrors.get(abs)]));
    }
    if(!text) return;

    // analyze
    if(detectKeysCheckbox.checked){
      const sens = scanSensitive(text);
      for(const s of sens){
        const snippet = text.slice(Math.max(0, (s.index||0)-40), Math.min(text.length, (s.index||0)+40)).replace(/\s+/g,' ');
        if(['git_exposed','env_filename','htpasswd','config_hint'].includes(s.type)) found.get(abs).misconfig.push(Object.assign({}, s, { context: snippet }));
        else {
          found.get(abs).sensitive.push(Object.assign({}, s, { context: snippet }));
          if(s.type && s.type.startsWith('firebase')) found.get(abs).firebaseMeta[s.type] = s.value;
        }
      }
    }

    // extract candidates & recurse
    const candidates = extractCandidatesFromText(text);
    for(const c of candidates){
      try{
        const resolved = new URL(c, abs).href;
        addFound(resolved, abs);
        const ps = extractParams(c);
        for(const p of ps) found.get(resolved).params.add(p);
        if(isSameHost(resolved) || isApiLike(c) || isApiLike(resolved)){
          await limit(()=>processResource(resolved, depth+1, abs, mode, preferSameHost));
        }
      }catch(e){}
    }
  }

  // ---------------- Gather initial candidates (aggressive like v2 but filtered) ----------------
  function gatherInitialCandidates(){
    const set = new Set();
    try{ performance.getEntriesByType('resource').map(r=>r.name).forEach(u=>set.add(u)); }catch(e){}
    document.querySelectorAll('script[src]').forEach(s => set.add(s.src));
    document.querySelectorAll('link[href]').forEach(l => set.add(l.href));
    document.querySelectorAll('a[href]').forEach(a => set.add(a.href));
    document.querySelectorAll('form[action]').forEach(f => set.add(f.action));
    // inline scripts: only extract candidates (we do not treat them as separate fetch resources)
    document.querySelectorAll('script:not([src])').forEach(s=>{
      try{ const t = s.textContent || ''; extractCandidatesFromText(t).forEach(p=>set.add(p)); }catch(e){}
    });
    // full HTML scanning for inline endpoints
    try{ const html = document.documentElement.outerHTML || document.body.innerHTML || ''; extractCandidatesFromText(html).forEach(p=>set.add(p)); }catch(e){}
    // return deduped absolute or relative list
    const arr = Array.from(set).map(u => { try { return new URL(u, location.href).href } catch(e){ return u } });
    return Array.from(new Set(arr));
  }

  // ---------------- Build list, render ----------------
  function isSensitiveItem(meta){
    if(!meta) return false;
    if(meta.sensitive && meta.sensitive.length>0) return true;
    if(meta.misconfig && meta.misconfig.length>0) return true;
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
        misconfig: meta.misconfig.slice(),
        source: meta.source,
        local: meta.local,
        apiLike: meta.apiLike,
        firebaseMeta: Object.assign({}, meta.firebaseMeta),
        fetchErrors: meta.fetchErrors || []
      });
    }
    const f = filterSelect.value;
    let filtered = list;
    if(f === 'api') filtered = list.filter(i=>i.apiLike && !isSensitiveItem(i));
    if(f === 'fuzzing') filtered = list.filter(i=>i.local && isParamBearing(i.url) && !isSensitiveItem(i));
    if(f === 'fuzzing-external') filtered = list.filter(i=>!i.local && isParamBearing(i.url) && !hostExcluded((() => { try { return new URL(i.url).host } catch(e){ return '' } })()));
    if(f === 'sensitive') filtered = list.filter(i=>isSensitiveItem(i));
    if(f === 'misconfig') filtered = list.filter(i=>i.misconfig && i.misconfig.length>0);
    filtered.sort((a,b) => (isSensitiveItem(b)?1:0) - (isSensitiveItem(a)?1:0) || ((b.apiLike|0) - (a.apiLike|0)));
    return filtered;
  }

  function render(){
    const rows = buildList();
    if(rows.length === 0){ resultsDiv.innerHTML = `<div style="color:#666">No endpoints found.</div>`; return; }
    const html = rows.map(it=>{
      const sensHtml = (it.sensitive && it.sensitive.length>0) ? `<div style="margin-top:6px;color:#900;font-weight:600">⚠ Sensitive (${it.sensitive.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.sensitive.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code title="${escapeHtml(s.context||'')}">${escapeHtml(redact(s.value))}</code>${s.context?` <span style="color:#666;font-size:11px">…${escapeHtml(redact(s.context))}</span>`:''}</li>`).join('')}</ul>` : '';
      const misHtml = (it.misconfig && it.misconfig.length>0) ? `<div style="margin-top:6px;color:#b56500;font-weight:600">⚠ Misconfig (${it.misconfig.length})</div><ul style="margin:6px 0 0 16px;color:#333">${it.misconfig.map(s=>`<li><strong>${escapeHtml(s.type)}</strong>: <code title="${escapeHtml(s.context||'')}">${escapeHtml(redact(s.value))}</code>${s.context?` <span style="color:#666;font-size:11px">…${escapeHtml(redact(s.context))}</span>`:''}</li>`).join('')}</ul>` : '';
      const fbHtml = (it.firebaseMeta && Object.keys(it.firebaseMeta).length>0) ? `<div style="margin-top:6px;color:#0366d6"><strong>Firebase:</strong> ${Object.entries(it.firebaseMeta).map(([k,v])=>`${escapeHtml(k)}=${escapeHtml(redact(v))}`).join(', ')}</div>` : '';
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

  function redact(v){ if(!v) return ''; const s=String(v); return s.length>44 ? s.slice(0,12)+'…'+s.slice(-12) : s; }
  function escapeHtml(s){ if(!s) return ''; return String(s).replace(/[&<>"']/g, m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[m])); }

  // copy/export actions
  panel.querySelector('#copy-all').onclick = async ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw && !confirm('Include raw secrets in clipboard?')) return;
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

  panel.querySelector('#export-txt').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw && !confirm('Include raw secrets in file?')) return;
    const lines = [];
    function pushItem(r){
      lines.push(`URL: ${r.url}`);
      if(r.params.length) lines.push(`Params: ${r.params.join(', ')}`);
      if(r.sensitive.length){ lines.push('Sensitive:'); for(const s of r.sensitive) lines.push(`  - ${s.type}: ${ includeRaw ? s.value : '[REDACTED]' } ${s.context?` (context: ${s.context})`:''}`); }
      if(r.misconfig.length){ lines.push('Misconfiguration:'); for(const s of r.misconfig) lines.push(`  - ${s.type}: ${ includeRaw ? s.value : '[REDACTED]' } ${s.context?` (context: ${s.context})`:''}`); }
      if(Object.keys(r.firebaseMeta||{}).length){ lines.push('Firebase hints:'); for(const [k,v] of Object.entries(r.firebaseMeta)) lines.push(`  - ${k}: ${ includeRaw ? v : '[REDACTED]' }`); }
      if(r.fetchErrors && r.fetchErrors.length) lines.push(`Fetch issues: ${r.fetchErrors.join('; ')}`);
      lines.push('');
    }
    // grouping similar to v2
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

    const blob = new Blob([lines.join('\n')], {type:'text/plain'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'endpoints-v4.txt'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  panel.querySelector('#export-json').onclick = ()=>{
    const rows = buildList();
    const includeRaw = includeRawCheckbox.checked;
    if(includeRaw && !confirm('Include raw secrets in JSON?')) return;
    const out = rows.map(r => ({
      url: r.url,
      params: r.params,
      sensitive: r.sensitive.map(s => includeRaw ? s : ({ type: s.type, value:'[REDACTED]', context: s.context })),
      misconfig: r.misconfig.map(s => includeRaw ? s : ({ type: s.type, value:'[REDACTED]', context: s.context })),
      source: r.source,
      local: r.local,
      apiLike: r.apiLike,
      firebaseMeta: r.firebaseMeta,
      fetchErrors: r.fetchErrors
    }));
    const blob = new Blob([JSON.stringify({ scanned: processedResources, found: out }, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a'); a.href = url; a.download = 'result-v4.json'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url);
  };

  panel.querySelector('#close-panel').onclick = ()=> panel.remove();

  // utility - isParamBearing
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

  // initial UI state
  resultsDiv.innerHTML = `<div style="color:#666">Ready. Choose mode and press Start.</div>`;
  scanProgressBar.style.width = '0%';
  scanProgressBar.parentElement.style.visibility = 'visible';

  // ---------------- Start/Stop logic ----------------
  startBtn.onclick = async ()=>{
    stopRequested = false;
    totalResources = 0; processedResources = 0; skippedResources = 0;
    seen.clear(); found.clear(); fetchCache.clear(); fetchErrors.clear(); skipped.clear();
    resultsDiv.innerHTML = `<div style="color:#666">Scanning... please wait.</div>`;
    const mode = modeSelect.value;
    const preferSameHost = !!sameHostOnlyCheckbox.checked;

    const inits = gatherInitialCandidates();
    // filter initial: keep those with whitelist ext or api-like or relative paths
    const filtered = inits.filter(u=>{
      try{
        const nu = new URL(u, location.href);
        if(urlHasWhitelistExt(nu.href)) return true;
        if(isApiLike(nu.href)) return true;
        if(nu.pathname && (nu.pathname.includes('/api/') || nu.pathname.includes('api'))) return true;
        return false;
      }catch(e){
        if(/\/api\//.test(String(u))) return true;
        if(/\.(js|json|xml|html|htm)(?:$|\?)/i.test(String(u))) return true;
        return false;
      }
    });

    const unique = Array.from(new Set(filtered));
    totalResources = unique.length || 1;
    processedResources = 0; skippedResources = 0;
    setProgress(0);

    const tasks = [];
    for(const r of unique){
      tasks.push(limit(()=>processResource(r, 0, 'root', mode, preferSameHost)));
    }
    await Promise.all(tasks);
    setProgress(100);
    scanStatus.textContent = `Scan complete — Found ${found.size} endpoints`;
    setTimeout(()=>{ scanProgressBar.style.width='0%'; scanProgressBar.parentElement.style.visibility='hidden'; }, 400);
    render();
  };

  stopBtn.onclick = ()=>{ stopRequested = true; scanStatus.textContent = 'Stopping...'; };

  filterSelect.onchange = render;
  detectKeysCheckbox.onchange = render;

  // ---------------- End ----------
})();
