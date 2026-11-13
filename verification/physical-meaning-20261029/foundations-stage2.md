# Foundations stage 2: necessity and terminology

Independent reviewer `/root/physics_foundations_review`, selected model gpt-6.1-sol with high reasoning. Local request `physics_foundations_review-stage2`. Actual tool-clock checkpoints: 2026-10-29 09:10:43 UTC start, 09:11:21 UTC earlier-definition check, 09:11:55 UTC conclusion. Wall time to conclusion: 1 minute 12 seconds; since previous checkpoint: 34 seconds. Awake execution time unverified because sleep/resume logs were not checked.

Scope: current foundations opening and full rewritten section, including folded content and list items; chapter read in full for prior terminology. Checked the index audience statement and reading-guide introduction of MSD. This is stage 2 only, with the accepted gain clarification present. No manuscript edits or builds.

## Required repairs

1. **Definition marking, lines 105, 140, 142.** Covariance and correlation coefficient are now introduced with plain bold rather than `[**term**]{.definition-term custom-style="Definition Term"}`. Displacement has the same problem. Restore the required term spans at these teaching occurrences. The whole-sentence `.definition-explanation` span does not replace the term span. The rule explicitly says, “Do not introduce terms with plain bold or italics.” MSD already has its blue first-definition occurrence in `00-reading-guide.md:82`; retain the useful reminder here in normal text rather than creating a second blue introduction. This is a term-format repair, not a reason to remove the definitions or formulas.
2. **Unintroduced specialist use of “lag,” lines 166, 168, 170.** Line 140 defines ell as elapsed time, but does not tell the reader that this is also called the lag. The later “fixed lag,” “short-lag,” and “nonzero lags” rely on that meaning. Add “also called the lag” to the elapsed-time introduction, or use elapsed time consistently. The notation does not need a new explanation. This is a small terminology repair, not a request for a separate subsection.

## Paragraph decisions and deletion tests

| Passage | Decision and reason |
| --- | --- |
| Opening, lines 3-5 | Retain. The first paragraph gives the shared scientific question and distinguishes the three papers. The second supplies the order from spikes to uncertainty to shared variation and directional change. Deleting that last distinction would hide why covariance/MSD enter a chapter about spikes. Its length is reasonable for a chapter map. |
| Line 99, fixation and neural-to-muscle chain | Retain. It supplies the observable small movement and tells the reader what acts on the muscles. Removing it would make the following command/noise comparison lack a physical setting. “Fixation” is explained by looking at a stationary target in the same sentence; no extra definition sentence is needed. |
| Line 101, two measurements | Retain. It separates which changes occur together from how displacement grows. The circuit limit prevents these measurements being mistaken for circuit identification. This is a useful boundary, not spare caution. |
| Line 103, shared command and private spikes | Retain. It connects common input to adding muscle effects, private fluctuations to partial cancellation, and the one-cell predictor to an analysis operation. The warning about one-cell causation addresses the misconception created by that very comparison. It is not a repeat of the more general circuit-identification limit. |
| Line 105, intuitive covariance/correlation | Retain with term-marking repair. The first statement gives the general centered comparison, the next applies it to the actual recorded pair, and private noise explains why correlation need not measure common movement fraction. Deleting one as mere repetition would lose the general-to-recording step or the interpretive limit. |
| Fold, lines 109-127 | Retain. It gives precise variables, units, sum/difference identity and normalization to readers who need the calculation. Folding this formal material leaves the physical argument visible as requested. The zero-covariance limit prevents an incorrect reverse inference. |
| Fold, lines 129-136 | Retain. The shared-source example explains why private variance and gain affect different parts of the measured relationship. Removing it would leave the physical reading of rho unsupported by a calculation. Its independence condition and statement that it is a simple model preserve scope. “Private” already refers to each cell's own variability, and gain is explained as conversion of the source effect. No additional vocabulary lesson is needed. |
| Line 140, wandering and directional error | Retain with the lag repair. The contrast prepares the mean/spread identity using a physical command. Muscle smoothing states why observing over different times matters. Each contributes a different step. |
| Lines 142-148, MSD and its two contributions | Retain. The named statistic, units, identity and interpretation let a reader distinguish random spreading from mean motion. The interpretation after the formula is needed rather than a repeat of the symbol equation. |
| Fold, lines 152-159 | Retain. The derivation explains the vanishing cross term and gives the finite-moment limit. Keeping the derivation folded avoids slowing the visible mechanism explanation. |
| Lines 163-168, parameter list | Retain. The four items change different objects: random accumulated changes, mean motion, command conversion, and temporal smoothing. Combining them into a vague “more noise means more movement” statement would lose the requested parameter consequences. The repaired gain bullet states what is held fixed and separates later noise. The fitted-slope warning matters because the chapter already introduced a tuning slope. |
| Line 170, measurement error | Retain. It separates recorded motion from physical motion, explains the factor of two under explicit assumptions, and motivates the later removal calculation. It is not a fifth physical cause of eye movement. |
| Line 172, next chapter | Retain. It returns from the measurement framework to the stored command that the next chapter explains. This is the one transition the reading path needs. |

## Optional choices, not required repairs

The repeated label “Physical meaning” could be shortened or removed without changing content, but it makes the user's requested mechanism explanation easy to find. Retain unless the author prefers fewer labels. “Shared command,” “common input,” and “shared drive” are close in meaning here; unifying them is optional because the surrounding sentences identify their roles. There is no evidenced need to shorten the section further. Its longer calculations are already folded, and the visible parameter list adds distinct consequences.

## Version evidence

SHA256 hashes:

- `guide/content/chapters/01-foundations.md`: `F2E4A15697387803D297D86DDBC14A8946A4C501066E7D9B1B9943F9A1E5B597`.
- `guide/content/chapters/01-foundations.yaml`: `68907E53BB0557DDE4448ACD9F3357269559718C315D2429F55E3F46C7E3274B`.
- `guide/content/chapters/00-reading-guide.md`: `07945A554F76591A8554F5F928D2F22F1EE52F8D5B13EB4D2750D38CB1D5227E`.
- `guide/content/index.md`: `361396B67AD80CD60D3A9B7767E6A360E0643D17ABF80EBECE7B4741923C8BFC`.
- `course-study-guide-builder/SKILL.md`: `B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A`.
- `course-study-guide-builder/references/pedagogy-language-contract.md`: `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`.
- `course-study-guide-builder/references/math-code-case-contract.md`: `CE2313F897B63E74BA59A3AFE1BBC4046D3AA84584072CDA7E76470A7E3CEF9A`.

Guide paths relative to `C:/dev/clsc/burak-papers`; rules relative to `C:/Users/vital/.codex/skills`. Stage 3 and the two repairs remain pending. Token stats unavailable.
