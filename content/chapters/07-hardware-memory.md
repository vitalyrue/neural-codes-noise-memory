# A stored weight and a remembered value are different states {#ch:HARDWARE-MEMORY}

A silicon circuit can keep a connection strength unchanged while losing the angle it was asked to remember. It can also keep that angle while its individual electrical signals change. To compare electronic memory with the neural memory in Part I, we first need to identify what information each physical quantity represents. This chapter separates the connection settings, the changing state of each artificial neuron, and the value represented by their joint activity. That separation will let us ask what feedback actually preserves.

**Draft diagrams:** These unreviewed generated images may contain missing labels, incorrect numbers or misleading relationships. Use the chapter text and sources as the reference.

{{block:fig:DRAFT-MAP-CH14-A}}

{{block:fig:DRAFT-MAP-CH14-B}}

## A connection setting shapes activity. The activity can represent a cue {#sec:HARDWARE-MEMORY-ROLES}

Imagine giving a circuit a brief cue for an angle of $30^\circ$. After the cue ends, a connected group of artificial neurons remains active. We estimate the remembered angle from which neurons are active and how strongly. The experiment involves:

1. **Connection weights** determine how a signal from one neuron changes another neuron's state. A weight can be fixed throughout the trial.
2. **Neuron and synapse states** change during the trial. Examples include a voltage, a current left by recent inputs, or a number representing either quantity.
3. **The remembered angle** is a property of the joint state, recovered by a readout rule. It need not occupy one dedicated storage cell.

[Keeping the weights unchanged preserves the circuit's rule of operation. Keeping the cue available requires the resulting activity to preserve information about that cue.]{.key-statement} Training can change the first object. Remembering a new angle can change the second and third without any further training.

[[**Neuromorphic computing**]{.definition-term custom-style="Definition Term"} implements computations inspired by neural circuits using electronic systems organized around neurons, connections, events, or their dynamics.]{.definition-explanation} Some systems calculate neural states as digital numbers. Others use voltages and currents that evolve physically. A system can combine both approaches. The word alone does not tell us where its memory is stored or whether it demonstrates a biological memory mechanism.

[[**Working memory**]{.definition-term custom-style="Definition Term"}, in this Part, means keeping information about a recent input available for a later task.]{.definition-explanation} Persistent activity is one candidate mechanism. A slowly decaying state, a sequence of states, or an explicit digital buffer can also store recent information. We must specify the allowed delay and readout error before calling one implementation adequate.

<div class="publisher-worked-calculation publisher-fold-always">

**Example: the same weights can hold different angles.**

Suppose a ring of 32 artificial neurons has fixed local excitation and broader inhibition. A cue near neuron 3 creates a localized group of active neurons there. A later trial cues neuron 11 and creates a group near that location. The same connection weights support both trials. A decoder assigns an angle to the active group's center. If the group moves after the cue, the decoded angle changes even though every stored weight remains correct. This is an example constructed to illustrate the distinction. It is not a specification of a chip.

</div>

## Bits, capacitor voltages, and material conductances store different physical states {#sec:HARDWARE-MEMORY-STORAGE}

The neural model still needs a physical implementation. If the model has a variable called membrane voltage, a chip may store it as a binary number or as an actual circuit voltage. Those choices expose the computation to different errors. [[**Current**]{.definition-term custom-style="Definition Term"} is electric charge flowing per unit time, measured in amperes (coulombs per second).]{.definition-explanation} [[**Voltage**]{.definition-term custom-style="Definition Term"} is an electrical energy difference per unit charge, measured in volts (joules per coulomb).]{.definition-explanation}

A [[**capacitor**]{.definition-term custom-style="Definition Term"} stores separated electric charge. For fixed capacitance $C$, its stored charge $Q$ and voltage difference $V$ satisfy $Q=CV$.]{.definition-explanation} Charge is measured in coulombs and capacitance in farads (coulombs per volt). Supplying current changes $Q$, so it changes the stored voltage.

<!-- vale ai-tells.ParallelStaccato = NO -->
[[**Digital storage**]{.definition-term custom-style="Definition Term"} uses distinguishable physical ranges to represent discrete symbols, usually bits.]{.definition-explanation} In [[**static random-access memory (SRAM)**]{.definition-term custom-style="Definition Term"}, powered transistor feedback maintains one of two states representing a bit.]{.definition-explanation} Several bits can encode a weight or a changing neuron variable. Reliable bits do not imply unlimited numerical precision: a finite word represents only finitely many values.
<!-- vale ai-tells.ParallelStaccato = YES -->

[[**Analog state**]{.definition-term custom-style="Definition Term"} represents a model quantity through the magnitude of a physical variable, such as capacitor voltage.]{.definition-explanation} Input current changes stored charge and so changes voltage. Leakage changes that voltage during a quiet interval. Feedback or new input can oppose the leakage. In BrainScaleS-2, the membrane state evolves this way, while local SRAM stores the synaptic weights.[^hardware-pehle]

[[**Phase-change memory (PCM)**]{.definition-term custom-style="Definition Term"} stores information in a material's atomic arrangement, including the proportions of ordered and disordered regions, which affect its electrical resistance.]{.definition-explanation} Programming pulses heat the material. Its heating and cooling history changes the arrangement. [[**Conductance**]{.definition-term custom-style="Definition Term"} measures the current produced per unit applied voltage where current is approximately proportional to voltage. It is the inverse of resistance, the voltage required per unit current.]{.definition-explanation} Reading the conductance can recover a stored weight. Such storage is [[**nonvolatile**]{.definition-term custom-style="Definition Term"}: it can retain its state without continuous power, within its retention limits.]{.definition-explanation} Nonvolatile weights can remain after the changing neural state has disappeared.

The following choices locate the stored quantity before we compare complete machines.

<div class="table-responsive">

{{block:tbl:HARDWARE-STORAGE}}

</div>

Here [[**device mismatch**]{.definition-term custom-style="Definition Term"} means persistent differences between nominally identical circuit elements.]{.definition-explanation} It differs from fluctuations that vary from moment to moment. A fixed mismatch can create a repeatable bias. Changing noise can create a different trajectory on each trial. We will measure these separately.

## The stored state matters through the update it produces {#sec:HARDWARE-MEMORY-UPDATES}

To understand a machine's memory, follow one input through it. On a digital spiking processor, an arriving event identifies connections, their weights contribute to inputs, and a program updates stored neuron variables. Those variables determine whether to send further events. Loihi 2 provides local digital state and weight memory with programmable neuron and learning rules. SpiNNaker2 uses many processor cores whose software updates neural states stored with weights in local SRAM. Their event communication does not make every model variable evolve continuously in physical time.[^hardware-intel][^hardware-spinnaker]

In an analog neural circuit, an input can directly supply current to a capacitor. Transistors implement leakage and other responses as the voltage evolves. Digital circuits may still route the events and store the settings. [[**Mixed-signal hardware**]{.definition-term custom-style="Definition Term"} combines analog circuit variables with digital storage, communication, or calculation.]{.definition-explanation} The division of labor, rather than the label, determines which dynamics are physical and which are calculated.

PCM supplies a third use of physics. At a fixed, sufficiently small read voltage, a cell's current is approximately $I=GV$, where $I$ is current, $V$ is applied voltage, and $G$ is conductance, measured in siemens (amperes per volt). The stored conductance represents a weight. In Le Gallo and colleagues' chip, the duration of a read pulse represents the input magnitude. For one positive contribution with fixed $G$ and $V$, a pulse lasting $T$ seconds passes charge $Q\simeq GVT$. The contribution is proportional to the product of weight and input duration. Currents from several cells add, and the chip converts the combined current over time to digital values. Signed inputs and weights require additional polarity handling beyond this simple example.[^hardware-legallo]

[[**In-memory computing**]{.definition-term custom-style="Definition Term"} performs some operations where the values are stored, reducing the need to transfer them to a separate arithmetic unit.]{.definition-explanation} The 64-core PCM chip demonstrates this approach to neural-network inference, with digital processing also part of the system. Its weighted response results from both the stored material state and the applied input signal.

[A circuit's storage medium tells us how a value is retained between updates. Its update rule tells us how that value affects subsequent computation. Both are needed to explain memory.]{.key-statement} The next chapter follows the feedback in flip-flops, multilevel circuits, and rings of artificial neurons. Those examples will let us compare what happens when a remembered state is disturbed.

<!-- vale ai-tells.EmDashUsage = NO -->
[^hardware-pehle]: Pehle, C., et al. (2022). *The BrainScaleS-2 accelerated neuromorphic system with hybrid plasticity*. Frontiers in Neuroscience, 16, 795876. [Sections 2.1–2.3](https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full). [DOI](https://doi.org/10.3389/fnins.2022.795876).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.ContrastiveFormulas = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
[^hardware-intel]: Intel Labs. (2021). *Taking neuromorphic computing to the next level with Loihi 2*. Technology brief, pp. 5–7. [PDF](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf#page=5). This is an architecture description, not a current availability or performance comparison.
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.ContrastiveFormulas = YES -->

<!-- vale ai-tells.OverusedVocabulary = NO -->
[^hardware-spinnaker]: Scholze, S., et al. (2026). *The SpiNNaker2 chip: A many-core platform for flexible and scalable brain-inspired computing*. arXiv:2607.24396v1, July 27, 2026. [Section 4.4](https://arxiv.org/html/2607.24396v1#S4.SS4). Preprint. The inspected version places demonstrated SNN states and weights in SRAM.
<!-- vale ai-tells.OverusedVocabulary = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^hardware-legallo]: Le Gallo, M., et al. (2023). *A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference*. Nature Electronics, 6, 680–693. [DOI](https://doi.org/10.1038/s41928-023-01010-1). [Author manuscript, Sections I–II](https://arxiv.org/pdf/2212.02872#page=2). Detailed implementation descriptions refer to that manuscript version.
<!-- vale ai-tells.EmDashUsage = YES -->
