from pathlib import Path
import json, datetime, hashlib
ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent
fixes=[
dict(file='content/chapters/03-memory-information.yaml',old='This chapter measures the best accuracy available from those spikes and derives the constraint that this information places on the circuit’s memory stability.',new='This chapter sets a bound on estimation error under the model’s assumptions and derives the constraint that spike information places on the circuit’s memory stability.',reason='Independent root Stage 1: a bound is not necessarily attained by a finite spike sample.'),
dict(file='content/chapters/01-foundations.md',old='Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both. This identity will help distinguish random spreading of a stored value from a systematic change in its average.',new='Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both.',reason='Independent memory Stage 2: the second sentence repeats the same interpretation.')]
for x in fixes:
 p=ROOT/x['file']; t=p.read_text(encoding='utf-8'); assert t.count(x['old'])==1
 x['before_sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
(OUT/'review-fixes.json').write_text(json.dumps({'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'fixes':fixes},indent=2,ensure_ascii=False),encoding='utf-8')
for x in fixes:
 p=ROOT/x['file']; p.write_text(p.read_text(encoding='utf-8').replace(x['old'],x['new']),encoding='utf-8')
print('Applied 2 independently requested repairs.')
