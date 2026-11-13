# Patterns of variable spikes can represent a value {#ch:FOUNDATIONS}

<!-- vale ai-tells.CataphoricForecasting = NO -->
<!-- vale ai-tells.VerbTricolon = NO -->
The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. [Both abilities require a useful quantity to remain represented in a changing biological system.]{.key-statement} The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns.
<!-- vale ai-tells.VerbTricolon = YES -->
<!-- vale ai-tells.CataphoricForecasting = YES -->

Before asking how a circuit keeps a value, we need to know how its activity represents that value and what makes the activity variable. We begin with the spikes that cells send and the patterns of firing rates across a population. A model of spike counts then shows why one brief observation can be uncertain and how combining counts from several cells can help. We then learn how to tell whether measurements vary together and how to separate random spreading from a change in the average value. Those distinctions will let us interpret both a memory model and measurements of eye motion.

## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}

<!-- vale ai-tells.StrawmanContrast = NO -->
[A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} [A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time.]{.definition-explanation} A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds.
<!-- vale ai-tells.StrawmanContrast = YES -->

[Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} In the models used here, inputs have two contrasting effects:

- [An [**excitatory input**]{.definition-term custom-style="Definition Term"} increases a receiving neuron's tendency to fire.]{.definition-explanation}
- [An [**inhibitory input**]{.definition-term custom-style="Definition Term"} reduces it.]{.definition-explanation}

The effect of a spike can last beyond the spike itself because synaptic input decays over time. [When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Such feedback can maintain activity after an external signal disappears.

[A [**tuning curve**]{.definition-term custom-style="Definition Term"} gives a neuron's expected firing rate as a function of a represented variable.]{.definition-explanation} For eye angle $\theta$, a simple local model is $r_i(\theta)=b_i+k_i\theta$. Neuron $i$ has baseline rate $b_i$ in spikes per second and slope $k_i$ in spikes per second per degree. The linear expression can describe an active range, but it must be modified where it would predict negative firing. The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]

Different cells have different tuning curves. The vector

$$
\mathbf r(\theta)=\bigl(r_1(\theta),\ldots,r_N(\theta)\bigr)
$$

<!-- vale ai-tells.FigurativeCarries = NO -->
<!-- vale ai-tells.StrawmanContrast = NO -->
[is a [**population code**]{.definition-term custom-style="Definition Term"}: the pattern across $N$ neurons carries information about $\theta$.]{.definition-explanation} The position of a cell in this vector is a neuron identity, rather than a location in physical space. [Reading a value from observed spikes is [**decoding**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} [Establishing a population pattern from an input is [**encoding**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} [The 2012 paper asks how accurately the network can maintain such a pattern using its own noisy activity.]{.key-statement}
<!-- vale ai-tells.StrawmanContrast = YES -->
<!-- vale ai-tells.FigurativeCarries = YES -->

<!-- vale ai-tells.FormalTransitions = NO -->
Spatial tuning gives a second example. In the hippocampus, a brain structure involved in memory and navigation, a place cell fires strongly in one or more localized regions of an environment. A connected region of elevated spatial firing is a place field. One neuron can have several fields. [A [**rate map**]{.definition-term custom-style="Definition Term"} estimates the rate at each position by dividing the spikes recorded there by the time spent there.]{.definition-explanation} Sparse visits, smoothing, and firing cutoffs therefore affect the estimated map and its fields. A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place]
<!-- vale ai-tells.FormalTransitions = YES -->

The hippocampal areas CA3 and CA1 contain place cells, but their connections differ:

- CA3 supplies major input to CA1 and has substantial recurrent excitation.
- CA1 also receives input from entorhinal cortex and has much less local recurrent excitation.

[A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena.]{.definition-explanation} These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]

## A variable spike count at a fixed rate {#sec:FOUNDATIONS-POISSON}

A tuning curve describes expected activity, but a brief spike observation can differ each time the same value is represented. [The 2012 model describes this variability with a [**Poisson process**]{.definition-term custom-style="Definition Term"}. At constant rate $r$, the number $K$ of spikes in an interval of length $\Delta t$ obeys]{.definition-explanation}

$$
\Pr(K=k)=e^{-\lambda}\frac{\lambda^k}{k!},
\qquad \lambda=r\Delta t,
\qquad k=0,1,2,\ldots .
$$

Here $\lambda$ is an expected count, so it has no units. For this distribution,

$$
\mathbb E[K]=\lambda,
\qquad \operatorname{Var}(K)=\lambda.
$$

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: why a Poisson count has variance equal to its mean"}

<!-- vale ai-tells.FormalTransitions = NO -->
Summing $k\Pr(K=k)$ gives $\lambda$. Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$. Since $K^2=K(K-1)+K$,
<!-- vale ai-tells.FormalTransitions = YES -->

$$
\mathbb E[K^2]=\lambda^2+\lambda,
\qquad
\operatorname{Var}(K)=\mathbb E[K^2]-\mathbb E[K]^2=\lambda.
$$

:::

<!-- vale ai-tells.FormalTransitions = NO -->
The count variance grows with rate, while its size relative to the mean falls. Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$. This is why collecting more independent spikes can improve a rate estimate. It also means that increasing a firing-rate scale does not keep absolute noise amplitude fixed. Comparisons between networks must specify which quantities are held constant.[^f-poisson]
<!-- vale ai-tells.FormalTransitions = YES -->

<div class="publisher-worked-calculation publisher-fold-always">

[**Example: an apparently silent cell and an informative population**]{#sec-foundations-count-example}

<!-- vale ai-tells.FormalTransitions = NO -->
Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms. The expected count is $20\times0.05=1$. The probability of seeing no spike is $e^{-1}=0.368$. A silent interval is therefore common even though the expected rate is positive.
<!-- vale ai-tells.FormalTransitions = YES -->

Now suppose 20 conditionally independent cells each have that rate. Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$. The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell. [Population averaging helps because the independent count variances add while the mean signal adds directly. If a common varying input makes several cells' firing rates rise and fall together, that shared variation will not disappear in the same way.]{.key-statement}

<!-- vale ai-tells.CataphoricForecasting = NO -->
The two count distributions can be compared on the same rate per cell scale.
<!-- vale ai-tells.CataphoricForecasting = YES -->

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-POISSON-POPULATION}}

</div>

Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed, while independent averaging reduces its relative spread. See [Poisson count likelihood, SI Eq. S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9).

</div>

<!-- vale ai-tells.FormalTransitions = NO -->
For changing rates, the expected count is the integral $\lambda=\int r(t)\,dt$. In a recurrent network, $r(t)$ itself depends on past activity. The useful independence statement is therefore conditional: given the current modeled state, the elementary spike-generation noise is independent across cells in the basic 2012 model. Averaging over the changing state can still produce correlations across time and across neurons. This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains.
<!-- vale ai-tells.FormalTransitions = YES -->

<!-- vale ai-tells.CataphoricForecasting = NO -->
Two other measurements describe different aspects of variability:
<!-- vale ai-tells.CataphoricForecasting = YES -->

- [The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals, the times between successive spikes, is their standard deviation divided by their mean.]{.definition-explanation} A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022.
- [The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}]{.definition-explanation}. Its value also depends on the counting interval.

CV and Fano factor cannot be substituted for one another without additional assumptions.

## Shared neural signals and a biased command leave different signs in eye motion {#sec:FOUNDATIONS-COVARIANCE}

During fixation, a monkey tries to keep looking at a stationary target, yet its eye moves slightly. A changing command from the brain can make many motor neurons change their firing together. Their spikes act on the eye muscles, which turn the eye. An individual motor neuron also adds spike variability of its own. The 2022 paper asks how much of the observed movement follows a shared neural command, and whether that command itself wanders over time.[^f-eye]

<!-- vale ai-tells.NegatedSubject = NO -->
[Covariance asks which recorded changes occur together. Displacement statistics ask how far the eye moves and how that movement grows with elapsed time.]{.key-statement} Neither measurement by itself identifies the neural circuit responsible.
<!-- vale ai-tells.NegatedSubject = YES -->

<!-- vale ai-tells.ContrastiveFormulas = NO -->
**Physical meaning: a shared command can survive averaging across neurons.** If a common input raises the firing of many motor neurons that pull the eye in the same direction, their effects add. Independent extra and missing spikes partly cancel when those neurons act together. The paper compares the measured eye displacement with a displacement predicted from one neuron's spikes, after converting both to degrees. That prediction is an analysis of a recording, not an extra command sent to the muscles. A relationship between the two is evidence to test against a model of shared input and private noise. It does not mean that the one recorded cell causes all the movement.
<!-- vale ai-tells.ContrastiveFormulas = YES -->

[**Covariance**]{.definition-term custom-style="Definition Term"} [measures whether two signals tend to be above their own averages together or on opposite sides of those averages.]{.definition-explanation} Positive covariance between the two displacements means that above-average changes in the neural prediction tend to accompany above-average changes in eye position. [The [**correlation coefficient**]{.definition-term custom-style="Definition Term"}, written $\rho$, expresses this shared variation relative to the spread of each signal.]{.definition-explanation} Extra private noise can lower $\rho$ even when the shared drive has not weakened. The [eye-drift calculation](ch-eye-drift.html#sec-eye-chi) explains why a modest correlation need not mean a small shared contribution to movement.

::: {.publisher-clarification-note .publisher-fold-always title="Mathematical definitions: covariance, variance and correlation"}

Let $X$ and $Y$ be the two displacements, in degrees, across repeated intervals of the same duration. Subtracting each average leaves its fluctuation. Their covariance is

$$
\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb E[X])(Y-\mathbb E[Y])].
$$

Here it has units degrees squared. In general its units are the product of the two signals' units. Variance is $\operatorname{Cov}(X,X)$. Expanding the square of a centered sum or difference gives

$$
\operatorname{Var}(X\pm Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)\pm2\operatorname{Cov}(X,Y).
$$

For nonzero variances, correlation is

$$
\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}.
$$

<!-- vale ai-tells.NegatedObject = NO -->
<!-- vale ai-tells.ParallelStaccato = NO -->
It is dimensionless and lies between $-1$ and $1$. Independence gives zero covariance when these moments exist. Zero covariance alone does not imply independence.
<!-- vale ai-tells.ParallelStaccato = YES -->
<!-- vale ai-tells.NegatedObject = YES -->

To see the physical roles, write $X=g_X S+\epsilon_X$ and $Y=g_Y S+\epsilon_Y$. Here $S$ is a shared displacement signal in degrees, the dimensionless [**gain**]{.definition-term custom-style="Definition Term"}s $g_X,g_Y$ multiply its contribution in each recording, and $\epsilon_X,\epsilon_Y$ are private contributions in degrees. If all three random contributions are independent,

$$
\operatorname{Cov}(X,Y)=g_Xg_Y\operatorname{Var}(S),\qquad
\operatorname{Var}(X)=g_X^2\operatorname{Var}(S)+\operatorname{Var}(\epsilon_X).
$$

Increasing private variance increases the denominator of $\rho$ without increasing the covariance. Changing a gain changes the measured covariance even if the shared source is unchanged. This simple construction explains the need for calibration and explicit noise assumptions. It is not the paper's full inference model.

:::

**Physical meaning: random wandering differs from a persistent directional error.** Let $x(t)$ be horizontal eye angle in degrees and let $\ell$ be the time between two measurements, called the lag, in seconds. [The [**displacement**]{.definition-term custom-style="Definition Term"} $\Delta x=x(t+\ell)-x(t)$ is the change in that angle.]{.definition-explanation} A random change in the maintained command can move the eye left in one interval and right in another. The average displacement can then be close to zero while individual displacements are large. A persistent imbalance in the command can instead make the average displacement grow in one direction. Muscles smooth the command before it becomes eye movement, so the timescale of the observation also matters.

[The **mean squared displacement**, or MSD, averages $(\Delta x)^2$ across repeated intervals and has units degrees squared.]{.definition-explanation} Its two contributions are

$$
\mathbb E[(\Delta x)^2]=\operatorname{Var}(\Delta x)+\mathbb E[\Delta x]^2.
$$

<!-- vale ai-tells.VerbTricolon = NO -->
[A larger MSD can mean stronger random movement, a larger directional bias, or both. Measuring the mean displacement separately prevents mistaking bias for increased noise.]{.key-statement}
<!-- vale ai-tells.VerbTricolon = YES -->

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: separating spread from mean displacement"}

Write $\mu=\mathbb E[\Delta x]$ and $\eta=\Delta x-\mu$, so $\mathbb E[\eta]=0$. Squaring and averaging gives

$$
\mathbb E[(\mu+\eta)^2]=\mu^2+2\mu\mathbb E[\eta]+\mathbb E[\eta^2]
=\mu^2+\operatorname{Var}(\Delta x).
$$

The cross term vanishes because the fluctuations are measured relative to their own mean. This identity needs finite second moments, but no diffusion assumption.

:::

**What changes the physical movement?** The model must say which part of the pathway a parameter controls:

- **Random changes in the stored command:** more frequent or larger lasting changes make the stored angle spread faster. The next chapter calls this rate of spreading the diffusion coefficient $D$ and explains why it depends on spike variability and the circuit's response to each spike.
  <!-- vale ai-tells.LabelAndExplain = NO -->
- **A persistent directional imbalance:** this changes the mean displacement. In a constant-velocity approximation, doubling that velocity doubles the mean displacement at a fixed lag and quadruples its squared contribution to MSD.
  <!-- vale ai-tells.LabelAndExplain = YES -->
- **The gain from command to eye angle:** multiplying the command's contribution to each displacement by a gain $G$ multiplies that contribution's variance and MSD by $G^2$, with the input fluctuations held fixed. Any noise added after that gain needs to be counted separately. A fitted tuning slope, which describes rate as a function of angle, is not by itself a causal muscle gain.
- **Muscle response time:** a slower response smooths rapid command changes more strongly. It changes the short-lag shape of the MSD curve, not just its height. The [timing chapter](ch-eye-timing.html#sec-eye-filtered-msd) separates this smoothing from growth of noise inside the memory circuit.

<!-- vale ai-tells.FormalTransitions = NO -->
Measurement error is a separate contribution: it changes recorded positions without moving the eye. Independent zero-mean position errors, each of variance $\sigma_m^2$ and independent of true motion, add $2\sigma_m^2$ to displacement MSD at nonzero lags. Thus an upward shift in the observed curve need not be a physical increase in movement. The [measurement-noise calculation](ch-eye-timing.html#sec-eye-measurement-noise) shows the conditions needed to remove it.
<!-- vale ai-tells.FormalTransitions = YES -->

The next chapter follows the proposed source upstream: how a circuit can keep a pattern of activity while random spikes change the angle that pattern represents.

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-eye]: Ben-Shushan, N., Shaham, N., Joshua, M., and Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [DOI](https://doi.org/10.1038/s41467-022-29201-y). Introduction, Figs. 1–2, and Methods, Eqs. 2–7.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-place]: Mainali, N., Azeredo da Silveira, R., and Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [DOI](https://doi.org/10.1016/j.neuron.2025.01.017). Introduction, Results, and STAR Methods. The distinction between map randomness and visit-to-visit spike variation follows from what the model's random function indexes.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-anatomy]: Maimon, S. R., and colleagues (2026). *Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1*. Nature. [DOI](https://doi.org/10.1038/s41586-026-10537-0). Main text, Introduction and Figs. 1–2. The present guide uses this later comparison for anatomical and coding context. It is not evidence reported in the 2025 paper.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-poisson]: Burak, Y., and Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). Results and Methods, Eqs. 7–10, describe the Poisson spike model and weak-fluctuation approximation. The finite count calculations in this section are direct consequences of the Poisson distribution and are guide derivations.
<!-- vale ai-tells.EmDashUsage = YES -->
