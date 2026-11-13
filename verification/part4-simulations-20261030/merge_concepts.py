from pathlib import Path
import json,shutil
p=Path(__file__).resolve().parent
concepts={};sections={};relations=[];sets=[];metadata=[];assumptions=set();descriptions=[]
for name in ['memory','eye','place']:
 d=json.loads((p/f'concept-judgments-{name}.json').read_text(encoding='utf-8'))
 for concept in d['concepts']:
  old=concepts.get(concept['id'])
  if old:old['aliases']=sorted(set(old.get('aliases',[]))|set(concept.get('aliases',[])))
  else:concepts[concept['id']]=concept
 sections.update(d['sections']);relations.extend(d['relations']);sets.extend(d.get('teaching_sets',[]))
 assumptions.update(d['audience'].get('assumed_concepts',[]));descriptions.append(d['audience']['description'])
 metadata.append({'reviewer_group':name,'evidence':f'review-{name}-stage3.json','judgments':f'concept-judgments-{name}.json'})
ambiguous={'elementary_probability':{'expectation','variance','standard deviation','probability density'},'topology':{'betti numbers','euler characteristic'},'spatial_covariance':{'covariance'}}
for cid,aliases in ambiguous.items():
 if cid in concepts:concepts[cid]['aliases']=[a for a in concepts[cid].get('aliases',[]) if a.lower() not in aliases]
result={'audience':{'status':'reviewed','description':' '.join(dict.fromkeys(descriptions)),'assumed_concepts':sorted(assumptions)},'concepts':list(concepts.values()),'sections':sections,'relations':relations,'teaching_sets':sets,'review_metadata':metadata,'coverage_limits':'Direct independent reviews also cover tables, equations and footnotes omitted by extraction. Earlier chapter knowledge is identified as an assumed reading baseline, not newly accepted here.'}
(p/'concept-judgments-merged.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
shutil.copy2(p/'concept-packet-final.json',p/'concept-packet-reviewed-text.json')
print('Merged',len(concepts),'concepts,',len(sections),'sections,',len(relations),'relations.')
