# Hardware source checks for Part III

Research start: 2026-10-30 14:07:13 UTC. Sources accessed: 2026-10-30. Research only, no manuscript or figure changes and no tests. This is a bounded primary-source check, not a complete survey or acceptance of teaching text. The research-synthesis-builder skill was used for source checks and evidence limits.

## Recommended scope

Use three physically different platforms to explain where a model's state lives: Loihi 2, SpiNNaker2 and BrainScaleS-2. Add the 2026 dual-memory design as a current research bridge. Hala Point belongs under scaling Loihi 2. It does not introduce another kind of storage. DYNAP-SE2 was omitted to keep the evidence set small.

Keep three objects separate throughout: connection weights; changing neuron/synapse variables; and a remembered quantity maintained by the network's ongoing dynamics. The first two are implementation resources. The third is a computational function that must be shown for a specific network and task. A research platform's capacity alone does not show reliable working memory.

Interpretation for the guide: comparing storage alone misses the recurrent computation. A digital implementation can retain the current network variables in local memory while repeatedly applying its update rule. An analog implementation lets circuit variables evolve continuously. Both still need suitable connections and stable dynamics to maintain the intended remembered quantity.

## H1. Loihi 2 official technical brief, older architecture reference

**Source:** Intel Labs, *Taking Neuromorphic Computing to the Next Level with Loihi 2*, technology brief, 2021 launch generation. The inspected copy ends with September 2021 characterization details; the search engine's later PDF date is not the architecture's launch date. No individual authors or revision identifier appear in the inspected text.

**URL:** [Intel technical brief](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf).

**Locators:** printed pp. 5–7, Base Architecture, Support for three-factor learning rules, Capacity, Fig. 2, Table 2; p. 3 for time steps/access; p. 7 footnotes for measurement limits.

**Verified:** weights and neuron variables use local digital memory banks, shared flexibly between functions; 192 KB per neuron core. Programmable learning uses pre-, post- and third-factor traces. Asynchronous circuitry still executes model time steps. Capacity depends on precision and connectivity encoding.

**Limits:** several speed claims mix silicon measurements and circuit simulations. The document's access information describes research-community arrangements at that time. It does not establish open retail availability in October 2026. The supplied brief does not explicitly spell out SRAM.

**Supplementary primary implementation source:** OzU-CAST, [LoihiScalingEfficiency author repository](https://github.com/OzU-CAST/LoihiScalingEfficiency), README sections “Loihi 2 Probes” and “Hardware Resources”, current main read 2026-10-30, commit not pinned. It explicitly describes CxStates as SRAM fields holding changing neuron state and separately describes synaptic memory in SRAM. This is an implementation companion, not a manufacturer circuit specification. Its compiler observations are time-specific and must not be repeated as current software limits.

## H2. Loihi 2 model state, time and noise

**Source:** Garrick Orchard, E. Paxon Frady, Daniel Ben Dayan Rubin, Sophia Sanborn, Sumit Bam Shrestha, Friedrich T. Sommer and Mike Davies, *Efficient Neuromorphic Signal Processing with Loihi 2*. arXiv:2111.03746v1, 5 November 2021; IEEE SiPS 2021, pp. 254–259, DOI 10.1109/SiPS52927.2021.00053.

**URL:** [author preprint](https://arxiv.org/html/2111.03746v1).

**Locator:** Section II, equations 1–3 and Fig. 3; abstract and introduction for evidence type.

**Verified:** neural current and voltage are numerical variables updated in discrete time. Neural programs read state memory, accumulated synaptic input, a timestep counter and random bits for stochastic models. Arithmetic and model values have finite precision; lowering precision changes memory capacity. Spikes access weighted connection lists and accumulate inputs for a following step.

**Limits:** this paper's application examples run in hardware-constrained simulation, not measured Loihi 2 application runs. Random bits are explicit model resources. Do not equate them with unavoidable analog transistor mismatch or biological spike noise. A digital variable called voltage is not itself an analog membrane voltage.

## H3. A measured Loihi 2 memory computation in 2025

**Source:** Denis Kleyko, Christopher J. Kymn, Anthony Thomas, Bruno A. Olshausen, Friedrich T. Sommer and E. Paxon Frady, *Principled neuromorphic reservoir computing*. Nature Communications 16, 640, published 14 January 2025, version of record. DOI 10.1038/s41467-025-55832-y.

**URLs:** [published article](https://www.nature.com/articles/s41467-025-55832-y), [full published text at PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11733134/).

**Locators:** Introduction; Results, “Experiments on neuromorphic hardware”; Fig. 5; Methods for readout training.

**Verified:** authors implement a memory buffer of recent input history and Sigma-Pi feature networks on Loihi 2. Three configurations compare history alone, nonlinear features alone and their combination. CPU and hardware results are compared. This directly connects changing neural state to a useful temporal computation.

**Limits:** a finite or fading history buffer is distinct from indefinitely stable persistent activity. The work separates representation from the trained readout; it does not demonstrate general continual on-chip learning. Fig. 5 explicitly says the illustrated Hala Point capacity far exceeds the experiment's needs. Do not describe this as a billion-neuron memory experiment. Nature's main page was intermittently inaccessible; the published PMC copy was read.

## H4. Hala Point, deployment and scale only

**Source:** Intel, *Intel Builds World’s Largest Neuromorphic System to Enable More Sustainable AI*, 17 April 2024, official deployment announcement.

**URL:** [Intel announcement](https://www.intel.com/content/www/us/en/newsroom/news/intel-builds-worlds-largest-neuromorphic-system.html).

**Locator:** “About Hala Point” and “What’s Next”.

**Verified:** Intel reports 1,152 Loihi 2 processors and initial deployment at Sandia National Laboratories. This establishes a built research system and reported scale, not another storage mechanism.

**Limits:** this is a vendor announcement, used only for deployment and system configuration. Do not use its efficiency headlines as independent benchmarks or its owl/capuchin comparisons as evidence of biological equivalence. Maximum resource counts and maximum speed figures need not describe one network mapping simultaneously. No claim of current public access was verified.

## H5. SpiNNaker2, directly checked 2026 primary technical paper

**Source:** Stefan Scholze, Johannes Partzsch, Sebastian Höppner, Florian Kelber, Andreas Dixius, Marco Stolba and 24 coauthors, *The SpiNNaker2 chip: a many-core platform for flexible and scalable brain-inspired computing*. arXiv:2607.24396v1, submitted 27 July 2026. Preprint, no journal acceptance established here.

**URLs:** [versioned full text](https://arxiv.org/html/2607.24396v1), [record](https://arxiv.org/abs/2607.24396).

**Locators:** Sections 3.2.1, 4.4, 4.6; supplement 6.5.1 and 6.7.

**Verified:** Section 4.4 places all demonstrated SNN neuron parameters, state variables and synaptic weights in each processing element's SRAM. ARM software updates neurons with discrete Euler steps. DRAM support for these SNN workloads is explicitly future software work, although the chip has an LPDDR4 interface. Precision is software dependent; fixed/floating-point formats and random-number resources are available. On-chip E-prop is measured in the chip paper, not just its earlier FPGA prototype.

**Limits:** missed processing deadlines can put cores out of phase and impair reproducibility. Real-time results depend on workload. E-prop energy advantages use utilization-adjusted energy and different batch sizes; the chip is much slower in that example. These are measured networks, not proof of general persistent memory or unrestricted continuous learning.

## H6. BrainScaleS-2 architecture, representative 2022 primary reference

**Source:** Christian Pehle, Sebastian Billaudelle, Benjamin Cramer, Jakob Kaiser, Korbinian Schreiber, Yannik Stradmann, Johannes Weis, Aron Leibfried, Eric Müller and Johannes Schemmel, *The BrainScaleS-2 Accelerated Neuromorphic System With Hybrid Plasticity*. Frontiers in Neuroscience 16, 795876, published 24 February 2022. DOI 10.3389/fnins.2022.795876.

**URL:** [published full text](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full).

**Locators:** Introduction; Sections 2.1–2.3; Section 3.2.1 for path integration.

**Verified:** membrane potential evolves physically on capacitance; synaptic inputs are currents. Neuron/synapse dynamics run continuously about 1,000 times faster than biological model time. Each synaptic weight is stored in local 6-bit SRAM and controls current-pulse amplitude. Analog correlation sensors measure pre/post timing; digital plasticity processors read observables and change weights online. Fixed mismatch and time/temperature drift require calibration or compensation. Configuration bits and DAC parameters are distinct from changing analog neural state.

**Limits:** analog dynamics do not imply analog weight storage. Path-integration demonstrations have hardware-specific model changes; do not identify their memory mechanism automatically with Burak's persistent-activity model. Large-scale future architecture claims in this older paper are proposals.

## H7. BrainScaleS-2 measured learning and noise

**Source:** Benjamin Cramer, Sebastian Billaudelle and 10 coauthors, *Surrogate gradients for analog neuromorphic computing*. PNAS 119(4), e2109194119, published online 14 January 2022, issue 25 January 2022. DOI 10.1073/pnas.2109194119.

**URL:** [published full text at PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8794842/).

**Locators:** “Recording Spikes and Analog Membrane Traces”; “Training Recurrent SNNs”; Discussion; Fig. 5.

**Verified:** physical membrane voltages are digitized for host-side learning. Measured recurrent networks outperform a control with shuffled recurrent connections and trained input/readout weights. Training compensates device mismatch. Authors discuss intrinsic analog stochasticity amplified through recurrence.

**Limits:** the suggested regularizing effect of device noise is explicitly an interpretation, not an established universal benefit. Surrogate gradients here use a host/PyTorch loop and recorded hardware activity. This demonstration must not be labelled wholly autonomous on-chip online learning merely because BrainScaleS-2 contains programmable plasticity processors. Its temporal classification result does not itself establish a stable long-delay attractor.

## H8. BrainScaleS-2 interconnection, verified recent progress

**Source:** Joscha Ilmberger and Johannes Schemmel, *The BrainScaleS-2 multi-chip system: Interconnecting continuous-time neuromorphic compute substrates*. arXiv:2512.03781v1, 3 December 2025. Preprint version inspected.

**URL:** [versioned full text](https://arxiv.org/html/2512.03781v1).

**Locators:** Sections III–V, Figs. 4–5.

**Verified:** FPGA routing connects a measured four-chip prototype. Within-backplane chip-to-chip latencies below 1.3 microseconds are reported. Four-chip latency tests use three senders and one receiver. Fixed communication delay and jitter must be considered against accelerated neural time constants. The current FPGA module has four transceiver lanes; a larger lane count is an upgrade option.

**Limits:** supported backplane size is not evidence that every proposed larger configuration or long-range recurrent memory network has been demonstrated. This paper mainly establishes communication measurements. It does not replace the older source for weight/state physics, nor show that accelerated analog dynamics remove communication delay.

## H9. Dual memory pathways, current 2026 bridge with an important evidence limit

**Source:** Pengfei Sun, Zhe Su, Jascha Achterberg, Giacomo Indiveri, Dan F. M. Goodman and Danyal Akarca, *Algorithm–hardware co-design of neuromorphic networks with dual memory pathways*. Nature Machine Intelligence 8, 901–912, published 16 June 2026, version of record. DOI 10.1038/s42256-026-01255-3.

**URLs:** [journal](https://www.nature.com/articles/s42256-026-01255-3), [published full text at PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC13286998/).

**Locators:** Results, “Dual memory pathways for efficient temporal computation”; Fig. 4; Methods, “Experimental set-up”, especially “Implementation and evaluation methodology” and “Reference baselines results”.

**Verified:** a compact slow state summarizes recent activity and feeds input current back to faster spiking units. Proposed hardware uses two register slots for successive slow states, SRAM for weights and neuron states, and separate sparse/dense paths.

**Critical limit:** hardware results are post-layout simulations in 22FDX using QuestaSim and Innovus. They do not establish measured fabricated DMP silicon. Networks were trained offline. Comparisons normalize values from other papers and target specific implementations. The paper's loose phrase “hardware-based inference measurements” must be read with its explicit simulation method. Nature's page failed; the published PMC copy was inspected.

## Suggested explanation and unresolved checks

Recommended sequence: first distinguish a stored weight from a changing state; then show how feedback or a slow state preserves task information; then compare digital updates and physical analog evolution; finally discuss noise, precision, mismatch and timing as causes of memory error. The 2025 Loihi example supplies actual temporal computation. The 2026 DMP design supplies a current, explicit slow-state example while keeping simulated hardware results visible.

The guide should avoid a single winner ranking. Workload, required time scale, accuracy, mapping constraints, measurement boundaries and learning mode determine the useful comparison. No purchase recommendation or claim of the latest worldwide performance record follows from this small source set.

Unverified details to avoid asserting: a universal Loihi 2 state/weight bit width; current October 2026 open-access or retail terms for every platform; a measured stable Burak-style memory attractor on each platform; full end-to-end energy comparisons with matched interfaces and training; or physical nonvolatile retention for these SRAM/register-based examples.

## Execution checkpoints

- 2026-10-30 14:07:13 UTC: research start, estimated 6 to 8 minutes.
- 2026-10-30 14:10:01 UTC: report written; wall elapsed 2 minutes 48 seconds; 2 minutes 48 seconds since previous checkpoint. Narrow report check remained.
- 2026-10-30 14:10:20 UTC: source check complete; wall elapsed 3 minutes 7 seconds; 19 seconds since previous checkpoint. Report was shorter than the initial estimate because full primary texts were accessible and DYNAP was omitted. No manuscript, figure, build or acceptance record changed.

Awake execution time is not verified from Windows sleep/resume logs. No system-time change was observed in these clock readings. Token stats unavailable.
