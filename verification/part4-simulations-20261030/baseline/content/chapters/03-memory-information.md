<!-- vale ai-tells.NounString = NO -->
# Spike information limits memory stability {#ch:MEMORY-INFORMATION}
<!-- vale ai-tells.NounString = YES -->

A neuron that receives spikes from a memory circuit can use them to estimate the value stored by that circuit. [Collecting more spikes helps distinguish nearby activity patterns, but during collection the pattern itself keeps moving.]{.key-statement} The same variability that limits readout also perturbs the recurrent network. Burak and Fiete connect these two effects by deriving a lower bound on memory diffusion from the information in the spikes.[^p1-info-main]

<!-- vale ai-tells.EmptyPadding = NO -->
<!-- vale ai-tells.FigurativeStays = NO -->
The useful quantity is how clearly a short spike sample distinguishes nearby memory values. Comparing that quantity with the random motion already derived gives a minimum rate of memory spreading. This is a limit for a particular network, so using it to compare different networks also requires keeping track of what changes and what stays fixed. More information can permit better stability without ensuring that a particular circuit achieves it.
<!-- vale ai-tells.FigurativeStays = YES -->
<!-- vale ai-tells.EmptyPadding = YES -->

We retain the memory coordinate $\theta$, initial value $\Theta$, firing rate $\bar r_i(\theta)$, synaptic time constant $\tau$, and diffusion convention $\operatorname{Var}(\Delta\theta)=2D\Delta t$. The [network projection](ch-memory-dynamics.html#sec-memory-linearization) determines which activity changes remain as changes in the stored value.

## Rate slopes and spike variability determine local information {#sec:MEMORY-FI}

<!-- vale ai-tells.ContrastiveFormulas = NO -->
<!-- vale ai-tells.FigurativeStays = NO -->
**Neural mechanism.** A receiving neuron gets spikes, not a label saying which angle the memory circuit represents. The same angle can produce different spike counts on different trials. To read the angle, an observer needs to know how each cell's expected count changes with angle and how much that count fluctuates when the angle stays fixed.
<!-- vale ai-tells.FigurativeStays = YES -->
<!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- vale ai-tells.EmptyPadding = NO -->
[[**Fisher information**]{.definition-term custom-style="Definition Term"} measures how sensitively the probabilities of possible observations change when the value being estimated changes slightly.]{.definition-explanation} Here the observations are spike counts and the unknown value is the circuit's present memory coordinate $\theta$. [Information is large when a small change in the stored value changes the expected counts strongly compared with their random spread.]{.key-statement} It is a property of the spike model at a particular value of $\theta$, before choosing a rule for decoding the spikes.
<!-- vale ai-tells.EmptyPadding = YES -->

“Local” means comparing values close to the current one. A neuron can distinguish small changes near one angle yet respond identically at two distant angles. Fisher information describes the nearby distinction. A large value alone does not resolve that distant ambiguity.

Let $h$ be the observation duration in seconds and $n_i$ neuron $i$'s spike count. For this calculation, hold $\theta$ effectively fixed during observation and assume positive rates. Once that state is fixed, the model treats the counts from different cells as independent Poisson variables. Their mean and variance are both $\bar r_i(\theta)h$. This is a short observation approximation to the recurrent circuit, whose state can otherwise move while spikes are collected.

<div class="publisher-worked-calculation publisher-fold-always">

**Example: extra background spikes can make an angle harder to read.**

<!-- vale ai-tells.FormalTransitions = NO -->
Consider an illustrative neuron with rate 40 spikes per second at the angle of interest. Near that angle, each degree of change increases its rate by 20 spikes per second. In a 0.1-second observation, its mean count is 4 and its standard deviation is $\sqrt{4}=2$ spikes. The mean count changes by 2 spikes per degree. Thus the change per degree is as large as one standard deviation of the count noise.
<!-- vale ai-tells.FormalTransitions = YES -->

<!-- vale ai-tells.EmptyPadding = NO -->
Now add 120 spikes per second of background firing that does not depend on angle. The mean count becomes 16 and its standard deviation becomes 4 spikes. The change per degree remains 2 spikes. The same angle change is now half as large relative to the noise. Squaring that comparison gives one quarter of the original information. More spikes have made this particular comparison worse because they added variability without increasing the response to angle.
<!-- vale ai-tells.EmptyPadding = YES -->

These numbers describe a chosen local tuning curve and a Poisson count model, not measured neurons. Multiplying the entire tuning curve would be a different change: it would increase the slope as well as the mean rate.

</div>

**Mathematical result.** Write $r_i'=d\bar r_i/d\theta$ for the rate change per unit change in the represented value. In an interval $h$, the expected count changes by $h r_i'\,\delta\theta$ for a small change $\delta\theta$. Dividing the squared change per unit $\theta$ by the count variance gives

$$
I_{h,i}(\theta)=\frac{(h r_i')^2}{\bar r_i h}
=h\frac{(r_i')^2}{\bar r_i}.
$$

This sensitivity divided by noise expression is exactly the single-cell Fisher information for the Poisson model. For independent counts, the contributions add:

$$
I_h(\theta)=h\sum_i\frac{(r_i')^2}{\bar r_i}=hJ(\theta),
\qquad
\boxed{J(\theta)=\sum_i\frac{(r_i')^2}{\bar r_i}.}
$$

[The [**internal Fisher information rate**]{.definition-term custom-style="Definition Term"} $J$ is the information per second in these spikes about the circuit's current represented value.]{.definition-explanation} “Internal” identifies what is being estimated: the state maintained by the circuit after the cue has disappeared. If angles are measured in radians, $I_h$ has units $\mathrm{rad}^{-2}$ and $J$ has units $\mathrm{rad}^{-2}\mathrm{s}^{-1}$. They are not numbers of stored bits.[^p1-fi-source]

The expression explains three ways a code can change:

- Doubling a cell's tuning slope while keeping its rate fixed gives four times the local information.
- Adding constant background firing while keeping the slope fixed lowers its contribution, as in the example.
- Adding another independently fluctuating, tuned cell adds information. Shared fluctuations require a different calculation.

A rate peak has zero slope, so that cell contributes no information about infinitesimal angle changes at that point under this positive-rate Poisson formula. Other cells with nonzero slopes can still inform the population's estimate. The following curves show where each cell's contribution comes from.

<div class="figure-scroll">

{{block:fig:MEMORY-TUNING-INFORMATION}}

</div>

Both curves change by the same amount with angle. The higher curve has more Poisson count noise, which explains its lower information away from the peak. The formal definition below shows why the sensitivity divided by noise calculation is Fisher information.

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: likelihood, score, and Fisher information"}

Here the parameter being estimated is $\theta$ during the short observation. [A [**likelihood**]{.definition-term custom-style="Definition Term"} compares proposed parameter values by the probability each assigns to the observations already obtained.]{.definition-explanation} Suppose four spikes were recorded. A candidate angle predicting four spikes on average and one predicting sixteen assign different probabilities to that same count. Evaluating those probabilities as the proposed angle changes gives the likelihood. It is not, by itself, a probability distribution over the proposed angles.

For the full vector $\mathbf n$ of observed counts, independence gives

$$
p(\mathbf n\mid\theta)=\prod_i
\frac{[\bar r_i(\theta)h]^{n_i}e^{-\bar r_i(\theta)h}}{n_i!}.
$$

Taking the logarithm turns the product into a sum. With $r_i'=d\bar r_i/d\theta$,

$$
\ell(\theta)=\log p(\mathbf n\mid\theta)
=\sum_i\{n_i\log[\bar r_i(\theta)h]-\bar r_i(\theta)h-\log(n_i!)\},
$$

$$
S(\theta)=\frac{d\ell}{d\theta}
=\sum_i\frac{r_i'}{\bar r_i}(n_i-\bar r_i h).
$$

<!-- vale ai-tells.StackedAnaphora = NO -->
[The [**score**]{.definition-term custom-style="Definition Term"} $S$ is the slope of the log likelihood with respect to the proposed value.]{.definition-explanation} A positive score means that a small increase in the proposed angle makes the observed count pattern more likely. A negative score favors a small decrease. At the true value, these signed slopes average to zero over repeated spike samples because $E[n_i]=\bar r_i h$. Squaring before averaging prevents the positive and negative slopes from canceling:
<!-- vale ai-tells.StackedAnaphora = YES -->

$$
E[S^2]
=\sum_i\frac{(r_i')^2}{\bar r_i^2}\operatorname{Var}(n_i)
=h\sum_i\frac{(r_i')^2}{\bar r_i}.
$$

Products of centered counts from different cells average to zero by conditional independence. The remaining terms use $\operatorname{Var}(n_i)=\bar r_i h$. The general definition of Fisher information is $I_h(\theta)=E_\theta[S(\theta)^2]$: the mean squared score over data generated at $\theta$. Here it gives the Poisson expression $I_h=hJ$ derived above. Other spike distributions can give a different expression.

:::

**Interpretation: information limits how accurately the value can be read.** [An [**estimator**]{.definition-term custom-style="Definition Term"} is a rule that turns observed data into an estimated value, here $\hat\theta(\mathbf n)$.]{.definition-explanation} [It is [**unbiased**]{.definition-term custom-style="Definition Term"} if repeating the observation at a fixed true value gives estimates whose average equals that value.]{.definition-explanation} Individual estimates can still be wrong. Their variance measures their trial-to-trial spread around that average.

[The [**Cramér Rao bound**]{.definition-term custom-style="Definition Term"} puts a lower limit on that variance for estimators unbiased across the nearby values, under the smoothness conditions used in the proof:]{.definition-explanation}

$$
\boxed{\operatorname{Var}(\hat\theta)\ge\frac{1}{I_h(\theta)}=\frac{1}{hJ(\theta)}.}
$$

<!-- vale ai-tells.BareReaches = NO -->
<!-- vale ai-tells.EmptyPadding = NO -->
Four times the information halves this lower bound on the standard deviation. It does not promise that a particular decoder reaches the bound. The paper uses an approximation in which the spike sample is informative enough for a suitable estimator to approach it.[^p1-cr]
<!-- vale ai-tells.EmptyPadding = YES -->
<!-- vale ai-tells.BareReaches = YES -->

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: why inverse information bounds estimation variance"}

Assume the same estimator is unbiased throughout a neighborhood of $\theta$, the probabilities vary smoothly with $\theta$, and differentiation can be exchanged with summation over the counts. Differentiate $E_\theta[\hat\theta]=\theta$:

$$
1=\sum_{\mathbf n}\hat\theta(\mathbf n)\partial_\theta p(\mathbf n\mid\theta)
=E[\hat\theta S]
=E[(\hat\theta-\theta)S].
$$

The last equality uses $E[S]=0$. The Cauchy Schwarz inequality says that the squared average product of two variables is no greater than the product of their mean squares. Applying it to estimation error $\hat\theta-\theta$ and score $S$ gives

$$
1\le E[(\hat\theta-\theta)^2]E[S^2],
\qquad
\boxed{\operatorname{Var}(\hat\theta)\ge\frac{1}{Jh}.}
$$

Unbiasedness makes the mean squared error equal to the variance. Dividing by $E[S^2]=I_h=hJ$ gives the bound when that information is positive and finite.

:::

[A [**prior distribution**]{.definition-term custom-style="Definition Term"} describes which parameter values were more plausible before observing these spikes.]{.definition-explanation} A decoder that uses this additional knowledge, or accepts a systematic error, has a different error problem. The bound above also needs care near boundaries or zero firing rates. For sensory estimation the same Poisson formula applies when the rates depend on a present stimulus, whereas here they depend on a maintained internal value.

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.FigurativeStays = NO -->
<!-- vale ai-tells.OverusedVocabulary = NO -->
Finally, $I_h=hJ$ assumes that the represented value stays effectively fixed during observation. Longer collection in a freely evolving memory circuit also allows that value to wander. The next section links $J$ to this physical wandering, and the [readout chapter](ch-memory-readout.html) treats what changes when the observer tries to recover the initial value. See [main Eq. 3, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2) and [SI Section IV, pp. 9–10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9).
<!-- vale ai-tells.OverusedVocabulary = YES -->
<!-- vale ai-tells.FigurativeStays = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

## Spike information sets a lower bound on memory diffusion {#sec:MEMORY-BOUND}

**Neural mechanism.** The network has no access to its exact firing rates as noiseless numbers. Its recurrent input is built from the same random spikes that an external observer sees. The lower bound on diffusion follows directly by comparing the state sensitivity of the network with the spike information.

**Mathematical derivation.** Cauchy Schwarz bounds a dot product by the product of the two vector lengths. Here the normalization of the memory projection fixes that dot product, while the two lengths measure diffusion and information. From the [projection and diffusion calculation](ch-memory-dynamics.html#sec-memory-diffusion),

$$
2D=\sum_i v_i^2\bar r_i,
\qquad
u_i=\tau r_i',
\qquad
\sum_i v_i u_i=1.
$$

Define two vectors $a_i=v_i\sqrt{\bar r_i}$ and $b_i=r_i'/\sqrt{\bar r_i}$. Their dot product is

$$
\sum_i a_i b_i=\sum_i v_i r_i'=\frac{1}{\tau}.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Their squared lengths are $\sum_i a_i^2=2D$ and $\sum_i b_i^2=J$. Cauchy Schwarz therefore gives
<!-- vale ai-tells.FormalTransitions = YES -->

$$
\left(\frac1\tau\right)^2
\le\left(\sum_i a_i^2\right)\left(\sum_i b_i^2\right)=2DJ,
$$

or

$$
\boxed{D\ge\frac{1}{2\tau^2J}.}
$$

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
**Interpretation.** This proof uses the general left vector formula, so symmetric weights are unnecessary. It is a shorter teaching reconstruction of the scalar proof in SI Section V. Its assumptions are those used to derive $D$ and $J$. It is not a general statement about all possible noisy memory systems.[^p1-bound-source]
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

The units agree: $\tau^2J$ has units of time per coordinate squared, so its reciprocal has the units of diffusion. [Small internal information forces a large minimum diffusion coefficient. Large information allows small diffusion, but does not guarantee it.]{.key-statement}

**Neural mechanism.** [Reaching the bound requires the network's retained response to each cell's spike noise to match that cell's information about memory.]{.key-statement} A cell that adds retained noise without helping distinguish nearby values prevents equality.

**Mathematical derivation.** Equality requires the two vectors in the proof to be proportional:

$$
v_i=c\frac{r_i'}{\bar r_i}
\quad\text{for every contributing cell},
\qquad c=\frac{1}{\tau J}.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Cells with zero tuning slope cannot contribute extra projected noise if equality is to hold. In a symmetric network, $v_i$ is proportional to $g_i'$, and $r_i'=\phi'(\bar g_i)g_i'$. At each state, the participating cells therefore need a common value of $\phi'(\bar g_i)/\phi(\bar g_i)$. A sufficient way to satisfy this at all states is to choose that ratio equal to the same constant $k$ throughout the relevant input range. Solving
<!-- vale ai-tells.FormalTransitions = YES -->

$$
\frac{d}{dg}\log\phi(g)=k
$$

gives $\phi(g)=A e^{kg}$.

**Interpretation.** This exponential family attains equality for symmetric weights with Poisson noise, under the other model assumptions. It is a sufficient condition, rather than a general necessity: the common ratio may depend on the current memory state.[^p1-equality]

::: {.publisher-clarification-note .publisher-fold-always title="Check: equality can also hold with a linear transfer rule"}

<!-- vale ai-tells.FormalTransitions = NO -->
The [mutual-excitation example](ch-memory-long-delays.html#sec-memory-long-time) shows why equality does not require an exponential transfer rule. Set its bias $b_0=0$ and use the linear rule $\phi(g)=g/\tau$ on positive inputs. Its fixed states are $s_1=s_2=\theta>0$, with $\mathbf u=(1,1)^T$ and $\mathbf v=(1/2,1/2)^T$. Both rates are $\theta/\tau$, and both rate derivatives are $1/\tau$. Therefore
<!-- vale ai-tells.FormalTransitions = YES -->

$$
2D=\frac{\theta}{2\tau},\qquad
J=\frac{2}{\tau\theta},\qquad
2DJ=\frac{1}{\tau^2}.
$$

<!-- vale ai-tells.ConclusionMarkers = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
Equality holds throughout this family even though its transfer rule is linear. At each state both cells receive the same input, and the ratio $\phi'/\phi=1/\theta$ changes between states. To conclude that equality forces an exponential rule, we need additional restrictions linking the participating input values across cells and states. Continuous variation of the represented value alone does not supply them. This qualification concerns the source's claim that equality requires an exponential rule. The information–diffusion inequality remains unchanged.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.ConclusionMarkers = YES -->

:::

<div class="publisher-worked-calculation publisher-fold-always">

**Example: the same diffusion with a looser information bound.**

<!-- vale ai-tells.ContrastiveFormulas = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
In the two cell mutual inhibition model, use $b=200$ activation units and $\tau=0.1\,\mathrm{s}$. The memory coordinate is an activation difference, not an angle. At $\theta=0$ both rates are $1000\,\mathrm{s}^{-1}$ and their slopes are $\pm5\,\mathrm{s}^{-1}$ per activation unit. Thus
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.ContrastiveFormulas = YES -->

$$
J=\frac{25}{1000}+\frac{25}{1000}=0.05,
\qquad D=\frac{b}{2\tau}=1000.
$$

Here $J$ has units of inverse activation unit squared per second, and $D$ has activation unit squared per second. The bound is $1/(2\tau^2J)=1000$, so equality holds at this balanced state. At $\theta=100$, the rates become $1500$ and $500\,\mathrm{s}^{-1}$, while their slopes stay $\pm5$. Now

$$
J=\frac{25}{1500}+\frac{25}{500}=\frac1{15}\simeq0.06667,
\qquad \frac1{2\tau^2J}=750.
$$

The actual diffusion remains $1000$. The inequality is strict because these two unequal rates no longer align the network's projection weights with the information optimal weights. This also shows why equality at a special state does not force the transfer function to be exponential on its whole domain. A constant lower bound attained everywhere and an accidental equality at one state are different claims.



<div class="figure-scroll">

{{block:fig:MEMORY-BOUND-STRICTNESS}}

</div>

The gap at $\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion. See [Diffusion bound, Eq. 4, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3).

</div>

<!-- vale ai-tells.FormalTransitions = NO -->
**Neural mechanism.** When a circuit stores several coordinates, a spike can shift more than one of them. Comparing each coordinate separately would miss combinations of shifts. The information and diffusion must therefore describe these shared directions.
<!-- vale ai-tells.FormalTransitions = YES -->

**Mathematical derivation.** For $m$ memory coordinates the information is a matrix,

$$
J_{\alpha\beta}=\sum_i
\frac{\partial_{\theta_\alpha}\bar r_i\,
\partial_{\theta_\beta}\bar r_i}{\bar r_i}.
$$

The matrix calculation assumes that every independent small coordinate change can be distinguished through a change in rates, so $J$ is invertible. The matrix bound $2D\succeq\tau^{-2}J^{-1}$ means that every linear combination of coordinate displacements obeys the corresponding variance lower bound. Here $A\succeq B$ means $\mathbf z^T(A-B)\mathbf z\ge0$ for every real vector $\mathbf z$. To derive it, form $N\times m$ matrices $U_{i\alpha}=u_i^\alpha/\sqrt{\bar r_i}$ and $V_{i\alpha}=v_i^\alpha\sqrt{\bar r_i}$. Then

$$
U^TV=I,\qquad U^TU=\tau^2J,\qquad V^TV=2D.
$$

::: {.publisher-clarification-note .publisher-fold-always title="Check: the residual matrix proves the lower bound"}

Set $Q=V-U(U^TU)^{-1}$. Expanding $Q^TQ$ and using $U^TV=I$ gives

$$
Q^TQ=V^TV-(U^TU)^{-1}
=2D-\tau^{-2}J^{-1}\succeq0.
$$

:::

**Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. If $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]

<!-- vale ai-tells.BareHolds = NO -->
<!-- vale ai-tells.ExplainerHeadings = NO -->
<!-- vale ai-tells.FigurativeHolds = NO -->
## Improving persistence depends on what a comparison holds fixed {#sec:MEMORY-COMPARISONS}
<!-- vale ai-tells.FigurativeHolds = YES -->
<!-- vale ai-tells.ExplainerHeadings = YES -->
<!-- vale ai-tells.BareHolds = YES -->

<!-- vale ai-tells.FigurativeStays = NO -->
<!-- vale ai-tells.HedgingPhrases = NO -->
**Neural mechanism.** [The inequality compares diffusion and information for the same network. To compare different networks, we must say what stays fixed.]{.key-statement} Otherwise an apparent benefit of a parameter change may come from changing another property at the same time. The comparisons below control how added neurons, altered firing rates, or slower synaptic decay affect the tuning curves and recurrent input.
<!-- vale ai-tells.HedgingPhrases = YES -->
<!-- vale ai-tells.FigurativeStays = YES -->

<!-- vale ai-tells.ContrastiveFormulas = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
**Mathematical derivation.** Increasing $N$ while retaining the same distribution of tuning curves and scaling weights as $1/N$ keeps individual inputs and rates fixed. The sums in the symmetric formula scale as $N$ in the numerator and $N^2$ in the denominator. Consequently $D\propto1/N$, while $J\propto N$. This is a controlled density or population replication comparison, not a promise about adding arbitrary neurons.
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.ContrastiveFormulas = YES -->

If all tuning rates are multiplied by a factor $a$, their slopes are also multiplied by $a$, so $J\mapsto aJ$. For equality achieving exponential networks, $D\mapsto D/a$ immediately follows. The same scaling follows from the symmetric diffusion formula when the change preserves $g_i'$ up to a common scale and preserves the tuning geometry. For a general fixed nonlinear transfer rule, multiplying rates need not preserve those quantities or even the attractor. The paper's rate comparison is made with the tuning shapes and appropriate network scaling held under control.[^p1-scaling]

Changing $\tau$ while holding the rate tuning curves and their input relation fixed gives $D\propto\tau^{-2}$ in the symmetric formula. Maintaining those curves requires retuning the network, because $\bar s=\tau\bar r$.

<!-- vale ai-tells.FigurativeStays = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
At fixed rates, longer-lasting spike effects give larger mean activations. The activation difference between two nearby stored values also grows in proportion to $\tau$. In this symmetric comparison, one spike's unit activation change therefore produces a smaller displacement of the stored value: the projection weights scale as $1/\tau$. The spike variance per unit time stays fixed, so the retained variance scales as $1/\tau^2$.
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.FigurativeStays = YES -->

<!-- vale ai-tells.FormalTransitions = NO -->
In contrast, holding activation curves and dimensionless weights fixed in the linear two cell example makes rates scale as $1/\tau$, so $D=b/(2\tau)\propto\tau^{-1}$.
<!-- vale ai-tells.FormalTransitions = YES -->

**Interpretation.** These two statements concern different controlled comparisons. A larger cellular time constant can improve memory stability while the exponent of its effect depends on what the experiment keeps fixed.

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.StrawmanContrast = NO -->
**Neural mechanism.** The paper also links tuning width to memory persistence. The reason for its opposite predictions in one and three dimensions can be derived from the number of active cells and their slopes. This derivation is a teaching reconstruction of the tuning width argument cited in the main text, rather than a proof that every tuning family follows one power law.[^p1-width]
<!-- vale ai-tells.StrawmanContrast = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

Assume preferred positions $\mathbf c$ have uniform density $\rho$ in a $d$ dimensional stimulus or memory space. Away from boundaries, let identical tuning curves have fixed peak rate $a$ and a common shape $f$:

$$
\bar r_{\mathbf c}(\boldsymbol\theta)
=a f[(\boldsymbol\theta-\mathbf c)/w].
$$

The width $w$ is varied while $a$, $\rho$, and the shape $f$ are fixed.

**Mathematical derivation.** For one coordinate direction $\alpha$, replace the population sum by an integral and substitute $\mathbf z=(\boldsymbol\theta-\mathbf c)/w$:

$$
J_{\alpha\alpha}
\simeq\rho\int d^d c\,
\frac{a^2w^{-2}(\partial_\alpha f)^2}{af}
=\rho a w^{d-2}
\int d^d z\,\frac{(\partial_\alpha f)^2}{f}.
$$

<!-- vale ai-tells.CataphoricForecasting = NO -->
Two factors determine how information changes with tuning width:
<!-- vale ai-tells.CataphoricForecasting = YES -->

- The volume element contributes $w^d$ because broader fields recruit more neurons.
- The squared slope contributes $w^{-2}$ because broader curves change more slowly.

<!-- vale ai-tells.FormalTransitions = NO -->
Each diagonal entry therefore scales as $J_{\alpha\alpha}\propto w^{d-2}$. Now restrict the tuning shape $f$ to depend only on distance from its center. Uniformly distributing those centers makes every coordinate direction equivalent: off-diagonal information terms vanish, and all diagonal entries are equal. For an exponential network that attains the matrix bound, $D_{\alpha\alpha}=1/(2\tau^2J_{\alpha\alpha})\propto w^{2-d}$.
<!-- vale ai-tells.FormalTransitions = YES -->

**Interpretation.** The resulting comparisons are:

- Narrower curves help in $d=1$.
- Width has no leading effect in $d=2$.
- Broader curves help in $d=3$.

<!-- vale ai-tells.BareReaches = NO -->
[These conclusions change under another resource constraint. Fixing the total population spike rate instead of peak rate makes $a\propto w^{-d}$, giving $J\propto w^{-2}$ in every dimension.]{.key-statement} Sparse coverage, a large baseline rate, finite boundaries, correlated noise, or a width too small for the population integral can also change the comparison. Attaining equality means the network reaches the diffusion lower bound for its information rate and synaptic time constant. Minimizing diffusion still requires deciding how much information the allowed architecture and firing budget can supply.
<!-- vale ai-tells.BareReaches = YES -->

<!-- vale ai-tells.EmptyPadding = NO -->
<!-- vale ai-tells.ExplainerLeads = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
<!-- vale ai-tells.ParallelStaccato = NO -->
If an external stimulus produces the same tuning curves as the network's input free memory states, the sensory and internal Fisher information are equal. In a symmetric exponential network, maximizing this information then improves sensory estimation and minimizes memory diffusion together. This is why the paper suggests that one circuit could support both sensory estimation and memory storage. The mathematical compatibility does not establish where a particular animal stores a memory, and the equality of tuning curves must be checked rather than inferred from the shared formula.[^p1-colocation]
<!-- vale ai-tells.ParallelStaccato = YES -->
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.ExplainerLeads = YES -->
<!-- vale ai-tells.EmptyPadding = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-info-main]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650, main pp. 2–4, Eqs. 3–5. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-fi-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 9–10, Section IV, Eqs. S42–S44; main Eq. 3. [DOI](https://doi.org/10.1073/pnas.1117386109). The score variance calculation is expanded for teaching.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
[^p1-cr]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 3, Information-Diffusion Inequality and Saturation. [DOI](https://doi.org/10.1073/pnas.1117386109). The scalar Cramér Rao proof is a teaching reconstruction of the bound invoked there.
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-bound-source]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–11, Eqs. S45–S49; main Eq. 4. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-equality]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 11, Eqs. S47–S51. [DOI](https://doi.org/10.1073/pnas.1117386109). The linear-family counterexample is a guide calculation qualifying the source's converse.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-matrix]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 10–12, Eqs. S44 and S52–S56. [DOI](https://doi.org/10.1073/pnas.1117386109). The residual matrix proof here is an equivalent teaching reconstruction.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-scaling]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 2, discussion after Eq. 2; pp. 5–6, Weak Fluctuations. [DOI](https://doi.org/10.1073/pnas.1117386109). Comparisons with different held quantities are made explicit here.
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-width]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, p. 4, tuning width discussion. [DOI](https://doi.org/10.1073/pnas.1117386109). The paper cites Zhang and Sejnowski's tuning work. The integral scaling and alternative firing budget here are teaching derivations, not a separate verification of that cited paper.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-colocation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, pp. 4–5, sensory representation comparison and footnote concerning similarity of sensory and persistent tuning. [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->
