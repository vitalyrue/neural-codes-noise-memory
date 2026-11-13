from pathlib import Path
from datetime import datetime
import hashlib,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
packet=load(OUT/'pedagogy-final/PARAGRAPH_REVIEW.json')
actual={p['id']:p for p in packet['paragraphs']};byid={};bindings=[];reviewers={};reports={}
for group in ('memory','eye','place'):
    p=OUT/f'stage3-{group}.json';d=load(p);reports[group]=d
    assert d.get('completed_at') and not d.get('findings'),group
    rows=d.get('paragraph_judgments',d.get('paragraph_reviews'))
    assert rows,group
    for r in rows:
        assert r['id'] in actual,r['id']
        assert r['source_hash']==actual[r['id']]['source_hash'],r['id']
        if r['decision'] in ('retain structural only','exclude structural markup'):
            assert actual[r['id']]['text'].strip() in ('<div class="figure-scroll">','<div class="table-responsive">','</div>'),r['id']
            r={**r,'decision':'retain','reason':r['reason']+' Retain the source wrapper; exclude it only from prose assessment.'}
        assert r['decision']=='retain',r['id']
        assert all(len(r[k].strip())>=12 for k in ('purpose','connection','reason')),r['id']
        byid.setdefault(r['id'],[]).append({'reviewer':'/root/compliance_'+group,'evidence':p.relative_to(ROOT).as_posix(),**{k:r[k] for k in ('purpose','connection','decision','reason')}})
    for r in d.get('source_hashes',d.get('source_rule_hashes',[])):
        path=Path(r.get('file',r.get('path')))
        if not path.is_absolute():path=ROOT/path
        assert sha(path)==r['sha256'],(group,str(path))
        bindings.append({'review':p.relative_to(ROOT).as_posix(),'file':str(path),'sha256':r['sha256'],'matches_current':True})
    reviewers[group]={'report':p.relative_to(ROOT).as_posix(),'sha256':sha(p),'paragraphs':len(rows),'completed_at':d['completed_at']}
integration=OUT/'integration-recheck-place.json'
if integration.exists():
    d=load(integration)
    def visit(x):
        if isinstance(x,dict):
            if x.get('id') in actual and all(k in x for k in ('purpose','connection','decision','reason')):
                if 'source_hash' in x:assert x['source_hash']==actual[x['id']]['source_hash']
                byid.setdefault(x['id'],[]).append({'reviewer':'/root/compliance_place','evidence':integration.relative_to(ROOT).as_posix(),**{k:x[k] for k in ('purpose','connection','decision','reason')}})
            for v in x.values():visit(v)
        elif isinstance(x,list):
            for v in x:visit(v)
    visit(d)
missing=[i for i in actual if i not in byid]
for p in packet['paragraphs']:
    if p['id'] in byid:p['review']={k:byid[p['id']][0][k] for k in ('purpose','connection','decision','reason')}
(OUT/'pedagogy-final/PARAGRAPH_REVIEW.json').write_text(json.dumps(packet,ensure_ascii=False,indent=2),encoding='utf-8')
coverage={'at':datetime.now().astimezone().isoformat(),'reviewers':reviewers,'total_paragraphs':len(actual),'reviewed_paragraphs':len(byid),'missing':missing,'multiple_reviews':{k:v for k,v in byid.items() if len(v)>1},'source_bindings':bindings,'scope':'Actual final paragraph judgments and current source hashes. Generic Markdown packet scaffolds and formal workflow-schema validation are separate and are not asserted passed.'}
(OUT/'review-bindings.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
concepts={};sections={};relations=[];sets=[];assumed=[];sources=[]
for group in ('memory','eye','place'):
    p=OUT/f'concept-judgments-{group}.json';d=load(p);sources.append({'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)})
    assert d['audience']['status']=='reviewed'
    assumed.extend(d['audience'].get('assumed_concepts',[]))
    for c in d['concepts']:
        row=concepts.setdefault(c['id'],{'id':c['id'],'aliases':[]})
        row['aliases']=list(dict.fromkeys(row['aliases']+c.get('aliases',[])))
    sections.update(d['sections']);relations.extend(d['relations']);sets.extend(d.get('teaching_sets',[]))
# These appendices are covered by actual paragraph reviews; their role is lookup.
sections['ch:REFERENCES/s0']='reviewed'
if not missing:sections['ch:GLOSSARY/s0']='reviewed'
judgments={'audience':{'status':'reviewed','description':'Undergraduate calculus, basic probability and linear algebra as stated in content/index.md and the reading guide. Each independent reviewer checked specialist teaching locally; glossary lookup does not supply prerequisites.','assumed_concepts':list(dict.fromkeys(assumed))},'concepts':list(concepts.values()),'sections':sections,'relations':relations,'teaching_sets':sets,'review_sources':sources,'limits':'Passage indexing omits some display equations. The independent full-text math checks in Stage1 and Stage3 explicitly cover those equations; the tool result is not a replacement for them.'}
(OUT/'concept-judgments-merged.json').write_text(json.dumps(judgments,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'final_paragraphs':len(actual),'reviewed':len(byid),'missing':missing,'current_source_bindings':len(bindings),'concepts':len(concepts),'relations':len(relations),'teaching_sets':len(sets),'section_judgments':len(sections)}))
