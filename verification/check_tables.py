"""Check every declared reader table against its rendered HTML cells."""
from pathlib import Path
from html.parser import HTMLParser
from datetime import datetime
import hashlib,json,re,yaml
ROOT=Path(__file__).resolve().parents[1]
class Tables(HTMLParser):
 def __init__(self,text):
  super().__init__();self.tables=[];self.depth=0;self.row=None;self.cell=None;self.line_depth=0;self.line_text='';self.line_blocks=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='div' and 'line-block' in a.get('class','').split():self.line_depth=1;self.line_text=''
  elif tag=='div' and self.line_depth:self.line_depth+=1
  if tag=='table':self.tables.append([]);self.depth+=1
  if self.depth and tag=='tr':self.row=[]
  if self.depth and tag in ('th','td'):self.cell=''
 def handle_data(self,data):
  if self.line_depth:self.line_text+=data
  if self.cell is not None:self.cell+=data
 def handle_endtag(self,tag):
  if tag=='div' and self.line_depth:
   self.line_depth-=1
   if self.line_depth==0:self.line_blocks.append(self.line_text)
  if self.depth and tag in ('th','td') and self.cell is not None:self.row.append(self.cell);self.cell=None
  if self.depth and tag=='tr' and self.row is not None:self.tables[-1].append(self.row);self.row=None
  if tag=='table':self.depth-=1
def norm(s):
 s=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m[1].strip()+'$',s,flags=re.S)
 return re.sub(r'\s+',' ',s).translate(str.maketrans({'’':"'",'‘':"'",'–':'-','—':'-'})).strip()
def check_page(html,expected):
 parsed=Tables(html);fail=[]
 if any('|' in s and re.search(r'\|[\s—–:-]+\|',s) for s in parsed.line_blocks):fail.append('flattened pipe table')
 if len(parsed.tables)!=len(expected):fail.append(f'expected {len(expected)} tables, found {len(parsed.tables)}')
 for actual,block in zip(parsed.tables,expected):
  wanted=[block['headers'],*block['rows']]
  if [[norm(s) for s in row] for row in actual]!=[[norm(s) for s in row] for row in wanted]:fail.append('cell mismatch: '+block['id'])
 return fail
# This must reject the specific original failure before its pass counts.
assert 'flattened pipe table' in check_page('<div class="line-block">A | B | |—|—| | one | two |</div>',[])
assert 'cell mismatch: tbl:TEST' in check_page('<table><tr><th>A</th></tr><tr><td>wrong</td></tr></table>',[{'id':'tbl:TEST','headers':['A'],'rows':[['right']]}])
records=[];failures=[];checked_html=set()
for source in sorted((ROOT/'content/chapters').glob('*.md')):
 metadata=yaml.safe_load(source.with_suffix('.yaml').read_text(encoding='utf-8'));expected=[b for b in metadata.get('blocks',[]) if b['kind']=='table']
 folder={'frontmatter':'frontmatter','appendix':'appendices'}.get(metadata['role'],'chapters');slug=metadata['chapter_id'].replace(':','-').lower();p=ROOT/'site'/folder/(slug+'.html')
 errors=check_page(p.read_text(encoding='utf-8'),expected)
 checked_html.add(p.resolve())
 if re.search(r'(?m)^\s*\|[- :|]+\|\s*$',source.read_text(encoding='utf-8')):errors.append('raw reader pipe table remains in source')
 records.append({'source':source.name,'html':p.relative_to(ROOT).as_posix(),'tables':len(expected),'rows':sum(len(b['rows']) for b in expected),'html_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'findings':errors})
 failures.extend({'source':source.name,'finding':e} for e in errors)
for p in (ROOT/'site').rglob('*.html'):
 if p.resolve() in checked_html:continue
 failures.extend({'source':p.relative_to(ROOT).as_posix(),'finding':e} for e in check_page(p.read_text(encoding='utf-8'),[]))
 checked_html.add(p.resolve())
report={'checked_at':datetime.now().astimezone().isoformat(),'status':'pass' if not failures else 'failed','reader_sources':len(records),'html_pages':len(checked_html),'tables':sum(r['tables'] for r in records),'body_rows':sum(r['rows'] for r in records),'records':records,'failures':failures,'planted_flattened_table_and_changed_cell_detected':True}
(ROOT/'verification/publication/all-reader-tables.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='records'},indent=2))
raise SystemExit(bool(failures))
