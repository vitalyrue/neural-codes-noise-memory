# Independent checks of Stage 1 source findings

Started: 2026-11-03 15:53:38 UTC. Completed: 2026-11-03 15:55:29 UTC.

This is a narrow supporting check by the configured gpt-6.1-sol reviewer at high reasoning, separate from the external Nemotron review. It checks F-01 through F-05 from `calls/stage1/BODY.json`. No guide text, build, simulation, or deployment was changed. Two complete PDF pages were rendered and inspected. No guide figures or additional hardware papers were audited. No prior review verdicts were reused. Awake execution time is unverified; wall-clock duration is 1 minute 51 seconds. Token stats unavailable.

| Finding | Check result | Guide error? |
| --- | --- | --- |
| F-01 | Guide's numerical background claim supported by original abstract | No error found; initial reviewer source-access limit resolved |
| F-02 | Guide's training timescale and reversal claim supported by original abstract and Fig. 4 caption | No error found; initial reviewer source-access limit resolved |
| F-03 | Guide's reading of printed S18 supported by fresh PDF image | No error found; reviewer extraction ambiguity resolved |
| F-04 | Guide's reading of printed S85 supported by fresh PDF image and adjacent S84 | No error found; reviewer extraction ambiguity resolved |
| F-05 | Unread-source category retained for eight hardware papers | Truth of those hardware claims remains unassessed here |

## F-01: Cannon and Robinson (1987)

**Support, high confidence.** Read the original abstract in [PubMed PMID 3585473](https://pubmed.ncbi.nlm.nih.gov/3585473/), DOI [10.1152/jn.1987.57.5.1383](https://doi.org/10.1152/jn.1987.57.5.1383), J. Neurophysiol. 57(5), 1383-1409, abstract paragraphs 3-5. It describes reversible effects after brainstem neurotoxin injections, intact time constants above 20 seconds measured after saccades in total darkness, and a minimum horizontal time constant of 200 milliseconds after bilateral injections. Those details support the guide's about 0.2 seconds versus over 20 seconds. No full-body access was needed for this specific claim. The initial finding concerns what the reviewer had not read, not a factual error found in the guide.

## F-02: Major et al. (2004)

**Support, high confidence.** Read the original abstract and the paper's Fig. 4 caption in [PubMed PMID 15136746](https://pubmed.ncbi.nlm.nih.gov/15136746/), DOI [10.1073/pnas.0401970101](https://doi.org/10.1073/pnas.0401970101), PNAS 101(20), 7739-7744. The abstract directly gives a training period ranging from tens of minutes to hours in goldfish and says ordinary visual feedback restores stability gradually. Fig. 4's caption describes retuning with a stationary visual surround after training and gives 80-minute training intervals. This supports the guide's timescale and reversibility. Direct PMC body access returned a browser check and the publisher returned HTTP 403; the accessible original abstract and figure caption suffice for the claim checked. This does not establish that the exact cellular learning rule is known.

## F-03: Mainali et al. (2025), supplement Eq. S18

**Support for the guide's printed-error flag, high confidence.** Freshly rendered and inspected the complete original supplement PDF page 13, printed page 12, Methods S3, Eq. S18 and the paragraph immediately above it. Source: `inputs/papers/mainali-2025-supplement.pdf`, SHA-256 `05af1fdf3079906871da12fdafa1f28895380f594a8c6bda3cafc5b503f07c31`; article DOI [10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017).

The printed expression is beta = [Gamma(D/2 + 1) times mean(s)]^(2/D). The immediately preceding moment relation gives mean(s) = Gamma(D/2 + 1) beta^(-D/2), which rearranges to beta = [Gamma(D/2 + 1) / mean(s)]^(2/D). Thus the PDF really prints multiplication where division follows from the preceding equation. The guide's statement at `content/chapters/05b-place-sizes.md:200` is supported. The Stage 1 statement that its extraction showed division is not a reliable reading of the printed formula. No code or fitted results were checked.

Image record: `source-check-images/mainali-2025-supplement-p13.png`.

## F-04: Burak and Fiete (2012), SI Eq. S85

**Support for the guide's printed-sign flag, high confidence.** Freshly rendered and inspected the complete SI PDF page 17, printed page 17, Section VII, Eqs. S84-S86. Source: `inputs/papers/burak-fiete-2012-persistent-activity-si.pdf`, SHA-256 `9bbff1fb83db4aa4b76364a92de7c481de1f27ccdd6735dce78ae1d7b8496efb`; DOI [10.1073/pnas.1117386109](https://doi.org/10.1073/pnas.1117386109).

The lower-right block in printed S85 is positive tau_m^(-1) delta_ij, with no leading minus. S84 on the same page is dot(r_i) + r_i/tau_m = phi(g_i)/tau_m. Moving the decay term to the right and linearizing gives a negative lower-right block, -tau_m^(-1) delta_ij. The guide's footnote at `content/chapters/03b-memory-readout.md:422` correctly identifies the mismatch. This conclusion follows directly from the printed differential equation, without a stability assumption or a simulation.

Image record: `source-check-images/burak-fiete-2012-persistent-activity-si-p17.png`.

## F-05: hardware papers

**Access limit only, high confidence about scope; truth not assessed.** Inspected the eight corresponding entries in `SOURCE_ACCESS.json`: HW-Pehle2022, HW-Scholze2026, HW-LeGallo2023, HW-Massoud2011, HW-Giulioni2012, HW-Ortner2025, HW-Wang2026, and HW-Ilmberger2025. Each records an empty `local_original_evidence` list and `source_body_available_locally: false`. Each also supplies a primary URL and an intended source locator. This supports classifying F-05 as an unread-source category for this review packet. It does not show the claims are false or that the sources are unavailable online. Their hardware numbers and performance claims remain unassessed in this supporting check. No request was made to expand the work into eight new paper reviews, so none was performed.

Checkpoint: 15:54:40 UTC, wall-clock elapsed 1 minute 2 seconds, time since start checkpoint 1 minute 2 seconds, awake time unverified. Final checkpoint: 15:55:29 UTC, wall-clock elapsed 1 minute 51 seconds, time since prior checkpoint 49 seconds, awake time unverified.
