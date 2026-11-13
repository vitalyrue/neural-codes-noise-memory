"""Split complete sections from the frozen sources and keep every stable anchor."""
from pathlib import Path
from datetime import datetime
from collections import Counter
import copy,hashlib,json,re,yaml
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[1]
read=lambda p:p.read_text(encoding='utf-8')
write=lambda p,t:p.write_text(t,encoding='utf-8',newline='\n')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
plan=json.loads(read(OUT/'selected-plan.json'))
replacements=json.loads(read(OUT/'reference-edits.json'))
records=[];redirects={};owners={};assets={}
for p in (ROOT/'assets/approved/visuals').iterdir():
 if p.is_file():assets[p.relative_to(ROOT).as_posix()]=sha(p)
for original in plan['originals']:
 src=Path('content/chapters')/original['file'];text=read(OUT/'baseline'/src)
 metadata=yaml.safe_load(read((OUT/'baseline'/src).with_suffix('.yaml')))
 oldurl=metadata['chapter_id'].lower().replace(':','-')+'.html'
 firstnote=re.search(r'(?m)^\[\^[^\]]+\]:',text)
 body=text[:firstnote.start()].rstrip() if firstnote else text.rstrip()
 notes={m.group(1):m.group(0).strip() for m in re.finditer(r'(?ms)^\[\^([^\]]+)\]:.*?(?=^\[\^[^\]]+\]:|\Z)',text)}
 starts=list(re.finditer(r'(?m)^## (.+?) \{#([^}]+)\}\s*$',body))
 units={m.group(2):body[m.start():starts[i+1].start() if i+1<len(starts) else len(body)].strip() for i,m in enumerate(starts)}
 assert [x for g in original['groups'] for x in g['sections']]==list(units),'Sections must occur once in original order'
 for group in original['groups']:
  dest=Path('content/chapters')/group['file']; url=group['id'].lower().replace(':','-')+'.html'
  newbody='\n\n'.join(units[s] for s in group['sections'])
  edits=[]
  for before,after in replacements.get(original['file'],[]):
   if before in newbody:
    assert newbody.count(before)==1,before
    newbody=newbody.replace(before,after);edits.append({'before':before,'after':after})
  opening='\n\n'.join(group['opening'])
  content=f"# {group['title']} {{#{group['id']}}}\n\n{opening}\n\n{newbody}\n"
  used=set(re.findall(r'\[\^([^\]]+)\]',content))
  assert used<=set(notes),used-set(notes)
  if used:content+='\n'+'\n\n'.join(v for k,v in notes.items() if k in used)+'\n'
  # Chapter references inside footnotes receive their explicitly reviewed correction too.
  for before,after in replacements.get(original['file'],[]):
   if before in content:
    assert content.count(before)==1,before
    content=content.replace(before,after);edits.append({'before':before,'after':after})
  write(ROOT/dest,content)
  meta=copy.deepcopy(metadata);meta['chapter_id']=group['id'];meta['title']=group['title'];meta['purpose']=opening.split('\n\n')[0]
  meta['pedagogical_prerequisites']=group['prerequisites']
  allids=set(re.findall(r'\{#([^}]+)\}',newbody))
  meta['section_list']=[s for s in meta['section_list'] if s['id'] in allids]
  for section in meta['section_list']:
   match=re.search(r'(?m)^#{2,6} .+? \{#'+re.escape(section['id'])+r'\}\s*\n',newbody)
   if match:section['summary']=newbody[match.end():].strip().split('\n\n')[0]
  meta['blocks']=[b for b in meta.get('blocks',[]) if b['placement'] in allids]
  write((ROOT/dest).with_suffix('.yaml'),yaml.safe_dump(meta,allow_unicode=True,sort_keys=False,width=88))
  for key in allids|{b['id'] for b in meta['blocks']}:
   owners[key]={'file':dest.as_posix(),'url':url,'chapter':group['id']}
   if url!=oldurl:redirects.setdefault(oldurl,{})[key.lower().replace(':','-')]=url
  records.append({'chapter':group['id'],'file':dest.as_posix(),'url':'chapters/'+url,'title':group['title'],'original':src.as_posix(),'sections':group['sections'],'opening':group['opening'],'edits':edits,'figures':sum(b['kind']=='figure' for b in meta['blocks']),'tables':sum(b['kind']=='table' for b in meta['blocks'])})

# Update existing explicit links to their section's new page; retain old bookmarks too.
for p in (ROOT/'content/chapters').glob('*.md'):
 text=read(p)
 for oldurl,anchors in redirects.items():
  for anchor,newurl in anchors.items():text=text.replace(oldurl+'#'+anchor,newurl+'#'+anchor)
 write(p,text)
chapterplan=yaml.safe_load(read(OUT/'baseline/plan/chapter-plan.yaml'))
chapterplan['book']['parts'][0]['chapters']=[r['chapter'] for r in records if r['original'].split('/')[-1][:2] in ['01','02','03']]
chapterplan['book']['parts'][1]['chapters']=[r['chapter'] for r in records if r['original'].split('/')[-1][:2] in ['04','05','06']]
write(ROOT/'plan/chapter-plan.yaml',yaml.safe_dump(chapterplan,allow_unicode=True,sort_keys=False,width=88))
write(ROOT/'source-maps/chapter-redirects.json',json.dumps(redirects,indent=2))

# Stable section IDs remain the evidence locations. Only source paths/line pointers move.
terms=yaml.safe_load(read(OUT/'baseline/source-maps/terminology-ledger.yaml'))
seen=set()
def retarget(obj):
 if isinstance(obj,dict):
  if id(obj) in seen:return
  seen.add(id(obj));owner=owners.get(obj.get('guide_location'))
  if owner and str(obj.get('source','')).startswith('content/chapters/'):
   obj['source']=owner['file'];lines=read(ROOT/owner['file']).splitlines()
   matches=[i+1 for i,l in enumerate(lines) if '**'+obj.get('term','')+'**' in l]
   if matches:obj['line']=matches[0]
  for v in obj.values():retarget(v)
 elif isinstance(obj,list):
  for v in obj:retarget(v)
retarget(terms)
write(ROOT/'source-maps/terminology-ledger.yaml',yaml.safe_dump(terms,allow_unicode=True,sort_keys=False,width=88))
visuals=yaml.safe_load(read(OUT/'baseline/source-maps/visual-ledger.yaml'))
for v in visuals.get('visuals',[]):
 owner=owners.get(v.get('placement'));old=v.get('caption_and_alt','')
 if owner:
  v['caption_and_alt']=str(Path(owner['file']).with_suffix('.yaml')).replace('\\','/')
  if v.get('teaching_introduction') and old:v['teaching_introduction']=v['teaching_introduction'].replace(old.replace('.yaml','.md'),owner['file'])
  v['toc_correspondence']=owner['chapter']+', '+v['placement']
write(ROOT/'source-maps/visual-ledger.yaml',yaml.safe_dump(visuals,allow_unicode=True,sort_keys=False,width=88))
report={'at':datetime.now().astimezone().isoformat(),'chapters':records,'owners':owners,'approved_assets':assets,'moved_anchors':sum(len(x) for x in redirects.values()),'limits':'Original section bodies retained except explicit reference edits. Openings replaced or carried according to selected-plan. Scientific reviews of unchanged bodies remain historical.'}
write(OUT/'integration.json',json.dumps(report,indent=2,ensure_ascii=False))
print(json.dumps({'chapters':len(records),'moved_anchors':report['moved_anchors'],'figures':sum(r['figures'] for r in records),'tables':sum(r['tables'] for r in records)}))
