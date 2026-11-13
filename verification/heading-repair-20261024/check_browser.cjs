const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
const url='http://127.0.0.1:8765/guide/site/chapters/ch-foundations.html?headings=20261024';
const anchors=['sec-foundations-count-example','sec-foundations-attractor-example','sec-foundations-diffusion-example'];
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage();const records=[];
 try {
  for(const width of [878,390]){
   await page.setViewportSize({width,height:816});
   await page.goto(url,{waitUntil:'networkidle'});
   await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;});
   const r=await page.evaluate(anchors=>({
    width:innerWidth,pageWidth:document.documentElement.scrollWidth,
    mainSections:[...document.querySelectorAll('main section.level2 > h2')].map(x=>x.textContent.trim()),
    nestedHeadings:document.querySelectorAll('main h3,main h4').length,
    labels:anchors.map(id=>{const e=document.getElementById(id);return {id,count:document.querySelectorAll('[id="'+id+'"]').length,tag:e?.tagName,parent:e?.parentElement.tagName,bold:!!e?.querySelector('strong'),text:e?.textContent};}),
    toc:[...document.querySelectorAll('#TOC a')].map(x=>new URL(x.href,location.href).hash),
    footnotes:document.querySelectorAll('a[role="doc-noteref"]').length,
    mathErrors:document.querySelectorAll('mjx-merror,.MathJax_Error').length,
    figures:[...document.querySelectorAll('main figure img')].map(i=>({loaded:i.complete&&i.naturalWidth>0,src:i.getAttribute('src')})),
   }),anchors);
   if(width===878){
    await page.locator('#toc-sec-foundations-poisson').click();
    r.tocClickWorks=new URL(page.url()).hash==='#sec-foundations-poisson';
    await page.locator('#sec-foundations-count-example').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(__dirname,'foundation-example-878.png')});
   }
   r.status=r.width===r.pageWidth&&r.mainSections.length===6&&r.nestedHeadings===0&&r.labels.every(x=>x.count===1&&x.tag==='SPAN'&&x.parent==='P'&&x.bold)&&anchors.every(id=>!r.toc.includes('#'+id))&&r.footnotes===7&&r.mathErrors===0&&r.figures.length===2&&r.figures.every(i=>i.loaded)&&(width!==878||r.tocClickWorks)?'pass':'fail';
   records.push(r);
  }
  await page.goto(url+'#sec-foundations-attractor-example',{waitUntil:'networkidle'});
  const oldAnchor=await page.locator('#sec-foundations-attractor-example').boundingBox();
  const result={at:new Date().toISOString(),records,oldAnchorNavigation:!!oldAnchor&&oldAnchor.y>=0&&oldAnchor.y<816,status:records.every(r=>r.status==='pass')&&!!oldAnchor&&oldAnchor.y>=0&&oldAnchor.y<816?'pass':'fail'};
  fs.writeFileSync(path.join(root,'verification/publication/foundations-heading-browser.json'),JSON.stringify(result,null,2));
  console.log(JSON.stringify(result,null,2));
  if(result.status!=='pass')process.exitCode=1;
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
