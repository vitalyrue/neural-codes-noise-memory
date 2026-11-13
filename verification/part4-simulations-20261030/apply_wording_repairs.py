from pathlib import Path
from datetime import datetime, timezone
import json, re, yaml

task=Path(__file__).resolve().parent
root=task.parents[1]
records=[]
texts={}
def edit(path,before,after,reason,expected=1):
    p=root/path
    t=texts.get(p,p.read_text(encoding='utf-8'))
    assert t.count(before)==expected,(path,t.count(before),before[:100])
    texts[p]=t.replace(before,after)
    records.append(dict(file=path,before=before,after=after,reason=reason))

place=json.loads((task/'review-place-stage2.json').read_text(encoding='utf-8'))
memory=json.loads((task/'review-memory-stage2.json').read_text(encoding='utf-8'))
eye=json.loads((task/'review-eye-stage2.json').read_text(encoding='utf-8'))
planpath=root/'plan/chapter-plan.yaml'
plan=yaml.safe_load(planpath.read_text(encoding='utf-8'))
for i,p in enumerate(place['proposals']):
    if i>=18:
        edit('content/chapters/13-simulating-place-fields.md',p['original'],p['replacement'],p['reason'])
    elif i not in [9,11]:
        count=0
        for part in plan['book']['parts']:
            if p['original'] in part['purpose']:
                count+=1; part['purpose']=part['purpose'].replace(p['original'],p['replacement'])
            for block in part.get('content',[]):
                if p['original'] in block.get('text',''):
                    count+=1;block['text']=block['text'].replace(p['original'],p['replacement'])
        assert count>0,(i,p['location'])
        records.append(dict(file='plan/chapter-plan.yaml',before=p['original'],after=p['replacement'],reason=p['reason'],occurrences=count))

for p in memory['paragraph_replacements']:
    edit('content/chapters/11-simulating-memory.md',p['before'],p['after'],p['reason'])
for p in eye['replacements']:
    edit('content/chapters/'+p['file'],p['old_paragraph'],p['new_paragraph'],p['why'])

part=plan['book']['parts'][0]
link='[Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109)'
for block in part['content']:
    for a,b in [(' supplies',' supply'),(' derives',' derive'),(' explains',' explain'),(' relates',' relate')]:
        block['text']=block['text'].replace(link+a,link+b)
    block['text']=block['text'].replace('background; Chapters','background. Chapters').replace('information results; Chapters','information results. Chapters').replace('Poisson network model; [','Poisson network model. [').replace(link+'; the two-variable',link+'. The two-variable')
part['purpose']=part['content'][0]['text']
records.append(dict(file='plan/chapter-plan.yaml',reason='Memory Stage 2 Part I author-verb agreement and specified sentence splits; top-level central source derives retained.'))

for p,t in texts.items(): p.write_text(t,encoding='utf-8')
planpath.write_text(yaml.safe_dump(plan,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')

# Keep existing IDs, dependencies and table blocks. Refresh only duplicated prose.
for name in ['11-simulating-memory','12-simulating-eye-drift','13-simulating-place-fields','14-simulation-tools']:
    md=root/'content/chapters'/f'{name}.md'; yp=md.with_suffix('.yaml')
    t=md.read_text(encoding='utf-8');d=yaml.safe_load(yp.read_text(encoding='utf-8'))
    d['purpose']=t.split('\n\n')[1]
    for m in re.finditer(r'^## (.+?) \{#(sec:[^}]+)\}\n\n',t,re.M):
        s=next(s for s in d['section_list'] if s['id']==m[2]);s['summary']=t[m.end():].split('\n\n')[0]
    yp.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=108),encoding='utf-8')

(task/'wording-repairs.json').write_text(json.dumps(dict(applied_at=datetime.now(timezone.utc).isoformat(),changes=records),ensure_ascii=False,indent=2),encoding='utf-8')

# Repair the evidence record accidentally overwritten by a later description variable.
cp=task/'content-changes.json'
if cp.exists():
    d=json.loads(cp.read_text(encoding='utf-8'))
    d['source_correction']={'file':'content/chapters/02-memory-dynamics.md','change':'Replaced the claim of an independent, unconfirmed Eq. 2 correction with the authors\' official 2017 correction. Equation unchanged. Other guide source checks remain separate.','doi':'10.1073/pnas.1706051114'}
    cp.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Applied',len(records),'reviewed wording repairs and synchronized sidecars.')
