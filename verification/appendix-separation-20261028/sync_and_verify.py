"""Synchronize current source metadata without replacing the chapter plan."""
from pathlib import Path
from collections import Counter
import re,json,hashlib,datetime,yaml
r=Path(__file__).resolve().parents[2];o=Path(__file__).resolve().parent
stems=['00-reading-guide','02-memory-dynamics','02b-memory-long-delays','03-memory-information','03b-memory-readout']
changes=[];checks=[]
def para(lines,start):
 out=[]
 for line in lines[start:]:
  if not line.strip():
   if out:break
   continue
  if line.startswith(('#','$$','|','{{','[^')):break
  out.append(line.strip())
 return ' '.join(out)
for stem in stems:
 p=r/'content/chapters'/(stem+'.md');old=(o/'baseline'/(stem+'.md')).read_text(encoding='utf-8');new=p.read_text(encoding='utf-8')
 patterns={'display_equations':r'\$\$[\s\S]*?\$\$','blue_definitions':r'\[\*\*[^*]+\*\*\]\{\.definition-term[^}]*\}','figure_markers':r'\{\{block:fig:[^}]+\}\}','footnote_definitions':r'^\[\^[^\]]+\]:.*$'}
 result={'file':stem+'.md','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 for name,pattern in patterns.items():
  a=Counter(re.findall(pattern,old,re.M));b=Counter(re.findall(pattern,new,re.M));assert a==b,(stem,name);result[name]=sum(b.values())
 oldhead=re.findall(r'^#{1,2} .+$',old,re.M);newhead=re.findall(r'^#{1,2} .+$',new,re.M)
 if stem=='00-reading-guide':
  newhead=[h for h in newhead if '{#sec:READING-MECHANISM-MATH}' not in h]
 assert oldhead==newhead,(stem,'existing headings')
 result['existing_headings_preserved']=True
 side=p.with_suffix('.yaml');data=yaml.safe_load(side.read_text(encoding='utf-8'));lines=new.splitlines()
 for sec in data['section_list']:
  idx=next(i for i,l in enumerate(lines) if re.search(r'\{#'+re.escape(sec['id'])+r'\}\s*$',l))
  summary=para(lines,idx+1)
  if summary != sec['summary']:
   changes.append({'file':side.name,'section':sec['id'],'old':sec['summary'],'new':summary});sec['summary']=summary
 if any(c['file']==side.name for c in changes):
  (o/'metadata-sync.json').write_text(json.dumps(changes,indent=2,ensure_ascii=False),encoding='utf-8')
  side.write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')
 checks.append(result)

p=r/'source-maps/terminology-ledger.yaml';terms=yaml.safe_load(p.read_text(encoding='utf-8'));termchanges=[]
for item in terms['first_teaching']:
 lines=(r/item['source']).read_text(encoding='utf-8').splitlines()
 found=[i+1 for i,l in enumerate(lines) if '[**'+item['term']+'**]{.definition-term' in l]
 if found and item['line']!=found[0]:
  termchanges.append({'term':item['term'],'source':item['source'],'old_line':item['line'],'new_line':found[0]});item['line']=found[0]
(o/'term-line-sync.json').write_text(json.dumps(termchanges,indent=2),encoding='utf-8')
if termchanges:p.write_text(yaml.safe_dump(terms,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')

for stem in stems:
 a=yaml.safe_load((o/'baseline'/(stem+'.yaml')).read_text(encoding='utf-8'));b=yaml.safe_load((r/'content/chapters'/(stem+'.yaml')).read_text(encoding='utf-8'))
 for key in set(a)|set(b):
  if key not in ('section_list','blocks'):assert a.get(key)==b.get(key),(stem,key)
 originalblocks={x['id']:x for x in a['blocks']};currentblocks={x['id']:x for x in b['blocks']}
 for k,v in originalblocks.items():assert currentblocks[k]==v,(stem,k)
 assert set(currentblocks)-set(originalblocks)==({'tbl:READING-APPENDIX'} if stem=='00-reading-guide' else set())
assert (r/'plan/chapter-plan.yaml').read_bytes()==(o/'baseline/chapter-plan.yaml').read_bytes()
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_checks':checks,'chapter_plan_unchanged':True,'existing_block_fields_unchanged':True,'added_reading_guide_section':'sec:READING-MECHANISM-MATH','added_typed_table':'tbl:READING-APPENDIX','updated_section_summaries':len(changes),'updated_first_teaching_lines':len(termchanges)}
(o/'source-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'preservation':'pass','files':len(checks),'display_equations':sum(x['display_equations'] for x in checks),'updated_summaries':len(changes),'updated_term_lines':len(termchanges)}))
