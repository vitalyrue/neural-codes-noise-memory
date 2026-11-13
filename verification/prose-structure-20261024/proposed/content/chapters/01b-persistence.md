# Stable representations can accumulate error {#ch:PERSISTENCE}

The next distinction is between a value and the activity that represents it. Eye position is one number, but a circuit can represent it through thousands of neural activities. A disturbance can change those activities without changing the represented value. Another disturbance can leave a coherent activity pattern while changing the value. The geometry of these two changes will explain why a stable-looking circuit can still accumulate memory error.[^f-memory]

We first build a small example in which some disturbances fade while others leave a different stored angle. We then ask what happens when small lasting changes arrive repeatedly, deriving how their spread grows with time and how a fixed bias changes that prediction. The final distinction is between this changing value and an irregular spatial map that stays fixed. It explains why the memory, eye-motion, and place-field papers need different models even though all three concern variable neural signals.

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

At $\theta=5$ degrees, the rates are $(50,30)$. Compare two disturbances from this same state:

- A disturbance of $(+3,+3)$ changes the rates to $(53,33)$. It creates $x=3$ but leaves the represented angle at 5 degrees. The restoring dynamics return to $(50,30)$.
- A disturbance of $(+3,-3)$ gives $(53,27)$, with $x=0$ and angle $26/(2\times2)=6.5$ degrees. This state lies on the fixed-point line, so there is no restoring response.

In the second case, the circuit remains coherent while holding the wrong angle.

The two changes occupy different directions in the activity plane. The solid arrow in the figure is the restoring motion produced by the model. The dashed arrow shows the imposed disturbance along the fixed-point line, rather than a deterministic restoring flow.

{{block:fig:FOUNDATIONS-ATTRACTOR}}

This construction illustrates the geometry; it is not a fit to eye-neuron recordings. In a larger network, the direction that survives depends on its connection weights and cannot always be found by an ordinary perpendicular projection. The [network calculation](ch-memory-dynamics.html#sec-memory-linearization) derives the correct projection from the network's linearized dynamics.

## Independent steps with equal duration and variance give linear variance growth {#sec:FOUNDATIONS-DIFFUSION}

If persistent angular changes arrive repeatedly, their errors accumulate. Divide time into intervals of length $\Delta t$. Let $\xi_j$ be the change in the represented coordinate during interval $j$. The calculation assumes:

- increments are independent;
- each increment has mean zero;
- each increment has variance $2D\Delta t$, where $D$ has units coordinate squared per time.

After $n$ intervals,

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

The [**Brownian motion**]{.definition-term custom-style="Definition Term"} $W(t)$ starts at zero, has independent Gaussian increments, and satisfies $\operatorname{Var}[W(t)-W(s)]=t-s$ for $t\geq s$. It describes the limit of many small, suitably independent fluctuations. A physical network need only approach this description over the time and noise scales relevant to the calculation. The parameter $D$ is its diffusion coefficient. It measures the rate of variance growth; a single trajectory need not move monotonically away from its starting value.

The mean squared displacement, or MSD, is the expected squared change across a lag. In the zero-mean diffusion just defined, MSD is $2Dt$. A [**root mean squared displacement**]{.definition-term custom-style="Definition Term"} is its square root, $\sqrt{2Dt}$, and has the same units as the represented coordinate. In several dimensions, adding independent coordinate contributions gives an overall MSD of $2dDt$ only when each of the $d$ coordinates has the same diffusion coefficient. A paper that defines its diffusion parameter as the entire two-dimensional MSD slope uses a different convention.

[**Example: why the noise grows slower than a fixed bias**]{#sec-foundations-diffusion-example}

Take an illustrative angular diffusion coefficient $D=0.02$ degrees squared per second. At 0.35 s its variance is $0.014$ degrees squared and its root mean squared displacement is 0.118 degrees, or about 7.10 arcminutes. At 1 s the root mean squared displacement is 0.20 degrees. These are teaching values, not a new estimate from either monkey.

If there is also a constant bias velocity $v=0.10$ degrees per second, then

$$
\theta(t)-\theta(0)=vt+\sqrt{2D}\,W(t),
\qquad
\operatorname{MSD}(t)=v^2t^2+2Dt.
$$

The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. A theory of random diffusion must therefore account for systematic drift separately.

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

[^f-place]: Mainali, N., Azeredo da Silveira, R., and Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [https://doi.org/10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017). Introduction, Results, and STAR Methods. The distinction between map randomness and visit-to-visit spike variation follows from what the model's random function indexes.
