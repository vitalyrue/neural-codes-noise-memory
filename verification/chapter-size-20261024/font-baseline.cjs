const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const page=await browser.newPage(); const rows=[];
 for(const width of [878,390]){
  await page.setViewportSize({width,height:816});
  await page.goto('http://127.0.0.1:8765/guide/site/chapters/ch-foundations.html',{waitUntil:'networkidle'});
  for(const media of ['screen','print']){
   await page.emulateMedia({media});
   rows.push({width,media,sizes:await page.evaluate(()=>Object.fromEntries(['html','body','main p','main h1','main h2','main figcaption','main summary','#quarto-sidebar','.sidebar-title','mjx-container'].map(s=>{
    const e=document.querySelector(s),c=e&&getComputedStyle(e);return [s,c?{size:c.fontSize,line:c.lineHeight,color:c.color}:null];
   })))});
  }
  await page.emulateMedia({media:'screen'});
 }
 await browser.close();fs.writeFileSync(__dirname+'/font-baseline.json',JSON.stringify(rows,null,2));console.log(JSON.stringify(rows,null,2));
})();
