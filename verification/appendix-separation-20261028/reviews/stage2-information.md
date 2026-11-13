# Stage 2: necessity and wording

Start: 2026-10-28T17:02:10.8356319+02:00. Completion: 2026-10-28T17:03:46.153027+02:00. Wall elapsed for this call: 95.3 seconds. Root wall elapsed since 16:44:38+02:00: 1148.2 seconds. Previous measured checkpoint was this call's start. Awake execution unverified; no system clock change established. Reviewer: separate_dynamics, Sol high. Local request: stage2-information.

This is a separate read-only wording/necessity call after Stage 1. I reread the connected current chapters, concentrating on labels, added bridges, moved paragraphs and the sentences around them. I did not repeat the formula audit. This call does not establish reader-flow acceptance or rendered-output quality.

## Current hashes

- `02b-memory-long-delays.md`: `5932a9fbcf8138994c0438320fc12a08063c04eb6d1878a0f0d3432758e0f857`
- `03-memory-information.md`: `5562f1334a1d3baec322e6a02203d3acbbe8e990ef3c3f247c2eca5853576629`

## Required wording repairs

These are small wording repairs, not correctness findings. Exact replacements follow; no manuscript was edited by this reviewer.

1. Long delays, line 89, added bridge into the two-cell calculation.

Old:

> The mutual-excitation network gives a concrete case: substituting its two conjugate weights into the spike-noise projection gives

New:

> For the mutual excitation network, substituting $v_1=v_2=1/2$ into the diffusion formula gives

Reason: “conjugate weights” is an unnecessary new phrase. The preceding setup gives v explicitly, and the earlier neural chapter calls v a left vector extracting the lasting displacement. The replacement identifies the actual numbers used and the formula they enter. It preserves the calculation's neural-to-mathematical connection and avoids two unnecessary hyphens.

2. Information, line 15, likelihood bridge.

Old:

> A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. This general tool measures which proposed values make a spike sample more likely. For the neural model,

New:

> A [**likelihood**]{.definition-term custom-style="Definition Term"} is the probability of observed data as a function of a proposed parameter value. For the neural model,

Reason: the middle sentence repeats what the definition has just explained. Removing it preserves the general definition, the bridge into the neural model and the following explicit likelihood. It adds no missing premise, mechanism, variable or limit. “This general tool” is also writing-process language the reader does not need.

3. Information, line 204, interpretation of the matrix bound.

Old:

> **Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. It applies under the rate-distinguishability condition used above; if $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]

New:

> **Interpretation.** The bound controls every combination of stored coordinates, including coupled directions that separate scalar bounds would miss. If $J$ is singular, this ordinary inverse formula cannot be used.[^p1-matrix]

Reason: “rate-distinguishability condition” is an avoidable compound. The proof's introduction already says in ordinary words that every independent small coordinate change must change the rates and therefore J is invertible. The retained singular-J sentence states the reader's actual limit. Removing the extra phrase preserves both the earlier assumption and the final limit.

## Retained changed wording and roles

- Long delays, lines 11–13: the mechanism identifies continuing spike fluctuations and the contrast between local spreading and long-delay error. The next paragraph tells readers why a general density calculation comes before fixed-D examples. Both are useful, even though the chapter introduction previews the subject.
- Long delays, moved density derivation and line 60: the derivation says what F and p do, and the interpretation explains why bounded angular error flattens. “Density equation below” correctly supports the new placement; no wording repair needed.
- Long delays, lines 72–96: the example's neural setup now precedes the calculation. “The same linear transfer rule” points back to the immediately preceding chapter's two-cell model; no replacement is required in this limited wording pass. The source discrepancy warning is necessary and remains qualified.
- Long delays, lines 100–110: mechanism, conversion calculation and interpretation do different work. The conditional-independence qualification is needed because shared circuit activity can still produce observed correlations. It should remain.
- Long delays, figure section: “Neural mechanism in the figures” introduces return-flow reading, while “Interpretation of the simulation tests” introduces what panels establish. The specific labels fit actual prose. This section has no independent new derivation requiring a generic derivation label.
- Information, lines 11–64: locally constant state and positive-rate assumptions need their early placement. Likelihood, score, information and prior are real technical terms with definitions; they should not be replaced with looser synonyms. The zero-rate and unbiased-estimation cautions remain useful.
- Information, lines 82–115: the general Cauchy Schwarz sentence connects the dot product and lengths to the network quantities. The explicit squared lengths appear a few lines later, so the introductory use of “lengths measure diffusion and information” needs no repair here.
- Information, lines 117–175: the equality mechanism explains which cells add lasting noise, then algebra states the proportionality condition. Their overlap serves the requested neural/mechanical versus mathematical distinction. The counterexample and numerical example teach different limits and should remain.
- Information, lines 177–204: the new multi-coordinate opening explains what separate scalar bounds miss; the invertibility assumption is now early enough. The matrix term “singular” is expected undergraduate mathematics and is tied to the unusable ordinary inverse.
- Information, lines 208–216: the added list of neurons, rates and slower decay turns the abstract controlled-comparison warning into a concrete guide to the next calculations. Keep it. The interpretation separates the two tau comparisons rather than repeating a result without its held quantities.
- Information, lines 218–258: width assumptions, the integral and the resource-limit interpretation remain distinct. The “teaching reconstruction” caution is useful source scope, not filler. The final sensory/internal comparison retains the condition on matching tuning curves.

No other required wording repairs found in this changed scope. Exact mathematical names and necessary source cautions were retained rather than replaced solely to vary wording. Separate Stage 3 reader-understanding/flow review should use the repaired current text. No edits, build or acceptance update was performed. Token stats unavailable.
