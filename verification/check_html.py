"""Check all local HTML targets, fragments, IDs and document assets."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from collections import Counter
from datetime import datetime
import hashlib,json,re,yaml,sys
ROOT=Path(__file__).resolve().parents[1]
SITE=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else ROOT/'site'
assert SITE.is_relative_to(ROOT), 'Check only this project tree'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__(); self.ids=[];self.targets=[];self.math=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and a.get('href'):self.targets.append(('link',a['href']))
  for k in ['src','poster']:
   if a.get(k):self.targets.append(('asset',a[k]))
  if tag=='link' and a.get('href'):self.targets.append(('asset',a['href']))
  if 'math' in a.get('class','').split():self.math+=1
pages={p.resolve():Page(p.read_text(encoding='utf-8')) for p in SITE.rglob('*.html')}
failures=[]; checked=0;external=set()
for p,page in pages.items():
 text=p.read_text(encoding='utf-8')
 if remainders:=re.findall(r'\[\^[^\]\n]+\]',text):
  failures.append(dict(file=str(p.relative_to(ROOT)),type='unresolved_footnote',targets=sorted(set(remainders))))
 for ident,count in Counter(page.ids).items():
  if count>1:failures.append(dict(file=str(p.relative_to(ROOT)),type='duplicate_id',target=ident,count=count))
 for kind,target in page.targets:
  u=urlsplit(target)
  if u.scheme in ('http','https'):external.add(target);continue
  if u.scheme or target.startswith('//'):continue
  q=(SITE/unquote(u.path.lstrip('/')) if u.path.startswith('/') else p.parent/unquote(u.path)).resolve() if u.path else p
  if q.is_dir():q=q/'index.html'
  checked+=1
  if not q.exists():failures.append(dict(file=str(p.relative_to(ROOT)),type='missing_'+kind,target=target));continue
  if u.fragment and q in pages and unquote(u.fragment) not in pages[q].ids:
   failures.append(dict(file=str(p.relative_to(ROOT)),type='missing_fragment',target=target))
footnotes=[]
for src in (ROOT/'content/chapters').glob('*.md'):
 meta=yaml.safe_load(src.with_suffix('.yaml').read_text(encoding='utf-8'))
 slug=meta['chapter_id'].replace(':','-').lower()
 folder={'frontmatter':'frontmatter','appendix':'appendices'}.get(meta['role'],'chapters')
 target=(SITE/folder/(slug+'.html')).resolve()
 if target not in pages:continue
 body=re.sub(r'(?m)^\[\^[^\]]+\]:.*\n?','',src.read_text(encoding='utf-8'))
 # Pandoc emits one note for each call, including repeated calls to one label.
 expected=len(re.findall(r'\[\^([^\]]+)\]',body))
 actual=sum(bool(re.fullmatch(r'fn\d+',i)) for i in pages[target].ids)
 footnotes.append(dict(source=src.name,expected=expected,rendered=actual))
 if expected!=actual:failures.append(dict(file=target.relative_to(ROOT).as_posix(),type='footnote_count',expected=expected,actual=actual))
result=dict(checked_at=datetime.now().astimezone().isoformat(),status='pass' if not failures else 'failed',html_pages=len(pages),local_targets=checked,math_spans=sum(p.math for p in pages.values()),external_urls=len(external),footnotes=footnotes,failures=failures,html_sha256={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in pages})
(ROOT/('verification/publication/html-links.json' if SITE==ROOT/'site' else 'verification/publication/html-links-fixture.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='html_sha256'},indent=2))
raise SystemExit(bool(failures))
