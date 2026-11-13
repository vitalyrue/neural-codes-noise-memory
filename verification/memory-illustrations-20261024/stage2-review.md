# Stage 2: necessity and wording

Recorded: 2026-10-24T18:17:34.043498+03:00. Reviewer: /root/review_memory_illustrations, GPT 6.1 sol, high reasoning. Root start 2026-10-24T18:06:16.7630300+03:00. Wall-clock elapsed about 11 minutes 15 seconds; since the 18:15:40 checkpoint about 1 minute 50 seconds. Awake execution time unverified. Token stats unavailable.

The new source links, captions, alt descriptions and M01 text can stay. Four short paragraphs around M02 and M03 repeat conclusions already supplied immediately before the figures and in their captions. Replace those paragraphs with the precise text below. The replacements identify chosen inputs or connect the plotted panels. No old mathematical explanation needs rewriting.

## W1: Chapter 2, line 257

Original: The mutual inhibition example makes the distinction between individual rates and their contribution to diffusion visible.

Replacement: The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

The original only announces that the figure makes a distinction visible. The preceding paragraph has already explained that distinction. State the chosen inputs so the reader can connect the numerical curves to the symbolic example.

## W2: Chapter 2, line 265

Original: The individual rates vary with the stored value, but their summed variability and therefore the local diffusion coefficient remain constant inside the valid range.

Replacement: The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$.

The original repeats the preceding derivation and caption. The replacement connects the two plotted panels directly and keeps the interior-domain limit.

## W3: Chapter 2, line 312

Original: Wrapping the Gaussian around a circle changes long delay errors even when the local diffusion coefficient stays constant.

Replacement: For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay.

The original repeats the immediately preceding explanation. The replacement introduces what is actually plotted and its chosen diffusion coefficient.

## W4: Chapter 2, line 320

Original: A flattening angular error curve can follow from the bounded way error is reported; it does not require the local noise mechanism to weaken.

Replacement: As the upper density approaches uniform, the wrapped error below approaches $\pi^2/3$; the line error keeps growing.

The existing paragraph immediately before the figure and its caption already explain unchanged local noise and bounded error. The replacement interprets the relationship between the two panels without repeating that conclusion a third time.

## Retained wording and first use

- Chapter opening, paper-link note: Explains the PDF locator behavior and the lack of numbered original text lines. Viewer support is qualified; SI is expanded at first use.
- M01 introduction and interpretation, lines 27 and 35: The introduction identifies chosen input events before the plot. The interpretation distinguishes spike events from the state they leave behind, which is the local teaching task. No added technical name or missing first use.
- All three captions and alt descriptions: They retain chosen parameters, analytic versus paper-data status, plotted relationships, units and domain conventions. Each is needed for a figure inspected separately. Repetition of essential limits in a caption is justified.
- Plot labels and legends: Activation, rates, D, density and angular error have already been taught before each plot. Symbols and units identify the plotted quantities without new specialist vocabulary.
- 48 paper links and all 14 footnotes: Equation/figure/paragraph labels are the requested means of inspecting exact source support. Complete references and source-discrepancy limits remain necessary. Longer references can be scanned without reading every item as narrative.

Apply corresponding changes to the figure brief and ledger introduction/interpretation fields so their text matches the reader source. Captions, alt text, pixels, source limits and the retained mathematical derivation stay as inspected.

This is Stage 2 only. The JSON records the current canonical input hashes and exact edits. After the edits, request a focused truth check of the four replacements, a Stage 2 recheck, and the separate connected-flow Stage 3. No reader files were edited by the reviewer.
