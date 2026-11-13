# Electronic feedback circuits store and transform neural-like states {#ch:ELECTRONIC-ARCHITECTURES}

How can a circuit remember a value after the signal that set it has ended? In Part I, interconnected neurons keep an activity pattern going, and the pattern can represent an angle. Electronic circuits can also use feedback to maintain states. Here we follow that shared idea from a two-state flip-flop to a ring of artificial neurons, and ask which properties actually carry over.

Hassabis and colleagues' review *Neuroscience-Inspired Artificial Intelligence* proposes a two-way exchange: findings about brains can suggest algorithms for AI, while AI models can give neuroscience ideas and tools to test. The authors discuss shared computational principles, not a claim that every useful electronic circuit reproduces a biological mechanism.[^arch-hassabis] The comparison in this chapter is likewise a guide-derived explanation of circuit organization, supported by the separate experiments cited below.

For each architecture, ask three questions: **what physical state changes, what does feedback do, and what value can be read from the state?** We start with circuits familiar from electronics, then connect them to spikes, synaptic activation and network memory. Folded examples give a closer look at particular devices. The earlier [comparison of stored weights and activity](ch-hardware-memory.html#sec-hardware-memory-roles) explains why the three roles must be kept separate.

## Electronic architectures can share neural organization while storing different things {#sec:ELECTRONIC-OVERVIEW}

[[**Feedback**]{.definition-term custom-style="Definition Term"} occurs when a change in a circuit's output affects its later input.]{.definition-explanation} Whether feedback restores a state, changes it repeatedly, or supports a family of states depends on the connections and component responses.

In the neural model, the connection $W_{ij}$ specifies how activation from neuron $j$ affects neuron $i$. The changing activation $s_j$ reflects the accumulated, decaying effect of spikes. A population pattern of these changing activations can represent a value $\theta$. In an electronic circuit the corresponding objects might be a programmed conductance, a capacitor voltage or current, and a value decoded from several signals. Which physical quantity plays which role must be checked for each design.

The list below is a reading map, not a claim that the circuits have identical equations or are biological models. A flip-flop and multilevel memory show how feedback can hold *discrete* states. An oscillator and a ring attractor illustrate different ways a displacement can persist.

- **Flip-flop:** feedback restores one of two states; the output indicates a bit.
- **Multilevel memory:** feedback restores one of several preferred voltage levels; the output indicates a discrete level.
- **Recurrent ring:** an activity bump can persist at different positions; its position indicates a direction.
- **Oscillator:** feedback sustains a cycle; its phase gives the position within that cycle and normally advances with time.
- **Pulse-based neuron circuit:** graded input can set pulse timing or rate; a circuit state can accumulate and leak input.

The first two are useful comparisons, not automatically neural networks. The ring is a network when its connected units and their dynamics implement the stated interactions. We now follow the feedback in each case.

## A flip-flop maintains one of two states through feedback {#sec:ELECTRONIC-FLIPFLOP}

Two inverting stages can be cross-coupled so that each stage's output is the other's input. An inverting stage responds to a high input with a low output and to a low input with a high output. If the first output is high, it drives the second low; that low output in turn supports the first being high. The reverse arrangement is also possible. A setting signal selects a state; after it is removed, powered feedback can maintain the selected pattern. The stored bit is read from one output.

A small disturbance is corrected if the new state is still within the set of states that return to the original one. This set is its [[**region of attraction**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} A sufficiently strong disturbance or an input intended to switch the device can move it to the other state. [[**Bistability**]{.definition-term custom-style="Definition Term"} means the same fixed circuit conditions support two locally stable states.]{.definition-explanation} The two coupled stages are an analogy for recurrent neural activity, but a binary latch does not by itself retain an arbitrary angle. [Chapter 15](ch-hardware-dynamics.html#sec-hardware-dynamics-errors) develops the stability comparison.[^arch-seung]

Giulioni and colleagues built a recurrent electronic network of spiking artificial neurons that exhibited low and high activity states. It is a closer network analogy than a two-stage latch: many artificial neurons participate in maintaining each state. Their experiment examined persistent activity and noise-related transitions, rather than storage of a continuously variable angle.[^arch-giulioni]

## Multilevel circuits hold several preferred states {#sec:ELECTRONIC-MULTILEVEL}

The same question extends beyond two levels: could feedback hold one of several voltages? Alhawari and Perrott fabricated a CMOS circuit with ten stable operating points. An input first sets a voltage; when its input switch is opened, nonlinear feedback moves the voltage toward a nearby stable level. The retained voltage identifies a level while the circuit is powered.[^arch-multilevel]

<div class="publisher-worked-calculation publisher-fold-always">

**Example: reading a voltage between two levels.**

Imagine adjacent preferred levels at 0.40 V and 0.50 V. If a setting input leaves the state in the first level's region of attraction, the feedback carries it toward 0.40 V; from the second region it moves toward 0.50 V. The boundary between regions depends on the circuit and need not be exactly halfway. These values illustrate the mechanism and are not measurements from the ten-level device.

</div>

Ten levels can distinguish more values than two, but each stable point has a region that pulls nearby voltages toward it. Increasing the number of discrete levels does not alone create the ideal continuous family of steady states used in the 2012 model. In principle, a sufficiently large noise disturbance can cause a jump between levels; this general switching mechanism differs from the local wandering of a neutral memory coordinate. The ten-level study is cited here for its stable levels, not as a measurement of those jumps.

## Ring networks store a value in the position of an activity bump {#sec:ELECTRONIC-RING}

Suppose artificial neurons are assigned preferred directions around a circle. Each excites nearby units, while inhibitory interactions suppress more distant activity. A brief cue can activate a localized group. Recurrent input then helps that group maintain its activity after the cue is removed; a suitable movement signal can shift the group. The **position of the bump** represents direction. The weights describe how units influence one another; they are not the angle itself.

Massoud and Horiuchi demonstrated a physical head-direction system with a 32-neuron ring, testing bumps initialized at 32 indexed locations. Some connections were routed through an external digital processor. Kreiser and colleagues implemented a recurrent head-direction network on the mixed analog and digital ROLLS neuromorphic chip. In the latter experiment, movement signals shifted the activity and a visual landmark corrected accumulated heading error. Device mismatch and movement-estimation error both contributed to the error; the experiment did not isolate the diffusion coefficient of the 2012 model.[^arch-massoud][^arch-kreiser]

The analogy to [Burak and Fiete's ring model](ch-memory-dynamics.html#sec-memory-linearization) concerns the organization of feedback and the encoded coordinate. A ring layout alone does not guarantee a stable bump or a continuum. Real circuits have finite units, unequal components and noise; they can favor particular positions. A set of measured positions is evidence for a graded representation at that resolution, not proof of an exact continuous attractor.

## Oscillator phase can wander while oscillation persists {#sec:ELECTRONIC-OSCILLATOR}

A multivibrator or a suitable ring of inverting stages can repeatedly switch rather than settle to a fixed state. Its **phase** describes where it is in one cycle. Even in a perfect oscillator, phase advances: after one period it returns to the same point in the cycle. A timing disturbance can make later cycles arrive early or late relative to a reference.

This resembles the neural memory's neutral direction, a direction in which a displacement is not driven back to its previous value: the system can return toward its usual cycle after a disturbance while keeping a phase shift. In an ideal continuous attractor, a bump can return toward its usual shape while retaining a shift in position. The comparison concerns the *error relative to the expected phase*, because oscillator phase also advances without noise. It does not make a ring oscillator a stationary ring-attractor memory.

Electronic oscillator research studies timing fluctuations using phase noise and jitter, the variability in the timing of oscillator events. Hajimiri, Limotyrakis and Lee analyze phase noise in ring oscillators and compare their theory with measurements. The noise sources and conditions must be identified before treating phase variance as a simple diffusion law.[^arch-phase]

## Pulse trains and analog states implement different neural variables {#sec:ELECTRONIC-SPIKES}

An individual electronic pulse is a brief event. A **pulse rate** describes the number of pulses per unit time, averaged over an interval or defined as a conditional expected rate. Many pulses, each contributing charge to a capacitor, can produce a changing voltage. Between pulses, leakage or a designed discharge path reduces that voltage. A transistor can convert voltage into a current or affect the timing of later pulses.

This gives a physical reading of the chain in [Chapter 1](ch-foundations.html): spikes are events; $r_i$ is their conditional firing rate; $s_i$ is the modeled accumulation of their decaying synaptic effects. These roles can be implemented by different circuit variables. A short observation can have no pulses even at a positive expected rate, and a long-time average can conceal pulse timing and shared fluctuations.

Some transistors can also hold several programmable conductance levels. Those levels often represent synaptic weights $W$, not the moment-to-moment neuron state $s$ or the stored angle $\theta$. Other devices exhibit neuron-like integration and firing. In a 2022 anti-ferroelectric transistor study the device was measured, while the larger digit-recognition network using its properties was evaluated in simulation.[^arch-device] A multilevel device is therefore a possible component, not proof that a recurrent memory network has been built.

The [earlier chip comparison](ch-neuromorphic-systems.html#sec-neuromorphic-systems-architectures) locates these roles in different machines. Loihi 2 and SpiNNaker 2 update represented neural states digitally; BrainScaleS-2 uses analog circuit dynamics for membrane states and digital storage for weights. In phase-change computing, material conductances can store weights while surrounding circuits or a host perform other operations. These hardware choices do not by themselves establish that a particular network implements a continuous attractor.

## Drift and Fisher information measure different limits on memory {#sec:ELECTRONIC-READOUT}

If an electronic bump is meant to preserve an initial direction, repeat the same setting and delay many times. Decode its position after each delay. The mean displacement shows repeatable bias; the spread across trials shows variability. When a local diffusion model with constant $D$ applies, its predicted displacement variance is $2Dt$. Device mismatch can instead create preferred positions or systematic motion. Measurement noise and movement-input errors require separate controls. The [hardware experiment](ch-hardware-tests.html#sec-hardware-tests-protocol) develops these distinctions.

[[**Fisher information**]{.definition-term custom-style="Definition Term"} describes how well the probability distributions of measured signals distinguish nearby values of a parameter.]{.definition-explanation} To estimate it for an electronic ring, one could record the available outputs at nearby controlled bump positions and model their variability. The result depends on which signals are observed and for how long. It concerns the **current** represented position; diffusion concerns how that position changes from its initial value.

Burak and Fiete relate spike information to memory diffusion for their specified neural model; see the [information-bound derivation](ch-memory-information.html#sec-memory-bound). The same calculation is not automatically a bound for all transistor circuits: the dynamics, noise statistics, observations and time scales must be matched first. Likewise, Ben-Shushan and colleagues' [eye measurements](ch-eye-drift.html) test an explanation of biological motor variability; a chip analogy cannot establish the eye circuit's wiring. Mainali and colleagues study [spatial firing-field statistics](ch-place-fields.html), not whether a ring circuit autonomously retains a position. A population pattern can encode a variable in both settings, but those are different experimental claims.

The architectural question to carry forward is therefore concrete: **which physical state represents the value, which feedback acts on it, and which disturbances can the circuit correct?**

[^arch-hassabis]: Hassabis, D., Kumaran, D., Summerfield, C., & Botvinick, M. (2017). *Neuroscience-inspired artificial intelligence*. Neuron, 95(2), 245–258. [DOI](https://doi.org/10.1016/j.neuron.2017.06.011); [author paper](https://www.columbia.edu/cu/appliedneuroshp/Papers/out.pdf).

[^arch-seung]: Seung, H. S. (1996). *How the brain keeps the eyes still*. Proceedings of the National Academy of Sciences, 93(23), 13339–13344. [DOI](https://doi.org/10.1073/pnas.93.23.13339).

[^arch-giulioni]: Giulioni, M., Camilleri, P., Mattia, M., Dante, V., Braun, J., & Del Giudice, P. (2012). *Robust working memory in an asynchronously spiking neural network realized with neuromorphic VLSI*. Frontiers in Neuroscience, 5, 149. [Article](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2011.00149/full).

[^arch-multilevel]: Alhawari, M., & Perrott, M. H. (2014). *A clockless, multi-stable, CMOS analog circuit*. IEEE International Symposium on Circuits and Systems, 1764–1767. [Paper](https://cppsim.com/Publications/CNF/alhawari_iscas14.pdf), especially Figs. 5 and 8.

[^arch-massoud]: Massoud, T. M., & Horiuchi, T. K. (2011). *A neuromorphic VLSI head direction cell system*. IEEE Transactions on Circuits and Systems I, 58(1), 150–163. [DOI](https://doi.org/10.1109/TCSI.2010.2055310).

[^arch-kreiser]: Kreiser, R., Cartiglia, M., Martel, J. N. P., Conradt, J., & Sandamirskaya, Y. (2018). *A neuromorphic approach to path integration: A head-direction spiking neural network with vision-driven reset*. [Paper](https://services.ini.uzh.ch/admin/extras/doc_get.php?id=71960), architecture and robotic experiments.

[^arch-phase]: Hajimiri, A., Limotyrakis, S., & Lee, T. H. (1999). *Jitter and phase noise in ring oscillators*. IEEE Journal of Solid-State Circuits, 34(6), 790–804. [Author repository](https://authors.library.caltech.edu/records/1hw2y-5p770).

[^arch-device]: Cao, R., Zhang, X., Liu, S., et al. (2022). *Compact artificial neuron based on anti-ferroelectric transistor*. Nature Communications, 13, 7018. [Article](https://www.nature.com/articles/s41467-022-34774-9). Device measurements and network simulation are described separately in Results and Methods.
