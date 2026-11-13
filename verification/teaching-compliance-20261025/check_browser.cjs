const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage(),checks=[],samples=[],errors=[],snapshots=[];
 page.on('pageerror',e=>errors.push(e.message));
 const base='http://127.0.0.1:8765/guide/site/';
 const check=(name,pass,detail)=>checks.push({name,pass,detail});
 async function go(url,width){
  await page.setViewportSize({width,height:816});await page.goto(base+url,{waitUntil:'networkidle'});
  if(await page.locator('.math').count())await page.waitForSelector('mjx-container',{timeout:20000});
  await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;await document.fonts.ready;});
  snapshots.push({url,width,headings:await page.locator('main h1,main h2').allTextContents()});
 }
 async function basic(label){
  check(label+' body font 11.9px',await page.locator('body').evaluate(e=>Math.abs(parseFloat(getComputedStyle(e).fontSize)-11.9)<0.02));
  check(label+' blue definitions',await page.locator('main .definition-term').evaluateAll(es=>es.length>0&&es.every(e=>getComputedStyle(e).color==='rgb(31, 78, 121)')));
  check(label+' no page overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  check(label+' no math errors',await page.locator('main mjx-merror,main .MathJax_Error').count()===0);
 }
 async function sample(name){await page.screenshot({path:path.join(__dirname,name)});samples.push(name);}
 try{
  await go('chapters/ch-persistence.html',878);await basic('persistence desktop');
  const brown=page.locator('main p').filter({hasText:'To describe this limit with a continuous path'});
  check('Brownian definition states zero mean and continuous paths',await brown.count()===1&&(await brown.innerText()).includes('mean zero')&&(await brown.innerText()).includes('continuous paths'));
  await brown.scrollIntoViewIfNeeded();await sample('sample-brownian-878.png');
  const map=page.locator('#fig-foundations-paper-map img');
  check('corrected paper map loads at original dimensions',await map.evaluate(e=>e.complete&&e.naturalWidth===1680&&e.naturalHeight===1428));
  await go('chapters/ch-eye-timing.html',878);await basic('eye timing desktop');
  const bridge=page.locator('main p').filter({hasText:'Products of distinct increments have zero mean'});
  check('new covariance bridge renders',await bridge.count()===1);
  await bridge.scrollIntoViewIfNeeded();await sample('sample-covariance-878.png');
  await go('chapters/ch-eye-timing.html',390);await basic('eye timing narrow');
  await page.locator('main p').filter({hasText:'Products of distinct increments have zero mean'}).scrollIntoViewIfNeeded();await sample('sample-covariance-390.png');
  const scrollers=page.locator('main .math.display');
  const scroll=await scrollers.evaluateAll(es=>{const e=es.find(e=>e.scrollWidth>e.clientWidth+4);if(!e)return {available:false};e.scrollLeft=25;return {available:true,scrollLeft:e.scrollLeft};});
  check('wide equation can scroll locally when needed',!scroll.available||scroll.scrollLeft>0,scroll);
  await go('chapters/ch-memory-information.html',878);
  const fold=page.locator('main details.publisher-long-content').first(),summary=fold.locator(':scope > summary');
  check('example starts closed',!(await fold.evaluate(d=>d.open)));
  await summary.click();check('example opens',await fold.evaluate(d=>d.open));
  await summary.focus();await page.keyboard.press('Enter');check('example closes by keyboard',!(await fold.evaluate(d=>d.open)));
  const note=page.locator('main a[role="doc-noteref"]').first();
  await note.click();check('source note navigation reaches existing target',await page.evaluate(()=>!!document.getElementById(decodeURIComponent(location.hash.slice(1)))));
  const paper=page.locator('main a[href*=".pdf#page="]').first();const href=await paper.getAttribute('href');
  const pdf=await page.request.get(new URL(href,page.url()).href.split('#')[0]);check('precise local paper link returns PDF',pdf.ok()&&(pdf.headers()['content-type']||'').includes('pdf'),{href,status:pdf.status()});
  check('no browser script errors',errors.length===0,errors);
 }finally{await browser.close();}
 const report={at:new Date().toISOString(),status:checks.every(c=>c.pass)?'pass':'fail',checks,samples,snapshots,scope:'Three screenshots: Brownian definition desktop, covariance derivation desktop/narrow. Actual example click/keyboard, source-note navigation, PDF target fetch, shared font and definition color, overflow and math checks. No full visual sweep.'};
 fs.writeFileSync(path.join(__dirname,'browser-check.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({status:report.status,checks:checks.length,samples,failures:checks.filter(c=>!c.pass)},null,2));
 if(report.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
