# Mathematical tools connect neural signals to the papers' predictions {#ch:MATHEMATICAL-TOOLS}

**Unreviewed draft diagrams.** These AI-generated images may contain incorrect or missing labels, arrows, formulas and numbers. Use the chapter text and paper links as the source for the explanation.

{{block:fig:DRAFT-MAP-FRONT-MATHEMATICAL-TOOLS-A}}

{{block:fig:DRAFT-MAP-FRONT-MATHEMATICAL-TOOLS-B}}


The three papers ask different questions about neural activity. How accurately can a circuit retain a value? What do fluctuations in neural recordings reveal about eye movement? Why do place cells have fields of different sizes and shapes? Each question needs a mathematical tool whose variables correspond to a physical part of the system.

This chapter introduces those tools before their use in Parts I and II. It assumes calculus, linear algebra and basic probability, including expected value, variance, standard deviation and probability density. The main text explains the physical meanings and conclusions; folded calculations supply the longer steps. The reading paths are:

- **Memory, Burak and Fiete (2012):** [connection weights](#sec-math-tools-weights) describe how neurons sustain activity, and [Fisher information](#sec-math-tools-fisher) measures precision in their spikes. The [information bound](#sec-math-tools-bound) connects that precision to memory spreading. Chapters 1–6 develop the model and proofs.
- **Eye drift, Ben-Shushan et al. (2022):** [covariance](#sec-math-tools-shared) tests for shared fluctuations, and [filtering](#sec-math-tools-filters) describes how neural signals become eye motion. Chapters 7–9 apply the tools to recordings and a circuit model.
- **Place fields, Mainali et al. (2025):** [random fields](#sec-math-tools-random-fields) describe correlated input over space; [crossings and peak geometry](#sec-math-tools-crossings-peaks) connect that input to field counts and sizes. Chapters 10–12 derive and test those predictions.

For a quick return to the complete arguments, use the [Results and connections](ch-exam-review.html): reasoning chains, formulas, symbol keys and exact locations.

## Connection weights determine how neurons sustain activity {#sec:MATH-TOOLS-WEIGHTS}

A single neural signal is brief, so retaining a value requires something to carry its effect forward. [A [**spike**]{.definition-term custom-style="Definition Term"} is a brief electrical event emitted by a neuron.]{.definition-explanation} [Its [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time.]{.definition-explanation} A rate gives an expectation; it does not specify an evenly spaced sequence of spikes.

In Burak and Fiete's (2012) model, a spike leaves a longer-lasting effect on the cells receiving it. [The [**synaptic activation**]{.definition-term custom-style="Definition Term"} $s_j$ tracks the remaining effect of neuron $j$'s outgoing spikes.]{.definition-explanation} Each spike increases $s_j$ by one, and between spikes it decays with time constant $\tau$, measured in seconds. The changing activation therefore carries the effect of earlier spikes into the present.[^tools-model]

How does that effect change another cell's activity? [The [**connection matrix**]{.definition-term custom-style="Definition Term"} $W$ lists the strengths and signs of all the modeled neural connections: $W_{ij}$ converts neuron $j$'s activation into input to neuron $i$.]{.definition-explanation} For $N$ neurons it is an $N\times N$ matrix. Rows identify receiving cells; columns identify sending cells. Each receiver adds its weighted inputs and a constant background input:

$$
g_i=\sum_jW_{ij}s_j+b_i,
\qquad r_i=\phi(g_i).
$$

Here $g_i$ is the total input, $b_i$ is its constant bias, and $r_i$ is the firing rate in spikes per second. The function $\phi$ converts total input into a nonnegative rate. Activations are dimensionless in this one-unit-per-spike convention, so $W_{ij}$ has input units per activation unit and $b_i$ has the same units as $g_i$. A positive weight raises input, a negative weight lowers it, and zero means no direct influence in the model. These signs raise or lower firing when $\phi$ increases with input.

The equations describe a complete feedback cycle:

1. A spike from cell $j$ increases $s_j$.
2. Receiving cell $i$ gets an input change $W_{ij}$, which can change its firing rate.
3. Its later spikes change other cells' inputs, including paths that return to the original cell.

Consider two mutually inhibiting populations. If population 1 becomes more active, it inhibits population 2 more strongly. Population 2 then fires less and inhibits population 1 less strongly. With the paper's particular balance of weights, decay and rate response, the circuit restores changes in the total activation while leaving a change in the activation difference in place. That difference stores the value. Arbitrary mutual inhibition does not guarantee this balance.

<details class="publisher-long-content publisher-long-example">
<summary>Example: feedback preserves a difference while correcting the total activity</summary>
<div class="publisher-fold-body">

Use the two-unit model with $W_{12}=W_{21}=-1$, zero self-weights, equal biases $b>0$, and $\phi(g)=g/\tau$ where both inputs are positive. Replacing spike events by their mean rate gives $\dot s_i=-s_i/\tau+r_i$. Substitution gives

$$
\tau\dot s_1=b-s_1-s_2,
\qquad \tau\dot s_2=b-s_1-s_2.
$$

For total activation $S=s_1+s_2$ and difference $\theta_s=s_1-s_2$,

$$
\dot S=\frac{2(b-S)}{\tau},\qquad \dot\theta_s=0.
$$

An equal increase in both activations raises $S$ above $b$, and the circuit drives it back down. A difference between the activations persists. For the illustrative choice $b=20$, the states $(s_1,s_2)=(12,8)$ and $(8,12)$ both have the required total but store different values, $4$ and $-4$. The weights and transfer rule are as in the paper's mutual-inhibition model; the calculation uses mean rates without random spikes. It does not imply that every inhibitory pair stores a continuous value. Both steady rates are positive only for $|\theta_s|<b$.

</div>
</details>

If $W=0$ in this model, rates become the constants $\phi(b_i)$. Any difference due to the initial synaptic activations then decays toward the bias-determined state. Connections allow the present activity to influence what happens next; their arrangement determines whether the circuit preserves a useful pattern. [The weights stay fixed during storage. The remembered value is carried by changing neural activity, rather than by changing the weights.]{.key-statement} Chapter 1 gives the [full spike and activation equations](../chapters/ch-foundations.html#sec-memory-spikes); Chapter 3 calculates which disturbances those interactions remove and which leave a lasting memory change.

In the model without spike fluctuations, [a [**fixed point**]{.definition-term custom-style="Definition Term"} is an activity pattern whose activations have zero rate of change.]{.definition-explanation} The tuned memory circuit has a continuous family of these patterns, each labeled by a represented value $\theta$. Small disturbances away from the family relax toward a member of it, which may differ from the original member. A shift along the family changes the represented value without being restored. [The direction along the family is its [**neutral tangent**]{.definition-term custom-style="Definition Term"}: a small displacement in that direction neither grows nor decays under the local noise-free dynamics.]{.definition-explanation}

Near one fixed pattern, the network's linear response matrix $K$ describes how a small activation disturbance $\delta\mathbf s$ changes: $d(\delta\mathbf s)/dt\simeq K\delta\mathbf s$. A small change $\delta s_j$ in cell $j$'s activation contributes $K_{ij}\delta s_j$ to the rate of change of cell $i$'s activation. If a right eigenvector $\mathbf z$ satisfies $K\mathbf z=\lambda\mathbf z$, a disturbance initially in that direction evolves as $e^{\lambda t}\mathbf z$. The eigenvalue $\lambda$ has units of inverse time. A negative real eigenvalue gives decay; zero gives a neutral direction. For complex eigenvalues, the sign of the real part controls growth or decay, while the imaginary part describes oscillation; real disturbances use the real and imaginary components together. Write $\bar{\mathbf s}(\theta)$ for the noise-free activations at value $\theta$. Their derivative $\mathbf u=d\bar{\mathbf s}/d\theta$ is the neutral tangent and satisfies $K\mathbf u=0$.

The network can return to the family along a tilted path. Let $\delta\theta$ be the lasting change in represented value. [The [**left zero eigenvector**]{.definition-term custom-style="Definition Term"} $\mathbf v$ satisfies $\mathbf v^TK=0$ and is normalized so that $\mathbf v^T\mathbf u=1$. It extracts the lasting coordinate change from a small disturbance: $\delta\theta=\mathbf v^T\delta\mathbf s$.]{.definition-explanation} The first condition makes $\mathbf v^T\delta\mathbf s$ constant during the noise-free linear return; the second makes a change along $\mathbf u$ read out in units of $\theta$. It need not point along $\mathbf u$: unlike a perpendicular projection, it incorporates the circuit's return path. Chapter 3 derives it for the neural model.

<details class="publisher-long-content publisher-long-example">
<summary>Example: a disturbance can move sideways while it decays</summary>
<div class="publisher-fold-body">

Let $x$ be a coordinate along a line of fixed states and $y$ a disturbance away from it; take both as dimensionless activation coordinates. Consider $\dot x=ay$, $\dot y=-by$, with $b>0$ and $a$ and $b$ in inverse seconds. The response matrix and two directions are

$$
K=\begin{pmatrix}0&a\\0&-b\end{pmatrix},\qquad
\mathbf u=\binom{1}{0},\qquad
\mathbf v=\binom{1}{a/b}.
$$

$K\mathbf u=0$, $\mathbf v^TK=0$, and $\mathbf v^T\mathbf u=1$. Starting at $(x_0,y_0)$, the disturbance $y$ decays as $y_0e^{-bt}$, but it also changes $x$. Integrating $\dot x$ gives $x(\infty)=x_0+(a/b)y_0$. Thus $\mathbf v^T(x_0,y_0)^T$ gives the final position on the fixed line. A perpendicular projection would give $x_0$ and miss that shift. The model is an illustration; it is not a fitted neural circuit.

</div>
</details>

Random spike counts also need a bridge to the continuous noise used later. Many weak, sufficiently independent contributions to a receiver can sum to an approximately Gaussian fluctuation. [Matching its mean and variance specifies the proposed approximation's scale; those two moments alone do not prove that the fluctuation is Gaussian.]{.key-statement} The network limit also requires an appropriate population and time-scale separation. Chapter 3 states how this approximation is used.

<details class="publisher-long-content publisher-long-example">
<summary>Example: averaging independent spike counts</summary>
<div class="publisher-fold-body">

Suppose $N$ independent cells each have a fixed rate $r$ for a window of length $h$, and their counts $n_j$ are Poisson with mean and variance $rh$. The average count $\bar n=N^{-1}\sum_jn_j$ has mean $rh$ and variance $rh/N$. As $N$ grows, the suitably centered and scaled average approaches a Gaussian distribution by the central limit theorem. No individual count has to be Gaussian. In a recurrent network, rates and inputs interact; applying a Gaussian approximation to their aggregate requires the paper's additional weak-input assumptions. A single cell's count over an interval made arbitrarily short remains a jump count.

</div>
</details>

## Fisher information measures how clearly spikes distinguish nearby values {#sec:MATH-TOOLS-FISHER}

Suppose a circuit currently represents an angle near $30^\circ$. A receiving cell sees spikes rather than an angle label. If $30^\circ$ and $31^\circ$ produce almost identical probabilities of spike patterns, a short observation gives little evidence about which value is represented. If their spike probabilities differ strongly, the distinction is easier.

[[**Fisher information**]{.definition-term custom-style="Definition Term"}, abbreviated FI, measures how sensitively the probabilities of observations change with a small change in the value being estimated.]{.definition-explanation} It describes local precision: the distinction between nearby values. A large FI at one angle does not resolve ambiguity between distant angles that happen to produce the same activity pattern. It is not a count of stored bits or of different memories.

[A [**tuning curve**]{.definition-term custom-style="Definition Term"} $\bar r_i(\theta)$ gives neuron $i$'s expected firing rate at represented value $\theta$.]{.definition-explanation} The bar here denotes the model's steady rate in the absence of noise. Its slope $\bar r_i'=d\bar r_i/d\theta$ measures sensitivity to a small value change. To turn sensitivity into a measure of precision, we must also specify how the spikes fluctuate.

For this calculation, hold $\theta$ approximately fixed during a brief observation of length $h$ seconds. Assume positive rates and independent [Poisson spike counts](../chapters/ch-foundations.html#sec-foundations-poisson) conditional on that value. Under this spike model, count mean and variance are both $h\bar r_i$. A small angle change $\delta\theta$ changes the expected count by approximately $h\bar r_i'\delta\theta$. [The [**count sensitivity**]{.definition-term custom-style="Definition Term"} $h\bar r_i'$ is the change in expected spike count per unit change in $\theta$.]{.definition-explanation} The rate sensitivity $\bar r_i'$ is the change in expected firing rate per unit change in $\theta$. Let $I_{h,i}(\theta)$ be the information supplied by cell $i$ in that observation. Comparing the squared count sensitivity with the count variance gives

$$
I_{h,i}(\theta)=\frac{(h\bar r_i')^2}{h\bar r_i}
=h\frac{(\bar r_i')^2}{\bar r_i}.
$$

For this Poisson model the ratio is exactly the single-cell Fisher information. Let $I_h(\theta)$ be the total information in the spike counts from all cells, and $J(\theta)$ be that information per unit observation time. Independent contributions add:

$$
I_h(\theta)=hJ(\theta),\qquad
J(\theta)=\sum_i\frac{(\bar r_i')^2}{\bar r_i}.
$$

[The [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"} $J$ is the information per unit observation time in these spikes about the circuit's current represented value.]{.definition-explanation} “Internal” means that the value is maintained by the circuit; a present external stimulus is not needed. If $\theta$ is measured in degrees, $I_h$ has units $\mathrm{degree}^{-2}$ and $J$ has units $\mathrm{degree}^{-2}\mathrm{s}^{-1}$. The paper uses this rate in Eq. 3.[^tools-fi]

The numerator measures how strongly expected firing changes with the value. The denominator reflects Poisson spike variability: sensitivity must be judged relative to count noise. Increasing every rate also changes the slopes, so the denominator alone does not imply that higher firing always lowers information.

<details class="publisher-long-content publisher-long-example">
<summary>Example: equal firing rates can provide different angle precision</summary>
<div class="publisher-fold-body">

Take two illustrative cells, each firing at 20 spikes per second at the current angle. Their local slopes are 2 and 10 spikes per second per degree. In a 0.1-second observation, each has mean count 2 and count variance 2. Their expected count changes per degree are 0.2 and 1. Their information contributions are

$$
I_{h,1}=\frac{0.2^2}{2}=0.02\,\mathrm{degree}^{-2},
\qquad I_{h,2}=\frac{1^2}{2}=0.5\,\mathrm{degree}^{-2}.
$$

The steeper response gives 25 times the local information despite the equal rates and count noise. If these two cells' counts are independent at the given angle, their joint information is $0.52\,\mathrm{degree}^{-2}$. These are chosen local response curves, not measured cells or a constructed recurrent network.

</div>
</details>

The derivation in Chapter 5 connects this count calculation to the [likelihood and formal definition of FI](../chapters/ch-memory-information.html#sec-memory-fi). Shared spike fluctuations require a joint probability model; they cannot generally be handled by adding these single-cell terms.

## Information limits how slowly a neural memory can spread {#sec:MATH-TOOLS-BOUND}

The same uncertain spikes that tell a receiving cell about the value also renew activity inside the memory circuit. Synaptic effects fade, so the network must carry the value forward through those new events. This links the precision of the signals to the persistence of the memory.

One statistical benchmark concerns reading a value that is effectively fixed during observation. Let $\hat\theta$ be an estimate computed from the spikes. [An estimate is [**locally unbiased**]{.definition-term custom-style="Definition Term"} when its mean agrees with the true value to first order near the value under study.]{.definition-explanation} For smooth probability models satisfying the differentiation conditions explained in Chapter 5, [the [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"} gives a lower limit on the variance of such an estimate:]{.definition-explanation}

$$
\operatorname{Var}(\hat\theta)\geq\frac{1}{I_h(\theta)}
=\frac{1}{hJ(\theta)}.
$$

The bound does not promise that every finite sample admits an estimate achieving it. Chapter 5 gives its [derivation and conditions](../chapters/ch-memory-information.html#sec-memory-fi).

A second quantity describes what happens while the circuit stores the value. With zero mean drift and approximately constant coefficients, the displacement variance grows as $\operatorname{Var}[\theta(t)-\theta(0)]\simeq2Dt$. Here $t$ is storage time and $D$ is the diffusion coefficient: half the variance growth per unit time. The paper's weights are tuned so that, without noise, a continuous range of represented values can persist as stationary activity patterns. Other activity disturbances relax toward those patterns. Burak and Fiete (2012) prove, for these networks in the weak-fluctuation approximation with a common synaptic time constant $\tau$ and conditionally independent Poisson spike generation,

$$
\boxed{D(\theta)\geq\frac{1}{2\tau^2J(\theta)}.}
$$

[Low information in the spikes forces a high minimum rate of memory spreading. Larger information lowers that minimum; the network's connections and dynamics determine whether it reaches the limit.]{.key-statement} The factor $\tau^2$ makes the units consistent: if $J$ is inverse angle squared per second, the bound has angle squared per second, as $D$ must.[^tools-bound]

The physical interpretation is that maintaining activity acts like repeatedly estimating the circuit's own state from its spikes. This motivates the bound. It does not replace the dynamical proof: the state can move while spikes are collected, and the circuit's feedback is itself noisy. Chapter 5 [derives the bound from the network equations](../chapters/ch-memory-information.html#sec-memory-bound) and states its equality conditions.

When a circuit represents several values, a single number cannot describe every possible change in them. The information-rate matrix $J$ describes how well the spikes distinguish small changes in each direction in that space. For a change $\delta\boldsymbol\theta$, the quadratic form $\delta\boldsymbol\theta^TJ\delta\boldsymbol\theta$ measures its local distinguishability per unit observation time. For a brief window of length $h$ in which the state is effectively fixed, multiplying by $h$ gives a dimensionless measure. A direction that produces no change in the expected rates has zero information in this Poisson model. Individual diagonal entries can be positive even when a combination of values is invisible.

<details class="publisher-long-content publisher-long-example">
<summary>Example: two values can be visible separately but ambiguous together</summary>
<div class="publisher-fold-body">

Suppose both coordinates are measured in degrees and all modeled firing rates depend on them only through their sum. At a given state, take their information-rate matrix to be

$$
J=j\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad j>0,
\quad [j]=\mathrm{degree}^{-2}\mathrm{s}^{-1}.
$$

Changing either coordinate alone changes that sum. Increasing one by an amount and decreasing the other by the same amount leaves it unchanged. Indeed $J(1,-1)^T=0$: this direction is invisible to those rates, and $J$ has no ordinary inverse. The multi-coordinate bound in Chapter 5 uses $J^{-1}$ only when the relevant directions are distinguishable. Its matrix inequality means that the corresponding scalar inequality holds for every linear combination of coordinates. For any matrix $Q$ and vector $\mathbf z$, $\mathbf z^TQ^TQ\mathbf z=\lVert Q\mathbf z\rVert^2\ge0$; this is the nonnegative quantity used in that proof.

</div>
</details>

Finally, $J$ measures information about the current value $\theta(t)$, while diffusion describes its departure from the initial value $\theta(0)$. [The current angle can be easy to read even after it has wandered far from the angle originally supplied by the cue.]{.key-statement} The eye paper asks how such internal fluctuations could appear in recordings and physical movement. That requires a model of shared signals and of the muscles that filter them.

## Covariance tests which fluctuations are shared {#sec:MATH-TOOLS-SHARED}

If one neuron's spikes predict some eye movement, is the neuron passing on a common command or adding its own noise? Both can make its activity vary. Comparing the prediction with measured movement helps separate the part they share from fluctuations present in only one signal.

[The [**covariance**]{.definition-term custom-style="Definition Term"} of $X$ and $Y$ measures how their deviations from their own means vary together.]{.definition-explanation} Positive covariance means that deviations tend to have the same sign. [The [**correlation coefficient**]{.definition-term custom-style="Definition Term"} $\rho$ scales that covariance by both signals' standard deviations.]{.definition-explanation} Private noise in either signal can reduce this scaled measure even if the common source has not changed.

<details class="publisher-long-content publisher-long-note">
<summary>Mathematical definitions: covariance and correlation</summary>
<div class="publisher-fold-body">

$$
\operatorname{Cov}(X,Y)=\mathbb E[(X-\mathbb EX)(Y-\mathbb EY)],\qquad
\rho=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.
$$

Here $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$. Covariance has the product of the signals' units. Correlation is dimensionless and lies between $-1$ and $1$ when both variances are finite and positive.

</div>
</details>

Consider a teaching model, with all signals measured in degrees:

$$
X=aS+\eta_x,\qquad Y=bS+\eta_y.
$$

Here $S$ is a shared displacement command, $X$ a cell's displacement prediction, and $Y$ measured displacement. [The dimensionless [**gain**]{.definition-term custom-style="Definition Term"}s $a,b$ multiply the common command to give its contribution to each signal.]{.definition-explanation} This $b$ is a gain, not the bias $b_i$ in the memory model. The private contributions $\eta_x,\eta_y$ vary independently of one another and of $S$. Let $\chi_Y$ be the fraction of the variance of measured displacement $Y$ contributed by the shared command $bS$. Thus only the shared command survives in the covariance:

$$
\operatorname{Cov}(X,Y)=ab\operatorname{Var}(S),\qquad
\chi_Y=\frac{b^2\operatorname{Var}(S)}{\operatorname{Var}(Y)}
=\frac ba\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(Y)}.
$$

The last equality requires $a\ne0$. [Correlation alone does not give a shared variance fraction. That interpretation requires a model of the shared and private contributions and a calibrated gain.]{.key-statement} The gain ratio $b/a$ converts the covariance to the shared contribution to $Y$'s variance. The eye study obtains an eye-position prediction from each cell's spikes by inverting a movement-to-firing fit calibrated on larger movements. Its variance estimate assumes this calibration also applies during drift and gives the shared component the same displacement scale in prediction and measurement. A calibration error can change the inferred fraction. Private noise in $X$ lowers correlation by increasing $\sigma_X$, the standard deviation of $X$, even when the shared command dominates $Y$.

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

The 2022 analysis uses this logic for 350 ms displacements, assuming that calibration from larger movements still holds during drift. It also neglects a small covariance between the two private contributions, of order $1/N_m$, where $N_m$ is the number of motor neurons in its population model. These are assumptions to check, not consequences of the covariance definition.[^tools-eye-shared] Many independent private contributions can average down in actual movement while remaining large in a single cell's prediction. Shared fluctuations survive that averaging; the paper's separate population bound tests whether independent motor noise alone could explain the observations.[^tools-eye-independent]

## Filtering changes how noise appears in eye motion {#sec:MATH-TOOLS-FILTERS}

Muscles take time to respond to neural commands. Could their response turn rapidly changing noise into the smooth, continuing motion seen during fixation? The answer depends on whether the input merely fluctuates or accumulates changes.

[A [**causal filter**]{.definition-term custom-style="Definition Term"} determines present output from present and past input.]{.definition-explanation} For a linear response that does not change with time, [its [**impulse response**]{.definition-term custom-style="Definition Term"} $h(u)$ gives the surviving response after a unit impulse $u$ seconds ago.]{.definition-explanation} Here $h$ is a function of time, not the observation duration $h$ used in the spike-count calculation. [The [**convolution**]{.definition-term custom-style="Definition Term"} adds these responses over the input history:]{.definition-explanation}

$$
E(t)=\int_0^\infty h(u)U(t-u)\,du.
$$

For a simple response, $h(u)=e^{-u/\tau}/\tau$ for $u\ge0$. Input $U$ and output $E$ are angles in degrees; $h$ has units s$^{-1}$ and response time $\tau$ is in seconds. This $\tau$ describes the eye's response. It is a different physical quantity from the synaptic decay time also denoted by $\tau$ in the memory model, and their values need not be equal. Equivalently, $\tau\dot E=U-E$: the command's mismatch with current position drives velocity. [This is a [**low pass filter**]{.definition-term custom-style="Definition Term"}: it suppresses rapid changes relative to slow changes.]{.definition-explanation}

[[**White noise**]{.definition-term custom-style="Definition Term"} idealizes fluctuations uncorrelated at distinct times; in continuous time its intensity specifies variability of integrated input, rather than an ordinary finite pointwise variance.]{.definition-explanation} Passing it through this decaying filter produces a stationary position after initial transients: mean and variance stay constant and covariance depends only on time separation. Its mean squared displacement $M(\ell)=\mathbb E[(E(t+\ell)-E(t))^2]$ approaches a plateau. The lag $\ell$ is the separation between readings, not the clock time $t$.[^tools-eye-white]

A diffusing position command instead accumulates independent changes with displacement variance $2D\ell$, where $D$ has units deg$^2$/s. Filtering smooths its motion without stopping that accumulation. In the simple model below, short lag MSD grows as $\ell^2$ and long lag MSD grows linearly. Position is not stationary; its increments have statistics independent of $t$ once the initial velocity transient has decayed.

<details class="publisher-long-content publisher-long-example">
<summary>Example: the same filter separates fluctuating and accumulating input</summary>
<div class="publisher-fold-body">

For centered white input with $\mathbb E[U(t)U(t')]=A\delta(t-t')$, intensity $A$ has units deg$^2$ s. [The [**Dirac delta**]{.definition-term custom-style="Definition Term"} $\delta$ is an instantaneous unit-area impulse; here it expresses the covariance concentrated at equal times.]{.definition-explanation} Write $C_E(\ell)=\mathbb E[E(t)E(t+\ell)]$ for the covariance of the centered output at lag $\ell$. Overlap of the two impulse responses gives

$$
C_E(\ell)=A\int_0^\infty h(u)h(u+\ell)\,du
=\frac{A}{2\tau}e^{-\ell/\tau},\qquad
M_{\rm white}(\ell)=2[C_E(0)-C_E(\ell)].
$$

Thus $M_{\rm white}=(A/\tau)(1-e^{-\ell/\tau})$, approaching $A/\tau$. For a Brownian position input with diffusivity $D$, the same filter gives stationary velocity covariance $C_v(s)=(D/\tau)e^{-|s|/\tau}$ after the initial velocity transient. Velocities at two times share some of the same past Brownian increments; their exponentially weighted overlap gives this covariance. The [eye-timing derivation](../chapters/ch-eye-timing.html#sec-eye-filtered-msd) calculates the overlap. Integrating velocity over the displacement interval gives

$$
M_{\rm diffusion}(\ell)=2\int_0^\ell(\ell-s)C_v(s)\,ds
=2D[\ell-\tau(1-e^{-\ell/\tau})].
$$

Expansion at $\ell\ll\tau$ gives $(D/\tau)\ell^2$: velocity barely changes across that interval. For $\ell\gg\tau$, it approaches $2D(\ell-\tau)$, with continuing growth. White input instead has linear short lag MSD in this single exponential example. The input and filter together determine short lag behavior.

</div>
</details>

These calculations use one response time as a teaching simplification. The 2022 model includes two muscle response times and visual feedback. Its conclusions concern the measured lag range; smooth movement alone does not identify diffusion, and short lag behavior also depends on measurement error. The [eye-drift](../chapters/ch-eye-drift.html) and [timing](../chapters/ch-eye-timing.html) chapters retain the full analysis.[^tools-eye-model]

## Random fields describe a fixed spatial map {#sec:MATH-TOOLS-RANDOM-FIELDS}

Why does a cell stay active over a stretch of track, rather than change its response independently at every position? Mainali, Azeredo da Silveira, and Burak (2025) describe the cell's combined input as a spatial map $h(x)$. This is a new use of $h$, distinct from the eye filter's impulse response. Nearby values depend on one another. A distribution of such maps can predict field sizes without predicting where a particular cell's fields will occur.[^tools-place-map]

[A [**random field**]{.definition-term custom-style="Definition Term"} assigns random values to positions; a Gaussian random field requires the values at every finite set of positions to form a jointly Gaussian vector.]{.definition-explanation} It is also called a [**Gaussian process**]{.definition-term custom-style="Definition Term"}, including when positions have more than one coordinate. [A [**jointly Gaussian vector**]{.definition-term custom-style="Definition Term"} has Gaussian distributions for all its linear combinations.]{.definition-explanation} Gaussian distributions at individual positions alone do not impose this joint rule.

For jointly Gaussian variables, zero covariance implies independence. This special rule will let us separate a map's height and slope in the crossing calculation. Zero covariance does not generally imply independence.

<details class="publisher-long-content publisher-long-example">
<summary>Example: zero covariance needs a joint Gaussian assumption</summary>
<div class="publisher-fold-body">

Let $X$ and $Z$ be independent standard Gaussian variables and set $Y=\rho X+\sqrt{1-\rho^2}\,Z$, with $-1<\rho<1$. The pair is jointly Gaussian and has covariance $\rho$. At $\rho=0$, $Y=Z$ is independent of $X$.

For a contrast, let $Y=X^2-1$. Its covariance with $X$ is $\mathbb E[X^3-X]=0$, yet knowing $X$ determines $Y$. This pair is not jointly Gaussian. The Gaussian rule cannot be applied merely because two quantities have zero covariance.

</div>
</details>

[Once a map is drawn, it stays fixed while the animal traverses it. Revisiting a position evaluates the same map value, rather than drawing a fresh input.]{.key-statement} The randomness describes possible maps, not changes with time during a visit.

[The [**spatial covariance**]{.definition-term custom-style="Definition Term"} $C(x,y)$ measures how deviations of input from its mean at two positions vary together across possible maps.]{.definition-explanation} Mean and covariance determine the Gaussian law. [For a field, [**stationarity**]{.definition-term custom-style="Definition Term"} means that shifting all positions leaves its probability law unchanged.]{.definition-explanation} The mean is then a constant $\mu$ and covariance depends on separation: $C(x,y)=C(y-x)$. This does not make an individual map flat. [For a field, [**isotropy**]{.definition-term custom-style="Definition Term"} means there is no preferred direction in its statistics.]{.definition-explanation} Stationarity alone does not require isotropy.

Normalize the input using its standard deviation $\sigma_0$, and express the firing threshold $h_{\mathrm{th}}$ in the same units:

$$
z(x)=\frac{h(x)-\mu}{\sigma_0},\qquad
q=\frac{h_{\mathrm{th}}-\mu}{\sigma_0},\qquad
F(x)=a[z(x)-q]_+.
$$

Here $[u]_+=\max(u,0)$ and $a>0$ converts dimensionless input excess into firing rate. [The [**excursion set**]{.definition-term custom-style="Definition Term"} $A_q=\{x:z(x)>q\}$ is the active part of the map.]{.definition-explanation} Each connected piece is one field. Two peaks can belong to the same field if an active path connects them.

Field widths also depend on how quickly the input changes over distance. [The paper's [**correlation length**]{.definition-term custom-style="Definition Term"} compares typical input height with typical spatial slope.]{.definition-explanation} For a differentiable stationary map along a line, write $z'=dz/dx$ for the spatial rate of change of the normalized input; $C(0)$ is the input variance and $C''(0)$ is the second derivative of spatial covariance with respect to separation, evaluated at zero. Then

$$
\ell_c=\sqrt{-\frac{C(0)}{C''(0)}},\qquad
\operatorname{Var}(z')=\ell_c^{-2}.
$$

It has distance units. For $C(r)=\sigma_0^2e^{-r^2/(2\ell_c^2)}$, increasing $\ell_c$ stretches the map. More generally it describes local covariance curvature, without fixing distant spatial relationships. In an isotropic map the same scale applies along every direction.[^tools-place-scale]

Gaussian values do not guarantee smooth maps. Crossing calculations need differentiable sample maps and a nonsingular covariance matrix for height and slope: those variables must not obey an exact linear constraint. Peak calculations additionally need second derivatives and enough regularity for a local quadratic approximation. For example, the corner at zero in $C(r)\propto e^{-|r|/b}$ prevents its use for the differentiable crossing calculation below.

## Crossings and peak geometry predict field counts and sizes {#sec:MATH-TOOLS-CROSSINGS-PEAKS}

On a track, a field begins where the input crosses upward through threshold. [An [**upcrossing**]{.definition-term custom-style="Definition Term"} is a crossing of $z=q$ with positive spatial slope.]{.definition-explanation} At a randomly selected position, conditioning on $z=q$ asks about slopes at that height. For a continuous height, an exact value has probability zero. Where the height density is positive and regular, the conditional mean can be understood as the limit of means for a narrowing band around $q$; equivalently it is calculated from the conditional density. It is not a ratio of probabilities of two zero-probability events.

To count crossings, imagine a narrow band of height $2\varepsilon$ around the threshold. A curve crossing upward with slope $v$ spends approximately $2\varepsilon/v$ of track length in that band. A steeper crossing therefore contributes less occupied length, so multiplying by its slope corrects for that shorter stay. Averaging gives the mean number of upcrossings per unit distance: the input's probability density at the threshold times its mean positive slope conditional on being there. Write $\nu_+(q)$ for that number per unit distance, $p_z(q)$ for the normalized input's density at threshold $q$, and $z'=dz/dx$ for its slope along the track; $(z')_+=\max(z',0)$ keeps only positive slopes. The scale $\ell_c$ is the correlation length defined above.

$$
\nu_+(q)=p_z(q)\,\mathbb E[(z')_+\mid z=q]
=\frac{e^{-q^2/2}}{2\pi\ell_c}.
$$

[The [**Kac–Rice formula**]{.definition-term custom-style="Definition Term"} counts crossings by combining the input density at threshold with conditional slope.]{.definition-explanation} The displayed result applies to the smooth stationary Gaussian model. [The result is exact under these assumptions at any threshold.]{.key-statement}[^tools-place-crossing]

<details class="publisher-long-content publisher-long-note">
<summary>Derivation: height and slope give the crossing density</summary>
<div class="publisher-fold-body">

In a narrow height band of width $2\varepsilon$ around $q$, an upward crossing with slope $v$ occupies distance approximately $2\varepsilon/v$. Weighting that distance by $v/(2\varepsilon)$ counts one crossing. Averaging gives $\nu_+=\int_0^\infty v\,p_{z,z'}(q,v)\,dv$.

Stationarity gives $\operatorname{Cov}(z,z')=0$. Joint Gaussianity makes height and slope independent, with $z\sim N(0,1)$ and $z'\sim N(0,\ell_c^{-2})$. Thus $p_z(q)=e^{-q^2/2}/\sqrt{2\pi}$ and $\mathbb E[(z')_+]=1/(\ell_c\sqrt{2\pi})$, giving the displayed result.

</div>
</details>

On a finite track of length $L$, a field can already be active at the left endpoint. Counting all active components that intersect the track gives $\mathbb E[N_L]=L\nu_+(q)+\Pr[z(0)>q]$. Discarding clipped boundary fields changes this convention. The later place field chapter follows this correction explicitly.

Counts do not determine the size distribution. At high positive $q$, fields counted once each typically surround isolated high peaks. This sampling gives each field equal weight, rather than selecting fields by the amount of space they occupy. A smooth isotropic Gaussian field becomes approximately a downward quadratic near such a peak. If its height exceeds threshold by $\epsilon$, the active radius grows as $\sqrt{\epsilon}$ at fixed $q$ and $\ell_c$. Length, area and volume therefore grow as $\epsilon^{d/2}$ in spatial dimension $d$.[^tools-place-peaks]

[The [**Hessian**]{.definition-term custom-style="Definition Term"} $H$ is the matrix of second spatial derivatives of the input map.]{.definition-explanation} At a point with zero gradient, a small spatial displacement $\mathbf x$ changes the normalized input by approximately $\tfrac12\mathbf x^TH\mathbf x$. Its eigenvectors give principal spatial directions, and the eigenvalues give curvature in those directions. Negative curvature in every direction describes a nondegenerate local peak; mixed signs describe a saddle. A zero eigenvalue needs further analysis.

<details class="publisher-long-content publisher-long-example">
<summary>Example: curvature distinguishes a peak from a saddle</summary>
<div class="publisher-fold-body">

For dimensionless input $z$ and coordinates $x,y$ in metres, suppose near a critical point

$$
z(x,y)\simeq z(0,0)-(1\,\mathrm{m}^{-2})x^2-(4\,\mathrm{m}^{-2})y^2,
\qquad H=\begin{pmatrix}-2&0\\0&-8\end{pmatrix}\,\mathrm{m}^{-2}.
$$

Moving along either axis lowers the input, faster along $y$, so the point is a peak. Reversing the sign of the $y^2$ term changes the second eigenvalue to $+8\,\mathrm{m}^{-2}$: input rises along $y$ but falls along $x$, giving a saddle. In two dimensions, $\det(-H)$ is positive for the peak and negative for this saddle. The [place-size chapter](../chapters/ch-place-sizes.html#sec-place-rare-peaks) applies the quadratic approximation to a random map; the [topology chapter](../chapters/ch-place-tests.html#sec-place-topology) uses the signs to count changes in connected regions and holes.

</div>
</details>

The Gaussian model also supplies the statistics of the peak excess. For fields selected this way in the high threshold limit, $U=q\epsilon$ approaches an exponential distribution of mean one: the chance that $U>u$ approaches $e^{-u}$ for $u\ge0$. Combining that excess law with the geometry gives the size distribution.[^tools-place-peaks]

The geometric conversion changes the density as well as the units. [A [**change of variables**]{.definition-term custom-style="Definition Term"} preserves the probability of each event while expressing it in a new variable.]{.definition-explanation} Let $X$ be a random quantity and $x$ a possible value. If $U=g(X)$ for a smooth, strictly increasing function $g$, a small interval $dx$ around $x$ corresponds to $du=g'(x)dx$. Hence $p_X(x)=p_U(g(x))g'(x)$: the derivative accounts for how the transformation stretches or compresses intervals. The density itself is not a probability at one exact value. For a decreasing transformation use the absolute derivative; a nonmonotonic transformation may have several branches.

<details class="publisher-long-content publisher-long-example">
<summary>Example: an exponential variable gives a Rayleigh-shaped density</summary>
<div class="publisher-fold-body">

Let $U$ have density $e^{-u}$ for $u\ge0$ and define the dimensionless size $X=\sqrt U$. The event $X\le x$ is the same event as $U\le x^2$, for $x\ge0$. Therefore

$$
\Pr(X\le x)=1-e^{-x^2},\qquad
p_X(x)=\frac{d}{dx}\Pr(X\le x)=2x e^{-x^2}.
$$

The factor $2x$ also follows from $u=x^2$ and $du/dx=2x$. Both expressions assign the same probability to corresponding intervals. The place-field calculation uses the same step with $U=\beta s^{2/d}$; its random field size $s$ has physical size units and $\beta$ supplies the required units.

</div>
</details>

The result is three different limiting size laws. [The 1D length law is a [**Rayleigh distribution**]{.definition-term custom-style="Definition Term"}: the chance of a length exceeding $S$ is $\exp(-\beta S^2)$ for a positive scale constant $\beta$.]{.definition-explanation} The corresponding chance is $\exp(-\beta S)$ for area in 2D, an exponential distribution, and $\exp(-\beta S^{2/3})$ for volume in 3D. Because size $S$ has units distance$^d$, $\beta$ has units inverse distance squared in every dimension; its geometric factor changes with dimension. Thus the same spatial mechanism can give different length, area and volume histograms.

<details class="publisher-long-content publisher-long-example">
<summary>Example: the same peak excess gives different size laws</summary>
<div class="publisher-fold-body">

For a stationary isotropic Gaussian field, conditioning on height $b$ gives mean second derivative $-b/\ell_c^2$ along each unit direction, with fluctuations that do not grow with $b$. Thus typical high peaks concentrate around a quadratic shape. Here $x$ is displacement from the peak, taken as the origin; $\epsilon$ is the peak height above threshold $q$; $\ell_c$ is the correlation length; and $r_*$ is the approximate radius where input falls back to threshold:

$$
z(x)-q\simeq\epsilon-\frac{q\|x\|^2}{2\ell_c^2},\qquad
r_*\simeq\ell_c\sqrt{2\epsilon/q}.
$$

For typical high fields the scaled excess $U=q\epsilon$ approaches an exponential distribution of mean one. Writing size as $s=v_dr_*^d$, with $v_1=2$, $v_2=\pi$, $v_3=4\pi/3$, converts the size event $s>S$ into $U>\beta S^{2/d}$. Therefore

$$
\Pr(s>S)\simeq\exp[-\beta S^{2/d}],\qquad
\beta=\frac{q^2}{2\ell_c^2v_d^{2/d}}.
$$

Geometry changes the distribution even though the scaled peak excess has the same limiting law.

</div>
</details>

[These size laws are high threshold limits, not exact laws at finite $q$.]{.key-statement} At lower thresholds fields can have several peaks or irregular shapes. The detailed chapter checks the approximation against finite threshold calculations.

## Major results connect formulas to physical questions {#sec:MATH-TOOLS-RESULTS}

<span id="tbl-math-results"></span>

The [Results and connections](ch-exam-review.html) organizes all 35 results by the question each paper answers. Begin with its three reasoning chains, then read the core results or open supporting calculations. A common notation key gives shared quantities and their aliases across the papers; paper keys add model-specific meanings, and result rows list further symbols or exceptions. Every result retains its paper equation/page locations and book chapter/section links.

This chapter introduces the mathematical tools. Use the separate review page when you want to reconstruct the complete argument or find a particular result quickly.

[^tools-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [Eqs. 7–9, PDF p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5) and [mutual-inhibition model, PDF p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6). [DOI](https://doi.org/10.1073/pnas.1117386109). The deterministic two-unit calculation is an explicit teaching reconstruction of the stated model.

[^tools-fi]: Burak and Fiete (2012), [internal Fisher information, Eq. 3 and Fig. 1B, PDF p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2), and [Supporting Text, Section IV, PDF pp. 9–10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9). The finite-interval count comparison and numerical example here explain the independent Poisson model.

[^tools-bound]: Burak and Fiete (2012), [information–diffusion inequality, Eq. 4, PDF p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3), and [Supporting Text, Section V, PDF pp. 10–12](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10). The bound is a result for the stated model assumptions, rather than a bound for all neural or electronic memories.

[^tools-eye-shared]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [DOI](https://doi.org/10.1038/s41467-022-29201-y). [calibration, Eqs. 4–7, PDF p. 9](../papers/ben-shushan-2022-fixational-drift.pdf#page=9), and [shared variance model, Eqs. 11–15, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10). The model with explicit gains and the numerical example are teaching constructions.

[^tools-eye-independent]: Ben-Shushan et al. (2022), [Supplementary Notes, independent contribution bound, Eqs. S1–S2, PDF p. 2](../papers/ben-shushan-2022-supplement-1.pdf#page=2).

[^tools-eye-white]: Ben-Shushan et al. (2022), [filtered white noise, Eqs. 20–22, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10). The normalized single exponential filter and filtered Brownian calculation are teaching reconstructions.

[^tools-eye-model]: Ben-Shushan et al. (2022), [muscle response, Eqs. 2–7, PDF p. 9](../papers/ben-shushan-2022-fixational-drift.pdf#page=9), [measurement error, Eqs. 18–19, PDF p. 10](../papers/ben-shushan-2022-fixational-drift.pdf#page=10), and [Supplementary Notes, visual feedback, PDF pp. 4–5](../papers/ben-shushan-2022-supplement-1.pdf#page=4).

[^tools-place-map]: Mainali, N., Azeredo da Silveira, R., & Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [DOI](https://doi.org/10.1016/j.neuron.2025.01.017). [model and Gaussian process definition, PDF p. 3](../papers/mainali-2025-universal-statistics.pdf#page=3); [STAR Methods, Eqs. 2–3, PDF p. 13](../papers/mainali-2025-universal-statistics.pdf#page=13). The normalization here includes a constant mean, which can equivalently be absorbed into the threshold.

[^tools-place-scale]: Mainali et al. (2025), [STAR Methods, Eq. 4 and simulation covariance, PDF p. 14](../papers/mainali-2025-universal-statistics.pdf#page=14). The notation $\sigma_0$ denotes input standard deviation; $\ell_c$ denotes the paper's spatial scale $\sigma$.

[^tools-place-crossing]: Mainali et al. (2025), [Methods S3, Eqs. S9–S13, supplement PDF pp. 11–12](../papers/mainali-2025-supplement.pdf#page=11). The slope weighting and finite track endpoint correction are teaching explanations; the endpoint term also appears in [STAR Methods Eq. 8, main PDF p. 15](../papers/mainali-2025-universal-statistics.pdf#page=15).

[^tools-place-peaks]: Mainali et al. (2025), [size law, Eq. 1, main PDF p. 3](../papers/mainali-2025-universal-statistics.pdf#page=3); [Methods S4, Eqs. S22–S25, supplement PDF pp. 14–15](../papers/mainali-2025-supplement.pdf#page=14). The quadratic and change of variables here are a teaching reconstruction. Solving S22 retains the factor $\sqrt2$ missing from printed S23; the finite excess exponent used before the limit is $-q\epsilon-\epsilon^2/2$. The detailed size chapter records these printed algebra issues.
