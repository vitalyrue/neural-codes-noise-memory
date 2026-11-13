# Eye simulations connect a noisy neural command to measured motion {#ch:SIMULATING-EYE}

A reproduction of Ben-Shushan et al. (2022) must distinguish the recording analysis from the simulated eye-control pathway. The [circuit chapter](ch-eye-circuit.html) explains why a noisy internal command is a possible source of drift. Here the added detail is how the published parameters, spike generator, update intervals, saved samples, and MATLAB files determine the numerical experiment, and which code or data gaps limit reproduction. The pathway below gives the mechanism needed to interpret those choices.

## Recorded data constrain the question before the model generates a trajectory {#sec:SIMULATING-EYE-DATA}

The empirical analysis uses earlier recordings of 57 ocular motor neurons from two macaques, paired with eye-position measurements. These are separate single-cell recordings, not a simultaneous recording of all 57 neurons. The authors fit each cell's firing-rate relation to eye position, velocity, and acceleration. For firing-rate prediction, they fit all trials except one and predict the firing rate in the omitted trial, repeating this leave-one-out procedure across trials. The analysis also uses the fitted movement relation to reconstruct motion from that cell's spikes.[^simeye-data]

After excluding rapid eye movements, the analysis compares measured and reconstructed displacements over 350 ms segments. Their covariance supports a substantial shared drive upstream of the motor neurons. The estimate near 82% depends on calibrated gains and the assumed separation of shared and private fluctuations. It is not a measurement of noise inside the integrator itself.

The authors then test whether an integrator with plausible cellular properties can generate enough shared motion, with the right timing, after the motor pathway filters it. Its tuning distributions and spike variability are constrained by earlier physiological studies. Some remaining choices are adjusted to compare with the measured drift. The paper notes that several parameter combinations can match its magnitude.

## The generated command acts through spikes, muscle response, and delayed feedback {#sec:SIMULATING-EYE-PATH}

The model has four connected stages. Each stage changes a different physical or represented quantity:

1. **Integrator activity:** two opposing neural populations sustain a represented eye-position command. Spikes renew decaying synaptic activity, and recurrent input sets later firing rates. A weighted difference between the populations produces the command $E_{\mathrm{OI}}$.
2. **Motor-neuron spikes:** each simulated motor neuron receives that command. Its tuning slope and threshold convert the commanded angle into a firing rate. Spike generation adds that neuron's private variability.
3. **Muscle and eye response:** filtered motor activity drives a mechanical response with position, velocity, and acceleration terms. Combining the motor contributions gives the eye angle $E$.
4. **Delayed visual feedback:** the difference between an earlier eye position and the current internal command changes the integrator's input. New changes in actual eye position enter this feedback after the delay, while the current internal-command term acts immediately.[^simeye-model]

[The internal command and the physical eye angle are separate outputs. The muscles smooth rapid command fluctuations, so the eye's short-lag motion need not have the same statistics as the neural state.]{.key-statement} The [eye-timing chapter](ch-eye-timing.html) derives a simplified filtering example. The [circuit chapter](ch-eye-circuit.html) explains the full model's neural assumptions.

The circuit structure is adapted from Aksay et al. (2007), with tuning and noise assumptions adjusted to primate evidence. Its weights are fitted so that a range of commands can persist in the mean-rate model. This is different from fitting an eye-drift trace.

The spikes are more regular than a Poisson process. The model generates candidate events at $M$ times the desired rate and retains every $M$th event. At constant rate, each retained interval sums $M$ exponential waiting times, giving interval coefficient of variation $1/\sqrt M$. This preserves the mean firing rate while reducing interval variability. The published simulations use integrator variability around 0.22 and motor-neuron variability around 0.07.

Simulated spike times are drawn by a program that generates a repeatable sequence of random-looking numbers. A [[**random seed**]{.definition-term custom-style="Definition Term"} sets its starting state, allowing the same implementation and sequence of calls to reproduce those samples.]{.definition-explanation} The spike-generation rule specifies the intended distribution; the seed chooses the sample sequence.

::: {.publisher-clarification-note .publisher-fold-always title="Published parameters and public-code settings have different sources"}

The final main Methods report an integrator size $N=30{,}000$, 1,000 motor neurons, synaptic time constant 20 ms, and feedback strength $A=0.015$. The feedback delay is about 70 ms. These are the main model settings, not values to combine with the different comparison runs in the supplement.

The inspected MATLAB code sets its internal update interval to $10^{-5}$ s and saves every 100 steps, giving 1 ms output samples. It uses a 10 ms motor-neuron synaptic time constant, initializes central gaze, and sets the random seed from the trajectory index. Synaptic decay is updated by first-order Euler steps. The mechanical calculation updates velocity and then position.

The code's `N` creates a vector in each of the paired populations, whereas the paper describes $N$ as the network's neuron number. That convention must be resolved before claiming a function call reproduces the published size. The code also uses a different motor-neuron variability regression from the final printed Eq. 35.[^simeye-code]

:::

## Controls test which stage can explain the observed fluctuations {#sec:SIMULATING-EYE-CONTROLS}

One matching trajectory is weak evidence because many mechanisms can look irregular. The paper compares outputs after changing sources of variability or feedback:

- **Change the noise source:** compare a fixed command with private motor noise (Figure 3), the noisy internal command before muscle filtering (Figure 4), and the complete pathway (Figure 5). The [circuit chapter](ch-eye-circuit.html) explains these comparisons. Keep the measured signal explicit: internal command and final eye angle are different outputs.
- **Check the measurement procedure:** apply the recording reconstruction and covariance analysis to simulated motor spikes and eye motion. This tests recovery of the shared contribution where its origin is known. Muscle filtering and delayed feedback must remain in the complete-pathway comparison.[^simeye-figures]

The supplement adds checks of measurement-noise subtraction, feedback removal, and the contribution of direct output spiking noise. In the last check, noise still drives the internal integrator, so removing motor-output noise does not turn the entire model deterministic.

These controls support the integrator as a sufficient explanation under the tested assumptions. They do not show that it is the only central circuit capable of producing the recordings. The shared-source estimate from data and the proposed location of that source remain different conclusions.

## Public MATLAB code and recordings support different reproduction tasks {#sec:SIMULATING-EYE-TOOLS}

The authors release MATLAB `.m` functions and `.mat` parameter files. `Run_model.m` starts trajectories and their mean-squared-displacement analysis. `Full_model_simulation.m` updates the integrator, motor neurons, and eye. `Fit_OI_circuit.m` fits a persistent mean-rate circuit, while the analysis routines compare generated trajectories with an already processed empirical MSD file.[^simeye-code]

The separately deposited raw recordings contain one spreadsheet per cell and one sheet per trial. The columns give horizontal and vertical eye angles and spike times. Eye samples are spaced by 1 ms. Reanalyzing those recordings tests the empirical reconstruction. Running the model tests a proposed source of the motion. Loading the processed MSD file alone does not reproduce the raw-data analysis.[^simeye-deposit]

The inspected repository does not specify a MATLAB version or a complete environment. Source calls include constrained least squares, random sampling, and correlation routines, whose required functions and toolboxes must be available. The repository's `rate` branch calls a function absent from the inspected file tree. These are practical limits to check before treating the package as a complete figure-reproduction workflow. No such end-to-end run is claimed here.

For a neurophysics study, the useful next calculation is controlled: vary one cellular or mechanical assumption, keep the measurement procedure fixed, and examine which observed statistic changes. Mainali et al. (2025) use a different form of this reasoning. Their simulations change spatial maps and measure the regions where cells would fire, without simulating eye motion or a time-dependent memory circuit.

[^simeye-data]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry*. Nature Communications, 13, 1697. [Behavioral task, fitting, and displacement analysis, PDF pp. 9–10](../papers/ben-shushan-2022-fixational-drift.pdf#page=9). [DOI](https://doi.org/10.1038/s41467-022-29201-y).

[^simeye-model]: Ben-Shushan et al. (2022), [Methods, Eqs. 23–35, PDF pp. 10–11](../papers/ben-shushan-2022-fixational-drift.pdf#page=10). The model adapts the circuit in Aksay et al. (2007), *Functional dissection of circuitry in a neural integrator*, Nature Neuroscience, 10, 494–504. [DOI](https://doi.org/10.1038/nn1877).

[^simeye-code]: The Burak Lab. (2022). *Fixational drift is driven by diffusive dynamics in central neural circuitry* [MATLAB source code]. [Inspected revision, February 28, 2022](https://github.com/The-Burak-lab/Fixational-drift-is-driven-by-diffusive-dynamics-in-central-neuralcircuitry/tree/27d4093008c6756fe8ae2ad77567176ed626bd17). Code inspection, not execution, checked October 30, 2026.

[^simeye-figures]: Ben-Shushan et al. (2022), [Figures 3–5, PDF pp. 6–8](../papers/ben-shushan-2022-fixational-drift.pdf#page=6); [supplementary Figures 2–5 and 10, PDF pp. 8–10 and 14](../papers/ben-shushan-2022-supplement-1.pdf#page=8).

[^simeye-deposit]: Ben-Shushan, N., Shaham, N., Joshua, M., & Burak, Y. (2022). *Fixational drift is driven by central neural circuitry* [Dataset]. Zenodo. [Recorded eye positions and spike times](https://doi.org/10.5281/zenodo.6076911).
