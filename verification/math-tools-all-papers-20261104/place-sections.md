## Random fields describe a fixed spatial map {#sec:MATH-TOOLS-RANDOM-FIELDS}

Why does a cell stay active over a stretch of track, rather than change its response independently at every position? Mainali, Azeredo da Silveira, and Burak (2025) describe the cell's combined input as a spatial map $h(x)$. Nearby values depend on one another. A distribution of such maps can predict field sizes without predicting where a particular cell's fields will occur.[^tools-place-map]

[A [**random field**]{.definition-term custom-style="Definition Term"} assigns random values to positions; a Gaussian random field requires the values at every finite set of positions to form a jointly Gaussian vector.]{.definition-explanation} In one spatial dimension it is also called a Gaussian process. [A [**jointly Gaussian vector**]{.definition-term custom-style="Definition Term"} has Gaussian distributions for all its linear combinations.]{.definition-explanation} Gaussian distributions at individual positions alone do not impose this joint rule.

[Once a map is drawn, it stays fixed while the animal traverses it. Revisiting a position evaluates the same map value, rather than drawing a fresh input.]{.key-statement} The randomness describes possible maps, not changes with time during a visit.

[The [**spatial covariance**]{.definition-term custom-style="Definition Term"} $C(x,y)$ measures how deviations of input from its mean at two positions vary together across possible maps.]{.definition-explanation} Mean and covariance determine the Gaussian law. [For a [**stationary**]{.definition-term custom-style="Definition Term"} field, shifting all positions leaves that law unchanged.]{.definition-explanation} The mean is then a constant $\mu$ and covariance depends on separation: $C(x,y)=C(y-x)$. This does not make an individual map flat. [An [**isotropic**]{.definition-term custom-style="Definition Term"} field also has no preferred direction in its statistics.]{.definition-explanation} Stationarity alone does not require isotropy.

Normalize the input using its standard deviation $\sigma_0$, and express the firing threshold $h_{\mathrm{th}}$ in the same units:

$$
z(x)=\frac{h(x)-\mu}{\sigma_0},\qquad
q=\frac{h_{\mathrm{th}}-\mu}{\sigma_0},\qquad
F(x)=a[z(x)-q]_+.
$$

Here $[u]_+=\max(u,0)$ and $a>0$ converts dimensionless input excess into firing rate. [The [**excursion set**]{.definition-term custom-style="Definition Term"} $A_q=\{x:z(x)>q\}$ is the active part of the map.]{.definition-explanation} Each connected piece is one field. Two peaks can belong to the same field if an active path connects them.

Field widths also depend on how quickly the input changes over distance. [The paper's [**correlation length**]{.definition-term custom-style="Definition Term"} compares typical input height with typical spatial slope.]{.definition-explanation} For a differentiable stationary map along a line,

$$
\ell_c=\sqrt{-\frac{C(0)}{C''(0)}},\qquad
\operatorname{Var}(z')=\ell_c^{-2}.
$$

It has distance units. For $C(r)=\sigma_0^2e^{-r^2/(2\ell_c^2)}$, increasing $\ell_c$ stretches the map. More generally it describes local covariance curvature, without fixing distant spatial relationships. In an isotropic map the same scale applies along every direction.[^tools-place-scale]

Gaussian values do not guarantee smooth maps. Crossing calculations need differentiable sample maps and regular, nondegenerate height and slope distributions. Peak calculations additionally need second derivatives and enough regularity for a local quadratic approximation. For example, the corner at zero in $C(r)\propto e^{-|r|/b}$ prevents its use for the differentiable crossing calculation below.

## Crossings and peak geometry predict field counts and sizes {#sec:MATH-TOOLS-CROSSINGS-PEAKS}

On a track, a field begins where the input crosses upward through threshold. [An [**upcrossing**]{.definition-term custom-style="Definition Term"} is a crossing of $z=q$ with positive spatial slope.]{.definition-explanation} The mean number per unit distance is the threshold density multiplied by the mean positive slope conditional on being at threshold:

$$
\nu_+(q)=p_z(q)\,\mathbb E[(z')_+\mid z=q]
=\frac{e^{-q^2/2}}{2\pi\ell_c}.
$$

[The [**Kac–Rice formula**]{.definition-term custom-style="Definition Term"} counts crossings by combining threshold density with conditional slope.]{.definition-explanation} The displayed result applies to the smooth stationary Gaussian model. A steep crossing occupies less distance near threshold, so its larger slope must compensate when converting spatial occupancy into a crossing count. [The result is exact under these assumptions at any threshold.]{.key-statement}[^tools-place-crossing]

<details class="publisher-long-content publisher-long-note">
<summary>Derivation: height and slope give the crossing density</summary>
<div class="publisher-fold-body">

In a narrow height band of width $2\varepsilon$ around $q$, an upward crossing with slope $v$ occupies distance approximately $2\varepsilon/v$. Weighting that distance by $v/(2\varepsilon)$ counts one crossing. Averaging gives $\nu_+=\int_0^\infty v\,p_{z,z'}(q,v)\,dv$.

Stationarity gives $\operatorname{Cov}(z,z')=0$. Joint Gaussianity makes height and slope independent, with $z\sim N(0,1)$ and $z'\sim N(0,\ell_c^{-2})$. Thus $p_z(q)=e^{-q^2/2}/\sqrt{2\pi}$ and $\mathbb E[(z')_+]=1/(\ell_c\sqrt{2\pi})$, giving the displayed result.

</div>
</details>

On a finite track of length $L$, a field can already be active at the left endpoint. Counting all active components that intersect the track gives $\mathbb E[N_L]=L\nu_+(q)+\Pr[z(0)>q]$. Discarding clipped boundary fields changes this convention. The later place field chapter follows this correction explicitly.

Counts do not determine the size distribution. At high positive $q$, typical fields surround isolated high peaks. A smooth isotropic Gaussian field becomes approximately a downward quadratic near such a peak. If its height exceeds threshold by $\epsilon$, the active radius grows as $\sqrt{\epsilon}$ at fixed $q$ and $\ell_c$. Length, area and volume therefore grow as $\epsilon^{d/2}$ in spatial dimension $d$.[^tools-place-peaks]

<details class="publisher-long-content publisher-long-example">
<summary>Example: the same peak excess gives different size laws</summary>
<div class="publisher-fold-body">

For a stationary isotropic Gaussian field, conditioning on height $b$ gives mean second derivative $-b/\ell_c^2$ along each unit direction, with fluctuations that do not grow with $b$. Thus typical high peaks concentrate around the quadratic shape

$$
z(x)-q\simeq\epsilon-\frac{q\|x\|^2}{2\ell_c^2},\qquad
r_*\simeq\ell_c\sqrt{2\epsilon/q}.
$$

For typical high fields the scaled excess $U=q\epsilon$ approaches an exponential distribution of mean one. Writing size as $s=v_dr_*^d$, with $v_1=2$, $v_2=\pi$, $v_3=4\pi/3$, converts the size event $s>S$ into $U>\beta S^{2/d}$. Therefore

$$
\Pr(s>S)\simeq\exp[-\beta S^{2/d}],\qquad
\beta=\frac{q^2}{2\ell_c^2v_d^{2/d}}.
$$

The resulting length law is Rayleigh in 1D, the area law is exponential in 2D, and the volume law has exponent $2/3$ in 3D. Geometry changes the distribution even though the scaled peak excess has the same limiting law.

</div>
</details>

[These size laws are high threshold limits, not exact laws at finite $q$.]{.key-statement} At lower thresholds fields can have several peaks or irregular shapes. The detailed chapter checks the approximation against finite threshold calculations.

[^tools-place-map]: Mainali, Azeredo da Silveira, and Burak (2025), [model and Gaussian process definition, PDF p. 3](../papers/mainali-2025-universal-statistics.pdf#page=3); [STAR Methods, Eqs. 2–3, PDF p. 13](../papers/mainali-2025-universal-statistics.pdf#page=13). The normalization here includes a constant mean, which can equivalently be absorbed into the threshold.

[^tools-place-scale]: Mainali et al. (2025), [STAR Methods, Eq. 4 and simulation covariance, PDF p. 14](../papers/mainali-2025-universal-statistics.pdf#page=14). The notation $\sigma_0$ denotes input standard deviation; $\ell_c$ denotes the paper's spatial scale $\sigma$.

[^tools-place-crossing]: Mainali et al. (2025), [Methods S3, Eqs. S9–S13, supplement PDF pp. 11–12](../papers/mainali-2025-supplement.pdf#page=11). The slope weighting and finite track endpoint correction are teaching explanations; the endpoint term also appears in [STAR Methods Eq. 8, main PDF p. 15](../papers/mainali-2025-universal-statistics.pdf#page=15).

[^tools-place-peaks]: Mainali et al. (2025), [size law, Eq. 1, main PDF p. 3](../papers/mainali-2025-universal-statistics.pdf#page=3); [Methods S4, Eqs. S22–S25, supplement PDF pp. 14–15](../papers/mainali-2025-supplement.pdf#page=14). The quadratic and change of variables here are a teaching reconstruction. Solving S22 retains the factor $\sqrt2$ missing from printed S23; the finite excess exponent used before the limit is $-q\epsilon-\epsilon^2/2$. The detailed size chapter records these printed algebra issues.
