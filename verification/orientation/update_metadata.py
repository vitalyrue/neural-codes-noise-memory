"""Refresh only the revised frontmatter metadata and first teaching records."""
from pathlib import Path
import datetime,hashlib,json,re,yaml
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'content/chapters/00-reading-guide.md'
text=p.read_text(encoding='utf-8');lines=text.splitlines()
side=p.with_suffix('.yaml');meta=yaml.safe_load(side.read_text(encoding='utf-8'))
meta['title']=re.match(r'^# (.*?) \{#',lines[0])[1]
meta['purpose']=next(x.strip() for x in lines[1:] if x.strip())
sections=[]
for i,line in enumerate(lines):
    m=re.match(r'^(#{2,6}) (.*?) \{#([^}]+)\}$',line)
    if not m:continue
    para=[]
    for following in lines[i+1:]:
        if not following.strip():
            if para:break
            continue
        if following.startswith(('#','$$','[^','{{')):break
        para.append(following.strip())
    sections.append({'id':m[3],'title':m[2],'summary':' '.join(para),'level':len(m[1])})
meta['section_list']=sections
side.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True),encoding='utf-8')

term_path=ROOT/'source-maps/terminology-ledger.yaml'
terms=yaml.safe_load(term_path.read_text(encoding='utf-8'))
baseline_terms=yaml.safe_load((ROOT/'verification/orientation/baseline/terminology-ledger.yaml').read_text(encoding='utf-8'))
moved={}
for term,section in [('fixational drift','sec:READING-EYE'),('place cell','sec:READING-PLACE'),('place field','sec:READING-PLACE'),('diffusion coefficient','sec:READING-SCOPE'),('mean squared displacement','sec:READING-SCOPE')]:
    marker='[**'+term+'**]'
    matches=[i+1 for i,line in enumerate(lines) if marker in line]
    assert len(matches)==1,(term,matches)
    rows=[r for r in terms['first_teaching'] if r['term']==term]
    assert len(rows)==1,term
    prior=next(r for r in baseline_terms['first_teaching'] if r['term']==term)
    moved[term]={'before':dict(prior),'after':{'term':term,'source':'content/chapters/00-reading-guide.md','line':matches[0],'guide_location':section}}
    rows[0].update(moved[term]['after'])
terms['terms']=terms['first_teaching']
term_path.write_text(yaml.safe_dump(terms,sort_keys=False,allow_unicode=True),encoding='utf-8')

original=(ROOT/'verification/orientation/baseline/00-reading-guide.md').read_text(encoding='utf-8')
def sections_of(t):
    out={}
    for match in re.finditer(r'^## (.*?) \{#([^}]+)\}\n(.*?)(?=^## |\Z)',t,re.M|re.S):out[match[2]]=match[3]
    return out
oldsec=sections_of(original);newsec=sections_of(text)
assert newsec['sec:READING-START']==oldsec['sec:READING-START']
assert newsec['sec:READING-PAPERS']==oldsec['sec:READING-PAPERS']
scope_boundary=oldsec['sec:READING-SCOPE'].strip().split('\n\n')[1]
assert scope_boundary in newsec['sec:READING-SCOPE']
record={
 'at':datetime.datetime.now().astimezone().isoformat(),
 'changed_scope':'Frontmatter scientific orientation and its metadata only; earlier detailed chapters, images and tables are untouched.',
 'title':{'before':'Reading path and paper copies','after':meta['title'],'chapter_id':'ch:READING-GUIDE'},
 'original_intro':'Rewritten into the concrete opening and field/problem section; guide derivation scope remains in sec:READING-SCOPE.',
 'retained_sections':list(oldsec),'new_sections':[s['id'] for s in sections if s['id'] not in oldsec],
 'renamed_section':{'id':'sec:READING-SCOPE','before':'What the derivations and examples establish','after':'Scope and notation'},
 'scope_wording':'Example distinctions rewritten in plain words and MSD/t explained; original reproduction and literature-coverage boundary paragraph preserved exactly.',
 'first_teaching_moves':moved,
 'source_evidence':'verification/orientation/source-evidence.md',
 'before_sha256':hashlib.sha256(original.encode()).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
}
(ROOT/'verification/orientation/change-ledger.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps({'sections':len(sections),'first_teaching_moves':list(moved),'reading_paths_papers_and_scope_boundary_preserved':True},indent=2))
