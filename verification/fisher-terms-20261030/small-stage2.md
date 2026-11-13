# Independent stage 2: necessity and terminology

Reviewer: `/root/terms_observations`. Local request ID: `terms-observations-stage2-20261030-125436` (local label, not platform call ID). Start: 2026-10-30T12:54:36.3158262+02:00. Reviewed the current midpoint repair in `content/chapters/02b-memory-long-delays.md:127-158` and five glossary entries. The reviewer did not write these passages. This is stage 2 only; no stage-3 review or manuscript edit was performed.

Audience correction preserved: expected value, variance, standard deviation and probability density are known. No general probability or statistics primer is needed for this scope.

Verdict: retain the added explanation and entries. No required necessity/terminology correction found. The small wording changes since stage 1 keep the same mathematical claim and limits; none creates a new truth question requiring another full stage-1 pass.

## Midpoint section

| Passage | Need, word meaning and decision |
| --- | --- |
| `02b-memory-long-delays.md:129-134` | The section's question is whether random spreading establishes movement of the average. That distinction is necessary for the next convention comparison. “Systematic drift” is explained as nonzero mean velocity, while “microscopic jump process” points back to individual spike events and the jump model in `02-memory-dynamics.md:73-87`. Retain; replacing it by a vague “noise model” would lose the required connection to individual neural events. |
| `:139`, first three sentences | “Where the coefficient is evaluated” is immediately made concrete by midpoint evaluation, contrasted with the earlier starting-point Itô definition at `:17`. The exact name Stratonovich is needed to identify the source's mathematical alternative. “Same written coefficient and zero written drift” prevents readers from confusing a convention change with two equivalent formulas that include different drift terms. Retain. |
| `:139`, positive/negative-step explanation | Adds the mechanism missing from a name or formula alone. A larger or smaller sampled noise amplitude changes the two step sizes differently. “Stronger noise” refers to the amplitude in the coefficient, not additional force introduced elsewhere. The following folded definition `b=sqrt(2D)` makes this relation explicit for the calculation. Retain; no additional noise terminology is needed. |
| `:139`, conversion and source limit | Gives the result `D'/2` after the physical reason and keeps its role as a possible drift scale distinct from an established neural drift. This limit is needed even for readers who leave the derivation closed. Retain. |
| `:143-147` | The temporary name `b` shortens the Taylor calculation and is defined before use. “Positive and smooth” is an actual local condition for using the square root and its derivatives, not removable caution. Midpoint `theta+Delta theta/2`, the expansion and leading substitution each contribute a necessary step. No undefined specialist term is introduced here. Retain. |
| `:150` | The increment moments, differentiation of `b^2`, and constant-`D` check explain the factor and its limit. “The squared-increment term contributes to the limit” now states its role directly and refers to the displayed `(Delta W)^2`, not a new unexplained object. Splitting the final limit into two sentences preserves the distinction between explaining a convention and choosing one for neurons. Retain. |
| `:154-158` | The scale estimate connects the added derivation to the paper's small-noise approximation. The following interpretation explains why subtracting a mean cannot remove random increments and preserves the independence limits. These are connected constraints on the result rather than an unrelated new lesson. Retain. |

The main-text limit and the folded note's limit have separate jobs: the first protects readers who skip the note; the second qualifies the calculation at its conclusion. Their brief repetition does not require deletion.

## Five glossary entries

| Passage | Need and terminology decision |
| --- | --- |
| `glossary.md:28`, estimator | Needed for repeated readout and error-bound uses. “A rule that converts observed data into an estimated value” defines it plainly; the next sentence attaches it to spikes and the represented coordinate. Retain. |
| `glossary.md:35`, Fisher information | The first sentence supplies the nearby-change meaning; “expected squared score” preserves the exact definition for lookup, supported by the score entry and derivation. The Poisson sentence gives the special form's meaning without claiming it is universal. The link points to full teaching. Each part has a different job. Retain. |
| `glossary.md:67`, median filter | The operation and its effect on small fields are both needed to read the processing discussion. “Middle-ranked value” identifies replacement by an ordered neighborhood value and avoids asserting an average of two central values for the source's even-sized neighborhood. The connected main text supplies the bin setting. Retain; no larger filtering lesson needed. |
| `glossary.md:75`, one sided t test | “In a specified direction” distinguishes the one-sided question. The normalized mean difference gives the test's operation, and the final sentence identifies the actual eye-study question. “Estimated sampling uncertainty” is made concrete by `s/sqrt(n)` in the connected teaching at `04-eye-drift.md:120`. Retain. |
| `glossary.md:99`, Spearman correlation | The rank replacement explains what acts on what. The next sentence gives the question asked and the absence of a linear-relation requirement. The ordinary correlation calculation is already taught; a fresh derivation or general dependence survey would not help this lookup entry. Retain. |

No added term needs a further standalone definition within these passages. No optional wording preference is being treated as a defect. Scientific correctness remains the prior stage's separate call; this record does not expand its scope. Token stats unavailable.

## Time and source evidence

Actual completion, wall-clock duration and SHA256 values follow. Awake execution time is not separately verified because Windows sleep/resume logs were not inspected. Hashes identify current reviewed files at completion rather than an initial freeze.

Completion: 2026-10-30T12:55:17.0231387+02:00
Wall-clock elapsed and time since previous checkpoint: 40.7 seconds.
```
content/chapters/02b-memory-long-delays.md A088BAE67645F1CEAA3389C8ED71700ECD24C9FCD010B8997F6ADEE0CED978A7
content/chapters/glossary.md 86944917BF60F4128BB7B06AAE1AD872BEFEDA2587F02EC3927447731BF476D3
content/chapters/02-memory-dynamics.md 622A08B479A8586B17FF7A8F7D847253123393EF6A64EE9A91FB52AAB69E577F
content/chapters/03-memory-information.md 1FA7A49F1741511F9827612EBB5FCAE35ECB27399673828C4D7A6D8B9906CCBE
content/chapters/04-eye-drift.md A6393AA211E9B38D16E0620B7B67D240F24E35A8DDDB5C200CD5CF0B9E218C52
content/chapters/04c-eye-circuit.md EB8DF5D89C1242A4703365D524F2688CA66F0E927229750BE08D44172FEE7E8B
content/chapters/05c-place-tests.md 3C42CBCC4F12F80799B169172E8FA59028C5CD7CB3361033C1E8B82C9B71FC16
```
