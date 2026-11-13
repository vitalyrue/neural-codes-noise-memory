## Covariance tests which fluctuations are shared {#sec:MATH-TOOLS-SHARED}

If one neuron's spikes predict some eye movement, is the neuron passing on a common command or adding its own noise? Both can make its activity vary. Comparing the prediction with measured movement helps separate the part they share from fluctuations present in only one signal.

[The [**covariance**]{.definition-term custom-style="Definition Term"} of $X$ and $Y$ measures their average product after each mean is removed: $\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)]$.]{.definition-explanation} Positive covariance means that deviations tend to have the same sign. [The [**correlation coefficient**]{.definition-term custom-style="Definition Term"} $\rho=\operatorname{Cov}(X,Y)/(\sigma_X\sigma_Y)$ divides by both standard deviations, giving a dimensionless measure between $-1$ and $1$ when both variances are finite and positive.]{.definition-explanation} Covariance has the product of the signals' units.

Consider a teaching model, with all signals measured in degrees:

$$
X=aS+\eta_x,\qquad Y=bS+\eta_y.
$$

Here $S$ is a shared displacement command, $X$ a cell's displacement prediction, and $Y$ measured displacement. The dimensionless gains $a,b$ say how strongly the same command affects each signal. The private contributions $\eta_x,\eta_y$ vary independently of one another and of $S$. Thus only the shared command survives in the covariance:

$$
\operatorname{Cov}(X,Y)=ab\operatorname{Var}(S),\qquad
\chi_Y=\frac{b^2\operatorname{Var}(S)}{\operatorname{Var}(Y)}
=\frac ba\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}.
$$

The last equality requires $a\ne0$. [Correlation alone does not give a shared variance fraction. That interpretation requires a model of the shared and private contributions and a calibrated gain.]{.key-statement} Private noise in $X$ lowers correlation by increasing $\sigma_X$, even when the shared command dominates $Y$.

<details class="publisher-long-content publisher-long-example">
<summary>Example: a weak correlation can accompany mostly shared movement</summary>
<div class="publisher-fold-body">

Choose unit gains and independent contributions with variances $\operatorname{Var}(S)=1$, $\operatorname{Var}(\eta_x)=24$, and $\operatorname{Var}(\eta_y)=0.25$, all in deg$^2$. Then $\operatorname{Var}(X)=25$, $\operatorname{Var}(Y)=1.25$, and $\operatorname{Cov}(X,Y)=1$ deg$^2$. Consequently

$$
\rho=\frac1{\sqrt{25\times1.25}}\simeq0.18,
\qquad \chi_Y=\frac1{1.25}=0.80.
$$

The prediction has large private noise, while measured movement has little. These chosen numbers illustrate the mechanism; they are not experimental estimates.

</div>
</details>

The 2022 analysis uses this logic for 350 ms displacements, assuming that calibration from larger movements still holds during drift. It also neglects a small covariance between the two private contributions, of order $1/N_m$ in its many motor neuron model. These are assumptions to check, not consequences of the covariance definition.[^tools-eye-shared] Many independent private contributions can average down in actual movement while remaining large in a single cell's prediction. Shared fluctuations survive that averaging; the paper's separate population bound tests whether independent motor noise alone could explain the observations.[^tools-eye-independent]

## Filtering changes how noise appears in eye motion {#sec:MATH-TOOLS-FILTERS}

Muscles take time to respond to neural commands. Could their response turn rapidly changing noise into the smooth, continuing motion seen during fixation? The answer depends on whether the input merely fluctuates or accumulates changes.

[A [**causal filter**]{.definition-term custom-style="Definition Term"} calculates present output from present and past input.]{.definition-explanation} For a linear response that does not change with time, [its [**impulse response**]{.definition-term custom-style="Definition Term"} $h(u)$ gives the surviving response after a unit impulse $u$ seconds ago.]{.definition-explanation} [The [**convolution**]{.definition-term custom-style="Definition Term"} adds these responses over the input history:]{.definition-explanation}

$$
E(t)=\int_0^\infty h(u)U(t-u)\,du.
$$

For a simple response, $h(u)=e^{-u/\tau}/\tau$ for $u\ge0$. Input $U$ and output $E$ are angles in degrees; $h$ has units s$^{-1}$ and response time $\tau$ is in seconds. Equivalently, $\tau\dot E=U-E$: the command's mismatch with current position drives velocity. [This is a [**low pass filter**]{.definition-term custom-style="Definition Term"}: it suppresses rapid changes relative to slow changes.]{.definition-explanation}

[[**White noise**]{.definition-term custom-style="Definition Term"} idealizes fluctuations uncorrelated at distinct times; in continuous time its intensity specifies variability of integrated input, rather than an ordinary finite pointwise variance.]{.definition-explanation} Passing it through this decaying filter produces a stationary position after initial transients: mean and variance stay constant and covariance depends only on time separation. Its mean squared displacement $M(\ell)=\mathbb E[(E(t+\ell)-E(t))^2]$ approaches a plateau. The lag $\ell$ is the separation between readings, not the clock time $t$.[^tools-eye-white]

A diffusing position command instead accumulates independent changes with displacement variance $2D\ell$, where $D$ has units deg$^2$/s. Filtering smooths its motion without stopping that accumulation. In the simple model below, short lag MSD grows as $\ell^2$ and long lag MSD grows linearly. Position is not stationary; its increments have statistics independent of $t$ once the initial velocity transient has decayed.

<details class="publisher-long-content publisher-long-example">
<summary>Example: the same filter separates fluctuating and accumulating input</summary>
<div class="publisher-fold-body">

For centered white input with $\mathbb E[U(t)U(t')]=A\delta(t-t')$, intensity $A$ has units deg$^2$ s. Overlap of the two impulse responses gives

$$
C_E(\ell)=A\int_0^\infty h(u)h(u+\ell)\,du
=\frac{A}{2\tau}e^{-\ell/\tau},\qquad
M_{\rm white}(\ell)=2[C_E(0)-C_E(\ell)].
$$

Thus $M_{\rm white}=(A/\tau)(1-e^{-\ell/\tau})$, approaching $A/\tau$. For a Brownian position input with diffusivity $D$, the same filter gives stationary velocity covariance $C_v(s)=(D/\tau)e^{-|s|/\tau}$. Integrating velocity over the displacement interval gives

$$
M_{\rm diffusion}(\ell)=2\int_0^\ell(\ell-s)C_v(s)\,ds
=2D[\ell-\tau(1-e^{-\ell/\tau})].
$$

Expansion at $\ell\ll\tau$ gives $(D/\tau)\ell^2$: velocity barely changes across that interval. For $\ell\gg\tau$, it approaches $2D(\ell-\tau)$, with continuing growth. White input instead has linear short lag MSD in this single exponential example. The input and filter together determine short lag behavior.

</div>
</details>

These calculations use one response time as a teaching simplification. The 2022 model includes two muscle response times and visual feedback. Its conclusions concern the measured lag range; smooth movement alone does not identify diffusion, and short lag behavior also depends on measurement error. The [eye drift](ch-eye-drift.html) and [timing](ch-eye-timing.html) chapters retain the full analysis.[^tools-eye-model]

[^tools-eye-shared]: Ben-Shushan et al. (2022), [calibration, Eqs. 4–7, PDF p. 9](../papers/ben-shushan-2022-fixational-drift.pdf#page=9), and [shared variance model, Eqs. 11–15, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10). The model with explicit gains and the numerical example are teaching constructions.

[^tools-eye-independent]: Ben-Shushan et al. (2022), [Supplementary Notes, independent contribution bound, Eqs. S1–S2, PDF p. 2](../papers/ben-shushan-2022-supplement-1.pdf#page=2).

[^tools-eye-white]: Ben-Shushan et al. (2022), [filtered white noise, Eqs. 20–22, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10). The normalized single exponential filter and filtered Brownian calculation are teaching reconstructions.

[^tools-eye-model]: Ben-Shushan et al. (2022), [muscle response, Eqs. 2–7, PDF p. 9](../papers/ben-shushan-2022-fixational-drift.pdf#page=9), [measurement error, Eqs. 18–19, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10), and [Supplementary Notes, visual feedback, PDF pp. 4–5](../papers/ben-shushan-2022-supplement-1.pdf#page=4).

