# Memory experiments must separate device error from network dynamics {#ch:HARDWARE-TESTS}

<!-- vale ai-tells.VerbTricolon = NO -->
The earlier stability comparison followed the response to one disturbance. A memory experiment instead repeats a cue and observes what happens as disturbances continue over time. After an angle cue, the estimate may be wrong because the state wandered, because unequal connections pull it toward another angle, or because the observer reads it poorly. One accuracy score combines these causes. This chapter first separates the mean motion from trial-to-trial spread, then relates that spread to circuit noise and finally asks what the output reveals about the state. The protocol and reduced models are proposed tools, not results already demonstrated on every platform in the previous chapter.
<!-- vale ai-tells.VerbTricolon = YES -->

**Draft diagrams:** These unreviewed generated images may contain missing labels, incorrect numbers or misleading relationships. Use the chapter text and sources as the reference.

{{block:fig:DRAFT-MAP-CH18-A}}

{{block:fig:DRAFT-MAP-CH18-B}}

## Repeated cue-and-delay trials separate drift from random spreading {#sec:HARDWARE-TESTS-PROTOCOL}

Begin with a circuit whose joint activity represents an angle. Choose a decoder on separate calibration data, then keep it fixed while testing retention. A [[**decoder**]{.definition-term custom-style="Definition Term"} is a specified rule for estimating the represented quantity from observable circuit signals.]{.definition-explanation} A decoder given every internal state has a different task from a downstream neuron receiving only spikes.

Use the following sequence:

1. Present a brief cue for angle $\theta_0$, then remove it. Test many angles, including values between any suspected preferred positions.
2. Hold the connection weights fixed during each retention trial. Record the actual settings, temperature, update interval, and any imposed noise.
3. Repeat trials at several delays $t$ and decode $\hat\theta(t)$. Use a common reference for angular differences. [[**Unwrapping**]{.definition-term custom-style="Definition Term"} tracks crossings of $0^\circ/360^\circ$ by adding or subtracting full turns to continue the trajectory.]{.definition-explanation} Use it only when sampling is frequent enough to identify crossings reliably.
4. Report mean error and error variance separately as functions of cue and delay. Also report failures in which the activity pattern disappears or changes form.
5. Repeat with changed noise, calibration, or numerical precision, changing one factor at a time. Compare with the same model running in a numerical reference implementation.

Record the decoded state immediately after each cue so that error in writing the value can be separated from error accumulated during retention. Report the number of repeated trials and uncertainty in the estimated drift and diffusion.

[An active circuit has demonstrated useful memory only when its later signals distinguish the earlier cues at the required accuracy.]{.key-statement} High firing rate alone does not establish this. Nor does a small average error if positive and negative errors cancel.

For short intervals, a useful local model is

$$
d\theta=b(\theta)dt+\sqrt{2D(\theta)}\,dW_t.
$$

Here $\theta$ is the represented angle, $b(\theta)$ is its systematic angular motion per unit time, and $D(\theta)$ is half its local variance growth rate. The Brownian increment $dW_t$ has mean zero and variance $dt$; it represents the random disturbance accumulated during the short interval $dt$. Let $\Delta\theta=\theta(t+\Delta t)-\theta(t)$ be the angular change over lag $\Delta t$. With nearly constant coefficients over that short lag, repeated trials near the same angle give $\mathbb E[\Delta\theta]\simeq b\Delta t$ and $\operatorname{Var}(\Delta\theta)\simeq2D\Delta t$. Correlated perturbations, preferred states, or boundaries can invalidate that short-lag fit. At long delays, report the distribution of angular errors around the circle. Values separated by a full turn represent the same angle, so a local unwrapped variance cannot be extended indefinitely as a measure of angular error.

The [[**mean squared displacement**]{.definition-term custom-style="Definition Term"}, or MSD, is the mean of the squared changes $\mathbb E[(\Delta\theta)^2]$ over the chosen lag.]{.definition-explanation} It equals $\operatorname{Var}(\Delta\theta)+\mathbb E[\Delta\theta]^2$. Thus a growing MSD can include systematic motion as well as random spreading. Compare the mean displacement and its variance before interpreting an MSD slope as diffusion. The [eye-drift measurements](ch-eye-timing.html#sec-eye-measurement-noise) likewise require an explicit displacement convention and an estimate of measurement error.

Estimate readout noise before interpreting short-lag variance as motion of the stored value. Independent errors with constant variance in two position readings add a constant offset to the measured displacement variance.

The measurement path can also smooth or delay a signal, and noise can enter at different points along that path. For example, a circuit's output filter smooths a changing voltage; a camera or actuator can introduce further delays. The [eye study](ch-eye-timing.html) asks a related question about neural commands filtered by eye mechanics. Measure or model the filter and the observation noise separately before assigning the observed time scale to the memory state. The electronic analogy does not establish the biological mechanism.

::: {.publisher-clarification-note .publisher-fold-always title="Measurement check: readout noise can look like state motion"}

Suppose each position estimate contains independent, zero-mean measurement error with variance $\sigma_m^2$. The difference of two estimates then adds $2\sigma_m^2$ to displacement variance, even when the circuit does not move. For independent constant-$D$ state motion, the measured short-lag displacement variance is $2D\Delta t+2\sigma_m^2$. A nonzero intercept can reveal this contribution. Correlated readout errors, overlapping observation windows, or a state that changes during the readout require a fuller model. This is the same type of separation needed when interpreting the eye-drift measurements.

:::

## Physical parameters act through decay, bias, and noise projection {#sec:HARDWARE-TESTS-PARAMETERS}

A changed component affects memory through the circuit's equations. Increasing a leak current can shorten a component time constant. Changing a recurrent weight can alter restoration or introduce a preferred angle. A fluctuating current can perturb many neurons, yet only part of the resulting activity change remains as a change of the remembered angle.

The [projection derived in Part I](ch-memory-dynamics.html#sec-memory-linearization) makes the last statement precise under a specific model. Let the vector $\mathbf r$ contain the network's activity variables, with local dynamics $d\mathbf r=\mathbf f(\mathbf r)dt+B\,d\mathbf W_t$. Here $\mathbf f(\mathbf r)$ is the deterministic rate of change of the activity, $d\mathbf W_t$ collects independent Brownian increments with covariance $I\,dt$, and the matrix $B$ maps those increments into the activity variables. Assume a smooth family $\mathbf r_*(\theta)$ of steady states with one neutral memory direction and locally decaying directions, and disturbances small enough for a leading-order approximation. Let $\boldsymbol\ell$ be the left neutral vector, the object called $\mathbf v$ in Part I, normalized so that $\boldsymbol\ell^T d\mathbf r_*/d\theta=1$. It converts an activity disturbance into its surviving angular displacement. Evaluating $B$ and $\boldsymbol\ell$ at that state, the leading local approximation gives

$$
D(\theta)=\tfrac12\boldsymbol\ell^TBB^T\boldsymbol\ell.
$$

[Noise matters through both its size and the directions in which it pushes the circuit.]{.key-statement} Large disturbances in rapidly corrected directions can matter less than small disturbances along the memory direction. In a general network the left neutral vector differs from the visible tangent to the family. Using the tangent alone can predict the wrong change in the remembered angle caused by a given activity disturbance. Curvature and state-dependent noise can also contribute drift beyond this local approximation.

Here $B$ represents fluctuations that vary across time and trials, including noise deliberately added to a digital update or measured fluctuations in an analog circuit. A fixed device mismatch instead changes the deterministic dynamics $\mathbf f$ and can create repeatable bias or preferred angles. It can also change which disturbances affect the remembered value by changing the return flow and noise sensitivity. If mismatch removes the family of steady states, the neutral-vector formula above is no longer directly applicable; any reduced description must be justified for the changed circuit. A configured deterministic neural rule has no stochastic term unless one is supplied; that statement does not make the physical digital chip free of timing variation or hardware errors.

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: project circuit fluctuations onto the remembered angle"}

Write $\delta\theta\simeq\boldsymbol\ell^T\delta\mathbf r$ in the local linear regime. For the neutral mode, $\boldsymbol\ell^T$ times the linearized deterministic drift is zero. The stochastic increment is $d\theta\simeq\boldsymbol\ell^TB\,d\mathbf W_t$. Since $\operatorname{Cov}(d\mathbf W_t)=I\,dt$, its variance is $\boldsymbol\ell^TBB^T\boldsymbol\ell\,dt$. Equating this to $2D\,dt$ gives the displayed coefficient. The normalization ensures that the result measures angular displacement rather than an arbitrarily scaled activity coordinate. This calculation transfers only after the hardware's local dynamics and noise assumptions have been checked.

:::

The following changes suggest tests under the model assumptions above. In the table, $B$ maps Brownian noise into the circuit activities, $BB^T$ describes its covariance per unit time, and $\mathbf f$ is the deterministic rate of change of those activities.

<div class="table-responsive">

{{block:tbl:HARDWARE-TEST-PARAMETERS}}

</div>

<div class="publisher-worked-calculation publisher-fold-always">

**Example: a tighter distribution can hide a biased memory.**

Consider two illustrative circuits after a one-second delay. Circuit A has zero mean angular error and variance $4$ deg$^2$. Circuit B has mean error $3^\circ$ and variance $1$ deg$^2$, because it is attracted toward a preferred angle. Their mean squared errors are $4$ and $1+3^2=10$ deg$^2$. Circuit B has less random spread but worse cue retention. Reporting only its smaller variance would hide the effect of pinning.

</div>

## Matching time and readout is necessary to compare memory accuracy {#sec:HARDWARE-TESTS-COMPARISON}

The source papers supply different constraints on this hardware experiment.

- **Burak and Fiete (2012):** compare diffusion with the information available in spikes under matched noise, dynamics, and observation assumptions. A processor that stores an exact internal angle and exposes it directly to the decoder has changed the readout problem.
- **Ben-Shushan and colleagues (2022):** a measured output can filter the internal command. Camera exposure, output smoothing, or a mechanical actuator can change the observed motion. Calibrate that path before assigning an output time scale to the memory circuit itself.
<!-- vale ai-tells.ParallelStaccato = NO -->
- **Mainali and colleagues (2025):** patterns of firing across physical positions constrain a spatial representation. Reproducing field-size statistics does not by itself show that a network implemented in hardware retains position without input. Spatial structure and temporal persistence need separate tests.
<!-- vale ai-tells.ParallelStaccato = YES -->

These links concern the tested mechanisms, not a claim that a chip reproduces the animal systems. The [synthesis chapter](ch-synthesis.html#sec-synthesis-evidence) sets out the evidence supplied by the original papers.

To compare readout with [Part I's Fisher information](ch-memory-information.html#sec-memory-fi), first specify the signal and observation duration. Fisher information measures how the distributions of those signals change with nearby values of the **current** state. An observer estimating the **initial cue** after a delay faces an additional uncertainty: the represented value may have moved since the cue. A precise estimate of the current bump does not by itself recover the earlier angle. For the neural model of Burak and Fiete, $D\ge 1/(2\tau^2J)$, where $D$ is the diffusion coefficient, $J$ is the internal spike information rate, and $\tau$ is the synaptic time constant. An electronic circuit needs matched noise and dynamics before the same bound can be tested.

Time conversion is especially important for accelerated hardware. If model time $t_m=a t_p$, where $t_p$ is physical time and $a>1$ is the acceleration factor, let $\Delta\theta$ be the angle change and $D_m$ the diffusion coefficient per unit of model time. The diffusion law $\operatorname{Var}(\Delta\theta)=2D_m t_m$ becomes $2(aD_m)t_p$. The physical-time coefficient is $D_p=aD_m$, measured per physical second. This is a change of units for the same ideal trajectory. Physical communication delay, temperature drift, or limited readout speed can prevent a real device from obeying that ideal rescaling.

For an energy comparison, specify the cue distribution, delay, permitted decoding error, and failed-trial rate. Measure energy over writing, waiting, and reading, including required host processing and interfaces. Then report how error and energy change as delay increases. An operations-per-second or operations-per-watt figure alone cannot establish the cost of retaining a useful value.

The resulting research question is concrete: **which part of the physical implementation limits the accuracy of a remembered quantity, and does changing that part improve retention under the same task and readout?** That question turns von Neumann's comparison into a test of contemporary neural and electronic memory mechanisms.
