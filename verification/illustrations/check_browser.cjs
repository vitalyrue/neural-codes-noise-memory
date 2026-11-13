/* Relevant figure checks, with only two representative visual samples. */
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),crypto=require('crypto');
const root=path.resolve(__dirname,'../..');
const rows=JSON.parse(fs.readFileSync(path.join(__dirname,'integration.json'),'utf8'));
const out=path.join(root,'verification/rendered-pages/illustrations');fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 page.setDefaultTimeout(15000);
 const records=[],errors=[],screenshots=[];
 page.on('pageerror',e=>errors.push(e.message));
 for(const width of [1440,390]){
   await page.setViewportSize({width,height:width===390?844:1000});
   const stems=[...new Set(rows.map(r=>r.stem))];
   for(const stem of stems){
     const own=rows.filter(r=>r.stem===stem);
     const cid={
       '01-foundations':'ch-foundations','02-memory-dynamics':'ch-memory-dynamics',
       '03-memory-information':'ch-memory-information','04-eye-drift':'ch-eye-drift','05-place-fields':'ch-place-fields'
     }[stem];
     const response=await page.goto('http://127.0.0.1:8765/guide/site/chapters/'+cid+'.html?illustrations=20261023',{waitUntil:'networkidle'});
     await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
     const common=await page.evaluate(()=>({viewport:innerWidth,documentWidth:document.documentElement.scrollWidth,mathErrors:[...document.querySelectorAll('mjx-merror,.MathJax_Error')].map(e=>e.textContent),unloadedImages:[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src)}));
     for(const row of own){
       const slug=row.visual_id.replace(':','-').toLowerCase();
       const selector='#'+slug;
       const state=await page.locator(selector).evaluate(el=>{
         const img=el.querySelector('img');const scroller=img.closest('div[aria-describedby]');
         const caption=el.querySelector('figcaption');const b=img.getBoundingClientRect();
         const before=scroller.scrollLeft;scroller.scrollLeft=scroller.scrollWidth;
         const moved=scroller.scrollLeft;scroller.scrollLeft=before;
         return {src:img.src,alt:img.alt,naturalWidth:img.naturalWidth,displayWidth:b.width,
           caption:caption?.textContent.trim(),captionWidth:caption?.getBoundingClientRect().width,
           scrollClient:scroller.clientWidth,scrollWidth:scroller.scrollWidth,
           needsScrolling:scroller.scrollWidth>scroller.clientWidth+2,scrollMoves:moved>0};
       });
       const imageResponse=await page.request.get(state.src);const body=await imageResponse.body();
       const actualHash=crypto.createHash('sha256').update(body).digest('hex');
       const success=response.status()===200&&imageResponse.status()===200&&actualHash===row.sha256&&
          state.alt.length>20&&state.caption?.length>25&&Math.abs(state.displayWidth-700)<1&&
          (!state.needsScrolling||state.scrollMoves)&&common.documentWidth<=common.viewport+2&&
          common.mathErrors.length===0&&common.unloadedImages.length===0;
       records.push({id:row.id,visual_id:row.visual_id,width,status:success?'pass':'fail',http:response.status(),imageHash:actualHash,...common,...state});
     }
     if(width===1440&&stem==='03-memory-information'){
       const p=path.join(out,'recall-timeline-desktop.png');await page.locator('#fig-memory-readout-timeline').screenshot({path:p});screenshots.push(p);
     }
     if(width===390&&stem==='05-place-fields'){
       const fig=page.locator('#fig-place-topology');await fig.scrollIntoViewIfNeeded();
       const p=path.join(out,'topology-narrow-start.png');await fig.screenshot({path:p});screenshots.push(p);
       await fig.locator('div[aria-describedby]').evaluate(e=>e.scrollLeft=e.scrollWidth);
       const p2=path.join(out,'topology-narrow-scrolled.png');await fig.screenshot({path:p2});screenshots.push(p2);
     }
   }
 }
 const result={at:new Date().toISOString(),scope:'All nine new images checked in browser at desktop and narrow widths; only two representative figure contexts visually sampled.',records,errors,screenshots,status:records.every(r=>r.status==='pass')&&errors.length===0?'pass':'fail'};
 fs.writeFileSync(path.join(root,'verification/publication/illustrations-browser.json'),JSON.stringify(result,null,2));
 console.log(JSON.stringify({status:result.status,checks:records.length,errors,failures:records.filter(r=>r.status!=='pass'),screenshots},null,2));
 await browser.close();if(result.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1);});
