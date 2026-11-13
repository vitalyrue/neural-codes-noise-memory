# Spiking noise produces diffusion along the memory attractor {#ch:MEMORY-DYNAMICS}

[A network can keep firing after a stimulus disappears and still lose the value that the stimulus supplied.]{.key-statement} The important question is whether the activity pattern stays in the right place, not just whether activity continues. Burak and Fiete study this distinction in a network whose stable activity patterns form a continuous set.[^p1-model]

To calculate the loss of accuracy, we first describe how spikes renew synaptic activity as it decays. We then follow a small disturbance through the circuit's return toward a stable pattern and identify the change in stored value that remains. Adding these lasting random changes gives a local rate of spreading. When connections have equal weights in both directions, we can express that rate using the cells' tuning curves and check its meaning in a two-cell example. The following chapter asks how this local prediction extends to longer delays.

Paper and Supporting Information (SI) links open the cited PDF page, near the passage where the viewer supports it. Use the equation, figure, or paragraph label to find the passage; the PDFs have no numbered text lines.

The memory coordinate is $\theta$. Its initial value is $\Theta$. A bar denotes a noise free steady state, so $\bar r_i(\theta)$ is neuron $i$'s steady firing rate at memory value $\theta$. The common synaptic time constant is $\tau$. A one dimensional diffusion coefficient $D$ has units of memory coordinate squared per time, with the convention $\operatorname{Var}[\theta(t)-\Theta]=2Dt$ when $D$ is constant and boundaries do not matter.

## Recurrent spikes renew decaying synaptic activity {#sec:MEMORY-SPIKES}

**Neural mechanism.** How can brief spikes maintain a state for much longer than the duration of a spike? In this model, each spike leaves a synaptic activation that decays gradually. [Incoming activations determine new firing rates; the resulting spikes renew those activations. This feedback can support activity after the external stimulus has ended.]{.key-statement}

The model assumes fixed connection weights, constant biases, a common synaptic decay time, and independent Poisson spike counts conditional on the present rates. The connections are tuned to a continuous family of steady patterns. The Gaussian description below also assumes weak fluctuations in total input.

**Mathematical derivation.** To combine discrete events with continuous decay, a count process records the events and a decay equation records how their effects fade. Here $N_i(t)$ counts neuron $i$'s spikes up to time $t$. The activation $s_i$ tracks the decaying synaptic effect of those outgoing spikes on receiving cells. It rises by one at each spike and otherwise decays:

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

The fixed weights $W_{ij}$ say how neuron $j$ affects neuron $i$, and $b_i$ is a constant input. [The [**neural transfer function**]{.definition-term custom-style="Definition Term"} $\phi$ converts total input into a nonnegative firing rate.]{.definition-explanation} For example, increasing input might increase firing linearly over some input range, or exponentially. The paper allows general connectivity and transfer functions at first ([Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372)).[^p1-model]

A spike from cell $j$ raises $s_j$ by one and therefore changes the input to cell $i$ by $W_{ij}$. That contribution then decays over time $\tau$. For an increasing transfer function, a positive weight raises the receiving cell's rate and a negative weight lowers it. The resulting new spikes affect other cells in turn. Thus the weights set where a disturbance goes, the transfer function sets the rate response, and $\tau$ sets how long each synaptic contribution lasts. The input $g_i$ is in the model's input units; it is not specified as a measured membrane voltage.

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

This is still a jump process. [In the paper's [**weak fluctuation approximation**]{.definition-term custom-style="Definition Term"}, many individually small spike contributions produce only small changes in each neuron's total input. Their summed fluctuation can then be represented by Gaussian noise with the same leading mean and covariance:]{.definition-explanation}

$$
ds_i=F_i(\mathbf s)dt+\sqrt{r_i}\,dB_i,
\qquad
F_i(\mathbf s)=-s_i/\tau+\phi\!\left(\sum_jW_{ij}s_j+b_i\right),
$$

where the $B_i$ are independent standard Brownian processes. The noise coefficient has units $\mathrm{s}^{-1/2}$, so its product with $dB_i$ is a dimensionless activation increment. The Gaussian approximation is for small fluctuations in total input. It does not require each single neuron's entire spike train to look like a Gaussian process ([SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128)).[^p1-weak]

The supplement makes this limit concrete by replacing each population with $n$ equivalent neurons and dividing each connection weight by $n$. A summed input has a mean proportional to $n/n=1$, while its variance is proportional to $n/n^2=1/n$. Increasing population size therefore keeps the mean dynamics fixed and reduces input fluctuations. [For a ring network, a neuron's [**preferred angle**]{.definition-term custom-style="Definition Term"} is an angle where its tuning curve peaks.]{.definition-explanation} Increasing the density of equally spaced preferred angles and scaling weights as $1/N$ serves the same purpose. The paper's formulas give the leading terms in this large population limit, rather than exact finite network identities.[^p1-large]

Setting noise to zero gives the deterministic rate dynamics $\dot{\mathbf s}=\mathbf F(\mathbf s)$. A continuous attractor is a family of fixed points satisfying

$$
0=-\frac{\bar s_i(\theta)}{\tau}
+\phi[\bar g_i(\theta)],
\qquad
\bar s_i(\theta)=\tau\bar r_i(\theta).
$$

**Interpretation.** In the noise free dynamics, recurrent firing balances synaptic decay at each fixed point. The network must be tuned to possess this family. An arbitrary recurrent network will generally have isolated fixed points rather than a whole line or ring of them.

## The network's return flow determines the lasting memory change {#sec:MEMORY-LINEARIZATION}

**Neural mechanism.** A spike perturbs many aspects of a network's state. Most of those changes decay as the state returns to the attractor. [To calculate memory loss, we need the one change that survives: the displacement to a different fixed point. We assume a smooth continuous family with one neutral memory direction, while all other local modes decay. The disturbance must be small enough that the first order response describes the return flow.]{.key-statement}

**Mathematical derivation.** [A [**linearization**]{.definition-term custom-style="Definition Term"} keeps the terms proportional to a small perturbation and drops terms quadratic or higher in it.]{.definition-explanation} Here the network activation is $\mathbf s=\bar{\mathbf s}(\theta)+\delta\mathbf s$. Taylor expansion of the transfer function gives

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

The term $-\delta_{ij}/\tau$ removes a disturbance as synaptic activation fades. The term $\phi'(\bar g_i)W_{ij}$ describes recurrent renewal: the connection converts a change in cell $j$'s activation into input to cell $i$, and the local slope of the transfer function converts that input into a rate change. A steeper slope makes this response stronger. [Whether a disturbance decays, persists, or grows depends on the combined feedback through the whole network.]{.key-statement} A stronger connection alone does not establish better memory.

Moving a little along the fixed point family changes the activation by

$$
\delta\mathbf s\simeq\mathbf u\,\delta\theta,
\qquad u_i=\frac{d\bar s_i}{d\theta}=\tau\frac{d\bar r_i}{d\theta}.
$$

Differentiate the fixed point equation $\mathbf F[\bar{\mathbf s}(\theta)]=0$. The chain rule gives

$$
K\mathbf u=0.
$$

[Thus $\mathbf u$ is a [**right zero eigenvector**]{.definition-term custom-style="Definition Term"}: a state direction that the linear dynamics neither restores nor amplifies.]{.definition-explanation} It is the tangent to the attractor. The other modes must decay for this local family to be attracting.

[We also need a [**left zero eigenvector**]{.definition-term custom-style="Definition Term"}, a vector $\mathbf v$ satisfying]{.definition-explanation}

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

**Interpretation.** This generally differs from a perpendicular geometric projection. Decay can be tilted relative to the tangent. Even symmetric synaptic weights do not usually make $K$ symmetric, because $\phi'(\bar g_i)$ multiplies different rows by different amounts.

<div class="publisher-worked-calculation publisher-fold-always">

**Example: a disturbance that slides while it decays.**

To see the distinction without a neural simulation, consider the local system

$$
\dot x=ay,\qquad \dot y=-\lambda y,\quad\lambda>0.
$$

Every point with $y=0$ is fixed. Starting from $(x_0,y_0)$ gives $y(t)=y_0e^{-\lambda t}$ and

$$
x(\infty)=x_0+\frac{a}{\lambda}y_0.
$$

Here $\mathbf u=(1,0)^T$ and $\mathbf v=(1,a/\lambda)^T$. A vertical perturbation changes the final memory whenever $a\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper.

<div class="figure-scroll">

{{block:fig:MEMORY-TILTED-DECAY}}

</div>

As y decays, x changes by one; the left vector extracts that lasting shift.

</div>

## Projecting spike fluctuations gives the diffusion coefficient {#sec:MEMORY-DIFFUSION}

**Neural mechanism.** We can now calculate how much random displacement remains after the stable components have relaxed. [Each cell's random spikes disturb its outgoing synaptic activation; the circuit's return flow determines the lasting shift in memory.]{.key-statement} This calculation uses the weak noise and conditional independence assumptions, with rates and return flow evaluated near one fixed point.

**Mathematical derivation.** The variance of a linear combination of independent noise increments is the sum of their variances multiplied by squared weights. Here the weights are the components of $\mathbf v$: multiply the linear stochastic equation by $\mathbf v^T$. Since $\mathbf v^TK=0$,

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

For several memory coordinates $\theta_\alpha$, choose tangent vectors $u_i^\alpha=\partial\bar s_i/\partial\theta_\alpha$ and left vectors with $\sum_i v_i^\alpha u_i^\beta=\delta_{\alpha\beta}$. The same covariance calculation gives

$$
2D_{\alpha\beta}=\sum_i v_i^\alpha\bar r_i v_i^\beta.
$$

**Interpretation.** For one memory coordinate, each neuron's contribution combines its spike variability, $\bar r_i$, with the squared effect of one activation fluctuation on the final memory, $v_i^2$. The formula does not say that neurons with high rates necessarily damage memory more: changing rates can also change the tuning curves and the projection weights. Those changes must be included in a comparison.[^p1-projection]

The result is local in state and leading order in weak noise. The time interval must satisfy two conditions:

- It must be long enough for the approximation based on many spike contributions to apply.
- It must be short enough that the coefficients do not change substantially as the memory moves.

These conditions justify a local spreading rate. Systematic drift requires a [separate check in the next chapter](ch-memory-long-delays.html#sec-memory-drift-scope).

[The [**diffusion tensor**]{.definition-term custom-style="Definition Term"} is the matrix of displacement covariances per twice the elapsed time.]{.definition-explanation} Its diagonal entries describe spreading in individual coordinates; its other entries describe how coordinate displacements vary together. Even independently generated spike-count fluctuations can generate coupled motion of the represented coordinates.[^p1-multid]

## Symmetric weights express diffusion through tuning curves {#sec:MEMORY-SYMMETRIC}

**Neural mechanism.** The general formula requires the left vector of the network dynamics. [When $W_{ij}=W_{ji}$, can we express it through the tuning curves and neural transfer function?]{.key-statement} Symmetric connections make each cell affect another cell's input with the same weight that it receives in return, while their firing responses can still differ. We retain the common synaptic time constant, a stable continuous family, and the weak noise and conditional independence assumptions.

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

**Interpretation.** The input slopes $g_i'$ now determine the projection weights, so the diffusion coefficient can be calculated from the tuning curves and transfer function. This follows from [SI Eq. S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,239), with $\bar g_i=\phi^{-1}(\bar r_i)$ wherever the transfer function is invertible over the relevant range. The supplied Early Edition [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88) appears to omit the square on $g_i'$ in the numerator; the projection calculation and SI S18 give the squared expression shown here. This is an independent source check, not an author-confirmed correction. The result requires:

- symmetric weights;
- a stable continuous family;
- the noise assumptions already introduced.

The result does not require translation symmetry, in which shifting an activity pattern along the represented coordinate leaves the network dynamics unchanged in form.[^p1-symmetric]

<div class="publisher-worked-calculation publisher-fold-always">

**Example: opposite firing changes with constant diffusion.**

Take two mutually inhibiting cells with $W_{12}=W_{21}=-1$, zero self weights, equal biases $b$, and $\phi(g)=g/\tau$ over the positive input range. Its fixed points obey

$$
\bar s_1=\frac{b+\theta}{2},\qquad
\bar s_2=\frac{b-\theta}{2},\qquad |\theta|<b.
$$

The coordinate is $\theta=s_1-s_2$. The sum $s_1+s_2$ relaxes to $b$, while the difference is neutral. Here $\mathbf u=(1/2,-1/2)^T$, $\mathbf v=(1,-1)^T$, and

$$
2D=\bar r_1+\bar r_2=b/\tau.
$$

Although the two firing rates change with the stored value, their summed spike variability is constant. Therefore this network has constant local diffusion throughout its valid range. Near an endpoint, a negative linear rate would be impossible; a physical implementation must alter the transfer rule, and the interior formula alone does not describe that boundary. This model underlies the mutual inhibition example in [Fig. 2E–G, p. 3](ch-memory-long-delays.html#fig-paper-memory-2).[^p1-two]

The plot uses $b=20$ activation units and $\tau=0.1\,\mathrm{s}$.

<div class="figure-scroll">

{{block:fig:MEMORY-INHIBITION-RATES}}

</div>

The dashed rate sum in the upper plot stays fixed, so the lower plot has the same $D$ at every interior value of $\theta$.

</div>

[^p1-model]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. Proceedings of the National Academy of Sciences, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). [Main Eq. 1 and the steady state, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,60); [Model, Eqs. 7–9, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,372).

[^p1-weak]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650. [DOI](https://doi.org/10.1073/pnas.1117386109). [Weak Fluctuations, Eqs. 10–11, p. 5](../papers/burak-fiete-2012-persistent-activity.pdf#page=5&zoom=125,0,550), [continuation, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22); [SI Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128). Brownian increment notation is a teaching rewrite of the paper's white noise notation.

[^p1-large]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S1, p. 1](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=1&zoom=125,0,548); [Eqs. S2–S5, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,128); [ring population limit, Eq. S6, p. 2](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=2&zoom=125,0,539). [DOI](https://doi.org/10.1073/pnas.1117386109).

[^p1-projection]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text, p. 3: [linearization, Eqs. S7–S10](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,82); [tangent, Eq. S11](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,328); [left vector, Eqs. S12–S13](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,409); [projected diffusion, Eqs. S14–S15](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=3&zoom=125,0,576). [DOI](https://doi.org/10.1073/pnas.1117386109). The left vector interpretation is expanded here for teaching.

[^p1-multid]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*, Supporting Text: [Eq. S21, p. 5](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=5&zoom=125,0,592); [Eqs. S22–S27, p. 6](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=6&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109).

[^p1-symmetric]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [main Eq. 2, p. 2](../papers/burak-fiete-2012-persistent-activity.pdf#page=2&zoom=125,0,88); [Supporting Text, Eqs. S16–S18, p. 4](../papers/burak-fiete-2012-persistent-activity-si.pdf#page=4&zoom=125,0,48). [DOI](https://doi.org/10.1073/pnas.1117386109).

[^p1-two]: Burak, Y., & Fiete, I. R. (2012). *Fundamental limits on persistent activity in networks of noisy neurons*. PNAS, 109(43), 17645–17650, [Fig. 2E–G and caption, p. 3](../papers/burak-fiete-2012-persistent-activity.pdf#page=3&zoom=125,0,205); [Network Simulations, mutual inhibition, p. 6](../papers/burak-fiete-2012-persistent-activity.pdf#page=6&zoom=125,0,22). [DOI](https://doi.org/10.1073/pnas.1117386109). The activation coordinate is made explicit here to avoid confusing it with a rate difference, which rescales $D$ by $1/\tau^2$.
