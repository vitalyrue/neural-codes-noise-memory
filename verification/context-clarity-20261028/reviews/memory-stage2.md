# Memory repairs: separate stage 2 wording and necessity review

Started: 2026-10-28T15:42:03+02:00. Completed: 2026-10-28T15:42:53.653173+02:00.

Scope: M1-M6 revised passages and their connected explanation in the five memory Markdown files. Audience: undergraduate math, no neuroscience. This is a separate wording/necessity call after the truth/context call. It does not repeat the source or formula audit. No manuscript edits.

## Required fix

File: 01-foundations.md, FOUNDATIONS-COVARIANCE, final prose paragraph.

Current text:

> Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both. This identity will help distinguish random spreading of a stored value from a systematic change in its average.

Exact replacement:

> Thus a growing mean squared displacement can contain random spread, a systematic change in the mean, or both.

Reason: the first sentence already interprets the identity and states the two possibilities. The second sentence repeats those same possibilities and promises later usefulness without adding a condition, mechanism, example or connection the reader needs. Removing it loses no teaching. This applies the skill's deletion test and rule against restatement; it does not undo the removal of the unexplained integrator term.

## Other changes

Retain the other additions. The outgoing-spike sentence identifies what s_i measures; the rate extension identifies what changes gradually; the symmetry sentences explain the patterns being shifted; the common-input sentence names the effect on rates; and the recipient sentence clearly separates the receiving neuron from the sending memory circuit. These contributions earn their space. The integration paragraph distinguishes accumulated value, mean, variance and leak without unexplained new machinery.

No further required wording repair found. Terms such as synaptic activation, transfer function, time constant and continuous attractor have earlier teaching and are used with their existing meanings. The references and transitions surrounding the changes have clear subjects; the separate flow call remains pending.

## Current file hashes

| File under guide/content/chapters | SHA-256 |
|---|---|
| 01-foundations.md | 5cdf42d7ef8aa1e11a21e1ceef450382170bcaed9acf052f20d7bb82d82ef63e |
| 02-memory-dynamics.md | f21241a321a3f30f1895e0b7e1fc52e119bcc14a18887811ede4328e7004132e |
| 02b-memory-long-delays.md | 8586645d980d1392b638b210b04ddbcd377f8c9ac9e90711398629b45ef5c563 |
| 03-memory-information.md | 0493ce19f0101b56b8299939ffb23f7ed2e13568a048742cbff2ba2ca2a736c1 |
| 03b-memory-readout.md | 40838058f6eade08eae8425e0bc055531a46955dd0b489c634b2575f83e75452 |

Rules: course-study-guide-builder SKILL.md and pedagogy-language-contract.md, already read. Relevant rules are deletion test, plain words and precise terms, concrete referents, and teaching each point once. This is a scoped review, not whole-guide acceptance.

Awake execution time was not verified from sleep/resume events. Token stats unavailable.
