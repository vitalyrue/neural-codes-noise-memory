from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,re,yaml
root=Path(__file__).resolve().parents[2]
folder=Path(__file__).resolve().parent
record=json.loads((folder/'edits-routes-methods.json').read_text(encoding='utf-8'))
extra=[]
def add(path,old,new,reason,source):
    extra.append(dict(path=path,original=old,replacement=new,reason=reason,source=source,recorded_before_edit_utc=datetime.now(timezone.utc).isoformat()))
path='content/chapters/00-reading-guide.yaml'
add(path,
'Recurrent weights couple synaptic activations to firing rates. Random spikes renew activation and disturb the represented coordinate.',
'Synaptic activations $s_i$ set rates $r_i=\\phi(\\sum_j W_{ij}s_j+b_i)$ through weights $W_{ij}$ and constant inputs $b_i$. Spikes renew activation and disturb the represented coordinate.',
'C3: include the central interaction equation with its variable roles in the evidence map.',
'Burak and Fiete main Eqs.7–9, PDF p.5.')
add(path,
'Two neural populations produce an internal eye-position command. Motor spikes, muscles, and delayed feedback connect it to actual eye angle.',
'Two neural populations produce command $E_{\\mathrm{OI}}$. Motor spikes, muscles, and delayed feedback connect it to actual eye angle $E$. The two angles are different signals.',
'C3: identify the command and measured-angle variables.',
'Ben-Shushan main Eqs.23–34, PDF pp.10–11.')
add(path,
'Each cell receives a smooth Gaussian spatial input function. Thresholding gives its active regions; the map itself is fixed during analysis.',
'Cell $i$ receives smooth Gaussian input $h_i(\\mathbf x)$ at position $\\mathbf x$. Activity occurs above a threshold; the spatial map is fixed during analysis.',
'C3: make the spatial model variables visible.',
'Mainali main STAR Methods Eqs.2–4, PDF pp.13–14.')
p='content/chapters/13-simulating-place-fields.md'
old='To reproduce Mainali et al.\'s (2025) place-field comparisons, a random map and a recorded map must be generated, fitted, and measured with compatible rules.'
new='To reproduce Mainali et al.\'s (2025) place-field comparisons, we need the rules for generating and fitting model maps, and for measuring both model and recorded maps.'
add(p,old,new,'Clarify that model maps are generated and fitted, while both kinds of map are measured.','Guide wording clarification; Mainali STAR Methods pp.13–15.')
sc='content/chapters/13-simulating-place-fields.yaml'
text=(root/sc).read_text(encoding='utf-8')
oldpurpose=re.search(r'^purpose:.*?(?=^role:)',text,re.M|re.S).group()
newpurpose=oldpurpose.replace(old,new)
add(sc,oldpurpose,newpurpose,'Align metadata with the corrected model versus recording roles.','Same source.')
record['edits'].extend(extra)
(folder/'edits-routes-methods.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
buffers={}
lineend={}
for e in extra:
    p=e['path']
    if p not in buffers:
        data=(root/p).read_bytes()
        lineend[p]=b'\r\n' in data
        buffers[p]=data.decode('utf-8').replace('\r\n','\n')
    assert buffers[p].count(e['original'])==1,(p,e['original'])
    buffers[p]=buffers[p].replace(e['original'],e['replacement'],1)
for p,text in buffers.items():
    (root/p).write_bytes((text.replace('\n','\r\n') if lineend[p] else text).encode('utf-8'))

result=json.loads((folder/'routes-methods-result.json').read_text(encoding='utf-8'))
integrity=[]
for f in result['files']:
    p=f['path']; raw=(root/p).read_bytes(); current=raw.decode('utf-8').replace('\r\n','\n'); previous=current
    for e in reversed(record['edits']):
        if e['path']==p:
            assert previous.count(e['replacement'])==1,(p,e['replacement'][:60])
            previous=previous.replace(e['replacement'],e['original'],1)
    previous_raw=(previous.replace('\n','\r\n') if b'\r\n' in raw else previous).encode('utf-8')
    assert hashlib.sha256(previous_raw).hexdigest()==f['sha256_before'],p
    f['sha256_after']=hashlib.sha256(raw).hexdigest()
    if p.endswith('.yaml'):yaml.safe_load(current)
    if p.endswith('.md'):
        for pattern in (r'\{#(?:sec|ch):[^}]+\}',r'\{\{block:fig:[^}]+\}\}',r'\.definition-(?:explanation|term)',r'publisher-fold-always',r'\.key-statement'):
            assert re.findall(pattern,current)==re.findall(pattern,previous),(p,pattern)
    integrity.append(p)
result.update(completed_utc=datetime.now(timezone.utc).isoformat(),checks='All 11 edited sources reconstruct exactly to their original hashes by reversing the recorded passage edits. Five YAML sidecars parse. Existing chapter/section anchors, figure references, blue definition markers, folded examples and highlighted-claim markers are unchanged. No build, gate, simulation run, visual review or independent acceptance performed.',unresolved=['Independent three-stage review and root integration remain pending.','Existing figure acceptance hold and reproduction limits remain unchanged.'],integrity_verified=integrity)
(folder/'routes-methods-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(completed_utc=result['completed_utc'],files=len(integrity),checks=result['checks']),indent=2))
