from pathlib import Path
import json,datetime,hashlib
r=Path(__file__).resolve().parents[2];o=Path(__file__).resolve().parent
fixes=[
{'file':'02b-memory-long-delays.md','old':'The mutual-excitation network gives a concrete case: substituting its two conjugate weights into the spike-noise projection gives','new':'For the mutual excitation network, substituting $v_1=v_2=1/2$ into the diffusion formula gives','reason':'Stage2-information: identify the weights and formula directly.'},
{'file':'03-memory-information.md','old':' This general tool measures which proposed values make a spike sample more likely.','new':'','reason':'Stage2-information: remove a restatement of the immediately preceding likelihood definition.'},
{'file':'03-memory-information.md','old':'It applies under the rate-distinguishability condition used above; if $J$ is singular, this ordinary inverse formula cannot be used.','new':'If $J$ is singular, this ordinary inverse formula cannot be used.','reason':'Stage2-information: assumption is already explained; keep the concrete limit without an invented compound.'},
{'file':'02-memory-dynamics.md','old':"**Interpretation.** Each neuron's contribution combines its spike variability,",'new':"**Interpretation.** For one memory coordinate, each neuron's contribution combines its spike variability,",'reason':'Stage3-dynamics-reading: distinguish the scalar interpretation from the newly preceding several-coordinate result.'}
]
for x in fixes:
 p=r/'content/chapters'/x['file'];t=p.read_text(encoding='utf-8');assert t.count(x['old'])==1,(x['file'],x['old']);x['before_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(o/'review-repairs.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'repairs':fixes},indent=2,ensure_ascii=False),encoding='utf-8')
for x in fixes:
 p=r/'content/chapters'/x['file'];p.write_text(p.read_text(encoding='utf-8').replace(x['old'],x['new']),encoding='utf-8')
print('Applied four independently requested repairs.')
