from pathlib import Path
from datetime import datetime, timezone
import json, hashlib
from playwright.sync_api import sync_playwright

root=Path(__file__).resolve().parent
out=root/'browser';out.mkdir(exist_ok=True)
result={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Two representative served pages; no full figure review','pages':[]}
try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(headless=True)
        page=browser.new_page(viewport={'width':1100,'height':900},device_scale_factor=1)
        base='https://vrdell15.tail8b993e.ts.net/burak/'
        for slug,label in [('frontmatter/ch-reading-guide.html','reading-guide'),('chapters/ch-foundations.html','foundations')]:
            response=page.goto(base+slug,wait_until='domcontentloaded',timeout=30000)
            assert response and response.status==200
            page.wait_for_selector('mjx-container',timeout=20000)
            page.evaluate('async () => { await document.fonts.ready; if(window.MathJax?.startup?.promise) await window.MathJax.startup.promise; }')
            rec={'url':page.url,'status':response.status,'title':page.title(),'body_font_px':page.locator('body').evaluate('(e)=>getComputedStyle(e).fontSize'),'math_containers':page.locator('mjx-container').count()}
            assert rec['body_font_px']=='11.9px',rec
            if label=='reading-guide':
                table=page.locator('#tbl-reading-evidence')
                assert table.count()==1
                rec['table_rows']=table.locator('tr').count()
                assert rec['table_rows']==7,rec
                rec['table_text']=table.inner_text()
                assert all(t in rec['table_text'] for t in ['Burak','Ben-Shushan','Mainali'])
                table.scroll_into_view_if_needed()
                rec['screenshot']='browser/reading-evidence.png'
                page.screenshot(path=str(out/'reading-evidence.png'))
                page.set_viewport_size({'width':733,'height':900})
                rec['mobile_page_width']=page.evaluate('document.documentElement.scrollWidth')
                assert rec['mobile_page_width']<=734,rec
                page.set_viewport_size({'width':1100,'height':900})
            else:
                msd=page.locator('p').filter(has_text='Before comparing simulated motion with theory').first
                assert msd.count()==1
                rec['msd_text']=msd.inner_text()
                assert 'same lag' in rec['msd_text'] and 'Squaring prevents' in rec['msd_text']
                rec['msd_is_in_closed_fold']=msd.evaluate('(e)=>{for(let p=e.parentElement;p;p=p.parentElement){if(p.tagName==="DETAILS"&&!p.open)return true;}return false;}')
                assert not rec['msd_is_in_closed_fold']
                summary=page.locator('summary').filter(has_text='Example:').first
                rec['example_summary']=summary.inner_text()
                details=summary.locator('..')
                assert details.evaluate('(e)=>e.tagName')=='DETAILS'
                rec['example_initially_closed']=not details.evaluate('(e)=>e.open')
                assert rec['example_initially_closed']
                summary.click();assert details.evaluate('(e)=>e.open')
                summary.click();assert not details.evaluate('(e)=>e.open')
                rec['example_open_close']='passed'
                definition=page.locator('.definition-term').first
                rec['definition_color']=definition.evaluate('(e)=>getComputedStyle(e).color')
                assert rec['definition_color']=='rgb(31, 78, 121)',rec
                msd.scroll_into_view_if_needed()
                rec['screenshot']='browser/foundations-msd.png'
                page.screenshot(path=str(out/'foundations-msd.png'))
            result['pages'].append(rec)
        browser.close()
    result['status']='pass'
except Exception as exc:
    result.update(status='failed',error=type(exc).__name__+': '+str(exc))
finally:
    result['completed_utc']=datetime.now(timezone.utc).isoformat()
    result['screenshots']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('*.png')}
    (root/'browser-check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='pages'},ensure_ascii=False))
if result['status']!='pass':raise SystemExit(1)
