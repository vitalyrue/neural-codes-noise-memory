# Part I: truth and reasoning review

Call: `memory-truth-20261029-01`. Independent reviewer: `/root/alignment_global`. Requested configuration: Astra, high reasoning. Runtime model label and token counts are not independently exposed in this report.

Started: 2026-10-29T12:32:27.0845644+02:00  
Completed: 2026-10-29T12:51:44.1430951+02:00  
Wall time: 1157.06 seconds, including any pauses. Awake execution time is unverified. Verified wall-clock checkpoints are stored in the JSON. No clock change was established. Earlier informal checkpoint labels are not used to compute duration.

## Result

No confirmed text truth or reasoning defect found in this call. All 29 assigned units have individual passage judgments and all 329 extracted claim rows have individual checks. I read the full assigned Markdown, including displayed mathematics and footnotes, rather than treating those rows as the complete inventory. The Part opening and 59 extra reader-text records cover chapter purposes/navigation text, sidecar captions and alt descriptions, and visible fold titles. This is a Part I truth review, not a full book acceptance or a terminology/flow pass.

The important checks were:

- `sec:MEMORY-SYMMETRIC`, paragraphs p243–p259: the squared derivative in the symmetric diffusion numerator is required by projection and SI S18. The guide correctly flags the missing square in main Eq. 2.
- `sec:MEMORY-LONG-TIME`, p84–p98: the excitation pair gives D=θ/(4τ). The source prints a factor-two inconsistency between S40 and S41; the guide keeps its own diffusion convention consistent.
- `sec:MEMORY-BOUND`, p127–p151: the linear equal-input excitation family is a valid equality case. The unrestricted exponential-only converse would be too strong; the guide's pointwise condition and qualification survive the source's strongest reasonable reading.
- `sec:MEMORY-BOUND`, p193–p210: the residual proof uses UᵀV=I and UᵀU=τ²J, giving QᵀQ=2D−τ⁻²J⁻¹. No hidden orthogonality assumption is needed for the original neural dynamics.
- `sec:MEMORY-READOUT-SETUP`, p35–p50: conditional unbiasedness and independent future noise justify zero storage/readout covariance. The passage states these assumptions instead of treating independence of increments alone as enough.
- `sec:MEMORY-IDEAL`, p129–p199: the backward precision recursion gives the negative Riccati term and the coth result. A separate finite-bin covariance inversion converges to it. The stated variance and standard-deviation ratios differ correctly.
- `sec:MEMORY-EXTENSIONS`, p244–p282: the two time constants belong to the specified two-stage model. The later constant additive Gaussian q model uses matching information and diffusion weights; it is not a rate-proportional Fano-factor substitution.
- `sec:MEMORY-FIG3-AND-CAUTION`, p320–p341: 2DJ≥τ⁻² gives √(2D/J)≤2Dτ. It cannot justify the printed universal lower bound by substitution. The guide calls this an apparent inconsistency rather than an author-issued correction.

I recomputed the Poisson example, two-cell coordinates, Brownian scales and bias crossing, ring limit, inhibition/equality cases, ideal/naive/partial readout numbers and strict-bound example. Details are in `memory-stage1-recomputations.json`. Focused source-PDF formula checks covered main pages 2 and 4 and SI pages 9, 11, 14, 17 and 19.

## Limits and next call

Caption and alt scientific statements were checked against their equations or primary source descriptions. Exact artwork excerpt identity, curve/arrow rendering, path counts, visible labels and all figure pixel acceptance remain deferred by the user's scope. A text-unit pass does not accept those items. No manuscript, packet or review ledger was changed.

The separate Stage 2 terminology/prerequisite and Stage 3 language/flow calls remain pending. In response to the root's handoff, the gain explanations are confirmed at Foundations lines 129 and 167; their first-teaching marker placement is reserved for Stage 2.

The JSON contains all source hashes, exact unit and paragraph references, claim decisions, and the extra reader-text inventory. Token stats unavailable.
