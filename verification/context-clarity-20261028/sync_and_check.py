"""Sync only changed section summaries, then check preserved reader structure."""
from pathlib import Path
import re, json, hashlib, datetime
import yaml
ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
changes, checks = [], []
def para(lines, start):
    result=[]
    for line in lines[start:]:
        if not line.strip():
            if result: break
            continue
        if line.startswith(('#','$$','|','{{','[^')): break
        result.append(line.strip())
    return ' '.join(result)
for p in sorted((ROOT/'content/chapters').glob('*.md')):
    before=(OUT/'baseline/chapters'/p.name).read_text(encoding='utf-8')
    after=p.read_text(encoding='utf-8')
    if before == after: continue
    displays=lambda text: re.findall(r'\$\$[\s\S]*?\$\$',text)
    headings=lambda text: re.findall(r'^#+ .+$',text,re.M)
    definitions=lambda text: re.findall(r'\[\*\*([^*]+)\*\*\]\{\.definition-term[^}]*\}',text)
    for name,fun in [('display_equations',displays),('headings',headings),('blue_definition_terms',definitions)]:
        assert fun(before)==fun(after),(p.name,name)
    data=yaml.safe_load(p.with_suffix('.yaml').read_text(encoding='utf-8'))
    lines=after.splitlines()
    for sec in data['section_list']:
        start=next((i for i,line in enumerate(lines) if re.search(r'\{#'+re.escape(sec['id'])+r'\}\s*$',line)),None)
        assert start is not None,sec['id']
        summary=para(lines,start+1)
        if summary != sec['summary']:
            changes.append(dict(file=str(p.with_suffix('.yaml')),section=sec['id'],old=sec['summary'],new=summary))
            sec['summary']=summary
    checks.append(dict(file=p.name,display_equations=len(displays(after)),headings_preserved=True,blue_definition_terms_preserved=True,sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
    # Preserve all fields; do not infer chapters, prerequisites or blocks.
    if any(x['file']==str(p.with_suffix('.yaml')) for x in changes):
        (OUT/'metadata-sync.json').write_text(json.dumps(changes,indent=2,ensure_ascii=False),encoding='utf-8')
        p.with_suffix('.yaml').write_text(yaml.safe_dump(data,sort_keys=False,allow_unicode=True,width=100),encoding='utf-8')

# Check navigation, artwork metadata, chapter order and dependency fields against baseline.
for p in (ROOT/'content/chapters').glob('*.yaml'):
    before=yaml.safe_load((OUT/'baseline/chapters'/p.name).read_text(encoding='utf-8'))
    after=yaml.safe_load(p.read_text(encoding='utf-8'))
    for key in set(before)|set(after):
        if key not in ('purpose','section_list'): assert before.get(key)==after.get(key),(p.name,key)
    assert [(s['id'],s['title'],s['level']) for s in before['section_list']] == [(s['id'],s['title'],s['level']) for s in after['section_list']]
plan=yaml.safe_load((ROOT/'plan/chapter-plan.yaml').read_text(encoding='utf-8'))
oldplan=yaml.safe_load((OUT/'baseline/chapter-plan.yaml').read_text(encoding='utf-8'))
assert [x['chapters'] for x in plan['book']['parts']]==[x['chapters'] for x in oldplan['book']['parts']]
for p in (ROOT/'content/chapters').glob('*.yaml'):
    assert '[^' not in yaml.safe_load(p.read_text(encoding='utf-8'))['purpose']
report={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'changed_manuscripts':checks,'section_summaries_synchronized':len(changes),'figure_metadata_unchanged':True,'chapter_order_dependencies_unchanged':True,'no_navigation_footnote_markers':True}
(OUT/'source-checks.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'changed_manuscripts':len(checks),'section_summaries_synchronized':len(changes),'preservation_checks':'pass'}))
