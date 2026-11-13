# Stage 3: connected reader check

Recorded 2026-10-24T18:20:09.672919+03:00. Wall-clock elapsed about 13 minutes 50 seconds from 2026-10-24T18:06:16.7630300+03:00; since preceding checkpoint about one minute. Awake time unverified. Token stats unavailable.

The connected source reading passes for the local additions. The rendered reading needs one repair: M03 is absent as an image because its caption interval breaks generated Markdown. Final diagram records remain pending this repair.

## M01

The chapter defines the activation and its exact spike-driven equation before introducing chosen spike times. The figure then separates events from activation; the following interpretation explains the difference and prepares the firing-rate/input equations. Tau is already introduced. No prerequisite gap is added.

## M02

The fixed states, activation coordinate, rate-to-activation relation, projection and valid interior are taught before the chosen numeric parameters and plot. The takeaway points from constant rate sum to constant D in the lower panel and keeps the interior limit. The following section asks about long delays, a useful next step.

## M03

The chapter introduces the trial density, line Gaussian, wrapping, uniform limit and squared-error convention before the plot. Its introduction fixes D and plotted quantities. The takeaway connects density convergence to bounded angular error and contrasts continuing line growth. The next paragraph changes to state-dependent D, so the constant-D case is complete first. Source flow passes, but the actual figure is absent in rendered HTML.

## Source links

The opening explains PDF page/near-passage behavior and the lack of numbered original lines. Direct links carry equation, figure or paragraph labels near their supported claim; footnotes retain full references and limitations. No unfamiliar source-link rule is needed to follow the text.

## Required rendered repair F1

At site/chapters/ch-memory-dynamics.html line 423, the caption interval opening bracket makes the M03 figure become literal `![With...` text and a normal link. M01 and M02 are real image elements; M03 is not. Escape the bracket at the generated figure Markdown boundary, preserving the visible caption and meaning, then check the rebuilt M03 image, caption, alt text and takeaway.

No source or reader files were edited by this reviewer. The JSON preserves exact inputs and the initial finding for a later focused recheck.

## F1 focused recheck and final local verdict

Recorded 2026-10-24T18:22:34.118120+03:00. The caption now protects the angular interval with inline math. Its meaning and limits are unchanged. The actual rebuilt HTML contains one image element for each new figure, their complete captions and alt text, and no literal image Markdown. M03 has a proper inline-math interval inside the figure caption. Introductions and takeaways were reread around all three rendered figures. F1 is resolved.

The connected source and rendered reading now pass for this local addition. All three current diagram records in `diagram-review.json` retain the actual independent accuracy, scene, readability, palette and scope judgments plus strongest objections and their resolutions. They pass the executable record validator. All source/file/context/policy bindings were rechecked; an independent BookModel load confirms the current book and Chapter 2 hashes. Earlier review records remain history rather than being silently refreshed.

Whole-book acceptance, external publication and the coordinator browser checks are outside this judgment. Wall-clock elapsed about 16 minutes from the persisted root start; since the preceding checkpoint about two minutes. Awake execution time remains unverified. Token stats unavailable.
