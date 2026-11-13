from pathlib import Path
import json,shutil
p=Path(__file__).resolve().parent
concepts={};sections={};relations=[];sets=[];metadata=[];assumptions=set();descriptions=[]
for name in ['memory','systems','tests']:
 d=json.loads((p/f'concept-judgments-{name}.json').read_text(encoding='utf-8'))
 for concept in d['concepts']:
  old=concepts.get(concept['id'])
  if old:old['aliases']=sorted(set(old.get('aliases',[]))|set(concept.get('aliases',[])))
  else:concepts[concept['id']]=concept
 sections.update(d['sections']);relations.extend(d['relations']);sets.extend(d.get('teaching_sets',[]))
 assumptions.update(d['audience'].get('assumed_concepts',[]));descriptions.append(d['audience']['description'])
 metadata.append({'reviewer_group':name,'evidence':f'review-{name}-stage3.json','judgments':f'concept-judgments-{name}.json'})
result={'audience':{'status':'reviewed','description':' '.join(dict.fromkeys(descriptions)),'assumed_concepts':sorted(assumptions)},'concepts':list(concepts.values()),'sections':sections,'relations':relations,'teaching_sets':sets,'review_metadata':metadata,'formatting_reuse':'footnote-spacing-reuse.json records only blank-line changes after review. Direct reviews also cover the tables and equations omitted by extraction.'}
(p/'concept-judgments-merged.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
shutil.copy2(p/'concept-index.json',p/'concept-index-reviewed-text.json')
print('Merged',len(concepts),'concepts,',len(sections),'sections,',len(relations),'relations.')
