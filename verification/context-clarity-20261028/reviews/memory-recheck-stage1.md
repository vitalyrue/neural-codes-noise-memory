# Memory repairs: independent stage 1 truth and context recheck

Started: 2026-10-28T15:40:21+02:00. Completed: 2026-10-28T15:41:35.135805+02:00.

Required repairs: none found in the six repair groups (M1-M6, including their linked subchanges).

Scope: current changed paragraphs and connected explanation in the five memory Markdown files below; the edit record; relevant 2012 main-text and supplement passages. Audience: undergraduate calculus, basic probability and linear algebra; no neuroscience assumed. This call checks truth, causal roles, quantity meanings and evidence limits. Separate wording and flow calls remain pending. No manuscript edits, rendered checks, broad proof audit or whole-guide acceptance.

Checks supporting this result:

- M1: The activation belongs to the sending cell's outgoing spike train. The following weights W_ij determine its effect on receiving cell i. This matches main Results lines 99-106 and Methods Eqs. 7-9. The displayed jump-and-decay formula retains its one-unit jump convention.
- M2: The foundations sentence correctly interprets the MSD identity without prematurely requiring an integrator definition. The readout passage makes accumulation conditional on using the circuit as an integrator. Its distinction between an accurate mean with increasing variance and a restoring leak matches SI “Integration time constant,” lines 930-938, and main Discussion lines 617-627. It does not turn a short useful observation interval into a short storage lifetime.
- M3: The basic r_i=phi(g_i) relation changes immediately with total input. The extension's tau_m derivative equation approaches that same rate gradually, while s retains its separate decay. This agrees with SI S84 and the explicit source statement that averaging follows the nonlinearity. The surrounding text retains symmetric weights, the location of spike noise, and the restriction to this two-stage model. The negative lower-right matrix block follows directly from S84, as the existing footnote explains.
- M4: The symmetry explanations distinguish equal opposite connection weights from shifting an activity pattern. Ring weights depend on preferred-angle differences; the two-cell mutual-inhibition design need not have that rotational symmetry. Main Results lines 174-217 and ring Methods support the comparison. The earlier large-population qualification remains in place; this repair does not add a finite-network guarantee.
- M5: The common input is identified by its stated effect on several cells' rates. The sentence does not claim a measured biological source or unconditional independence of whole spike trains. The next connected paragraph correctly limits independent elementary spike generation to conditioning on the current model state.
- M6: The recipient neuron and sending memory circuit are now distinct. The sentence states a possible use of received spikes, not a measured biological decoding mechanism or a guarantee of perfect recovery. The following information calculation retains its locally constant state and conditional Poisson assumptions. Main Discussion lines 587-591 and SI readout lines 649-658 support this role.

No changed statement removes the existing source discrepancy warnings, noise conditions, readout limits or experimental qualifications. I did not recalculate every unchanged derivation.

## Reviewed current file hashes

| File under guide/content/chapters | SHA-256 |
|---|---|
| 01-foundations.md | 5cdf42d7ef8aa1e11a21e1ceef450382170bcaed9acf052f20d7bb82d82ef63e |
| 02-memory-dynamics.md | f21241a321a3f30f1895e0b7e1fc52e119bcc14a18887811ede4328e7004132e |
| 02b-memory-long-delays.md | 8586645d980d1392b638b210b04ddbcd377f8c9ac9e90711398629b45ef5c563 |
| 03-memory-information.md | 0493ce19f0101b56b8299939ffb23f7ed2e13568a048742cbff2ba2ca2a736c1 |
| 03b-memory-readout.md | 40838058f6eade08eae8425e0bc055531a46955dd0b489c634b2575f83e75452 |

## Supporting file hashes

| Project-relative file | SHA-256 |
|---|---|
| research/burak-fiete-2012-main.txt | 10a33ffff51519638bae8f54b97994e1235646be284189e86a33e077ee291354 |
| research/burak-fiete-2012-si.txt | e92cb5b43d206ed99eca6e916cc702f89908228d913176aa850aad9201915552 |
| guide/verification/context-clarity-20261028/edits-memory.json | 1f837211b58e650d3bccfba48181f656861106cec44ef43cd05d0657aabdba71 |

Applicable rules: course-study-guide-builder SKILL.md and pedagogy-language-contract.md, already read in this review session. Their hashes remain B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A and F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A.

Wall-clock checkpoints above include any pause. Awake execution time was not verified from sleep/resume events. Token stats unavailable.
