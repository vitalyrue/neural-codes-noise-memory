# Memory repairs: separate stage 3 connected-reader review

Started: 2026-10-28T15:43:32+02:00. Completed: 2026-10-28T15:44:41.498794+02:00.

Audience: undergraduate calculus, basic probability and linear algebra; no neuroscience assumed. Scope: revised memory passages with their preceding and following paragraphs, the earlier spike-to-input equation, the two-cell example, the figure comparison, and the information-to-readout connections. No edits or repeated whole proof audit. Metadata purposes were outside this call.

Stage 2 deletion verified: the repeated final foundations sentence is gone. The remaining MSD sentence fully interprets the displayed identity. No new gap or rough transition results.

## One remaining reader-understanding repair

File: 03b-memory-readout.md, MEMORY-EXTENSIONS, immediately after the two-stage equation, line 230 in the reviewed snapshot.

Original:

> The activation noise retains its Poisson strength.

Exact replacement:

> Here $\xi_i$ is the zero mean noise from variable spike generation, with the same Poisson strength as in the basic model.

Reason: the newly expanded introduction names both time constants and the rate adjustment, but the displayed extension introduces xi_i without identifying it. Earlier teaching uses dN, dM and Brownian increments rather than xi_i. A reader should not have to decide whether this new term is an outside signal or the intrinsic spike fluctuations already taught. The current sentence gives the noise strength but never directly maps the symbol to its source. This small mapping adds no new mechanism and preserves the strength qualification. It is a reader gap noticed in this separate connected call; it does not change the stage 1 truth verdict on the additions.

Support already established in Stage 1: the extension retains the basic activation-noise source while adding rate relaxation. Main Methods Eqs. 10-11 and SI S84 supply that role. The existing paragraph immediately follows the equation, so replacing its first sentence is enough; no chapter reordering is needed.

## Connected reading otherwise passes

- Outgoing spikes, their lingering activation, connection weights, received input and new firing now have clear roles in reading order.
- The common-input example explains why averaging cannot remove shared changes; the following conditional-independence paragraph preserves the distinction.
- Translation symmetry is explained beside the symmetric-weight result. The ring comparison later applies rotational symmetry to its activity pattern and contrasts the two-cell circuit.
- The information opening identifies the receiving neuron and sending circuit before presenting estimation uncertainty.
- The final integration paragraph explains what is accumulated before distinguishing its persistence from the useful readout interval and from leak. The algebraic example before it remains a separate bound check; the paragraph returns to the biological interpretation without requiring a new formal definition.

No other required flow or referent repair found in the scoped changes. This is not whole-guide acceptance.

## Current file hashes

| File under guide/content/chapters | SHA-256 |
|---|---|
| 01-foundations.md | a1f5aa388ddba71a1492b0fb7b512347fb0c0d0684812827797a022279e3ccca |
| 02-memory-dynamics.md | f21241a321a3f30f1895e0b7e1fc52e119bcc14a18887811ede4328e7004132e |
| 02b-memory-long-delays.md | 8586645d980d1392b638b210b04ddbcd377f8c9ac9e90711398629b45ef5c563 |
| 03-memory-information.md | 0493ce19f0101b56b8299939ffb23f7ed2e13568a048742cbff2ba2ca2a736c1 |
| 03b-memory-readout.md | 40838058f6eade08eae8425e0bc055531a46955dd0b489c634b2575f83e75452 |

Rules: course-study-guide-builder SKILL.md and pedagogy-language-contract.md, already read, especially first reasoning-dependent use, concrete actors and objects, and connected narration. Awake execution time was not verified from sleep/resume events. Token stats unavailable.
