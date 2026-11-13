from pathlib import Path
from datetime import datetime, timezone
import json,hashlib,re
folder=Path(__file__).resolve().parent
root=folder.parents[1]
record=json.loads((folder/'edits-routes-methods.json').read_text(encoding='utf-8'))
p='content/chapters/11-simulating-memory.md'
old="The ring simulation uses an [[**Euler update**]{.definition-term custom-style=\"Definition Term\"}, which approximates a variable's change over a short interval by its current derivative times that interval.]{.definition-explanation}"
new="The ring simulation uses the [Euler update introduced in Chapter 1](ch-foundations.html#sec-foundations-simulation): approximate a variable's change over a short interval by its current derivative times that interval."
record['edits'].append(dict(path=p,original=old,replacement=new,reason='S2-06, root follow-up: use a plain linked reminder of the first Chapter 1 definition, retaining the local numerical explanation and cautions.',source='Guide Chapter 1 sec:FOUNDATIONS-SIMULATION and Burak and Fiete Network Simulations, main PDF p.6.',recorded_before_edit_utc=datetime.now(timezone.utc).isoformat()))
(folder/'edits-routes-methods.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
raw=(root/p).read_bytes();text=raw.decode('utf-8');assert text.count(old)==1
(root/p).write_bytes(text.replace(old,new,1).encode('utf-8'))
result=json.loads((folder/'routes-methods-result.json').read_text(encoding='utf-8'))
for f in result['files']:
    path=f['path'];raw=(root/path).read_bytes();now=raw.decode('utf-8').replace('\r\n','\n');before=now
    for e in reversed(record['edits']):
        if e['path']==path:
            assert before.count(e['replacement'])==1
            before=before.replace(e['replacement'],e['original'],1)
    reconstructed=(before.replace('\n','\r\n') if b'\r\n' in raw else before).encode('utf-8')
    assert hashlib.sha256(reconstructed).hexdigest()==f['sha256_before']
    f['sha256_after']=hashlib.sha256(raw).hexdigest()
    if path.endswith('.md'):
        for pattern in (r'\{#(?:sec|ch):[^}]+\}',r'\{\{block:fig:[^}]+\}\}',r'publisher-fold-always',r'\.key-statement'):
            assert re.findall(pattern,now)==re.findall(pattern,before)
result.update(completed_utc=datetime.now(timezone.utc).isoformat(),checks='All 11 edited sources reconstruct exactly to original hashes by reversing recorded edits. Five YAML sidecars parse. Existing chapter/section anchors, figure references, folds and major-claim markers are unchanged. Blue definition markers are unchanged except the requested repeated Euler definition now uses a plain linked reminder. No build, gate, simulation run, visual review or independent acceptance performed.')
(folder/'routes-methods-result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(result['completed_utc']); print('Euler reminder changed; recorded exact reversal remains valid for all 11 sources.')
