# Fresh guide review with Nemotron through OpenCode

3 November 2026. Review only; no manuscript or site edits.

**Nemotron found no confirmed error in the core derivations and no essential gap in the current chapter order.** Its remaining suggestions are optional teaching refinements. Several are already substantially covered, and one proposed label would be wrong if applied literally.

## Model and material

OpenCode v2.0.32 recorded `opencode/nemotron-3.5-super-vl-free#high` for all three review stages. Its model metadata maps this to NVIDIA Nemotron 3.5 Super VL, 120B/A12B. The custom agent denied edits, shell commands and delegation. The guide's source hash was `6198157910f51426cdb6c6db6a23a0bdf592476163778ee16781360dcaa4818e`.

The first call received the current four-Part outline, all 21 teaching chapters, the reading guide, glossary, references, table/caption content, six scientific main/supplement text extractions and five additional source texts. Original PDFs and selected author files were also made available. OpenCode's stored first request was checked against the saved prompt: it contained the full packet, with only Windows line-ending differences.

The first call was fresh and did not receive earlier review verdicts. The second assessed terminology and missing explanation. The third assessed the whole learning path and reconsidered source questions using additional evidence. One session was reused for these separate calls so the source context could be cached.

## My recommended priorities

1. **A compact hardware-study comparison would help most.** Use columns such as study, what persists, physical carrier, measured or simulated result, and what has not been demonstrated. This compares the recent studies themselves; the existing architecture table compares platforms. Keep each study's current caveats. This is a proposed presentation of existing facts, not new verification of unread source bodies. Nemotron R-02, N-04/A-02.

2. **Call the Chapter 1 simulation angle a numerical estimate at first use.** Chapter 18 already explains that choosing the largest-rate neuron is a practical readout, whereas the theory assigns a coordinate through noise-free return dynamics. A short early reminder could prevent conflation without importing the later derivation into Chapter 1. Nemotron N-02/A-03/C-03.

3. **If units still cause difficulty, move the activation-unit label a few lines earlier.** Chapter 2 already says `b=40 spikes per second`. Chapter 3 explicitly calls its `b` an activation bias and gives the conversion `b=2τ b_rate` before computing diffusion. This is an optional placement improvement, not a missing unit definition or a formula error. Nemotron N-01/C-01.

I would not add all of Nemotron's other suggestions automatically:

- **The running example is already present.** Chapter 3 connects its activation model to Chapter 2's rate model. Chapter 5 explicitly returns to that mutual-inhibition model, and Chapter 6 calls it the recurring example and explains its readout assumptions. An example index or one extra link may be useful; another worked block in every chapter would repeat substantial teaching. Nemotron R-01 is therefore largely satisfied by the current text. The readout approximation must not be mistaken for an exact decoder of the same physical spike process.
- **Local state meanings are already explicit.** Chapter 3's opening distinguishes the activation vector, represented coordinate and estimate. The hardware opening and its three-item list distinguish weights, neuron/synapse states and the remembered angle. Add reminders only at a specific remaining point of confusion. Nemotron N-03/C-02 is not an established omission.
- **Do not label `g_i` only as recurrent input.** Equation 8 defines it as the recurrent contribution plus the bias. Chapter 1 already calls it total input and explains both terms. Nemotron A-04/C-04 would lose that distinction if applied literally. Retain the current explanation; `Σ_j W_ij s_j` is the recurrent contribution.

## Source questions resolved

Nemotron's Stage 1 findings F-01 to F-05 were confirmation limits, rather than demonstrated guide errors. Independent checks resolved the four specific questions:

- **F-01:** the original Cannon and Robinson abstract supports the intact and post-disruption gaze-holding time constants used in the guide. [Original abstract](https://pubmed.ncbi.nlm.nih.gov/3585473/).
- **F-02:** the original Major et al. abstract supports the training timescale and retuning under normal visual feedback. [Original abstract](https://pubmed.ncbi.nlm.nih.gov/15136746/).
- **F-03:** Mainali's supplement, PDF p.13/printed p.12, visibly prints multiplication by mean size in S18. The preceding moment relation requires division, as the guide explains.
- **F-04:** Burak and Fiete's SI, p.17, visibly prints the positive rate-decay block in S85, while S84 requires the negative block derived in the guide.

After these checks, Nemotron itself successfully opened both supplied source-page images and confirmed F-03/F-04 in its final response. It accepted F-01/F-02 on the coordinator's primary-source check. The source checks did not inspect the guide's full figure set.

**F-05 remains a real review limit:** eight hardware source bodies were not inspected by this review. Their listing or discussion in the guide is not equivalent to checking the original article. No adverse hardware-claim verdict follows from that limit.

## Coverage and corrections to the review

Stages 1 and 2 each contain 24 reader-unit coverage records. Stage 3 contains 27 path entries: four Parts, 21 teaching chapters, glossary and references. It discusses the reading guide in its overall assessment but does not give it a separate path entry in that stage.

Stage 1 overstated its inspection of author code and full peer-review material. The tool trace showed no file or web reads in that stage: it had read the inline packet, including the guide's descriptions of those materials. This was explicitly corrected in the later prompts and responses. The code files and full peer-review document were not independently inspected by Nemotron, and no simulations were run.

Other limits: source text extraction can damage equations; the two targeted page images resolved the flagged cases, not every source equation. This was a broad expert diagnostic, not paragraph-by-paragraph release acceptance, a complete secondary-literature audit, a code reproduction, or a full guide-figure review. The previously deferred figure acceptance remains pending.

## Evidence

- [Complete original findings and recommendations](FINDINGS_REGISTER.md)
- [Stage 1 original answer](calls/stage1/ANSWER.md)
- [Stage 2 original answer](calls/stage2/ANSWER.md)
- [Stage 3 original answer](calls/stage3/ANSWER.md)
- [Independent source checks](SOURCE_FINDING_CHECKS.md)
- [Actual stage identities, coverage and usage](COVERAGE_AND_USAGE.json)
- [Full-input delivery check](calls/stage1/INPUT_DELIVERY_CHECK.json)

Original final answers are preserved unchanged. A parsed copy of Stage 1 fixes one closing bracket; the exact repair is recorded in its RESULT_CHECK.json. The first wrapper also expected a final event that OpenCode v2 does not emit; the session's successful outcome and recorded model establish completion. No model call was repeated for either formatting issue. The separate access test's denied file read was a permission configuration issue, not a failed book review.

## Time and usage

Start: 2026-11-03 15:31:14 UTC, 17:31:14 Jerusalem. Final wall time is recorded in STATE.json. Awake execution time is unverified.

OpenCode reports the following cumulative session counts, counted once:

| Input | Cache read | Output | Reasoning |
| ---: | ---: | ---: | ---: |
| 885,526 | 841,184 | 24,660 | 51,026 |

These are OpenCode's separate fields; the access smoke test is excluded. It recorded a session cost of $0. Coordinator and supporting-agent token stats are unavailable.
