from pathlib import Path
import yaml

root = Path(__file__).resolve().parents[2]
md = root / 'content/chapters/00-mathematical-tools.md'
sidecar = md.with_suffix('.yaml')
rows = []

def row(label, formula, derivation, decoding):
    rows.append([f'**{label}**<br>{formula}', derivation, decoding])

row('2012 · Spike-driven feedback · model',
    r'$ds_i=-s_i\,dt/\tau+dN_i$<br>$g_i=\sum_jW_{ij}s_j+b_i$<br>$r_i=\phi(g_i)$',
    r'A spike count $N_i$ increases outgoing activation $s_i$ by one; between spikes it decays over time $\tau$. The fixed weight $W_{ij}$ sends cell $j$\'s activation to receiver $i$; bias $b_i$ completes total input $g_i$. [Chapter 1; paper Eqs. 7–9](../chapters/ch-foundations.html#sec-memory-spikes).',
    r'The circuit stores a value through activity that renews itself. The weights determine who affects whom; they do not change during storage. The response $\phi$ converts input into firing rate, rather than directly into eye angle.')

row('2012 · Spike variability · model',
    r'$K_i\mid\theta\sim\mathrm{Poisson}(\lambda_i)$<br>$\lambda_i=h\bar r_i(\theta)$<br>$\operatorname{Var}(K_i\mid\theta)=\lambda_i$',
    r'Independent rare events in short subdivisions give the Poisson count law over a duration $h$. Its first two moments give equal count mean and variance. Here $\bar r_i$ is the steady tuning curve at value $\theta$. [Count derivation](../chapters/ch-foundations.html#sec-foundations-poisson).',
    r'Higher firing supplies more events and more absolute count noise. The elementary spike noise is independent across cells conditional on the current state; recurrent interactions can still correlate complete neural trajectories.')

row('2012 · Lasting displacement · central',
    r'$K\mathbf u=0$<br>$\mathbf v^TK=0,\quad\mathbf v^T\mathbf u=1$<br>$2D(\theta)=\sum_i v_i^2\bar r_i$',
    r'$K$ is the matrix governing small activation disturbances, and $\mathbf u=\partial\bar{\mathbf s}/\partial\theta$ follows the steady-state family. The left vector $\mathbf v$ removes the decaying part: a disturbance $\delta\mathbf s$ leaves shift $\mathbf v^T\delta\mathbf s$. Add independent projected spike variances. [Projection](../chapters/ch-memory-dynamics.html#sec-memory-linearization) and [diffusion; SI S14–S15](../chapters/ch-memory-dynamics.html#sec-memory-diffusion).',
    r'$v_i$ measures the lasting change in the represented value caused by one activation change in cell $i$, after other disturbances relax. $D$ is half the local growth rate of displacement variance. This is a leading weak-noise result near a tuned continuous family with stable transverse directions.')

row('2012 · Symmetric connections · supporting',
    r'$2D=\dfrac{\sum_i\bar r_i(g_i\prime)^2}{\tau^2(\sum_i\bar r_i\prime g_i\prime)^2}$',
    r'If $W_{ij}=W_{ji}$, differentiate the fixed-state equations to find $v_i\propto g_i\prime$, then normalize by $\mathbf v^T\mathbf u=1$. Primes mean derivatives with respect to memory value $\theta$. [Chapter 3; corrected Eq. 2](../chapters/ch-memory-dynamics.html#sec-memory-symmetric).',
    r'For this special connectivity, tuning and input slopes determine diffusion without separately solving for $\mathbf v$. The numerator contains squared input slopes, as in the published correction. The general projection formula does not require symmetric weights.')

row('2012 · More than one stored coordinate · supporting',
    r'$2D_{\alpha\beta}=\sum_i v_i^\alpha\bar r_i v_i^\beta$',
    r'Choose a tangent for each stored coordinate and left vectors satisfying $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. Project the same spike noise onto each pair of coordinates. [Diffusion tensor; SI S14](../chapters/ch-memory-dynamics.html#sec-memory-diffusion).',
    r'The diagonal entries give spreading in each coordinate. Off-diagonal entries give coupled changes in two stored coordinates, even when the elementary spike noises are independent. The weak-noise and local-state assumptions remain.')

row('2012 · Accumulated storage error · supporting',
    r'$\partial_t p=\partial_\theta^2[D(\theta)p]$<br>$\operatorname{Var}[\theta(t)-\Theta]=2Dt$<br>$p(\theta,t)=\dfrac{e^{-(\theta-\Theta)^2/(4Dt)}}{\sqrt{4\pi Dt}}$',
    r'Combine small Itô diffusion increments, with no systematic drift, into a probability evolution equation. The Gaussian and $2Dt$ formulas additionally require constant $D$, a point initial value $\Theta$ and an unbounded coordinate. [Chapter 4; SI Section II](../chapters/ch-memory-long-delays.html#sec-memory-long-time).',
    r'The remembered value spreads even while neural activity persists. With state-dependent $D$, variance instead grows at rate $2\mathbb E[D(\theta)]$. Boundaries, angular wrapping and systematic drift require their own treatment; a linear MSD need not continue forever.')

row('2012 · Spike precision · central',
    r'$J(\theta)=\sum_i\dfrac{(\bar r_i\prime)^2}{\bar r_i}$<br>$I_h=hJ$<br>$\operatorname{Var}(\hat\theta)\ge1/(hJ)$',
    r'Differentiate the log probability of independent Poisson counts with respect to $\theta$. The mean squared derivative is Fisher information $I_h$; independent terms add. Cauchy Schwarz applied to estimation error gives the variance bound for regular locally unbiased estimates. [Chapter 5; Eq. 3 and Cramér Rao derivation](../chapters/ch-memory-information.html#sec-memory-fi).',
    r'Steep tuning relative to spike noise makes nearby current values easier to distinguish. $J$ is information per second about the present state, not stored bits or certainty about the original cue. The state is effectively fixed during this short count calculation, and finite-sample attainment is not guaranteed.')

row('2012 · Information–diffusion bound · central',
    r'$D\ge\dfrac{1}{2\tau^2J}$<br>$2DJ\tau^2\ge1$',
    r'The normalization of the lasting-shift weights gives $\tau\sum_i v_i\bar r_i\prime=1$. Cauchy Schwarz bounds its square by $\tau^2(\sum_i v_i^2\bar r_i)(\sum_i(\bar r_i\prime)^2/\bar r_i)$. [Chapter 5; Eq. 4 and SI Section V](../chapters/ch-memory-information.html#sec-memory-bound).',
    r'The same noisy spikes convey the value and renew the activity carrying it. At fixed $J$ and synaptic time $\tau$, tuning the network cannot reduce diffusion below this bound in the stated model. It assumes the tuned continuous family, weak independent conditional spike noise, a common decay time and no external anchoring signal.')

row('2012 · Equal-weight readout · supporting',
    r'$V_{\rm naive}(L)=\dfrac1{JL}+\dfrac{2DL}{3}$<br>$L_{\rm naive}^*=\sqrt{\dfrac3{2DJ}}$',
    r'Average observations for duration $L$ after the readout cue. Count noise averages to $1/(JL)$; integrating Brownian covariance $2D\min(t,s)$ over the observation square gives $2DL/3$. Differentiate to find the optimum. [Chapter 6; SI S76–S81](../chapters/ch-memory-readout.html#sec-memory-naive).',
    r'Collecting more spikes first helps, then hurts because later spikes represent a state that has moved further from the cue state. $V$ is readout error variance under the local Gaussian observation model, with constant $D,J$ and separate state-motion and observation noise.')

row('2012 · Diffusion-aware readout · central',
    r'$V_{\rm ideal}(L)=\sqrt{\dfrac{2D}{J}}\coth(\sqrt{2DJ}\,L)$<br>$V_{\rm ideal}(\infty)=\sqrt{2D/J}$<br>$L^*=1/\sqrt{2DJ}\le\tau$',
    r'Combine observation precision backward in time while adding diffusion variance between observations. Precision $P$ obeys $dP/dL=J-2DP^2$, $P(0)=0$; solve and use $V=1/P$. [Chapter 6; SI S58–S75](../chapters/ch-memory-readout.html#sec-memory-ideal).',
    r'Accounting for motion makes more observation keep helping, toward a finite limit. $L^*$ is a characteristic saturation time, not a hard deadline. This is an ideal observer within the local Gaussian readout model; it does not show a biological decoder implementing the rule.')

row('2012 · Storage plus partial readout · supporting',
    r'$V_{\rm recall}=2DT+V_{\rm readout}$<br>$J_{\rm obs}=\alpha J$<br>$L_{\rm obs}^*=L^*/\sqrt\alpha$<br>$V_{\rm ideal,obs}(\infty)=\sqrt{2D/(\alpha J)}$',
    r'Storage for delay $T$ adds independent error when readout is locally unbiased and future noise is independent of storage history. Independently retain each spike with probability $\alpha$; substitute the thinned rates into the FI formula. [Error addition](../chapters/ch-memory-readout.html#sec-memory-readout-setup) and [partial access; SI S82](../chapters/ch-memory-readout.html#sec-memory-partial).',
    r'Missing spikes reduces readout information while the full circuit keeps diffusing at the same $D$. Reading becomes slower and less precise. A selected fraction of neurons need not carry the same fraction of information; $\alpha J$ follows from random spike thinning or a verified information fraction.')

row('2022 · From spikes to eye position · method',
    r'$m\ddot x+r\dot x+kx=f$<br>$h_0(u)=\dfrac{\tau_+\tau_-}{m(\tau_+-\tau_-)}(e^{-u/\tau_+}-e^{-u/\tau_-}),\ u>0$<br>$\widehat E(t)=E_T+\sum_j h(t-t_j)$',
    r'Invert the fitted rate–movement equation for $x=E-E_T$. Factor $mp^2+rp+k=m(p+1/\tau_+)(p+1/\tau_-)$; each root supplies a decay. Set $h_0=0$ for $u<0$ and restore the fitted delay by $h(u)=h_0(u-\Delta t)$. [Chapter 7; Eqs. 2–7](../chapters/ch-eye-drift.html#sec-eye-inverse-filter).',
    r'Each recorded spike at $t_j$ contributes a calibrated position response in degrees. Coefficients $k,r,m$ couple firing to position, velocity and acceleration; $r$ here is not a firing rate. The two distinct positive decay times describe the fitted response. This predicts movement from one cell, rather than claiming that one cell controls the eye by itself.')

row('2022 · Independent-noise limit · supporting',
    r'$\sum_{i=1}^{N_m}R_i^2\le1$<br>$\langle R_i^2\rangle\le1/N_m$',
    r'Standardize independent single-cell predictors and measured displacement. Subtract their best linear prediction; its residual variance $1-\sum_iR_i^2$ cannot be negative. Here $R_i$ is the displacement correlation and $N_m$ is motor population size. [Chapter 7; SI S1–S2](../chapters/ch-eye-drift.html#sec-eye-shared-variance).',
    r'If independent motor fluctuations alone supplied the movement, the average cell could explain only a small fraction of its variance. The measured mean correlation gives $\langle R^2\rangle\ge0.17^2\simeq0.029$, challenging that explanation for a population of thousands. Applying the bound to sampled cells requires a representative average.')

row('2022 · Shared movement fraction · central',
    r'$X=C+\epsilon,\quad Y=C+\eta$<br>$\chi\simeq\dfrac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}$<br>$\chi\simeq R\sqrt{\operatorname{Var}(X)/\operatorname{Var}(Y)}$',
    r'$X$ is spike-predicted displacement and $Y$ is measured displacement, both calibrated in degrees. Expand their covariance: it retains the shared component variance $\operatorname{Var}(C)$ when the other covariances are negligible. [Chapter 7; Eqs. 11–15](../chapters/ch-eye-drift.html#sec-eye-chi).',
    r'Weak single-cell correlation can coexist with a large common contribution to movement. The paper reports $\widehat\chi=0.82\pm0.07$ at 350 ms. This requires transferable gain calibration and nearly uncorrelated private contributions; the recorded cell creates a neglected order-$1/N_m$ covariance. Locating the shared source upstream also uses the biological independence premise.')

row('2022 · Measurement offset · method',
    r'$M_{\rm obs}(\ell)=M(\ell)+2\sigma_m^2,\quad\ell>0$',
    r'For measured position $E_{\rm obs}=E+\nu$, expand its squared displacement. Independent errors at the two times each contribute variance $\sigma_m^2$; movement–error cross terms vanish. $M(\ell)=\mathbb E[(E(t+\ell)-E(t))^2]$. [Chapter 8; Eqs. 18–19](../chapters/ch-eye-timing.html#sec-eye-measurement-noise).',
    r'Independent position-reading error raises every positive-lag MSD by a constant, which can dominate the smallest movements. At zero lag it cancels exactly. Temporally correlated measurement error needs a lag-dependent correction instead.')

row('2022 · Filtered white noise · supporting',
    r'$C_E(\ell)=A\int_0^\infty h(u)h(u+\ell)\,du$<br>$M(\ell)=2[C_E(0)-C_E(\ell)]$',
    r'Convolve white input of intensity $A$ with a stable response $h$, then average the product at two times. For a centered stationary position, expand the squared displacement. [Chapter 8; Eqs. 20–22](../chapters/ch-eye-timing.html#sec-eye-filtered-msd).',
    r'If filter overlap decays to zero, MSD tends to the finite plateau $2C_E(0)$. Muscle filtering can smooth private motor noise, but cannot make this stationary position noise accumulate displacement variance indefinitely. Eye MSD instead keeps growing over the observed range.')

row('2022 · Filtered accumulating command · guide derivation',
    r'$\tau_f\dot E+E=B,\quad dB=\sqrt{2D}\,dW$<br>$M(\ell)=2D[\ell-\tau_f(1-e^{-\ell/\tau_f})]$<br>$M\sim D\ell^2/\tau_f\ (\ell\ll\tau_f)$<br>$M\sim2D(\ell-\tau_f)\ (\ell\gg\tau_f)$',
    r'A Brownian position command $B$ drives a one-time-constant eye response $\tau_f$. After velocity transients, $C_v(s)=(D/\tau_f)e^{-|s|/\tau_f}$. Integrate it as $M=2\int_0^\ell(\ell-s)C_v(s)\,ds$. [Chapter 8, teaching reconstruction](../chapters/ch-eye-timing.html#sec-eye-filtered-msd).',
    r'The eye can move smoothly while its internal position command diffuses. Increasing $\tau_f$ reduces short-lag motion; increasing $D$ raises the entire curve. The synaptic time $\tau$ from 2012 is a different parameter. This simplified calculation illustrates the 2022 interpretation; the paper uses two muscle times and feedback, and does not uniquely identify the circuit.')

row('2025 · Active spatial regions · model',
    r'$z=(h-\mu)/\sigma_0$<br>$q=(h_{\rm th}-\mu)/\sigma_0$<br>$F=a[z-q]_+$<br>$\ell_c=\sqrt{-C(0)/C\prime\prime(0)}$',
    r'Normalize a stationary Gaussian input map $h$ with mean $\mu$, standard deviation $\sigma_0$ and covariance $C$. Threshold at $q$; gain $a$ converts excess into firing. Differentiating covariance gives $\operatorname{Var}(z\prime)=\ell_c^{-2}$. [Chapter 10; model and spatial scale](../chapters/ch-place-fields.html#sec-place-gp).',
    r'A field is one connected region where $z>q$. The sampled map stays fixed during traversal. Raising threshold removes active space; increasing $\ell_c$ stretches the local spatial scale. Here $\ell_c$ is the distance scale called $\sigma$ in later place chapters, not input standard deviation $\sigma_0$.')

row('2025 · Random inputs create spatial covariance · supporting',
    r'$h(x)=\sum_i W_i u_i(x)$<br>$C(x,y)=v_W\sum_i u_i(x)u_i(y)$',
    r'Use fixed input profiles $u_i(x)$ and independent random weights with mean zero and variance $v_W$. Average over weight choices; cross terms vanish. Many individually small contributions permit a Gaussian limit. [Chapter 12; Methods S2](../chapters/ch-place-tests.html#sec-place-wiring).',
    r'The same input cell contributes at nearby positions, creating spatial covariance. Broader input profiles can broaden fields; changing weight variance instead changes input amplitude and hence effective threshold if the absolute threshold stays fixed. Random weights alone do not guarantee smooth, stationary or isotropic maps.')

row('2025 · Crossing density and finite-track count · exact',
    r'$\nu_+(q)=\dfrac{e^{-q^2/2}}{2\pi\ell_c}$<br>$\mathbb E[N_L]=L\nu_+(q)+Q(q)$',
    r'Kac–Rice multiplies height density at $q$ by mean positive spatial slope there. Stationary Gaussian height and slope are independent. Add $Q(q)=\Pr(Z>q)$, $Z\sim N(0,1)$, for a field already active at the left end of a track of length $L$. [Chapter 10; S9–S13 and main Eq. 8](../chapters/ch-place-fields.html#sec-place-kac-rice).',
    r'This counts active components intersecting the track, including clipped boundary fields. It is exact for a sufficiently smooth stationary nondegenerate Gaussian map at any threshold. Higher $q$ reduces counts when $q>0$; larger $\ell_c$ reduces crossings per unit length at fixed $q$.')

row('2025 · Means identify threshold and scale · exact',
    r'$\mu_s=Q(q)/\nu_+$<br>$\mu_g=[1-Q(q)]/\nu_+$<br>$q=Q^{-1}\!\left(\dfrac{\mu_s}{\mu_s+\mu_g}\right)$<br>$\ell_c=\dfrac{\mu_s+\mu_g}{2\pi}e^{-q^2/2}$',
    r'Divide active and inactive spatial fractions by the same upcrossing density to obtain mean field length $\mu_s$ and gap length $\mu_g$. Their ratio gives active fraction; invert the Gaussian upper tail and crossing scale. [Chapter 10; Methods S3](../chapters/ch-place-fields.html#sec-place-inference).',
    r'Two measured means constrain two model parameters before testing the full length histograms. These are stationary complete-field and complete-gap means. Finite-track clipping or selection of only cells with fields must be handled before treating sample means as these quantities.')

row('2025 · Universal size laws · central approximation',
    r'$\Pr(s>S)\simeq e^{-\beta S^{2/d}}$<br>$\beta=\dfrac{q^2}{2\ell_c^2v_d^{2/d}}$<br>$(v_1,v_2,v_3)=(2,\pi,4\pi/3)$',
    r'At large positive $q$, a typical counted field surrounds one nearly quadratic peak: radius $r_*\simeq\ell_c\sqrt{2\epsilon/q}$ for peak excess $\epsilon$. The scaled excess $q\epsilon$ tends to a unit-mean exponential law. Substitute size $s=v_dr_*^d$. [Chapter 11; Eq. 1, Methods S4 and corrected constants](../chapters/ch-place-sizes.html#sec-place-size-law).',
    r'The same input mechanism gives Rayleigh lengths in 1D, exponential areas in 2D and a Weibull volume law with exponent $2/3$ in 3D. Each field has equal sampling weight. These are high-threshold limits; multi-peak fields and finite thresholds can change the distribution.')

row('2025 · Size moments and shape · supporting approximation',
    r'$\mathbb E[s^k]\simeq\Gamma(1+kd/2)\beta^{-kd/2}$<br>$\mu_s\simeq\Gamma(1+d/2)\beta^{-d/2}$',
    r'Differentiate the size survival law to obtain its density; set $u=\beta s^{2/d}$ in the moment integral. Here $k\ge0$ and $\Gamma$ is the gamma function, defined by its integral in the linked derivation. [Chapter 11, size-law moments](../chapters/ch-place-sizes.html#sec-place-size-law).',
    r'After the mean fixes size scale, higher moment ratios test the predicted shape. No extra shape fit is needed in the limiting law. These moments inherit its high-threshold assumption and describe complete fields rather than fields selected by occupied volume.')

row('2025 · Boundary slopes · exact',
    r'$p_{\uparrow}(v)=\ell_c^2v\,e^{-\ell_c^2v^2/2},\quad v>0$',
    r'Select an upcrossing rather than a uniformly chosen position. Its slope density is proportional to $v p_{z\prime}(v)$; normalize over positive slopes. Here $v=z\prime$ is the normalized input slope at a boundary. [Chapter 11; boundary-slope derivation](../chapters/ch-place-sizes.html#sec-place-slopes).',
    r'Steep slopes are sampled more often at crossings. This Rayleigh law is independent of $q$ under the smooth stationary Gaussian model, without a high-threshold approximation. Firing-rate slope is $av$, so its scale also depends on the rate gain $a$.')

row('2025 · Components and holes · exact',
    r'$\eta_1=\dfrac{e^{-q^2/2}}{2\pi\ell_c}$<br>$\eta_2=\dfrac{qe^{-q^2/2}}{(2\pi)^{3/2}\ell_c^2}$<br>$\eta_3=\dfrac{(q^2-1)e^{-q^2/2}}{(2\pi)^2\ell_c^3}$<br>$\mathbb E[\chi_d]=Q(q)+\sum_{j=1}^d\binom dj L^j\eta_j$',
    r'Count spatial critical points with signs: maxima create components, while other critical points join regions or alter holes. The signed Kac–Rice calculation gives $\eta_j$; faces and edges supply the coefficients for a closed box of side $L$, in $d=1,2,3$. [Chapter 12; Eqs. 8–10](../chapters/ch-place-tests.html#sec-place-topology).',
    r'Here $\chi_d$ is Euler characteristic, unrelated to the eye variance fraction $\chi$. It counts components minus holes in 2D, and components minus tunnels plus cavities in 3D. These formulas retain boundary contributions for a smooth stationary isotropic nondegenerate Gaussian map; they are not periodic-box formulas or general field counts.')

row('2025 · Rare-field count in higher dimensions · supporting approximation',
    r'$\mathbb E[N]\simeq\dfrac{Vq^{d-1}e^{-q^2/2}}{(2\pi)^{(d+1)/2}\ell_c^d}$',
    r'At high $q$, isolated components usually have one peak and no holes, so their count approaches Euler characteristic. Retain the leading volume term and leading power of $q$ in the preceding formula; $V$ is environment length, area or volume. [Chapter 12, high-threshold count](../chapters/ch-place-tests.html#sec-place-topology).',
    r'This predicts how field count changes with threshold, spatial scale and dimension in a large region at high threshold. It drops boundary terms and holes; the exact Euler-characteristic formula must not be used as an exact component count at ordinary thresholds.')

summary = '''## Major results connect formulas to physical questions {#sec:MATH-TOOLS-RESULTS}

Which formula answers the question you are asking? Use this table as a reference while reading the detailed chapters. The **derivation** column gives the main steps and links to the full calculation and its paper references. **Decoding** means what the formula tells us about the neural circuit, eye movement or spatial map, including what it cannot establish. It does not always mean reconstructing a value from spikes.

The rows follow Burak and Fiete (2012), Ben-Shushan et al. (2022), then Mainali et al. (2025). **Central** marks a principal result; **supporting** marks a result that explains or qualifies it. **Model** and **method** identify assumptions and measurement rules. **Guide derivation** identifies a teaching calculation. Exact and approximate labels refer to the stated mathematical models, rather than guarantees about every biological circuit. Each row uses local notation; in particular, the memory and eye response times differ, and the two meanings of $\\chi$ are separate.

The full derivations remain in their chapters. You can continue to Part I without studying every row now.

{{block:tbl:MATH-RESULTS}}

'''
text = md.read_text(encoding='utf-8')
marker = '[^tools-model]:'
assert 'sec:MATH-TOOLS-RESULTS' not in text
text = text.replace(marker, summary + marker, 1)
md.write_text(text, encoding='utf-8')
meta = yaml.safe_load(sidecar.read_text(encoding='utf-8'))
meta['section_list'].append({'id':'sec:MATH-TOOLS-RESULTS','title':'Major results connect formulas to physical questions','summary':'A reference table links the major formulas from all three papers to their derivations, physical meanings and limits.','level':2})
meta['blocks'].append({'id':'tbl:MATH-RESULTS','kind':'table','placement':'sec:MATH-TOOLS-RESULTS','headers':['formula','derivation','decoding'],'rows':rows,'caption':'Major mathematical results and model equations from the three papers. The guide uses corrected expressions where its detailed derivations identify printed errors.','first_column_role':'row-labels','html_fold':'never'})
sidecar.write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
print(f'Added {len(rows)} rows.')
