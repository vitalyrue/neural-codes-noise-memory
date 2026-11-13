# Random spatial maps test the statistics of place fields {#ch:SIMULATING-PLACE}

To reproduce Mainali et al.'s (2025) place-field comparisons, we need the rules for generating and fitting model maps, and for measuring both model and recorded maps. The [spatial-model chapter](ch-place-fields.html) explains the statistical assumptions, and the [tests chapter](ch-place-tests.html) interprets the evidence. Here the additional detail is the Python map-generation procedure, filter and boundary conventions, fitted summaries, field detectors, and access to code and recordings. Position is the independent variable; each generated map is fixed during analysis, so these computations do not simulate a remembered position changing over time.


## A smooth random input becomes a firing map after thresholding {#sec:SIMULATING-PLACE-GENERATE}

For each model cell, the theory assigns a smooth Gaussian input field $h(\mathbf x)$ to locations $\mathbf x$. Its covariance controls how similar nearby input values tend to be. A threshold determines which locations activate the cell. With this notation, the rate is proportional to

$$
\max\{h(\mathbf x)-q\sqrt{C(0)},0\}.
$$

Here $h(\mathbf x)$ is the input at position $\mathbf x$, $q$ is the threshold in units of input standard deviation, and $C(0)$ is the input variance. The expression selects the positive part of the input above $q\sqrt{C(0)}$; an overall gain converts that excess into a firing rate. The threshold and spatial correlation scale govern the shapes and sizes of the active regions. The gain supplies the firing-rate scale. The [spatial-model chapter](ch-place-fields.html) develops these quantities before deriving field-count and gap predictions.[^simplace-model]

The published Python archive constructs such maps directly:

1. Draw independent normally distributed values at the spatial grid points for each cell.
2. Smooth the array with a [[**Gaussian filter**]{.definition-term custom-style="Definition Term"}, which averages nearby values with weights that decrease with distance.]{.definition-explanation} Neighboring outputs share inputs, making them correlated.
3. Divide each map by the square root of the mean of its squared grid values, its root mean square. This sets its sampled root mean square to one.
4. Subtract the threshold and replace negative values with zero.
5. Measure the connected nonzero regions as fields.

This procedure implements the spatial model without explicitly simulating presynaptic neurons or their synapses. The paper's random-input argument explains one possible origin of a Gaussian field. It is not a simulated recurrent hippocampal circuit in this code. [Agreement with place-field statistics tests the spatial description, while the proposed wiring remains an interpretation requiring further evidence.]{.key-statement}

Smoothing, amplitude normalization, and edge handling affect the finite sampled map. Matching the published implementation requires these numerical choices.[^simplace-code]

## Fitted summaries and additional comparisons supply different evidence {#sec:SIMULATING-PLACE-FIT}

The authors choose threshold and spatial scale to match a small number of measured summaries. For the long 200 m bat tunnel, they match mean field length and mean gap. In the short 6 m tunnel, they use mean field length and occupied fraction, because many cells have only one field. The 2D comparison fits mean field size and count, while the 3D comparison uses mean volume and occupied fraction.[^simplace-fit]

A [[**fitted statistic**]{.definition-term custom-style="Definition Term"} is a measured summary used to choose a model's parameters.]{.definition-explanation} Recovering that statistic checks the fit, but gives less independent evidence than successfully describing other features. The full size distribution, lower-dimensional slices, multiple peaks, and holes in fields provide further comparisons. Some of those analyses also fit a firing-rate gain, which must remain visible when judging how independent a test is.

The paper compares simulated size distributions with a fitted lognormal alternative using likelihood-based criteria. This is a comparison on the available data, rather than a reported test on a separate held-out dataset. Its high-threshold analytical laws also have a different role from finite-threshold simulation: the simulations can examine regimes where those limiting formulas are only approximate.

For uncertainty in size histograms, the Methods describe $10^4$ model realizations, each containing the experimental number of cells. The resulting spread reflects variation between model samples of that size. It does not include every source of recording error or uncertainty about the biological model.

## Field detection and preprocessing change what the simulation is asked to match {#sec:SIMULATING-PLACE-MEASURE}

To compare a generated field with a recorded one, both must be measured in compatible ways. A small positive noise value can connect two regions, while thresholding can split them. Smoothing can remove a peak or fill a small hole.

The STAR Methods specify several distinct measurements:

- **Lengths and gaps in 1D:** count consecutive nonzero or zero bins and convert their counts to physical lengths. The archived implementation places field edges at grid-bin boundaries.
- **Volumes in 3D:** label connected nonzero components and multiply their bin counts by bin volume. The reported analysis removes fields more than three standard deviations above the mean volume as probable mergers.
- **Peak and boundary shape:** use peak detection and local finite differences, with additional smoothing or rate thresholds stated for the relevant comparison.
- **Connectedness and holes:** use the Gudhi Python library to calculate Betti numbers and form their alternating sum, the Euler characteristic. The [place-field tests chapter](ch-place-tests.html) explains why this statistic contains information absent from field volumes alone.[^simplace-measure]

The experimental 3D maps have 10 cm spatial bins and receive a median filter in the described processing. Different analyses use different cutoffs. A reproduction therefore needs the rule for its target panel, rather than one generic threshold applied to every figure.

Figures 1 and 2 connect the generated maps to size, count, gap, and slice statistics. Figure 3 tests shapes and connectedness. Figures 4 and 5 examine how fitted parameters and threshold changes relate to field structure. The supplement checks alternative spherical fields, cell-to-cell threshold variation, and sensitivity to processing choices. These comparisons extend the evidence beyond a visually similar random map.

::: {.publisher-clarification-note .publisher-fold-always title="Width and edge conventions must be checked before copying parameters"}

For one spatial dimension, let $C(x)$ be the input covariance between positions separated by distance $x$; $C(0)$ is the variance and $C''(0)$ is the second derivative with respect to separation, evaluated at zero. The paper defines its local correlation scale by $\ell=\sqrt{-C(0)/C''(0)}$. The code also uses a parameter called `sigma`, but as the width $b$ of the Gaussian smoothing filter. For ideal continuous white noise smoothed by a Gaussian of width $b$, the covariance is proportional to $\exp[-x^2/(4b^2)]$. Differentiating at zero gives $\ell=\sqrt2\,b$. The two widths are therefore different quantities.

This conversion follows from the smoothing construction. It is not another fitted biological result. Finite sampling and filter truncation can modify the ideal relation. The archived 1D generator uses reflected edges, whereas its 3D generator wraps the filter around the array edges. The boundary rule used for smoothing also does not, by itself, specify the boundary rule for a later topology calculation.

The README's dummy-data settings illustrate package use. They are not a complete list of the grid, cell count, and random seed used for each published panel. Exact reproduction needs those panel-specific choices as well as the archive.

:::

## The released tools generate maps and analyze data, with access limits {#sec:SIMULATING-PLACE-TOOLS}

The paper reports using Python 3.11. The code uses NumPy for arrays and random samples, and SciPy for smoothing and map measurements. The Methods identify SciPy routines for connected components, peak detection, and density estimation, and Gudhi for topology. These are spatial and statistical computations. A spiking-neuron simulator is not required by the released method.

The published code is archived on Zenodo, with an accompanying public GitHub repository. The inspected archive contains source files and dependency information. It does not contain all recording data or a complete set of per-figure run records. A current repository example therefore cannot automatically establish the settings used in the 2025 publication.[^simplace-code]

The article points to public source datasets, including the bat-tunnel deposit. It also acknowledges directly shared full bat maps and a 20-cell sample of rat maps used for particular analyses. Access to every required map must be checked for the intended figure. Availability of the model code is different from availability of all experimental inputs.[^simplace-data]

For a new study, two questions can now be separated. One is whether thresholded smooth random inputs describe the measured spatial patterns. The other is which neural dynamics, connections, and learning rules create those inputs. The simulations in this paper directly address the first and provide constraints for investigating the second.

[^simplace-model]: Mainali, N., Azeredo da Silveira, R., & Burak, Y. (2025). *Universal statistics of hippocampal place fields across species and dimensionalities*. Neuron, 113(7), 1110–1120.e3. [STAR Methods, Eqs. 2–4, PDF pp. 13–14](../papers/mainali-2025-universal-statistics.pdf#page=13); [Methods S2, supplement PDF pp. 10–11](../papers/mainali-2025-supplement.pdf#page=10). [DOI](https://doi.org/10.1016/j.neuron.2025.01.017).

[^simplace-code]: Mainali, N. (2025). *Gaussian process place-field model* [Python source code]. [Published code archive, version DOI](https://doi.org/10.5281/zenodo.14650881). [Repository revision inspected October 30, 2026](https://github.com/5183nischal/gp-model/tree/eae7eab801bb6ca016b3a6ff4f35d6a47df98d6a). The archive and selected source functions were inspected. The figure-generation runs were not executed.

[^simplace-fit]: Mainali et al. (2025), [STAR Methods, Parameter inference in 1D, 2D and 3D, PDF p. 14](../papers/mainali-2025-universal-statistics.pdf#page=14), and [Figures 1–5](../papers/mainali-2025-universal-statistics.pdf#page=4).

[^simplace-measure]: Mainali et al. (2025), [STAR Methods, Data processing, PDF pp. 14–15](../papers/mainali-2025-universal-statistics.pdf#page=14), and [supplementary Figures S1–S5](../papers/mainali-2025-supplement.pdf#page=2). The source specifies the processing rule for each analysis.

[^simplace-data]: Mainali et al. (2025), [resource availability and acknowledgments, PDF p. 10](../papers/mainali-2025-universal-statistics.pdf#page=10), and [key resources, PDF p. 13](../papers/mainali-2025-universal-statistics.pdf#page=13). The linked source dataset is Eliav et al. (2021), *Multiscale representation of very large environments in the hippocampus of flying bats*. [Public bat-tunnel data](https://doi.org/10.5281/zenodo.4646728).
