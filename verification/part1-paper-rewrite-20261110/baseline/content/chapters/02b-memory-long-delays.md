<!-- vale ai-tells.NounString = NO -->
# Boundaries and drift change memory error over long delays {#ch:MEMORY-LONG-DELAYS}
<!-- vale ai-tells.NounString = YES -->

<!-- vale ai-tells.VerbTricolon = NO -->
[A rate of random spreading measured near one stored value does not yet tell us how memory error behaves after a long wait.]{.key-statement} The value may approach a boundary, wrap around an angular range, or reach a region where the spreading rate differs. A consistent movement of the average value would also change the error without being captured by the rate of random spreading alone.
<!-- vale ai-tells.VerbTricolon = YES -->

We begin by following the distribution of stored values across repeated trials, using the local diffusion coefficient derived in the preceding chapter. This shows why errors can keep growing on a line but level off when angular error is measured within one turn. We then separate random spreading from systematic drift and make the noise assumptions explicit. Finally, the paper's figures show what its network simulations test and distinguish movement of the memory from uncertainty when another circuit reads it. That second uncertainty motivates the information calculation that follows.

Here $\theta$ is the current stored value and $\Theta$ its common initial value across trials. The local diffusion coefficient $D(\theta)$ comes from the weak spike fluctuations derived in the [preceding chapter](ch-memory-dynamics.html#sec-memory-diffusion), after stable disturbances have relaxed. For constant $D$, displacement variance is $2Dt$ before boundaries matter and when there is no systematic drift.

## Long delay errors depend on boundaries and local diffusion {#sec:MEMORY-LONG-TIME}

**Paper location:** [Supporting text, section III, PDF p. 7, Eqs. S28–S31](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7), continues to [pp. 8–9, Eqs. S32–S41](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8). The folded density-equation derivation and the uniform-limit calculation are expanded in the guide.

**Neural mechanism.** Spike fluctuations keep shifting the stored value after the cue has ended. The local diffusion coefficient describes the variance of those shifts after stable disturbances have relaxed. It does not by itself say that variance grows at the same rate forever: boundaries and variation of $D$ can change the long time behavior. We first keep $D$ constant, so the line and circle differ only in how the memory coordinate is bounded.

**Mathematical derivation.** Let $p(\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\Theta$. [The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment.]{.definition-explanation} A density equation tracks how small random increments redistribute probability. The calculation below first obtains that equation for a general state-dependent $D$. Constant $D$ then gives the line and circle solutions.

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: from random increments to the memory density equation"}

To pass from random increments to a density equation, choose any smooth function $F(\theta)$. In a short interval $dt$, the zero-drift Itô increment has conditional mean zero and conditional second moment $2D(\theta)dt$. Taylor expansion at the starting coordinate gives

$$
\begin{aligned}
\mathbb E[F(\theta+d\theta)-F(\theta)\mid\theta]
&=F'(\theta)\mathbb E[d\theta\mid\theta]
+\tfrac12F''(\theta)\mathbb E[(d\theta)^2\mid\theta]+o(dt)\\
&=D(\theta)F''(\theta)dt+o(dt).
\end{aligned}
$$

The higher-order terms vanish faster than $dt$ in this diffusion approximation. Averaging over the starting-coordinate density and dividing by $dt$ gives

$$
\frac{d}{dt}\int F(\theta)p(\theta,t)\,d\theta
=\int F''(\theta)D(\theta)p(\theta,t)\,d\theta.
$$

Take $F$ to vanish outside an interior region, or use boundaries for which the integration terms vanish. Integrating by parts twice moves both derivatives from $F$ onto the product $Dp$. Because the resulting identity holds for every such smooth $F$, it gives the density equation below.

:::

[In the zero-drift diffusion approximation, this density evolves according to the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:]{.definition-explanation}

$$
\frac{\partial p}{\partial t}
=\frac{\partial^2}{\partial\theta^2}[D(\theta)p],
\qquad p(\theta,0)=\delta(\theta-\Theta).
$$

Here the Dirac delta denotes a point mass: initially all probability is at $\Theta$. It differs from the earlier zero-or-one symbol $\delta_{ij}$. For constant $D$ on an unbounded line, the Gaussian solution is

$$
p(\theta,t)=\frac{1}{\sqrt{4\pi Dt}}
\exp\left[-\frac{(\theta-\Theta)^2}{4Dt}\right].
$$

Its variance is $2Dt$. For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle. This wrapped sum appears in [SI Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483). At long times the density approaches $1/(2\pi)$. If angular errors are reported in $[-\pi,\pi)$, their limiting mean squared value is

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}x^2dx=\frac{\pi^2}{3}.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
**Interpretation.** [The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.]{.key-statement}[^p1-fp]
<!-- vale ai-tells.FormalTransitions = YES -->

For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay.

<div class="figure-scroll">

{{block:fig:MEMORY-LINE-RING}}

</div>

As the wrapped density approaches uniform, its mean squared error approaches $\pi^2/3$. The unbounded line error keeps growing.

**Paper location:** [Supporting text, section III, PDF pp. 8–9, Eqs. S33–S41](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8), and [Fig. S1, PDF p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10). The guide shows the intermediate moment calculation and identifies an apparent factor discrepancy in the printed formulas.

**Neural mechanism.** The rate of random spreading can change as the stored value changes, because the current firing rates set the spike variability. The supplement illustrates this dependence with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule. The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$. Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$.

<!-- vale ai-tells.ContrastiveFormulas = NO -->
<!-- vale ai-tells.FigurativeFires = NO -->
<!-- vale ai-tells.FigurativeStays = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
Here $\theta$ is an activation coordinate, not an angle, and both steady rates are positive only when $\theta>|b_0|/2$. When both activations rise together, each cell raises the other's firing enough to replace the extra synaptic decay. This common increase persists and changes the stored value. A disturbance in their difference instead decays toward the difference set by the biases. Larger $\theta$ raises both firing rates and hence both Poisson count variances. Because the projection weights stay fixed in this example, more of that variability remains as memory error.
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.FigurativeStays = YES -->
<!-- vale ai-tells.FigurativeFires = YES -->
<!-- vale ai-tells.ContrastiveFormulas = YES -->

**Mathematical derivation.** When $D$ varies with state, the zero drift stochastic equation is $d\theta=\sqrt{2D(\theta)}\,dB$ with the Itô convention. Under conditions that remove boundary terms, the density equation gives

$$
\frac{d}{dt}E[\theta]=0,
\qquad
\frac{d}{dt}\operatorname{Var}(\theta)=2E[D(\theta)].
$$

<!-- vale ai-tells.ConsequenceParticiple = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
To obtain these identities, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice. The second derivatives of these functions are respectively zero and two, giving the two identities. A similar calculation for the smooth function $D$ gives $dE[D]/dt=E[DD'']$. Expanding at $t=0$ therefore yields
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.ConsequenceParticiple = YES -->

$$
\operatorname{Var}(\theta)
=2D(\Theta)t+D(\Theta)D''(\Theta)t^2+O(t^3).
$$

This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602).[^p1-variable] For the mutual excitation network, substituting $v_1=v_2=1/2$ into the diffusion formula gives

$$
2D=\frac{1}{4}(\bar r_1+\bar r_2)=\frac{\theta}{2\tau},
\qquad D=\frac{\theta}{4\tau}.
$$

**Interpretation.** A state dependent $D$ need not produce a nonlinear increase of variance with time. If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain. The implied variance for this network is $\Theta t/(2\tau)$, agreeing with [SI Eq. S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig. S1, p. 10](ch-memory-long-delays.html#fig-paper-memory-s1). SI Eq. S40 instead prints $D=\theta/(2\tau)$. Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41.[^p1-excitation]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Burak and Fiete (2012), Figure S1</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-MEMORY-S1}}

</div>
</details>

## A diffusion calculation does not determine systematic drift {#sec:MEMORY-DRIFT-SCOPE}

**Paper location:** [Supporting text, section II, “Systematic drift,” PDF pp. 4–5, Eqs. S19–S20](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4). The explicit convention conversion below is a guide derivation.

**Neural mechanism.** [Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction.]{.key-statement} Both can occur, and the derivation of $D$ alone does not settle the second question.

<!-- vale ai-tells.ConsequenceParticiple = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
[The paper assumes that the network is tuned to eliminate systematic drift, meaning a nonzero mean velocity along the attractor.]{.definition-explanation} A deterministic mismatch in weights can create such a velocity. In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor. The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic]
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.ConsequenceParticiple = YES -->

**Mathematical derivation.** For state dependent $D$, where the coefficient is evaluated affects the process. [The [**Stratonovich convention**]{.definition-term custom-style="Definition Term"} uses midpoint evaluation in its limiting increments.]{.definition-explanation} With the same written coefficient and zero written drift, it describes a different process from the Itô equation. If noise is stronger at larger values, a positive step samples stronger noise at its midpoint and a negative step samples weaker noise. Their average no longer cancels. Converting to Itô form expresses this effect as a drift $D'/2$. The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network.

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: midpoint evaluation adds a mean displacement"}

Write $b(\theta)=\sqrt{2D(\theta)}$ in a region where $D$ is positive and smooth. A Stratonovich step uses $\Delta\theta=b(\theta+\Delta\theta/2)\Delta W$. Expand about the starting value and use $\Delta\theta\simeq b\Delta W$ in the correction:

$$
\Delta\theta\simeq b\Delta W+\frac{b'}2\Delta\theta\Delta W
\simeq b\Delta W+\frac{bb'}2(\Delta W)^2.
$$

Since $E[\Delta W]=0$ and $E[(\Delta W)^2]=\Delta t$, the added mean step is $bb'\Delta t/2$. Differentiating $b^2=2D$ gives $bb'=D'$, so the mean velocity is $D'/2$. The squared-increment term contributes to the limit as the time steps shrink. If $D$ is constant, the correction vanishes. This expansion explains the convention change. It does not determine which convention a microscopic neural process produces.

:::

With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$. 

**Interpretation.** The variance calculation captures the leading random term. [Small changes to weights or biases might cancel the mean drift. They cannot remove the random increments by subtracting a known average.]{.key-statement} A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions.

**Paper location:** [Main article, Discussion, PDF p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5). The covariance projection below is a guide extension; the article presents a general correlated-noise inequality as a conjecture.

The independence assumption also has a precise scope. Newly generated spike-count fluctuations are conditionally independent given the present state. Shared recurrent fluctuations can still correlate the observed spike trains over time. An extra source of correlated fluctuations would change the projection formula to $2D=\mathbf v^TQ\mathbf v$, where $Q\,dt$ is their increment covariance. A matching calculation of information would need the probabilities of joint spike patterns. The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142)). It does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]

## Figures distinguish memory motion from readout error and test diffusion {#sec:MEMORY-FIGURES}

**Paper location:** [Main article, Fig. 1, PDF p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2), and [Fig. 2, PDF p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3). Simulation details are in [Materials and Methods, PDF p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6).

**Neural mechanism in the figures.** [Figure 1A, p. 2](ch-memory-long-delays.html#fig-paper-memory-1) illustrates the [coordinate assigned by the return flow in Chapter 3](ch-memory-dynamics.html). The green state returns to the black attractor point under noise free dynamics. Comparing the endpoints before and after one noisy interval isolates the retained memory change. The [tilted two variable example](ch-memory-dynamics.html#sec-memory-linearization) shows why the return path matters.

<!-- vale Google.Units = NO -->
In Fig. 1B, an activity bump is a localized peak of population firing rates across the neurons' preferred angles. The figure separates two sources of error:
<!-- vale Google.Units = YES -->

- During storage, the bump's location has moved away from its initial value $\Theta$.
- At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes.

The [information calculation](ch-memory-information.html#sec-memory-fi) measures this second uncertainty and relates it to diffusion. The [readout chapter](ch-memory-readout.html) then follows observation of the moving state.[^p1-fig1]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Burak and Fiete (2012), Figure 1</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-MEMORY-1}}

</div>
</details>

[Figure 2, p. 3](ch-memory-long-delays.html#fig-paper-memory-2) tests the diffusion calculation in two different network designs. Panel A shows a ring with weights determined by differences of preferred angles. This gives rotational symmetry: rotating the activity pattern around the ring leaves its dynamics unchanged in form.

Panel B shows the exponential-transfer simulation with 1,024 neurons. Its inset compares activity patterns 10 seconds apart. The horizontal axis orders neurons around the ring; the solid curves show their firing rates, with peaks near 85 Hz. Vertical marks show the spikes emitted in a 10 ms window at each snapshot. The peak moves between snapshots. The main trace follows the represented angle through time, rather than overall activity amplitude. [The pattern can persist while its position, and therefore the remembered value, changes.]{.key-statement}

**Interpretation of the simulation tests.** Panels C and D test different parts of the prediction:

  <!-- vale ai-tells.ContrastiveFormulas = NO -->
- Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions, shown in its inset. Circles are simulation measurements; solid lines are the diffusion prediction from Eq. 2. The dashed [information bound](../frontmatter/ch-mathematical-tools.html#sec-math-tools-bound) is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agreeing with the derived diffusion formula. Error bars in C and D show [the [**standard error of the mean (SEM)**]{.definition-term custom-style="Definition Term"}: uncertainty in the mean MSD estimated from 100 trials, rather than the spread of individual trial values.]{.definition-explanation} In C they are smaller than the symbols.
  <!-- vale ai-tells.ContrastiveFormulas = YES -->
- Panel D follows angular error to longer intervals. Its theoretical curve inserts the predicted diffusion coefficient into the wrapped-angle mean squared error formula, SI Eq. S32. It therefore includes the effect of periodic boundaries rather than extending the short-lag straight line indefinitely. Its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.

<!-- vale ai-tells.CataphoricForecasting = NO -->
Panel E replaces the ring with two mutually inhibiting units, which can also represent two neural populations. Equal opposing weights and a linear firing rule support a continuous range of rate differences. That difference represents a nonperiodic stored value, rather than an angle that wraps around.

In F the two rates vary in opposite directions. The vertical axis uses $\mathrm{ms}^{-1}$: one spike per millisecond is 1,000 spikes per second. The large plotted rates can describe the summed activity of each population. They should not be read as ordinary rates of two individual biological neurons.

Panel G asks how far their rate difference changes over a lag. For each lag, the authors square that change and average over starting times in the 200-second simulation. Its vertical axis therefore has units $(\mathrm{ms}^{-1})^2$, while its horizontal axis is lag in seconds. Circles are those measurements; the solid line is the diffusion prediction from Eq. 2. The [simulation chapter](ch-simulating-memory.html#sec-simulating-memory-controls) writes out the measured quantity and its unit conversion. This second design matters because the projection argument does not require rotational symmetry. These are simulations checking the model calculation. They are not direct measurements of memory noise in an animal.[^p1-fig2]
<!-- vale ai-tells.CataphoricForecasting = YES -->

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Burak and Fiete (2012), Figure 2</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-MEMORY-2}}

</div>
</details>

The derivation has now supplied a dynamical quantity, $D$, from spike variability and the way a network returns to its attractor. We next derive a statistical quantity from the same tuning curves and ask why it puts a lower limit on $D$.

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-fp]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [density equation, Eqs. S28–S29, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,48); [Gaussian on a line, Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,329); [wrapped density and uniform limit, Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483); [angular error, Eq. S32, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109). The uniform angular variance calculation is a teaching reconstruction.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-variable]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, [Supporting Text, Eqs. S33–S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,139). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-excitation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, [Supporting Text, Eqs. S38–S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,48); [Fig. S1, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10&zoom=125,0,45). [DOI](https://doi.org/10.1073/pnas.1117386109). The factor discrepancy between S40, S41, and the projection calculation is visible in the supplied PDF. No author correction is asserted.
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-systematic]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [“Systematic drift,” p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362); [Eqs. S19–S20 and continuation, p. 5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale Microsoft.Quotes = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-correlation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142). [DOI](https://doi.org/10.1073/pnas.1117386109). The covariance projection is an immediate linear algebra extension. The paper's proposed general correlated noise inequality remains a conjecture there.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale Microsoft.Quotes = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-fig1]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 1 and caption, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439); [flow definition, “In what follows,” p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,191). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-fig2]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 2 and caption, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,18); Network Simulations: [ring model, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,103) and [mutual inhibition, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->
