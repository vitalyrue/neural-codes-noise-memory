# Patterns of variable spikes can represent a value {#ch:FOUNDATIONS}

<!-- vale ai-tells.CataphoricForecasting = NO -->
<!-- vale ai-tells.VerbTricolon = NO -->
The eyes can hold a position after a brief movement command has ended. An animal can also keep track of its location while the activity of individual neurons fluctuates. [Both abilities require a useful quantity to remain represented in a changing biological system.]{.key-statement} The three papers study different parts of this problem: the loss of a stored value, the origin of slow eye motion, and the arrangement of spatial firing patterns.
<!-- vale ai-tells.VerbTricolon = YES -->
<!-- vale ai-tells.CataphoricForecasting = YES -->

Before asking how a circuit keeps a value, we need to know what its signals do. We begin with brief neural spikes and the eye muscles they activate, explaining how repeated activation can maintain an eye angle. We next establish the equations that connect spikes, synaptic input and firing rate. With that physical meaning in place, we ask how a pattern of rates represents an angle or an animal's location. A model of spike counts shows why one brief observation can be uncertain and how combining counts from several cells can help. Finally, we separate shared variation, random spreading and a change in the average value. These distinctions prepare us to interpret both a memory model and measurements of eye motion.

## Repeated spikes maintain eye muscle tension {#sec:FOUNDATIONS-EYE-ACTION}

For the eye to stay directed at a target, its muscles must keep exerting force after the movement command ends.

<!-- vale ai-tells.StrawmanContrast = NO -->
[A neuron communicates through brief electrical events called [**spike**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} [A [**firing rate**]{.definition-term custom-style="Definition Term"} is the expected number of spikes per unit time.]{.definition-explanation} A rate of 20 hertz means an average of 20 spikes per second under the specified conditions, rather than a promise of one spike every 50 milliseconds.
<!-- vale ai-tells.StrawmanContrast = YES -->

**Anatomy: muscles turn the eyeball.** In humans and macaques, the eyeball rotates within the bony eye socket, or orbit. [The six [**extraocular muscles**]{.definition-term custom-style="Definition Term"} attach to the outside of the eyeball and control its orientation.]{.definition-explanation} The medial rectus pulls it toward the nose; the lateral rectus pulls it away. The superior and inferior rectus and the two oblique muscles contribute to vertical movement and rotation about the line of sight. Their actions depend on the eye's orientation.[^p-eye-anatomy]

[**Ocular motoneurons (OMNs)**]{.definition-term custom-style="Definition Term"} [are neurons that activate these muscles through long nerve fibres.]{.definition-explanation} Their cell bodies lie in brainstem groups, and these fibres travel through three cranial nerves. The abducens nerve, VI, supplies the lateral rectus; the trochlear nerve, IV, supplies the superior oblique; the oculomotor nerve, III, supplies the other four. For horizontal gaze, changing the relative pull of the medial and lateral rectus rotates the eye. [A force's turning effect is its [**torque**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Opposing torques can balance even while the muscles remain under tension.[^p-eye-anatomy]

**Repeated spikes maintain tension.** Each motor spike affects muscle force for longer than the electrical event lasts. Repeated activation and the combined action of many muscle fibres give a smoother force than a sequence of isolated eye movements. [**Tonic firing**]{.definition-term custom-style="Definition Term"} [means sustained firing during the holding period.]{.definition-explanation} It need not be perfectly periodic. During a rapid repositioning movement, called a [**saccade**]{.definition-term custom-style="Definition Term"}, a brief strong drive moves the eye; a sustained position-dependent drive then holds the new angle. This is the pulse-and-step description: the step means continuing drive, not one more spike.[^p-eye-mechanics][^p-eye-plasticity]

The mechanical properties contribute in different ways:

- [**Elasticity**]{.definition-term custom-style="Definition Term"} [creates restoring forces when muscles and surrounding tissues are stretched.]{.definition-explanation} At an off-centre gaze angle, active muscle torque must balance the restoring tendency.
- [**Viscosity**]{.definition-term custom-style="Definition Term"} [resists motion and dissipates mechanical energy.]{.definition-explanation} It damps rapid changes but supplies no holding torque once velocity is zero.
- [**Inertia**]{.definition-term custom-style="Definition Term"} [is resistance to a change in angular velocity.]{.definition-explanation} It matters during acceleration, not as a force holding a stationary eye. In primate eye movements, elastic and viscous effects dominate inertia.[^p-eye-mechanics]

[Mechanical damping smooths movement; sustained neural drive selects the angle around which the eye is held. Inertia cannot preserve a stationary gaze against an unbalanced elastic pull.]{.key-statement}

So far we have followed the output from motor neurons to muscles. The next step is a model of how neurons act on one another and sustain a signal.

## Recurrent spikes renew decaying synaptic activity {#sec:MEMORY-SPIKES}

**Neural mechanism.** How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. [Incoming activations determine new firing rates. The resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.]{.key-statement}

[Neurons affect one another through connections called [**synapse**]{.definition-term custom-style="Definition Term"}s.]{.definition-explanation} In the models used here, inputs have two contrasting effects:

- [An [**excitatory input**]{.definition-term custom-style="Definition Term"} increases a receiving neuron's tendency to fire.]{.definition-explanation}
- [An [**inhibitory input**]{.definition-term custom-style="Definition Term"} reduces it.]{.definition-explanation}

The effect of a spike can last beyond the spike itself because synaptic input decays over time. [When neurons send signals back into the same population, the circuit has [**recurrent connectivity**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Such feedback can maintain activity after an external signal disappears.

Burak and Fiete (2012) use the following equations for interactions inside a neural circuit. These describe synaptic activity; muscle motion is a later part of the pathway. The model assumes fixed connection weights, constant input biases and a common synaptic decay time. Its statistical rule for spike timing is explained in the [spike-count section](#sec-foundations-poisson).[^p1-model]

**Model dynamics: Burak and Fiete (2012), Equation 7.** [The [**synaptic activation**]{.definition-term custom-style="Definition Term"} $s_i$ tracks the decaying effect of neuron $i$'s outgoing spikes on receiving cells.]{.definition-explanation} The paper writes its dynamics as

$$
\dot s_i+\frac{s_i}{\tau}=\sum_\alpha\delta(t-t_i^\alpha).
$$

The dot means $\dot s_i=ds_i/dt$, and $\tau$ is the decay time in seconds. [The [**Dirac delta**]{.definition-term custom-style="Definition Term"} $\delta(t-t_i^\alpha)$ represents an instantaneous unit pulse at the spike time $t_i^\alpha$; its integral across that time is one.]{.definition-explanation} Between spikes, the right-hand side is zero and activation decays. Integrating through one spike gives a one-unit increase in $s_i$. [Read Eq. 7 as a balance: spikes add activation, while the term $s_i/\tau$ removes it.]{.key-statement} [Original Eq. 7, PDF p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5).

**Equivalent count form.** Let $N_i(t)$ count neuron $i$'s spikes up to time $t$. Integrating the pulse train counts the spikes, so the same dynamics can be written as

$$
ds_i=-\frac{s_i}{\tau}\,dt+dN_i(t).
$$

Equivalently, if its spikes occur at times $t_i^\alpha$,

$$
s_i(t)=\sum_{t_i^\alpha\le t}\exp[-(t-t_i^\alpha)/\tau]
$$

once the contribution from any activation present at the starting time has decayed. The sum includes a spike at time $t$, so it gives the activation immediately after that spike. Here $s_i$ is dimensionless in the convention that each spike adds one unit.

For five illustrative spike times, the plot shows the events and the activation they leave behind.

<div class="figure-scroll">

{{block:fig:MEMORY-SPIKE-TRACE}}

</div>

The activation retains a decaying contribution from earlier spikes, so a spike train and its activation trace are different objects.

**From activation to new spikes: Equations 8 and 9.** The total input to neuron $i$ combines the activation arriving from other cells with a constant input bias:

$$
g_i=\sum_jW_{ij}s_j+b_i.\qquad\text{(Burak and Fiete, Eq. 8)}
$$

The expected firing rate then follows from that input:

$$
r_i=\phi(g_i).\qquad\text{(Burak and Fiete, Eq. 9)}
$$

Here $r_i$ has units of spikes per second. These equations specify how the input sets the rate; they do not prescribe each spike's time.

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. [The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate.]{.definition-explanation} For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model]
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.FormalTransitions = NO -->
A spike from cell $j$ raises $s_j$ by one and therefore changes the input to cell $i$ by $W_{ij}$. That contribution then decays over time $\tau$. For an increasing transfer function, a positive weight raises the receiving cell's rate and a negative weight lowers it. The resulting new spikes affect other cells in turn. Thus the weights set where a disturbance goes, the transfer function sets the rate response, and $\tau$ sets how long each synaptic contribution lasts. The input $g_i$ is in the model's input units. It is not specified as a measured membrane voltage.
<!-- vale ai-tells.FormalTransitions = YES -->

Together, Eqs. 7–9 describe one feedback cycle: spikes change synaptic activation, weighted activation changes input, and input changes the rate of new spikes. The next question is how the resulting pattern of rates can represent an eye angle or location.

## Patterns of firing rates represent a value {#sec:FOUNDATIONS-SPIKES}

[A [**tuning curve**]{.definition-term custom-style="Definition Term"} gives a neuron's expected firing rate as a function of a represented variable.]{.definition-explanation} For eye angle $\theta$, a simple local model is $r_i(\theta)=r_{i,0}+k_i\theta$. Neuron $i$ has baseline rate $r_{i,0}$ in spikes per second and slope $k_i$ in spikes per second per degree. This rate baseline is different from the input bias $b_i$ in Eq. 8. The linear expression can describe an active range, but it must be modified where it would predict negative firing. The eye paper includes a firing threshold and terms for movement as well as position.[^f-eye]

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

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: where the Poisson count formula and its variance come from"}

**From random spike times to a count.** Hold the rate $r$ fixed over the observation of length $\Delta t$. Divide that observation into $n$ short bins of width $\delta t=\Delta t/n$. Approximate each bin by one independent spike-or-no-spike trial, with spike probability

$$
p=r\delta t=\frac{\lambda}{n},\qquad \lambda=r\Delta t.
$$

Take $n$ large enough that $p<1$. This construction assumes a constant chance of a spike per unit time and independence between nonoverlapping bins. In the continuous-time limit, the chance of two or more spikes in one bin becomes negligible compared with its width. These are assumptions of the Poisson model, not properties of every recorded neuron.[^f-poisson-limit]

A particular pattern with spikes in exactly $k$ bins and silence in the other $n-k$ bins has probability $p^k(1-p)^{n-k}$. There are

$$
\binom nk=\frac{n(n-1)\cdots(n-k+1)}{k!}
$$

ways to choose the occupied bins. The numerator chooses them in order; dividing by $k!=1\cdot2\cdots k$ removes the repeated counting of the same set in different orders. For $k=0$, there is one empty set and $0!=1$. Adding the probabilities of all these patterns gives

$$
\begin{aligned}
\Pr(K_n=k)
&=\binom nk\left(\frac{\lambda}{n}\right)^k
  \left(1-\frac{\lambda}{n}\right)^{n-k}\\
&=\frac{\lambda^k}{k!}
  \left[\prod_{j=0}^{k-1}\left(1-\frac{j}{n}\right)\right]
  \left(1-\frac{\lambda}{n}\right)^{n-k}.
\end{aligned}
$$

Here $K_n$ is the count in the finite-bin construction. Keep the observation duration, $\lambda$, and the integer $k$ fixed while making the bins finer. The finite product tends to one. The remaining factor tends to

$$
\lim_{n\to\infty}\left(1-\frac{\lambda}{n}\right)^{n-k}
=e^{-\lambda}.
$$

For example, its logarithm is $(n-k)\log(1-\lambda/n)$, which tends to $-\lambda$ because $\log(1-u)/u\to-1$ as $u\to0$. Exponentiating gives the displayed limit. The limiting count $K$ therefore obeys

$$
\boxed{\Pr(K=k)=e^{-\lambda}\frac{\lambda^k}{k!}.}
$$

[The exponential comes from requiring silence in all the unoccupied bins. The factor $\lambda^k$ comes from the $k$ spike probabilities together with the number of possible bin locations, and $k!$ corrects repeated counting.]{.key-statement} In particular, $e^{-\lambda}$ is the probability of no spikes. A positive expected count can therefore coexist with a silent observation.

**From the count formula to its mean and variance.** Shifting the summation index by one gives

$$
\begin{aligned}
\mathbb E[K]
&=e^{-\lambda}\sum_{k=1}^{\infty}k\frac{\lambda^k}{k!}\\
&=\lambda e^{-\lambda}\sum_{j=0}^{\infty}\frac{\lambda^j}{j!}
=\lambda,
\end{aligned}
$$

where the last sum is $e^\lambda$. Shifting by two similarly gives

$$
\mathbb E[K(K-1)]
=e^{-\lambda}\sum_{k=2}^{\infty}
  \frac{\lambda^k}{(k-2)!}
=\lambda^2e^{-\lambda}\sum_{j=0}^{\infty}\frac{\lambda^j}{j!}
=\lambda^2.
$$

Since $K^2=K(K-1)+K$,

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
For a predetermined rate function $r(t)$, the time-varying Poisson model has a count parameter $\lambda=\int r(t)\,dt$ over the observation. In a recurrent network, however, $r(t)$ itself depends on earlier spikes. The whole-interval count need not then be Poisson. The useful independence statement is local and conditional: given the current modeled state, the elementary spike-generation noise is independent across cells in the basic 2012 model. The changing state can still produce correlations across time and across neurons. This qualification prevents treating a recurrent Poisson network as a collection of independent complete spike trains.
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

[^f-poisson-limit]: Massachusetts Institute of Technology, OpenCourseWare (2018). *Introduction to Probability: Lecture 22 notes, the Poisson process*. [PDF, pp. 3–5](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/d92a00a2bc9d20d84ad11d43be0e7ae0_MITRES_6_012S18_L22.pdf#page=3). The guide reconstructs the independent-bin limit using $r$ for rate and $\lambda=r\Delta t$ for expected count.

[^p-eye-anatomy]: Dragoi, V. (2026, July 7 review). *Ocular Motor Control*. Neuroscience Online, Section 3, Chapter 8, McGovern Medical School, UTHealth Houston. [Sections 8.2–8.3 and Fig. 8.1](https://nba.uth.tmc.edu/neuroscience/m/s3/chapter08.html). Anatomy, muscle innervation and visual/vestibular control.

[^p-eye-mechanics]: Anderson, S. R., Porrill, J., Sklavos, S., Gandhi, N. J., Sparks, D. L., and Dean, P. (2009). *Dynamics of primate oculomotor plant revealed by effects of abducens microstimulation*. Journal of Neurophysiology, 101(6), 2907–2923. [DOI](https://doi.org/10.1152/jn.91045.2008). Introduction and stimulation/relaxation results. The spring-and-damper calculation is a guide reconstruction of the physical roles, not a fitted reproduction of these experiments.

[^p-eye-plasticity]: Major, G., Baker, R., Aksay, E., Mensh, B., Seung, H. S., and Tank, D. W. (2004). *Plasticity and tuning by visual feedback of the stability of a neural integrator*. Proceedings of the National Academy of Sciences, 101(20), 7739–7744. [DOI](https://doi.org/10.1073/pnas.0401970101). Fig. 1 for movement and holding signals; Figs. 2–4 and Discussion for goldfish training, reversibility and unresolved cellular mechanisms.

[^p1-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). [Main Eq. 1 and the steady state, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,60); [Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372).
