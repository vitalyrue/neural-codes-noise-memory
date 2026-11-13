# Part III neurophysics source checks

Research only. No manuscript or artwork changed. Started 2026-10-30 14:07:35 UTC. Checkpoint 14:08:47 UTC: wall elapsed 72 seconds; awake execution time unverified because sleep/resume events were not checked. Model inherited from parent; exact version and token counts unavailable.

## Opening quotation and its limits

John von Neumann, *The Computer and the Brain* (Yale University Press, 1958), printed page 66, PDF page 78, zero-based page index 77:

> Lastly, I would like to mention that systems of nerve cells, which stimulate each other in various possible cyclical ways, also constitute memories.

This is 23 words. It was checked against the page image, not only OCR. Source: [book PDF, page 78](https://vpb.smallyu.net/%5BAuthor%5D%20John.Von.Neumann/The%20Computer%20and%20The%20Brain.pdf#page=78). Local evidence: `research/von-neumann-1958.pdf` and `research/von-neumann-printed66-pdf78.png`.

Context, paraphrased: printed pages 66-68 compare mutually active neural elements with electronic flip-flops. Von Neumann then doubts that such active elements supply the nervous system's main large-capacity memory because of their cost. Other physical forms of storage could differ from the elements performing computation. Do not present this paragraph as a prediction that all brain memory uses recurrent firing or as evidence that modern neuromorphic devices descend directly from this passage. A conceptual link is supported; a historical chain of influence was not checked. Keep the quotation above as the sole book quotation to stay below 25 quoted words.

## Seung: the missing distinction between a bit and a graded memory

H. S. Seung (1996), *How the brain keeps the eyes still*, PNAS 93:13339-13344. [DOI 10.1073/pnas.93.23.13339](https://doi.org/10.1073/pnas.93.23.13339); [public paper PDF](https://neurophysics.ucsd.edu/courses/physics_171/seung_pnas_line.pdf). Saved as `research/seung-1996.pdf`. This copy has a cover: journal page 13339 is PDF page 2.

Page 13343, nonlinear-model section and Discussion: discrete stable states in digital circuits resist small disturbances, whereas eye position is graded. The line direction preserves an intended change but also allows noise to alter the remembered value. Disturbances across the line relax. Pages 13341-13343 explain slow drift under imperfect tuning and the difference between changing a state and changing its dynamics. Pages 13343-13344 discuss learning and longer synaptic times as ways to reduce the tuning demand.

Use this as a mechanistic comparison, not a claim that spikes cannot support continuous variables, that analog electronics cannot implement bits, or that every nonlinear network can only approximate a line. Seung analyzes particular network classes. The relevant object is the population's evolving state, not the label digital/analog attached to a device.

## Hardware bridge 1: a head-direction estimate, with finite positions

Tarek M. Massoud and Timothy K. Horiuchi (2011), *A Neuromorphic VLSI Head Direction Cell System*, IEEE TCAS I 58(1):150-163. [DOI 10.1109/TCSI.2010.2055310](https://doi.org/10.1109/TCSI.2010.2055310). The primary manuscript, uploaded by its author, is readable at [ResearchGate](https://www.researchgate.net/publication/260666649_A_Neuromorphic_VLSI_Head_Direction_Cell_System). No local full PDF saved.

Sections III-IV describe physical analog neuron/synapse circuits with digital spike routing through microcontrollers, including four neuron chips. Section V.F and Figure 21 show stimulation creating a bump that persists after the cue and later resetting it. Section V.G, manuscript page 11, explicitly states 32 bump positions over 360 degrees, hence 11.25-degree resolution; equations (1)-(5) connect angular velocity, bump movement and angle. Earlier integration results and Figures 19-20 show systematic errors. It is a working physical recurrent memory for an orientation estimate. It is not an experimental realization of an exact continuum of fixed points or an unqualified demonstration of noise-driven Brownian drift. Its finite resolution is central to the bridge.

## Hardware bridge 2: noisy bistable working memory

Massimiliano Giulioni, Patrick Camilleri, Maurizio Mattia, Vittorio Dante, Jochen Braun and Paolo Del Giudice (2012), *Robust Working Memory in an Asynchronously Spiking Neural Network Realized with Neuromorphic VLSI*. [Full primary article](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2011.00149/full), [DOI 10.3389/fnins.2011.00149](https://doi.org/10.3389/fnins.2011.00149). Published 2 February 2012, although the volume/DOI uses 2011.

Materials and Methods, sections The neuromorphic chip and The network: 128 available neurons; the network uses two excitatory populations of 48 and one inhibitory population of 31. Strong recurrence supports low/high activity states. Results show stimulus-triggered persistence, spontaneous transitions and correction of corrupted high states. The paper reports persistence lasting seconds despite millisecond circuit time scales, and ties transitions to noise and the effective landscape. Its theory-guided method measures the open-loop response and compares repeated trials with a model. Device mismatch matters; adaptation and plasticity were disabled. This is bistable memory, not graded line-attractor memory. It supports the collective-timescale and controlled-noise bridge.

## Recent actual hardware example

Muhammad Aitsam, Aung Htet, Syed Saad Hasan, Alejandro Jimenez Rodriguez and Alessandro Di Nuovo (2026), *A spiking continuous attractor network for event-driven neuromorphic robot guidance*. Published 16 September 2026. [Full primary article](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2026.1910808/full), [DOI 10.3389/fnins.2026.1910808](https://doi.org/10.3389/fnins.2026.1910808), [university record and PDF](https://shura.shu.ac.uk/37995/). Saved as `research/aitsam-2026.pdf`.

Sections 2.1 and 3.3: 768 spiking neurons on a 32 by 24 sheet, integer recurrent weights, one SpiNNaker 2 chip. Physical event camera and Raspberry Pi supply evidence. Section 4.1, Figure 3, printed pages 8-9: persistence through an eight-second input-free interval, with decoded-centroid displacement at most 0.50 cells. Eight seconds is a lower bound, not a measured lifetime. Section 4.4 uses a simulated robot; both sets of ten guidance trials reach the goal. Section 4.5, page 13, gives estimated power, not direct board measurements.

Good recent endpoint: persistent recurrent state actually runs on neuromorphic hardware. Limits: finite grid, quantization, host preprocessing and finite trials. The paper does not establish an exact continuum or measure the noise diffusion coefficient proposed below. This targeted search was not a full literature review and does not support any claim that other recent examples do not exist.

## Proposed neurophysics questions, not results from those hardware papers

1. **What state stores the cue?** Define an experiment: briefly write a cue x0, remove it, record population activity, and decode x(t). Test many cue values and delays. Persistent total firing alone does not show that the cue's value remains available.
2. **Which disturbances are corrected?** Identify the slow direction along the memory family and the fast directions away from it. Apply equal-size perturbations in each. Measure recovery across the family separately from displacement along it. Seung supplies the logic; implementation and calibration must be measured on the device.
3. **Does noise project onto the remembered value?** An intentional reduced model is dx = b(x)dt + sqrt(2D(x))dW. Here b is systematic drift, and D is half the short-time variance growth rate. Fit repeated cue-matched trials; separate decoder noise, trial-to-trial offsets and actual state fluctuations. A variance fit can be distorted by pinning, boundaries, correlations and slow drift.
4. **How does circuit noise become memory noise?** For dr = f(r)dt + B dW near an ideal family r*(x), normalize the left neutral vector l by l^T dr*/dx = 1. To leading order with a local linear projection, D(x) = l^T BB^T l / 2. The left vector, not only the visible tangent, determines sensitivity in a general nonsymmetric network. Curved families and state-dependent noise can add drift terms. Present this equation as a proposed model to fit and test, not a measurement already established by the cited hardware papers.
5. **What do mismatch and quantization do?** Measure conditional mean displacement b(x), preferred resting positions and transitions. Change weight resolution, calibration and network size. A flat drift curve over a finite interval can support an approximate integrator; a set of preferred positions points to pinning. The 32-position device makes the distinction concrete.
6. **Which time scale is long?** Compare component decay, recovery across the family, drift along it and cue-decoding error. For an illustrative linear feedback mode, tau_s du/dt = -(1-lambda)u gives tau_memory = tau_s/(1-lambda) only for lambda < 1. Close feedback extends persistence; excessive feedback can instead grow until nonlinear limits intervene. This is a teaching model, not a fit to every hardware circuit.
7. **How much memory survives?** Report error as a function of delay and cue. Hardware register bits, synaptic weight bits and usable remembered cue information are different quantities. A population with digital events can represent a graded value; its effective resolution is measured from decoding, noise and drift. Claim bits only after defining the cue distribution, decoder/readout assumptions and precision criterion.
8. **What does the physical substrate change?** Record actual timing, measured transfer functions, mismatch, spike correlations, quantization and energy at a stated system boundary. Compare the same recurrence and decoder on a numerical reference. Distinguish on-chip dynamics from host work. Use repeated trials, with a prespecified fit and separate test conditions, to decide where the intended equations fail.

## Safe narrative spine

The book gives a short, limited analogy: mutually active elements can hold a memory. Seung asks how such activity can preserve a graded physical variable rather than only a discrete state. The older hardware papers show that orientation estimates and noisy recurrent working memory can be built in silicon, with finite resolution and circuit limits. The 2026 example puts a persistent spatial estimate on a current neuromorphic chip. The new research question is what controls the estimate's drift, precision and recoverability in an actual physical network. This is a teaching sequence, not a demonstrated line of historical influence.

## Memory consulted

Only repository-scope guidance was reused: `MEMORY.md:64-90`, especially the existing figure-review hold and the instruction not to confuse focused checks with full release acceptance. All scientific facts above were checked from current primary-source contents.

Completed 2026-10-30 14:09:45 UTC. Wall-clock elapsed 130 seconds; time since previous persisted checkpoint 58 seconds. Awake execution time unverified. The original estimate was 6-8 minutes; direct source access allowed completion sooner. Source note, three PDFs and the inspected book-page image exist. Token stats unavailable.
