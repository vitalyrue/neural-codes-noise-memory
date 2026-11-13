# Eye chapters: stage 1 independent context review

Completed: 2026-10-28, Asia/Jerusalem. Report only; no manuscript edits.

## Scope and method

Audience: undergraduate calculus, basic probability and linear algebra; no neuroscience assumed. Fresh open read of all prose, callout titles, footnotes, captions, alt text and table cells in `04-eye-drift.md/.yaml`, `04b-eye-timing.md/.yaml`, and `04c-eye-circuit.md/.yaml`. No historical review or current-state findings read. Read foundations' spike/synapse/tuning/population/variability and covariance explanations, and the persistence definitions and teaching example, before deciding that a term needed more explanation. The assigned chapters' argument runs from paired recordings, to a shared-variance estimate, to timing, to a possible circuit; that order is sound for this task.

Rules: course-study-guide-builder SKILL.md and pedagogy-language-contract.md, especially the audience baseline, ordinary words with technical meanings, system setup, actors and objects, first reasoning-dependent use, connected reading, and strongest reasonable reading requirements. This is a targeted context review, not a mathematical proof audit, complete source correctness audit, artwork inspection, build check or release acceptance. The source extracts were sufficient for the findings below; no web research was needed.

Result: four small local repairs recommended. No wholesale rewrite or added glossary is needed. The existing text already teaches most requested distinctions well. Findings 2 and 3 concern local clarity after adequate earlier basic teaching, not absent book-wide definitions.

## 1. Complete the experimental setting before angles are used

- File/section: `04-eye-drift.md`, EYE-RECORDINGS, line 25; corresponding YAML section summary if synchronized.
- Original: “The animals first fixated a stationary target and then tracked a moving target. A wire search coil on one eye measured eye position while an electrode recorded one neuron's spikes.”
- Missing context: the monkeys' heads were held still and the target was a spot on a monitor. This matters because eye angle and a target's location on a screen are different objects; “eye position” is later expressed in degrees. Species and sample size are already supplied and should remain.
- Proposed repair: “With their heads held still, the monkeys first looked at a stationary spot of light on a monitor and then followed the moving spot. A wire search coil on one eye measured the eye's angle while an electrode recorded one neuron's spikes.” Keep the existing statement of two male rhesus macaques and the remaining recording limitations. “Fixated” can remain if the plain description accompanies it.
- Source support: main-text.txt lines 744–758, main paper p. 9, Behavioral task and recordings: head restrained; spots of light on a monitor; coil on one eye; electrode in brainstem. The angular interpretation is consistent with the main paper's eye-position units and the guide's forward fit.
- Later explanation: EYE-FORWARD-FIT line 50 supplies degrees, but does not supply head restraint or monitor setting. No need to repeat these details there.

## 2. State which cells act on which, and distinguish held gaze from movement direction

- File/section: `04c-eye-circuit.md`, EYE-CIRCUIT-MODEL, line 9; corresponding YAML section summary.
- Original: “There are two populations, with excitation within each and inhibition between them. Their firing increases for opposite directions of gaze. This supplies the recurrent interaction needed to maintain a range of stored positions.”
- Missing context: “populations” refers to two groups of integrator neurons. “Opposite directions of gaze” can mean motion to the right/left, although this model's rate depends on represented position. The paragraph also states interactions in abstract nouns, leaving the reader to supply which neurons send a signal and which neurons respond. Foundations correctly teaches excitation/inhibition; a compact application here is enough.
- Proposed repair: “The model has two groups of integrator neurons. One group fires more when the eye points farther right; the other fires more when it points farther left. Neurons excite cells in their own group and inhibit cells in the other group. The connection strengths are tuned so that the circuit can approximately maintain a range of represented eye positions.” Retain the goldfish-to-primate qualification and citation. The later fixed-point derivation should remain, since it teaches why connections must be tuned.
- Source support: main-text.txt lines 1039–1055 and 1106–1113, main paper pp. 10–11, Oculomotor integrator network, Eqs. 23–27: two populations more active for left/right eye directions; same-population excitation and other-population inhibition; connectivity tuned to steady states and observed tuning curves. Approximate persistence is the guide's existing, carefully qualified account of the optimized finite model.
- Later explanation: the rate formula and slope definition immediately clarify position sensitivity; the G(z) derivation later explains the tuning condition. These resolve the mathematics, but the first paragraph can make the biological roles clear before those equations.

## 3. Give synaptic activity and the internal readout concrete roles before their equations

- File/section: `04c-eye-circuit.md`, EYE-CIRCUIT-MODEL, lines 20–30.
- Original: “Spikes produce synaptic activity according to” followed by the S, X and E_OI equations; later, “The readout E_OI feeds back into the rates, so these equations define a recurrent network.”
- Missing context: the text gives units, jumps and decay accurately, but never directly says what S_i stands for in the biological model: the lingering effect of cell i's spikes on neurons receiving them. E_OI is a weighted summary of those effects, used both to set future integrator rates and to command motor neurons. The reader should not have to infer this complete loop by substituting symbols across three equations. Earlier foundations explains a synapse and lingering spike effects, but does not map those objects to this model's new variables.
- Proposed repair before the equations: “Each integrator neuron's spikes have a lingering effect on the neurons receiving them. The model represents that effect by S_i. A weighted difference between the right and left groups gives E_OI, the circuit's represented eye angle. That value sets the cells' firing rates again, closing the feedback loop:” Then keep the equations and jump/decay/saturation explanation. Shorten the later “readout feeds back” sentence to avoid teaching this loop twice, while retaining the following persistence condition.
- Source support: main-text.txt lines 1086–1111, main p. 11, Eqs. 23–26: S_i is synaptic output generated by neuron i; tau_s describes postsynaptic currents; E_OI is the internal linear readout of those synaptic activities. Eqs. 23 and 28 supply its effects on integrator and motor rates. This repair describes the model, not a direct experimental observation of integrator neurons.
- Later explanation: “The motor neurons receive this position signal” at line 55 completes its downstream use. Keep that sentence. The earlier loop should be taught before the recurrence/persistence derivation, rather than relying on this later use.

## 4. Explain what makes the feedback visual

- File/section: `04c-eye-circuit.md`, EYE-CIRCUIT-MODEL, line 76.
- Original: “The final loop is delayed visual feedback:” followed by F(t)=A[E(t−tau_d)−E_OI(t)].
- Missing context: the subsequent paragraph explains the sign and the velocity-like approximation well, but does not explain the visual event represented by the loop. The reader sees a subtraction of eye-angle variables without being told that moving the eye shifts a stationary target's image across the retina.
- Proposed repair: “As the eye moves while viewing a stationary target, the target's image moves across the retina. The authors assume that visual feedback responds to this recent image motion rather than to an absolute target-position error. Their delayed feedback model is:” Then retain the equation, delay, dimensions, sign example, and slow-tracking qualification. Remove or combine the later sentence saying it is not a fixed absolute target error, so this distinction is taught once.
- Source support: main-text.txt lines 1223–1234, main p. 11, Visual feedback: assumed motion of the target on the retina, rather than fixing its absolute position; estimated recent target angular velocity relative to eye direction; approximately 70 ms delay; Eq. 34.
- Later explanation: the current post-equation paragraph already gives “estimate of recent movement” and excludes fixed absolute target error. It supplies the mathematical interpretation, but not the retinal setting. The following paragraph correctly limits conclusions drawn from delay and should remain unchanged.

## Passages to retain

- EYE-DRIFT opening uses “changing command” before “shared drive”; the physical-pathway section soon names the motor neurons and muscles. No new abstract definition of “drive” is needed.
- Species, the two-animal sample, one cell at a time, calibration on larger movements, uncertainty across cells versus animals, and shared versus private noise are already explained.
- The inverse filter is clearly a calculation from spikes to predicted eye angle, not a physical signal sent backward. Its purpose and gain are taught before the covariance estimate.
- EYE-TIMING gives meaning and purpose for lag, MSD, white noise, low pass filter, stationarity, and the Brownian teaching model. It separates measurement correction from recovery of an individual trajectory and separates teaching reconstructions from the fitted full model. No context repair found in its connected prose or two figure captions/alt texts.
- EYE-CIRCUIT distinguishes experimental support from the proposed integrator source, and explicitly says no integrator neurons were recorded. Retain the model limits, active-cell conditions, approximate persistence, delayed-feedback limits, and absolute-versus-fractional sensitivity distinction.
- All five assigned figure/table blocks were read, including every EYE-FIGURE-GUIDE row. Their captions and alt text preserve the physical-versus-analysis and model-versus-data distinctions. No additional caption repair found. Pixel fidelity and text inside artwork were outside this assigned text/caption review.

## SHA-256 input record

Paths below are relative to the indicated base. Hashes fix the reviewed snapshot; no claim of unchanged files after this report.

| Base/path | SHA-256 |
|---|---|
| skill/course-study-guide-builder/SKILL.md | B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A |
| skill/course-study-guide-builder/references/pedagogy-language-contract.md | F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A |
| guide/content/chapters/04-eye-drift.md | 6FFC545E25041C3DEF9A36F94C9709D6E9608419A1120F93A8EC191707171EF7 |
| guide/content/chapters/04-eye-drift.yaml | F8E64B79A27747332C02C760B61C2B8B566AF5281681DC54A436CB8F0356A630 |
| guide/content/chapters/04b-eye-timing.md | BDFBEC009BE758D492904F440D03CD1E9517586BBBCDA7A07C69A54845ABAB7F |
| guide/content/chapters/04b-eye-timing.yaml | DD9CDC4F76E69B4A382B73353F752E529B7D976899AE136E16A8C301771B3C5C |
| guide/content/chapters/04c-eye-circuit.md | AF8D48839CF62B2B6271B2B23A70BDE52C24AB8EC83211ADB3628AE681F43481 |
| guide/content/chapters/04c-eye-circuit.yaml | 388E58F64BD4962D4901F318810EFADD08DBBA1BB9E90C431563DD602EC269F5 |
| guide/content/chapters/01-foundations.md | 599892122DC98DE34E6EE22148E5688415C6B50E776ED25A6043CB8108234A01 |
| guide/content/chapters/01b-persistence.md | 299F9015CAC9EF69CC5581E7D71F088BC5704A10589C16C2F2C6A5D97B461BCB |
| research/ben-shushan-2022-main-text.txt | B52B017AD8D63AF12D7301407E3CACE4C0725B1F906AB3543B8A8014666C8EB5 |
| research/ben-shushan-2022-si1.txt | B636BFA42ABC26BD1BC2DEA5B3224AE14F92723BA5783F2AEA3E1DB8280B53B0 |

Skill base: `C:/Users/vital/.codex/skills`. Project base: `C:/dev/clsc/burak-papers`.

Token stats unavailable. Awake execution time was not verified from Windows sleep/resume events; no claim of measured awake time is made.
