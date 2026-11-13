const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const read=n=>JSON.parse(fs.readFileSync(path.join(__dirname,n),'utf8'));
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
 try {
  for(const width of [878,390]){
   await go('chapters/ch-foundations.html',width);
   for(const media of ['screen','print']){
    await page.emulateMedia({media});
    const sizes=await page.evaluate(()=>Object.fromEntries(['html','body','main p','main h1','main h2','main figcaption','main summary','#quarto-sidebar','.sidebar-title'].map(s=>{const e=document.querySelector(s);return[s,e?parseFloat(getComputedStyle(e).fontSize):null];})));
    const before=read('font-baseline.json').find(r=>r.width===width&&r.media===media);
    for(const [selector,size] of Object.entries(sizes)){
     const old=parseFloat(before.sizes[selector]?.size);if(!old||size===null)continue;
     const expected=old*(media==='screen'?0.7:1);
     check(`${width}px ${media} font ${selector}`,Math.abs(size-expected)<0.025,{before:old,after:size,expected});
    }
   }
   await page.emulateMedia({media:'screen'});
   const fold=page.locator('main details.publisher-long-content').first(),summary=fold.locator(':scope > summary');
   await summary.click();check(`${width}px example opens`,await fold.evaluate(d=>d.open));
   await summary.focus();await page.keyboard.press('Enter');check(`${width}px keyboard closes example`,!(await fold.evaluate(d=>d.open)));
   check(`${width}px definitions stay blue`,await page.locator('main .definition-term').evaluateAll(es=>es.every(e=>getComputedStyle(e).color==='rgb(31, 78, 121)')));
   check(`${width}px no page overflow`,await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
   if(width===878){await page.locator('main h1').scrollIntoViewIfNeeded();const name='sample-foundations-878.png';await page.screenshot({path:path.join(__dirname,name)});samples.push(name);}
  }
  await go('chapters/ch-place-tests.html',390);
  check('place continuation opens with overview',await page.locator('main').evaluate(m=>{const first=m.querySelector('section.level2');return first&&[...m.children].some(e=>e.tagName==='P'&&e.compareDocumentPosition(first)&Node.DOCUMENT_POSITION_FOLLOWING);}));
  check('place continuation has no page overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  await page.locator('main h1').scrollIntoViewIfNeeded();await page.screenshot({path:path.join(__dirname,'sample-place-tests-390.png')});samples.push('sample-place-tests-390.png');
  await go('chapters/ch-memory-information.html',878);
  const note=page.locator('main details.publisher-long-content').first();await note.locator('summary').click();
  check('information example expands',await note.evaluate(d=>d.open));
  await note.scrollIntoViewIfNeeded();await page.screenshot({path:path.join(__dirname,'sample-information-expanded-878.png')});samples.push('sample-information-expanded-878.png');
  check('expanded example has no math errors',await page.locator('main mjx-merror,main .MathJax_Error').count()===0);
  await note.locator('summary').click();
  await page.evaluate(()=>dispatchEvent(new Event('beforeprint')));
  check('printing expands notes',await page.locator('main details').evaluateAll(es=>es.every(e=>e.open)));
  await page.evaluate(()=>dispatchEvent(new Event('afterprint')));
  await go('chapters/ch-foundations.html#fig-foundations-paper-map',878);
  await page.waitForURL('**/ch-persistence.html#fig-foundations-paper-map');
  check('old figure bookmark reaches moved figure',await page.locator('#fig-foundations-paper-map').count()===1,{url:page.url()});
  check('retained figure width',await page.locator('#fig-foundations-paper-map img').evaluate(e=>Math.abs(e.getBoundingClientRect().width-700)<1));
  check('no browser script errors',errors.length===0,errors);
 }finally{await browser.close();}
 const report={at:new Date().toISOString(),status:checks.every(c=>c.pass)?'pass':'fail',checks,samples,scope:'Three screenshot samples; exact screen font reduction and unchanged print sizes on one representative page at878px/390px; real fold interaction; moved bookmark; no full visual sweep.'};
 fs.writeFileSync(path.join(__dirname,'browser-check.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({status:report.status,checks:checks.length,samples,failures:checks.filter(c=>!c.pass)},null,2));
 if(report.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exitCode=1;});
