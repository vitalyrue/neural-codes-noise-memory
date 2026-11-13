const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');const root=path.resolve(__dirname,'..');
(async()=>{
 const b=await chromium.launch({channel:'msedge',headless:true});
 try {
  const p=await b.newPage({viewport:{width:1440,height:1000}});p.setDefaultTimeout(15000);
  const errors=[];p.on('pageerror',e=>errors.push(e.message));const records=[];
  for(const name of ['ch-eye-drift','ch-place-fields','ch-synthesis']){
   await p.setViewportSize({width:1440,height:1000});
   const response=await p.goto('http://127.0.0.1:8765/guide/site/chapters/'+name+'.html?tables=20261023',{waitUntil:'networkidle'});
   await p.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise});
   for(const viewport of [1440,390]){
    await p.setViewportSize({width:viewport,height:1000});
    const state=await p.evaluate(()=>({viewport:innerWidth,documentWidth:document.documentElement.scrollWidth,mathErrors:document.querySelectorAll('mjx-merror,.MathJax_Error').length,flattened:[...document.querySelectorAll('main .line-block')].filter(e=>e.textContent.includes('|')).length,tables:[...document.querySelectorAll('main table')].map(t=>{
     const w=t.closest('.table-responsive');const needed=!!w&&w.scrollWidth>w.clientWidth+1;let moved=0;if(w){w.scrollLeft=w.scrollWidth;moved=w.scrollLeft;w.scrollLeft=0}
     return {id:t.closest('[id^="tbl-"]')?.id,columns:t.querySelectorAll('thead th').length,rows:t.querySelectorAll('tbody tr').length,math:t.querySelectorAll('mjx-container').length,clientWidth:w?.clientWidth,contentWidth:w?.scrollWidth,scrollNeeded:needed,scrollWorks:!needed||moved>0};
    })}));
    records.push({page:name,status:response.status(),...state});
    if(viewport===1440)for(const t of state.tables)await p.locator('[id="'+t.id+'"]').screenshot({path:path.join(root,'verification/rendered-pages',t.id+'-20261023.png')});
    if(viewport===390&&name==='ch-place-fields')await p.locator('#tbl-place-size-laws').screenshot({path:path.join(root,'verification/rendered-pages','tbl-place-size-laws-mobile-20261023.png')});
   }
  }
  const failed=records.some(r=>r.status!==200||r.documentWidth>r.viewport+2||r.mathErrors||r.flattened||r.tables.some(t=>!t.scrollWorks));
  const out={checked_at:new Date().toISOString(),status:failed||errors.length?'failed':'pass',records,errors,scope:'All four guide tables on desktop and 390px screens; table-only checks, no new semantic review.'};
  fs.writeFileSync(path.join(root,'verification/publication/all-table-browser.json'),JSON.stringify(out,null,2));
  console.log(JSON.stringify(out));if(out.status!=='pass')process.exitCode=1;
 }finally{await b.close()}
})().catch(e=>{console.error(e);process.exit(1)});
