# Stable representations can accumulate error {#ch:PERSISTENCE}

Holding the eye at an angle requires muscles to maintain tension after the command to move has ended. The brain must therefore keep producing a position-dependent signal. The horizontal eye angle considered here is one number, but a circuit can represent it through thousands of neural activities. A disturbance can change those activities without changing the represented value. Another disturbance can leave a coherent activity pattern while changing the value. The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]

<!-- vale ai-tells.FigurativeStays = NO -->
We first follow the physical path from motor neurons to muscles and eye rotation, separating mechanical smoothing from the neural command that holds a gaze angle. A small circuit example then shows why some disturbances fade while others leave a different stored angle. Repeating those lasting changes gives the diffusion calculation. The final distinction is between this changing value and an irregular spatial map that stays fixed. It explains why the memory, eye-motion, and place-field papers need different models even though all three concern variable neural signals.
<!-- vale ai-tells.FigurativeStays = YES -->

## Sustained muscle tension holds the eye against elastic restoring forces {#sec:PERSISTENCE-EYE-MECHANICS}

**Anatomy: muscles turn the eyeball.** In humans and macaques, the eyeball rotates within the bony eye socket, or orbit. [The six [**extraocular muscles**]{.definition-term custom-style="Definition Term"} attach to the outside of the eyeball and control its orientation.]{.definition-explanation} The medial rectus pulls it toward the nose; the lateral rectus pulls it away. The superior and inferior rectus and the two oblique muscles contribute to vertical movement and rotation about the line of sight. Their actions depend on the eye's orientation.[^p-eye-anatomy]

[**Ocular motoneurons (OMNs)**]{.definition-term custom-style="Definition Term"} [are neurons that activate these muscles through long nerve fibres.]{.definition-explanation} Their cell bodies lie in brainstem groups, and these fibres travel through three cranial nerves. The abducens nerve, VI, supplies the lateral rectus; the trochlear nerve, IV, supplies the superior oblique; the oculomotor nerve, III, supplies the other four. For horizontal gaze, changing the relative pull of the medial and lateral rectus rotates the eye. [A force's turning effect is its [**torque**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} Opposing torques can balance even while the muscles remain under tension.[^p-eye-anatomy]

**Repeated spikes maintain tension.** Each motor spike affects muscle force for longer than the electrical event lasts. Repeated activation and the combined action of many muscle fibres give a smoother force than a sequence of isolated eye movements. [**Tonic firing**]{.definition-term custom-style="Definition Term"} [means sustained firing during the holding period.]{.definition-explanation} It need not be perfectly periodic. During a rapid repositioning movement, called a [**saccade**]{.definition-term custom-style="Definition Term"}, a brief strong drive moves the eye; a sustained position-dependent drive then holds the new angle. This is the pulse-and-step description: the step means continuing drive, not one more spike.[^p-eye-mechanics][^p-eye-plasticity]

The mechanical properties contribute in different ways:

- [**Elasticity**]{.definition-term custom-style="Definition Term"} [creates restoring forces when muscles and surrounding tissues are stretched.]{.definition-explanation} At an off-centre gaze angle, active muscle torque must balance the restoring tendency.
- [**Viscosity**]{.definition-term custom-style="Definition Term"} [resists motion and dissipates mechanical energy.]{.definition-explanation} It damps rapid changes but supplies no holding torque once velocity is zero.
- [**Inertia**]{.definition-term custom-style="Definition Term"} [is resistance to a change in angular velocity.]{.definition-explanation} It matters during acceleration, not as a force holding a stationary eye. In primate eye movements, elastic and viscous effects dominate inertia.[^p-eye-mechanics]

[Mechanical damping smooths movement; sustained neural drive selects the angle around which the eye is held. Inertia cannot preserve a stationary gaze against an unbalanced elastic pull.]{.key-statement}

::: {.publisher-clarification-note .publisher-fold-always title="Mechanical calculation: what holds an angle, and what only slows its change"}

For a small angular range, a teaching approximation treats the eye as a rotating mass with a spring and viscous resistance. Let $\phi$ be angle in radians measured from the position where the passive forces balance. Let $I$ be the rotational inertia, $B>0$ the viscous resistance, $K>0$ the angular stiffness, and $\tau_m(t)$ the net active muscle torque. The angular force balance is

$$
I\ddot\phi+B\dot\phi+K\phi=\tau_m(t).
$$

The terms are torques: $I$ multiplies angular acceleration, $B$ multiplies angular velocity, and $K$ multiplies displacement. This is a guide approximation, not the full model of eye mechanics in Ben-Shushan et al. (2022). Real muscle force is nonlinear and depends on activation and movement history.[^p-eye-mechanics]

At a held angle, $\dot\phi=\ddot\phi=0$, so

$$
\tau_m=K\phi.
$$

The steady angle therefore depends on active torque and stiffness. At fixed torque, doubling $K$ halves the angle in this linear model. Increasing $I$ or $B$ cannot replace the torque required to hold that angle.

If the active torque is removed, neglecting the relatively small inertial term gives

$$
B\dot\phi+K\phi=0,\qquad
\phi(t)=\phi(0)e^{-t/\tau_p},\qquad
\tau_p=\frac{B}{K}.
$$

Greater viscous resistance slows the return; greater stiffness speeds it up at fixed $B$. Neither creates a choice of indefinitely held angles. Actual eye mechanics include several relaxation times, so $\tau_p$ is an effective timescale in this simplified calculation.

:::

**The brain maintains the holding command.** [The [**oculomotor integrator**]{.definition-term custom-style="Definition Term"} converts movement commands into a maintained eye-position signal.]{.definition-explanation} This signal sustains the motor output after a saccade. The name refers to accumulating an eye-velocity command over time into a position signal. In monkeys, Cannon and Robinson (1987) reversibly disrupted brainstem regions involved in this function. Horizontal gaze then drifted back with a time constant of about 0.2 s, compared with more than 20 s before disruption in darkness. The muscles alone did not provide the original persistence.[^p-eye-integrator]

Visual feedback can correct gaze errors, and signals from the inner ear help compensate for head motion. Holding can nevertheless continue in darkness, so immediate visual correction is not the whole mechanism. [**Plasticity**]{.definition-term custom-style="Definition Term"} [is a lasting, experience-dependent change in neural responses or connections.]{.definition-explanation} It can adjust how well the holding circuit is calibrated. Major et al. (2004) altered visual feedback in goldfish and trained their gaze holding toward drift or instability over tens of minutes to hours; normal feedback could reverse the change. That is a change in neural control over a longer timescale, distinct from the immediate elastic and viscous response of the tissues. The experiment did not identify the exact cellular learning rule.[^p-eye-anatomy][^p-eye-plasticity]

The next model isolates the remaining neural question: how can a circuit preserve an activity pattern while losing the angle that pattern was supposed to hold?

## Stable activity with a vulnerable stored value {#sec:FOUNDATIONS-ATTRACTOR}

<!-- vale ai-tells.FigurativeKeeps = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
Imagine a group of neurons maintaining a pattern that represents an eye angle after a movement command has ended. Random spikes disturb that pattern. Recurrent input can correct some disturbances by changing the cells' firing back toward a persistent pattern. But if a disturbance produces the pattern for a different angle, an ideal memory circuit has no record of which angle was originally intended. [Keeping a pattern stable is therefore different from keeping the stored value correct.]{.key-statement}
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.FigurativeKeeps = YES -->

[A circuit's current activities are its [**state**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} A dynamical equation specifies how that state changes. [A [**fixed point**]{.definition-term custom-style="Definition Term"} is a state where the deterministic rate of change is zero.]{.definition-explanation} It is stable in a direction if a small disturbance in that direction decays.

Memory of a continuous quantity calls for a family of persistent states. [A [**continuous attractor**]{.definition-term custom-style="Definition Term"} is a continuous family of fixed points with restoring dynamics toward the family and a neutral direction along it. Neutral means that there is no restoring force along that direction in the ideal deterministic model.]{.definition-explanation} [The family is an [**attractor manifold**]{.definition-term custom-style="Definition Term"}. Its dimension counts independent coordinates represented on it, rather than neurons in the circuit.]{.definition-explanation} A line attractor has one represented coordinate. A ring can represent a periodic coordinate such as heading.[^f-memory]

In the illustrative two-cell model below, the difference between the firing rates represents the angle. Raising both rates equally leaves that difference unchanged. The model's feedback removes the common increase. Raising one rate while lowering the other changes the represented angle. That second change persists. The calculation makes these two responses explicit. It is not a fitted biological circuit.

<div class="publisher-worked-calculation publisher-fold-always">

[**Example: two disturbances to the same stored angle**]{#sec-foundations-attractor-example}

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
Consider a teaching model with two activities $r_1,r_2$ in spikes per second. Let $b=40$ spikes per second and let $k=2$ spikes per second per degree. A stored angle $\theta$ corresponds to
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

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

Increasing $a$ shortens the recovery time $1/a$ for the common activity disturbance. It does not correct the angle error, because $\dot\theta$ is still zero. At fixed rate disturbance, a larger tuning slope $k$ gives a smaller decoded angle change through division by $2k$. Changing $k$ in an actual circuit may also change its dynamics.

At $\theta=5$ degrees, the rates are $(50,30)$. Compare two disturbances from this same state:

- A disturbance of $(+3,+3)$ changes the rates to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$.
- A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response.

[In the second case, the circuit remains coherent while holding the wrong angle.]{.key-statement}

<!-- vale ai-tells.CataphoricForecasting = NO -->
<!-- vale ai-tells.StrawmanContrast = NO -->
The two changes occupy different directions in the activity plane. The solid arrow in the figure is the restoring motion produced by the model. The dashed arrow shows the imposed disturbance along the fixed-point line, rather than a deterministic restoring flow.
<!-- vale ai-tells.StrawmanContrast = YES -->
<!-- vale ai-tells.CataphoricForecasting = YES -->

{{block:fig:FOUNDATIONS-ATTRACTOR}}

In a larger network, the lasting change depends on its connection weights and cannot always be found by an ordinary perpendicular projection. The [network calculation](ch-memory-dynamics.html#sec-memory-linearization) derives the correct projection from the network's linearized dynamics.

</div>

## Independent steps with equal duration and variance give linear variance growth {#sec:FOUNDATIONS-DIFFUSION}

<!-- vale ai-tells.ContrastiveFormulas = NO -->
Each extra or missing spike changes synaptic input. After the circuit has corrected the disturbances it can remove, a small change in the represented angle may remain. Repeating this process makes trials that began at the same angle gradually spread apart. We first model these lasting changes as independent, with no preferred direction and a constant variance per unit time. These are assumptions about the surviving changes, not about complete spike trains.
<!-- vale ai-tells.ContrastiveFormulas = YES -->

::: {.publisher-clarification-note .publisher-fold-always title="Mathematical model: independent steps and Brownian motion"}

Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. The calculation assumes:

- Increments are independent.
- Each increment has mean zero.
- Each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.

After $n$ intervals,

$$
\theta_n-\theta_0=\sum_{j=1}^{n}\xi_j,
\qquad
\operatorname{Var}(\theta_n-\theta_0)
=\sum_{j=1}^{n}\operatorname{Var}(\xi_j)
=2Dn\Delta t.
$$

Writing $t=n\Delta t$ gives linear variance growth $2Dt$. [To describe this limit with a continuous path, use [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$. It starts at zero, has continuous paths and independent Gaussian increments with mean zero, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$.]{.definition-explanation} It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation.

In this continuous diffusion approximation,

$$
\theta(t)=\theta(0)+\sqrt{2D}\,W(t),
\qquad
\mathbb E[(\theta(t)-\theta(0))^2]=2Dt.
$$

:::

[The **diffusion coefficient** $D$ measures half the rate at which the variance of the stored angle grows.]{.definition-explanation} With independent, zero-mean increments of constant variance per unit time,

$$
\operatorname{Var}[\theta(t)-\theta(0)]=2Dt.
$$

<!-- vale ai-tells.FillerIntensifier = NO -->
Here $D$ has units degrees squared per second when $\theta$ is in degrees. More frequent retained disturbances, or larger ones at the same frequency, increase $D$. At a fixed delay, doubling $D$ doubles error variance and multiplies its standard deviation by $\sqrt{2}$. [A single memory trajectory can turn back even while the spread across trials grows.]{.key-statement} The [network calculation](ch-memory-dynamics.html#sec-memory-diffusion) obtains $D$ from the spike variability and the lasting effect of each cell's disturbance.
<!-- vale ai-tells.FillerIntensifier = YES -->

The mean squared displacement, or MSD, is the expected squared change across a lag. In the zero-mean diffusion just defined, MSD is $2Dt$. [A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate.]{.definition-explanation} In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient. A paper that defines its diffusion parameter as the entire two-dimensional MSD slope uses a different convention.

<div class="publisher-worked-calculation publisher-fold-always">

[**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}

<!-- vale ai-tells.NounString = NO -->
Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second. At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes. At 1 s the root mean squared displacement is 0.20 degrees.
<!-- vale ai-tells.NounString = YES -->

If there is also a constant bias velocity $v=0.10$ degrees per second, then

$$
\theta(t)-\theta(0)=vt+\sqrt{2D}\,W(t),
\qquad
\operatorname{MSD}(t)=v^2t^2+2Dt.
$$

The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. A theory of random diffusion must account separately for [**systematic drift**]{.definition-term custom-style="Definition Term"}, a nonzero mean velocity.

Sample paths show the irregular motion. Exact displacement scales show how its spread differs from a fixed bias.

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-DIFFUSION-BIAS}}

</div>

A constant bias grows linearly, so it eventually exceeds the square root growth of the random displacement scale. See [Gaussian displacement density, SI Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7).

</div>

<!-- vale ai-tells.FormalTransitions = NO -->
A later memory state contains earlier accumulated errors as well as new ones. Observing it twice therefore does not give two independent copies of the original memory. The covariance calculation below quantifies the shared history used in the readout chapter.
<!-- vale ai-tells.FormalTransitions = YES -->

::: {.publisher-clarification-note .publisher-fold-always title="Mathematical detail: why two times share accumulated noise"}

Two times along a Brownian path are correlated even though its increments are independent. For $0\leq s\leq t$, write $W(t)=W(s)+[W(t)-W(s)]$. The bracketed increment is independent of $W(s)$ and has mean zero, giving

$$
\operatorname{Cov}(W(s),W(t))
=\operatorname{Var}(W(s))=s,
\qquad
\operatorname{Cov}(W(s),W(t))=\min(s,t).
$$

The same argument gives covariance $2D\min(s,t)$ for a diffusing coordinate started at a fixed value. This identity is the intermediate step needed to compute the error from averaging a memory that moves during readout. It also helps explain why smoothing a diffusive input is different from smoothing a stationary noise source.

:::

<!-- vale ai-tells.FormalTransitions = NO -->
A finite range, a periodic coordinate, external feedback, or a position-dependent diffusion coefficient changes long-time behavior. For example, ordinary squared angular distance on a ring cannot keep growing linearly forever. The basic $2Dt$ result is local or unbounded unless those conditions are treated separately.
<!-- vale ai-tells.FormalTransitions = YES -->

## A fixed spatial map differs from a value that wanders over time {#sec:FOUNDATIONS-RANDOMNESS}

The memory and eye papers study fluctuations that accumulate as time passes. The place-field paper instead starts with a random function of physical position. Once drawn for a cell and an environment, that function is fixed while the animal moves through the map. Revisiting a place evaluates the same expected-rate function, although the actual spikes can still vary from visit to visit.

<!-- vale ai-tells.FormalTransitions = NO -->
These two kinds of randomness can occur together. A circuit may maintain a position estimate with time-dependent noise, while downstream cells respond to position through irregular but repeatable tuning curves. [Observing irregular spatial maps does not tell us how fast the maintained position drifts. Conversely, finding diffusion of a stored value does not determine the shapes of individual place fields.]{.key-statement} The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place]
<!-- vale ai-tells.FormalTransitions = YES -->

<!-- vale ai-tells.CataphoricForecasting = NO -->
The three questions can now be placed beside the kind of variation each paper studies.
<!-- vale ai-tells.CataphoricForecasting = YES -->

<div class="figure-scroll">

{{block:fig:FOUNDATIONS-PAPER-MAP}}

</div>

The rows compare different questions. They do not establish one circuit connecting all three papers.

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-memory]: Burak, Y., and Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). Introduction, Fig. 1, and SI I–III. The two-activity example is a guide construction illustrating the geometry, not the paper's simulated network.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^f-place]: Mainali, N., Azeredo da Silveira, R., and Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [DOI](https://doi.org/10.1016/j.neuron.2025.01.017). Introduction, Results, and STAR Methods. The distinction between map randomness and visit-to-visit spike variation follows from what the model's random function indexes.
<!-- vale ai-tells.EmDashUsage = YES -->

[^p-eye-anatomy]: Dragoi, V. (2026, July 7 review). *Ocular Motor Control*. Neuroscience Online, Section 3, Chapter 8, McGovern Medical School, UTHealth Houston. [Sections 8.2–8.3 and Fig. 8.1](https://nba.uth.tmc.edu/neuroscience/m/s3/chapter08.html). Anatomy, muscle innervation and visual/vestibular control.

[^p-eye-mechanics]: Anderson, S. R., Porrill, J., Sklavos, S., Gandhi, N. J., Sparks, D. L., and Dean, P. (2009). *Dynamics of primate oculomotor plant revealed by effects of abducens microstimulation*. Journal of Neurophysiology, 101(6), 2907–2923. [DOI](https://doi.org/10.1152/jn.91045.2008). Introduction and stimulation/relaxation results. The spring-and-damper calculation is a guide reconstruction of the physical roles, not a fitted reproduction of these experiments.

[^p-eye-integrator]: Cannon, S. C., and Robinson, D. A. (1987). *Loss of the neural integrator of the oculomotor system from brain stem lesions in monkey*. Journal of Neurophysiology, 57(5), 1383–1409. [DOI](https://doi.org/10.1152/jn.1987.57.5.1383). Abstract reports the reversible disruption and gaze-holding time constants.

[^p-eye-plasticity]: Major, G., Baker, R., Aksay, E., Mensh, B., Seung, H. S., and Tank, D. W. (2004). *Plasticity and tuning by visual feedback of the stability of a neural integrator*. Proceedings of the National Academy of Sciences, 101(20), 7739–7744. [DOI](https://doi.org/10.1073/pnas.0401970101). Fig. 1 for movement and holding signals; Figs. 2–4 and Discussion for goldfish training, reversibility and unresolved cellular mechanisms.
