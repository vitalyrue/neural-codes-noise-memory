# How spiking noise moves a stored memory {#ch:MEMORY-DYNAMICS}

A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied. The important question is whether the activity pattern stays in the right place, not just whether activity continues. Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set. This chapter derives how random spikes move the network along that set. The next chapter asks how well another network can read the moving memory.[^p1-model]

The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.

## From individual spikes to a slowly changing network state {#sec:MEMORY-SPIKES}

How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. Incoming activations determine new firing rates; the resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.

Let $N_i(t)$ count neuron $i$'s spikes up to time $t$. The activation $s_i$ rises by one at each of its spikes and otherwise decays:

$$
ds_i=-\frac{s_i}{\tau}\,dt+dN_i(t).
$$

Equivalently, if its spikes occur at times $t_i^\alpha$,

$$
s_i(t)=\sum_{t_i^\alpha<t}\exp[-(t-t_i^\alpha)/\tau]
$$

after initial transients. Here $s_i$ is dimensionless in the convention that each spike adds one unit. The rate $r_i$ has units of spikes per second. The summed input and the firing rule are

$$
g_i=\sum_j W_{ij}s_j+b_i,
\qquad r_i=\phi(g_i).
$$

The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate. For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first.[^p1-model]

Conditioned on the present rates, spike counts over a short interval $dt$ are independent Poisson variables. Thus

$$
E[dN_i\mid r_i]=r_i\,dt,
\qquad
\operatorname{Cov}(dN_i,dN_j\mid\mathbf r)
=\delta_{ij}r_i\,dt.
$$

The symbol $\delta_{ij}$ is one when $i=j$ and zero otherwise. Splitting the count into its mean and fluctuation gives

$$
ds_i=\left[-\frac{s_i}{\tau}+\phi(g_i)\right]dt+dM_i,
\qquad
E[dM_i]=0,
\quad E[dM_i dM_j]=\delta_{ij}r_i\,dt.
$$

This is still a jump process. In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input. Their summed fluctuation can then be represented by Gaussian noise with the same leading mean and covariance:

$$
ds_i=F_i(\mathbf s)dt+\sqrt{r_i}\,dB_i,
\qquad
F_i(\mathbf s)=-s_i/\tau+\phi\!\left(\sum_jW_{ij}s_j+b_i\right),
$$

where the $B_i$ are independent standard Brownian processes. The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Gaussian approximation is for small fluctuations in total input. It does not require each single neuron's entire spike train to look like a Gaussian process.[^p1-weak]

The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks. Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]

Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

$$
0=-\frac{\bar s_i(\theta)}{\tau}
+\phi[\bar g_i(\theta)],
\qquad
\bar s_i(\theta)=\tau\bar r_i(\theta).
$$

The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.

## Which part of a perturbation survives? {#sec:MEMORY-LINEARIZATION}

A spike perturbs many aspects of a network's state. Most of those changes decay as the state returns to the attractor. To calculate memory loss, we need the one change that survives: the displacement to a different fixed point.

Write the current activation as $\mathbf s=\bar{\mathbf s}(\theta)+\delta\mathbf s$. A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to the small perturbation and drops terms quadratic or higher in it. Taylor expansion of the transfer function gives

$$
\phi\!\left(\bar g_i+\sum_j W_{ij}\delta s_j\right)
\simeq\phi(\bar g_i)+\phi'(\bar g_i)\sum_jW_{ij}\delta s_j.
$$

The constant terms cancel because $\bar{\mathbf s}$ is a fixed point. Therefore

$$
d\delta\mathbf s=K\delta\mathbf s\,dt+R^{1/2}d\mathbf B,
\qquad
K_{ij}=-\frac{\delta_{ij}}{\tau}+\phi'(\bar g_i)W_{ij},
\qquad R=\operatorname{diag}(\bar r_i).
$$

In this leading local calculation the noise strengths are evaluated at the fixed point. The entries of $K$ have units of inverse time.[^p1-projection]

Moving a little along the fixed point family changes the activation by

$$
\delta\mathbf s\simeq\mathbf u\,\delta\theta,
\qquad u_i=\frac{d\bar s_i}{d\theta}=\tau\frac{d\bar r_i}{d\theta}.
$$

Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$. The chain rule gives

$$
K\mathbf u=0.
$$

Thus $\mathbf u$ is a [**right zero eigenvector**]{.definition-term custom-style="Definition Term"}: a state direction that the linear dynamics neither restores nor amplifies. It is the tangent to the attractor. The other modes must decay for this local family to be attracting.

We also need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying

$$
\mathbf v^T K=0,
\qquad \mathbf v^T\mathbf u=1.
$$

Its purpose is to extract the lasting memory displacement from a general perturbation. The normalization makes $\mathbf v^T(\mathbf u\,\delta\theta)=\delta\theta$. If a stable mode $\mathbf z$ satisfies $K\mathbf z=\lambda\mathbf z$ with $\lambda\ne0$, then

$$
0=\mathbf v^T K\mathbf z=\lambda\mathbf v^T\mathbf z,
$$

so $\mathbf v^T\mathbf z=0$. The left vector discards every decaying mode. Consequently the surviving part of a small perturbation is

$$
\delta\mathbf s_{\mathrm{surviving}}
=\mathbf u\,(\mathbf v^T\delta\mathbf s).
$$

This generally differs from a perpendicular geometric projection. Decay can be tilted relative to the tangent. Even symmetric synaptic weights do not usually make $K$ symmetric, because $\phi'(\bar g_i)$ multiplies different rows by different amounts.

**Example: a disturbance that slides while it decays.** To see the distinction without a neural simulation, consider the local system

$$
\dot x=ay,\qquad \dot y=-\lambda y,\quad\lambda>0.
$$

Every point with $y=0$ is fixed. Starting from $(x_0,y_0)$ gives $y(t)=y_0e^{-\lambda t}$ and

$$
x(\infty)=x_0+\frac{a}{\lambda}y_0.
$$

Here $\mathbf u=(1,0)^T$ and $\mathbf v=(1,a/\lambda)^T$. A vertical perturbation changes the final memory whenever $a\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper.

## Projecting spike fluctuations gives the diffusion coefficient {#sec:MEMORY-DIFFUSION}

We can now calculate how much random displacement remains after the stable components have relaxed. Multiply the linear stochastic equation by $\mathbf v^T$. Since $\mathbf v^TK=0$,

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

Matching this to $2D\,dt$ yields the general local result

$$
\boxed{2D(\theta)=\sum_i v_i(\theta)^2\bar r_i(\theta).}
$$

Each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$. The formula does not say that neurons with high rates necessarily damage memory more: changing rates can also change the tuning curves and the projection weights. Those changes must be included in a comparison.[^p1-projection]

The result is local in state and leading order in weak noise. A short interval must be long enough for the coarse description of many spike contributions to apply, yet short enough that the coefficients do not change substantially as the memory moves. Systematic drift requires a separate check below.

For several memory coordinates $\theta_\alpha$, choose tangent vectors $u_i^\alpha=\partial\bar s_i/\partial\theta_\alpha$ and left vectors with $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. The same covariance calculation gives

$$
2D_{\alpha\beta}=\sum_i v_i^\alpha\bar r_i v_i^\beta.
$$

The [**diffusion tensor**]{.definition-term custom-style="Definition Term"} is the matrix of displacement covariances per twice the elapsed time. Its diagonal entries describe spreading in individual coordinates; its other entries describe how coordinate displacements vary together. Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]

## Symmetric weights make the projection measurable {#sec:MEMORY-SYMMETRIC}

The general formula requires the left vector of the network dynamics. When $W_{ij}=W_{ji}$, can we write it using tuning curves and the input to rate rule?

Let $g_i'=d\bar g_i/d\theta$ and $r_i'=d\bar r_i/d\theta$. Differentiating the fixed point identities gives

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

Therefore $\mathbf v$ is proportional to $\mathbf g'$. Its normalization is

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

This follows from SI Eq. S18, with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition main Eq. 2 appears to omit the square on $g_i'$ in the numerator; the projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction. The result requires symmetric weights, a stable continuous family, and the noise assumptions already introduced; translation symmetry is unnecessary.[^p1-symmetric]

**Example: opposite firing changes with constant diffusion.** Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

$$
\bar s_1=\frac{b+\theta}{2},\qquad
\bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b.
$$

The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

$$
2D=\bar r_1+\bar r_2=b/\tau.
$$

Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible; a physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in Fig. 2.[^p1-two]

## From local spreading to long delay errors {#sec:MEMORY-LONG-TIME}

A local diffusion coefficient answers how variance initially grows. It does not by itself say that variance grows at the same rate forever. Boundaries and variation of $D$ can change the long time behavior.

Let $p(\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\Theta$. The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment. To pass from random increments to a density equation, choose any smooth function $F(\theta)$. In a short interval $dt$, the zero-drift Itô increment has conditional mean zero and conditional second moment $2D(\theta)dt$. Taylor expansion at the starting coordinate gives

$$
\begin{aligned}
\mathbb E[F(\theta+d\theta)-F(\theta)\mid\theta]
&=F'(\theta)\mathbb E[d\theta\mid\theta]
+\tfrac12F''(\theta)\mathbb E[(d\theta)^2\mid\theta]+o(dt)\\
&=D(\theta)F''(\theta)dt+o(dt).
\end{aligned}
$$

The higher-order terms vanish faster than $dt$ in this diffusion approximation. Averaging over the starting-coordinate density and dividing by $dt$ gives

$$
\frac{d}{dt}\int F(\theta)p(\theta,t)\,d\theta
=\int F''(\theta)D(\theta)p(\theta,t)\,d\theta.
$$

Take $F$ to vanish outside an interior region, or use boundaries for which the integration terms vanish. Integrating by parts twice moves both derivatives from $F$ onto the product $Dp$. Because the resulting identity holds for every such smooth $F$, the density obeys the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:

$$
\frac{\partial p}{\partial t}
=\frac{\partial^2}{\partial\theta^2}[D(\theta)p],
\qquad p(\theta,0)=\delta(\theta-\Theta).
$$

Here the [**Dirac delta**]{.definition-term custom-style="Definition Term"} denotes a point mass: initially all probability is at $\Theta$. It differs from the earlier zero-or-one symbol $\delta_{ij}$. For constant $D$ on an unbounded line, the Gaussian solution is

$$
p(\theta,t)=\frac{1}{\sqrt{4\pi Dt}}
\exp\left[-\frac{(\theta-\Theta)^2}{4Dt}\right].
$$

Its variance is $2Dt$. For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle. This teaches the content of SI Eq. S31 without needing the special function notation used there. At long times the density approaches $1/(2\pi)$. If angular errors are reported in $[-\pi,\pi)$, their limiting mean squared value is

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}x^2dx=\frac{\pi^2}{3}.
$$

The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.[^p1-fp]

When $D$ varies with state, the zero drift stochastic equation is $d\theta=\sqrt{2D(\theta)}\,dB$ with the Itô convention. Under conditions that remove boundary terms, the density equation gives

$$
\frac{d}{dt}E[\theta]=0,
\qquad
\frac{d}{dt}\operatorname{Var}(\theta)=2E[D(\theta)].
$$

For completeness, multiply the density equation by $\theta$ or $(\theta-\Theta)^2$, integrate over $\theta$, and integrate by parts twice. The second derivatives of these functions are respectively zero and two, giving the two identities. A similar calculation for the smooth function $D$ gives $dE[D]/dt=E[DD'']$. Expanding at $t=0$ therefore yields

$$
\operatorname{Var}(\theta)
=2D(\Theta)t+D(\Theta)D''(\Theta)t^2+O(t^3).
$$

This is SI Eq. S37. A state dependent $D$ need not produce a curved variance versus time graph. If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain.[^p1-variable]

The supplement illustrates this with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule. The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$. Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$, and

$$
2D=\frac{1}{4}(\bar r_1+\bar r_2)=\frac{\theta}{2\tau},
\qquad D=\frac{\theta}{4\tau}.
$$

The implied variance is $\Theta t/(2\tau)$, agreeing with SI Eq. S41 and the slope tested in Fig. S1. SI Eq. S40 instead prints $D=\theta/(2\tau)$. Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41. We keep the calculation explicit so the discrepancy does not become a hidden change of convention.[^p1-excitation]

## Random drift, systematic drift, and a mistuned network {#sec:MEMORY-DRIFT-SCOPE}

Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction. Both can occur, and the derivation of $D$ alone does not settle the second question.

The paper assumes that the network is tuned to eliminate [**systematic drift**]{.definition-term custom-style="Definition Term"}, meaning a nonzero mean velocity along the attractor. A deterministic mismatch in weights can create such a velocity. In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor. The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation.[^p1-systematic]

For state dependent $D$, where the coefficient is evaluated affects the process. The [**Stratonovich convention**]{.definition-term custom-style="Definition Term"} uses midpoint evaluation in its limiting increments. With the same written coefficient and zero written drift, it describes a different process from the Itô equation. Converting the Stratonovich equation into Itô form adds a drift $D'/2$. This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$. The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network.

With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$. The variance calculation captures the leading random term. Small changes to weights or biases might cancel the mean drift; they cannot remove the random increments by subtracting a known average. A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions.

The independence assumption also has a precise scope. Newly generated spike-count fluctuations are conditionally independent given the present state. Shared recurrent fluctuations can still correlate the observed spike trains over time. An extra source of correlated fluctuations would change the projection formula to $2D=\mathbf v^TQ\mathbf v$, where $Q\,dt$ is their increment covariance. Calculating the corresponding Fisher information would require the matching joint likelihood. The paper discusses such correlated models as future extensions; it does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]

## Reading the first two figures {#sec:MEMORY-FIGURES}

Figure 1A shows the definition of the memory coordinate. Start at a green point off the attractor and follow the noise free flow to the black point on it. This endpoint defines the instantaneous attractor state. After one noisy interval, repeat that flow. The difference between the two endpoints is the retained memory change. The relevant projection follows the flow, as in the tilted two variable example above.

In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles. Its location has moved away from its initial value $\Theta$ during storage. At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes. The next chapter derives this second uncertainty and relates it to the first.[^p1-fig1]

Figure 2 tests the diffusion calculation in two different network designs. Panel A shows a ring with weights determined by differences of preferred angles. In B, compare the firing rate curves and spike marks in the inset before reading the wandering angular trace. The curve describes rates; the marks are particular random spike events. The trace shows the represented angle rather than overall activity amplitude.

Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agree with the derived diffusion formula. Panel D follows angular error to longer intervals; its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.

Panels E to G use mutual inhibition rather than a ring. The two rates in F vary in opposite directions; their difference represents memory. Panel G compares their displacement statistics with the analytic prediction. This second design matters because the projection argument does not require rotational symmetry. These are simulations checking the model calculation. They are not direct measurements of memory noise in an animal.[^p1-fig2]

The derivation has now supplied a dynamical quantity, $D$, from spike variability and the way a network returns to its attractor. We next derive a statistical quantity from the same tuning curves and ask why it puts a lower limit on $D$.

[^p1-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. https://doi.org/10.1073/pnas.1117386109. Main text pp. 1–2 and 5, Eqs. 1 and 7–9.

[^p1-weak]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. https://doi.org/10.1073/pnas.1117386109. Main text pp. 5–6, Eqs. 10–11; Supporting Text, Section I. Brownian increment notation is a teaching rewrite of the paper's white noise notation.

[^p1-large]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 1–2, Eqs. S1–S6. https://doi.org/10.1073/pnas.1117386109.

[^p1-projection]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 3–4, Eqs. S7–S15. https://doi.org/10.1073/pnas.1117386109. The left vector interpretation is expanded here for teaching.

[^p1-multid]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 5–6, Eqs. S21–S27. https://doi.org/10.1073/pnas.1117386109.

[^p1-symmetric]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, main Eq. 2; Supporting Text, p. 4, Eqs. S16–S18. https://doi.org/10.1073/pnas.1117386109.

[^p1-two]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Fig. 2E–G and Network Simulations, p. 6. https://doi.org/10.1073/pnas.1117386109. The activation coordinate is made explicit here to avoid confusing it with a rate difference, which rescales $D$ by $1/\tau^2$.

[^p1-fp]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 6–8, Eqs. S28–S32. https://doi.org/10.1073/pnas.1117386109. The uniform angular variance calculation is a teaching reconstruction.

[^p1-variable]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 8, Eqs. S33–S37. https://doi.org/10.1073/pnas.1117386109.

[^p1-excitation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 8–10, Eqs. S38–S41 and Fig. S1. https://doi.org/10.1073/pnas.1117386109. The factor discrepancy between S40, S41, and the projection calculation is visible in the supplied PDF; no author correction is asserted.

[^p1-systematic]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, pp. 4–5, Systematic drift, Eqs. S19–S20. https://doi.org/10.1073/pnas.1117386109.

[^p1-correlation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Discussion, p. 5. https://doi.org/10.1073/pnas.1117386109. The covariance projection is an immediate linear algebra extension; the paper's proposed general correlated noise inequality remains a conjecture there.

[^p1-fig1]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Fig. 1, p. 2. https://doi.org/10.1073/pnas.1117386109.

[^p1-fig2]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, Fig. 2, p. 3; Network Simulations, p. 6. https://doi.org/10.1073/pnas.1117386109.
