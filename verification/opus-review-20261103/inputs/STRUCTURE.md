# Current guide structure

Neural Codes, Noise, and Memory: A Guide to Three Papers

Scope: 4 Parts,21 teaching chapters,reading guide,glossary and references. Frozen from current reader sources.

### What the three papers establish (ch:READING-GUIDE)
Purpose: These neuroscience papers study memory, eye control, and navigation. Their settings are mathematical models of stored values, eye-movement and neural recordings from macaque monkeys, and recordings of location-dependent neural activity in rodents and bats. This reading guide explains each study’s question, methods, findings, and limits.
Source file: guide/00-reading-guide.md
- Variable neural signals must support reliable behavior (sec:READING-FIELD)
- Persistent activity can still lose memory accuracy (sec:READING-MEMORY)
- Eye drift points to a shared neural source (sec:READING-EYE)
- Smooth random maps explain the variety of place fields (sec:READING-PLACE)
- Electronic implementations make memory mechanisms testable (sec:READING-HARDWARE)
- Simulations separate the model from the evidence used to test it (sec:READING-SIMULATIONS)
- Starting knowledge and reading paths (sec:READING-START)
- Neural mechanisms and mathematical derivations answer different questions (sec:READING-MECHANISM-MATH)
- How to interpret the calculations and evidence (sec:READING-SCOPE)
- The original papers (sec:READING-PAPERS)

## Noise limits memory accuracy in continuous attractor models (part:MECHANISMS)
In a model neural circuit, a pattern of firing rates across many nerve cells can represent a remembered angle. Random spike timing can change that angle while activity persists. The central source, [Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109), derives how quickly accuracy can be lost and how well the value can be read. Chapters 1 and 2 establish the background. Chapters 3 and 5 develop the central diffusion and information results. Chapters 4 and 6 explain long-delay behavior and readout. Expanded examples and marked checks of printed formulas are guide-derived.

### 1. Patterns of variable spikes can represent a value (ch:FOUNDATIONS)
Purpose: Start from eye muscles and neural spikes, establish the dynamical model in Burak and Fiete (2012), Eqs. 7–9, then explain coding, variable spike counts and the network simulation that tests the theory. These foundations precede the stability and diffusion arguments.
Source file: guide/01-foundations.md
- Repeated spikes maintain eye muscle tension (sec:FOUNDATIONS-EYE-ACTION)
- Recurrent spikes renew decaying synaptic activity (sec:MEMORY-SPIKES)
- Patterns of firing rates represent a value (sec:FOUNDATIONS-SPIKES)
- A variable spike count at a fixed rate (sec:FOUNDATIONS-POISSON)
- Network simulations test whether spike noise moves a stored value (sec:FOUNDATIONS-SIMULATION)
- Shared neural signals and a biased command leave different signs in eye motion (sec:FOUNDATIONS-COVARIANCE)
### 2. Stable representations can accumulate error (ch:PERSISTENCE)
Purpose: Building on the eye anatomy and firing-rate code in Chapter 1, this chapter examines mechanical balance and sustained neural drive. It then separates changes in neuronal activity from changes in the value represented, showing how persistent activity can still accumulate memory error.
Source file: guide/01b-persistence.md
- Sustained muscle tension holds the eye against elastic restoring forces (sec:PERSISTENCE-EYE-MECHANICS)
- Stable activity with a vulnerable stored value (sec:FOUNDATIONS-ATTRACTOR)
- Independent steps with equal duration and variance give linear variance growth (sec:FOUNDATIONS-DIFFUSION)
- A fixed spatial map differs from a value that wanders over time (sec:FOUNDATIONS-RANDOMNESS)
### 3. Spiking noise produces diffusion along the memory attractor (ch:MEMORY-DYNAMICS)
Purpose: Starting from the neural model in Chapter 1, derive the weak-fluctuation approximation and follow small disturbances through the circuit to calculate diffusion of a stored value.
Source file: guide/02-memory-dynamics.md
- Many weak inputs allow a continuous approximation to spike noise (sec:MEMORY-WEAK-NOISE)
- The network's return flow determines the lasting memory change (sec:MEMORY-LINEARIZATION)
- Projecting spike fluctuations gives the diffusion coefficient (sec:MEMORY-DIFFUSION)
- Symmetric weights express diffusion through tuning curves (sec:MEMORY-SYMMETRIC)
### 4. Boundaries and drift change memory error over long delays (ch:MEMORY-LONG-DELAYS)
Purpose: In the memory-network model, random changes in a stored angle accumulate over time. This chapter extends the local spreading calculation to longer delays, where boundaries, angular wraparound, and systematic drift can change the size of the memory error.
Source file: guide/02b-memory-long-delays.md
- Long delay errors depend on boundaries and local diffusion (sec:MEMORY-LONG-TIME)
- A diffusion calculation does not determine systematic drift (sec:MEMORY-DRIFT-SCOPE)
- Figures distinguish memory motion from readout error and test diffusion (sec:MEMORY-FIGURES)
### 5. Spike information limits memory stability (ch:MEMORY-INFORMATION)
Purpose: A neuron receiving spikes from a memory circuit has access to information about the stored value. This chapter sets a bound on estimation error under the model’s assumptions and derives the constraint that spike information places on the circuit’s memory stability.
Source file: guide/03-memory-information.md
- Rate slopes and spike variability determine local information (sec:MEMORY-FI)
- Spike information sets a lower bound on memory diffusion (sec:MEMORY-BOUND)
- Improving persistence depends on what a comparison holds fixed (sec:MEMORY-COMPARISONS)
### 6. Readout accuracy depends on how a moving memory is observed (ch:MEMORY-READOUT)
Purpose: Reading spikes from a memory circuit takes time, during which its stored value can keep changing. This chapter calculates how much longer observation can help recover the value present at a recall cue, and explains why it cannot recover every earlier random displacement.
Source file: guide/03b-memory-readout.md
- Storage loss and readout error add under specific assumptions (sec:MEMORY-READOUT-SETUP)
- Equal weighting becomes harmful when observation lasts too long (sec:MEMORY-NAIVE)
- Accounting for diffusion makes readout improve toward a limit (sec:MEMORY-IDEAL)
- Limited access can make observation slower (sec:MEMORY-PARTIAL)
- Time scales and noise laws change the bound and its equality condition (sec:MEMORY-EXTENSIONS)
- Readout saturates, and one printed error bound needs qualification (sec:MEMORY-FIG3-AND-CAUTION)

## Eye motion and place fields constrain different parts of a neural code (part:OBSERVATIONS)
These studies connect neural activity to eye control in monkeys and location in rodents and bats. [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) supply the central shared-drive inference and a possible integrator explanation in Chapters 7 to 9. [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) supply the spatial model, field-size predictions, and supporting shape tests in Chapters 10 to 12. Chapter 13 is a guide-derived comparison of those results with Burak and Fiete (2012). The eye chapters begin with recordings and then test a possible neural source. The place chapters begin with a spatial input model and then test its field statistics.

### 7. Eye drift points to a shared neural drive (ch:EYE-DRIFT)
Purpose: Even when a monkey looks at a stationary spot, its eyes drift slightly. This chapter explains how paired measurements of eye angle and the firing of neurons that command eye muscles support a shared neural source of that drift, before considering a particular circuit mechanism.
Source file: guide/04-eye-drift.md
- From stored eye position to muscle action (sec:EYE-PATHWAY)
- The recordings pair one motor neuron with movement at a time (sec:EYE-RECORDINGS)
- A fitted model links movement to firing rate (sec:EYE-FORWARD-FIT)
- A calibrated filter predicts eye position from one cell's spikes (sec:EYE-INVERSE-FILTER)
- The measured correlation challenges independent motor noise alone (sec:EYE-SHARED-VARIANCE)
- Calibrated covariance estimates the common share of movement variance (sec:EYE-CHI)
### 8. Drift growth distinguishes diffusion from filtered white noise (ch:EYE-TIMING)
Purpose: Eye movements recorded during steady gaze in monkeys look different over short and long time intervals. This chapter uses their timing to distinguish fluctuations around a fixed command from accumulated changes in the command, while accounting for eye-position measurement error.
Source file: guide/04b-eye-timing.md
- Independent measurement error adds a constant offset to the MSD (sec:EYE-MEASUREMENT-NOISE)
- The MSD plateaus for filtered white noise but grows for filtered diffusion (sec:EYE-FILTERED-MSD)
### 9. A noisy memory circuit can produce eye drift (ch:EYE-CIRCUIT)
Purpose: A circuit that stores the intended eye angle is one possible source of fixational drift. This chapter follows the proposed model from interacting neurons through motor neurons and muscles to eye motion, and explains how delayed visual feedback can limit that motion.
Source file: guide/04c-eye-circuit.md
- A noisy integrator can reproduce drift after muscle filtering (sec:EYE-CIRCUIT-MODEL)
- Spike regularity and circuit parameters set the model's drift scale (sec:EYE-SCALING)
- The figures test shared drive, diffusion, and the full circuit model (sec:EYE-FIGURES)
- The evidence places shared drive upstream without identifying one circuit (sec:EYE-LIMITS)
### 10. Field counts and gaps reveal threshold and scale (ch:PLACE-FIELDS)
Purpose: Hippocampal place cells fire more at particular locations as an animal moves. This chapter introduces the rodent and bat recordings, then shows how a smooth random input that exceeds a firing threshold can produce several separate active regions for one cell.
Source file: guide/05-place-fields.md
- Thresholding a smooth Gaussian input produces place fields (sec:PLACE-GP)
- Upcrossings count fields, with an endpoint correction (sec:PLACE-KAC-RICE)
- Mean field and gap lengths separate threshold from scale (sec:PLACE-INFERENCE)
### 11. High peaks explain size laws across dimensions (ch:PLACE-SIZES)
Purpose: A place cell’s active regions can have different sizes on a route, across a floor, or in a flight volume. This chapter derives why the spatial model predicts different field-size distributions in one, two, and three dimensions, and identifies the high-threshold approximation used in that derivation.
Source file: guide/05b-place-sizes.md
- Near a high peak, the input is nearly parabolic (sec:PLACE-RARE-PEAKS)
- Geometry gives different size laws in each dimension (sec:PLACE-SIZE-LAW)
- Slices test spatial structure beyond field volume (sec:PLACE-SLICES)
- Why slopes at field boundaries are Rayleigh (sec:PLACE-SLOPES)
### 12. Holes and measurements test the spatial explanation (ch:PLACE-TESTS)
Purpose: Recordings show where a hippocampal cell is active as an animal moves through an environment. This chapter tests the spatial model against the shapes and arrangement of those regions, then asks what agreement can reveal about the inputs and connections that produce them.
Source file: guide/05c-place-tests.md
- Holes distinguish maps with the same field count (sec:PLACE-TOPOLOGY)
- What was fitted and what was tested (sec:PLACE-DATA)
- Random input weights can generate Gaussian maps (sec:PLACE-WIRING)
### 13. Spatial maps and memory dynamics need separate tests (ch:SYNTHESIS)
Purpose: The three papers address different links between nerve-cell activity and behavior: retaining a value, producing eye movement, and representing location. This chapter compares what the models and recordings establish, and separates supported connections from further questions about how a complete neural circuit would work.
Source file: guide/06-synthesis.md
- The three papers constrain maps, dynamics, and movement (sec:SYNTHESIS-QUESTIONS)
- A shared position error changes rates according to their tuning slopes (sec:SYNTHESIS-JOINT-CALCULATION)
  - Example: opposite rate changes from the same position error (sec:SYNTHESIS-COVARIANCE-EXAMPLE)
- Each model needs a test matched to its claim (sec:SYNTHESIS-EVIDENCE)
- Related studies change assumptions and leave circuit choices open (sec:SYNTHESIS-RELATED)
- A joint test would compare tuning maps with population fluctuations (sec:SYNTHESIS-NEXT)

## Neural memory in electronic hardware (part:HARDWARE)
Electronic circuits can store connection settings, changing neuron states, and values represented by a network. Von Neumann (1958) motivates this comparison. Chapters 14 and 15 connect physical storage with Seung (1996) and Burak and Fiete (2012). Chapter 16 examines the separate contributions of selected hardware studies through October 30, 2026. Chapter 17 develops guide-derived experiments using the three original papers. Each contribution is attributed in the Part introduction.

### 14. A stored weight and a remembered value are different states (ch:HARDWARE-MEMORY)
Purpose: A silicon circuit can keep a connection strength unchanged while losing the angle it was asked to remember. It can also keep that angle while its individual electrical signals change. To compare electronic memory with the neural memory in Part I, we first need to identify what information each physical quantity represents. This chapter separates the connection settings, the changing state of each artificial neuron, and the value represented by their joint activity. That separation will let us ask what feedback actually preserves.
Source file: guide/07-hardware-memory.md
- A connection setting shapes activity. The activity can represent a cue (sec:HARDWARE-MEMORY-ROLES)
- Bits, capacitor voltages, and material conductances store different physical states (sec:HARDWARE-MEMORY-STORAGE)
- The stored state matters through the update it produces (sec:HARDWARE-MEMORY-UPDATES)
### 15. Discrete restoration and continuous drift produce different memory errors (ch:HARDWARE-DYNAMICS)
Purpose: A circuit can remain active for seconds even when its individual voltages decay in milliseconds. The explanation is feedback: activity supplies new input before old input disappears. But long-lived activity does not by itself identify what is being preserved. This chapter first explains how feedback extends a time scale, then distinguishes a restoring discrete memory from a freely changing continuous one. Measured silicon circuits show why this distinction matters beyond a mathematical model.
Source file: guide/08-hardware-dynamics.md
- Feedback can extend persistence beyond a component's decay time (sec:HARDWARE-DYNAMICS-FEEDBACK)
- A bit corrects small displacements. A continuous memory preserves some of them (sec:HARDWARE-DYNAMICS-ERRORS)
- Silicon experiments distinguish discrete persistence from graded representation (sec:HARDWARE-DYNAMICS-EVIDENCE)
### 16. Neuromorphic chips choose where physics performs the calculation (ch:NEUROMORPHIC-SYSTEMS)
Purpose: Suppose we want to study how a noisy network retains an angle. One machine can calculate every state update as arithmetic. Another can let capacitor voltages perform part of the dynamics. A third can use material conductances to multiply inputs by stored weights. The scientific choice is which physical effects we want to control, measure, or exploit. This chapter compares these implementations and then examines recent demonstrations of memory and learning.
Source file: guide/09-neuromorphic-systems.md
- Digital and analog implementations expose different parts of the neural model (sec:NEUROMORPHIC-SYSTEMS-ARCHITECTURES)
- Recent results improve temporal computation, adaptation, and device stability (sec:NEUROMORPHIC-SYSTEMS-ADVANCES)
- Explicit slow memory is a current design choice, with distinct costs (sec:NEUROMORPHIC-SYSTEMS-LIMITS)
### 17. Memory experiments must separate device error from network dynamics (ch:HARDWARE-TESTS)
Purpose: After a circuit receives an angle cue, its later estimate may be wrong because the state wandered, because unequal connections pull it toward another angle, or because the observer reads it poorly. One accuracy score combines these causes. The controlled tests below connect these errors to physical parameters. The protocol and reduced models below are proposed tools for reasoning about these experiments, not results already demonstrated on every platform in the previous chapter.
Source file: guide/10-hardware-tests.md
- Repeated cue-and-delay trials separate drift from random spreading (sec:HARDWARE-TESTS-PROTOCOL)
- Physical parameters act through decay, bias, and noise projection (sec:HARDWARE-TESTS-PARAMETERS)
- Matching time and readout is necessary to compare memory accuracy (sec:HARDWARE-TESTS-COMPARISON)

## Simulations connect model assumptions to measurable outcomes (part:SIMULATIONS)
[Burak and Fiete (2012)](https://doi.org/10.1073/pnas.1117386109) test memory diffusion in spiking networks. [Ben-Shushan et al. (2022)](https://doi.org/10.1038/s41467-022-29201-y) connect a simulated neural command to eye motion. [Mainali et al. (2025)](https://doi.org/10.1016/j.neuron.2025.01.017) generate spatial maps and compare their fields with recordings. This Part explains the methods, measurements, and software behind those studies, then gives a guide-derived route for checking a reproduction.

### 18. Network simulations test how random spikes move a stored value (ch:SIMULATING-MEMORY)
Purpose: Burak and Fiete (2012) derive memory diffusion from assumptions about recurrent connections and random spike timing. To test that prediction, they simulate individual spikes and measure how the stored value moves. The central result remains an analytical bound. The simulations check its predicted motion in different network designs, including the limits imposed by an angular coordinate.
Source file: guide/11-simulating-memory.md
- A simulation renews the same synaptic state that the theory approximates (sec:SIMULATING-MEMORY-STATE)
- Ring trajectories test both the diffusion rate and the effect of angular boundaries (sec:SIMULATING-MEMORY-RING)
- Other network designs test which conclusions depend on the ring (sec:SIMULATING-MEMORY-CONTROLS)
- A plotted analytical curve is different from a network simulation (sec:SIMULATING-MEMORY-OUTPUTS)
### 19. Eye simulations connect a noisy neural command to measured motion (ch:SIMULATING-EYE)
Purpose: Ben-Shushan et al. (2022) ask whether fluctuations in a neural memory circuit can explain the small eye movements that continue during fixation. Their simulation must turn a changing neural command into muscle action and eye position. It must also produce signals that can be analyzed like the recordings. The paper's central evidence combines a shared-source inference from data with a model showing that a noisy integrator can account for the observed motion.
Source file: guide/12-simulating-eye-drift.md
- Recorded data constrain the question before the model generates a trajectory (sec:SIMULATING-EYE-DATA)
- The generated command acts through spikes, muscle response, and delayed feedback (sec:SIMULATING-EYE-PATH)
- Controls test which stage can explain the observed fluctuations (sec:SIMULATING-EYE-CONTROLS)
- Public MATLAB code and recordings support different reproduction tasks (sec:SIMULATING-EYE-TOOLS)
### 20. Random spatial maps test the statistics of place fields (ch:SIMULATING-PLACE)
Purpose: Mainali et al. (2025) ask whether one statistical model can explain the many firing regions observed in hippocampal place cells across different environments. Their simulation generates a cell's firing-rate map over space and measures the active regions. Position is the independent variable. The generated map is fixed while it is analyzed, so this simulation addresses spatial coding rather than how a neural circuit retains a position over time.
Source file: guide/13-simulating-place-fields.md
- A smooth random input becomes a firing map after thresholding (sec:SIMULATING-PLACE-GENERATE)
- Fitted summaries and additional comparisons supply different evidence (sec:SIMULATING-PLACE-FIT)
- Field detection and preprocessing change what the simulation is asked to match (sec:SIMULATING-PLACE-MEASURE)
- The released tools generate maps and analyze data, with access limits (sec:SIMULATING-PLACE-TOOLS)
### 21. Reproduction depends on the model, numerical method, and measurement (ch:SIMULATION-TOOLS)
Purpose: A simulated eye trace can look convincing while answering the wrong question. It may use different spike statistics, a different muscle response, or a different definition of displacement from the experiment. Reproducing a result requires matching those choices before comparing curves. This chapter collects the practical decisions shared by the three papers and identifies tools for making those decisions visible.
Source file: guide/14-simulation-tools.md
- The original code and a teaching reconstruction serve different purposes (sec:SIMULATION-TOOLS-ROUTES)
- Tools should match the operation being tested (sec:SIMULATION-TOOLS-SOFTWARE)
- Time and space resolution must preserve the modeled physics (sec:SIMULATION-TOOLS-RESOLUTION)
- A useful reproduction saves the choices that determine the conclusion (sec:SIMULATION-TOOLS-RECORD)
### Glossary (ch:GLOSSARY)
Purpose: These short definitions support lookup after the explanations and examples in the main chapters.
Source file: guide/glossary.md
- Physical implementation and neural memory (sec:GLOSSARY-HARDWARE)
### References (ch:REFERENCES)
Purpose: Entries follow their first use in the reading path and chapters. The paper's supporting information shares its main article entry. The author's mathematical notes are listed separately because the guide also uses them for the excursion derivation.
Source file: guide/references.md