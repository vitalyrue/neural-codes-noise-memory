# Spiking noise produces diffusion along the memory attractor {#ch:MEMORY-DYNAMICS}

[A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied.]{.key-statement} Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]

Starting from the neural dynamics established in Chapter 1, we first express the random spike input as continuous noise under the paper's weak-fluctuation assumptions. We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains. Adding these lasting random changes gives a local rate of spreading. When connections have equal weights in both directions, we can express that rate using the cells' tuning curves and check its meaning in a two-cell example. The following chapter extends this local prediction to longer delays.

Sources: Burak and Fiete (2012), [paper](../papers/burak-fiete-2012-persistent-activity.pdf) and [Supporting Information (SI)](../papers/burak-fiete-2012-persistent-activity-si.pdf).

Here the physical network state is the vector of synaptic activations $\mathbf s=(s_1,\ldots,s_N)$; firing rates follow from that state through the input and transfer function. The memory coordinate is $\theta$, and its initial value is $\Theta$. “Stored value” and “represented value” refer to this same coordinate, rather than to the whole activation vector. An observer's estimate $\widehat\theta$, obtained from a finite spike sample, can differ from $\theta$.

Noise generally puts $\mathbf s$ slightly away from the attractor. To assign it a memory coordinate, imagine turning off further noise and following the deterministic return flow. [The fixed point reached by this flow is the paper's [**instantaneous attractor state**]{.definition-term custom-style="Definition Term"}; $\theta$ labels that point.]{.definition-explanation} This local definition assumes that nearby states return to a unique point on the continuous family. It uses the circuit's return dynamics, which can differ from a perpendicular geometric projection. [Original definition and Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2).

A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$, and $\bar s_i=\tau\bar r_i$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.

## Many weak inputs allow a continuous approximation to spike noise {#sec:MEMORY-WEAK-NOISE}

**Paper location:** [Materials and Methods, “Weak Fluctuations,” Eqs. 10–11, PDF pp. 5–6](../papers/burak-fiete-2012-persistent-activity.pdf#page=5); [supporting text, section I, Eqs. S1–S6, PDF pp. 1–2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1). Brownian increments express the paper's Gaussian-noise approximation in teaching notation.

**Neural mechanism.** [Chapter 1 established the spike, activation and firing-rate model, Eqs. 7–9](ch-foundations.html#sec-memory-spikes). The [connection-matrix explanation](../frontmatter/ch-mathematical-tools.html#sec-math-tools-weights) establishes the feedback role of those connections. Here we calculate how random spike timing makes activation fluctuate. The connections are tuned to a continuous family of steady patterns, and the Gaussian approximation assumes small fluctuations in each neuron's total input.

**Mathematical derivation.** We start from $ds_i=-s_i\,dt/\tau+dN_i$. The elementary spike-generation noise is independent across neurons conditional on the present rates.

<!-- vale ai-tells.FormalTransitions = NO -->
Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Let $\delta_{ij}$ be one when $i=j$ and zero otherwise. Thus
<!-- vale ai-tells.FormalTransitions = YES -->

$$
E[dN_i\mid r_i]=r_i\,dt,
\qquad
\operatorname{Cov}(dN_i,dN_j\mid\mathbf r)
=\delta_{ij}r_i\,dt.
$$

Write $dM_i=dN_i-r_i\,dt$ for the spike count minus its conditional mean: the surplus or deficit of spikes in this interval. Splitting the count into its mean and this fluctuation gives

$$
ds_i=\left[-\frac{s_i}{\tau}+\phi(g_i)\right]dt+dM_i,
\qquad
E[dM_i\mid\mathbf r]=0,
\quad E[dM_i dM_j\mid\mathbf r]=\delta_{ij}r_i\,dt.
$$

The split into a mean and a fluctuation leaves the individual spike events unchanged. Each spike raises $s_i$ by one, and $s_i$ decays between spikes. [In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input. Their summed fluctuation can then be represented by Gaussian noise with the same leading mean and covariance.]{.definition-explanation} Many suitably independent contributions justify the approximately Gaussian sum; matching mean and covariance alone would not establish its distribution. The approximation describes a summed input on a scale where many small contributions matter. A single neuron's count in an infinitesimal interval remains a discrete spike count.

<details class="publisher-long-content publisher-long-example">
<summary>Example: how many small spike inputs approach a Gaussian</summary>
<div class="publisher-fold-body">

Suppose $n$ cells fire independently at the same constant rate $r$ during an interval $h$, and each spike adds $1/n$ to a receiving cell's input. The total number of spikes is Poisson with mean $nrh$, so the summed input has mean $rh$ and variance $rh/n$. When $nrh$ is large, the standardized total count is approximately Gaussian: no single spike supplies a large share of the summed input. Increasing $n$ keeps the mean input fixed while shrinking its fluctuations.

This example holds the rates fixed during the interval. In a recurrent network the rates change with the state, so the approximation must also use intervals short enough for the rates to change little. Synaptic activation sums and smooths spike effects over its decay time $\tau$. The approximation does not say that each cell produces many spikes in every infinitesimal interval.

</div>
</details>

Each receiving cell sees a weighted sum $g_i=\sum_j W_{ij}s_j+b_i$. With fixed weights, the random part of its input increment is $\sum_jW_{ij}\,dM_j$. Conditional independence gives its leading covariance with the corresponding increment of receiver $k$:

$$
\operatorname{Cov}(dg_i,dg_k\mid\mathbf r)
=\sum_jW_{ij}W_{kj}r_j\,dt.
$$

The same presynaptic fluctuation can affect both receivers, so their summed inputs can be correlated even when spike generation is conditionally independent. In the weak-fluctuation limit, the paper approximates the summed and synaptically smoothed input as Gaussian. It can represent that approximation using a separate Gaussian drive for each activation variable: multiplying those drives by $W$ gives the input covariance above.

Let $F_i(\mathbf s)$ be the mean rate of change of neuron $i$'s activation. Let $B_i$ be independent standard [Brownian motions](ch-persistence.html#sec-foundations-diffusion). The increment $dB_i=B_i(t+dt)-B_i(t)$ has mean zero and variance $dt$. Multiplying it by $\sqrt{r_i}$ gives the same leading variance $r_i\,dt$ as the centered spike count. The Gaussian representation of the activation equation is

$$
ds_i=F_i(\mathbf s)dt+\sqrt{r_i}\,dB_i,
\qquad
F_i(\mathbf s)=-s_i/\tau+\phi\!\left(\sum_jW_{ij}s_j+b_i\right),
$$

<!-- vale ai-tells.EmDashUsage = NO -->
The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Brownian drives are a representation of the approximated summed-input dynamics; they are not a claim that an individual neuron's discrete spike path or its isolated synaptic activation is Gaussian. The supplement derives the equivalent input equations after making the Gaussian approximation ([SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak]
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.FormalTransitions = NO -->
The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. For a ring network, a neuron's preferred angle is an angle where its tuning curve peaks. Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]
<!-- vale ai-tells.FormalTransitions = YES -->

Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

$$
0=-\frac{\bar s_i(\theta)}{\tau}
+\phi[\bar g_i(\theta)],
\qquad
\bar s_i(\theta)=\tau\bar r_i(\theta).
$$

**Interpretation.** In the noise free dynamics, recurrent firing balances synaptic decay at each fixed point. The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.

## The network's return flow determines the lasting memory change {#sec:MEMORY-LINEARIZATION}

**Paper location:** [Supporting text, section II, Eqs. S7–S13, PDF p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3). The explanation of the expansion, eigenvectors, and return flow fills in steps between the printed equations.

**Neural mechanism.** A spike perturbs many aspects of a network's state. Most of those changes decay as the state returns to the attractor. [To calculate memory loss, we need the lasting change: the displacement to a different fixed point. We assume a smooth continuous family with one neutral memory direction, while all other local modes decay. The disturbance must be small enough that the first order response describes the return flow.]{.key-statement}

**Mathematical derivation.** [A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to a small perturbation and drops terms quadratic or higher in it.]{.definition-explanation} Here the network activation is $\mathbf s=\bar{\mathbf s}(\theta)+\delta\mathbf s$. Taylor expansion of the transfer function gives

$$
\phi\!\left(\bar g_i+\sum_j W_{ij}\delta s_j\right)
\simeq\phi(\bar g_i)+\phi'(\bar g_i)\sum_jW_{ij}\delta s_j.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Let $K$ be the linear response matrix: $K\delta\mathbf s$ is the mean rate of change of the activation disturbance. Let $R$ be the diagonal matrix of spike-count variance rates, evaluated at that fixed point. Then
<!-- vale ai-tells.FormalTransitions = YES -->

$$
d\delta\mathbf s=K\delta\mathbf s\,dt+R^{1/2}d\mathbf B,
\qquad
K_{ij}=-\frac{\delta_{ij}}{\tau}+\phi'(\bar g_i)W_{ij},
\qquad R=\operatorname{diag}(\bar r_i).
$$

In this leading local calculation the noise strengths are evaluated at the fixed point. The entries of $K$ have units of inverse time.[^p1-projection]

The term $-\delta_{ij}/\tau$ removes a disturbance as synaptic activation fades. The term $\phi'(\bar g_i)W_{ij}$ describes recurrent renewal: the connection converts a change in cell $j$'s activation into input to cell $i$, and the local slope of the transfer function converts that input into a rate change. A steeper slope makes this response stronger. [Whether a disturbance decays, persists, or grows depends on the combined feedback through the whole network.]{.key-statement} A stronger connection alone does not establish better memory.

To see how the matrix controls time, temporarily switch off the noise and consider a disturbance in a right eigenvector direction $\mathbf z$, with $K\mathbf z=\lambda\mathbf z$. If it starts at $c\mathbf z$, the linear equation gives $\delta\mathbf s(t)=c e^{\lambda t}\mathbf z$. A negative real eigenvalue makes that component decay; a zero eigenvalue leaves it unchanged. Complex eigenvalues describe oscillating combinations, which decay when their real parts are negative. The attractor calculation assumes all directions away from its neutral tangent decay. Even if the matrix is not diagonalizable, stable components can have transient polynomial factors but still decay when their eigenvalues have negative real parts.

**Paper location:** [Supporting text, Eq. S11, PDF p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) defines the tangent direction. The derivative steps below explain why it is a zero mode.

Moving a little along the fixed point family changes the activation by

$$
\delta\mathbf s\simeq\mathbf u\,\delta\theta,
\qquad u_i=\frac{d\bar s_i}{d\theta}=\tau\frac{d\bar r_i}{d\theta}.
$$

Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$. The chain rule gives

$$
K\mathbf u=0.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
[Thus $\mathbf u$ is a [**right zero eigenvector**]{.definition-term custom-style="Definition Term"}: a state direction that the linear dynamics neither restores nor amplifies.]{.definition-explanation} It is the tangent to the attractor. The other modes must decay for this local family to be attracting.
<!-- vale ai-tells.FormalTransitions = YES -->

<!-- vale ai-tells.NegatedObject = NO -->
**Paper location:** [Supporting text, Eqs. S12–S13, PDF p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) define and normalize the left vector. The tilted two-variable example below is a guide construction.

To extract the lasting memory displacement from a general perturbation, recall the [left zero eigenvector](../frontmatter/ch-mathematical-tools.html#sec-math-tools-weights), a vector $\mathbf v$ satisfying
<!-- vale ai-tells.NegatedObject = YES -->

$$
\mathbf v^T K=0,
\qquad \mathbf v^T\mathbf u=1.
$$

The normalization makes $\mathbf v^T(\mathbf u\,\delta\theta)=\delta\theta$. If a stable mode $\mathbf z$ satisfies $K\mathbf z=\lambda\mathbf z$ with $\lambda\ne0$, then

$$
0=\mathbf v^T K\mathbf z=\lambda\mathbf v^T\mathbf z,
$$

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
so $\mathbf v^T\mathbf z=0$. The left vector discards every decaying mode ([SI Eqs. S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409)). More generally, $\mathbf v^T K=0$ makes $\mathbf v^T\delta\mathbf s$ constant during the noise-free linear return, even when stable modes are not a complete eigenvector basis. Once those modes decay, this constant is the remaining coordinate change. Consequently the surviving part of a small perturbation is
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

$$
\delta\mathbf s_{\mathrm{surviving}}
=\mathbf u\,(\mathbf v^T\delta\mathbf s).
$$

**Interpretation.** This generally differs from a perpendicular geometric projection. Decay can be tilted relative to the tangent. Even symmetric synaptic weights do not usually make $K$ symmetric, because $\phi'(\bar g_i)$ multiplies different rows by different amounts.

<div class="publisher-worked-calculation publisher-fold-always">

**Example: a disturbance that slides while it decays.**

To see the distinction without a neural simulation, let $x$ and $y$ be dimensionless state coordinates and consider the local system

$$
\dot x=ay,\qquad \dot y=-\lambda y,\quad\lambda>0,
\qquad [a]=[\lambda]=\mathrm{s}^{-1}.
$$

Every point with $y=0$ is fixed. Starting from $(x_0,y_0)$ gives $y(t)=y_0e^{-\lambda t}$ and

$$
x(\infty)=x_0+\frac{a}{\lambda}y_0.
$$

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.ContrastiveFormulas = NO -->
The response matrix and its neutral vectors are

$$
K=\begin{pmatrix}0&a\\0&-\lambda\end{pmatrix},\qquad
\mathbf u=\begin{pmatrix}1\\0\end{pmatrix},\qquad
\mathbf v=\begin{pmatrix}1\\a/\lambda\end{pmatrix}.
$$

The right vector $\mathbf u$ points along the fixed-point line. The left vector $\mathbf v$ reads out the final shift: $\mathbf v^T(x_0,y_0)=x_0+(a/\lambda)y_0$. The decaying eigenvector is $\mathbf z=(-a/\lambda,1)^T$, with $K\mathbf z=-\lambda\mathbf z$ and $\mathbf v^T\mathbf z=0$. A vertical perturbation changes the final memory whenever $a\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper.
<!-- vale ai-tells.ContrastiveFormulas = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<div class="figure-scroll">

{{block:fig:MEMORY-TILTED-DECAY}}

</div>

As $y$ decays, $x$ changes by one. The left vector extracts that lasting shift.

</div>

## Projecting spike fluctuations gives the diffusion coefficient {#sec:MEMORY-DIFFUSION}

**Paper location:** [Supporting text, Eqs. S14–S15, PDF p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3) gives the general local diffusion result; [the main article's diffusion discussion, PDF p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2) states its role in memory loss.

**Neural mechanism.** We can now calculate how much random displacement remains after the stable components have relaxed. [Each cell's random spikes disturb its outgoing synaptic activation. The circuit's return flow determines the lasting shift in memory.]{.key-statement} This calculation uses the weak noise and conditional independence assumptions, with rates and return flow evaluated near one fixed point.

**Mathematical derivation.** Recall the [projection vector $\mathbf v$ derived above](#sec-memory-linearization): a small disturbance $\delta\mathbf s$ leaves a coordinate shift $\delta\theta=\sum_i v_i\delta s_i$ after the other components decay. Thus $v_i$ is the lasting change in the represented value per unit change in neuron $i$'s synaptic activation, in this local linear model. These projection coefficients describe the whole circuit's response; they are distinct from its connection weights $W_{ij}$.

The variance of a linear combination of independent noise increments is the sum of their variances multiplied by squared weights. Multiplying the linear stochastic equation by $\mathbf v^T$ removes its deterministic return term because $\mathbf v^TK=0$, leaving

$$
d\theta=\mathbf v^T R^{1/2}d\mathbf B
=\sum_i v_i\sqrt{\bar r_i}\,dB_i.
$$

The independent Brownian increments have covariance $E[dB_i dB_j]=\delta_{ij}dt$, so

$$
E[(d\theta)^2]
=\sum_{ij}v_iv_j\sqrt{\bar r_i\bar r_j}\,E[dB_i dB_j]
=\left(\sum_i v_i^2\bar r_i\right)dt.
$$

<!-- vale ai-tells.EmDashUsage = NO -->
Matching this to $2D\,dt$ yields the general local result ([SI Eqs. S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576))
<!-- vale ai-tells.EmDashUsage = YES -->

$$
\boxed{2D(\theta)=\sum_i v_i(\theta)^2\bar r_i(\theta).}
$$

**Interpretation.** For one memory coordinate, each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$. The formula does not say that neurons with high rates necessarily damage memory more: changing rates can also change the tuning curves and the projection coefficients. Those changes must be included in a comparison.[^p1-projection]

The result is local in state and leading order in weak noise. The time interval must satisfy two conditions:

- It must be long enough for the approximation based on many spike contributions to apply.
- It must be short enough that the coefficients do not change substantially as the memory moves.

These conditions justify a local spreading rate.

**Paper location:** [Supporting text, multidimensional generalization, Eqs. S21–S27, PDF pp. 5–6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5). The paired-vector example that follows is added by the guide.

For several memory coordinates $\theta_\alpha$, choose tangent vectors $u_i^\alpha=\partial\bar s_i/\partial\theta_\alpha$ and left zero vectors $\mathbf v^\alpha$ satisfying $(\mathbf v^\alpha)^T K=0$ and $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. A unit change of coordinate $\beta$ moves the activation along $\mathbf u^\beta$. The projection vector $\mathbf v^\alpha$ extracts one unit when $\alpha=\beta$ and zero when the two coordinates differ. It also discards the decaying activity components. Thus $\sum_i v_i^\alpha\delta s_i$ gives the lasting local change in coordinate $\alpha$. The same covariance calculation gives

$$
2D_{\alpha\beta}=\sum_i v_i^\alpha\bar r_i v_i^\beta.
$$

[In this local approximation, the [**diffusion tensor**]{.definition-term custom-style="Definition Term"} is the matrix of displacement covariances divided by twice the elapsed time over a short interval.]{.definition-explanation} Its diagonal entries describe spreading in individual coordinates. Its other entries describe how coordinate displacements vary together. Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]

<details class="publisher-long-content publisher-long-example">
<summary>Example: reading two coordinates from tilted directions</summary>
<div class="publisher-fold-body">

Suppose two coordinate changes alter two activities along $\mathbf u^1=(1,0)^T$ and $\mathbf u^2=(1,1)^T$. A change by $a$ in the first coordinate and $b$ in the second gives the combined activity change $(a+b,b)^T$. The corresponding projection vectors are $\mathbf v^1=(1,-1)^T$ and $\mathbf v^2=(0,1)^T$: their dot products with the combined change give $a$ and $b$, respectively. For example, $\mathbf v^1$ removes the contribution of the second coordinate because $(\mathbf v^1)^T\mathbf u^2=0$. This is a geometric example of the paired vectors; it does not specify a biological circuit.

</div>
</details>

Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).

## Symmetric weights express diffusion through tuning curves {#sec:MEMORY-SYMMETRIC}

**Paper location:** [Main article, Eq. 2, PDF p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2); [supporting text, Eqs. S16–S18, PDF p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4). The printed main equation needs the authors' 2017 correction, identified beside the result below.

<!-- vale ai-tells.VerbTricolon = NO -->
**Neural mechanism.** The general formula uses the projection vector $\mathbf v$ derived from the network's dynamics. The distinct matrix $W$ contains the [connection weights](ch-foundations.html#sec-memory-spikes): $W_{ij}$ describes the effect of neuron $j$'s synaptic activation on neuron $i$'s input. [If each pair has equal connection weights in opposite directions, $W_{ij}=W_{ji}$, can we express $\mathbf v$ through the tuning curves and neural transfer function?]{.key-statement} Equal connection weights do not require equal firing responses. We retain the common synaptic time constant, a stable continuous family, and the weak noise and conditional independence assumptions.
<!-- vale ai-tells.VerbTricolon = YES -->

**Mathematical derivation.** The chain rule relates the slope of a response curve to the slope of its input curve. Here let $g_i'=d\bar g_i/d\theta$ and $r_i'=d\bar r_i/d\theta$. Differentiating the fixed point identities gives

$$
r_i'=\phi'(\bar g_i)g_i',
\qquad \mathbf g'=\tau W\mathbf r'.
$$

With symmetric $W$, the transpose of the linearized matrix satisfies

$$
K^T\mathbf g'
=-\mathbf g'/\tau+W\operatorname{diag}[\phi'(\bar g_i)]\mathbf g'
=-\mathbf g'/\tau+W\mathbf r'=0.
$$

<!-- vale ai-tells.FormalTransitions = NO -->
Therefore $\mathbf v$ is proportional to $\mathbf g'$. Its normalization is
<!-- vale ai-tells.FormalTransitions = YES -->

$$
v_i=\frac{g_i'}{\tau\sum_jr_j'g_j'},
$$

because $u_i=\tau r_i'$. Substituting into the noise projection gives

$$
\boxed{
2D(\theta)=
\frac{\sum_i\bar r_i(g_i')^2}
{\tau^2[\sum_i r_i'g_i']^2}.
}
$$

<!-- vale ai-tells.ContrastiveFormulas = NO -->
**Interpretation.** The input slopes $g_i'$ now determine the projection coefficients, so the diffusion coefficient can be calculated from the tuning curves and transfer function. This follows from [SI Eq. S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) omits the square on $g_i'$ in the numerator. [Burak and Fiete's published correction (2017)](https://doi.org/10.1073/pnas.1706051114) confirms the squared expression shown here, which also follows from the projection calculation and SI S18. The guide's checks of other printed formulas remain separate from that correction. The result requires:
<!-- vale ai-tells.ContrastiveFormulas = YES -->

- Symmetric weights.
- A stable continuous family.
- The noise assumptions already introduced.

The result does not require [**translation symmetry**]{.definition-term custom-style="Definition Term"}, in which shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.[^p1-symmetric]

<div class="publisher-worked-calculation publisher-fold-always">

**Example: opposite firing changes with constant diffusion.**

Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

$$
\bar s_1=\frac{b+\theta}{2},\qquad
\bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b.
$$

Here $b$ is an activation bias and $\theta=s_1-s_2$ is an activation difference. These have different units from the rate baseline and angle in the [earlier two-cell example](ch-persistence.html#sec-foundations-attractor-example). Writing that example's baseline as $b_{\mathrm{rate}}$ and its angle as $\theta_{\mathrm{angle}}$, the conversion is $b=2\tau b_{\mathrm{rate}}$ and $\theta=2\tau k\theta_{\mathrm{angle}}$. The sum $s_1+s_2$ relaxes to $b$ at rate $2/\tau$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

$$
2D=\bar r_1+\bar r_2=b/\tau.
$$

The boxed tuning-curve formula gives the same result. Here $\bar g_1=(b+\theta)/2$ and $\bar g_2=(b-\theta)/2$, so $g_1'=1/2$, $g_2'=-1/2$ and $r_i'=g_i'/\tau$. Thus $\sum_i r_i'g_i'=1/(2\tau)$ and the boxed formula reduces to $2D=\bar r_1+\bar r_2$.

<!-- vale ai-tells.DefensiveHedges = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.FormalTransitions = NO -->
Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible. A physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](ch-memory-long-delays.html#fig-paper-memory-2).[^p1-two]
<!-- vale ai-tells.FormalTransitions = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.DefensiveHedges = YES -->

The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

<div class="figure-scroll">

{{block:fig:MEMORY-INHIBITION-RATES}}

</div>

<!-- vale ai-tells.FigurativeStays = NO -->
The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$.
<!-- vale ai-tells.FigurativeStays = YES -->

</div>

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). [Main Eq. 1 and the steady state, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,60); [Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.AnthropomorphicCognition = NO -->
<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-weak]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). [Weak Fluctuations, Eqs. 10–11, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,550), [continuation, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22); [SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128). Brownian increment notation is a teaching rewrite of the paper's white noise notation.
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->
<!-- vale ai-tells.AnthropomorphicCognition = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-large]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S1, p. 1](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1&zoom=125,0,548); [Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128); [ring population limit, Eq. S6, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,539). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-projection]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 3: [linearization, Eqs. S7–S10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,82); [tangent, Eq. S11](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,328); [left vector, Eqs. S12–S13](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409); [projected diffusion, Eqs. S14–S15](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576). [DOI](https://doi.org/10.1073/pnas.1117386109). The left vector interpretation is expanded here for teaching.
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
<!-- vale ai-tells.SemicolonUsage = NO -->
[^p1-multid]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S21, p. 5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,592); [Eqs. S22–S27, p. 6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=6&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.SemicolonUsage = YES -->
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-symmetric]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88); [Supporting Text, Eqs. S16–S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109).
<!-- vale ai-tells.EmDashUsage = YES -->

<!-- vale ai-tells.EmDashUsage = NO -->
[^p1-two]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 2E–G and caption, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205); [Network Simulations, mutual inhibition, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22). [DOI](https://doi.org/10.1073/pnas.1117386109). The activation coordinate is made explicit here to avoid confusing it with a rate difference, which rescales $D$ by $1/\tau^2$.
<!-- vale ai-tells.EmDashUsage = YES -->
