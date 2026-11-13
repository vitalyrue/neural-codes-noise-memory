"""Apply the bounded, independently diagnosed Stage 2 repairs once."""
from pathlib import Path
from datetime import datetime
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
def mark(s): return '[**'+s+'**]{.definition-term custom-style="Definition Term"}'
changes={
'00-reading-guide.md':[
 (' The 2025 supplement was unavailable during the earlier overview task and was retrieved for this guide.',''),
],
'02-memory-dynamics.md':[
 ('For a ring network, increasing the density of equally spaced preferred angles',"For a ring network, a neuron's "+mark('preferred angle')+' is an angle where its tuning curve peaks. Increasing the density of equally spaced preferred angles'),
 ('independent spike innovations','independently generated spike-count fluctuations'),
 ('The result does not require translation symmetry or a particular bump shape. It does require symmetric weights, a stable continuous family, and the noise assumptions already introduced.','The result requires symmetric weights, a stable continuous family, and the noise assumptions already introduced; translation symmetry is unnecessary.'),
 ('To pass from random increments to a density equation, choose any smooth function', 'The '+mark('Itô convention')+' evaluates a state-dependent noise coefficient at the beginning of each increment. To pass from random increments to a density equation, choose any smooth function'),
 ('For constant $D$ on an unbounded line, its Gaussian solution is','Here the '+mark('Dirac delta')+' denotes a point mass: initially all probability is at $\\Theta$. It differs from the earlier zero-or-one symbol $\\delta_{ij}$. For constant $D$ on an unbounded line, the Gaussian solution is'),
 (' That convention evaluates the coefficient at the beginning of each increment.',''),
 ('Why does a convention for stochastic equations matter here? For state dependent $D$, the expression $d\\theta=\\sqrt{2D}\\,dB$ needs a rule for where inside an increment to evaluate $D$. An Itô equation with zero drift is not the same process as the corresponding Stratonovich equation with zero written drift. Converting the latter into Itô form adds a drift $D\'/2$.','For state dependent $D$, where the coefficient is evaluated affects the process. The '+mark('Stratonovich convention')+' uses midpoint evaluation in its limiting increments. With the same written coefficient and zero written drift, it describes a different process from the Itô equation. Converting the Stratonovich equation into Itô form adds a drift $D\'/2$.'),
 ('Spike innovations are conditionally independent','Newly generated spike-count fluctuations are conditionally independent'),
 ('An arbitrary extra source of correlated innovations','An extra source of correlated fluctuations'),
 ('In Fig. 1B, distinguish two uncertainties. The bump has moved away from its initial location $\\Theta$ during storage.','In Fig. 1B, an '+mark('activity bump')+" is a localized peak of population firing rates across the neurons' preferred angles. Its location has moved away from its initial value $\\Theta$ during storage."),
 ('black sigmoidal case','black sigmoidal, or S-shaped, case'),
],
'03-memory-information.md':[
 ('A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.','A '+mark('prior distribution')+' represents knowledge about likely parameter values before observing the spikes. A strong prior, bias, boundaries, or globally ambiguous tuning changes the estimation problem.'),
 ('Initially no observation means zero precision.',r'The hyperbolic tangent is $\tanh z=(e^z-e^{-z})/(e^z+e^{-z})$. Its inverse on $(-1,1)$ is $\operatorname{artanh}z=\tfrac12\log[(1+z)/(1-z)]$, whose derivative is $1/(1-z^2)$. Initially no observation means zero precision.'),
 (r'Here $\coth z=\cosh z/\sinh z$.',r'Here $\coth z=1/\tanh z$.'),
 ('Example: a sparse projection changes the useful interval','Example: limited spike access changes the useful interval'),
 ('replace Poisson innovations','replace Poisson spike-count fluctuations'),
],
'04-eye-drift.md':[
 ('because an incorrect gain during drift would change the inferred common variance.','because an incorrect '+mark('gain')+' during drift would change the inferred common variance. Gain is the scale that converts a change in one signal into a change in the other.'),
 ('For a repeated pole, $r^2=4km$, the continuous limit is','When the two decay times coincide, $r^2=4km$, the limit is'),
 ('The one sided test across 57 cells gave $p=3\\times10^{-9}$.','The one sided test asks whether the mean correlation is positive, compared with a zero-mean reference. Its $p$ value is the probability, under that reference, of a test statistic at least as large as observed. Across 57 cells it gave $p=3\\times10^{-9}$.'),
 ('where the error is the standard error of the mean (SEM), with one sided','where the error is the standard error of the mean (SEM). SEM estimates uncertainty in the across-cell mean, rather than the spread of individual cells or uncertainty across animals. The one sided test gave'),
 ('with the regularity factor and fixed geometry,','including the $\\mathrm{CV}^2$ factor just derived and holding the network geometry fixed,'),
],
'05-place-fields.md':[
 ('differentiable sample functions and nondegenerate joint distributions; peak calculations','differentiable sample functions and nondegenerate joint distributions: the relevant vector of heights and derivatives must have an invertible covariance matrix, rather than obey an exact linear constraint. Peak calculations'),
 (r'R(\Delta x)=\frac{C(\Delta x)}{C(0)},\qquad'+'\n',''),
 ('then, with probability one under nondegeneracy,','then, under regularity conditions that exclude tangencies and give nonzero slopes at crossings,'),
 ('nondegenerate derivatives, and $q\\to\\infty$','an invertible covariance matrix for the relevant derivative variables, and $q\\to\\infty$'),
 ('an affine plane. Thresholding commutes with restriction: first slicing','a flat plane. First slicing'),
 ('for a smooth function with nondegenerate critical points on a compact domain,','for a smooth function on a compact domain whose critical points have zero gradient and invertible Hessians,'),
 ('with no periodic identification','whose opposite faces are not joined'),
 ('On a $j$ dimensional face, the tangential calculation is the same as above. Each of its $d-j$ outward normal gradient components must have the appropriate sign','On a $j$ dimensional face, derivatives along the face give the same calculation as above. Each of its $d-j$ gradient components perpendicular to the face and directed out of the box must have the appropriate sign'),
 ('For the long-tunnel comparison, the authors report $\\Delta\\mathrm{LLR}=-50.3$, $\\Delta\\mathrm{BIC}=-109.1$, and $\\Delta\\mathrm{AIC}=-104.5$, with their sign convention favoring the Gaussian excursion model over a fitted lognormal. BIC and AIC penalize fitted parameter count when comparing likelihoods.','For the long-tunnel data, the authors compared the Gaussian excursion model with a fitted lognormal using likelihoods and criteria that penalize fitted parameter count. Those comparisons favored the Gaussian model.'),
 ('The same framework also allows differences between cells.','The model also allows differences between cells.'),
 ('this shared cell property creates cross-direction correlations despite remapping.','this shared cell property creates correlations between flight directions even when field locations differ between directions.'),
],
'06-synthesis.md':[
 ('Koyluoglu and colleagues treat persistent-activity storage as a noisy channel and ask how recall changes with delay and the number of stored items.','Koyluoglu and colleagues ask how noise limits recall as the delay and number of stored items increase.'),
 ("The model's success leaves a mechanistic identification problem to be resolved with input, connectivity, learning, or perturbation measurements.","The model's success leaves open which circuit mechanism produces these maps. Input, connectivity, learning, or perturbation measurements could distinguish the possibilities."),
 ('combine human eye tracking with retinal coding and Bayesian decoding','combine human eye tracking with a model of how eye movement affects visual signals'),
],
}
pending={}; records=[]
for name,repls in changes.items():
 p=ROOT/'content/chapters'/name; original=p.read_text(encoding='utf-8'); text=original
 for old,new in repls:
  assert text.count(old)==1,(name,old,text.count(old))
  text=text.replace(old,new)
 pending[p]=text
 records.append(dict(file=p.relative_to(ROOT).as_posix(),before_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),after_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(),changes=len(repls)))
for p,text in pending.items(): p.write_text(text,encoding='utf-8',newline='\n')
record=dict(applied_at=datetime.now().astimezone().isoformat(),reason='Bounded repairs diagnosed in independent memory/eye/place-stage2 reports; affected review required',files=records)
(ROOT/'verification/reviews/stage2-repairs.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
