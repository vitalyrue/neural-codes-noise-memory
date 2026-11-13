"""Record the guide's actual source/check links; this does not accept prose."""
from pathlib import Path
from datetime import datetime
import csv, hashlib, json, re
import yaml

ROOT = Path(__file__).resolve().parents[1]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
sources = {
 'P1': ('Burak and Fiete (2012)', 'https://doi.org/10.1073/pnas.1117386109', '2012'),
 'P2': ('Ben-Shushan et al. (2022)', 'https://doi.org/10.1038/s41467-022-29201-y', '2022-03-28'),
 'P3': ('Mainali et al. (2025)', 'https://doi.org/10.1016/j.neuron.2025.01.017', '2025-04-02'),
}
# Locations and verification paths identify the worked reasoning, not just a formula.
rows = [
 ('MD01','P1','MEMORY-SPIKES','Jump/decay dynamics and population scaling','Main Eqs.7-11; SI I','memory-numeric-results.json','Exact dynamics, then leading weak-noise approximation'),
 ('MD02','P1','MEMORY-LINEARIZATION','Neutral tangent and left-vector projection','SI S7-S15','memory-numeric-results.json','Local linearization; other directions decay'),
 ('MD03','P1','MEMORY-DIFFUSION','Projected variance gives 2D=sum(v_i^2 r_i)','Main Eq.1; SI S15','memory-numeric-results.json','Conditionally independent Poisson innovations'),
 ('MD04','P1','MEMORY-SYMMETRIC','Symmetric projection and two-neuron example','SI S16-S18; main Fig.2E-G','memory-numeric-results.json','Main Eq.2 apparent missing square explicitly identified'),
 ('MD05','P1','MEMORY-LONG-TIME','Increment moments imply density equation and long-time distributions','SI S28-S41','memory-numeric-results.json','Boundary conditions, circular saturation and variable D distinguished'),
 ('MI01','P1','MEMORY-FI','Poisson likelihood, score and information rate','Main Eq.3; SI S42-S44','memory-numeric-results.json','Local regularity and finite-time decoding limits stated'),
 ('MI02','P1','MEMORY-BOUND','Scalar and matrix information-diffusion bounds','Main Eq.4; SI S45-S54','memory-numeric-results.json','Cauchy-Schwarz proof and PSD meaning; J nonsingular for matrix inverse'),
 ('MI03','P1','MEMORY-BOUND','Pointwise equality and linear-family counterexample','SI S48-S49; guide counterexample','../checks/equality-counterexample.json','Exponential transfer is sufficient; source necessity claim qualified'),
 ('MI04','P1','MEMORY-COMPARISONS','Population, rate, time and tuning-width comparisons','Main pp.3-5; SI scaling discussion','memory-numeric-results.json','Held resources are explicit'),
 ('MI05','P1','MEMORY-NAIVE','Naive readout variance and optimum','SI S79-S81','memory-numeric-results.json','Local Gaussian readout and Brownian covariance'),
 ('MI06','P1','MEMORY-IDEAL','Ideal readout by backward Gaussian precision recursion','Main Eq.5; SI S55-S78','memory-numeric-results.json','Equivalent teaching derivation independently compared with finite covariance inversion'),
 ('MI07','P1','MEMORY-EXTENSIONS','Partial readout, two time constants and additive Gaussian noise','SI S82-S95','memory-numeric-results.json','Different noise normalizations retained explicitly'),
 ('ED01','P2','EYE-INVERSE-FILTER','Forward firing fit and causal inverse kernel','Main Eqs.2-7','eye-checks.json','Quadratic roots, partial fractions, gain and delay checked'),
 ('ED02','P2','EYE-SHARED-VARIANCE','Independent variance bound from squared correlation','SI S1-S2','eye-checks.json','Population representation/private independence assumptions retained'),
 ('ED03','P2','EYE-CHI','Covariance estimate of shared contribution','Main Eqs.11-17','eye-checks.json','Single-cell readout, approximation and weighted-mean uncertainty distinguished'),
 ('ED04','P2','EYE-MEASUREMENT-NOISE','Measurement-noise MSD offset','Main Eqs.18-19; SI Fig.2','eye-checks.json','Positive-lag 2sigma^2; colored noise is separate'),
 ('ED05','P2','EYE-FILTERED-MSD','Stationary-noise plateau versus filtered Brownian growth','Main Eqs.20-22; guide one-pole reconstruction','eye-checks.json','Simplified reconstruction is not the full experimental model'),
 ('ED06','P2','EYE-CIRCUIT-MODEL','Integrator fixed points, motor/plant/feedback roles','Main Eqs.23-31,34','eye-checks.json','G(z)=z derived; delayed feedback changes ongoing fluctuations at all lags'),
 ('ED07','P2','EYE-SCALING','Rate/tuning/noise scaling and renewal regularization','Main Eq.1 and Sub-Poisson spike trains; SI S3-S6','eye-checks.json','Absolute versus fractional slope and long-window conditions explicit'),
 ('PF01','P3','PLACE-KAC-RICE','Expected upcrossings from Gaussian value and derivative','Main Eq.2; SI Methods S1','place-numeric-checks.json','Smooth stationary unit-variance Gaussian field'),
 ('PF02','P3','PLACE-INFERENCE','Field lengths, gaps, finite boundaries and count selection','Main Eqs.2-4; SI Methods S1','place-numeric-results.json','Exact mean identity distinguished from count-distribution approximation'),
 ('PF03','P3','PLACE-RARE-PEAKS','Conditional Hessian, overshoot and rare-peak geometry','SI Methods S3; author mathematical notes','place-numeric-results.json','High-threshold limit and isolated approximately spherical components'),
 ('PF04','P3','PLACE-SIZE-LAW','Dimensional size density, normalization, moments and units','Main Eq.1; SI S16-S18','place-numeric-results.json','Rayleigh/exponential/Weibull laws; apparent S18 units issue explained'),
 ('PF05','P3','PLACE-SLOPES','Crossing slope law and full field width','SI Methods S4','place-numeric-results.json','Crossing-weighted slope exact; width asymptotic; apparent factor issue checked'),
 ('PF06','P3','PLACE-TOPOLOGY','Expected Euler characteristic with boundary terms','SI Methods S2; Taylor (2006)','place-numeric-results.json','Theorem input disclosed; dimension-specific Gaussian integrals derived'),
 ('PF07','P3','PLACE-DATA','Experimental processing, fits and finite thresholds','Main Figs.1-4 and STAR Methods; SI S1-S5','place-evidence.md','Reported results checked against source; no raw-data reproduction'),
 ('PF08','P3','PLACE-WIRING','Random-weight input covariance and Gaussian example','Main Discussion; SI model; guide reconstruction','place-numeric-results.json','Sufficient model mechanism does not identify unique biological wiring'),
]
ledger=[]; equations=[]
for cid,src,sec,claim,locator,check,limit in rows:
 check=check.replace('place-numeric-results.json','place-numeric-checks.json')
 assert (ROOT/'verification/writers'/check).is_file(), check
 title,url,date=sources[src]
 ledger.append(dict(claim_id=cid,claim=claim,source_title=title,source_url=url,publication_or_version_date=date,access_date='2026-10-22',guide_location='sec:'+sec,status='independently truth-reviewed; later stages recorded separately',notes=locator+'; '+limit))
 equations.append(dict(equation_id=cid,guide_location='sec:'+sec,result=claim,source=src,source_locator=locator,verification='verification/writers/'+check,limits=limit,review_evidence='verification/reviews/'+({'P1':'memory','P2':'eye','P3':'place'}[src])+'-stage1-recheck.json'))
with (ROOT/'source-maps/research-ledger.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(ledger[0])); w.writeheader(); w.writerows(ledger)
(ROOT/'source-maps/equation-registry.yaml').write_text(yaml.safe_dump(dict(schema_version=1,equations=equations),sort_keys=False,allow_unicode=True),encoding='utf-8')

terms=[]; glossary=[]
for p in sorted((ROOT/'content/chapters').glob('*.md')):
 current=''; text=p.read_text(encoding='utf-8')
 for n,line in enumerate(text.splitlines(),1):
  m=re.search(r'\{#((?:ch|sec):[^}]+)\}',line)
  if m: current=m.group(1)
  for m in re.finditer(r'\[\*\*([^*]+)\*\*\]\{\.definition-term[^}]*\}',line):
   entry=dict(term=m.group(1).rstrip(':'),source=p.relative_to(ROOT).as_posix(),line=n,guide_location=current)
   (glossary if p.stem=='glossary' else terms).append(entry)
(ROOT/'source-maps/terminology-ledger.yaml').write_text(yaml.safe_dump(dict(schema_version=1,note='Marked terms and glossary entries, extracted from actual text. First-use adequacy is assessed in independent Stage 2 reports.',first_teaching=terms,glossary=glossary),sort_keys=False,allow_unicode=True),encoding='utf-8')
fig=ROOT/'assets/approved/visuals/attractor-directions.svg'
visual=dict(visual_id='fig:FOUNDATIONS-ATTRACTOR',asset=fig.relative_to(ROOT).as_posix(),sha256=sha(fig),origin='Guide-created deterministic vector plot from the explicitly taught two-activity example',source_status='Teaching construction, not a reproduced paper figure',generator='verification/checks/foundations_checks.py',placement='sec:FOUNDATIONS-ATTRACTOR-EXAMPLE',caption_and_alt='content/chapters/01-foundations.yaml',content_review='verification/reviews/memory-stage1-recheck.json',visual_review='pending representative browser check',rights='Original guide figure')
(ROOT/'source-maps/visual-ledger.yaml').write_text(yaml.safe_dump(dict(schema_version=1,visual_ledger_version=2,visuals=[visual]),sort_keys=False,allow_unicode=True),encoding='utf-8')
result=dict(prepared_at=datetime.now().astimezone().isoformat(),claims=len(ledger),equation_records=len(equations),first_teaching_marks=len(terms),glossary_entries=len(glossary),visuals=1,limits='These ledgers connect actual content to checks and independent reports; counts do not establish semantic acceptance.')
(ROOT/'verification/checks/evidence-ledgers.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
