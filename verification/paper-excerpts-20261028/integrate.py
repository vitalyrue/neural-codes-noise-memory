from pathlib import Path
import json,re,hashlib,datetime,html
import yaml
O=Path(__file__).resolve().parent;R=O.parents[1]
def H(p):return hashlib.sha256(p.read_bytes()).hexdigest()
edits=[]
def save_edit(p,old,new,reason):
 assert p.read_text(encoding='utf-8')==old
 edits.append(dict(file=p.relative_to(R).as_posix(),old=old,new=new,reason=reason))
 p.write_text(new,encoding='utf-8',newline='\n')

# Reuse the existing fold behavior. Give each run-in title its own paragraph so
# the control contains the title only, never the calculation's first paragraph.
example_ledger=json.loads((R/'verification/example-panels-20261028/edits.json').read_text(encoding='utf-8'))
for f in example_ledger['files']:
 p=R/'content/chapters'/f['file'];old=p.read_text(encoding='utf-8');new=old
 for e in f['edits']:
  before=e['new'].replace('\r\n','\n');assert new.count(before)==1
  body=e['old'].replace('\r\n','\n')
  if body.startswith('### '):
   title,body=body.split('\n\n',1)
   replacement=title+'\n\n<div class="publisher-worked-calculation publisher-fold-always">\n\n**Calculation and figure**\n\n'+body+'</div>\n\n'
  else:
   body=re.sub(r'^(\*\*Example:.*?\*\*) ',r'\1\n\n',body,count=1)
   replacement='<div class="publisher-worked-calculation publisher-fold-always">\n\n'+body+'</div>\n\n'
  new=new.replace(before,replacement,1)
 save_edit(p,old,new,'Make example foldable; split run-in title from calculation; preserve existing heading and all example text.')

items=[]
for prefix in ['memory','eye','place']:
 data=json.loads((O/f'{prefix}.json').read_text(encoding='utf-8'))
 for x in data.get('figures',data.get('items',[])):
  if prefix=='memory':
   f=dict(x);f['anchor']=f['insert_after_paragraph_start'];f['number']=f['figure'];f['label']='Figure '+f['number']
  else:
   number=x['figure'].replace('Extended Data Figure ','ED').replace('Figure ','')
   f=dict(figure=x['figure'],number=number,label=x['figure'] if prefix=='eye' else 'Figure '+number,source_pdf=x['source_pdf'],source_sha256=x['source_sha256'],pdf_page=x['pdf_page_1based'],crop_rect=x.get('crop_rect_points',x.get('clip_rect_pdf_points')),asset=x['output'],sha256=x['output_sha256'],chapter=Path(x['chapter']).name,anchor=x.get('insertion_anchor_substring',x.get('insertion_anchor_unique_substring')),caption=x['caption_proposal'],alt=x['alt_proposal'],width_inches=6.5,source_label='Ben-Shushan et al. (2022)' if prefix=='eye' else 'Mainali, Azeredo da Silveira, and Burak (2025)')
  # The proposed place Figure1 anchor is in the chapter overview, before a
  # section. Keep the excerpt beside the normalized input model taught in 10.1.
  if prefix=='place' and f['number']=='1':f['anchor']='Here $z$ has variance one'
  f['prefix']=prefix;f['block_id']=f"fig:PAPER-{prefix.upper()}-{f['number'].upper()}";f['html_id']=f['block_id'].lower().replace(':','-')
  assert H(R/f['asset'])==f['sha256'] and H(R/f['source_pdf'])==f['source_sha256']
  items.append(f)
assert len(items)==30

def paragraph_end(text,anchor):
 assert text.count(anchor)==1,anchor
 pos=text.index(anchor);start=text.rfind('\n\n',0,pos)+2
 end=text.find('\n\n',pos);end=len(text) if end<0 else end
 para=text[start:end]
 # Keep an introductory sentence and its following list together. Figures
 # attached to a list item follow the whole list rather than breaking it.
 if para.lstrip().startswith(('- ','1. ')) or para.rstrip().endswith(':'):
  while True:
   next_start=end+2;next_end=text.find('\n\n',next_start)
   if next_end<0:next_end=len(text)
   next_para=text[next_start:next_end]
   if not re.match(r'(?:- |\d+\. )',next_para):break
   end=next_end
 return end

visual=yaml.safe_load((R/'source-maps/visual-ledger.yaml').read_text(encoding='utf-8'))
for chapter in dict.fromkeys(x['chapter'] for x in items):
 p=R/'content/chapters'/chapter;old=p.read_text(encoding='utf-8');new=old
 y=p.with_suffix('.yaml');side=yaml.safe_load(y.read_text(encoding='utf-8'))
 inserts={}
 for f in [a for a in items if a['chapter']==chapter]:
  end=paragraph_end(old,f['anchor']);headings=list(re.finditer(r'^#{2,3} .*?\{#(sec:[^}]+)\}',old[:end],re.M));assert headings
  f['placement']=headings[-1][1]
  summary=f"Original paper figure: {f['source_label']}, {f['label']}"
  caption=f"{f['caption']} Original {f['label']} from {f['source_label']}; exact artwork excerpt. [PDF page {f['pdf_page']}](../papers/{Path(f['source_pdf']).name}#page={f['pdf_page']}). [Open image at full size](../assets/{f['html_id']}.png)."
  side['blocks'].append(dict(id=f['block_id'],kind='figure',placement=f['placement'],asset=f['asset'],caption=caption,alt=f['alt'],width_inches=f['width_inches'],html_fold='never'))
  block='\n\n<details class="publisher-long-content publisher-source-figure">\n<summary>'+html.escape(summary)+'</summary>\n<div class="publisher-fold-body">\n\n{{block:'+f['block_id']+'}}\n\n</div>\n</details>'
  inserts.setdefault(end,[]).append(block)
  visual['visuals'].append(dict(visual_id=f['block_id'],block_id=f['block_id'],asset=f['asset'],sha256=f['sha256'],status='selected',embedded=True,origin='Exact PDF figure artwork excerpt; no generated or redrawn elements',source_status=f"{f['source_label']}, {f['label']}",source_pdf=f['source_pdf'],source_pdf_sha256=f['source_sha256'],source_pdf_page=f['pdf_page'],crop_rect_points=f['crop_rect'],placement=f['placement'],caption_and_alt=y.relative_to(R).as_posix(),caption=caption,accessibility_description=f['alt'],rights='Original paper copyright retained; excerpt included in the user requested private study guide',visual_review=f'verification/paper-excerpts-20261028/{f["prefix"]}.json',teaching_introduction=f['anchor'],interpretation=f['caption'],provenance='Rendered directly from the supplied local paper PDF',toc_correspondence=f['placement']))
 for end,blocks in sorted(inserts.items(),reverse=True):new=new[:end]+''.join(blocks)+new[end:]
 save_edit(p,old,new,'Insert exact original paper figures under expandable source controls after their discussion.')
 y.write_text(yaml.safe_dump(side,allow_unicode=True,sort_keys=False,width=110),encoding='utf-8')
(R/'source-maps/visual-ledger.yaml').write_text(yaml.safe_dump(visual,allow_unicode=True,sort_keys=False,width=110),encoding='utf-8')

# Link figure-specific PDF references to the embedded source figure. The caption
# keeps a direct PDF-page link. Ordinary paper/method citations stay as authored.
for prefix,files in [('memory',['02-memory-dynamics.md','02b-memory-long-delays.md','03-memory-information.md','03b-memory-readout.md']),('eye',['04-eye-drift.md','04b-eye-timing.md','04c-eye-circuit.md']),('place',['05-place-fields.md','05b-place-sizes.md','05c-place-tests.md'])]:
 for name in files:
  p=R/'content/chapters'/name;old=p.read_text(encoding='utf-8');body,sep,footnotes=old.partition('\n[^')
  def replace_link(m):
   label=m[1];num=re.search(r'(?:Fig\.|Figure)\s+(S?\d+)',label)
   if not num:return m[0]
   candidates=[f for f in items if f['prefix']==prefix and f['number']==num[1] and Path(f['source_pdf']).name in m[2]]
   if len(candidates)!=1:return m[0]
   f=candidates[0];side=yaml.safe_load((R/'content/chapters'/f['chapter']).with_suffix('.yaml').read_text(encoding='utf-8'));target=side['chapter_id'].lower().replace(':','-')+'.html#'+f['html_id']
   return '['+label+']('+target+')'
  body=re.sub(r'\[([^\]\n]+)\]\((\.\./papers/[^)]+)\)',replace_link,body)
  new=body+sep+footnotes
  if new!=old:save_edit(p,old,new,'Make figure-specific body links open the embedded excerpt; original PDF remains linked in its caption.')

css=R/'assets/styles/reading.css';text=css.read_text(encoding='utf-8')
text+='\n/* Original paper excerpts use the same accessible disclosure control as examples. */\n.publisher-source-figure { background: #fff; }\n.publisher-source-figure > .publisher-fold-body { padding: 0.65rem 0.85rem; }\n.publisher-source-figure figure { margin-bottom: 0; }\n'
css.write_text(text,encoding='utf-8')
(O/'integrated.json').write_text(json.dumps(dict(at=datetime.datetime.now().astimezone().isoformat(),figures=items,edits=edits),ensure_ascii=False,indent=2),encoding='utf-8')
print('Integrated 30 original paper figures and 9 foldable examples.')
