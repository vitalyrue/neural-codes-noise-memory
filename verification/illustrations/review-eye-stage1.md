# Independent Stage 1 review of V04 and V05

Completed: 2026-10-23T22:09:44.839746+03:00
Reviewer: `/root/draw_memory_figures`; did not author these two figures or their insertion text.

Both exact candidate images pass truth/accuracy, visual explanation, full-size and 700 px readability, and SVG palette-token review. The coordinator repaired the two administrative ID mismatches during review. The final brief IDs match the integration packet, and the report binds their corrected hashes. No artwork change is needed.

This is Stage 1 only. It does not claim wording/necessity review, reader-flow review, whole-chapter acceptance or publication readiness.

## Findings

No remaining scientific, visual or acceptance-binding blocker. Initial brief-ID mismatches were corrected by the coordinator and rechecked before the final hash capture.

## Actual figure checks

V04: The shared-drive fan, individual motor cells, muscle/eye stage and position marker depict physical flow. The attractor source is explicitly proposed. Only the highlighted lower cell is linked to a spike record, and that record is paired with eye position. Measurement noise enters the record rather than the physical eye. The lower dashed orange path computes predicted position from one cell through the calibrated filter. No simultaneous motor-neuron pair covariance or backward biological connection is implied.

The strongest possible correction is that a circuit drawing could make the attractor origin look directly recorded. The proposed-source label, one-cell recording limitation and connected chapter discussion resolve that concern. The two required scenes, physical-path and recordings-and-analysis, are both visible and explain different relationships beyond their labels.

V05: Both inputs pass through identical one-pole response drawings. The left normalization is M_white/(A/tau), with function 1-exp(-x); the right is M_Brownian/(2D tau), with function x-1+exp(-x). The axes use the same logarithmic lag variable x=ell/tau. Short-lag slopes are one and two; long-lag behavior is a plateau and continued growth. The independent scales are printed on the axes and reinforced by a visible note. Five independent covariance-integral checks reproduce the plotted formulas.

The strongest possible correction is transfer of the white one-pole short-lag slope to the paper fuller muscle model. The figure says one-pole, its caption identifies a guide calculation, and the interpretation explicitly limits that slope. The connected chapter derives the Brownian formula after its velocity transient. The required filter-comparison scene shows the actual shape distinction, without finite-variance white-noise samples or equal-amplitude claims.

Both full-size images and both 700 px previews were viewed. No clipping or overlapping labels prevent reading. Supporting labels remain readable at 700 px. Exact SVG color tokens were independently compared with house-graphic-v1 and match; no raster pixel-deviation claim is made. All individual label groups, arrow claims, caption claims and alt/interpretation claims are recorded in the JSON with source references.

Original source checks: main paper p. 9 recording and inverse-filter Methods; main p. 10 Eqs. 20-22 and model staging; peer-review response stating no simultaneous recordings of more than one OMN. These targeted local source checks support the connected Chapter 4 passages.

## Exact bindings and timing

The JSON records SHA-256 hashes for PNG, SVG, 700 px preview, QA report, figure brief, complete connected chapter and sidecar, integration packet, drawing source, style helper, plan, style lock/profile, review rules and targeted original source extractions. It also records that each insertion anchor occurs once.

Root wall-clock elapsed: 792.9 seconds. Previous checkpoint: 2026-10-23T22:07:04.842327+03:00; since checkpoint: 160.0 seconds. Awake execution time unverified. No system clock change was observed. Token stats unavailable.
