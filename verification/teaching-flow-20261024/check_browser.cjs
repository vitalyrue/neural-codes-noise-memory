/* Check the selected folds and changed outline. Only three pixel samples. */
const {chromium}=require('playwright');
const fs=require('fs'), path=require('path');
const read=name=>JSON.parse(fs.readFileSync(path.join(__dirname,name),'utf8'));
(async()=>{
 const expected=read('render-expectations.json');
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage();
 const errors=[],records=[],screenshots=[];
 page.on('pageerror',e=>errors.push(e.message));
 const started=new Date().toISOString();
 try {
  for(const width of [878,390]) {
   await page.setViewportSize({width,height:816});
   for(const row of expected.pages) {
    await page.goto('http://127.0.0.1:8765/guide/site/'+row.url+'?teachingFlow=20261024',{waitUntil:'networkidle'});
    await page.evaluate(async()=>{
      if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise;
      await document.fonts.ready;
    });
    const state=await page.evaluate(()=>{
      const main=document.querySelector('main');
      const folds=[...main.querySelectorAll('details.publisher-long-content')];
      return {
       title:main.querySelector('h1')?.textContent.trim(),
       folds:folds.map(d=>({title:d.querySelector('summary')?.textContent.trim(),open:d.open,
          nested:d.querySelectorAll('details').length,
          figures:d.querySelectorAll('figure img').length,
          definitions:d.querySelectorAll('.definition-term').length,
          headings:d.querySelectorAll('h1,h2,h3,h4,h5,h6').length})),
       figures:main.querySelectorAll('figure img').length,
       definitions:[...main.querySelectorAll('.definition-term')].map(d=>({text:d.textContent,color:getComputedStyle(d).color})),
       tables:main.querySelectorAll('table').length,
       mathErrors:main.querySelectorAll('mjx-merror,.MathJax_Error').length,
       pageWidth:Math.max(document.documentElement.scrollWidth,document.body.scrollWidth),
       literalFence:main.textContent.includes('publisher-fold-always')||main.textContent.includes('{{block:'),
      };
    });
    const result={chapter:row.chapter,width,...state,checks:[]};
    const check=(name,passed)=>result.checks.push({name,passed});
    check('chapter title matches reviewed source',state.title?.replace(/^\d+(\.\d+)*\s*/,'')===row.title);
    check('fold titles match explicit selections',JSON.stringify(state.folds.map(f=>f.title))===JSON.stringify(row.folds));
    check('folds initially closed and contain only optional depth',state.folds.every(f=>!f.open&&!f.nested&&!f.figures&&!f.definitions&&!f.headings));
    check('figures and tables preserved',state.figures===row.figures && state.tables===row.tables);
    check('first definitions render blue',state.definitions.every(d=>d.color==='rgb(31, 78, 121)'));
    check('no page overflow or rendering errors',state.pageWidth<=width+1&&!state.mathErrors&&!state.literalFence);
    const folds=page.locator('main details.publisher-long-content');
    for(let i=0;i<await folds.count();i++) {
      const fold=folds.nth(i), summary=fold.locator(':scope > summary');
      await summary.click();
      check('opens fold '+i,await fold.evaluate(d=>d.open));
      check('expanded math renders '+i,await fold.locator('mjx-merror,.MathJax_Error').count()===0);
      if(width===878 && row.chapter==='ch:MEMORY-INFORMATION' && i===0) {
        await summary.scrollIntoViewIfNeeded();
        const name='sample-information-open-878.png';
        await page.screenshot({path:path.join(__dirname,name)});screenshots.push(name);
      }
      await summary.click();
      check('closes fold '+i,!(await fold.evaluate(d=>d.open)));
    }
    if(await folds.count()) {
      const fold=folds.first(),summary=fold.locator(':scope > summary');
      await summary.focus();await page.keyboard.press('Enter');
      check('keyboard opens first fold',await fold.evaluate(d=>d.open));
      await page.keyboard.press('Enter');
      check('keyboard closes first fold',!(await fold.evaluate(d=>d.open)));
      await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
      check('print opens every fold',await folds.evaluateAll(ds=>ds.every(d=>d.open)));
      await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
      check('after print restores closed state',await folds.evaluateAll(ds=>ds.every(d=>!d.open)));
    }
    if((width===878&&row.chapter==='ch:MEMORY-DYNAMICS')||(width===390&&row.chapter==='ch:PLACE-FIELDS')) {
      if(await folds.count()) await folds.first().scrollIntoViewIfNeeded();
      else await page.locator('main h1').scrollIntoViewIfNeeded();
      const name=`sample-${row.chapter.replace(':','-').toLowerCase()}-closed-${width}.png`;
      await page.screenshot({path:path.join(__dirname,name)});screenshots.push(name);
    }
    result.status=result.checks.every(c=>c.passed)?'pass':'fail';records.push(result);
   }
  }
 } finally {await browser.close();}
 const report={started_at:started,finished_at:new Date().toISOString(),
  scope:'Changed page outlines and explicit folds at 878 and 390 pixels, actual mouse and keyboard toggles, print open/restore; three screenshot samples.',
  records,screenshots,errors,status:records.every(r=>r.status==='pass')&&!errors.length?'pass':'fail'};
 fs.writeFileSync(path.join(__dirname,'browser-check.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({status:report.status,pages:records.length,screenshots,errors,failures:records.filter(r=>r.status!=='pass')},null,2));
 if(report.status!=='pass')process.exitCode=1;
})().catch(error=>{console.error(error);process.exitCode=1;});
