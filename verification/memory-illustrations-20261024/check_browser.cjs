const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const url='http://127.0.0.1:8765/guide/site/chapters/ch-memory-dynamics.html?figures=20261024';
const stems=['memory-spike-trace','memory-inhibition-rates','memory-line-ring'];
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage();
 const pdfOnly=process.argv.includes('--pdf-only');
 const records=pdfOnly?JSON.parse(fs.readFileSync(path.join(__dirname,'browser-check.json'),'utf8')).records:[];
 const links=[];
 try{
  for(const width of (pdfOnly?[]:[878,390])){
   await page.setViewportSize({width,height:816});
   await page.goto(url,{waitUntil:'networkidle'});
   await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;});
   const result=await page.evaluate(stems=>({
    width:innerWidth,pageWidth:document.documentElement.scrollWidth,
    mathErrors:document.querySelectorAll('mjx-merror,.MathJax_Error').length,
    mainFigures:document.querySelectorAll('main figure img').length,
    pdfLinks:[...document.querySelectorAll('main a[href]')].filter(a=>a.href.includes('.pdf#page=')).length,
    figures:stems.map(stem=>{
     const img=[...document.querySelectorAll('main figure img')].find(i=>i.src.includes(stem));
     const wrapper=img?.closest('.figure-scroll');
     return {stem,loaded:!!img&&img.complete&&img.naturalWidth>0,width:img?.getBoundingClientRect().width,
      alt:img?.alt,wrapperWidth:wrapper?.clientWidth,wrapperScrollWidth:wrapper?.scrollWidth,
      caption:img?.closest('figure')?.querySelector('figcaption')?.textContent.trim()};
    })
   }),stems);
   const last=page.locator('.figure-scroll').filter({has:page.locator('img[src*="memory-line-ring"]')});
   const scroller=last.locator('figure > div[aria-describedby]');
   await last.scrollIntoViewIfNeeded();
   result.horizontalScroll=await scroller.evaluate(el=>{el.scrollLeft=150;return {overflow:el.scrollWidth>el.clientWidth,moved:el.scrollLeft>0};});
   if(width===878){
    await page.locator('img[src*="memory-spike-trace"]').scrollIntoViewIfNeeded();
    await page.screenshot({path:path.join(__dirname,'chapter-spikes-878.png')});
   }else{
    await scroller.evaluate(el=>{el.scrollLeft=0;});
    await page.screenshot({path:path.join(__dirname,'chapter-ring-390.png')});
   }
   result.status=result.pageWidth===width&&result.mathErrors===0&&result.mainFigures===4&&result.figures.every(f=>f.loaded&&f.alt&&f.caption&&Math.abs(f.width-700)<2)&&(!result.horizontalScroll.overflow||result.horizontalScroll.moved)?'pass':'fail';
   records.push(result);
  }
  await page.setViewportSize({width:1100,height:900});
  for(const [label,pageNumber,file] of [
    ['Model, Eqs. 7–9, p. 5',5,'clicked-paper-model.png'],
    ['SI Eq. S18, p. 4',4,'clicked-si-s18.png']]){
   await page.goto(url,{waitUntil:'networkidle'});
   await page.getByRole('link',{name:label,exact:true}).first().click();
   await page.waitForURL('**/*.pdf#*',{waitUntil:'load'});
   await page.waitForTimeout(6000);
   await page.screenshot({path:path.join(__dirname,file)});
   links.push({label,url:page.url(),expectedPage:pageNumber,status:page.url().includes('.pdf#page='+pageNumber+'&zoom=')?'pass':'fail'});
  }
  const data={at:new Date().toISOString(),records,links,status:[...records,...links].every(r=>r.status==='pass')?'pass':'fail',scope:'Three new figures at two widths; two representative native PDF clicks. Screenshot content inspected separately.'};
  fs.writeFileSync(path.join(__dirname,'browser-check.json'),JSON.stringify(data,null,2));
  console.log(JSON.stringify(data,null,2));
  if(data.status!=='pass')process.exitCode=1;
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1);});
