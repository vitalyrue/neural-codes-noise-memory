# Author inspection, 2026-10-24 18:11 +03:00

Author: `/root/draw_memory_additions`. Independent review remains pending. These are candidate assets only. No reader chapter, main visual ledger, old asset, or shared style file was edited.

All three full images and all three 700 px previews were opened with `view_image`. M02 was regenerated with more space above its legend and both sizes were inspected again. Its initial crowded top placement is closed. The plots use calculated coordinates, not a generic structural template. No generic template gate or raster pixel-deviation measurement is claimed.

## M01, fig:MEMORY-SPIKE-TRACE

Visible spike marks at 20, 55, 70, 130 and 210 ms align with five vertical unit rises of the activation trace. The activation between each rise is an exponential sum, not a linear interpolation. The plotted jump at 130 ms is labelled +1, which refers to the difference between left and right limits, not its final height. Time is in ms; activation is dimensionless under the chapter's one-unit-per-spike convention. Both rows share their time coordinate. All labels and the small +1 marker remain legible at 700 px.

Strongest objection: a spike trace should not be described as a continuous function. Resolution: the brief and proposed caption distinguish discrete events from activation, and say that activation decays between spikes while jumping at each event. It is a continuous-time jump process, with no assertion of mathematical continuity at a spike time. The source's strict inequality at an exact event is recorded in qa.json as a left/right-limit convention.

Book check: sec:MEMORY-SPIKES, activation jump equation and exponential sum. This image depicts one specified illustrative input; it does not claim to be a stochastic simulation or paper data. Caption, alt, introduction and conclusion are in M01-brief.yaml.

## M02, fig:MEMORY-INHIBITION-RATES

The navy increasing rate and teal decreasing rate meet at theta = 0 and 100 spikes/s. The gray dashed sum remains at 200 spikes/s. The lower teal diffusion curve remains at 100 coordinate units squared/s. Both panels share theta in activation units. Open endpoint markers show interior limits and exclude the endpoints. The displayed coordinate is the activation difference, not a rate difference. Legend, rate label, units and endpoint marks are legible at 700 px, with room above the legend after the repair.

Strongest objection: extending this constant D to boundary dynamics would be unjustified. Resolution: only the interior limits are plotted, endpoints are open, and the proposed caption explicitly says that the linear interior model does not determine boundary behavior. No curve extends beyond the interval.

Book check: sec:MEMORY-SYMMETRIC, two mutually inhibiting cells example. For b = 20 and tau = 0.1 s, r1 = (20 + theta)/0.2, r2 = (20 - theta)/0.2, and 2D = 200. Caption, alt, introduction and conclusion are in M02-brief.yaml.

## M03, fig:MEMORY-LINE-RING

The navy, teal and gray densities at 0.2, 1 and 5 s spread over the same angular interval. The dashed uniform reference lies at 1/(2 pi). The lower plot uses the same constant D = 0.5 rad squared/s. The line error grows as 2Dt while the wrapped angular error approaches the dashed pi squared/3 reference. The angular error interval [-pi, pi) and both axes' units are explicit. No simulated points or fitted data are drawn. Series legends and labels are legible at 700 px.

Strongest objection: the lower curve's flattening could be mistaken for a decrease in local D or a periodic trajectory's unwrapped variance. Resolution: the two curves explicitly compare line and wrapped angle, the bounded angular interval is written on the density axis, and the caption says that the same constant D applies and the flattening comes from the error convention. The visible pi label at the periodic right edge marks the coordinate limit, not an extra included probability mass.

Book check: sec:MEMORY-LONG-TIME, wrapped Gaussian construction, uniform limit and mean squared angular error calculation. The normalization and moments are independently checked by numerical integration in qa.json against the Fourier expression. Caption, alt, introduction and conclusion are in M03-brief.yaml.

## Checks and remaining work

`palette-consistency.json` passes against the current book lock. Each asset's `qa.json` reports passing computed checks and exact SVG color token membership, with no warnings or text outside the canvas. All artwork uses the selected house palette. Ordinary curves use navy, teal and gray, with no decorative panels or title banner.

Independent review must still inspect these final pixels and connected chapter/style inputs. The pending ledger retains pending verdicts and no author approval. No document insertion or publication was performed.

Root start: 2026-10-24T18:06:16.7630300+03:00. Final author inspection: approximately 18:11 +03:00. Wall-clock elapsed: about 5 minutes. Awake execution time unverified because Windows sleep/resume events were not inspected. Token stats unavailable.
