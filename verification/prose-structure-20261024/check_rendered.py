from pathlib import Path
from urllib.parse import urlsplit,unquote
from datetime import datetime
import hashlib,json,re
from bs4 import BeautifulSoup
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];SITE=ROOT/'site'
read=lambda p:p.read_text(encoding='utf-8');load=lambda p:json.loads(read(p))
data=load(OUT/'layout.json');broken=[];rows=[];cache={}
def soup(path):
 path=path.resolve()
 if path not in cache:cache[path]=BeautifulSoup(read(path),'html.parser')
 return cache[path]
pages=[p for p in SITE.rglob('*.html') if 'site_libs' not in p.parts]
for p in pages:
 s=soup(p)
 for e in s.select('a[href],img[src]'):
  href=e.get('href',e.get('src'));u=urlsplit(href)
  if u.scheme or u.netloc or href.startswith('data:'):continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p.resolve()
  if target.is_dir():target=target/'index.html'
  if not target.exists():broken.append({'page':str(p.relative_to(SITE)),'link':href,'reason':'missing file'})
  elif u.fragment and target.suffix=='.html' and not soup(target).find(id=unquote(u.fragment)):
   broken.append({'page':str(p.relative_to(SITE)),'link':href,'reason':'missing anchor'})
for r in data['chapters']:
 p=SITE/r['url'];s=soup(p);m=s.select_one('main');source=read(ROOT/r['file'])
 ids=[x.lower().replace(':','-') for x in re.findall(r'\{#([^}]+)\}',source) if not x.startswith('ch:')]
 ids +=[x.lower().replace(':','-') for x in re.findall(r'\{\{block:([^}]+)\}\}',source)]
 missing=[i for i in ids if not s.find(id=i)]
 notes=m.select('.publisher-fold-always');images=m.select('figure img')
 row={'chapter':r['chapter'],'missing_ids':missing,'figures':len(images),'tables':len(m.select('table')),'optional_notes':len(notes),'intro_paragraphs_before_first_section':len([e for e in m.children if getattr(e,'name',None)=='p']),'unresolved_markup':'{{block:' in m.get_text() or 'publisher-fold-always' in m.get_text(),'note_content_preserved':len(notes)==source.count('.publisher-fold-always'),'notes_have_no_first_definitions_or_figures':all(not n.select('.definition-term,figure,h1,h2,h3') for n in notes)}
 row['status']='pass' if not missing and row['figures']==r['figures'] and row['tables']==r['tables'] and row['note_content_preserved'] and row['notes_have_no_first_definitions_or_figures'] and not row['unresolved_markup'] and row['intro_paragraphs_before_first_section']>0 else 'fail'
 rows.append(row)
redirect_errors=[]
for old,anchors in load(ROOT/'source-maps/chapter-redirects.json').items():
 for anchor,new in anchors.items():
  if not soup(SITE/'chapters'/new).find(id=anchor):redirect_errors.append((old,anchor,new))
metrics=[]
for before in load(OUT/'baseline-html-metrics.json'):
 main=soup(SITE/before['url']).select_one('main')
 lists=[e for e in main.select('ul,ol') if not e.find_parent('section',class_='footnotes') and not e.find_parent(attrs={'role':'doc-endnotes'})]
 metrics.append({'chapter':before['chapter'],'before':before,'after':{'lists':len(lists),'list_items':sum(len(e.find_all('li',recursive=False)) for e in lists),'definitions':len(main.select('.definition-term'))}})
bad_assets=[]
for rel,digest in load(OUT/'baseline/hashes.json')['assets'].items():
 if hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()!=digest:bad_assets.append(rel)
report={'at':datetime.now().astimezone().isoformat(),'html_pages_checked':len(pages),'rows':rows,'list_and_definition_changes':metrics,'broken_local_links':broken,'redirect_target_errors':redirect_errors,'changed_assets':bad_assets,'status':'pass' if not broken and not redirect_errors and not bad_assets and all(r['status']=='pass' for r in rows) else 'fail'}
(OUT/'rendered-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'pages':len(pages),'chapters':len(rows),'figures':sum(r['figures'] for r in rows),'optional_notes':sum(r['optional_notes'] for r in rows),'added_lists':sum(r['after']['lists']-r['before']['lists'] for r in metrics),'broken_links':broken,'changed_assets':bad_assets,'failed_pages':[r for r in rows if r['status']!='pass']},indent=2))
raise SystemExit(0 if report['status']=='pass' else 1)
