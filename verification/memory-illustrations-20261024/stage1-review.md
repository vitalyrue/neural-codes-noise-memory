# Stage 1: truth, reasoning and figure judgment

Recorded 2026-10-24T18:15:40+03:00. Reviewer: /root/review_memory_illustrations, GPT 6.1 sol, high reasoning. Local request: memory-illustrations-20261024-stage1. Root task start: 2026-10-24T18:06:16.7630300+03:00. Wall-clock elapsed about 9 minutes 23 seconds; since the 18:13 checkpoint about 2 minutes 40 seconds. Awake execution time remains unverified because Windows sleep/resume events were not checked. Token stats unavailable.

## Decision

Accept M01, M02 and M03 as candidate assets for local insertion with their inspected captions, alt text and connected explanations. No required mathematical or pixel correction remains in this scope. This is an independent asset judgment and a Stage 1 judgment of the proposed changes. It does not complete the separate wording and reader-flow stages, browser link behavior, or final canonical hash binding.

The detailed record is `stage1-figure-judgments.yaml`: 86 individual label, caption, alt, introduction, interpretation, leader and marker judgments, five separate criteria per figure, all six required scene judgments, strongest objections and their resolutions, actual inspected asset hashes, and a focused recheck of coordinator changes. The canonical chapter was being prepared during review; no final compiled source hash is invented.

## Inputs actually checked

- All three full-resolution PNGs and their separate 700 px previews. M03 was also opened with original-resolution detail after the first display resize.
- The three current content briefs, pending contracts, final insertion rows, generator, shared scientific-figure style, current QA reports, book style lock and selected profile.
- The original canonical Chapter 2 text and sidecar, then all of the proposed Chapter 2 Markdown and sidecar, including new introduction/interpretation paragraphs, captions, alt text and the 14 converted footnotes.
- Source-locators.json and its relevant passage text. Original PDF crops were independently rendered and visually inspected for main Eq. 7, the mutual-inhibition network paragraph and fixed states, and SI S30–S32. Both original source-file hashes agree with the source record. The existing tilted-decay image was inspected in the initial assessment and is unchanged.
- The three narrower equation locators added during review: S18 on PDF p. 4, S37 on p. 8, S41 on p. 9. Their source text and page/box positions match the intended equations. A one-point rounding difference in a suggested scroll margin has no effect on the locator meaning.

## Mathematical and source judgments

M01 correctly turns chosen event times into the exact sum of exponentials. Each vertical jump is one, including the fourth jump at 130 ms indicated by the +1 leader. Independent arithmetic gives successive post-jump levels 1, 1.4965853038, 2.1086976619, 1.6351275304 and 1.3301265549. The trace decays between events with the chosen 50 ms constant. Main Eq. 7 supplies the model; the spike times are plainly guide inputs. The strict inequality at an exact event time and the drawn jump show the left and right limits without a finite-time contradiction.

M02 correctly applies the chapter's activation coordinate theta = s1 - s2. With b = 20 and tau = 0.1 s, the rates are (20 + theta)/0.2 and (20 - theta)/0.2 spikes/s. They sum to 200 and give D = 100 coordinate units squared/s. At theta = 0 both rates are 100; at theta = -19 they are 5 and 195. The open endpoints and surrounding qualification preserve the positive-rate interior. These are chosen values, not the paper's b = 5000 simulation parameters. The retained coordinate footnote addresses the difference between activation and rate coordinates.

M03 correctly uses constant D = 0.5 rad squared/s for both the wrapped density and the comparison of mean squared errors. The wrapped density is normalized on [-pi, pi). The lower curve agrees with the density integral and with the Fourier identity pi squared/3 + 4 sum[(-1)^n exp(-Dn squared t)/n squared]. The uniform density is 0.1591549431 per radian, the limiting squared error is 3.2898681337 rad squared, and the line slope is 1 rad squared/s. The caption and axes keep the error convention visible. Flattening is not presented as a decline in local noise.

The supplied paper passages support the model and limit used. The new captions consistently distinguish calculated guide curves from paper simulation data. Main Eq. 2 and SI S40 source cautions remain explicit; no author-confirmed correction is asserted. The figure additions change none of the chapter's mathematical equations or assumptions.

## Readability and style

At the declared 700 px insertion width, all three plots retain readable axis labels, legends and tick values. Event/jump alignment, rate intersections, excluded endpoints and line/ring curve identities are clear. Nothing needed is clipped. This judgment assumes the existing horizontal-scroll treatment on narrow displays; it does not approve shrinking the plots proportionally to a 390 px viewport.

Current SVG QA uses only the seven recorded house-profile color tokens, with no outside token. Manual inspection confirms the existing scientific-plot style: navy and teal data series, muted references, white plotting areas and warm outside paper. These are mathematical series, not success/risk statements. No raster all-pixel palette claim or generic structural-template gate is made. The figures are internal quantitative illustrations, so chapter-opening-map coverage is not applicable; every required scene was checked separately.

## Source links and the focused recheck

The current proposed chapter has 48 PDF links, with 33 unique targets after the three equation-only offsets were narrowed. The links use explicit paper/section/equation/figure/paragraph locators and retain complete references. The source records distinguish PDF pages from final journal pages and do not invent original line numbers. The opening now says near-passage scrolling depends on viewer support. That qualification resolves the initial portability concern.

The coordinator also added both original PDFs and source-locators.json to all three figure contracts and synchronized the M01 brief introduction with the proposed text. These actual changed fields were reread and passed. Canonical hash binding must use the final inserted chapter and current source inputs after the remaining stages. Browser clicking remains a separate output check.

No reader files were edited by this reviewer. No whole-book audit, external publication, or final release approval is included.
