# Persistent neural activity can still accumulate memory error {#ch:FOUNDATIONS}

The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. Both abilities require a useful quantity to remain represented in a changing biological system. The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns.

The first distinction is between a value and the activity that represents it. Eye position is one number, but a circuit can represent it through thousands of neural activities. A disturbance can change those activities without changing the represented value. Another disturbance can leave a coherent activity pattern while changing the value. The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]

## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}

A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s. A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time. A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds.

Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s. In the models used here, an excitatory input increases a receiving neuron's tendency to fire and an inhibitory input reduces it. The effect of a spike can last beyond the spike itself because synaptic input decays over time. When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}. Such feedback can maintain activity after an external signal disappears.

A [**tuning curve**]{.definition-term custom-style="Definition Term"} gives a neuron's expected firing rate as a function of a represented variable. For eye angle $\theta$, a simple local model is $r_i(\theta)=b_i+k_i\theta$. Neuron $i$ has baseline rate $b_i$ in spikes per second and slope $k_i$ in spikes per second per degree. The linear expression can describe an active range, but it must be modified where it would predict negative firing. The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]

Different cells have different tuning curves. The vector

$$
\mathbf r(\theta)=\bigl(r_1(\theta),\ldots,r_N(\theta)\bigr)
$$

is a [**population code**]{.definition-term custom-style="Definition Term"}: the pattern across $N$ neurons carries information about $\theta$. The position of a cell in this vector is a neuron identity, rather than a location in physical space. Reading a value from observed spikes is [**decoding**]{.definition-term custom-style="Definition Term"}. Establishing a population pattern from an input is encoding. The 2012 paper asks how accurately the network can maintain such a pattern using its own noisy activity.

Spatial tuning gives a second example. In the hippocampus, a brain structure involved in memory and navigation, a [**place cell**]{.definition-term custom-style="Definition Term"} fires strongly in one or more localized regions of an environment. A connected region of elevated spatial firing is a [**place field**]{.definition-term custom-style="Definition Term"}. One neuron can have several fields. A [**rate map**]{.definition-term custom-style="Definition Term"} estimates the rate at each position by dividing the spikes recorded there by the time spent there. Sparse visits, smoothing, and firing cutoffs therefore affect the estimated map and its fields. A field in a model's expected rate and a field extracted from finite recordings are related objects with different measurement uncertainties.[^f-place]

The hippocampal areas CA3 and CA1 contain place cells. CA3 supplies major input to CA1 and has substantial recurrent excitation. CA1 also receives input from entorhinal cortex and has much less local recurrent excitation. A [**grid cell**]{.definition-term custom-style="Definition Term"}, found in entorhinal cortex, has repeated spatial fields that often form an approximately hexagonal pattern in a two-dimensional arena. These repeated grid fields and a place cell's irregular multiple fields should be kept distinct. A model explaining CA1's output maps need not identify where the animal's position estimate is maintained.[^f-anatomy]

## A variable spike count at a fixed rate {#sec:FOUNDATIONS-POISSON}

Even when the represented value stays fixed, the spikes need not repeat from trial to trial. The 2012 model starts with a tractable description of this variability: a [**Poisson process**]{.definition-term custom-style="Definition Term"}. At constant rate $r$, the number $K$ of spikes in an interval of length $\Delta t$ obeys

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

The variance follows directly from the first two factorial moments. Summing $k\Pr(K=k)$ gives $\lambda$. Likewise, summing $k(k-1)\Pr(K=k)$ gives $\lambda^2$. Since $K^2=K(K-1)+K$,

$$
\mathbb E[K^2]=\lambda^2+\lambda,
\qquad
\operatorname{Var}(K)=\mathbb E[K^2]-\mathbb E[K]^2=\lambda.
$$

:::

The count variance grows with rate, while its size relative to the mean falls. Its relative standard deviation is $\sqrt\lambda/\lambda=1/\sqrt\lambda$. This is why collecting more independent spikes can improve a rate estimate. It also means that increasing a firing-rate scale does not keep absolute noise amplitude fixed. Comparisons between networks must specify which quantities are held constant.[^f-poisson]

[**Example: an apparently silent cell and an informative population**]{#sec-foundations-count-example}

Suppose the expected rate is 20 spikes per second and an observation lasts 50 ms. The expected count is $20\times0.05=1$. The probability of seeing no spike is $e^{-1}=0.368$. A silent interval is therefore common even though the expected rate is positive.

Now suppose 20 conditionally independent cells each have that rate. Their total count is Poisson with mean 20 and standard deviation $\sqrt{20}=4.47$. The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell. Population averaging helps because the independent count variances add while the mean signal adds directly. If cells share an additional fluctuating drive, that common variation will not disappear in the same way.

The two count distributions can be compared on the same rate per cell scale.

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-POISSON-POPULATION}}

</div>

Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed, while independent averaging reduces its relative spread. See [Poisson count likelihood, SI Eq. S43, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9).

For changing rates, the expected count is the integral $\lambda=\int r(t)\,dt$. In a recurrent network, $r(t)$ itself depends on past activity. The useful independence statement is therefore conditional: given the current modeled state, the elementary spike-generation noise is independent across cells in the basic 2012 model. Averaging over the evolving state can still produce correlations across time and across neurons. This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains.

Other measurements describe other aspects of variability. The [**coefficient of variation**]{.definition-term custom-style="Definition Term"}, or CV, of interspike intervals is their standard deviation divided by their mean. A homogeneous Poisson process has exponential intervals and CV equal to one. More regular firing can have CV below one, as in the ocular motor neurons analyzed in 2022. The count variance divided by mean count is the [**Fano factor**]{.definition-term custom-style="Definition Term"}; its value also depends on the counting interval. CV and Fano factor cannot be substituted for one another without additional assumptions.

## Mean squared displacement combines random spread with mean motion {#sec:FOUNDATIONS-COVARIANCE}

To identify where variability enters a pathway, the eye paper compares measurements that share some fluctuations and have other fluctuations of their own. The required probability identities are short, but their interpretation matters.

For random variables $X$ and $Y$, [**covariance**]{.definition-term custom-style="Definition Term"} measures how their centered values vary together:

$$
\operatorname{Cov}(X,Y)=
\mathbb E[(X-\mathbb E[X])(Y-\mathbb E[Y])].
$$

It has units equal to the product of the units of $X$ and $Y$. Variance is the special case $\operatorname{Cov}(X,X)$. Expanding a centered sum or difference gives

$$
\operatorname{Var}(X\pm Y)=
\operatorname{Var}(X)+\operatorname{Var}(Y)
\pm2\operatorname{Cov}(X,Y).
$$

Independence makes the covariance zero when the relevant moments exist. Zero covariance alone does not imply independence in general. The [**correlation coefficient**]{.definition-term custom-style="Definition Term"} rescales covariance:

$$
\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}
{\sqrt{\operatorname{Var}(X)\operatorname{Var}(Y)}}.
$$

It has no units and lies between $-1$ and $1$ for variables with nonzero variance. The magnitude of a correlation is not automatically the fraction of an output variance caused by a particular source. Establishing that interpretation requires a model of the signal, noise, and measurement gains. Chapter 4 supplies that model for eye displacement.

The quantity that changes between two times is a displacement $\Delta x=x(t+\ell)-x(t)$, where $\ell$ is a time lag. Its mean square splits into

$$
\mathbb E[(\Delta x)^2]=
\operatorname{Var}(\Delta x)+\mathbb E[\Delta x]^2.
$$

Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both. This identity will distinguish random memory diffusion from a biased or leaky integrator.

## Stable activity with a vulnerable stored value {#sec:FOUNDATIONS-ATTRACTOR}

A circuit's current activities are its [**state**]{.definition-term custom-style="Definition Term"}. A dynamical equation specifies how that state changes. A [**fixed point**]{.definition-term custom-style="Definition Term"} is a state where the deterministic rate of change is zero. It is stable in a direction if a small disturbance in that direction decays.

Memory of a continuous quantity calls for a family of persistent states. A [**continuous attractor**]{.definition-term custom-style="Definition Term"} is a continuous family of fixed points with restoring dynamics toward the family and a neutral direction along it. Neutral means that there is no restoring force along that direction in the ideal deterministic model. The family is an [**attractor manifold**]{.definition-term custom-style="Definition Term"}. Its dimension counts independent coordinates represented on it, rather than neurons in the circuit. A line attractor has one represented coordinate; a ring can represent a periodic coordinate such as heading.[^f-memory]

[**Example: two disturbances to the same stored angle**]{#sec-foundations-attractor-example}

Consider a teaching model with two activities $r_1,r_2$ in spikes per second. Let $b=40$ spikes per second and let $k=2$ spikes per second per degree. A stored angle $\theta$ corresponds to

$$
r_1=b+k\theta,\qquad r_2=b-k\theta.
$$

The fixed points lie on the line $r_1+r_2=2b$. Restrict attention to angles where both rates remain positive. Define the deviation in their mean activity and the represented angle as

$$
x=\frac{r_1+r_2}{2}-b,
\qquad
\theta=\frac{r_1-r_2}{2k}.
$$

Suppose each activity changes according to

$$
\dot r_1=-a x,\qquad \dot r_2=-a x,
$$

where $a>0$ has units inverse seconds. Adding and subtracting these equations gives

$$
\dot x=-a x,\qquad \dot\theta=0.
$$

The first equation has solution $x(t)=x(0)e^{-at}$, so disturbances in the common activity decay. The second equation retains any angle set by the initial state.

At $\theta=5$ degrees, the rates are $(50,30)$. A disturbance of $(+3,+3)$ changes them to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$. A disturbance of $(+3,-3)$ instead gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response. The circuit remains coherent while holding the wrong angle.

The two changes occupy different directions in the activity plane. The solid arrow in the figure is the restoring motion produced by the model. The dashed arrow shows the imposed disturbance along the fixed-point line, rather than a deterministic restoring flow.

{{block:fig:FOUNDATIONS-ATTRACTOR}}

This construction illustrates the geometry; it is not a fit to eye-neuron recordings. In a larger network, the direction that survives depends on its connection weights and cannot always be found by an ordinary perpendicular projection. Chapter 2 derives the correct projection from the network's linearized dynamics.

## Independent steps with equal duration and variance give linear variance growth {#sec:FOUNDATIONS-DIFFUSION}

If persistent angular changes arrive repeatedly, their errors accumulate. Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. Assume independent increments with mean zero and variance $2D\Delta t$, where $D$ has units coordinate squared per time. After $n$ intervals,

$$
\theta_n-\theta_0=\sum_{j=1}^{n}\xi_j,
\qquad
\operatorname{Var}(\theta_n-\theta_0)
=\sum_{j=1}^{n}\operatorname{Var}(\xi_j)
=2Dn\Delta t.
$$

Writing $t=n\Delta t$ gives linear variance growth $2Dt$. In the continuous diffusion approximation this becomes

$$
\theta(t)=\theta(0)+\sqrt{2D}\,W(t),
\qquad
\mathbb E[(\theta(t)-\theta(0))^2]=2Dt.
$$

The [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$ starts at zero, has independent Gaussian increments, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$. It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation. The parameter $D$ is its [**diffusion coefficient**]{.definition-term custom-style="Definition Term"}. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.

The [**mean squared displacement**]{.definition-term custom-style="Definition Term"}, or MSD, is the expected squared change across a lag. In the zero-mean diffusion just defined, MSD is $2Dt$. A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate. In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient. A paper that defines its diffusion parameter as the entire two-dimensional MSD slope uses a different convention.

[**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}

Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second. At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes. At 1 s the root mean squared displacement is 0.20 degrees. These are teaching values, not a new estimate from either monkey.

If there is also a constant bias velocity $v=0.10$ degrees per second, then

$$
\theta(t)-\theta(0)=vt+\sqrt{2D}\,W(t),
\qquad
\operatorname{MSD}(t)=v^2t^2+2Dt.
$$

The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. Removing systematic drift is therefore a substantive assumption in a theory devoted to random diffusion.

Sample paths show the irregular motion; exact displacement scales show how its spread differs from a fixed bias.

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-DIFFUSION-BIAS}}

</div>

A single path can turn back toward zero even while the root mean squared displacement grows. A constant bias grows linearly, so it eventually exceeds the square root growth of the random displacement scale. See [Gaussian displacement density, SI Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7).

Two times along a Brownian path are correlated even though its increments are independent. For $0\leq s\leq t$, write $W(t)=W(s)+[W(t)-W(s)]$. The bracketed increment is independent of $W(s)$ and has mean zero, giving

$$
\operatorname{Cov}(W(s),W(t))
=\operatorname{Var}(W(s))=s,
\qquad
\operatorname{Cov}(W(s),W(t))=\min(s,t).
$$

The same argument gives covariance $2D\min(s,t)$ for a diffusing coordinate started at a fixed value. This identity is the intermediate step needed to compute the error from averaging a memory that moves during readout. It also helps explain why smoothing a diffusive input is different from smoothing a stationary noise source.

A finite range, a periodic coordinate, external feedback, or a position-dependent diffusion coefficient changes long-time behavior. For example, ordinary squared angular distance on a ring cannot keep growing linearly forever. The basic $2Dt$ result is local or unbounded unless those conditions are treated separately.

## A fixed spatial map differs from a value that wanders over time {#sec:FOUNDATIONS-RANDOMNESS}

The memory and eye papers study fluctuations that accumulate as time passes. The place-field paper instead starts with a random function of physical position. Once drawn for a cell and an environment, that function is fixed while the animal moves through the map. Revisiting a place evaluates the same expected-rate function, although the actual spikes can still vary from visit to visit.

These two kinds of randomness can occur together. A circuit may maintain a position estimate with time-dependent noise, while downstream cells respond to position through irregular but repeatable tuning curves. Observing irregular spatial maps does not tell us how fast the maintained position drifts. Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields. The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place]

The three questions can now be placed beside the kind of variation each paper studies.

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-PAPER-MAP}}

</div>

The rows compare different questions; they do not establish a single circuit connecting all three papers.

[^f-memory]: Burak, Y., and Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [https://doi.org/10.1073/pnas.1117386109](https://doi.org/10.1073/pnas.1117386109). Introduction, Fig. 1, and SI I–III. The two-activity example is a guide construction illustrating the geometry, not the paper's simulated network.

[^f-eye]: Ben-Shushan, N., Shaham, N., Joshua, M., and Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [https://doi.org/10.1038/s41467-022-29201-y](https://doi.org/10.1038/s41467-022-29201-y). Introduction, Figs. 1–2, and Methods, Eqs. 2–7.

[^f-place]: Mainali, N., Azeredo da Silveira, R., and Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [https://doi.org/10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017). Introduction, Results, and STAR Methods. The distinction between map randomness and visit-to-visit spike variation follows from what the model's random function indexes.

[^f-anatomy]: Maimon, S. R., and colleagues (2026). *Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1*. Nature. [https://doi.org/10.1038/s41586-026-10537-0](https://doi.org/10.1038/s41586-026-10537-0). Main text, Introduction and Figs. 1–2. The present guide uses this later comparison for anatomical and coding context; it is not evidence reported in the 2025 paper.

[^f-poisson]: Burak, Y., and Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). Results and Methods, Eqs. 7–10, describe the Poisson spike model and weak-fluctuation approximation. The finite count calculations in this section are direct consequences of the Poisson distribution and are guide derivations.
