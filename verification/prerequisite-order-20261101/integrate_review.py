from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,yaml
from book_runtime.compiler.loader import load_book
from book_runtime.release_audit import build_structure_lock,write_structure_lock

root=Path(__file__).resolve().parents[2];task=Path(__file__).resolve().parent
packet=json.loads((task/'concept-index-final.json').read_text(encoding='utf-8'))
merged={'audience':{'status':'reviewed','description':'Undergraduate calculus and basic linear algebra; ordinary expectation, variance, standard deviation and probability density are assumed. Neuroscience, specialized stochastic tools and each model-specific symbol must be taught in the reader path. User explicitly excluded elementary probability re-teaching.','assumed_concepts':[]},'concepts':[],'sections':{},'relations':[],'teaching_sets':[]}
for group in ['memory','observations','hardware-sim']:
    review=json.loads((task/f'stage3-{group}.json').read_text(encoding='utf-8'))
    status=str(review.get('status',review.get('verdict',''))).lower()
    assert 'pass' in status or status.startswith('no pending prerequisite-order'),(group,status)
    data=json.loads((task/f'concept-judgments-{group}.json').read_text(encoding='utf-8'))
    for key in ['concepts','relations','teaching_sets']:merged[key].extend(data.get(key,[]))
    for key,value in data.get('sections',{}).items():
        assert key not in merged['sections'],key
        merged['sections'][key]=value
    merged['audience']['assumed_concepts'].extend(data.get('audience',{}).get('assumed_concepts',[]))
merged['audience']['assumed_concepts']=sorted(set(merged['audience']['assumed_concepts']))
for section in packet['sections']:
    if section['chapter_id'] in ['ch:GLOSSARY','ch:REFERENCES']:
        merged['sections'][section['id']]='reviewed'
assert len(merged['sections'])==len(packet['sections'])
merged['review_scope']='Whole-book prerequisite order for the inspected concepts and actual reading path. Display equations were directly read by reviewers but are omitted by the extractor. This is not a fresh scientific/figure/release audit of every existing claim.'
(task/'concept-judgments-merged.json').write_text(json.dumps(merged,indent=2),encoding='utf-8')

# Root's overall comparison, plus reference material that has no teaching dependencies.
global_review={'reviewer':'/root','at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Book/Part purposes, chapter boundaries, landing text, glossary and reference-list role; integration of three independent prerequisite diagnoses and final connected reading checks.',
 'reading_path':['Physical spikes, muscles and recurrent dynamics -> coding and variability -> stability -> diffusion -> information -> readout','Recorded eye motion -> movement/noise inference -> proposed circuit; spatial map model -> size laws -> shape tests -> synthesis','Physical electronic states -> feedback/errors -> implementations -> measurement protocol','Each paper model -> its simulation method -> shared numerical and reproduction checks'],
 'alternative_considered':'Part IV simulations could be read before Part III hardware because it mainly depends on Parts I and II. That alternative does not remove a missing prerequisite. Retaining the current Part order preserves the accepted guide and keeps the original-paper simulation methods together.',
 'repair_choice':'Move short essential definitions/results to the visible first teaching location and supply symbol roles before the dependent equation. Full derivations remain at their current topic and folded where optional. No chapter reordering is needed.',
 'backmatter':'Glossary entries are explicitly lookup after main teaching, not substitutes for prerequisite explanations. References are source citations rather than a forward calculation. Root read both appendices and their sidecars; no independent reasoning requiring earlier glossary entries occurs there.',
 'no_remaining_prerequisite_finding_in_reviewed_scope':True,'limits':'No image-pixel audit, original simulation rerun, new SOTA literature review or whole-book truth acceptance. The broad release and figure holds remain.'}
(task/'global-reading-review.json').write_text(json.dumps(global_review,indent=2),encoding='utf-8')

# Refresh the term-location index for the definitions actually moved or clarified.
p=root/'source-maps/terminology-ledger.yaml';terms=yaml.safe_load(p.read_text(encoding='utf-8'))
locations={'Brownian motion':('01b-persistence.md','sec:FOUNDATIONS-DIFFUSION'),
 'likelihood':('03-memory-information.md','sec:MEMORY-FI'),
 'hyperbolic cotangent':('03b-memory-readout.md','sec:MEMORY-IDEAL'),
 'White noise':('03b-memory-readout.md','sec:MEMORY-EXTENSIONS'),
 'Gaussian process':('05-place-fields.md','sec:PLACE-GP'),
 'jointly Gaussian vector':('05-place-fields.md','sec:PLACE-GP'),
 'random seed':('12-simulating-eye-drift.md','sec:SIMULATING-EYE-PATH')}
seen=set()
for key in ['first_teaching','terms']:
    rows=terms[key]
    if id(rows) in seen:continue
    seen.add(id(rows))
    for term,(filename,section) in locations.items():
        path='content/chapters/'+filename
        line=next(i for i,s in enumerate((root/path).read_text(encoding='utf-8').splitlines(),1) if '**'+term+'**' in s)
        matches=[x for x in rows if x.get('term')==term and x.get('source')!='content/chapters/glossary.md']
        record={'term':term,'source':path,'line':line,'guide_location':section}
        if matches:
            for match in matches:match.update(record)
        else:rows.append(record)
p.write_text(yaml.safe_dump(terms,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8',newline='\n')

# Preserve every accepted outline item. Only the content/model hash changes.
book=load_book(root/'guide-project.yaml')
old=yaml.safe_load((task/'baseline/plan/structural-locks/current.yaml').read_text(encoding='utf-8'))
new=build_structure_lock(book)
old.pop('book_model_hash',None);new.pop('book_model_hash',None)
assert old==new,'Outline or sidecar structure changed unexpectedly'
write_structure_lock(root/'guide-project.yaml','plan/structural-locks/current.yaml')
changes=yaml.safe_load((root/'plan/change-ledger.yaml').read_text(encoding='utf-8'))
changes['changes'].append({'date':'2026-11-01','scope':'Whole-guide prerequisite-order repair','disposition':'moved and clarified within existing sections','details':'verification/prerequisite-order-20261101/change-ledger.json','repair_details':'verification/prerequisite-order-20261101/stage2-repairs.json','retained':'All chapter/section IDs and titles, Part/chapter order, sidecars, equations other than equivalent notation explanations, source assets, typography and print rules.','reason':'Required definitions and results must be available before the main reading path depends on them.','review':'verification/prerequisite-order-20261101/stage3-memory.json; stage3-observations.json; stage3-hardware-sim.json'})
(root/'plan/change-ledger.yaml').write_text(yaml.safe_dump(changes,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8',newline='\n')
manifest=json.loads((task/'baseline-hashes.json').read_text(encoding='utf-8'))
changed={name:{'before':digest,'after':hashlib.sha256((root/name).read_bytes()).hexdigest()} for name,digest in manifest.items() if hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest}
(task/'final-source-changes.json').write_text(json.dumps(changed,indent=2),encoding='utf-8')
(task/'preservation.json').write_text(json.dumps({'at_utc':datetime.now(timezone.utc).isoformat(),'outline_identical_except_model_hash':True,'all_sidecars_unchanged':all(not n.startswith('content/chapters/') or not n.endswith('.yaml') for n in changed),'changed_files':list(changed),'book_model_hash':book.content_hash()},indent=2),encoding='utf-8')
print(f'Integrated {len(merged["sections"])} sections, {len(merged["concepts"])} concepts and {len(merged["relations"])} relations. Outline unchanged.')
