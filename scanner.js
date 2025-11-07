javascript:(async function(){
  const panel=document.createElement("div");
  Object.assign(panel.style,{
    position:"fixed",bottom:"0",left:"0",width:"100%",maxHeight:"60%",
    overflowY:"auto",backgroundColor:"#fff",color:"#000",padding:"10px",
    zIndex:99999,borderTop:"2px solid #000",fontFamily:"Arial, sans-serif",
    fontSize:"13px"
  });

  panel.innerHTML=`
  <div style="display:flex;justify-content:space-between;align-items:center;gap:8px">
    <h4 style="margin:0">Endpoint Scanner</h4>
    <div>
      <select id="scan-filter" title="Filter">
        <option value="all">All</option>
        <option value="api">API-like only</option>
        <option value="external">External only</option>
        <option value="local">Local only</option>
      </select>
      <label style="margin-left:8px">
        <input type="checkbox" id="detect-keys" checked> Detect keys
      </label>
      <button id="export-json">Export JSON</button>
      <button id="export-csv">Export CSV</button>
      <button id="copy-all">Copy All</button>
      <button id="close-scan">Close</button>
    </div>
  </div>
  <hr>
  <div id="results" style="max-height:45vh;overflow:auto;padding-left:8px"></div>`;

  document.body.appendChild(panel);
  const resultsDiv=panel.querySelector("#results"),
        filterSelect=panel.querySelector("#scan-filter"),
        detectKeysCheckbox=panel.querySelector("#detect-keys");

  const MAX_DEPTH=3;
  const excludedHosts=[
    /(^|\.)googleapis\.com$/,
    /(^|\.)gstatic\.com$/,
    /(^|\.)googleusercontent\.com$/,
    /(^|\.)cloudflare\.com$/,
    /(^|\.)cdnjs\.cloudflare\.com$/
  ];
  
  const seenUrls=new Set(),found=new Map();

  function hostExcluded(host){
    try{for(const r of excludedHosts) if(r.test(host)) return true}catch(e){}
    return false;
  }
  function isLocal(u){
    try{
      const url=new URL(u,location.href);
      return url.origin===location.origin && !hostExcluded(url.host);
    }catch(e){return false;}
  }
  function isApiLike(u){
    try{
      const url=new URL(u,location.href);
      return url.pathname.includes('/api/') ||
             url.host.startsWith('api.') ||
             /\/v\d+(\.|\/)/.test(url.pathname) ||
             /\/graphql$/.test(url.pathname);
    }catch(e){
      return /\/api\//.test(u)||/:\\w+/.test(u)||/\{.+\}/.test(u);
    }
  }

  async function fetchText(url){
    try{
      const r=await fetch(url,{credentials:'same-origin'});
      if(!r.ok) return null;
      return await r.text();
    }catch{return null;}
  }

  function extractCandidates(text){
    const set=new Set();
    if(!text) return[];
    const re1=/['"]((?:https?:\/\/|\/\/|\/|\.\.\/|\.\/)[^'"]{1,800})['"]/g;
    for(const m of text.matchAll(re1)) set.add(m[1]);
    const re2=/`([^`]{1,800})`/g;
    for(const m of text.matchAll(re2))
      set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    const ajaxRe=/(?:fetch|axios\.(?:get|post|put|delete|patch)|open)\s*\(\s*['"`]((?:https?:\/\/|\/|\.\.\/|\.\/)[^'"`]{1,800})['"`]/g;
    for(const m of text.matchAll(ajaxRe))
      set.add(m[1].replace(/\$\{[^}]+\}/g,'{param}'));
    return Array.from(set);
  }

  function addFound(abs,meta={}){
    try{
      const u=new URL(abs,location.href).href;
      if(!found.has(u))
        found.set(u,{
          params:new Set(),keys:new Set(),
          source:meta.source||'detected',
          local:isLocal(u),apiLike:isApiLike(u)
        });
    }catch{}
  }

  function extractParamsFromUrlString(u){
    const params=new Set();
    try{
      (u.match(/\{([^}]+)\}/g)||[]).forEach(x=>params.add(x.replace(/[{}]/g,'')));
      (u.match(/:([a-zA-Z0-9_]+)/g)||[]).forEach(x=>params.add(x.replace(/^:/,'')));
      const parsed=new URL(u,location.href);
      for(const k of parsed.searchParams.keys()) params.add(k);
    }catch{}
    return params;
  }

  function extractKeys(text){
    const keys=new Set();
    if(!text) return keys;
    const re=/(?:(?:api[_-]?key|apikey|apiKey|token|access[_-]?token|auth|client[_-]?id|secret)[\s'"]{0,5}[:=]\s*['"]([^'"]{6,200})['"])/gi;
    for(const m of text.matchAll(re)) keys.add(m[1]);
    return keys;
  }

  async function processUrl(u,depth=0,source='root'){
    if(depth>MAX_DEPTH) return;
    let abs;
    try{abs=new URL(u,location.href).href;}catch{return;}
    if(seenUrls.has(abs)) return;
    seenUrls.add(abs);
    addFound(abs,{source});
    extractParamsFromUrlString(abs).forEach(p=>found.get(abs).params.add(p));
    if(!isLocal(abs)){return;}
    const text=await fetchText(abs);
    if(!text) return;
    if(detectKeysCheckbox.checked)
      extractKeys(text).forEach(k=>found.get(abs).keys.add(k));
    const candidates=extractCandidates(text);
    for(const c of candidates){
      try{
        const resolved=new URL(c,abs).href;
        addFound(resolved,{source:abs});
        extractParamsFromUrlString(c).forEach(p=>found.get(resolved).params.add(p));
        if(isLocal(resolved)||isApiLike(c)||isApiLike(resolved))
          await processUrl(resolved,depth+1,abs);
      }catch{}
    }
  }

  // ambil semua resource (tanpa log spam)
  const resources=new Set();
  try{performance.getEntriesByType('resource').map(r=>r.name).forEach(u=>resources.add(u));}catch{}
  for(const s of document.querySelectorAll('script[src]')) resources.add(s.src);
  for(const s of document.querySelectorAll('script:not([src])')) 
    try{extractCandidates(s.textContent||'').forEach(p=>resources.add(p));}catch{}
  try{extractCandidates(document.documentElement.outerHTML||document.body.innerHTML).forEach(p=>resources.add(p));}catch{}

  for(const r of resources) await processUrl(r,0,'resource');

  // Tampilkan hasil langsung
  function buildList(){
    const list=[];
    for(const [u,meta] of found.entries())
      list.push({
        url:u,
        params:Array.from(meta.params),
        keys:Array.from(meta.keys),
        source:meta.source,
        local:meta.local,
        apiLike:meta.apiLike
      });
    const f=filterSelect.value;
    let filtered=list;
    if(f==='api') filtered=list.filter(i=>i.apiLike);
    if(f==='external') filtered=list.filter(i=>!i.local);
    if(f==='local') filtered=list.filter(i=>i.local);
    filtered.sort((a,b)=>(b.apiLike|0)-(a.apiLike|0));
    return filtered;
  }

  function render(){
    const rows=buildList();
    const html=rows.map(it=>`
      <div style="padding:6px;border-bottom:1px solid #eee">
        <div><a href="${it.url}" target="_blank" rel="noreferrer noopener">${it.url}</a></div>
        <div style="font-size:12px;color:#333">
          ${it.params.length?`params: ${it.params.join(', ')} `:''}
          ${it.keys.length?` <span style="color:crimson">keys: ${it.keys.map(k=>'[REDACTED]').join(', ')}</span>`:''}
          <span style="margin-left:8px">src: ${it.source}</span>
          <span style="margin-left:8px">local: ${it.local}</span>
          <span style="margin-left:8px">apiLike: ${it.apiLike}</span>
        </div>
      </div>`).join('');
    resultsDiv.innerHTML = html || '<i>No endpoints found</i>';
  }

  render();
  filterSelect.onchange=render;
  panel.querySelector("#close-scan").onclick=()=>panel.remove();

  // Copy All
  panel.querySelector("#copy-all").onclick=async ()=>{
    const rows=buildList();
    const text=rows.map(r=>`${r.url}${r.params.length?` | params: ${r.params.join(',')}`:''}${r.keys.length?` | keys: ${r.keys.join(',')}`:''} | src: ${r.source}`).join("\n");
    try{
      await navigator.clipboard.writeText(text);
      alert(`Copied ${rows.length} items`);
    }catch{
      const ta=document.createElement('textarea');
      ta.value=text;document.body.appendChild(ta);
      ta.select();document.execCommand('copy');
      ta.remove();alert('Copied (fallback)');
    }
  };

  // Export JSON/CSV
  function downloadFile(filename,content){
    const blob=new Blob([content],{type:'application/octet-stream'});
    const url=URL.createObjectURL(blob);
    const a=document.createElement('a');
    a.href=url;a.download=filename;
    document.body.appendChild(a);a.click();a.remove();
    URL.revokeObjectURL(url);
  }
  panel.querySelector('#export-json').onclick=()=>{
    const rows=buildList();
    downloadFile('endpoints.json',JSON.stringify(rows,null,2));
  };
  panel.querySelector('#export-csv').onclick=()=>{
    const rows=buildList();
    const header=['url','params','keys','source','local','apiLike'];
    const csv=[header.join(',')].concat(rows.map(r=>{
      const esc=v=>`"${String(v).replace(/"/g,'""')}"`;
      return [esc(r.url),esc(r.params.join(';')),esc(r.keys.join(';')),esc(r.source),r.local,r.apiLike].join(',');
    })).join('\n');
    downloadFile('endpoints.csv',csv);
  };
})();
