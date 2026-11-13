# Spatial maps and memory dynamics need separate tests {#ch:SYNTHESIS}

A model can explain the shape of a neural code without explaining how that code is maintained. It can also explain fluctuations inside a circuit without uniquely locating the source of a measured behavior. The three papers become more useful together when these different claims are kept attached to their actual mathematical and experimental tests.

To connect them, we first separate the spatial map, the changing represented position, and the movement measured downstream. A short calculation then shows how a common position error can make cells with different tuning change together. Comparing that calculation with each paper's evidence and related studies identifies what a joint experiment would still need to measure.

## The three papers constrain maps, dynamics, and movement {#sec:SYNTHESIS-QUESTIONS}

For a circuit representing position, three questions arise. What activity pattern corresponds to each position? How does the represented position evolve when there is no corrective input? How does a downstream physical system transform that changing signal into an observable movement? The place-field model addresses the first question. The persistent-activity model addresses the second. The eye-drift model combines a candidate answer to the second with a detailed answer to the third.[^s-three]

The objects differ even when the word position appears in all three. In 2012, $\theta(t)$ locates a network state on its attractor. In 2022, the internal eye-position command and actual eye angle are separate quantities linked through motor neurons and mechanics. In 2025, $x$ locates an animal in an environment, and $h_i(x)$ is a spatial input function assigned to a cell. The Gaussian process does not update a remembered $x$ through time.

The [guide map](ch-persistence.html#fig-foundations-paper-map) gives a visual comparison of these three questions.

<div class="table-responsive">

{{block:tbl:SYNTHESIS-MODELS}}

</div>

The 2012 and 2022 connection is direct: neural noise can move a maintained eye-position command, which then drives muscles. The 2022 result provides evidence for a substantial shared source before the final motor neurons and shows that integrator diffusion is sufficient within the constructed model. It does not measure the circuit's Fisher information or test equality in the 2012 bound. The 2025 connection is broader: an internally coherent position estimate can be expressed through spatially irregular tuning curves.

## How a static map can carry a moving estimate {#sec:SYNTHESIS-JOINT-CALCULATION}

Suppose a network maintains a one-dimensional estimate $x(t)$ and cell $i$ has a fixed expected-rate function $f_i(x)$. Its time-dependent expected rate is

$$
R_i(t)=f_i(x(t)).
$$

Here $f_i$ describes spatial tuning and $x(t)$ describes dynamics. A source of time variation has entered even though $f_i$ is fixed. Actual spike counts add another layer of variability around the expected rate. This construction is a guide calculation connecting the papers' objects, not a model tested jointly by the three studies.

Consider a short interval of duration $t$ starting at $x_0$. Assume that the estimate's local displacement $\delta x=x(t)-x_0$ has mean zero and variance $2Dt$, and that it is small enough to linearize each rate curve. Taylor expansion gives

$$
f_i(x_0+\delta x)
=f_i(x_0)+f_i'(x_0)\delta x+O((\delta x)^2).
$$

To leading order, the change is $\delta R_i=f_i'(x_0)\delta x$. Multiplying the centered changes for neurons $i$ and $j$ and averaging yields

$$
\operatorname{Cov}(\delta R_i,\delta R_j)
\simeq f_i'(x_0)f_j'(x_0)\operatorname{Var}(\delta x)
=2Dt\,f_i'(x_0)f_j'(x_0).
$$

This covariance concerns expected-rate changes caused by the common represented displacement, conditional on the starting position. It is not a formula for every covariance in a spiking recurrent network. It neglects higher-order changes in tuning and additional private or shared fluctuations. Near a threshold or over a large spatial displacement, the linear approximation must be revisited.

### Example: opposite rate changes from the same position error {#sec:SYNTHESIS-COVARIANCE-EXAMPLE}

Let the local slopes of two rate curves be $f_1'=2$ Hz/m and $f_2'=-1$ Hz/m. Suppose $D=0.01$ m²/s and the interval is 0.5 s. Then the variance of the common position displacement is $2Dt=0.01$ m². The contributions to rate variance and covariance are

$$
\operatorname{Var}(\delta R_1)=2^2(0.01)=0.04\ \mathrm{Hz}^2,
$$

$$
\operatorname{Var}(\delta R_2)=(-1)^2(0.01)=0.01\ \mathrm{Hz}^2,
\qquad
\operatorname{Cov}(\delta R_1,\delta R_2)=(2)(-1)(0.01)
=-0.02\ \mathrm{Hz}^2.
$$

With only this one source, the two rate changes have correlation $-1$: one rises whenever the other falls. Adding independent private noise lowers the magnitude. The negative covariance here comes from opposite tuning slopes under a common position change. It does not establish an inhibitory connection between the cells.

For the same slopes, set both expected rates to 10 Hz at the starting position. The upper plot shows the fixed rate curves; the lower plot shows their changes under a common position displacement.

<div class="figure-scroll">

{{block:fig:SYNTHESIS-SHARED-POSITION}}

</div>

Both changes are set by the same position displacement, so they occupy one direction in the two-rate plane. Independent private fluctuations would spread them away from that line.

This example explains why irregular or mixed single-cell responses can coexist with a low-dimensional population fluctuation. It also shows the extra evidence required to connect a spatial map to a dynamical mechanism: one must measure how population changes align with the directions implied by those maps, rather than infer dynamics from field shapes alone.

## Each model needs a test matched to its claim {#sec:SYNTHESIS-EVIDENCE}

A model that matches one distribution may have enough adjustable parameters to do so for several different reasons. The place-field paper gains support by fitting arrangement parameters and then comparing additional features, including slices and shape statistics. The separate firing-rate multiplier used in some comparisons should remain visible when counting how many quantities were predicted without further fitting. A successful high-threshold formula is also a statement about its limiting assumptions; finite-threshold simulations and the original recordings provide different kinds of checks.

The eye paper uses a different strategy. It calibrates a movement-to-firing relationship, inverts it, and compares the resulting single-neuron displacement predictions with measured displacement. Shared covariance then carries information that independent private fluctuations cannot supply under the decomposition's assumptions. The additional MSD comparison tests the time structure: increasing stationary motor-noise amplitude cannot by itself reproduce the accumulating upstream signal. Calibration validity, source correlations, two animals, and horizontal movement remain part of the result's scope.

The 2012 inequality is a mathematical constraint rather than an experimental fit. Its derivation specifies what noise and dynamics it covers. An experimental comparison would need estimates of diffusion, the relevant time constants, and the appropriate instantaneous information rate, all under compatible conditions. Agreement with $1/N$ scaling alone would not test the entire inequality, since several mechanisms can share that scaling.

## Related studies change assumptions and leave circuit choices open {#sec:SYNTHESIS-RELATED}

The foundational eye-position account is Seung's line-attractor model. Aksay and colleagues then used recordings and perturbations in goldfish to constrain integrator circuitry. These establish the dynamical problem and experimental architecture behind the 2022 model. Neither supplies the macaque displacement-variance estimate. Burak and Fiete's earlier grid-cell study puts a related integrator problem in navigation: recurrent population activity is driven by velocity and accumulates path-integration errors. Its accuracy ranges belong to the simulated networks and parameter choices, rather than all biological grid circuits.[^s-attractors]

Noise-driven storage also connects to memory capacity. Koyluoglu and colleagues ask how noise limits recall as the delay and number of stored items increase. Their comparison with human data shows why direct storage of several independent values need not capture observed behavior; transformations before and after storage alter the performance prediction. Seeholzer and colleagues examine how short-term changes in synaptic strength affect diffusion and systematic drift. These papers change the storage assumptions rather than invalidate the 2012 calculation inside its original model.[^s-extensions]

For place fields, Eliav and colleagues' long-tunnel recordings and Harland and colleagues' large-arena recordings supply the multiple-field, multiple-scale observations. Yartsev and Ulanovsky supply the three-dimensional bat recordings. The 2025 paper reanalyzes those existing data, so its agreement across dimensions is not three newly collected experiments under one protocol. The later study by Maimon and colleagues directly compares CA3 and CA1 in large tunnels: predominantly single fields in CA3 contrast with multiple fields in CA1, while field sizes are similar. That distinction supports treating the CA1 statistics and the upstream spatial circuit as related but separately constrained parts of the explanation.[^s-place-data]

There are also direct reasons to avoid reading Gaussian spatial statistics as a unique wiring diagram. Druckmann and colleagues report structured synaptic connectivity between hippocampal regions. Bittner and colleagues show how electrical events in dendrites, the branching input structures of neurons, can induce changes in synaptic strength and form CA1 place fields. Structure and learning can therefore be present even when a random-function model describes many aggregate field statistics. The model's success leaves open which circuit mechanism produces these maps. Input, connectivity, learning, or perturbation measurements could distinguish the possibilities.[^s-wiring]

Finally, the source and use of eye motion are different questions. Nghiem and colleagues combine human eye tracking with a model of how eye movement affects visual signals to explain why an intermediate amount of fixational motion can help fine visual discrimination. A movement that partly originates from internal noise can still have useful sensory consequences, and feedback can regulate its statistics. Benefit for perception does not uniquely identify the neural generator.[^s-acuity]

## A joint test would compare tuning maps with population fluctuations {#sec:SYNTHESIS-NEXT}

The combined calculation suggests a concrete research direction. For the same population, first estimate the tuning maps with their uncertainty. Then measure fluctuations during periods where external anchoring is weak and test whether their covariance is aligned with changes along those maps. Fit diffusion only over a range where the local approximation and measurement corrections are justified. A downstream behavioral comparison must additionally include the physical or neural filters between representation and measurement.

This would ask whether one system satisfies both spatial-statistics and dynamical-stability constraints. A static Gaussian-process fit alone cannot supply the diffusion coefficient. A diffusion fit alone cannot establish the distribution of fields. A joint success would be more restrictive, while a mismatch would point to a particular assumption to change: spatial input statistics, recurrent maintenance, the observation filter, or their coupling. This is proposed follow-up work, not a replication claimed by this guide.

[^s-three]: Burak, Y., and Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109), Eqs. 1–5; Ben-Shushan, N., Shaham, N., Joshua, M., and Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [DOI](https://doi.org/10.1038/s41467-022-29201-y), Figs. 2–5; Mainali, N., Azeredo da Silveira, R., and Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [DOI](https://doi.org/10.1016/j.neuron.2025.01.017), Eq. 1 and Figs. 1–5.

[^s-attractors]: Seung, H. S. (1996). *How the brain keeps the eyes still*. PNAS, 93(23), 13339–13344. [DOI](https://doi.org/10.1073/pnas.93.23.13339); Aksay, E., and colleagues (2007). *Functional dissection of circuitry in a neural integrator*. Nature Neuroscience, 10, 494–504. [DOI](https://doi.org/10.1038/nn1877); Burak, Y., and Fiete, I. R. (2009). *Accurate path integration in continuous attractor network models of grid cells*. PLoS Computational Biology, 5(2), e1000291. [DOI](https://doi.org/10.1371/journal.pcbi.1000291).

[^s-extensions]: Koyluoglu, O. O., Pertzov, Y., Manohar, S., Husain, M., and Fiete, I. R. (2017). *Fundamental bound on the persistence and capacity of short-term memory stored as graded persistent activity*. eLife, 6, e22225. [DOI](https://doi.org/10.7554/eLife.22225); Seeholzer, A., Deger, M., and Gerstner, W. (2019). *Stability of working memory in continuous attractor networks under the control of short-term plasticity*. PLoS Computational Biology, 15, e1006928. [DOI](https://doi.org/10.1371/journal.pcbi.1006928).

[^s-place-data]: Eliav, T., and colleagues (2021). *Multiscale representation of very large environments in the hippocampus of flying bats*. Science, 372, eabg4020. [DOI](https://doi.org/10.1126/science.abg4020); Harland, B., Contreras, M., Souder, M., and Fellous, J. M. (2021). *Dorsal CA1 hippocampal place cells form a multi-scale representation of megaspace*. Current Biology, 31, 2178–2190.e6. [DOI](https://doi.org/10.1016/j.cub.2021.03.003); Yartsev, M. M., and Ulanovsky, N. (2013). *Representation of three-dimensional space in the hippocampus of flying bats*. Science, 340, 367–372. [DOI](https://doi.org/10.1126/science.1235338); Maimon, S. R., and colleagues (2026). *Sparse-to-dense coding transformation between hippocampal areas CA3 and CA1*. Nature. [DOI](https://doi.org/10.1038/s41586-026-10537-0).

[^s-wiring]: Druckmann, S., and colleagues (2014). *Structured synaptic connectivity between hippocampal regions*. Neuron, 81, 629–640. [DOI](https://doi.org/10.1016/j.neuron.2013.11.026); Bittner, K. C., Milstein, A. D., Grienberger, C., Romani, S., and Magee, J. C. (2017). *Behavioral time scale synaptic plasticity underlies CA1 place fields*. Science, 357, 1033–1036. [DOI](https://doi.org/10.1126/science.aan3846).

[^s-acuity]: Nghiem, T. E., Witten, J. L., Dufour, O., Harmening, W. M., and Azeredo da Silveira, R. (2025). *Fixational eye movements as active sensation for high visual acuity*. PNAS, 122, e2416266122. [DOI](https://doi.org/10.1073/pnas.2416266122). Results, 17-participant acuity experiment and Bayesian retinal model.
