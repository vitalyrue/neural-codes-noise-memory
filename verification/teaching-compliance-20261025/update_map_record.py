from pathlib import Path
from datetime import datetime
import json,yaml,hashlib
from book_runtime.release_audit import load_book
from book_runtime.visual_review import context_hash,policy_hash,review_input_paths,validate_visual_review
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
report=json.loads((OUT/'stage3-memory.json').read_text(encoding='utf-8'));m=report['map_criterion_review'];criteria={c['criterion']:c for c in m['criteria']}
p=ROOT/'source-maps/visual-ledger.yaml';ledger=yaml.safe_load(p.read_text(encoding='utf-8'));v=next(x for x in ledger['visuals'] if x['visual_id']==m['asset_id'])
assert sha(ROOT/v['asset'])==m['png_sha256']
assert sha(ROOT/v['vector_source'])==m['svg_sha256']
assert sha(ROOT/'content/chapters/01b-persistence.md')==m['chapter_md_sha256']
assert sha(ROOT/'content/chapters/01b-persistence.yaml')==m['chapter_yaml_sha256']
meta=yaml.safe_load((ROOT/'content/chapters/01b-persistence.yaml').read_text(encoding='utf-8'))
block=next(b for b in meta['blocks'] if b['id']==m['asset_id'])
assert hashlib.sha256(block['caption'].encode()).hexdigest()==m['caption_sha256']
v['sha256']=m['png_sha256'];v['content_review']=v['visual_review']='verification/teaching-compliance-20261025/stage3-memory.json'
v['review_contract']['source_files']=['content/chapters/01b-persistence.md','content/chapters/01b-persistence.yaml','plan/chapter-plan.yaml','verification/illustrations/draw_orientation.py','verification/illustrations/figure_style.py']
v['review_contract']['palette_audit']='verification/teaching-compliance-20261025/map-candidate/V01/qa.json'
scenes=[]
old_scenes=v['diagram_review']['checks']['visual_explanation']['scenes']
for scene,label in zip(old_scenes,['time scene','eye pathway scene','fixed spatial scene']):
    scenes.append({**scene,'relationship':criteria[label]['reason'],'teaching_contribution':criteria[label]['why_objection_fails']})
def evidence(label):return [criteria[label]['reason'],criteria[label]['why_objection_fails'],'Current independent criterion record: verification/teaching-compliance-20261025/stage3-memory.json, map_criterion_review.']
book=load_book(ROOT/'guide-project.yaml');chapter=next(c for part in book.parts for c in part.chapters if c.chapter_id=='ch:PERSISTENCE')
v['diagram_review']={'schema_version':1,'status':'approved','reviewer':'/root/compliance_memory','reviewed_sha256':m['png_sha256'],'policy_sha256':policy_hash(),'context_sha256':context_hash(v),'input_sha256':{name:sha(ROOT/name) for name in review_input_paths(v['review_contract'])},'source_scope_sha256':{'ch:PERSISTENCE':chapter.content_hash},'strongest_objection':criteria['eye pathway scene']['strongest_objection'],'objection_resolution':criteria['eye pathway scene']['why_objection_fails'],'checks':{'technical_accuracy':{'verdict':'pass','evidence':evidence('technical and navigation')},'visual_explanation':{'verdict':'pass','evidence':[criteria[k]['reason'] for k in ['time scene','eye pathway scene','fixed spatial scene']],'reference_comparison':None,'scenes':scenes},'readability':{'verdict':'pass','evidence':evidence('full-size readability')+evidence('700px readability'),'full_size_inspected':True,'reviewed_width_px':700},'palette':{'verdict':'pass','evidence':evidence('palette and contrast')},'coverage':{'verdict':'not-applicable','evidence':evidence('opening coverage'),'covered_ids':[],'visible_evidence':{}}}}
findings=validate_visual_review(v,ROOT)
assert not findings,findings
p.write_text(yaml.safe_dump(ledger,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8',newline='\n')
result={'at':datetime.now().astimezone().isoformat(),'status':'pass','figure':v['visual_id'],'independent_evidence':v['visual_review'],'findings':findings,'historical_ledger':'verification/teaching-compliance-20261025/baseline/source-maps/visual-ledger.yaml','limits':'Only the changed paper-map record is refreshed using its actual current independent review. Other historical diagram records are not silently rebound.'}
(OUT/'map-ledger-check.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
