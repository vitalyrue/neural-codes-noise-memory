"""Separate post-repair truth and Stage2 disposition; no reader edits."""
from pathlib import Path
from datetime import datetime
import json,hashlib,yaml
ROOT=Path(__file__).resolve().parents[2];HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def textsha(s):return hashlib.sha256(s.encode('utf-8')).hexdigest()
items={x['id']:x for x in read(HERE/'integration.json')}
application=read(HERE/'stage2-application.json');old=read(HERE/'stage2-review.json')
approved=read(HERE/'stage1-approved.json')['figures']
truth={
'W1':'The section defines RMS as sqrt(2Dt) for zero-mean diffusion. With D=.02>0 this scale increases with time, while an individual Brownian path need not move monotonically away from zero. A02 upper caption still says zero drift, and its lower plot separates vt from random RMS. The new phrase names the specific displayed ensemble scale; it does not assert that every path or a finite-sample spread increases. The following bias sentence retains linear versus square-root comparison.',
'W2':'The source-derived expansion of the squared endpoint difference is unchanged: for independent errors at distinct samples, Var(nu(t+ell)-nu(t))=2 sigma_m squared; same-sample zero lag cancels. The chosen Brownian M(ell)=2D ell has D=.010, giving M(.020)=.0004 and observed=.0014 after adding .001. The .0001 subtraction uncertainty remains25 percent. The two expressions now use balanced valid math delimiters and the same symbols; no mathematical claim changed. Browser math rendering is pending the later build.',
'W3':'The unchanged figure has an open circle at (0,.001), representing the positive-lag curve endpoint, and a filled dot at (0,0), representing the actual same-sample MSD. Saying the curve has an open endpoint at lag zero does not include that point in the positive-lag function. The complete alt still specifies strictly positive lags, the constant .001 offset and the20ms points. The original adjoining paragraph retains the temporally correlated-error alternative.',
'W4':'For d3 the limiting dimensionless density is (2/3) w^(-1/3) exp(-w^(2/3)), which grows without bound as positive w approaches zero. Its integral is one by the substitution U=w^(2/3); more generally U=beta s^(2/d), with survival Pr(U>u)=exp(-u) for u>=0. Thus the new direct explanation preserves the integrable-density claim and states the meaning of survival probabilities correctly. The original Stage1 independent integrals were one, with no mass at zero. The entire caption retains limiting/high-threshold status and excludes finite-threshold simulation or empirical-histogram claims.'}
wording={
'W1':'Retain revised whole interpretation: the already taught RMS term is necessary and specific, and the next sentence explains the long-time consequence of fixed bias without a new specialist term.',
'W2':'Retain revised whole caption: factor two, chosen movement law, zero-lag exception, numeric uncertainty and analytic-example status all earn their place. Rendering the symbols removes raw subscript notation.',
'W3':'Retain revised whole alt: it now describes the two actual endpoints without the contradictory phrase zero positive lag. The remaining values and bracket description serve the unseen-image reader.',
'W4':'Retain revised whole caption: the longer first clause is needed to say what the unbounded density means, and the probability explanation defines survival at use. Both transformed formulas remain exact. No new optional edits are requested.'}
out=dict(request_id='focused-W1-W4-20261024',reviewer='/root/all_illustrations_review',reviewed_at=datetime.now().astimezone().isoformat(),
 scope='Four repaired whole fields and their attached unchanged conditions in proposed sources; separate focused truth and Stage2 recheck.',
 truth_decision='pass',stage2_decision='pass',stage3_status='not started',canonical_acceptance='pending final insertion/source binding',
 repairs={},asset_reuse={},input_sha256={},rule_sha256=old['rule_sha256'],unresolved_findings=[],limits=['No reader sources edited','Browser math rendering not yet available; source expressions checked','Token stats unavailable','Awake execution time unverified'])
for repair in application['repairs']:
 id=repair['figure'];it=items[id];field=repair['field'];expected=repair['full_replacement'];assert it[field]==expected
 cp=it.get('chapter',it.get('chapter_path'));md=HERE/'proposed'/cp;ys=md.with_suffix('.yaml');src=md.read_text(encoding='utf-8');block=next(b for b in yaml.safe_load(ys.read_text(encoding='utf-8'))['blocks'] if b['id']==it['visual_id'])
 if field in ['caption','alt']:assert block[field]==expected
 else:assert expected in src
 context=[]
 for p in old['units'][id]['paragraphs']:
  if p['role'] in ['preceding_original','following_original','intro']:
   assert p['text'] in src,(id,p['role'],'context changed')
   context.append(dict(role=p['role'],paragraph_sha256=p['paragraph_sha256'],text=p['text'],disposition='unchanged and reread; original assumptions remain attached'))
 out['repairs'][repair['id']]=dict(figure=id,field=field,old_text_sha256=textsha(repair['full_original']),new_text_sha256=textsha(expected),text=expected,
   truth=dict(verdict='pass',evidence=truth[repair['id']]),necessity_and_wording=dict(verdict='pass',evidence=wording[repair['id']]),context=context)
 for p in [md,ys]:out['input_sha256'][str(p.relative_to(ROOT)).replace('\\','/')]=sha(p)

prior1={x['id']:x for x in read(HERE/'stage1-A01-A04.json')['figures']};prior2=read(HERE/'stage1-A05-A08.json')['figures'];prior3=read(HERE/'stage1-A09.json')
for id,oldasset in approved.items():
 folder=ROOT/'candidate-content/visuals/candidates/20261024-all'/id
 prior=prior1.get(id,prior2.get(id,prior3));widthhash=prior.get('book_width_sha256',prior.get('reviewed_book_width_sha256'))
 assert sha(folder/'figure.png')==oldasset['png_sha256'] and sha(folder/'figure.svg')==oldasset['svg_sha256']
 assert sha(folder/'book-width.png')==widthhash
 out['asset_reuse'][id]=dict(png_sha256=oldasset['png_sha256'],svg_sha256=oldasset['svg_sha256'],book_width_sha256=widthhash,decision='unchanged bytes; retain original independent pixel judgment',original_reviewer=oldasset['reviewer'])
for filename in ['integration.json','stage2-application.json','stage2-repairs.json','draw_foundations_information.py','draw_eye_place.py','foundation-information-integration.json','eye-place-integration.json']:
 p=HERE/filename;out['input_sha256'][str(p.relative_to(ROOT)).replace('\\','/')]=sha(p)
for id in ['A02','A06','A08']:
 for p in [HERE/(id+'-brief.yaml'),ROOT/'candidate-content/visuals/candidates/20261024-all'/id/'qa.json']:
  out['input_sha256'][str(p.relative_to(ROOT)).replace('\\','/')]=sha(p)
for p,h in out['rule_sha256'].items():assert sha(Path(p))==h,'rule changed'
(HERE/'focused-W1-W4-recheck.json').write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps(dict(reviewed_at=out['reviewed_at'],truth=out['truth_decision'],stage2=out['stage2_decision'],repairs=list(out['repairs']),unchanged_asset_sets=len(out['asset_reuse'])),indent=2))
