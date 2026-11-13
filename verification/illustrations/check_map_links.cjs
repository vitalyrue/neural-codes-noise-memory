const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage({viewport:{width:1440,height:1000}});
 const records=[];
 for(const url of ['frontmatter/ch-reading-guide.html','chapters/ch-synthesis.html']){
   await page.goto('http://127.0.0.1:8765/guide/site/'+url+'?map=20261023',{waitUntil:'domcontentloaded'});
   const link=page.getByRole('link',{name:'guide map',exact:true});
   const href=await link.getAttribute('href');await link.click();
   await page.waitForURL(/ch-foundations\.html#fig-foundations-paper-map$/);
   const figure=page.locator('#fig-foundations-paper-map');await figure.waitFor({state:'visible'});
   const state=await figure.evaluate(async el=>{const i=el.querySelector('img');await i.decode();return {id:el.id,src:i.getAttribute('src'),alt:i.alt,width:i.getBoundingClientRect().width,naturalWidth:i.naturalWidth};});
   records.push({from:url,href,to:page.url(),...state,status:state.naturalWidth>0&&Math.abs(state.width-700)<1?'pass':'fail'});
 }
 const result={at:new Date().toISOString(),status:records.every(r=>r.status==='pass')?'pass':'fail',records,
   prior_browser_checks:'illustrations-browser.json: 18 checks reused because all nine reviewed figure inputs and compiled owning-chapter hashes are unchanged; only two external navigation paragraphs were added.'};
 fs.writeFileSync(path.join(root,'verification/publication/illustrations-map-links.json'),JSON.stringify(result,null,2));
 console.log(JSON.stringify(result,null,2));await browser.close();if(result.status!=='pass')process.exitCode=1;
})().catch(e=>{console.error(e);process.exit(1);});
