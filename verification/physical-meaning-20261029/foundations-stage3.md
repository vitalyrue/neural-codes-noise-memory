# Foundations stage 3: reader understanding and flow

Independent reviewer `/root/physics_foundations_review`, gpt-6.1-sol high reasoning. Local request `physics_foundations_review-stage3`. Actual tool-clock checkpoints: 2026-10-29 09:14:37 UTC start; 09:15:35 UTC connected-read conclusion. Wall time to conclusion and since previous checkpoint: 58 seconds. Awake execution time unverified; sleep/resume events were not checked.

Read the full current foundations chapter, the reading guide through its audience/reading instructions and shared symbols, the index audience statement, and the current persistence opening through its two-cell setup. Focused acceptance scope: repaired foundations section 1.3 and its connections. Equations and folded paragraphs were read; the conceptual route was then reread with both new folds treated as closed. No edits, builds, or rendered-output checks.

**Result: pass for this local reading path.** The visible explanation supports the requested physical account without opening the formal covariance algebra. No required flow repair found. This does not accept the full book or later chapters.

## What the reader can explain from the visible path

- **What acts on what?** A brain command changes motor-neuron firing, those spikes act on eye muscles, and the muscles turn the eye. This is stated at line 99. Line 103 explains how a common input adds through cells pulling in the same direction, while independent extra/missing spikes partly cancel. It also distinguishes the computed prediction from a physical command.
- **What does covariance tell us?** Lines 103-105 identify the paired quantities as measured and spike-predicted displacement on the same degree scale. The visible definition describes departures from each signal's own average. Correlation compares this co-variation with each spread, so a weak correlation need not mean a small shared movement source. The reader is not asked to derive the calibrated fraction here; the linked eye chapter supplies that later calculation.
- **Why can a large MSD mean different things?** Line 140 contrasts alternating directions with a persistent directional change. Lines 142-148 define the statistic and display/interpet its spread-plus-squared-mean identity. Basic probability supplies variance and expectation. Opening the derivation is optional for this distinction.
- **Which parameter changes which observed feature?** Lines 165-168 distinguish faster accumulated spreading, a changed mean, a squared gain effect on the command contribution, and stronger temporal smoothing at shorter lags. The visible gain sentence holds input fluctuations fixed and separates later noise. D is a preview of the next chapter's spreading calculation, not a hidden prerequisite for using these distinctions.
- **Could the recorded curve rise without more eye movement?** Line 170 says yes: independent position errors add an offset to displacement MSD. The endpoint-independence and movement-independence assumptions are visible. The linked derivation is optional for this qualitative warning.

The reader does not need the hidden S/epsilon construction to follow these answers. That construction permits a more exact check of calibration and noise assumptions; it is not silently used to supply a missing visible causal step.

## Needed terms and where they are supplied

Neurons, spikes, rates, synapses and recurrence are taught in the reading-guide opening and foundations lines 9-19. Tuning slope and degree conversion occur at line 19. The population-code paragraph supplies the distinction between a value and the activities representing it, and the count section supplies basic spike variability. Motor neurons are identified by their action on muscles at line 99. Shared input and each cell's own variation are described before “private noise” is used at lines 103-105. Covariance/correlation receive visible meanings at line 105; undergraduate basic probability supplies averages and spread. Lag is explicitly the time between two measurements at line 140. That sentence defines displacement as change in eye angle. MSD is both introduced in the reading guide and explained again at line 142. The gain bullet defines gain by the multiplication it performs. Smoothing is described as suppressing rapid changes at line 168. None of these visible uses requires the formal fold first.

## Paragraph purposes and order

Each hash below is the first 12 hexadecimal digits of SHA256 of that source paragraph's UTF-8 text without its line ending. Line numbers refer to current `01-foundations.md`. Retain decisions include the surrounding equation or fold title where indicated. Pure fence, div and blank-line markup adds no separate reader claim.

| Line/hash | Purpose and connection | Decision |
| --- | --- | --- |
| 3 / ADA6616FE370 | Sets the shared representation problem, then distinguishes the papers' questions. | Retain. |
| 5 / 349745A3BCA8 | Places spikes, uncertainty, shared variation and mean change in the chapter's teaching order. | Retain. |
| 99 / 18AB4A7CB2F4 | Establishes observed eye movement, physical signal chain, and private variability. | Retain. |
| 101 / 4DEA63CEC712 | Turns that problem into two measurement questions and limits circuit inference. | Retain. |
| 103 / 426602416288 | Explains shared addition/private cancellation and identifies the two recorded displacement quantities. | Retain. |
| 105 / 19C7860866DD | Gives intuitive covariance/correlation and explains the danger of reading correlation as a shared fraction. | Retain. |
| 109 / 206B2BA07DD1 | Inside the clearly titled mathematical fold, defines variables before the covariance equation. | Retain, folded. |
| 115 / 8CABCD64A60D | Adds units and the sum/difference identity needed for later variance calculations. | Retain with equation, folded. |
| 121 / B7C88FC555EB | States the nonzero-variance condition before formal correlation. | Retain with equation, folded. |
| 127 / FA5B38DB550A | Interprets scale and limits the reverse independence inference. | Retain, folded. |
| 129 / 71120C18D428 | Makes shared/private roles concrete before computing their covariance and variance. | Retain with equations, folded. |
| 136 / C8047818C6BF | Interprets private variance and gain, and limits this simplified construction. | Retain, folded. |
| 140 / 3FAD765F29F8 | Resumes the visible route by defining lag/displacement and contrasting wandering with directional error. | Retain. |
| 142 / 693F2D1DDB89 | Names MSD, states units and introduces its decomposition after the physical contrast. | Retain with identity. |
| 148 / 4C8E0D90FB6A | Converts the identity into the measurement decision: inspect the mean separately. | Retain. |
| 152 / 4BCB2EF0A739 | Starts the optional centered-variable derivation. | Retain with expansion, folded. |
| 159 / 3BB7E52E20EE | Explains the disappearing cross term and finite-moment condition. | Retain, folded. |
| 163 / 62F9606ED740 | Changes from interpreting statistics to identifying which physical part a parameter controls. | Retain. |
| 165 / C8238836A1F1 | Connects lasting random command changes to spreading and the next chapter's D. | Retain. |
| 166 / F417BF21A23A | Connects persistent directional change to mean and squared bias at fixed lag. | Retain. |
| 167 / 3D99D5A4BC3F | Separates command scaling from later noise and fitted tuning slope. | Retain. |
| 168 / 45070397F7C3 | Adds a time-dependent shape effect distinct from amplitude. | Retain. |
| 170 / 56434EE79D4D | Separates recorded error from physical movement under visible assumptions. | Retain. |
| 172 / 60159BECA4E1 | Returns to the stored command whose stability is the next chapter's problem. | Retain. |

Reference footnotes identify evidence rather than introduce an extra explanatory step. The existing Poisson figure and callout were read as prior context; they are unchanged and do not need rebuilding for this local flow review.

## Connected-read conclusion

With the folds closed, the route remains: the eye moves despite a fixed target; common and private activity have different combined effects; covariance compares recorded changes; mean and spread distinguish directional error from wandering; the parameter list separates effects on movement; recording error is counted separately. The current persistence opening then asks which changes in neural activity alter the represented value and which fade, so the handoff has a direct purpose. Moving the formal definitions before the physical setup would interrupt this progression without supplying a needed visible premise. No reordering is warranted in this scope.

## Version evidence

- Foundations SHA256: `E4FD06733F893BF1334702F3D7045844415A988032CC0B583105833CD430E42A`.
- Reading guide SHA256: `07945A554F76591A8554F5F928D2F22F1EE52F8D5B13EB4D2750D38CB1D5227E`.
- Current persistence SHA256: `5BEA2D0482DBC15B2862E5FD2B16ECC8E7F257056D224AEEE2FBE07E370A7EA5`.
- Index SHA256: `361396B67AD80CD60D3A9B7767E6A360E0643D17ABF80EBECE7B4741923C8BFC`.
- Pedagogy-language rule SHA256: `F4C1EB544CF640B708E1970D9572FDC758FCC6AEA806675D01A0256658DF847A`.
- Math-code-case rule SHA256: `CE2313F897B63E74BA59A3AFE1BBC4046D3AA84584072CDA7E76470A7E3CEF9A`.

The repeated blue MSD explanation is retained under the user's explicit preference, as recorded in the stage 2 addendum. Token stats unavailable.
