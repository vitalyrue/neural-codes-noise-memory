# Stage 2: Figure 2 necessity and wording review

Local request ID: fig2-stage2-20261103. Independent reviewer: fig2_edit_review. This separate request followed completion of Stage 1. No guide text was edited and no build was run.

Audience: knows expected value, variance, standard deviation and density; needs neural meanings, mechanisms and measurement explained.
Scope: additions to the two chapters and their immediate connected passages, with targeted earlier prerequisite checks. No whole-book acceptance.

UTC start: 2026-11-03T17:51:34Z
UTC end: 2026-11-03T17:52:39Z
Wall-clock duration: 66 seconds
Awake execution time: unverified.

## Reviewed versions

- `content/chapters/02b-memory-long-delays.md`: SHA256 `C0F51C1EC21A8C50230BF7CDFBC0D5A32E6331BD122E24334908E0E3F9C02CEA`
- `content/chapters/11-simulating-memory.md`: SHA256 `D907DA29338C9045DC020DB361CF4111E5CA477BBF4012EB3F70882D114F9AFB`
- Rule source: `C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md`, SHA256 `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`. Applied terminology, first-definition, sentence contribution and deletion rules.

## Passage-based answers

- 02b, Panel B paragraph: retain the two distinct time windows, rates and spike marks. Removing 10 seconds or 10 ms would leave the reader unable to separate the separation of the snapshots from the period collecting spike marks. Peak movement connects the inset to the stored angle. The final persistence sentence supplies the neural consequence, not an extra visual description.
- 02b, Panel C: retain circle/line/bound identities and the inset reference. They tell the reader which marks are observations, predictions and a lower limit; removing one invites a wrong comparison. Sigmoidal is glossed as S-shaped. One new term needs repair, below.
- 02b, Panel D: retain S32 and the boundary explanation. The theoretical curve now has an identified calculation, while the flattening sentence explains why the line ceases to rise. The earlier wrapped-density treatment in 02b (especially lines 58-76) teaches the limiting value, so this local use does not need another derivation.
- 02b, E: retain the two-population reading and the difference as the stored quantity. Those explain what changes when leaving the ring. Linear firing rule and equal inhibition specify why a continuous family is possible. This uses the earlier mutual-excitation and linear-rate treatment without introducing a new unexplained formal method.
- 02b, F: retain the inverse-millisecond conversion and summed-population meaning. These stop the high axis values being mistaken for ordinary single-cell rates. Each sentence contributes either a scale or its neural interpretation.
- 02b, G: retain the rate-difference/time-average explanation, axes and line identities. The link moves exact measurement detail to its appropriate simulation chapter while leaving enough to read G here. The scope limit distinguishes model checking from animal measurement at the point the plot might otherwise be overread.
- 11, measurement setup and equation: retain. Both rates are named before their difference is measured, T and lag are assigned roles, and theta_r is already defined in the immediately preceding coordinate-conversion paragraph. The formula measures a change of differences, not either rate alone. The MSD abbreviation and lag are taught in `01-foundations.md:288-292`; they are not new terms here.
- 11, finite-average explanation: retain. The hat is explained immediately after the equation before further use. The 2-second example makes the allowed start times concrete. Overlap explains why these intervals do not become independent trials, preserving a distinction the audience cannot infer from familiar expected-value notation alone.
- 11, units and prediction: retain the squared conversion and 2 D_r lag comparison. Removing the factor of one million would leave a practical scale mismatch with the published panel. The concluding interpretation states what agreement tests.

## Required finding

1. **02b line 189: `Error bars in C and D are standard errors across 100 trials`.** The audience baseline includes standard deviation but not standard error. The sentence identifies the quantity without explaining whether bars describe trial-to-trial spread or uncertainty in the mean. Earlier teaching checked: reading guide, foundations, persistence and memory dynamics; no preceding standard-error teaching was found. The first explicit definition currently appears later in `04-eye-drift.md:243`, where SEM is explained as uncertainty in the across-cell mean. Add a short meaning here, for example that these bars show uncertainty in the mean across trials rather than the spread of individual trials. Apply the first-definition emphasis and glossary consistency rules at the actual first teaching occurrence. Do not add a derivation of SEM; it is not needed to interpret this figure.

## Optional and retained choices

- Optional source-reading aid: say that the paper calls theta_r `Delta r`. Both are explicitly the same r1 minus r2, so the present guide formula is understandable and this is not a missing mathematical definition.
- No other new phrase requires deletion or a new explanation. Exact rate/difference terminology is usefully repeated because varying the words would blur which quantity is measured.

Stage 2 remains pending the standard-error clarification. Connected reading is a separate Stage 3 request.

Token stats unavailable.
