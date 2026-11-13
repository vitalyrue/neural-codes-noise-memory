# Part III device and memory sources

Research checkpoint started: 2026-10-30 14:07:23 UTC. Sources accessed: 2026-10-30. Research only, no manuscript or figure changes.

Recommended set: Le Gallo et al. (2023) for integrated PCM computation; Ortner et al. (2025) for learning with recurrent networks on physical PCM; Wang et al. (online 2025, issue 2026) for a materials change that reduces drift. Richter et al. (2024) supplies the contrasting capacitor and digital configuration example.

## Verified primary papers and safe claims

### D1. Le Gallo et al., 2023

Manuel Le Gallo, Riduan Khaddam-Aljameh, Milos Stanisavljevic et al., **A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference**, *Nature Electronics* 6, 680–693 (2023). [DOI](https://doi.org/10.1038/s41928-023-01010-1). Published 10 August 2023. [Author manuscript](https://arxiv.org/pdf/2212.02872).

- **Measured hardware:** a fabricated 64-core chip, each core with a 256 by 256 PCM matrix. Final publisher abstract confirms these dimensions and 14 nm CMOS.
- **Memory location:** phase configuration sets cell conductance; multiple cells encode signed weights. Matrix products use electrical reads, followed by digital processing. Author manuscript sections I–II, pp. 2–3.
- **Precision limit:** programming error, read noise, converter errors and wire effects differ. Conductance drift changes weights over time; common rescaling cannot remove differences between cells. Section IV, pp. 4–5, Fig. 2.
- **Scope:** inference hardware, including digital LSTM processing. The author manuscript retains off-chip layer transfer and some operations. Section V, p. 5, Conclusions, p. 6. Do not describe it as a self-contained persistent activity experiment.
- **Energy claim:** keeping weights local can reduce repeated movement. No universal energy advantage is established. No benchmark numbers are recommended here.

Version boundary: the detailed page references above are to the December 2022 author manuscript. The final publisher page was checked for identity and abstract, but its full text was not available through that page. Do not transfer manuscript precision or performance numbers into the guide as final-paper specifications.

### D2. Ortner et al., 2025

Thomas Ortner, Horst Petschenig, Athanasios Vasilopoulos, Roland Renner, Špela Brglez, Thomas Limbacher, Enrique Piñero, Alejandro Linares-Barranco, Angeliki Pantazi and Robert Legenstein, **Rapid learning with phase-change memory-based in-memory computing through learning-to-learn**, *Nature Communications* 16, 1243 (2025). [DOI](https://doi.org/10.1038/s41467-025-56345-4). Published 1 February 2025. [Final PDF](https://www.nature.com/articles/s41467-025-56345-4.pdf?error=cookies_not_supported).

- **Measured advance:** physical PCM weight adaptation supports a recurrent spiking network producing robotic arm commands after one task-specific update. Meta-training is done in software. Results, motor-command section, pp. 7–10, Figs. 4–5.
- **Memory location:** PCM conductances encode input and recurrent weights. This is weight storage, not direct storage of membrane voltage in PCM.
- **Host boundary:** Methods, “Deploying models on the neuromorphic hardware,” p. 11, explicitly places MVMs on two hardware units and all other operations on the host. Do not call this an autonomous physical recurrent attractor.
- **Device limits:** iterative read/write verification addresses stochastic programming; local digital affine correction addresses drift. Methods, “Neuromorphic hardware,” p. 11.
- **Research status:** demonstrated task adaptation and robot use, not a general long-term memory guarantee. No whole-system energy or endurance claim is recommended.

### D3. Wang et al., online 2025, issue 2026

Xiaozhe Wang, Ruobing Wang, Suyang Sun et al., **Amorphous phase-change memory alloy with no resistance drift**, *Nature Materials* 25, 456–462 (2026). [DOI](https://doi.org/10.1038/s41563-025-02361-0). Published online 1 October 2025; March 2026 issue. [Final PDF](https://www.nature.com/articles/s41563-025-02361-0.pdf?error=cookies_not_supported).

- **Measured advance:** CrTe3 films show very small measured resistance drift across tested temperatures; electrically reset confined devices also show low drift. Abstract; “Electrical measurement of CrTe3 devices,” pp. 459–460, Figs. 2–3. Prefer “very low measured drift” over an unlimited no-drift promise.
- **Distinct physics:** calculations connect stable local atomic arrangements with reduced structural relaxation. “Design of molecular-glass-like a-PCM,” pp. 457–458. The structural explanation combines measurements and modelling.
- **Important separation:** electrical switching/cycling and deterministic multilevel programming are different demonstrations. The latter uses laser programming with electrical readout, p. 460 and Extended Data Fig. 4. It is not a demonstrated dense, electrically programmed multilevel processor.
- **Limits:** nanoscale multilevel operation, endurance beyond a million cycles and large-crossbar variability remain work to do. Closing discussion, p. 461.
- **Retention caution:** reduced drift is not unlimited retention or elimination of programming noise. No chip-wide energy claim follows.

### D4. Richter et al., 2024, supporting contrast

Ole Richter, Chenxi Wu, Adrian M. Whatley, German Köstinger, Carsten Nielsen, Ning Qiao and Giacomo Indiveri, **DYNAP-SE2: a scalable multi-core dynamic neuromorphic asynchronous spiking neural network processor**, *Neuromorphic Computing and Engineering* 4, 014003 (2024). [DOI](https://doi.org/10.1088/2634-4386/ad1cd7). [Author PDF, version 2](https://arxiv.org/pdf/2310.00564v2). Bibliography verified through the authors' [university record](https://research.rug.nl/en/publications/dynap-se2-a-scalable-multi-core-dynamic-neuromorphic-asynchronous/).

- **Physical state:** the somatic circuit integrates using capacitor voltage and transistor currents; analog state changes continuously. Author version section 4.1, pp. 12–14.
- **Digital memory:** SRAM/CAM holds connection configuration, not the same thing as the evolving membrane state. Sections 5–6.1.
- **Measured circuit limits:** leak current limits an isolated neuron's hold time; longer biological time constants carry a power cost. Section 4.1.2, p. 13. No numeric specification is needed for the proposed comparison.
- **Status:** characterized mixed-signal research hardware. This paper alone does not establish a specific Burak-like attractor result.

## Suggested explanation and research bridge

The following is engineering interpretation, not a theorem claimed by the papers:

| Physical quantity | What it can represent | What must be checked |
|---|---|---|
| PCM phase configuration, read as conductance | A trained or adapted synaptic weight | Drift, read noise, programming spread, finite precision, write cost and wear |
| Capacitor charge, read as voltage or transistor current | A membrane or synaptic state changing during computation | Leakage, thermal noise, circuit mismatch, power and time constants |
| A powered SRAM latch | Discrete weights, routing configuration or a digital state variable | Power loss, bit precision and the cost of moving/updating words |
| Recurrent population activity | The remembered value carried by a network trajectory or attractor | Feedback stability, accumulated noise, systematic bias and decoding error |

SRAM retains a bit through active transistor feedback while powered. A capacitor instead stores charge on a node. A PCM cell retains a material configuration without continuous neuron-like firing. These are different mechanisms even when all are called memory. A system can use all three.

For neurophysics, ask whether a weight error changes the recurrent dynamics: fixed unequal weights can bias the remembered value; noise can spread it; slow drift can change that bias over time. Those are proposed questions for a controlled experiment, not measurements supplied by D1–D4. Compare errors in the decoded state over time, with the same task and noise assumptions, rather than comparing headline operations per watt.

Retention means keeping a useful state while waiting. Drift means a systematic change in a measured value over time. Endurance concerns repeated writes. A low-drift result does not settle retention under all conditions, write endurance or circuit noise. Increasing precision, calibration or repeated reads can cost energy and time, so assess the complete implementation.

Do not infer a universal RAM capacity limit, or a bound on every memory device, from Burak's model-specific persistent activity analysis. Nonvolatile weights do not by themselves retain a network's current remembered value. A saved weight matrix can survive power loss while the active state disappears.

Spintronic and ferroelectric examples were omitted: the verified PCM and capacitor examples already supply the needed distinction, and an extra device list would not strengthen this bridge.

## Access and timing notes

Nature's standard URLs intermittently redirected to its cookie service; adding `?error=cookies_not_supported` exposed the final Ortner and Wang papers. The final Le Gallo abstract and the author manuscript were checked separately. No final-paper performance metrics were inferred from an older manuscript. D4 details use the explicitly linked author version.

An early progress message estimated the wrong clock time and elapsed duration. It was corrected immediately using the tool clock. Persisted checkpoints are authoritative. Start 14:07:23 UTC; checked clock 14:07:59 UTC; checked clock 14:08:45 UTC. System sleep/resume logs were not inspected, so awake execution time is unverified.

Memory was consulted only to establish the existing guide's scope and avoid confusing source research with release or figure acceptance: MEMORY.md lines 64–104, rollout 01a16429-56cd-7531-92ce-552e368634a9. All scientific claims above were verified against current primary sources. Token stats unavailable.

Completed checkpoint: 2026-10-30 14:09:37 UTC. Wall-clock elapsed since start: 2 minutes 14 seconds. Since previous persisted clock checkpoint (14:08:45): 52 seconds. Awake execution time unverified. Remaining work in this subtask: none.
