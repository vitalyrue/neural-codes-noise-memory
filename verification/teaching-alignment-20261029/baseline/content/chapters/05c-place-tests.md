# Holes and measurements test the spatial explanation {#ch:PLACE-TESTS}

[Two maps can have the same field sizes and counts while arranging their active regions differently. One may contain rings or tunnels that the other lacks. Can the Gaussian spatial model account for these differences, and how much would that agreement tell us about the circuit that produced the maps?]{.key-statement}

We first count connected regions and holes together, which gives a prediction across activity thresholds. The boundary of the observed environment matters for this calculation, so we keep its contributions. We then examine which measured quantities set the model's parameters and which provide further tests. Finally, a sum of many randomly weighted inputs shows one way a circuit could produce Gaussian spatial input, while making clear which assumptions and circuit measurements that explanation still needs.

The map is still fixed over space. As before, $q$ is the normalized activity threshold, $\sigma$ is the local spatial scale, and $a$ converts normalized input above threshold into firing rate. The number of spatial dimensions is $d$; it is separate from the diffusion coefficient $D$ used in the memory chapters.

## Holes distinguish maps with the same field count {#sec:PLACE-TOPOLOGY}

Two maps can have the same field count and total active area but different holes. As the activity threshold rises, active regions shrink and can split or disappear. The numbers of components and holes can change.

[The [**Euler characteristic**]{.definition-term custom-style="Definition Term"}, written $\chi$, combines these counts differently in each dimension:]{.definition-explanation}

- In 1D it equals the number of connected active intervals.
- In 2D it is the number of connected components minus the number of independent holes. Three disjoint disks have $\chi=3$; one connected ring has $\chi=1-1=0$.
- In 3D it is components minus independent tunnels plus enclosed cavities. A solid ball has $\chi=1$, a solid ring has $\chi=0$, and a hollow spherical shell has $\chi=2$.

[These counts are the first three [**Betti numbers**]{.definition-term custom-style="Definition Term"}: numbers of independent components, loops, and cavities, respectively.]{.definition-explanation}[^p3-ec-source]

Thresholding one fixed smooth map separates the number of connected fields from the number of holes.

<div class="figure-scroll">

{{block:fig:PLACE-TOPOLOGY}}

</div>

A negative chi means that holes outnumber components in this 2D example. It does not mean a negative number of fields. When holes are absent, chi equals the component count.

The expected Euler characteristic has an exact Gaussian formula even where identifying it with field count would be wrong. We already derived the 1D case. To understand the higher dimensional factors, we use a mathematical result: [for a smooth function on a compact domain whose [**critical point**]{.definition-term custom-style="Definition Term"}s have zero gradient and invertible Hessians, the Euler characteristic of a level set region can be computed as a signed count of critical points, including boundary contributions. This is the relevant conclusion of [**Morse theory**]{.definition-term custom-style="Definition Term"}.]{.definition-explanation} We do not prove that topological theorem here. The calculation below shows how its Gaussian expectation produces the paper's polynomials and boundary terms; the general Gaussian result is given by Taylor's kinematic formula.[^p3-taylor]

First take the interior of a $j$ dimensional region, with $j\le3$, and set $\lambda=\sigma^{-2}$. A critical point has gradient zero. The multidimensional Kac–Rice rule counts these zeros with the absolute Hessian determinant; the Morse signs replace that absolute determinant by $\det(-H)$. The resulting signed density above level $q$ is

$$
\eta_j(q)=p_{\nabla z}(0)
\int_q^\infty
\mathbb E[\det(-H)\mid z=b,\nabla z=0]\,\phi(b)\,db,
$$

where $\phi(b)=e^{-b^2/2}/\sqrt{2\pi}$. The gradient's $j$ components are independent Gaussians of variance $\lambda$, so $p_{\nabla z}(0)=(2\pi\lambda)^{-j/2}$. The determinant measures how spatial volume near a gradient zero converts to gradient volume, just as the slope did for a scalar crossing.

The resulting signed densities are

$$
\eta_1=\frac{e^{-q^2/2}}{2\pi\sigma},\qquad
\eta_2=\frac{q e^{-q^2/2}}{(2\pi)^{3/2}\sigma^2},\qquad
\eta_3=\frac{(q^2-1)e^{-q^2/2}}{(2\pi)^2\sigma^3}.
$$

These are signed densities per length, area, and volume, not three formulas for positive field counts.

::: {.publisher-clarification-note .publisher-fold-always title="Derivation: the Gaussian determinant average and its integrals"}

Here are the Gaussian algebra steps behind the determinant average. Write the conditional Hessian as $H=-b\lambda I+G$, where $G$ has zero mean. Differentiating an isotropic covariance four times gives, for distinct indices $i,k$,

$$
\mathbb E[G_{ii}G_{kk}]=\kappa-\lambda^2,
\qquad
\mathbb E[G_{ik}^2]=\kappa.
$$

The constant $\kappa$ describes a fourth derivative of covariance. Conditioning on height subtracts $\lambda^2$ from the covariance of the two diagonal entries, but not from the off-diagonal variance. Hence each pair contributes

$$
\mathbb E[G_{ii}G_{kk}-G_{ik}^2]=-\lambda^2.
$$

For $j=1$, $\mathbb E[\det(-H)\mid b]=b\lambda$. For $j=2$, expand the two by two determinant to obtain $\lambda^2(b^2-1)$. For $j=3$, the leading term is $b^3\lambda^3$; the three index pairs each contribute $-b\lambda^3$, and all odd centered Gaussian products vanish. The result is $\lambda^3(b^3-3b)$. The unknown fourth derivative $\kappa$ has canceled.

Integrating the three polynomials gives

$$
\begin{aligned}
\int_q^\infty b\phi(b)\,db&=\phi(q),\\
\int_q^\infty(b^2-1)\phi(b)\,db&=q\phi(q),\\
\int_q^\infty(b^3-3b)\phi(b)\,db&=(q^2-1)\phi(q).
\end{aligned}
$$

For example, differentiate $-q\phi(q)$ to get $(q^2-1)\phi(q)$, which verifies the second integral using its vanishing upper endpoint. Combining the determinant, gradient density, and integral gives the signed densities above.

:::

Now include the boundary of an ordinary closed square or cube of side $L$, whose opposite faces are not joined and with every intersecting component retained. On a $j$ dimensional face, derivatives along the face give the same calculation as above. Each of its $d-j$ gradient components perpendicular to the face and directed out of the box must have the appropriate sign to contribute to the boundary Morse count. Symmetry and independence give a factor $2^{-(d-j)}$. There are $2^{d-j}\binom dj$ such faces, each of size $L^j$. Their combined coefficient is therefore $\binom djL^j$. Corners supply $Q(q)$ in total. With $r=L/\sigma$, the formulas become

$$
\begin{aligned}
\mathbb E[\chi_1]&=Q(q)+\frac{r}{2\pi}e^{-q^2/2},\\
\mathbb E[\chi_2]&=Q(q)+
\left[\frac{2r}{2\pi}+\frac{r^2q}{(2\pi)^{3/2}}\right]e^{-q^2/2},\\
\mathbb E[\chi_3]&=Q(q)+
\left[\frac{3r}{2\pi}+\frac{3r^2q}{(2\pi)^{3/2}}
+\frac{r^3(q^2-1)}{(2\pi)^2}\right]e^{-q^2/2}.
\end{aligned}
$$

These reproduce the paper's Equations 8–10 for interval, square, and cube geometry. They are not the formulas for a periodic box. For a rectangle or rectangular room, replace $2L$ or $3L$ by the sum of side lengths, $3L^2$ by the sum of pairwise side products, and $L^3$ by volume. A general domain requires its own geometric boundary factors. Applying only the volume term to a small room would discard real boundary contributions.

The formulas have two limiting checks:

- As $q\to-\infty$, the whole box becomes active and all three expectations tend to one.
- As $q\to+\infty$, they tend to zero.

At intermediate thresholds the higher dimensional signed densities can be negative because tunnels or holes outnumber components. For example a cube with $L/\sigma=10$ has expected $\chi=-20.06$ at $q=0$. A negative expected Euler characteristic is meaningful; a negative expected field count would not be.

At a sufficiently high threshold, almost every component is a small solid blob with one peak and no holes. Then $\chi\simeq N$. For a large box, retaining the leading volume term and the leading power of $q$ gives

$$
\mathbb E[N]\simeq
\frac{V}{(2\pi)^{(d+1)/2}\sigma^d}
q^{d-1}e^{-q^2/2},
$$

where $V$ is environment length, area, or volume. Dividing $VQ(q)$ by this count and using $Q(q)\simeq\phi(q)/q$ recovers $\mu_s\simeq(\sqrt{2\pi}\sigma/q)^d$, independently checking the size-law mean. [The exact EC formula and this approximate component count have different ranges of validity.]{.key-statement}[^p3-higher-count]

Read Figure 3F–H as whole curves, rather than single field counts. Increasing the applied firing rate cutoff by $t\ge0$ changes the normalized level to $q+t/a$. It can reveal separation between peaks or remove components. The measured maps only test levels at or above their original effective cutoff; the rest of an analytic curve is a prediction. The gain was matched using mean maximum firing rate before the EC comparison, so the horizontal conversion from Hz to normalized level also uses fitted information. Two dimensional holes and three dimensional tunnels help explain the nonmonotonic curves.[^p3-ec-source]

## What was fitted and what was tested {#sec:PLACE-DATA}

The experiments supply estimated firing rate maps, not the hidden Gaussian input. To assess a prediction, we must therefore track both which summaries set its parameters and which processing decisions change the map's geometry.

The paper reanalyzes earlier bat and rodent recordings. It uses different available summaries in different conditions. The inspected article and supplement do not clearly give the final included cell count for every analysis, particularly the long-tunnel and 3D reanalyses; counts from an original recording study should therefore not be silently substituted for those final samples.[^p3-processing]

<div class="table-responsive">

{{block:tbl:PLACE-DATA-COMPARISONS}}

</div>

The STAR Methods call the virtual-track animals rats in one sentence; Figure 1F and the main results identify them as mice. Several STAR figure cross-references also appear displaced. The table follows the main figure captions and the analyses described in full, rather than those isolated labels.

Figure 1C distinguishes a limiting analytical Rayleigh curve from the finite threshold simulation histogram. Its parameters were constrained by both mean length and mean gap, so the full length histogram is an additional check. Figure 1D does the same for gaps. E tests skew and excess kurtosis of log lengths. For $Y=\log s$, write $m_k=\mathbb E[(Y-\mathbb EY)^k]$; [then [**skew**]{.definition-term custom-style="Definition Term"} is $m_3/m_2^{3/2}$ and [**excess kurtosis**]{.definition-term custom-style="Definition Term"} is $m_4/m_2^2-3$. A [**lognormal distribution**]{.definition-term custom-style="Definition Term"} of sizes makes $Y$ Gaussian and both population quantities zero.]{.definition-explanation} Finite sample estimates still fluctuate, which is why the figure compares simulated sampling distributions.[^p3-fit-tests]

For the long-tunnel data, the authors compared the Gaussian excursion model with a fitted lognormal using likelihoods and criteria that penalize fitted parameter count. Those comparisons favored the Gaussian model. [These are in-sample model comparisons. They are not reported held-out forecasts.]{.key-statement} Model histogram error bars come from $10^4$ simulations matched to the number of recorded cells; they do not quantify every source of animal-level or measurement uncertainty.[^p3-fit-tests]

The processing choices affect the quantities being compared:

- Bat maps were rectified at about 0.5 Hz for denoising.
- The 3D maps, sampled in 10 cm bins, also received a median filter.
- Fields larger than three standard deviations above mean 3D volume were removed as possible merges, including from slice analyses.
- Peak counting excluded incomplete boundary fields and used a range of smoothing widths.
- The 1D rate versus width comparison used an additional 1 Hz cutoff.

[These decisions can remove small components, alter peaks, and change tails. They belong to the definition of the analyzed fields.]{.key-statement}[^p3-processing]

The supplement adds useful checks. Figure S1 matches the rat maze's 15 cm minimum length cutoff in simulations and removes unusually large empirical fields; changing that cutoff changes log-length moments. Figure S5 shows sensitivity of the higher-moment comparison across small denoising thresholds, while the rate versus width slope becomes stable above about 1 Hz. Figure S2 compares the spherical-field alternative and measures boundary curvature. [Locally, [**mean curvature**]{.definition-term custom-style="Definition Term"} averages bending in two principal directions and [**Gaussian curvature**]{.definition-term custom-style="Definition Term"} multiplies them: a spherical patch bends the same way in both directions, while a saddle bends in opposite directions.]{.definition-explanation} These are extra shape measurements; they are not needed to derive the field-size law. Surface representations and finite differences affect their estimates.[^p3-supp-tests]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure S1</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-S1}}

</div>
</details>

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure S5</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-S5}}

</div>
</details>

Figure 4A–B summarizes fitted parameter changes across a small set of environments. The correlation length increases with environment size while the threshold generally decreases. Increasing $\sigma$ reduces crossings per metre; decreasing $q$ increases them. Both parameters also affect mean length, so these effects must be considered together. Figure S3 reports count scaling exponents below one and hence a weak decline in count per unit environment size. These cross-experiment trends do not establish a biological scaling law. In particular, the 3D table's reported $\sigma=4.0$ has an unclear distance-unit conversion relative to the spatial binning, so it should not be read as a verified value in metres.[^p3-trends]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure 4</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-4}}

</div>
</details>

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure S3</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-S3}}

</div>
</details>

The model also allows differences between cells. Figure S4 draws a positive threshold separately for each cell and keeps that threshold for two otherwise independent maps representing opposite flight directions. Low-threshold cells tend to have more and larger fields in both maps; this shared cell property creates correlations between flight directions even when field locations differ between directions. Two distribution parameters were chosen to match the two empirical correlations, so those correlations are fitted features of this extension. Its continued agreement with length and gap distributions is the additional comparison. This extension should not be described as a two-parameter model shared by all cells.[^p3-threshold-variation]

<details class="publisher-long-content publisher-source-figure">
<summary>Original paper figure: Mainali, Azeredo da Silveira, and Burak (2025), Figure S4</summary>
<div class="publisher-fold-body">

{{block:fig:PAPER-PLACE-S4}}

</div>
</details>

## Random input weights can generate Gaussian maps {#sec:PLACE-WIRING}

The statistical model becomes biologically useful if it suggests how a circuit could make the maps. A random weighted sum of many inputs is one possible mechanism, and the supplement makes its assumptions explicit.

At position $x$, each input cell contributes according to its spatial firing profile. Fixed connection weights determine how those contributions combine at the receiving cell. The source treats the sum as effective input relative to a background that can be balanced through inhibition or regulation of excitation and inhibition. The signed random weights below are part of this simplified input model; they do not establish the signs of individual biological synapses.

Let $u_i(x)$ be the fixed spatial tuning of input neuron $i$, and let independent weights $W_i$ have zero mean and variance $v_W$. The profiles $u_i$ may have nonzero spatial means. The expectation below is over weights: their zero means make the summed input $h(x)$ have mean zero. The summed input is

$$
h(x)=\sum_{i=1}^n W_i u_i(x).
$$

[At a finite list of positions this is a sum of independent random vectors, one per input cell. Under a multivariate central limit condition, with a suitable normalization and no single input dominating, the sum approaches a Gaussian vector as the number of contributing inputs grows. Applying this at every finite list supplies the Gaussian-process description. The theorem needs many contributing inputs at the positions in question; a large anatomical input count alone does not show that this condition holds.]{.key-statement}[^p3-wiring-source]

The covariance calculation exposes which assumption supplies spatial structure:

$$
\begin{aligned}
\mathbb E[h(x)h(y)]
&=\sum_{i,j}\mathbb E[W_iW_j]u_i(x)u_j(y)\\
&=v_W\sum_i u_i(x)u_i(y).
\end{aligned}
$$

The same fixed weight multiplies an input cell's activity at both positions. For positive input profiles, cells active at both $x$ and $y$ therefore make positive contributions to covariance across possible weight choices. Little overlap gives a smaller contribution. For profiles defined as deviations from background, the products can also be negative. Broad input profiles can produce broad spatial covariance, as the Gaussian example below shows.

If inputs are translated copies $u_i(x)=u_0(x-x_i)$ with centres densely and uniformly covering space at density $\rho$, the sum is approximately

$$
C(y-x)\simeq v_W\rho\int u_0(s)u_0(s+y-x)\,ds.
$$

The assumptions supply different parts of the model:

- Uniform coverage supplies stationarity away from boundaries.
- Smooth input tuning supplies smoothness.
- Random weights supply the Gaussian limit under their independence and size conditions.

For input profiles with different shapes, average the last integral over the distribution of those shapes, as in Methods S2, Equation S8.

At fixed profile shape, increasing the weight variance $v_W$ or input density $\rho$ increases the covariance amplitude. It does not change the normalized spatial dependence in this construction. Widening each input profile instead broadens the distances over which positions share input. These are different changes: input amplitude can alter the effective threshold $q$ when the absolute threshold is held fixed, whereas input width changes the spatial scale.

For example, take $u_0(s)=R_0e^{-s^2/(2b^2)}$ in one dimension. Completing the square gives

$$
\int u_0(s)u_0(s+\Delta)\,ds
=R_0^2\sqrt\pi b\,e^{-\Delta^2/(4b^2)}.
$$

The covariance's Gaussian standard deviation is $\sqrt2 b$, fixing the width convention used in the comparison.

Agreement with the Gaussian field predictions supports this random-summation account as a possible explanation. It does not uniquely recover synaptic weights from rate maps. Correlated inputs, a structured component added to many random contributions, plasticity, or recurrent processing could also produce approximately Gaussian spatial input under some conditions. The paper measures rate maps, rather than the relevant weights or subthreshold input directly. Its analyzed environments were familiar and fairly uniform; stationarity may fail near landmarks, boundaries, rewards, or in changing tasks.[^p3-discussion]

[The result to carry into the synthesis is therefore specific: thresholding a smooth spatial Gaussian field links field arrangement, shape, and topology through a small set of parameters and gives several successful cross-checks. Turning that statistical agreement into a claim about circuit mechanism requires additional measurements or perturbations.]{.key-statement}

[^p3-ec-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 3F–H; STAR Methods, “Euler characteristics,” Equations 8–10, p. e3.

[^p3-taylor]: Taylor, J. E. (2006). *A Gaussian kinematic formula*. The Annals of Probability, 34(1), 122–158. [DOI](https://doi.org/10.1214/009117905000000594); [author preprint](https://arxiv.org/pdf/math/0602545), Equation 1.4, Theorem 4.1, Section 5.1 and Equation 5.1. This chapter uses the signed critical-point and boundary-counting framework, then derives the Gaussian algebra for dimensions at most three and the face factors for a box, matching Mainali et al.'s Equations 8–10. It does not prove the underlying Morse or kinematic theorem.

[^p3-higher-count]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S3, Equations S16–S17, p. 12. These are high threshold, volume-dominated approximations.

[^p3-processing]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), STAR Methods, “Data processing,” “Parameter inference,” “Fields in 3D,” “Number of local peaks within a field,” and “Maximum firing rate vs. field width,” pp. e2–e3; Figures 1F, 2, 5D.

[^p3-fit-tests]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 1C–F; STAR Methods, “Fields in 1D,” “Kurtosis and skew,” Equations 6–7, pp. e2–e3. Centered moment notation is made explicit here.

[^p3-supp-tests]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figures S1–S2 and S5, supplemental pp. 1–3, 6–7. Curvature comparisons use local surface derivatives; the empirical surface representation does not supply an exact analytic reconstruction of every field surface.

[^p3-trends]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure 4A–B and accompanying text, p. 1116; Figure S3, supplemental p. 4.

[^p3-threshold-variation]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Figure S4 and caption, supplemental p. 5; “Parameter variation across experiments,” p. 1116. The threshold distribution is positive-conditioned skew normal, its mean fixed to the baseline fit and its two remaining parameters fitted to correlations.

[^p3-wiring-source]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Supplemental Methods S2, Equations S2–S8, pp. 9–10; Figure 1B. The Gaussian autocorrelation integral is evaluated explicitly here.

[^p3-discussion]: Mainali et al. (2025), *Universal statistics of hippocampal place fields across species and dimensionalities*, Neuron, 113, 1110–1120.e3, [doi:10.1016/j.neuron.2025.01.017](https://doi.org/10.1016/j.neuron.2025.01.017), Discussion, pp. 1117–1118. The distinction between a sufficient mechanism and a uniquely identified mechanism is this guide's inference from the model and measurement scope.
