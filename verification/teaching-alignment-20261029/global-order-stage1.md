# Fresh global teaching order review, stage 1

Local request ID: alignment_global/stage1. Reviewer agent: /root/alignment_global, instructed model Astra high; platform model build not independently exposed. This is a global truth, purpose, and order diagnosis, not three completed review stages or book acceptance.

Start measured by PowerShell: 2026-10-29T12:26:17.7840104+02:00.
Fresh context: neutral assignment, actual manuscript, plan, project description, current teaching rules. No prior findings, current-state notes, or historical review reports read. No manuscript changed. Memory not consulted so prior judgments could not guide this fresh review.

Sequence performed: read rules and intended reader; read actual plan, landing page and front matter; read all 13 chapters for their actual contributions and dependencies; inspect selected typed tables/captions and glossary entries; compare alternative orders; record findings. Initial estimate to coordinator was 12–18 minutes; actual measured duration is recorded below. No visual sweep.

## Outcome

The current book and Part order is defensible. I found no required whole-chapter move and no missing book-level premise that prevents following its main argument. This is a narrow positive result: it does not approve every claim, paragraph, formula, source comparison, or rendered figure. There is one small first-definition marking defect below. The more detailed independent stages must still judge the complete reader-facing text.

The book actually teaches three different kinds of result: a limit within a memory model, an inference from paired eye and neuron measurements, and a statistical account of spatial maps. It repeatedly preserves that distinction. The book's goal is not to prove that the three papers describe one identified biological circuit. This matches guide-project.yaml description, content/index.md, the front matter and synthesis.

Reader baseline: 00-reading-guide.md, section READING-START, assumes undergraduate calculus, basic probability and linear algebra; neuroscience and stochastic/information/filtering/random-field tools are supplied by the guide. The global judgment does not silently assume stochastic calculus or neuroscience background.

## Current teaching path and why it works

| Unit | What it actually contributes | Earlier teaching needed and verdict |
| --- | --- | --- |
| Front matter | Distinguishes the papers' questions, methods, findings and limits; sets audience and reading paths | The neural setting begins with neurons, eye angle, movement and place fields in ordinary language. Retain. The short paper previews are not used as substitutes for the later teaching. |
| Ch. 1, FOUNDATIONS | Spikes, rates, synapses, tuning and population codes; Poisson variability; shared/private variation; displacement and MSD | 01-foundations.md:9–28 supplies actors and what their signals represent; :97–170 supplies actual eye-command and measurement roles before covariance and MSD interpretations. Retain. |
| Ch. 2, PERSISTENCE | Persistent activity differs from accurate memory; decay toward a family versus motion along it; accumulating error; fixed spatial versus changing temporal randomness | 01b-persistence.md:9–15 explains recurrent correction before state/fixed-point geometry; :21–62 works through two disturbances; :68–108 connects retained spike effects to variance growth. This prepares Ch. 3 rather than presuming its derivation. Retain. |
| Ch. 3, MEMORY-DYNAMICS | Spike-to-synapse feedback; local network response; lasting displacement; diffusion and symmetric-weight case | 02-memory-dynamics.md:13–50 establishes the cycle, roles, transfer function and parameter effects. :95–152 derives the left vector from what survives return flow; :184–220 connects it to diffusion. Retain. |
| Ch. 4, MEMORY-LONG-DELAYS | Distribution of memories over time; line versus ring; variable diffusion; systematic drift; interpretation of network figures | 02b-memory-long-delays.md:3–13 explicitly uses local D from Ch. 3; :47–60 shows why bounded angular error levels off; :111–121 keeps drift and noise assumptions separate. :125–132 distinguishes current-state observation error from storage error, motivating Ch. 5. Retain. |
| Ch. 5, MEMORY-INFORMATION | Likelihood and information; lower diffusion bound; equality; controlled parameter comparisons | 03-memory-information.md:11–68 teaches nearby-state discrimination before score and Fisher information. :82–115 uses Ch. 3's projection. :214–264 states what changes and what stays fixed before comparing populations, rates, time constants and widths. Retain. |
| Ch. 6, MEMORY-READOUT | Storage versus readout error; equal weighting versus diffusion-aware inference; limited access and extensions | 03b-memory-readout.md:11–46 states target, available observations and independent-error assumptions; :60–109 shows why equal weighting can become harmful; :113–142 derives the better inference through precision rather than requiring prior Kalman-filter knowledge. Retain. |
| Ch. 7, EYE-DRIFT | Physical pathway and paired recording design; forward calibration; inverse prediction; independent-noise bound; common-variance estimate | 04-eye-drift.md:11–34 distinguishes integrator, OMNs, muscles and recorded signals; :47–57 establishes calibration and physical versus computed pathways; :241–279 states the gain and noise assumptions for covariance. This uses the foundations, not an unintroduced causal pathway. Retain. |
| Ch. 8, EYE-TIMING | Measurement correction, then stationary filtered noise versus filtered accumulation | 04b-eye-timing.md:17–48 separates measurement error from physical movement; :71–90 teaches white noise and stationarity before the covariance calculation; :110–178 explains command mismatch, response time and retained long-time growth. Retain. |
| Ch. 9, EYE-CIRCUIT | A proposed full circuit; persistence condition; motor/plant response and feedback; regularity and scale; inference limits | 04c-eye-circuit.md:9–53 explains two interacting populations and derives G(z)=z; :64–94 carries output through motor units and feedback. :128–160 uses the earlier information calculation for a controlled scaling comparison. :248–261 separates upstream evidence from unique circuit identification. Retain. |
| Ch. 10, PLACE-FIELDS | New spatial setting; Gaussian map plus threshold; covariance length; crossing counts; parameter inference | 05-place-fields.md:3–17 restarts from recorded maps and the hidden input; :40–50 explains threshold and firing gain effects; :97–143 derives crossings; :157–187 separates threshold from spatial scale using measured lengths/gaps. Retain subject to first-definition marking below. |
| Ch. 11, PLACE-SIZES | High-threshold local geometry; size laws in different dimensions; slices; selected boundary slopes | 05b-place-sizes.md:11–20 sets asymptotic assumptions before the calculation. :22–76 connects height and curvature to radius. :168 quantifies finite-threshold error. :186–206 distinguishes slice sampling from whole-field sampling. Retain. |
| Ch. 12, PLACE-TESTS | Topology with boundaries; fitted quantities versus tests; possible random-input mechanism | 05c-place-tests.md:11–31 teaches components, holes and Euler characteristic before the formula. :121–145 connects measured maps and processing to tests. :200–249 introduces random summation as one possible mechanism after statistical predictions, preserving the distinction between a fitted descriptive model and measured wiring. Retain. |
| Ch. 13, SYNTHESIS | Separate maps, dynamics and movement; a new conditional connection; evidence needed for a joint test | 06-synthesis.md:9–25 states the distinct objects; :29–52 explicitly labels its fixed-map/moving-state construction as a guide calculation. :93–122 matches tests to claims. Its position after all three papers is needed to interpret the comparison. Retain. |

Part MECHANISMS has a coherent question: why can persistent activity still lose accuracy, and how does spike information constrain this loss? Part OBSERVATIONS tests different links between neural representation and measured behavior. Its broad title accurately includes both eye motion and spatial maps; the place chapters do not require claiming that spatial map randomness is temporal noise. The end of Ch. 2 (:159–171), Ch. 10 (:11), and Ch. 13 (:15) explicitly prevent that confusion.

## Alternative orders tested

1. Put the information/readout chapters immediately after local diffusion, before the long-delay chapter: 1, 2, 3, 5, 6, 4. Benefit: the central information–diffusion result arrives sooner. Cost: Ch. 5's linear mutual-excitation counterexample (:139–147) currently needs Ch. 4's model (:72–98), and Ch. 4's distinction between storage and observation error (:125–132) motivates information. A short move could preserve those prerequisites, so there is no mathematical demand for the present whole-chapter order. However, the current progression first establishes what D predicts and where that prediction fails, then asks what bounds D. That is a good learning progression for a guide explaining the appendix. No required change.

2. Teach the eye recording/timing chapters after the two foundations chapters and before the detailed memory theory. Benefit: concrete evidence earlier. Cost: the eye story is then split, because Ch. 9's scale argument needs information and projection from Chs. 3 and 5. The current front matter already gives a concrete eye question and empirical finding, and Ch. 1 supplies the physical command-to-muscle path. Moving whole chapters would add backward travel without fixing a missing premise. Optional alternate reading route only, not a defect.

3. Move random wiring from Ch. 12 before the Gaussian spatial model in Ch. 10. Benefit: an explicit candidate neural construction appears earlier. Cost: it would burden the map model with central-limit and input-covariance machinery and could make a sufficient proposed mechanism seem necessary. Ch. 10:7 already says what physical quantity h represents and that recordings do not directly measure it. Ch. 12:249 keeps the wiring claim conditional. Retain present order. Physical setup before mathematics does not require proving an unmeasured biological cause before teaching a descriptive model.

No order change is required merely because a later chapter contains a deeper explanation. Ch. 11:63 explicitly states the higher-dimensional high-peak count factor and marks its later derivation; it does not silently pretend the factor has already been proved. Putting topology before high-peak geometry would complicate the first spatial calculation. The limited proof claim at :20 and :63 matters to this verdict.

## Finding G1: first blue definition is placed after the first teaching occurrence

Location: 05-place-fields.md:17 and :21, section PLACE-GP.

Passage: at :17, “A **Gaussian process** specifies a distribution of such maps,” followed by its mean, covariance, and fixed-map interpretation. This is the first teaching occurrence and introduces the term using plain bold. The blue definition span appears at :21 inside the folded formal definitions.

Strongest reasonable reading: :17 is a conceptual definition and :21 adds the exact finite-dimensional Gaussian property. This is good separation of conceptual and formal depth. It still fails the rule that the first teaching occurrence carries the blue span and that introduced terms do not use plain bold. No missing concept is alleged: the combined passages explain the meaning correctly for the later crossing argument.

Proposed narrow repair, pending authorization: move the blue term mark to :17 and leave “Gaussian process” plain at :21; preserve both explanations and the glossary entry (glossary.md:38). This changes marking only. It does not justify chapter reordering or a full book rebuild.

## Optional formal notes and parameter meanings

The conceptual path has usable main-text explanations: Ch. 2:68,100–108 states retained increments, D, units and consequences outside its Brownian derivation fold; Ch. 6:177–199 states the readout limit, timescale and interpretation outside the hyperbolic solution; Ch. 10:17 gives the map interpretation before its formal Gaussian definition. The later detailed calculations need the formal notes. I do not call this a hidden prerequisite defect merely because a formal definition is in a fold: the reader route explicitly separates a conceptual pass from checking derivations. A later flow stage should verify that each optional note is optional for its claimed route; this global call has not certified every fold.

Concrete parameter consequences are present, not inferred from equations alone: connection signs/transfer slope/time in 02-memory-dynamics.md:50,115; rates/time/population constraints in 03-memory-information.md:214–226; filtering response time versus diffusion in 04b-eye-timing.md:118,171; absolute versus fractional rate slope in 04c-eye-circuit.md:130–160; spatial threshold, input scale and firing gain in 05-place-fields.md:48–50; covariance amplitude versus input width in 05c-place-tests.md:238. Preserve these explanations in any wording edits.

## Coverage and limits

Read the actual project description, landing text, chapter plan, front matter and all 13 chapter Markdown bodies for this global diagnosis. Read typed blocks in reading guide, persistence, place sizes, place tests and synthesis. Checked selected glossary definitions. Did not inspect all other sidecars, figure pixels, all glossary/reference entries, external papers, all algebra or computational listings in this call. No prior source checks were assumed valid. No rendered output or browser behavior checked.

The concept-prerequisite reference was read. This call used direct passage comparisons and did not generate or validate a Publisher concept index; coordinator was notified. No complete concept-order check is claimed. Detailed truth, wording and flow calls remain separate work. Source hashes below are captured at report completion, not falsely recorded as hashes captured before reading.

Timing correction: two early coordinator messages contained estimated clock values (12:28:01 and 12:31:46) instead of measured checkpoints. They are invalid timing evidence and were explicitly withdrawn. Actual measured checkpoints were 12:26:17.7840104, 12:28:20.6672774, 12:28:28.4255639 and 12:29:11.9173943, all +02:00 on 2026-10-29. A Windows sleep/resume/time-change query returned no usable events. Awake duration is unverified; no system clock change was established. Only the measured timestamps and final elapsed duration should be used.

Token stats unavailable.

## Source hashes (SHA256)

- guide-project.yaml: 45f330cec771d6223e8ec81341dea1781e4d4c32d27a1a82b0f616e813313907
- plan/chapter-plan.yaml: 394e5bfdcca536683bacfef577c10434b25361ddfd31f5588248fab976bbf8e6
- content/index.md: 361396b67ad80cd60d3a9b7767e6a360e0643d17abf80ebece7b4741923c8bfc
- content/chapters/00-reading-guide.md: 07945a554f76591a8554f5f928d2f22f1ee52f8d5b13eb4d2750d38cb1d5227e
- content/chapters/00-reading-guide.yaml: 7ee74d6dfe7e8c88a63a258a351a6e01a574ff3eb99fd242503dee6da010687e
- content/chapters/01-foundations.md: e4fd06733f893bf1334702f3d7045844415a988032cc0b583105833cd430e42a
- content/chapters/01-foundations.yaml: 68907e53bb0557dde4448acd9f3357269559718c315d2429f55e3f46c7e3274b
- content/chapters/01b-persistence.md: 5bea2d0482dbc15b2862e5fd2b16ecc8e7f257056d224aeee2fbe07e370a7ea5
- content/chapters/01b-persistence.yaml: df5138c8652286d947d32ae264913e933487b541cdc37e85163cbfdf0efd2b3f
- content/chapters/02-memory-dynamics.md: 869913aa0dfbc2e06145d5458dd0b7f14535e9cffd985b2122fea54e1816f858
- content/chapters/02-memory-dynamics.yaml: 24a3cc98bbf9b482dd61584b011cf4740c7b83647d2db653ea6224caa5d6748a
- content/chapters/02b-memory-long-delays.md: 70b5efc6650d2b6c1bbf35b0bdae7a379d80dff863944a872b45df257d7b6baa
- content/chapters/02b-memory-long-delays.yaml: 69ce685f1aedf9c0c1a1df5fc40d8bc447d9af7361fb00130a9b6950a2f83fe6
- content/chapters/03-memory-information.md: 63a62a989b01e89ad8a26a342bf311f987286d75167d8854f708d0a8de4b2d2c
- content/chapters/03-memory-information.yaml: c7f851d3de3c2b8aef5a9b04cfde68a7ae272e648aa686c20c3fdcbe42d00f6b
- content/chapters/03b-memory-readout.md: 3fa9ce95117610c8dfe5e9f0c7995ed4d38fe96674d3b2bdd2af04d1ebe268d5
- content/chapters/03b-memory-readout.yaml: c60bc0bb97b99d88c7067c0dc6d42ad9c119dc0c5bd3a9f7aeb93ae2c2fa5f06
- content/chapters/04-eye-drift.md: a41b01f6486d719a8c11ce80d4d1d8a6bf89356b3e339781f9c99494e20c8ce6
- content/chapters/04-eye-drift.yaml: 240bde4197801b21b8a2a1e5e021f7e5254c2618232e4d9936c062f36799fc29
- content/chapters/04b-eye-timing.md: 09d2fe568cd0bcf9a9130bf7318e273aa8b13c4142faae0dd74d0873d4a4ddd4
- content/chapters/04b-eye-timing.yaml: 0269c4f78ff2566c7ff78e51cc7d025e1cacd9c3a587a115e38de500b3d787be
- content/chapters/04c-eye-circuit.md: d78c954750e1ab16bd1a7b8cbd9743382f6333e98c121afd48ef2fab3063f5fd
- content/chapters/04c-eye-circuit.yaml: 5960f38e5b4b3bf8c1b97ef224b1c0b7dd584d9e2eecace12df3069c55b4012d
- content/chapters/05-place-fields.md: 342268f4d10c4d5ace00d23d10372638ac7bbe982cf574bb08b33764e921fcb9
- content/chapters/05-place-fields.yaml: 8258ecdab0c6e402aacd6238ab2d7f744c05985595069262bae13e1ad4e787ea
- content/chapters/05b-place-sizes.md: 0b85730becd9e26563fc9f7a78801aa11d27508a66e3b7326402bda6b231135d
- content/chapters/05b-place-sizes.yaml: 501d2953ce7fbce4c4b71db1e6df769a94e85585bb7e2c5fc5135f35e71f8c8c
- content/chapters/05c-place-tests.md: a30e5c2dd6f101524affd5761922b18d95d76361b46698f1eb9120c3755689c4
- content/chapters/05c-place-tests.yaml: 3bf82a80a71d635f05ddc52bbc839c235a606f1e85b0ddfe70c0a5b4c009b490
- content/chapters/06-synthesis.md: 54f589c1d9ce1c8e0d65b9849bb8fd7e29a3e9a8db6b7963a02b20fd5ee6a76f
- content/chapters/06-synthesis.yaml: 60b396173d94b5b4e2a078a71b2c7ff64ee651f2dce0d736cc343f54eb8df9a2
- content/chapters/glossary.md: 7b13a6a8df927b2758b5e43740cbddb4a9b41c25b99e443c652b5efb05a12850
- content/chapters/glossary.yaml: f98a3e8dc1995bc446f9a0ebda9abd3510a119a243110e07b3d203fba0351b1c
- content/chapters/references.md: 5daf2401b5b9127d72de0d124fe99e706160c105a4e29c7bb41ece2bfc47fbdf
- content/chapters/references.yaml: bd3438c9ca97a07924f2d7591abcea7052424ca162a73de91ef651a3f68a71c6

## Rule hashes (SHA256)

- SKILL.md: b78068e9874e6d1d97b2017bf8f940492f9b08fc11b74f20fd75019ff388984a
- references/pedagogy-language-contract.md: f4c1eb544cf640b708e1970d9572fdc758fcc6aea806675d01a0256658df847a
- references/math-code-case-contract.md: ce2313f897b63e74ba59a3afe1bbc4046d3aa84584072cda7e76470a7e3cef9a
- references/concept-prerequisites.md: 4c8d4af325fb63af8dbe41d447d4bac7197df550b0ddb9f4cdb0dea3b1fe9f9a

End measured: 2026-10-29T12:31:02.3938761+02:00. Wall-clock elapsed: 284.61 seconds. Awake execution time: unverified.
