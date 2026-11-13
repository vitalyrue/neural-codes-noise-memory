# Linked Chapter 2 draft check

Checked: 2026-10-24T18:16:59.769298+03:00

Status: pass. All 48 Markdown PDF links have correct source pages and equation, figure or paragraph labels. All 14 footnote definitions and 16 calls were mapped. No wrong source links found.

All 170 math expressions are unchanged from baseline. Source qualifications remain, including formula discrepancies, guide-only examples, boundary conditions, weak-noise limits, activation/rate coordinate rescaling and correlated-noise limits. The four YAML captions clearly identify teaching calculations.

The three initial focus issues for S18, S37 and S41 are resolved with tight equation boxes. One PDF point of integer rounding in an offset is harmless.

## Post-build check

`check_links.py` is syntax checked and ready. It checks only built Chapter 2 HTML and its linked PDF copies: PDF hashes/page counts, all link labels and targets, fragment syntax/bounds, expanded footnotes, duplicate IDs, unresolved placeholders and static math/block errors. No other HTML is opened. The source has 48 PDF links; expected HTML has 54 because repeated model and projection notes add 2 and 4.

Runtime and two representative native PDF target checks remain pending after build. External DOI resolution and whole-book checks were not rerun.

## All link labels

| Number | Label | PDF page | Verified locator |
|---|---|---|---|
| 1 | Model, Eqs. 7–9, p. 5 | 5 | main-model |
| 2 | SI Eqs. S2–S5, p. 2 | 2 | si-gaussian |
| 3 | SI Eqs. S12–S13, p. 3 | 3 | si-left |
| 4 | SI Eqs. S14–S15, p. 3 | 3 | si-project |
| 5 | SI Eq. S18, p. 4 | 4 | si-s18 |
| 6 | main Eq. 2, p. 2 | 2 | main-eq2 |
| 7 | Fig. 2E–G, p. 3 | 3 | main-fig2-caption |
| 8 | SI Eq. S31, p. 7 | 7 | si-wrapped |
| 9 | SI Eq. S37, p. 8 | 8 | si-s37 |
| 10 | SI Eq. S41, p. 9 | 9 | si-s41 |
| 11 | Fig. S1, p. 10 | 10 | si-excitation-fig |
| 12 | SI “Systematic drift,” pp. 4–5 | 4 | si-drift-limit |
| 13 | Discussion, p. 5, paragraph beginning “Our spiking model” | 5 | main-correlations |
| 14 | Figure 1A, p. 2 | 2 | main-fig1 |
| 15 | Figure 2, p. 3 | 3 | main-fig2 |
| 16 | Main Eq. 1 and the steady state, p. 2 | 2 | main-steady-state |
| 17 | Model, Eqs. 7–9, p. 5 | 5 | main-model |
| 18 | Weak Fluctuations, Eqs. 10–11, p. 5 | 5 | main-weak |
| 19 | continuation, p. 6 | 6 | main-large, main-two-sim |
| 20 | SI Eqs. S2–S5, p. 2 | 2 | si-gaussian |
| 21 | Eq. S1, p. 1 | 1 | si-population |
| 22 | Eqs. S2–S5, p. 2 | 2 | si-gaussian |
| 23 | ring population limit, Eq. S6, p. 2 | 2 | si-ring-large |
| 24 | linearization, Eqs. S7–S10 | 3 | si-linearization |
| 25 | tangent, Eq. S11 | 3 | si-tangent |
| 26 | left vector, Eqs. S12–S13 | 3 | si-left |
| 27 | projected diffusion, Eqs. S14–S15 | 3 | si-project |
| 28 | Eq. S21, p. 5 | 5 | si-multid-start |
| 29 | Eqs. S22–S27, p. 6 | 6 | si-multid |
| 30 | main Eq. 2, p. 2 | 2 | main-eq2 |
| 31 | Supporting Text, Eqs. S16–S18, p. 4 | 4 | si-symmetric |
| 32 | Fig. 2E–G and caption, p. 3 | 3 | main-fig2-caption |
| 33 | Network Simulations, mutual inhibition, p. 6 | 6 | main-large, main-two-sim |
| 34 | density equation, Eqs. S28–S29, p. 7 | 7 | si-fp |
| 35 | Gaussian on a line, Eq. S30, p. 7 | 7 | si-gaussian-line |
| 36 | wrapped density and uniform limit, Eq. S31, p. 7 | 7 | si-wrapped |
| 37 | angular error, Eq. S32, p. 8 | 8 | si-wrapped-moment |
| 38 | Supporting Text, Eqs. S33–S37, p. 8 | 8 | si-variable |
| 39 | Supporting Text, Eqs. S38–S41, p. 9 | 9 | si-excitation |
| 40 | Fig. S1, p. 10 | 10 | si-excitation-fig |
| 41 | “Systematic drift,” p. 4 | 4 | si-drift-limit |
| 42 | Eqs. S19–S20 and continuation, p. 5 | 5 | si-drift |
| 43 | Discussion, p. 5, paragraph beginning “Our spiking model” | 5 | main-correlations |
| 44 | Fig. 1 and caption, p. 2 | 2 | main-fig1 |
| 45 | flow definition, “In what follows,” p. 2 | 2 | main-flow-definition |
| 46 | Fig. 2 and caption, p. 3 | 3 | main-fig2 |
| 47 | ring model, p. 6 | 6 | main-ring-sim |
| 48 | mutual inhibition, p. 6 | 6 | main-large, main-two-sim |

## All footnotes

- `p1-model`: 2 call(s); correct targets for main-model, main-steady-state.
- `p1-weak`: 1 call(s); correct targets for main-weak, main-large, si-gaussian.
- `p1-large`: 1 call(s); correct targets for si-population, si-gaussian, si-ring-large.
- `p1-projection`: 2 call(s); correct targets for si-linearization, si-tangent, si-left, si-project.
- `p1-multid`: 1 call(s); correct targets for si-multid-start, si-multid.
- `p1-symmetric`: 1 call(s); correct targets for si-symmetric, main-eq2.
- `p1-two`: 1 call(s); correct targets for main-fig2-caption, main-two-sim.
- `p1-fp`: 1 call(s); correct targets for si-fp-intro, si-fp, si-gaussian-line, si-wrapped, si-wrapped-moment.
- `p1-variable`: 1 call(s); correct targets for si-variable.
- `p1-excitation`: 1 call(s); correct targets for si-excitation, si-excitation-fig.
- `p1-systematic`: 1 call(s); correct targets for si-drift-limit, si-drift.
- `p1-correlation`: 1 call(s); correct targets for main-correlations, si-linearization, si-project.
- `p1-fig1`: 1 call(s); correct targets for main-fig1, main-flow-definition.
- `p1-fig2`: 1 call(s); correct targets for main-fig2, main-ring-sim, main-two-sim, si-wrapped-moment.

Wall-clock elapsed since 2026-10-24T18:06:16.7630300+03:00: 643.0 seconds. Awake time unverified. No reader files edited. Token stats unavailable.

Follow-up 2026-10-24T18:18:49.149294+03:00: W1-W4 wording changes leave all48 link label-target pairs unchanged. All170 original math expressions are preserved exactly in order; 6 new math expressions occur in added teaching text (176 total). Locator map hash unchanged. Updated draft hashes saved in JSON.

Final built-page check 2026-10-24T18:19:16.217866+03:00: PASS. Exactly54 rendered source PDF links match the48 Markdown links after repeated footnotes expand. Both PDF copies match their source hashes and6/20 page counts. All16 footnotes render; no duplicate IDs, invalid fragments, unresolved placeholders or static math/block errors. Only Chapter2 HTML and itsPDF copies were checked. Canonical Markdown equals the reviewed draft and the source locator map hash is unchanged. Root owns native PDF/MathJax browser checks.

Final checkpoint 2026-10-24T18:19:30.178616+03:00. Wall-clock elapsed 793.4seconds; since previous checkpoint 41.0seconds. Awake time unverified. Token stats unavailable.

Final caption-fix rebuild check 2026-10-24T18:21:44.965409+03:00: PASS. Added figure checks require4 actual image nodes in Chapter2 figure elements, the3 new asset paths plus retained tilted-decay path, existing asset files, and no literal ![ in main text. All pass. The54 rendered PDF links,16 notes, PDF hashes/page counts, IDs/fragments/placeholders and static math checks also pass. Earlier pass covered links and static markup; it did not yet check actual figure nodes. Current HTML SHA256: `f339c53482fc90ceb4112f24940a629b801677d9e60055e0a9f295c6b2ca6511`. Reader Markdown unchanged and source locator map remains frozen.

Final checkpoint 2026-10-24T18:22:05.830774+03:00; wall-clock elapsed 949.1seconds; since previous checkpoint 155.7seconds; awake time unverified. Token stats unavailable.
