from pathlib import Path
from urllib.parse import urlsplit,unquote
from datetime import datetime
import json,re
from bs4 import BeautifulSoup
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];SITE=ROOT/'site'
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
layout=load(ROOT/'verification/prose-structure-20261024/layout.json')
cache={};broken=[];rows=[];targets=0
def soup(p):
    p=p.resolve()
    if p not in cache:cache[p]=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    return cache[p]
pages=[p for p in SITE.rglob('*.html') if 'site_libs' not in p.parts]
for p in pages:
    s=soup(p)
    for e in s.select('a[href],img[src]'):
        href=e.get('href',e.get('src'));u=urlsplit(href)
        if u.scheme or u.netloc or href.startswith('data:'):continue
        targets+=1;t=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
        if t.is_dir():t=t/'index.html'
        if not t.exists():broken.append({'page':p.relative_to(SITE).as_posix(),'link':href,'reason':'file missing'})
        elif u.fragment and t.suffix=='.html' and not soup(t).find(id=unquote(u.fragment)):
            broken.append({'page':p.relative_to(SITE).as_posix(),'link':href,'reason':'anchor missing'})
for r in layout['chapters']:
    s=soup(SITE/r['url']);m=s.select_one('main');text=(ROOT/r['file']).read_text(encoding='utf-8')
    ids=[v.lower().replace(':','-') for v in re.findall(r'\{#([^}]+)\}',text) if not v.startswith('ch:')]
    ids +=[v.lower().replace(':','-') for v in re.findall(r'\{\{block:([^}]+)\}\}',text)]
    folds=m.select('.publisher-fold-always')
    checks={'ids_present':all(s.find(id=v) for v in ids),'figures':len(m.select('figure img'))==r['figures'],'tables':len(m.select('table'))==r['tables'],'folds':len(folds)==text.count('.publisher-fold-always'),'first_definitions_visible':all(not n.select('.definition-term,figure,h1,h2,h3') for n in folds),'opening_present':any(getattr(e,'name',None)=='p' for e in m.children),'markup_resolved':'{{block:' not in m.get_text(),'no_error_markup':not m.select('mjx-merror,.MathJax_Error')}
    rows.append({'chapter':r['chapter'],'checks':checks,'figures':len(m.select('figure img')),'tables':len(m.select('table')),'folds':len(folds),'pass':all(checks.values())})
redirect_errors=[]
for old,anchors in load(ROOT/'source-maps/chapter-redirects.json').items():
    for anchor,new in anchors.items():
        if not soup(SITE/'chapters'/new).find(id=anchor):redirect_errors.append((old,anchor,new))
report={'at':datetime.now().astimezone().isoformat(),'status':'pass' if not broken and not redirect_errors and all(r['pass'] for r in rows) else 'fail','html_pages':len(pages),'local_targets':targets,'chapters':rows,'broken_links':broken,'redirect_errors':redirect_errors,'scope':'Rendered structure and local targets across the HTML output; this is not a whole-book pixel inspection.'}
(OUT/'rendered-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'pages':len(pages),'local_targets':targets,'figures':sum(r['figures'] for r in rows),'tables':sum(r['tables'] for r in rows),'folds':sum(r['folds'] for r in rows),'broken_links':broken,'failed':[r for r in rows if not r['pass']]}))
raise SystemExit(0 if report['status']=='pass' else 1)
