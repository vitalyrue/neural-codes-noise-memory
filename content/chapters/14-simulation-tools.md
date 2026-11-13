# Reproduction depends on the model, numerical method, and measurement {#ch:SIMULATION-TOOLS}

A simulated eye trace can look convincing while answering the wrong question. It may use different spike statistics, a different muscle response, or a different definition of displacement from the experiment. Beyond the paper-specific methods in the preceding chapters, a reproduction needs checks that its software, resolution, and saved run record preserve the intended comparison. This chapter explains how to choose those checks and distinguish the authors' program from an independent implementation or a smaller teaching model.

**Draft diagrams:** These unreviewed generated images may contain missing labels, incorrect numbers or misleading relationships. Use the chapter text and sources as the reference.

{{block:fig:DRAFT-MAP-CH22-A}}

{{block:fig:DRAFT-MAP-CH22-B}}

## The original code and a teaching reconstruction serve different purposes {#sec:SIMULATION-TOOLS-ROUTES}

The starting point depends on the intended result. Running the authors' program tests whether its implementation produces the reported output. Rebuilding the equations in another program tests whether an independent implementation agrees. A smaller teaching model can isolate a mechanism, but its numerical output belongs to that smaller model.

For Burak and Fiete (2012), the paper and supporting text specify the network equations and numerical settings. The inspected publication records did not identify a public simulation-code package. For Ben-Shushan et al. (2022), public MATLAB code and deposited recordings support a more direct route. Mainali et al. (2025) provide Python code and links to the source datasets. The preceding chapters identify what was checked in each package and where the inspected defaults differ from the publication.

[A successful program run establishes that the chosen program executed. Agreement with a paper also requires matching its model, parameters, measurements, and uncertainty.]{.key-statement} The simulation summaries here are source-based explanations. The guide has not rerun the authors' full simulations or reprocessed their animal recordings.

One further distinction matters for Part III. A computer can calculate a neural model, calculate a proposed transistor circuit, or collect measurements from a fabricated chip. Sun et al. (2026) report post-layout hardware simulations. Pehle et al. (2022) describe physical analog neural circuits. Both can address memory, but their outputs support different claims about an electronic device. The [hardware comparison](ch-neuromorphic-systems.html) keeps these cases separate.

## Tools should match the operation being tested {#sec:SIMULATION-TOOLS-SOFTWARE}

The authors' implementation is the first choice when the goal is to reproduce their figures. Other libraries are useful when the goal is to isolate a mechanism or change a model. The following tools have distinct roles. The optional tools are suggestions for a new implementation, not claims about what all three papers used.

<div class="table-responsive">

{{block:tbl:SIMULATION-TOOLS}}

</div>

NumPy's `Generator` supplies random samples for a Python implementation. To repeat a sequence using a [random seed](ch-simulating-eye.html#sec-simulating-eye-path), record the generator, software versions, and order of calls as well as the seed. A seed alone does not guarantee identical results after changing the program or library version.[^simtools-numpy]

SciPy's `solve_ivp` integrates ordinary differential equations from an initial state. It can handle deterministic decay or a deterministic rate model. A stochastic spiking model also needs rules for generating events and applying their jumps. A Brownian-noise model needs a numerical method with the appropriate random increments. Passing freshly drawn noise into an adaptive deterministic solver does not, by itself, specify either model.[^simtools-ode]

For a spatial firing map, SciPy's `ndimage.label` identifies connected groups of nonzero array entries. Its connectivity rule determines which neighboring samples belong to one field. Diagonal contact can merge two regions under one rule and leave them separate under another. That choice changes field counts and sizes, so it belongs in the scientific method.[^simtools-label]

Brian 2 is an optional simulator for spiking neural networks, with equation-based neuron definitions and event handling. Its convenience does not make a default neuron model equivalent to the papers' models. A replacement must preserve the actual state variables, rate rule, spike statistics, and synaptic update before its results can be compared.[^simtools-brian]

## Time and space resolution must preserve the modeled physics {#sec:SIMULATION-TOOLS-RESOLUTION}

A simulated trajectory is recorded at finitely many times, and a generated field is sampled at finitely many positions. [[**Discretization**]{.definition-term custom-style="Definition Term"} replaces a continuous variable such as time or position by a finite set of sample points.]{.definition-explanation} The resulting numerical approximation can introduce its own drift, missed spikes, or merged fields.

For a time simulation, reduce the update interval while preserving physical rates and time constants. Compare the estimated diffusion coefficient, correlation function, and any drift of the mean. Separately change the interval at which results are saved: a small internal update does not recover information discarded by sparse output sampling. For a spatial simulation, reduce the grid spacing while preserving the physical correlation length and domain. Then examine field counts, size distributions, and the smallest features that remain resolved.

A [[**convergence check**]{.definition-term custom-style="Definition Term"} tests whether the quantity being reported changes acceptably little when the numerical resolution is refined.]{.definition-explanation} The acceptable difference depends on the scientific comparison and the uncertainty from repeated random realizations. A smooth-looking trajectory is not a convergence check.

<div class="publisher-worked-calculation publisher-fold-always">

**Example: a smaller time step must keep the same diffusion per second.**

Consider the guide's reduced Brownian model, with diffusion coefficient $D=0.5$ deg$^2$/s. Over a step of duration $h$, the angular increment has variance $2Dh$. At $h=0.01$ s, its standard deviation is $0.1^\circ$. Reducing the step to $0.0025$ s makes the standard deviation $0.05^\circ$.

There are now four times as many steps per second, each with one quarter of the variance. The variance accumulated in one second remains $1$ deg$^2$. If the increment's standard deviation were reduced by four instead of two, that variance would fall to $0.25$ deg$^2$. The program would be simulating a different noise strength.

This calculation concerns Gaussian increments of the reduced model. A network driven by discrete spikes instead generates events according to its firing-rate rule and applies the specified synaptic jumps.

</div>

The spatial counterpart is a field defined in meters whose grid spacing is halved. Its correlation scale in grid samples must double to represent the same physical length. Keeping a filter width fixed in samples would change the model while appearing to improve resolution.

## A useful reproduction saves the choices that determine the conclusion {#sec:SIMULATION-TOOLS-RECORD}

To reproduce one panel, identify its target quantity before running the model. Figure 2 of Burak and Fiete (2012) tests memory diffusion, whereas a field-size histogram in Mainali et al. (2025) tests a spatial distribution. The following record connects a computation to the claim it can support:

1. **Source and target:** paper, correction if applicable, figure or equation, code revision, and the statistic being compared.
2. **Model and inputs:** equations, initial state, boundaries, noise law, and which parameters are measured, fitted, or chosen.
3. **Numerical choices:** update rule, time or spatial resolution, output sampling, trial count, and random-generator settings.
4. **Measurement:** decoder or field detector, filtering, discarded transients, normalization, and units.
5. **Comparison:** published prediction or dataset, uncertainty over independent repeats, and the effect of refining numerical resolution.

[[**Monte Carlo simulation**]{.definition-term custom-style="Definition Term"} estimates a quantity by repeating a calculation with random samples.]{.definition-explanation} Its uncertainty depends on the effective number of independent repeats. Hundreds of overlapping time windows from one eye trace are not hundreds of independent trajectories. Many fields from one generated map can also share the same underlying random realization. The unit of repetition should match the uncertainty being estimated.

A practical progression is to test one deterministic decay or one generated field, then a few repeated runs, and then the published parameter set. Saving the inputs and intermediate measurements makes a disagreement diagnosable. A mismatch in the final plot can then be traced to the dynamics, the measurement rule, or the comparison itself.

[The common neurophysics question is which physical assumption produces the measured pattern, and whether that pattern remains after reasonable changes to the numerical implementation.]{.key-statement} Software supplies controlled experiments on a model. The link to an animal or a fabricated circuit still comes from the evidence used to constrain and test that model.

[^simtools-numpy]: NumPy developers. *Random Generator*, NumPy 2.5 documentation. [Generator and reproducibility guidance](https://numpy.org/doc/stable/reference/random/generator.html). Retrieved October 30, 2026. The guide recommends this for an optional Python reconstruction.

[^simtools-ode]: SciPy developers. *scipy.integrate.solve_ivp*, SciPy 1.18.0 documentation. [Ordinary differential equation solver](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html). Retrieved October 30, 2026.

[^simtools-label]: SciPy developers. *scipy.ndimage.label*, SciPy 1.18.0 documentation. [Connected-component labeling](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.label.html). Retrieved October 30, 2026.

[^simtools-brian]: Brian developers. *Brian 2 documentation*, version 2.11.0. [Spiking-network simulator](https://brian2.readthedocs.io/en/stable/). Retrieved October 30, 2026.
