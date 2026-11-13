# Spiking noise produces diffusion along the memory attractor {#ch:MEMORY-DYNAMICS}

A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied. The important question is whether the activity pattern stays in the right place, not just whether activity continues. Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set. This chapter derives how random spikes move the network along that set. The next chapter asks how well another network can read the moving memory.[^p1-model]

Paper and Supporting Information (SI) links open the cited PDF page, near the passage where the viewer supports it. Use the equation, figure, or paragraph label to find the passage; the PDFs have no numbered text lines.

The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.

## Recurrent spikes renew decaying synaptic activity {#sec:MEMORY-SPIKES}

How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. Incoming activations determine new firing rates; the resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.

Let $N_i(t)$ count neuron $i$'s spikes up to time $t$. The activation $s_i$ rises by one at each of its spikes and otherwise decays:

$$
ds_i=-\frac{s_i}{\tau}\,dt+dN_i(t).
$$

Equivalently, if its spikes occur at times $t_i^\alpha$,

$$
s_i(t)=\sum_{t_i^\alpha<t}\exp[-(t-t_i^\alpha)/\tau]
$$

after initial transients. Here $s_i$ is dimensionless in the convention that each spike adds one unit.

For five illustrative spike times, the plot shows the events and the activation they leave behind.

<div class="figure-scroll">

{{block:fig:MEMORY-SPIKE-TRACE}}

</div>

The activation retains a decaying contribution from earlier spikes, so a spike train and its activation trace are different objects.

The rate $r_i$ has units of spikes per second. The summed input and the firing rule are

$$
g_i=\sum_j W_{ij}s_j+b_i,
\qquad r_i=\phi(g_i).
$$

The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate. For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model]

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

where the $B_i$ are independent standard Brownian processes. The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Gaussian approximation is for small fluctuations in total input. It does not require each single neuron's entire spike train to look like a Gaussian process ([SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak]

The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks. Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]

Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

$$
0=-\frac{\bar s_i(\theta)}{\tau}
+\phi[\bar g_i(\theta)],
\qquad
\bar s_i(\theta)=\tau\bar r_i(\theta).
$$

The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.

## The network's return flow determines the lasting memory change {#sec:MEMORY-LINEARIZATION}

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

so $\mathbf v^T\mathbf z=0$. The left vector discards every decaying mode ([SI Eqs. S12–S13, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409)). Consequently the surviving part of a small perturbation is

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

The exact trajectory in this example shows why the lasting displacement follows the flow rather than a perpendicular projection.

<div class="figure-scroll">

{{block:fig:MEMORY-TILTED-DECAY}}

</div>

As y decays, x changes by one; the left vector extracts that lasting shift.

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

Matching this to $2D\,dt$ yields the general local result ([SI Eqs. S14–S15, p. 3](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576))

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

## Symmetric weights express diffusion through tuning curves {#sec:MEMORY-SYMMETRIC}

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

This follows from [SI Eq. S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator; the projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction. The result requires symmetric weights, a stable continuous family, and the noise assumptions already introduced; translation symmetry is unnecessary.[^p1-symmetric]

**Example: opposite firing changes with constant diffusion.** Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

$$
\bar s_1=\frac{b+\theta}{2},\qquad
\bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b.
$$

The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

$$
2D=\bar r_1+\bar r_2=b/\tau.
$$

Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible; a physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205).[^p1-two]

The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

<div class="figure-scroll">

{{block:fig:MEMORY-INHIBITION-RATES}}

</div>

The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$.

## Long delay errors depend on boundaries and local diffusion {#sec:MEMORY-LONG-TIME}

A local diffusion coefficient answers how variance initially grows. It does not by itself say that variance grows at the same rate forever. Boundaries and variation of $D$ can change the long time behavior.

Let $p(\theta,t)$ be the density of the memory coordinate across repeated trials initialized at $\Theta$. The [**Itô convention**]{.definition-term custom-style="Definition Term"} evaluates a state-dependent noise coefficient at the beginning of each increment. In the zero-drift diffusion approximation, this density evolves according to the [**Fokker Planck equation**]{.definition-term custom-style="Definition Term"}:

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

Its variance is $2Dt$. For an angular coordinate, add the densities at all displacements $\theta-\Theta+2\pi k$, $k\in\mathbb Z$, to wrap the Gaussian around the circle. This teaches the content of [SI Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483) without needing the special function notation used there. At long times the density approaches $1/(2\pi)$. If angular errors are reported in $[-\pi,\pi)$, their limiting mean squared value is

$$
\frac{1}{2\pi}\int_{-\pi}^{\pi}x^2dx=\frac{\pi^2}{3}.
$$

The flattening of a ring network's error curve can therefore occur while its local noise mechanism remains unchanged. It reflects the bounded way angular error is reported.[^p1-fp]

For $D=0.5\,\mathrm{rad}^2/\mathrm{s}$, the plots show how the density and squared error change with delay.

<div class="figure-scroll">

{{block:fig:MEMORY-LINE-RING}}

</div>

As the upper density approaches uniform, the wrapped error below approaches $\pi^2/3$; the line error keeps growing.

**Expandable note: Derivation: from random increments to the memory density equation**
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

This is [SI Eq. S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,602). A state dependent $D$ need not produce a curved variance versus time graph. If $D$ is linear in $\theta$, then $E[D(\theta)]=D(E[\theta])=D(\Theta)$, so the variance remains linear while the process stays within the model's valid domain.[^p1-variable]

The supplement illustrates this with mutual excitation, $W_{12}=W_{21}=1$, biases $(b_0,-b_0)$, and the same linear transfer rule. The fixed activation states are $(\theta+b_0/2,\theta-b_0/2)$. Now $\mathbf u=(1,1)^T$, $\mathbf v=(1/2,1/2)^T$, and

$$
2D=\frac{1}{4}(\bar r_1+\bar r_2)=\frac{\theta}{2\tau},
\qquad D=\frac{\theta}{4\tau}.
$$

The implied variance is $\Theta t/(2\tau)$, agreeing with [SI Eq. S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,383) and the slope tested in [Fig. S1, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10&zoom=125,0,45). SI Eq. S40 instead prints $D=\theta/(2\tau)$. Under the convention used throughout this guide, that displayed value differs by a factor of two from the direct projection and S41. We keep the calculation explicit so the discrepancy does not become a hidden change of convention.[^p1-excitation]

## A diffusion calculation does not determine systematic drift {#sec:MEMORY-DRIFT-SCOPE}

Repeated trials can spread apart even if their average stays at the original value. That random spreading differs from a reproducible movement in one direction. Both can occur, and the derivation of $D$ alone does not settle the second question.

The paper assumes that the network is tuned to eliminate [**systematic drift**]{.definition-term custom-style="Definition Term"}, meaning a nonzero mean velocity along the attractor. A deterministic mismatch in weights can create such a velocity. In addition, state dependent noise and curved network dynamics can create a small mean motion even if the noise free model has an exact continuous attractor. The supplement explains that deriving the exact mean motion requires the microscopic jump process, beyond the leading variance calculation ([SI “Systematic drift,” pp. 4–5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362)).[^p1-systematic]

For state dependent $D$, where the coefficient is evaluated affects the process. The [**Stratonovich convention**]{.definition-term custom-style="Definition Term"} uses midpoint evaluation in its limiting increments. With the same written coefficient and zero written drift, it describes a different process from the Itô equation. Converting the Stratonovich equation into Itô form adds a drift $D'/2$. This follows from the conversion term $bb'/2$ with $b=\sqrt{2D}$ and $bb'=D'$. The supplement uses the difference to estimate a possible scale of noise induced drift, not to identify the exact drift of every neural network.

With $D$ of order $1/N$, random displacement over $dt$ is of order $\sqrt{dt/N}$, while such a mean displacement is of order $dt/N$. The variance calculation captures the leading random term. Small changes to weights or biases might cancel the mean drift; they cannot remove the random increments by subtracting a known average. A known mean drift can in principle be accounted for by a decoder, but any actual implementation must know that drift and respect the domain and boundary conditions.

The independence assumption also has a precise scope. Newly generated spike-count fluctuations are conditionally independent given the present state. Shared recurrent fluctuations can still correlate the observed spike trains over time. An extra source of correlated fluctuations would change the projection formula to $2D=\mathbf v^TQ\mathbf v$, where $Q\,dt$ is their increment covariance. Calculating the corresponding Fisher information would require the matching joint likelihood. The paper discusses such correlated models as future extensions ([Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142)); it does not prove that every correlated spiking model obeys its Poisson formulas.[^p1-correlation]

## Figures distinguish memory motion from readout error and test diffusion {#sec:MEMORY-FIGURES}

[Figure 1A, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439) shows the definition of the memory coordinate. Start at a green point off the attractor and follow the noise free flow to the black point on it. This endpoint defines the instantaneous attractor state. After one noisy interval, repeat that flow. The difference between the two endpoints is the retained memory change. The relevant projection follows the flow, as in the tilted two variable example above.

In Fig. 1B, an [**activity bump**]{.definition-term custom-style="Definition Term"} is a localized peak of population firing rates across the neurons' preferred angles. Its location has moved away from its initial value $\Theta$ during storage. At the later time, an observer has additional uncertainty about the bump's current location because it sees only a finite sample of spikes. The next chapter derives this second uncertainty and relates it to the first.[^p1-fig1]

[Figure 2, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,18) tests the diffusion calculation in two different network designs. Panel A shows a ring with weights determined by differences of preferred angles. In B, compare the firing rate curves and spike marks in the inset before reading the wandering angular trace. The curve describes rates; the marks are particular random spike events. The trace shows the represented angle rather than overall activity amplitude.

Panel C compares simulated mean squared angular displacements with the prediction from the tuning curves and transfer function. The gray exponential case and black sigmoidal, or S-shaped, case have different transfer functions. The dashed bound is a lower limit for the sigmoidal case, not a separate fitted trajectory. A model can lie above its information bound while still agree with the derived diffusion formula. Panel D follows angular error to longer intervals; its flattening uses angular wrapping, not a disappearance of noise. The expected limiting value with the caption's error convention is $\pi^2/3$.

Panels E to G use mutual inhibition rather than a ring. The two rates in F vary in opposite directions; their difference represents memory. Panel G compares their displacement statistics with the analytic prediction. This second design matters because the projection argument does not require rotational symmetry. These are simulations checking the model calculation. They are not direct measurements of memory noise in an animal.[^p1-fig2]

The derivation has now supplied a dynamical quantity, $D$, from spike variability and the way a network returns to its attractor. We next derive a statistical quantity from the same tuning curves and ask why it puts a lower limit on $D$.

[^p1-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. https://doi.org/10.1073/pnas.1117386109. [Main Eq. 1 and the steady state, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,60); [Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372).

[^p1-weak]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. https://doi.org/10.1073/pnas.1117386109. [Weak Fluctuations, Eqs. 10–11, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,550), [continuation, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22); [SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128). Brownian increment notation is a teaching rewrite of the paper's white noise notation.

[^p1-large]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S1, p. 1](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1&zoom=125,0,548); [Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128); [ring population limit, Eq. S6, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,539). https://doi.org/10.1073/pnas.1117386109.

[^p1-projection]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 3: [linearization, Eqs. S7–S10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,82); [tangent, Eq. S11](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,328); [left vector, Eqs. S12–S13](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409); [projected diffusion, Eqs. S14–S15](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576). https://doi.org/10.1073/pnas.1117386109. The left vector interpretation is expanded here for teaching.

[^p1-multid]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S21, p. 5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,592); [Eqs. S22–S27, p. 6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=6&zoom=125,0,48). https://doi.org/10.1073/pnas.1117386109.

[^p1-symmetric]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88); [Supporting Text, Eqs. S16–S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,48). https://doi.org/10.1073/pnas.1117386109.

[^p1-two]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 2E–G and caption, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205); [Network Simulations, mutual inhibition, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22). https://doi.org/10.1073/pnas.1117386109. The activation coordinate is made explicit here to avoid confusing it with a rate difference, which rescales $D$ by $1/\tau^2$.

[^p1-fp]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [density equation, Eqs. S28–S29, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,48); [Gaussian on a line, Eq. S30, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,329); [wrapped density and uniform limit, Eq. S31, p. 7](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=7&zoom=125,0,483); [angular error, Eq. S32, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,48). https://doi.org/10.1073/pnas.1117386109. The uniform angular variance calculation is a teaching reconstruction.

[^p1-variable]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, [Supporting Text, Eqs. S33–S37, p. 8](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=8&zoom=125,0,139). https://doi.org/10.1073/pnas.1117386109.

[^p1-excitation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, [Supporting Text, Eqs. S38–S41, p. 9](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=9&zoom=125,0,48); [Fig. S1, p. 10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=10&zoom=125,0,45). https://doi.org/10.1073/pnas.1117386109. The factor discrepancy between S40, S41, and the projection calculation is visible in the supplied PDF; no author correction is asserted.

[^p1-systematic]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [“Systematic drift,” p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,362); [Eqs. S19–S20 and continuation, p. 5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,48). https://doi.org/10.1073/pnas.1117386109.

[^p1-correlation]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Discussion, p. 5, paragraph beginning “Our spiking model”](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,142). https://doi.org/10.1073/pnas.1117386109. The covariance projection is an immediate linear algebra extension; the paper's proposed general correlated noise inequality remains a conjecture there.

[^p1-fig1]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 1 and caption, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,439); [flow definition, “In what follows,” p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,191). https://doi.org/10.1073/pnas.1117386109.

[^p1-fig2]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 2 and caption, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,18); Network Simulations: [ring model, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,103) and [mutual inhibition, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22). https://doi.org/10.1073/pnas.1117386109.
