from pathlib import Path
import re,yaml,json
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
read=lambda p:p.read_text(encoding='utf-8')
plan=yaml.safe_load(read(ROOT/'plan/chapter-plan.yaml'))['book']
order=plan['front_matter']+[c for part in plan['parts'] for c in part['chapters']]+plan['appendices']
byid={yaml.safe_load(read(p))['chapter_id']:p.with_suffix('.md') for p in (ROOT/'content/chapters').glob('*.yaml')}
terms=[]
for cid in order:
    p=byid[cid];locus=cid
    for number,line in enumerate(read(p).splitlines(),1):
        h=re.search(r'^#{1,6} .*\{#([^}]+)\}',line)
        if h:locus=h.group(1)
        for term in re.findall(r'\[\*\*([^*]+)\*\*\]\{\.definition-term[^}]*\}',line):
            terms.append({'term':term.rstrip(':'),'source':p.relative_to(ROOT).as_posix(),'line':number,'guide_location':locus})
old=yaml.safe_load(read(ROOT/'source-maps/terminology-ledger.yaml'))
assert [(t['term'],t['source']) for t in terms]==[(t['term'],t['source']) for t in old['first_teaching']]
old['first_teaching']=terms;old['terms']=terms
old['note']='Locations of existing blue teaching terms and glossary entries in the current text. Independent teaching, wording and flow judgments are recorded in verification/teaching-compliance-20261025; markup alone is not evidence of adequate teaching.'
(ROOT/'source-maps/terminology-ledger.yaml').write_text(yaml.safe_dump(old,sort_keys=False,allow_unicode=True,width=88),encoding='utf-8',newline='\n')
print(json.dumps({'definition_locations':len(terms),'distinct_terms':len({t['term'] for t in terms}),'glossary_entries':sum(t['source'].endswith('glossary.md') for t in terms)}))
