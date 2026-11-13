from pathlib import Path
import json,re,hashlib,datetime,urllib.parse
from bs4 import BeautifulSoup
import yaml
O=Path(__file__).resolve().parent;R=O.parents[1];record=json.loads((O/'integrated.json').read_text(encoding='utf-8'))
# Every prose change is an exact recorded edit; reverse the edits and compare
# with the baseline after normalizing only Windows line endings.
restored={}
for e in reversed(record['edits']):
 key=e['file'];current=restored.get(key,(R/key).read_text(encoding='utf-8'))
 assert current==e['new'],(key,'unrecorded edit')
 restored[key]=e['old']
for key,text in restored.items():assert text==(O/'baseline'/Path(key).name).read_text(encoding='utf-8'),key

rows=[];example_count=0;source_count=0
for p in (R/'site').rglob('*.html'):
 if 'site_libs' in p.parts:continue
 soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
 for el in soup.select('.publisher-worked-calculation'):
  example_count+=1;assert 'publisher-fold-always' in el.get('class',[]),(p,'unfoldable example')
  assert el.find('p').get_text().startswith(('Example:','Calculation and figure'))
  assert len(el.find('p').get_text())<100,(p,'long control label')
 source_count+=len(soup.select('details.publisher-source-figure'))
 if not soup.select('details.publisher-source-figure'):continue
 for a in soup.select('details.publisher-source-figure a[href]'):
  url=urllib.parse.urlparse(a['href'])
  if url.scheme:continue
  target=(p.parent/urllib.parse.unquote(url.path)).resolve()
  assert target.exists(),(p.name,a['href'])
 for el in soup.select('details.publisher-source-figure'):
  assert not el.has_attr('open')
  assert el.find('summary') and len(el.select('figure'))==1,(p,'source control structure')
  assert el.select_one('img[alt]')
 rows.append(dict(page=p.relative_to(R/'site').as_posix(),source_figures=len(soup.select('details.publisher-source-figure'))))
assert example_count==9 and source_count==30,(example_count,source_count)
for f in record['figures']:
 asset=R/'site/assets'/f'{f["html_id"]}.png'
 assert asset.is_file(),asset
 assert hashlib.sha256(asset.read_bytes()).hexdigest()==f['sha256'],asset
 path=R/'content/chapters'/f['chapter'];side=yaml.safe_load(path.with_suffix('.yaml').read_text(encoding='utf-8'))
 html=R/'site/chapters'/(side['chapter_id'].lower().replace(':','-')+'.html')
 soup=BeautifulSoup(html.read_text(encoding='utf-8'),'html.parser')
 target=soup.find(id=f['html_id']);assert target and target.find_parent('details'),(f['block_id'],'anchor outside fold')
result=dict(at=datetime.datetime.now().astimezone().isoformat(),passed=True,examples=example_count,original_figures=source_count,exact_edit_reversal=True,source_assets_hashes_match=True,source_image_and_pdf_links_pass=True,pages=rows)
(O/'checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='pages'}))
