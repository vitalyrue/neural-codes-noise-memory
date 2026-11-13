from pathlib import Path
from datetime import datetime
import hashlib,json,shutil,re
OUT=Path(__file__).resolve().parent;ROOT=OUT.parents[1];P=OUT/'proposed'
read=lambda p:p.read_text(encoding='utf-8');sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=list((ROOT/'content/chapters').glob('*.md'))+list((ROOT/'content/chapters').glob('*.yaml'))+[ROOT/'plan/chapter-plan.yaml',ROOT/'guide-project.yaml',ROOT/'verification/illustrations/draw_orientation.py']
for p in files:
 dest=P/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True)
 assert not dest.exists(),dest
 shutil.copy2(p,dest)
edits=[]
def change(rel,before,after,reason,finding):
 p=P/rel;text=read(p);assert text.count(before)==1,(rel,before[:80],text.count(before))
 old=sha(p);p.write_text(text.replace(before,after),encoding='utf-8',newline='\n')
 edits.append({'file':rel,'before':before,'after':after,'reason':reason,'finding':finding,'before_sha256':old,'after_sha256':sha(p)})

change('content/chapters/01b-persistence.md',r'''Writing $t=n\Delta t$ gives linear variance growth $2Dt$. In the continuous diffusion approximation this becomes

$$
\theta(t)=\theta(0)+\sqrt{2D}\,W(t),
\qquad
\mathbb E[(\theta(t)-\theta(0))^2]=2Dt.
$$

The [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$ starts at zero, has independent Gaussian increments, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$. It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation. The parameter $D$ is its diffusion coefficient. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.''',r'''Writing $t=n\Delta t$ gives linear variance growth $2Dt$. To describe this limit with a continuous path, use [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$. It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$. It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation.

In this continuous diffusion approximation,

$$
\theta(t)=\theta(0)+\sqrt{2D}\,W(t),
\qquad
\mathbb E[(\theta(t)-\theta(0))^2]=2Dt.
$$

The parameter $D$ is the diffusion coefficient. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.''','Explain the new process before its equation and make the zero-mean and continuity properties explicit; these distinguish random spreading from the bias comparison that follows.','ROOT-S1-01')
change('content/chapters/glossary.md','A continuous random process starting at zero with independent Gaussian increments and increment variance equal to elapsed time.','A continuous random process starting at zero with independent Gaussian increments of mean zero and variance equal to elapsed time.','Match the explicit Brownian increment assumptions used by the displacement calculation.','ROOT-S1-01')
change('content/chapters/03-memory-information.md',r'''Under these assumptions $J\propto w^{d-2}$. In an equality achieving isotropic exponential network, diffusion in each coordinate consequently scales as $D\propto w^{2-d}$. The resulting comparisons are:''',r'''Each diagonal entry therefore scales as $J_{\alpha\alpha}\propto w^{d-2}$. Now restrict the tuning shape $f$ to depend only on distance from its center. Uniformly distributing those centers makes every coordinate direction equivalent: off-diagonal information terms vanish, and all diagonal entries are equal. For an exponential network that attains the matrix bound, $D_{\alpha\alpha}=1/(2\tau^2J_{\alpha\alpha})\propto w^{2-d}$. The resulting comparisons are:''','State the extra directional symmetry before reducing the matrix bound to a scalar per-coordinate result; avoid requiring the as-yet untaught term isotropic.','M-S1-01')
change('content/chapters/04b-eye-timing.md',r'''Velocity loses its past value over time $\tau$ and receives new random input. After its velocity transient has decayed, its solution is

$$
v(t)=\frac{\sqrt{2D}}{\tau}\int_{-\infty}^{t}e^{-(t-u)/\tau}\,dW(u),
\qquad
C_v(s)=\frac D\tau e^{-|s|/\tau}.
$$

The covariance follows by multiplying the two integrals: only their shared increments contribute, with the same exponential overlap as in the white noise calculation. Integrating velocity over an interval gives position change. The double integral over its covariance reduces to''',r'''Velocity loses its past value over time $\tau$ and receives new random input. To add the surviving effect of those inputs, divide the past into short intervals of width $h$. The Brownian change $\Delta W_j=W(u_j+h)-W(u_j)$ has mean zero and variance $h$. Changes in disjoint intervals are independent. Its contribution to the velocity at time $t$ is approximately $(\sqrt{2D}/\tau)e^{-(t-u_j)/\tau}\Delta W_j$: the initial change has decayed between $u_j$ and $t$.

The integral against $dW(u)$ denotes the limit of these weighted sums as $h$ tends to zero. It does not require an ordinary derivative of the Brownian path. After the initial velocity has decayed, extending the input history into the distant past gives

$$
v(t)=\frac{\sqrt{2D}}{\tau}\int_{-\infty}^{t}e^{-(t-u)/\tau}\,dW(u).
$$

For a lag $s\geq0$, multiply the sums for $v(t)$ and $v(t+s)$ and average. Products of distinct increments have zero mean. The same increment contributes its variance $h$, so the sum becomes an ordinary overlap integral over their shared past:

$$
\begin{aligned}
C_v(s)
&=\frac{2D}{\tau^2}\int_{-\infty}^{t}
e^{-(t-u)/\tau}e^{-(t+s-u)/\tau}\,du\\
&=\frac{2D}{\tau^2}e^{-s/\tau}\int_0^\infty e^{-2r/\tau}\,dr
=\frac D\tau e^{-s/\tau}.
\end{aligned}
$$

Here $r=t-u$ is the age of an input increment. Covariance is even in the lag, so $C_v(s)=(D/\tau)e^{-|s|/\tau}$ for either sign of $s$. Integrating velocity over an interval gives position change. The double integral over its covariance reduces to''','Teach the weighted-increment integral from a finite-step interpretation, then show why independence reduces its covariance to the exponential overlap; retain the stationary-velocity qualification.','EYE-S1-01')

# DOI-label markup only. Each exact footnote change is retained separately; URLs and claims stay the same.
for p in sorted((P/'content/chapters').glob('*.md')):
 for line in read(p).splitlines():
  if not line.startswith('[^'):continue
  after=re.sub(r'\[(https://doi\.org/[^\]]+)\]\(\1\)',lambda m:'[DOI]('+m.group(1)+')',line)
  after=re.sub(r'(?<=\s)(https://doi\.org/[^\s<>]+)',lambda m:'[DOI]('+m.group(1).rstrip('.,;')+')'+m.group(1)[len(m.group(1).rstrip('.,;')):],after)
  if after!=line:change(p.relative_to(P).as_posix(),line,after,'Replace a displayed raw DOI URL with a descriptive DOI link label. Full citation, locator and target remain unchanged.','ROOT-FORMAT-01')
for before,after in [('Chapters 2–3','Chapters 3–6'),('Chapter 4','Chapters 7–9'),('Chapter 5','Chapters 10–12')]:
 change('verification/illustrations/draw_orientation.py',before,after,'Correct the existing map label to the current thirteen-chapter reading path.','M-S1-02')
(OUT/'repairs-v1.json').write_text(json.dumps({'at':datetime.now().astimezone().isoformat(),'author':'/root','edits':edits},indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'edits':len(edits),'changed_files':sorted({e['file'] for e in edits})}))
