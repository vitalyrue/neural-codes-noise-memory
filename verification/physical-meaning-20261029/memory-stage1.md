# Memory chapters: independent stage 1 correctness and reasoning

Reviewer: physics_memory_review. Local request ID: memory-stage1-20261029-110850. This identifies this actual reviewer call, not a platform-generated call ID.

Start: 2026-10-29T11:08:50.7846951+02:00.
Initial source-hash checkpoint: 2026-10-29T11:10:18.5367852+02:00.
Readout repair recheck: 2026-10-29T11:10:57.6367259+02:00.

Scope: added claims, changed parameter interpretations, new folds, and connected transitions in the five memory chapters listed below. Current text was read against `edits.json`, with the existing source equations and actual earlier foundations used as context. The first gap-search call had already inspected the local main PDF pp. 2 and 5 and SI pp. 3 and 9 directly. This call rechecked the added claims against those equations. Audience assumes calculus, basic probability, and linear algebra; neuroscience must be taught. This is stage 1 only. Wording and reader-understanding calls remain separate.

## Verdict

No unresolved correctness defect in the reviewed revisions after the focused readout-fence repair. One concrete fold error was found, reported, repaired by the coordinator, and rechecked below. No manuscript edits were made by this reviewer. This is a local revision verdict, not whole-book acceptance or visual verification.

## Passage evidence

### Persistence

`01b-persistence.md:9–15`: the ideal-memory example describes a persistent pattern reached after a cue ends, with no remaining record of the original angle in that maintained state. Read with the immediately following continuous-attractor definition, this correctly explains why a disturbance to another persistent state receives no restoring correction. It does not claim that every biological memory system lacks other cues or error correction. The example is explicitly illustrative.

`01b-persistence.md:21–56`: the rate difference gives theta through division by `2k`; equal rate increments cancel in the difference; opposite increments change it. Adding and subtracting the two rate equations gives `dot x=-a x`, `dot theta=0`. Consequently `1/a` is the common-mode recovery time, and increasing `k` reduces the angular effect of a fixed rate disturbance. The positive-rate restriction and warning about changing a real circuit remain present. The given numerical disturbances still evaluate to 5 and 6.5 degrees.

`01b-persistence.md:68–108`: extra or missing spikes are deviations from the expected synaptic drive. The surviving displacement is distinguished from the part removed by return flow. Independence, zero mean, and constant variance per unit time are explicit in visible prose and repeated inside the mathematical fold. Therefore the visible `Var=2Dt` statement keeps its conditions. The new definition correctly assigns D half the variance growth rate, with coordinate-squared/time units. More retained independent disturbances, or greater disturbance magnitudes at fixed event frequency, increase the variance rate in this model. Doubling D doubles variance and multiplies standard deviation by square root of two. This is not presented as a prediction for changing raw firing rates while leaving network sensitivity uncontrolled.

`01b-persistence.md:138–155`: the visible shared-history explanation is true for accumulated increments. The folded Brownian covariance proof keeps the fixed initial value and independent-increment conditions. The following visible paragraph retains the limits from boundaries, wrapping, feedback, and changing D. Folding has not turned the local/unbounded result into an unrestricted long-time claim.

### Dynamics

`02-memory-dynamics.md:17–29,44–50`: a spike adds one to s_j, so its immediate input increment at cell i is W_ij. Its individual exponential contribution decays with tau. The rate-sign statement is explicitly restricted to an increasing transfer rule. Neither a positive connection nor a larger rate is claimed to improve memory on its own. The text correctly separates the model input variable from measured membrane voltage. The phrase about how long a contribution lasts describes its time scale; the defining exponential already shows that it has no abrupt cutoff at tau.

`02-memory-dynamics.md:95–121`: the loss term `-delta_ij/tau` and recurrent term `phi'(g_i)W_ij` have exactly the claimed roles in the local linear dynamics. The latter converts an activation change to an input change and then a rate change. A larger positive local slope increases this response at fixed weight. The text correctly leaves stability to the combined network dynamics and preserves the small-disturbance/local-mode assumptions before using K. Source: main Eqs. 7–11 and SI S7–S15.

### Long delays

`02b-memory-long-delays.md:72–98`: for the stated positive-weight, linear-rule network, adding the deterministic equations makes the mean activation neutral; subtracting gives relaxation of the activation difference toward b_0 with decay rate `2/tau`. Thus a common activation increase persists while a difference disturbance decays. Both rates are positive exactly when `theta>|b_0|/2`. Theta is correctly identified as an activation coordinate. Increasing theta increases both Poisson variance rates with fixed projection weights, giving `2D=theta/(2tau)`. The new explanation agrees with the direct projection and retains the existing explicit warning about the printed S40 discrepancy. The no-drift and valid-domain conditions remain present for the later variance claim.

### Information and parameter comparison

`03-memory-information.md:214–226`: the new tau explanation stays inside the stated symmetric comparison with rate and input curves held fixed and the network retuned. Since `s_bar=tau r_bar`, the tangent activation difference scales with tau. In the symmetric projection formula, fixed input and rate curves imply `v_i` scales as inverse tau. Conditional Poisson variance rates remain unchanged, so D scales as inverse tau squared. The following paragraph separately holds activation curves fixed, changes rates, and gives inverse tau. These are different comparisons, correctly kept separate. This is not an unqualified instruction to increase tau in an otherwise fixed network.

### Readout

`03b-memory-readout.md:113–199`: the moved hyperbolic-function definitions, separation of variables, finite-L variance, and short-L expansion retain their mathematics. The visible precision equation and interpretation remain connected. The long-time limit, saturation scale, variance ratios, and full-access qualification belong outside the fold. The only initial failure was the closing fence described below; its repair restores that intended scope without changing the equations or assumptions.

## Finding and focused recheck

Initial defect: `03b-memory-readout.md:175` contained `::: For long intervals,`. A read-only Pandoc conversion reported `Div at line 144 column 1 unclosed ... closing implicitly`, printed that closing line as prose, and left later main text inside the mathematical div. This was a real change in what a closed fold would hide, not a wording preference.

Initial readout SHA256: `0777A33C6F25CED45F1995956FCA5E6A2AA8A07A12168C39C31F5E3F15115CB8`.

The coordinator repaired the line to bare `:::`, followed by a blank line and `For long intervals,`. At the recheck timestamp above, this reviewer reread lines 140–201 and repeated the read-only Pandoc conversion. No unclosed-div warning remained; the HTML closed the mathematical div before the long-time paragraph. The interpretation and limited-access section are again outside that fold. Finding closed.

The new persistence folds also passed a read-only Pandoc conversion without unclosed-div warnings. These were direct syntax checks with output in the tool response, not a publication build or browser/pixel check.

## Source and rule SHA256

The first four source values were recorded at the initial hash checkpoint and remained unchanged during this call. The final readout value is from the focused repair recheck.

| File | SHA256 |
| --- | --- |
| 01b-persistence.md | 5BEA2D0482DBC15B2862E5FD2B16ECC8E7F257056D224AEEE2FBE07E370A7EA5 |
| 02-memory-dynamics.md | 869913AA0DFBC2E06145D5458DD0B7F14535E9CFFD985B2122FEA54E1816F858 |
| 02b-memory-long-delays.md | 70B5EFC6650D2B6C1BBF35B0BDAE7A379D80DFF863944A872B45DF257D7B6BAA |
| 03-memory-information.md | 63A62A989B01E89AD8A26A342BF311F987286D75167D8854F708D0A8DE4B2D2C |
| 03b-memory-readout.md, after repair | 3FA9CE95117610C8DFE5E9F0C7995ED4D38FE96674D3B2BDD2AF04D1EBE268D5 |
| course-study-guide-builder/SKILL.md | B78068E9874E6D1D97B2017BF8F940492F9B08FC11B74F20FD75019FF388984A |
| references/pedagogy-language-contract.md | F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A |

No additional preferences were treated as correctness defects. Later stages must still judge wording and the reader's visible learning path.

Completion checkpoint: 2026-10-29T11:12:07.8022718+02:00. Wall-clock duration is measured from the recorded 11:08:50 start. Awake execution time is unverified because no sleep/resume-event check was performed. Token stats unavailable.
