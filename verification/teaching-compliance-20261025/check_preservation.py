from pathlib import Path
from datetime import datetime
import json,hashlib,re,yaml
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
edits=load(OUT/'repairs-v1.json')['edits']+load(OUT/'repairs-v2.json')['edits']
checks=[]
def add(name,passed,detail=None):checks.append({'check':name,'pass':bool(passed),'detail':detail})
for rel in sorted({e['file'] for e in edits}):
    text=(OUT/'baseline'/rel).read_text(encoding='utf-8')
    for e in edits:
        if e['file']!=rel:continue
        assert text.count(e['before'])==1,(rel,e.get('id',e.get('finding')))
        text=text.replace(e['before'],e['after'])
    add('All differences explained by exact reviewed edits: '+rel,text==(ROOT/rel).read_text(encoding='utf-8'))
for p in sorted((ROOT/'content/chapters').glob('*.md')):
    before=(OUT/'baseline/content/chapters'/p.name).read_text(encoding='utf-8');after=p.read_text(encoding='utf-8')
    add('Headings and stable IDs preserved: '+p.name,re.findall(r'^#{1,6} .+$',before,re.M)==re.findall(r'^#{1,6} .+$',after,re.M))
    add('Typed figure/table positions retained: '+p.name,re.findall(r'\{\{block:[^}]+\}\}',before)==re.findall(r'\{\{block:[^}]+\}\}',after))
    add('Optional folds retained: '+p.name,before.count('.publisher-fold-always')==after.count('.publisher-fold-always'))
before_assets=load(OUT/'baseline/hashes.json')['assets']
changed=[rel for rel,h in before_assets.items() if sha(ROOT/rel)!=h]
add('Only approved map assets changed',set(changed)=={'assets/approved/visuals/foundations-paper-map.png','assets/approved/visuals/foundations-paper-map.svg'},changed)
for rel in ['publisher-lock.yaml','skill-lock.yaml','plan/chapter-plan.yaml','guide-project.yaml']:
    add('Existing tooling and reading order retained: '+rel,sha(ROOT/rel)==sha(OUT/'baseline'/rel))
for p in sorted((ROOT/'content/chapters').glob('*.yaml')):
    old=yaml.safe_load((OUT/'baseline/content/chapters'/p.name).read_text(encoding='utf-8'))
    new=yaml.safe_load(p.read_text(encoding='utf-8'))
    add('Typed table contents preserved: '+p.name,[b for b in old.get('blocks',[]) if b['kind']=='table']==[b for b in new.get('blocks',[]) if b['kind']=='table'])
report={'at':datetime.now().astimezone().isoformat(),'status':'pass' if all(c['pass'] for c in checks) else 'fail','recorded_edits':len(edits),'checks':checks,'scope':'Exact-edit replay, stable structure and asset preservation. No inference of teaching quality from these mechanical checks.'}
(OUT/'preservation-check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'recorded_edits':len(edits),'failed':[c for c in checks if not c['pass']]}))
raise SystemExit(0 if report['status']=='pass' else 1)
