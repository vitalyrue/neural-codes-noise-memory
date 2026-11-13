from pathlib import Path
import yaml,json,re

root=Path(__file__).resolve().parents[2]
task=root/'verification/exam-notation-20261104'
meta=yaml.safe_load((task/'00-exam-review.yaml').read_text(encoding='utf-8'))

local={
'm1':[r'$N_i(t)$ counts cell $i$\'s spikes up to time $t$; $dN_i$ counts new spikes in $dt$.'],
'm3':[r'$\delta\mathbf s$: a small activation disturbance, an $N$-vector. Its retained coordinate shift is $\mathbf v^T\delta\mathbf s$.'],
'm7':[r'$I_h=hJ$: information in a short observation, in inverse coordinate units squared. The state is effectively fixed during $h$.'],
'm8':[],
'm9':[r'$A>0$: rate scale (spikes/s).',r'$k>0$: sensitivity to total input, in inverse input units; $kg$ is dimensionless.',r'$W=W^T$ means symmetric connection weights.'],
'm13':[r'$V_{\rm ideal}(L)$: variance of error in reading the cue-time state; $V_{\rm ideal}(\infty)$ is its long-observation limit.',r'$L^*=1/\sqrt{2DJ}$: characteristic approach time (s), not a finite optimum.',r'$P=1/V_{\rm ideal}$: Gaussian precision, in inverse coordinate units squared.',r'$\coth z=(e^{2z}+1)/(e^{2z}-1)$; the argument here is dimensionless.',r'$D,J$ are held locally constant in this Gaussian readout calculation.'],
'm2':[r'$K_i$: cell $i$\'s spike count during the observation interval, dimensionless; distinct from response matrix $K$.',r'$\lambda_i=h\bar r_i$: expected count, dimensionless. Poisson names the count distribution.'],
'm4':[r'$g_i$ is evaluated at a steady state here; $g_i\prime=dg_i/d\theta$ has input units per coordinate unit.',r'$W_{ij}=W_{ji}$ is pairwise connection symmetry. Primes are first derivatives.'],
'm5':[r'$m$: number of stored coordinates; $\boldsymbol\theta$ is an $m$-vector. Indices $\alpha,\beta=1,\ldots,m$ label coordinates.',r'$\mathbf u^\beta=\partial\bar{\mathbf s}/\partial\theta_\beta$ and $\mathbf v^\alpha$: matching right and left $N$-vectors, with activation/coordinate and coordinate/activation units.',r'$\partial_\alpha\bar r_i$: rate slope in coordinate $\alpha$; $\delta_{\alpha\beta}$ is one for equal indices and zero otherwise.',r'Here $D,J$ are $m\times m$ matrices. $D_{\alpha\beta}$ has coordinate-$\alpha$ times coordinate-$\beta$/s units; $J_{\alpha\beta}$ has inverse coordinate-$\alpha$ times inverse coordinate-$\beta$/s units. $J$ must be invertible.',r'$A\succeq B$ means $A-B$ has a nonnegative quadratic form in every direction.'],
'm6':[r'$p(\theta,t)$: density across trials, in inverse coordinate units. The Gaussian and $2Dt$ formulas use constant $D$.',r'$\mathbb E[D(\theta)]$: trial-averaged diffusion coefficient.',r'For the circle example the coordinate is an angle in radians and error is wrapped to $[-\pi,\pi)$; its limiting MSD is $\pi^2/3$ rad$^2$.'],
'm10':[r'$c>0$: dimensionless multiplier of each rate tuning curve and its slope; distinct from preferred-value vector $\mathbf c$ in M11.',r'Each proportionality describes the controlled change specified in the derivation, with the other properties kept fixed.'],
'm11':[r'$d$: number of stored spatial coordinates; $\alpha$ labels one of them. Here $D,J$ are $d\times d$ matrices with the coordinate-wise units given in M5.',r'$\boldsymbol\theta,\mathbf c$: represented and preferred positions, both $d$-vectors in coordinate units. $\mathbf c$ is not multiplier $c$ in M10.',r'$w>0$: tuning width (coordinate units).',r'$a$: fixed peak rate (spikes/s); $f$: fixed dimensionless radial tuning shape, whose argument $(\boldsymbol\theta-\mathbf c)/w$ is dimensionless.',r'$\rho$: preferred-position density, in coordinate$^{-d}$ units.'],
'm12':[r'$V_{\rm naive}(L)$: error variance for the cue-time state under equal observation weights; $L_{\rm naive}^*$ minimizes it (s).',r'In covariance $2D\min(t,s)$, both $t$ and $s$ are elapsed observation times (s); this $s$ is not activation.',r'$D,J$ are held locally constant, and state-motion and observation noises are separate in the Gaussian readout model.'],
'm14':[r'$0<\alpha\le1$: probability of observing each spike independently, or a verified information fraction; distinct from the coordinate index in M5.',r'$J_{\rm obs}$: observed information rate, with the same units as $J$.',r'$L^*$ and $L_{\rm obs}^*$: full- and partial-access characteristic readout times (s).',r'$V_{\rm recall}$: error variance about the original value; $V_{\rm readout}$: error variance in reading the cue-time state.',r'$V_{\rm ideal,obs}(\infty)$: ideal partial-access limiting readout variance. The final displayed lower bound is the full-access benchmark, $\alpha=1$.'],
'm15':[r'$\tau_m$: firing-rate response time (s), distinct from synaptic decay $\tau$.',r'$\dot r_i$: time derivative of rate (spikes/s$^2$); $\phi(g_i)$ is the target rate at the present input.'],
'm16':[r'$q_n>0$: common additive Gaussian noise intensity, activation units squared/s, or s$^{-1}$ with unit-spike activation. A noise increment has variance $q_n\,dt$; the rate average over $h$ has noise variance $q_n/h$ (s$^{-2}$).',r'Here $J$ is information per second in Gaussian rate observations. The coordinate, projection and time units are unchanged.',r'This $q_n$ is unrelated to the dimensionless place-field threshold $q$.'],
'e1':[r'$f$: firing rate (spikes/s); $x=E-E_T$: position offset from fitted threshold angle $E_T$ (degrees).',r'$k$: position coefficient (spikes/(s degree)); $r$: velocity coefficient (spikes/degree), not firing rate; $m$: acceleration coefficient (spikes s/degree).',r'$t_j$: time of spike $j$; $\Delta t$: fitted neural lead (both s); $p$: Laplace frequency (s$^{-1}$).',r'$\tau_+,\tau_-$: distinct positive slow and fast response times (s).',r'$h_0,h$: causal position responses before and after the delay, in degrees/spike; each vanishes before its effective input.'],
'e3':[r'$X,Y$: spike-predicted and measured displacements over 350 ms (degrees).',r'$C$: shared upstream displacement; $\epsilon$: private prediction error; $\eta$: other measured-displacement contributions (all degrees). Here $C$ is not a covariance function.',r'$\chi=\operatorname{Var}(C)/\operatorname{Var}(Y)$: dimensionless shared fraction; $\widehat\chi$ is its weighted estimate.',r'The reported $0.82\pm0.07$ uses propagated weighted estimation error, not between-animal spread.'],
'e5':[r'$\xi$: white input in a chosen input unit $U$; $A$ is its intensity, defined by $\mathbb E[\xi(t)\xi(t\prime)]=A\delta(t-t\prime)$, with units $U^2$ s.',r'For this normalization $h$ has units degrees/($U$ s). $E$ is centered and stationary in this calculation.',r'$A$ here is noise intensity, not the visual-feedback gain used elsewhere.'],
'e6':[r'$B$: accumulating Brownian position command (degrees).',r'$\tau_f$: the single eye-response time (s), written $\tau$ in the detailed chapter; distinct from the 2012 synaptic time.',r'$W$: standard Brownian process with increment variance $dt$ and units sqrt(s), not a connection weight.',r'$v=\dot E$: eye velocity (degrees/s); $C_v(s)$: stationary velocity covariance (degrees$^2$/s$^2$), where $s$ is a time lag.'],
'e2':[r'Angle brackets denote a motor-population mean; a representative sample estimates it with sampling uncertainty.',r'$R_i^2$: explained variance fraction after best linear rescaling. Predictors and measured displacement are standardized to zero mean and unit variance for the proof.'],
'e4':[r'$\nu(t)$: position-reading error (degrees); $\sigma_m^2$: variance of one reading error (degrees$^2$).',r'$M_{\rm obs}$: MSD from measured angles $E_{\rm obs}$, with the same units as $M$. Displacement error uses two readings.'],
'e7':[r'$N$: number of comparable integrator neurons, rather than motor count $N_m$.',r'$\lambda,\lambda_0$: rate and typical mean rate (spikes/s).',r'$a=d\lambda/dE$: absolute slope (spikes/(s degree)); $b=a/\lambda_0$: fractional slope (degree$^{-1}$). These are not the place-field gain.',r'$J$: Poisson information rate about angle (s$^{-1}$ degree$^{-2}$).',r'$\mathrm{CV}$: interspike-interval standard deviation divided by its mean, dimensionless; $\tau_s$: synaptic decay time (s).',r'The paper calls $k_0$ position sensitivity but leaves its absolute/fractional normalization unclear.'],
'p1':[r'$[u]_+=\max(u,0)$ retains positive excess and sets negative excess to zero; $u=z-q$ is dimensionless.',r'$C\prime\prime(0)$: second spatial covariance derivative along a unit direction (input units squared/distance$^2$). The normalized covariance is $C/C(0)$.'],
'p3':[r'$L$: track length (distance); $N_L$: count of connected active intervals intersecting $[0,L]$, including clipped intervals.',r'$z\prime$: spatial derivative (distance$^{-1}$); height density times the mean positive part of slope gives a count per distance.'],
'p4':[r'$\mu_s,\mu_g$: stationary mean complete-field and complete-gap lengths (distance), measured per field or gap rather than per occupied position.',r'$Q^{-1}$: inverse Gaussian upper-tail function, dimensionless.',r'These are not finite clipped-track ratios; $\mu_s$ is distinct from input mean $\mu$.'],
'p6':[r'$U=q\epsilon$: dimensionless scaled excess tending to a mean-one exponential variable.',r'$r_*$: approximate field radius (distance), not a firing rate.',r'Each field is sampled once, rather than weighted by occupied volume.'],
'p2':[r'$i$: input-cell index; $u_i(x)$: fixed input firing profile (Hz).',r'$W_i$: zero-mean random weight (input units/Hz); $v_W=\operatorname{Var}(W_i)$: weight variance (input units squared/Hz$^2$). These are not Brownian quantities.',r'Covariance is over choices of weights. The Gaussian limit requires many active terms with no dominant input; spatial properties also depend on the fixed profiles.'],
'p5':[r'$L$: track length; $G$: inactive gap length; $g$: nonnegative gap cutoff (all distance units).',r'$N_L$: rare-field count on that track; $N$: unconditioned field count; $\lambda$: unconditioned Poisson mean count, dimensionless rather than a firing rate.',r'The survival law concerns large gaps in the rare-field limit; the conditioned mean excludes zero-field cells.'],
'p7':[r'$F_{\max}$: peak rate (Hz); $r_*$: approximate field radius (distance).',r'$s^{1/d}$: linear-size measure (distance); for a 1D full width, $v_1=2$.'],
'p8':[r'$k\ge0$: dimensionless moment order, not the eye coefficient.',r'$\mu_s=\mathbb E[s]$: mean field size (distance$^d$). This limiting mean differs from the exact 1D mean in P4.',r'$u=\beta s^{2/d}$: dimensionless integration variable; $\Gamma(t)=\int_0^\infty u^{t-1}e^{-u}\,du$ for dimensionless $t>0$. The moment has distance$^{dk}$ units.'],
'p9':[r'$x_0$: point on the sampling line (position vector, distance units); $\mathbf e$: dimensionless unit direction.',r'$t,t\prime$: signed spatial coordinates along the line (distance), not times.',r'$h_{\rm line}$ and $C_{\rm line}$: restricted input and covariance, with the same units as $h,C$. The original map dimension $d$ differs from the slice dimension.'],
'p10':[r'$v=z\prime(x)>0$: normalized input slope at an upcrossing (distance$^{-1}$).',r'$p_{\uparrow}(v)$: density of slopes selected at upcrossings; $p_{z\prime}(v)$: derivative density at an ordinary spatial point (both have distance units).',r'$w$: positive slope integration variable (distance$^{-1}$); $av$: rate slope (Hz/distance). This $v$ is not eye velocity or unit-ball volume $v_d$.'],
'p11':[r'$L$: side length of the box (distance); $j=1,\ldots,d$: dimension of the contributing interior, face or edge.',r'$\eta_j$: signed Euler-characteristic contribution per $j$-dimensional measure (distance$^{-j}$), not a positive field density.',r'$\chi_d$: Euler characteristic of the active set in the closed box, a dimensionless signed count; unrelated to eye fraction $\chi$. The sum retains real boundary terms.'],
'p12':[r'$N$: number of connected active fields, not neurons; $V$: environment length, area or volume (distance$^d$).',r'$\chi_d$: signed Euler-characteristic count from P11; it approaches $N$ only for isolated simple blobs at high threshold. The bulk formula omits boundary terms.'],
}

keys={
'memory':r'''<span id="notation-memory"></span>

**Shared memory notation.** These definitions apply to both memory tables. A row states any changed meaning or extra symbol.

- [$N$: number of neurons; $i,j$: neuron indices. $W_{ij}$ sends activation from cell $j$ to receiver $i$.]{.definition-explanation}
- [$\theta$: current represented coordinate; $\Theta$: its initial value; $\hat\theta$: an estimate from observations. Their units are the chosen coordinate units, for example radians.]{.definition-explanation}
- [$t$: time; $h$: short counting window; $T$: storage delay; $L$: observation duration after the recall cue (all seconds). The source writes readout duration as $\Delta T$.]{.definition-explanation}
- [$s_i$: outgoing activation of cell $i$, dimensionless with one unit added per spike. A bar, as in $\bar s_i$, denotes a noise-free steady value.]{.definition-explanation}
- [$r_i,\bar r_i$: firing rate and steady firing rate (spikes/s); $\bar r_i\prime=d\bar r_i/d\theta$: tuning slope (rate per coordinate unit).]{.definition-explanation}
- [$g_i$: total input; $b_i$: constant bias (same input units). $W$ is an $N\times N$ matrix in input units per activation unit. $\phi(g)$ converts input into rate; $\phi\prime$ differentiates with respect to input.]{.definition-explanation}
- [$\tau$: synaptic activation decay time (s).]{.definition-explanation}
- [$D$: scalar diffusion coefficient (coordinate units squared/s); $2D$ is the local displacement-variance growth rate. $J$: scalar information per second about the coordinate (inverse coordinate units squared/s). M5 and M11 use matrix versions.]{.definition-explanation}
- [$K$: $N\times N$ linear response matrix (s$^{-1}$). $\mathbf u=\partial\bar{\mathbf s}/\partial\theta$: tangent $N$-vector (activation/coordinate). $\mathbf v$: normalized left zero vector; $v_i$ measures the retained coordinate shift per activation unit from cell $i$.]{.definition-explanation}
- [$V$ with a subscript denotes error variance (coordinate units squared); the subscript identifies the estimate being assessed.]{.definition-explanation}

''',
'eye':r'''<span id="notation-eye"></span>

**Shared eye-motion notation.** These definitions apply to both eye tables. Filter normalization and response times are specified in the rows that use them.

- [$t$: time; $\ell$: separation between two readings; $u$: integration lag (all seconds). A dot differentiates with respect to time.]{.definition-explanation}
- [$E$: true eye angle; $\widehat E$: spike-predicted angle; $E_{\rm obs}$: measured angle (degrees).]{.definition-explanation}
- [$M(\ell)=\mathbb E[(E(t+\ell)-E(t))^2]$: mean squared displacement (MSD), in degrees$^2$. $C_E(\ell)$: covariance of centered eye position at lag $\ell$, also in degrees$^2$.]{.definition-explanation}
- [$D$: temporal angle diffusion coefficient (degrees$^2$/s). It is unrelated to place-field dimension $d$.]{.definition-explanation}
- [$h$: causal response kernel. Its units depend on the input normalization in E1 or E5; it is not the spatial input map in the place-field model.]{.definition-explanation}
- [$N_m$: number of contributing motor neurons; $i$: motor-neuron index; $R_i$: correlation between cell $i$\'s displacement prediction and measured displacement over the same 350 ms intervals, dimensionless. $R$ omits the cell index.]{.definition-explanation}

''',
'place':r'''<span id="notation-place"></span>

**Shared place-field notation.** These definitions apply to both place-field tables. The independent variable is position, rather than time.

- [$x,y$: spatial positions, scalar on a track or vectors in $\mathbb R^d$ (distance units); $d$: spatial dimension, 1, 2 or 3.]{.definition-explanation}
- [$h(x)$: fixed Gaussian input map; $\mu$: constant input mean; $\sigma_0$: input standard deviation; $h_{\rm th}$: absolute firing threshold (all in input units).]{.definition-explanation}
- [$z=(h-\mu)/\sigma_0$: normalized input; $q=(h_{\rm th}-\mu)/\sigma_0$: normalized threshold; $\epsilon$: peak excess above $q$ (all dimensionless).]{.definition-explanation}
- [$F$: firing rate (Hz); $a$: gain converting normalized excess into firing rate (Hz). It is not the eye model's tuning slope.]{.definition-explanation}
- [$C(x,y)$, or $C(y-x)$ for a stationary map: covariance of unnormalized input, in input units squared. It is not the eye model's shared displacement $C$. Spatial primes differentiate with respect to distance.]{.definition-explanation}
- [$\ell_c$: local distance scale, written $\sigma$ in the place-field chapters; distinct from input standard deviation $\sigma_0$.]{.definition-explanation}
- [$Q(q)=\Pr(Z>q)$ for a standard normal scalar $Z$: dimensionless Gaussian upper-tail probability. $\nu_+(q)$: upcrossing density (distance$^{-1}$).]{.definition-explanation}
- [$s$: complete-field size (length, area or volume, with distance$^d$ units); $S$: nonnegative cutoff in the same units.]{.definition-explanation}
- [$v_d$: dimensionless unit-ball volume, with $v_1=2$, $v_2=\pi$ and $v_3=4\pi/3$. $\beta$: size-law coefficient, in inverse distance squared in every dimension.]{.definition-explanation}

'''
}

changes=[]
for block in meta['blocks'][1:]:
    for row in block['rows']:
        rid=re.search(r'id="result-([^"]+)"',row[0]).group(1)
        assert rid in local
        oldcell=row[0]
        formula=oldcell.split('<br>[**Symbols and units:**',1)[0]
        items=[s.replace(r'\prime',"'").replace("\\'","'") for s in local[rid]]
        if items:
            # Span-based ARIA lists keep list semantics inside Pandoc pipe-table cells.
            bullets='<br>'.join('<span role="listitem">&#8226; <span class="definition-explanation">'+s+'</span></span>' for s in items)
            formula+='<br>**Extra symbols and notes:**<br><span role="list">'+bullets+'</span>'
        row[0]=formula
        changes.append({'result':rid,'old':oldcell,'new':formula,'shared_key':rid[0]})

md=(task/'00-exam-review.md').read_text(encoding='utf-8')
md=md.replace('Use the **Symbols and units**, **Paper location** and **Guide location** beside a formula to repair the missing step.','Read the paper\'s **shared notation** first. Each formula then lists only its extra symbols and notes, followed by **Paper location** and **Guide location**.')
markers={'memory':'{{block:tbl:EXAM-MEMORY-CORE}}','eye':'{{block:tbl:EXAM-EYE-CORE}}','place':'{{block:tbl:EXAM-PLACE-CORE}}'}
for paper,marker in markers.items():
    # The key precedes its table wrapper so its bullets occupy the full reading width.
    wrapper='<div class="table-responsive">\n\n'+marker
    key=keys[paper].replace(r'\prime',"'").replace("\\'","'")
    md=md.replace(wrapper,key+wrapper,1)
md=md.replace('Each row defines its own physical symbols.','The shared key below defines recurring symbols; rows list only additions and exceptions.')
(root/'content/chapters/00-exam-review.md').write_text(md,encoding='utf-8')
(root/'content/chapters/00-exam-review.yaml').write_text(yaml.safe_dump(meta,sort_keys=False,allow_unicode=True,width=105),encoding='utf-8')
(task/'DEFINITION-MOVES.json').write_text(json.dumps(changes,indent=2),encoding='utf-8')
print('Added3shared keys; compacted35row symbol keys into local bullet lists.')
