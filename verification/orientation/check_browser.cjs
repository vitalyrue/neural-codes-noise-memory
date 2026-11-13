/* Revised opening only; meaning is checked by the independent reader. */
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
const out=path.join(root,'verification/rendered-pages/orientation');fs.mkdirSync(out,{recursive:true});
const ids=['sec-reading-field','sec-reading-memory','sec-reading-eye','sec-reading-place','sec-reading-start','sec-reading-papers','sec-reading-scope'];
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage();page.setDefaultTimeout(15000);
 const records=[],screenshots=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
 for(const width of [1440,878,390]){
   await page.setViewportSize({width,height:width===878?816:844});
   const response=await page.goto('http://127.0.0.1:8765/guide/site/frontmatter/ch-reading-guide.html?orientation=20261023',{waitUntil:'networkidle'});
   await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;});
   const state=await page.evaluate(ids=>({
     title:document.querySelector('main h1')?.textContent.trim(),viewport:innerWidth,documentWidth:document.documentElement.scrollWidth,
     sections:ids.map(id=>({id,count:document.querySelectorAll('[id="'+id+'"]').length,title:document.getElementById(id)?.querySelector('h2')?.textContent.trim()})),
     mathErrors:[...document.querySelectorAll('mjx-merror,.MathJax_Error')].map(e=>e.textContent),
     tocTargets:[...document.querySelectorAll('#TOC a')].map(e=>new URL(e.href,location.href).hash),
     footnotes:document.querySelectorAll('a[role="doc-noteref"]').length,
   }),ids);
   if(width===1440){
     const toc=page.locator('#toc-sec-reading-place');await toc.click();
     state.tocClickWorks=new URL(page.url()).hash==='#sec-reading-place';
   }
   if(width===878){
     await page.evaluate(()=>scrollTo(0,0));const p=path.join(out,'scientific-opening-878.png');await page.screenshot({path:p});screenshots.push(p);
   }
   if(width===390){
     await page.locator('#sec-reading-eye h2').scrollIntoViewIfNeeded();const p=path.join(out,'eye-overview-390.png');await page.screenshot({path:p});screenshots.push(p);
   }
   state.status=response.status()===200&&state.title==='Research questions and reading guide'&&state.documentWidth<=width+2&&state.sections.every(s=>s.count===1)&&ids.every(id=>state.tocTargets.includes('#'+id))&&state.mathErrors.length===0&&state.footnotes===3&&(width!==1440||state.tocClickWorks)?'pass':'fail';
   records.push({width,http:response.status(),...state});
 }
 const result={at:new Date().toISOString(),scope:'Revised frontmatter at desktop, user viewport and narrow width; two representative screenshots, one real TOC click. No whole-book visual sweep.',records,screenshots,errors,status:records.every(r=>r.status==='pass')&&errors.length===0?'pass':'fail'};
 fs.writeFileSync(path.join(root,'verification/publication/orientation-browser.json'),JSON.stringify(result,null,2));
 console.log(JSON.stringify({status:result.status,records,errors,screenshots},null,2));
 await browser.close();if(result.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1);});
