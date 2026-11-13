from pathlib import Path
import json, datetime, hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
fixes=[
dict(file='content/chapters/03b-memory-readout.md',old='The activation noise retains its Poisson strength.',new='Here $\u005cxi_i$ is the zero mean noise from variable spike generation, with the same Poisson strength as in the basic model.',reason='Independent memory Stage 3: connect the new noise symbol to intrinsic spikes.'),
dict(file='content/chapters/05-place-fields.md',old='The recordings include bats flying through tunnels, rats moving over an arena floor, and bats flying through a room.',new='The study compares recordings of hippocampal place cells from bats flying through tunnels, rats moving over an arena floor, and bats flying through a room.',reason='Independent eye/place Stage 3: identify the cells at the chapter entry, including for direct arrivals.')]
for x in fixes:
 p=ROOT/x['file']; t=p.read_text(encoding='utf-8'); assert t.count(x['old'])==1
 x['before_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'flow-fixes.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixes':fixes},indent=2,ensure_ascii=False),encoding='utf-8')
for x in fixes:
 p=ROOT/x['file']; p.write_text(p.read_text(encoding='utf-8').replace(x['old'],x['new']),encoding='utf-8')
print('Applied 2 independently checked reader-flow fixes.')
