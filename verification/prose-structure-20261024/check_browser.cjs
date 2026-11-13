const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage(),checks=[],samples=[],errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const base='http://127.0.0.1:8765/guide/site/';
 const check=(name,pass,detail)=>checks.push({name,pass,detail});
 async function go(url,width){
  await page.setViewportSize({width,height:816});await page.goto(base+url,{waitUntil:'networkidle'});
  if(await page.locator('.math').count())await page.waitForSelector('mjx-container',{timeout:20000});
  await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;await document.fonts.ready;});
 }
 async function basic(label){
  check(label+' body font remains 11.9px',await page.locator('body').evaluate(e=>Math.abs(parseFloat(getComputedStyle(e).fontSize)-11.9)<0.02));
  check(label+' blue definitions',await page.locator('main .definition-term').evaluateAll(es=>es.length>0&&es.every(e=>getComputedStyle(e).color==='rgb(31, 78, 121)')));
  check(label+' no page overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  check(label+' no math errors',await page.locator('main mjx-merror,main .MathJax_Error').count()===0);
 }
 try{
  await go('chapters/ch-synthesis.html',878);await basic('synthesis desktop');
  for(const [id,tag,count] of [['sec-synthesis-questions','ul',3],['sec-synthesis-evidence','ul',3],['sec-synthesis-related','ul',5],['sec-synthesis-next','ol',4]]){
   const n=await page.locator('#'+id+' > '+tag+' > li').count();check(id+' renders list',n===count,{actual:n,expected:count});
  }
  await page.locator('#sec-synthesis-questions').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(__dirname,'sample-synthesis-878.png')});samples.push('sample-synthesis-878.png');
  await go('chapters/ch-synthesis.html',390);await basic('synthesis mobile');
  await page.locator('#sec-synthesis-next').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(__dirname,'sample-synthesis-390.png')});samples.push('sample-synthesis-390.png');
  await go('chapters/ch-place-fields.html',878);await basic('place assumptions desktop');
  const assumptions=page.locator('main ul').first();await assumptions.scrollIntoViewIfNeeded();
  check('place assumptions render as a list',await assumptions.locator(':scope > li').count()>=3);
  await page.screenshot({path:path.join(__dirname,'sample-place-assumptions-878.png')});samples.push('sample-place-assumptions-878.png');
  await go('chapters/ch-memory-information.html',878);
  const fold=page.locator('main details.publisher-long-content').first(),summary=fold.locator(':scope > summary');
  check('example starts closed',!(await fold.evaluate(d=>d.open)));
  await summary.click();check('example opens',await fold.evaluate(d=>d.open));
  await summary.focus();await page.keyboard.press('Enter');check('example closes with keyboard',!(await fold.evaluate(d=>d.open)));
  check('no browser script errors',errors.length===0,errors);
 }finally{await browser.close();}
 const report={at:new Date().toISOString(),status:checks.every(c=>c.pass)?'pass':'fail',checks,samples,scope:'Three screenshots: synthesis desktop and mobile, place assumptions desktop. Real fold interaction on information chapter. Shared font, blue definitions, list structure, overflow and math rendering checks. No full visual sweep.'};
 fs.writeFileSync(path.join(__dirname,'browser-check.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({status:report.status,checks:checks.length,samples,failures:checks.filter(c=>!c.pass)},null,2));
 if(report.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
