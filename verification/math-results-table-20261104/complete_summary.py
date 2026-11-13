from pathlib import Path
import yaml

root=Path(__file__).resolve().parents[2]
path=root/'content/chapters/00-mathematical-tools.yaml'
meta=yaml.safe_load(path.read_text(encoding='utf-8'))
rows=meta['blocks'][0]['rows']

def find(label):
    return next(r for r in rows if label in r[0])

def after(label,new_label,formula,derivation,decoding):
    i=rows.index(find(label))+1
    rows.insert(i,[f'**{new_label}**<br>{formula}',derivation,decoding])

r=find('More than one stored coordinate')
r[1]=r[1].replace('SI S14','SI S22–S24')
r[0]+=r'<br>$J_{\alpha\beta}=\sum_i(\partial_\alpha\bar r_i)(\partial_\beta\bar r_i)/\bar r_i$<br>$2D\succeq\tau^{-2}J^{-1}$'
r[1]+=r' Applying the same normalization in matrix form gives the bound when the information matrix $J$ is invertible. [Matrix proof; SI S52–S56](../chapters/ch-memory-information.html#sec-memory-bound).'
r[2]+=r' The matrix inequality means every linear combination of coordinate changes obeys its variance bound, including coupled directions.'

after('Information–diffusion bound','2012 · Attaining the bound · central',
      r'$v_i=\bar r_i\prime/(\tau J\bar r_i)$<br>$\phi(g)=A e^{kg}\quad\text{is sufficient for }W=W^T$',
      r'Equality in Cauchy Schwarz requires $v_i\sqrt{\bar r_i}$ to be proportional to $\bar r_i\prime/\sqrt{\bar r_i}$ for every contributing cell. In a symmetric network an exponential transfer rule supplies the required common ratio $\phi\prime/\phi$; $A>0$ and $k>0$ are constants. [Chapter 5, equality condition; SI S45–S51](../chapters/ch-memory-information.html#sec-memory-bound).',
      r'The retained effect of each cell\'s spike noise must match the information its spikes provide. Suitable symmetric exponential networks reach the lower bound under the same tuned-model assumptions. Exponential transfer is a sufficient class, not a general necessity; the guide gives a linear counterexample to the stronger source claim.')

after('Attaining the bound','2012 · Controlled changes of circuit parameters · supporting',
      r'$J\propto N,\quad D\propto N^{-1}$<br>$J\mapsto cJ,\quad D\mapsto D/c$<br>$D\propto\tau^{-2}$',
      r'Replicate a population of $N$ neurons with the same tuning distribution and weights scaled as $1/N$. Count the sums in the symmetric diffusion formula. A uniform rate multiplier $c>0$ also multiplies tuning slopes. For the time comparison, hold rate tuning and its input relation fixed. [Chapter 5, controlled comparisons](../chapters/ch-memory-information.html#sec-memory-comparisons).',
      r'More comparable neurons can reduce independent noise, and longer synaptic effects can reduce the lasting shift per spike. The stated rate-to-diffusion scaling needs an equality-achieving network or preserved tuning/input geometry. Changing rate or decay time without the corresponding circuit adjustment need not preserve the stored-state family.')

after('Controlled changes of circuit parameters','2012 · Tuning width depends on dimension · supporting',
      r'$J_{\alpha\alpha}\propto\rho a w^{d-2}$<br>$D_{\alpha\alpha}\propto w^{2-d}\quad\text{at equality}$',
      r'Use tuning $a f[(\boldsymbol\theta-\mathbf c)/w]$ with uniform preferred-value density $\rho$, fixed peak rate $a$, radial shape $f$ and width $w$. The information integral gains $w^d$ from recruited cells and $w^{-2}$ from squared slopes. [Chapter 5, width derivation](../chapters/ch-memory-information.html#sec-memory-comparisons).',
      r'Under these fixed resources, narrower tuning helps in one dimension and broader tuning helps in three; the leading width power vanishes in two. The diffusion statement additionally assumes an equality-achieving network. Holding total spike rate fixed would be a different comparison. This is the guide\'s reconstruction of the paper\'s width argument.')

after('Storage plus partial readout','2012 · A rate response time changes the bound · extension',
      r'$\tau_m\dot r_i=-r_i+\phi(g_i)$<br>$D\ge\dfrac{1}{2(\tau+\tau_m)^2J}$',
      r'Keep synaptic activation decay $\tau$ and add a firing-rate response time $\tau_m$. Linearize both sets of variables and normalize the left mode against their combined tangent. In the symmetric model the diffusion denominator gains $(\tau+\tau_m)^2$ in place of $\tau^2$. [Chapter 6; SI S84–S92](../chapters/ch-memory-readout.html#sec-memory-extensions).',
      r'Slower intrinsic rate response can also carry memory between spikes. The two times add for this specified two-stage model, with the same Poisson drive and stable transverse directions. Replacing $\tau$ by a sum of arbitrary biological response times is not justified.')

after('A rate response time changes the bound','2012 · Noise law changes the equality condition · extension',
      r'$J=\sum_i(\bar r_i\prime)^2/q_n$<br>$2D=q_n\sum_i v_i^2$<br>$2DJ\ge\tau^{-2}$',
      r'Replace Poisson fluctuations by independent additive Gaussian noise with constant intensity $q_n>0$; a rate observation averaged for $h$ has noise variance $q_n/h$. Repeat the likelihood and projection calculations with this same noise law. [Chapter 6; SI S93–S95 with explicit normalization](../chapters/ch-memory-readout.html#sec-memory-extensions).',
      r'The information–diffusion relation survives this matched noise model, but equality now needs $v_i\propto\bar r_i\prime$. In the symmetric model a linear transfer rule is sufficient. An optimal transfer rule therefore depends on how neurons fluctuate. The noise intensity $q_n$ is unrelated to the place-field threshold $q$.')

r=find('Accumulated storage error')
r[2]+=r' For constant angular diffusion on a circle, wrapped error eventually becomes uniform and its MSD tends to $\pi^2/3$ in radian-squared units; the plateau does not mean noise stopped.'
r=find('Storage plus partial readout')
r[0]+=r'<br>$V_{\rm recall}(T,L)\ge2DT+\sqrt{2D/J}$'
r[2]+=r' The general ideal total-error limit is $2DT+\sqrt{2D/J}$; it equals $2D(T+\tau)$ only at equality in the information bound. [Why printed Eq. 6 needs this qualification](../chapters/ch-memory-readout.html#sec-memory-fig3-and-caution).'

after('Filtered accumulating command','2022 · Firing variability and sensitivity set a noise scale · supporting estimate',
      r'$J\simeq Na^2/\lambda_0$<br>$D\propto\dfrac{\mathrm{CV}^2\lambda_0}{Na^2\tau_s^2}=\dfrac{\mathrm{CV}^2}{N\lambda_0 b^2\tau_s^2}$',
      r'In a comparable population of $N$ cells, write mean firing $\lambda_0$, absolute position slope $a=d\lambda/dE$ and fractional slope $b=a/\lambda_0$. Long-window renewal count variance supplies the squared interval coefficient of variation, $\mathrm{CV}^2$; project that noise with fixed network geometry. [Chapter 9, scale estimate and Eq. 1 comparison](../chapters/ch-eye-circuit.html#sec-eye-scaling).',
      r'Within this estimate, more regular spikes, more comparable cells or longer synaptic decay $\tau_s$ reduce diffusion. Increasing rate helps at fixed fractional slope but raises the scale at fixed absolute slope. The paper\'s Eq. 1 leaves slope normalization unclear. This simpler Poisson-based scale comparison is not an exact formula for its full saturating, sub-Poisson network.')

after('Means identify threshold and scale','2025 · Rare field locations and gaps · limiting approximation',
      r'$N_L\approx\mathrm{Poisson}(\nu_+L)$<br>$\Pr(G>g)\simeq e^{-\nu_+g}$<br>$\mathbb E[N\mid N\ge1]=\lambda/(1-e^{-\lambda})$',
      r'At high threshold, well-separated rare excursions can approach independent locations if spatial correlations decay sufficiently. Their spacing is then approximately exponential, and short field widths make gaps $G$ approach the same scale. Conditioning a Poisson count with mean $\lambda$ on at least one field gives the last expression. [Chapter 10, rare events and selection; main Eq. 5](../chapters/ch-place-fields.html#sec-place-inference).',
      r'The model predicts whole count and gap distributions beyond their means. Smoothness and stationarity alone do not imply independence. The bulk count omits finite-track boundary effects; excluding zero-field cells also raises the observed mean and must be accounted for in fitting.')

after('Universal size laws','2025 · Peak firing and field size · supporting approximation',
      r'$F_{\max}=a\epsilon$<br>$F_{\max}\simeq\dfrac{aq}{2\ell_c^2}(s/v_d)^{2/d}$',
      r'Use the same high-peak parabola: $\epsilon\simeq q r_*^2/(2\ell_c^2)$ and $s=v_dr_*^d$. Firing above threshold is $a\epsilon$ at the peak. [Chapter 11; Methods S4, Figs. 3 and 5](../chapters/ch-place-sizes.html#sec-place-rare-peaks).',
      r'Higher peaks create wider fields, with limiting exponent two against linear size $s^{1/d}$. The exponent against area or volume differs. Finite-threshold data and simulations have smaller fitted exponents, so the limiting square law is not an exact empirical relation.')

after('Size moments and shape','2025 · Slices retain Gaussian structure · central test',
      r'$h_{\rm line}(t)=h(x_0+t\mathbf e)$<br>$C_{\rm line}(t,t\prime)=C[(t-t\prime)\mathbf e]$',
      r'Restrict a jointly Gaussian map to points on a line with unit direction $\mathbf e$, or to a plane. The retained joint distributions remain Gaussian with the restricted covariance. Under isotropy they retain the local scale $\ell_c$. [Chapter 11; Fig. 2 and Fig. S2](../chapters/ch-place-sizes.html#sec-place-slices).',
      r'At high threshold, line-slice lengths approach a Rayleigh law and plane-slice areas an exponential law, even within a 3D map. Slice components have different sampling weights from complete fields; larger objects are more likely to be intersected. A chosen central cut through each field is a different sampling rule.')

for r in rows:
    for i,s in enumerate(r):
        r[i]=s.replace(r'C\prime\prime',"C''").replace(r'\prime',"'").replace("\\'","'")
path.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')

md=root/'content/chapters/00-mathematical-tools.md'
text=md.read_text(encoding='utf-8')
text=text.replace('The units and numerical value of $\\beta$ depend on the dimension.','Because size $S$ has units distance$^d$, $\\beta$ has units inverse distance squared in every dimension; its geometric factor changes with dimension.')
marker='## Connection weights determine'
text=text.replace(marker,'For a compact reference while reading, use the [major-results table](#sec-math-tools-results): formula, derivation and physical meaning.\n\n'+marker,1)
text=text.replace('**Guide derivation** identifies a teaching calculation.','**Extension** changes the original model; **guide derivation** identifies a teaching calculation. **Exact** and **approximation** mark how strongly a formula follows from the model.')
md.write_text(text,encoding='utf-8')
print(f'Completed {len(rows)} rows.')
