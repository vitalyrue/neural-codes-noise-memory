# Network simulations test how random spikes move a stored value {#ch:SIMULATING-MEMORY}

To compare a simulated memory trace with Burak and Fiete's (2012) theory, the numerical update and the measurement of the stored value must match the model. The [foundation chapter](ch-foundations.html#sec-foundations-simulation) explains the spike-update cycle, and the [long-delay chapter](ch-memory-long-delays.html) interprets its diffusion tests. Here the additional task is to recover the published network settings, distinguish a numerical position measurement from the theoretical coordinate, and identify choices left open for an independent reproduction.

**Draft diagrams:** These unreviewed generated images may contain missing labels, incorrect numbers or misleading relationships. Use the chapter text and sources as the reference.

{{block:fig:DRAFT-MAP-CH19-A}}

{{block:fig:DRAFT-MAP-CH19-B}}

## A simulation renews the same synaptic state that the theory approximates {#sec:SIMULATING-MEMORY-STATE}

The physical idea is continuing neural activity after a cue has ended. A spike briefly increases synaptic activation. That activation decays, but it also changes the rates at which other neurons fire. Recurrent connections can therefore renew the activity. Random event times disturb the pattern that represents the remembered value.

The computer stores each neuron's synaptic activation $s_i$. The total input $g_i$ and firing rate $r_i$ are calculated from it:

$$
g_i=\sum_j W_{ij}s_j+b_i,\qquad r_i=\phi(g_i).
$$

Here $W_{ij}$ is the connection from neuron $j$ to neuron $i$, $b_i$ is a constant input, and $\phi$ converts total input into a rate in spikes per second. In the paper's normalization, each spike increases $s_i$ by one and activation decays with time constant $\tau$. The [earlier neural mechanism and derivation](ch-foundations.html#sec-memory-spikes) explain these variables and the continuous-time equations.[^simmem-model]

One short simulation step has a causal order:

1. Read the current activations and calculate the recurrent inputs and firing rates.
2. Generate spikes using those rates and the chosen time interval.
3. Apply synaptic decay and the increments caused by those spikes.
4. Decode the represented value and repeat after the external cue is absent.

The ring simulation uses the [Euler update introduced in Chapter 1](ch-foundations.html#sec-foundations-simulation): approximate a variable's change over a short interval by its current derivative times that interval. For decay alone, an interval $h$ changes $s_i$ to approximately $s_i(1-h/\tau)$. Spike increments are added according to the event model. This finite step approximates the continuous dynamics, so its accuracy must be checked at the resolution needed for the reported statistic.

[Each generated spike changes the recurrent inputs and can change the rates of later spikes.]{.key-statement} The theory explains when these interacting changes can be described by diffusion of one coordinate.

## Ring trajectories test both the diffusion rate and the effect of angular boundaries {#sec:SIMULATING-MEMORY-RING}

In the ring model, neurons are ordered by preferred angle, and the position of their localized activity pattern represents the stored angle. The [earlier Figure 2 discussion](ch-memory-long-delays.html) explains the diffusion and information comparison. To reproduce that comparison, keep the exponential and sigmoid transfer functions as separate runs, with a theoretical prediction calculated from each run's steady tuning curves.[^simmem-ring]

The comparison separates prediction from measurement. First, solve the noise-free network for its steady activity pattern and calculate the predicted diffusion coefficient and information rate. Then run the stochastic network and measure its angular displacement. For this simulation the authors record the preferred angle of the neuron with the largest instantaneous rate. This is a numerical proxy for the represented position. The theoretical coordinate $\theta$ is assigned by following noise-free relaxation back to the attractor; the largest-rate rule does not carry out that projection. Its output can take only one of the neurons' preferred angles, and brief changes in the pattern's shape can shift its maximum during relaxation. These effects matter when interpreting very short lags. This rule also differs from the ideal spike-based estimator studied later in the paper.

At short lags, the displacement variance tests $\operatorname{Var}(\Delta\theta)\simeq2D\ell$. Here $\Delta\theta=\theta(t+\ell)-\theta(t)$ is the change in represented angle over lag $\ell$, measured in seconds, and $D$ is the diffusion coefficient in angle squared per second. At long lags, the reported differences are wrapped into $(-\pi,\pi)$, so the mean square levels off. The long-lag comparison uses a diffusion calculation with periodic boundaries. This saturation limits the reported angular error. It does not recover the initial angle.

::: {.publisher-clarification-note .publisher-fold-always title="Published settings: the ring network in Figure 2"}

The Methods specify 1,024 neurons, synaptic time constant 10 ms, and update interval 0.1 ms. Each step generates a spike for neuron $i$ with probability $r_i h$, where $r_i$ is its current firing rate and $h$ is the update interval. This one-event approximation requires that probability to remain small. There are 100 trials of 1,000 seconds each. The displacement analysis excludes the first 10 ms. Error bars are standard errors across trials.

Writing $\alpha$ for the separation of preferred angles, the finite network uses the connection weight $w(\alpha)$ from one neuron to the other:

$$
w(\alpha)=e^{\cos\alpha-1}-e^{0.3(\cos\alpha-1)}.
$$

The common input is $b=-2$ and $\tau=10$ ms is the synaptic decay time. With $g$ the total input to a neuron and $\phi(g)$ its firing rate, the two transfer rules are $\tau\phi(g)=10e^g$ and $\tau\phi(g)=0.2[1+\tanh(g+4)]$. Initial activations are independently uniform between 0 and 0.01. These settings describe the finite simulation. The supporting text separately divides a connection rule by $N$ to study larger populations. Applying that extra factor here would change the reported weights.

The symmetric-network prediction uses the squared input slope in its numerator. Burak and Fiete's 2017 correction confirms that square, which was missing in the supplied Early Edition's Eq. 2. The correction does not change these simulation settings.[^simmem-correction]

:::

## Other network designs test which conclusions depend on the ring {#sec:SIMULATING-MEMORY-CONTROLS}

A second network contains two mutually inhibiting units, interpreted also as two neural populations. Increasing one population's activity while decreasing the other's changes the stored value. Figure 2E–G tests diffusion in this family without relying on rotational symmetry. The diffusion calculation applies to both models because each has a continuous family of states and restoring dynamics toward that family.[^simmem-two]

The Methods report cross-couplings of $-1$, no self-coupling, common input $b=5{,}000$, time constant 100 ms, update interval 0.4 ms, and duration 200 seconds. The transfer rule is $\tau r_i=g_i$ in the valid positive-rate range. These large rates can represent aggregate population activity. They should not be read as ordinary firing rates of two biological cells.

Converting between activation and rate changes the units of the stored value. Let $\theta_s=s_1-s_2$ be the activation difference and $\theta_r=r_1-r_2$ the rate difference along the steady-state family. Since $s_i=\tau r_i$ there, $\theta_r=\theta_s/\tau$ and their diffusion coefficients satisfy $D_r=D_s/\tau^2$. Their units differ, so their numerical values should not be compared without this conversion. A population can also emit several spikes within one update. The ring's at-most-one-spike rule cannot be copied into this setting. The paper specifies a Poisson process but does not say how spike counts were drawn or give the complete initial state for this example.

To reproduce Figure 2G, the measured displacement must be a change in the rate difference, not a change in either rate alone. Write $T=200\,\mathrm{s}$ for the recording duration and $\ell$ for the lag. Using the rate coordinate $\theta_r(t)=r_1(t)-r_2(t)$, the plotted statistic is

$$
\widehat{\operatorname{MSD}}_r(\ell)
=\left\langle[\theta_r(t+\ell)-\theta_r(t)]^2\right\rangle_{0\leq t\leq T-\ell}.
$$

The hat marks an average calculated from the finite simulation. For each lag, take both rates at the beginning and end of every available interval, form their differences, square the change, and average those squared changes over starting times. At a 2-second lag, for example, valid starts run from 0 to 198 seconds. Intervals can overlap, so these are not independent trials. The average uses many positions along one simulated trajectory; it is not the 100-trial standard error calculation used for the ring panels.

Figure 2F reports rates in $\mathrm{ms}^{-1}$, so G reports squared rate displacements in $(\mathrm{ms}^{-1})^2$. If a reproduction stores rates in $\mathrm{s}^{-1}$, divide its squared displacements by $10^6$ to compare their numerical values with G. The theoretical line must use $2D_r\ell$ in the same units. [Agreement tests whether the predicted diffusion gives the spreading of the simulated rate difference.]{.key-statement} It does not compare the rate trace with a recorded animal's memory errors.[^simmem-two]

The supporting text also tests a mutually excitatory pair in Figure S1. Across 4,000 trials started at the same coordinate, its variance grows linearly even though the local diffusion coefficient depends on the state. The guide's [long-delay chapter](ch-memory-long-delays.html#sec-memory-long-time) explains the coordinate and the printed factor-of-two discrepancy. That discrepancy is separate from the authors' 2017 correction.

## A plotted analytical curve is different from a network simulation {#sec:SIMULATING-MEMORY-OUTPUTS}

Figures 3 and S2 plot formulas for readout error. They compare an ideal estimator with an estimator that weights all observations equally as the observation interval grows. The sources do not describe an additional spiking-network experiment or a biological circuit implementing ideal estimation in these figures.

The paper specifies its network equations and several numerical settings, but does not identify a programming language or simulator package. No public simulation-code archive was identified in the checked paper, supplement, or author publication entries. This describes the search as of October 30, 2026. It is not proof that no code exists. A new implementation must document choices the paper leaves open, including how it generates random numbers and events for aggregate populations.

[The simulations show that the stated network models can produce the predicted memory errors. Connecting those errors to animal behavior requires a measurement model and biological data.]{.key-statement} Ben-Shushan et al. (2022) add those elements by following an internal eye-position command through motor neurons and muscles to measured motion.

[^simmem-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [Model equations 7–11, PDF pp. 5–6](../papers/burak-fiete-2012-persistent-activity.pdf#page=5); [Supporting Text, Sections I–II](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1). [DOI](https://doi.org/10.1073/pnas.1117386109).

[^simmem-ring]: Burak and Fiete (2012), [Figure 2A–D, PDF p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3), [Network Simulations, PDF p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6), and [Supporting Text, Eq. S32](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8).

[^simmem-correction]: Burak, Y., & Fiete, I. R. (2017). *Correction for Burak and Fiete, Fundamental limits on persistent activity in networks of noisy neurons*. [Published correction to Eq. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5441759/). [DOI](https://doi.org/10.1073/pnas.1706051114).

[^simmem-two]: Burak and Fiete (2012), [Figure 2E–G and caption, PDF p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3), [mutual-inhibition simulation, PDF p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6), and [Supporting Text, Figure S1, PDF p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10).
