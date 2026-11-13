# Claude CLI review of mathematical guide passages

Completed 2026-11-09 11:51 +02:00. Review only; no guide changes.

Claude Code 2.1.310 used Claude Opus 5.5 at high effort, with tool access disabled. It received the five assigned chapters, the reading guide and three earlier/connected chapters, and the relevant course-study-guide-builder and course-quality-gate rules. Three separate calls reviewed truth/reasoning, wording, and reader flow. The flow call continued the wording session. Request and result JSON files record timestamps, model usage, prompt/source hashes and raw responses. The reviewed source/rule hashes still matched after the calls.

## Prioritized findings to consider

1. In 00-mathematical-tools.md:60-62, fixed-point family, neutral tangent and the left projection are used before the reader is given enough context. The generic eigenvector u becomes the neutral tangent without an explicit restriction; the defining left-vector equations occur only in the fold. Explain the fixed states and neutral tangent, then connect v^T K=0 and v^T u=1 to the lasting displacement.
2. In 00-mathematical-tools.md:209, chi_Y appears before it is explicitly named as the fraction of observed displacement variance attributed to the shared source. Explain how the gains and calibration enter the inference. In the same chapter, tau refers to a synaptic decay time and later to a muscle response time; flag that they are different quantities. Other reused symbols should be assessed individually.
3. In 02-memory-dynamics.md:199, a general memory coordinate is described as an angle even though a later example uses an activation difference. Use coordinate language or explicitly scope the statement to angles. In 03-memory-information.md:359, the comparison uses a synaptic rather than an unspecified cellular time constant, and describes model comparisons rather than an experiment.
4. In 05c-place-tests.md:214, the crossing rate exp(-q^2/2) increases as q decreases only on the positive-q side. State the relevant range and preserve the actual fitted-data qualifications. At line 9, 'fixed over space' may suggest the map is spatially constant; its values vary across space but the drawn map stays fixed in time.
5. In 03-memory-information.md:254, 'preceding chapter's plot' appears to point to Chapter 3 even though Chapter 4 immediately precedes this chapter; confirm and name the actual plot. State how the reported rate slopes follow from the rates.
6. The 02-memory-dynamics.md:41-63 explanation calls the approximation a Gaussian summed input but writes continuous noise in each activation equation. Explain why that representation is used for the summed-input calculation under the paper's weak-noise limit. Avoid claiming that a single infinitesimal spike count is itself Gaussian.
7. Some transitions can be tightened, especially the main-text reason why a tuned feedback network retains a difference, the role of the steepness weighting in crossing counts, and the interpretation before the multi-coordinate extension. Evaluate repeated examples for instructional value; do not automatically delete examples that serve as a useful preview and later elaboration.

## Adjudication and limits

- Q(q) is defined earlier in 05-place-fields.md:189; a local reminder in place tests may help, but the term is not absent from the guide.
- The figure caption in 02-memory-dynamics.yaml states a/lambda=1/2 and initial y=2, making the stated shift of one correct. A prose reminder is optional.
- The 2017 published correction (https://doi.org/10.1073/pnas.1706051114) confirms the squared numerator. The passage distinguishes this published correction from the guide's independent checks of other formulas.
- The two-unit network's weights and linear transfer rule agree with the paper's PDF page 6, while the guide's numerical bias is illustrative. The model can also be interpreted as two groups of neurons. Claims that the equations are false because the example rates are high need separate evidence; do not silently adopt that claim.
- A live browser check found the Chapter 3 tilted-flow example collapsed, so its source markup was not evidence of a folding failure. Other fold instances were not individually checked.
- Claude suggested a heuristic sentence claiming each re-estimation error cannot be corrected later. Do not adopt this as a proof or a general statement without checking the model's assumptions; the guide correctly labels its readout analogy a heuristic and derives the bound separately.
- Claude's broad recommendation to delete repeated examples was revised by its third pass after considering their teaching role. Decide case by case.
- Claude did not receive the PDFs, figure/table blocks, the full glossary, or every chapter. Source claims and all figures were not independently audited. This is not a full quality-gate or book-acceptance result.

## Usage

Across the three substantive review calls: 539,938 input tokens including cache creation/read, 132,931 output tokens including 108,711 thinking tokens. The small CLI readiness check is not included. User-visible and thinking outputs are not additive categories.
