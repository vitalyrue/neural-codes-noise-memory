const { chromium }=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'..');
const out=path.join(root,'verification','rendered-pages');fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000},deviceScaleFactor:1});
 page.setDefaultTimeout(15000);
 const records=[],errors=[];page.on('pageerror',e=>errors.push(e.message));
 const views=[
  ['index.html',null,'guide-home',1440,1000],
  ['chapters/ch-foundations.html','sec:FOUNDATIONS-ATTRACTOR-EXAMPLE','attractor-desktop',1440,1000],
  ['chapters/ch-memory-information.html','sec:MEMORY-IDEAL','ideal-readout-desktop',1440,1000],
  ['chapters/ch-eye-drift.html','sec:EYE-INVERSE-FILTER','eye-mobile',390,844],
  ['chapters/ch-place-fields.html','sec:PLACE-TOPOLOGY','place-mobile',390,844],
 ];
 for(const [url,id,label,width,height] of views){
  await page.setViewportSize({width,height});
  const response=await page.goto('http://127.0.0.1:8765/guide/site/'+url,{waitUntil:'networkidle'});
  await page.evaluate(async()=>{if(window.MathJax?.startup?.promise)await window.MathJax.startup.promise;});
  if(id)await page.locator('[id="'+id.replace(/:/g,'-').toLowerCase()+'"]').scrollIntoViewIfNeeded();
  const state=await page.evaluate(()=>({title:document.title,viewport:innerWidth,documentWidth:document.documentElement.scrollWidth,math:document.querySelectorAll('mjx-container').length,mathErrors:[...document.querySelectorAll('mjx-merror,.MathJax_Error')].map(e=>e.textContent),figures:[...document.images].map(e=>({src:e.getAttribute('src'),complete:e.complete,width:e.naturalWidth,alt:e.alt})),hasSidebar:!!document.querySelector('#quarto-sidebar'),brokenImages:[...document.images].filter(e=>!e.complete||e.naturalWidth===0).map(e=>e.src)}));
  if(width<500)state.mathScrolling=await page.evaluate(()=>{
   const e=[...document.querySelectorAll('span.math.display')].find(e=>e.scrollWidth>e.clientWidth+2);
   if(!e)return {needed:false};
   e.scrollLeft=e.scrollWidth;const moved=e.scrollLeft;e.scrollLeft=0;
   return {needed:true,clientWidth:e.clientWidth,contentWidth:e.scrollWidth,moved,works:moved>0};
  });
  await page.screenshot({path:path.join(out,label+'.png')});
  if(label==='attractor-desktop')await page.locator('[id="fig-foundations-attractor"]').screenshot({path:path.join(out,'attractor-figure.png')});
  records.push({url,id,label,width,height,status:response.status(),...state});
 }
 // Use the actual navigation controls and footnote links.
 await page.setViewportSize({width:1440,height:1000});
 await page.goto('http://127.0.0.1:8765/guide/site/chapters/ch-foundations.html',{waitUntil:'networkidle'});
 const next=page.locator('a.pagination-link').last();
 const nextText=await next.innerText();await next.click();await page.waitForLoadState('networkidle');
 const navigation={nextText,result:page.url(),success:page.url().endsWith('ch-memory-dynamics.html')};
 const footnote=page.locator('a[role="doc-noteref"]').first();
 await footnote.click();
 const footnoteInteraction={href:await footnote.getAttribute('href'),fragment:new URL(page.url()).hash};
 await page.goto('http://127.0.0.1:8765/guide/site/frontmatter/ch-reading-guide.html',{waitUntil:'networkidle'});
 const paper=page.locator('a[href$="burak-fiete-2012-persistent-activity.pdf"]').first();
 const paperURL=await paper.getAttribute('href');const paperResponse=await page.request.get(new URL(paperURL,page.url()).href);
 const paperLink={href:paperURL,status:paperResponse.status(),type:paperResponse.headers()['content-type']};
 await page.goto('http://127.0.0.1:8765/guide/site/chapters/ch-eye-drift.html',{waitUntil:'networkidle'});
 await page.setViewportSize({width:390,height:844});
 const toggle=page.locator('.quarto-btn-toggle').first();
 let mobileNavigation={controlFound:await toggle.count()};
 if(await toggle.count()){await toggle.click();mobileNavigation.expanded=await toggle.getAttribute('aria-expanded');}
 const failures=records.filter(r=>r.status!==200||r.documentWidth>r.viewport+2||r.mathErrors.length||r.brokenImages.length||(r.id&&r.math===0)||(r.mathScrolling?.needed&&!r.mathScrolling.works));
 const result={checked_at:new Date().toISOString(),scope:'Representative views and real navigation/footnote/paper/menu interaction, not every page visually inspected',records,errors,navigation,footnoteInteraction,paperLink,mobileNavigation,status:failures.length||errors.length||!navigation.success||paperLink.status!==200?'failed':'pass'};
 fs.writeFileSync(path.join(root,'verification/publication/browser-checks.json'),JSON.stringify(result,null,2));
 console.log(JSON.stringify(result,null,2));await browser.close();
 if(result.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1);});
