# Mathematical tools connect neural interactions to memory accuracy {#ch:MATHEMATICAL-TOOLS}

A neural circuit can keep firing after a cue disappears and still lose the value that cue supplied. To understand this possibility, we need two connections between mathematics and the physical system: how cells influence one another, and how clearly their variable signals distinguish nearby remembered values. [Connection weights describe the feedback that sustains activity. Fisher information measures the precision available in the spikes that renew it.]{.key-statement}

This chapter establishes those meanings before Part I uses the equations. It assumes calculus, linear algebra and basic probability, including expected value, variance, standard deviation and probability density. The main text explains the mechanisms and results; the folded calculations give the supporting steps. The detailed neural dynamics and general proofs remain in Chapters 1–6.

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

Consider two mutually inhibiting populations. If population 1 becomes more active, it inhibits population 2 more strongly. Population 2 then fires less and inhibits population 1 less strongly. With the paper's particular balance of weights, decay and rate response, a difference between their activities can persist. That difference stores the value. Arbitrary mutual inhibition does not guarantee this balance.

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

An equal increase in both activations raises $S$ above $b$, and the circuit drives it back down. A difference between the activations persists. For $b=20$, the states $(s_1,s_2)=(12,8)$ and $(8,12)$ both have the required total but store different values, $4$ and $-4$. This is a deterministic calculation with the paper's tuned parameters, not a claim that random spikes disappear or that every inhibitory pair stores a continuous value. Both steady rates are positive only for $|\theta_s|<b$.

</div>
</details>

If $W=0$ in this model, rates become the constants $\phi(b_i)$. Any difference due to the initial synaptic activations then decays toward the bias-determined state. Connections allow the present activity to influence what happens next; their arrangement determines whether the circuit preserves a useful pattern. [The weights stay fixed during storage. The remembered value is carried by changing neural activity, rather than by changing the weights.]{.key-statement} Chapter 1 gives the [full spike and activation equations](../chapters/ch-foundations.html#sec-memory-spikes); Chapter 3 calculates which disturbances those interactions remove and which leave a lasting memory change.

## Fisher information measures how clearly spikes distinguish nearby values {#sec:MATH-TOOLS-FISHER}

Suppose a circuit currently represents an angle near $30^\circ$. A receiving cell sees spikes rather than an angle label. If $30^\circ$ and $31^\circ$ produce almost identical probabilities of spike patterns, a short observation gives little evidence about which value is represented. If their spike probabilities differ strongly, the distinction is easier.

[[**Fisher information**]{.definition-term custom-style="Definition Term"}, abbreviated FI, measures how sensitively the probabilities of observations change with a small change in the value being estimated.]{.definition-explanation} It describes local precision: the distinction between nearby values. A large FI at one angle does not resolve ambiguity between distant angles that happen to produce the same activity pattern. It is not a count of stored bits or of different memories.

[A [**tuning curve**]{.definition-term custom-style="Definition Term"} $\bar r_i(\theta)$ gives neuron $i$'s expected firing rate at represented value $\theta$.]{.definition-explanation} The bar here denotes the model's steady rate in the absence of noise. Its slope $\bar r_i'=d\bar r_i/d\theta$ measures sensitivity to a small value change. To turn sensitivity into a measure of precision, we must also specify how the spikes fluctuate.

For this calculation, hold $\theta$ approximately fixed during a brief observation of length $h$ seconds. Assume positive rates and independent [Poisson spike counts](../chapters/ch-foundations.html#sec-foundations-poisson) conditional on that value. Under this spike model, count mean and variance are both $h\bar r_i$. A small angle change $\delta\theta$ changes the expected count by approximately $h\bar r_i'\delta\theta$. Comparing the squared change per unit angle with count variance gives

$$
I_{h,i}(\theta)=\frac{(h\bar r_i')^2}{h\bar r_i}
=h\frac{(\bar r_i')^2}{\bar r_i}.
$$

For this Poisson model the ratio is exactly the single-cell Fisher information. Independent contributions add:

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

Finally, $J$ measures information about the current value $\theta(t)$, while diffusion describes its departure from the initial value $\theta(0)$. [The current angle can be easy to read even after it has wandered far from the angle originally supplied by the cue.]{.key-statement} Part I now follows these two quantities from the neural signals through the model, its simulations and its limits on memory accuracy.

[^tools-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [Eqs. 7–9, PDF p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5) and [mutual-inhibition model, PDF p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6). [DOI](https://doi.org/10.1073/pnas.1117386109). The deterministic two-unit calculation is an explicit teaching reconstruction of the stated model.

[^tools-fi]: Burak and Fiete (2012), [internal Fisher information, Eq. 3 and Fig. 1B, PDF p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2), and [Supporting Text, Section IV, PDF pp. 9–10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9). The finite-interval count comparison and numerical example here explain the independent Poisson model.

[^tools-bound]: Burak and Fiete (2012), [information–diffusion inequality, Eq. 4, PDF p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3), and [Supporting Text, Section V, PDF pp. 10–12](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10). The bound is a result for the stated model assumptions, rather than a bound for all neural or electronic memories.
