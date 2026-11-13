"""Exact guide constructions for V02, V03A and V03B.

Run from any folder. Coordinates and curves are mathematical, not paper data.
The saved checks are computed evidence, not independent figure acceptance.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from figure_style import (INK, TEXT, MUTED, TEAL, FLOW, ORANGE, LINE,
                          PALE, PALE_TEAL, WARM, save, setup)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def arrow(ax, start, end, color=FLOW, **kwargs):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='-|>', color=color, lw=2,
                                mutation_scale=14, shrinkA=0, shrinkB=0,
                                **kwargs))


def v02():
    fig, ax = plt.subplots(figsize=(8, 5.1))
    fig.subplots_adjust(left=.09, right=.97, bottom=.20, top=.93)
    ax.set(xlim=(-.9, 2.15), ylim=(-.69, 2.60))
    ax.axis('off')
    ax.plot([-.72, 2.02], [0, 0], color=INK, lw=2.4)
    ax.text(1.76, -.15, r'fixed points: $y=0$', ha='center', va='top')
    # x0=0, y0=2, lambda=1 and a=1/2 in dimensionless coordinates.
    ts = np.arange(0,4.01,.5)
    y = 2*np.exp(-ts)
    x = 1-y/2
    ax.plot(np.r_[x,1], np.r_[y,0], color=TEAL, lw=2.8, zorder=2)
    for t0, t1 in [(.2, .55), (1.2, 1.65)]:
        arrow(ax, (1-np.exp(-t0), 2*np.exp(-t0)),
              (1-np.exp(-t1), 2*np.exp(-t1)), color=TEAL)
    ax.scatter(x, y, s=27, facecolor=WARM, edgecolor=TEAL, zorder=4)
    # The geometric projection shares the vertical line with the imposed jump.
    ax.plot([0, 0], [0, 2], color=LINE, lw=1.1, ls=':', zorder=0)
    arrow(ax, (0, .06), (0, 1.92), color=ORANGE, linestyle='--')
    ax.add_patch(Rectangle((0, 0), .075, .075, fill=False, ec=LINE, lw=1.1))
    ax.scatter([0], [0], s=47, color=INK, zorder=6)
    ax.scatter([1], [0], s=53, color=TEAL, zorder=6)
    ax.text(-.08, 2.13, r'$(x_0,y_0)=(0,2)$', ha='right')
    ax.text(-.13, 1.08, 'imposed\njump', color=ORANGE, ha='right', va='center')
    ax.text(.61, 1.84, 'flow after the jump', color=TEAL)
    for time,label,pos in [(.5,r'$\lambda t=0.5$',(.74,1.49)),
                            (1,r'$1$',(.91,.91)),(2,r'$2$',(1.10,.48))]:
        ax.annotate(label,xy=(1-np.exp(-time),2*np.exp(-time)),
                    xytext=pos,color=TEAL,
                    arrowprops=dict(arrowstyle='-',color=LINE,lw=.8))
    for time in [3,4]:
        ax.plot([1-np.exp(-time),1.09],[2*np.exp(-time),.15],color=LINE,lw=.8)
    ax.text(1.12, .15, r'$3,4$', color=TEAL)
    ax.text(.02, -.16, 'start: $(0,0)$', ha='center', va='top')
    ax.annotate('perpendicular foot:\nnot the dynamical endpoint', xy=(0, 0),
                xytext=(-.72, -.50), color=MUTED, fontsize=10,
                arrowprops=dict(arrowstyle='-', color=LINE), va='top')
    ax.annotate('endpoint: $(1,0)$', xy=(1, 0), xytext=(1.45, -.46),
                ha='center', va='top', color=TEAL,
                arrowprops=dict(arrowstyle='-', color=TEAL))
    # A tangent is a direction; the left vector is instead shown as a measurement.
    arrow(ax, (1.42, .16), (1.94, .16), color=INK)
    ax.text(1.68, .30, r'$\mathbf{u}=(1,0)$', ha='center', fontsize=10.5)
    fig.text(.10, .085, r'$a/\lambda=1/2$     Lasting shift: $\mathbf{v}^T\delta\mathbf{s}=\delta x+\frac{1}{2}\delta y=1$',
             fontsize=12)
    fig.text(.10, .025, 'The left vector measures displacement; it is not a path.',
             fontsize=10.5, color=MUTED)
    K = np.array([[0, .5], [0, -1.]])
    u, v = np.array([1.,0]), np.array([1.,.5])
    values = np.column_stack([x,y])
    checks = {
        'trajectory_satisfies_straight_relation': bool(np.allclose(x, 1-y/2)),
        'exact_solution_derivative_matches_ode': bool(np.allclose(np.column_stack([.5*y,-y]), values@K.T)),
        'left_vector_annihilates_dynamics': bool(np.allclose(v@K, 0)),
        'right_vector_is_neutral': bool(np.allclose(K@u, 0)),
        'left_right_normalization_one': bool(np.isclose(v@u, 1)),
        'lasting_coordinate_constant': bool(np.allclose(values@v, 1)),
        'all_time_marks_half_time_unit_apart': bool(np.allclose(np.diff(ts),.5)),
        'equal_half_time_steps_crowd_toward_endpoint': bool(np.all(np.diff(np.linalg.norm(np.diff(values,axis=0),axis=1)) < 0)),
    }
    return save(fig, 'V02', checks, {
        'coordinate_status': 'Dimensionless original guide example, not paper network data.',
        'parameters': {'x0':0, 'y0':2, 'lambda':1, 'a':.5},
        'sample_times_lambda_t':ts.tolist(),
        'sample_coordinates':values.tolist(),
        'endpoint':[1,0], 'perpendicular_foot':[0,0],
        'placement':'sec:MEMORY-LINEARIZATION',
    })


def v03a():
    fig, ax = plt.subplots(figsize=(8, 4.9))
    fig.subplots_adjust(left=.10, right=.91, bottom=.24, top=.94)
    ax.set(xlim=(-.25,10.9), ylim=(-.8,2.4))
    ax.spines[['top','right','left','bottom']].set_visible(False)
    ax.set_xticks([]); ax.set_yticks([])
    # An explicit illustrative path, with no claim to sampled Brownian statistics.
    t=np.array([0,.25,.55,.85,1.1,1.4,1.7,2.,2.3,2.6,2.9,3.2,3.5,3.8,4.1,4.4,4.7,5.,5.3,5.6,6.,6.3,6.6,6.9,7.2,7.5,7.8,8.1,8.4,8.7,9.,9.3,9.6,10.])
    y=np.array([0,.11,-.04,.18,.14,.38,.26,.34,.55,.45,.73,.61,.67,.81,.69,.94,.78,.91,.83,1.04,.9,1.08,.96,1.20,1.11,1.38,1.26,1.43,1.34,1.54,1.37,1.55,1.46,1.64])
    ax.axvspan(6,10,facecolor=PALE_TEAL,alpha=.7,zorder=0)
    ax.plot(t,y,color=TEAL,lw=2.1)
    ax.hlines(0,0,10.3,color=LINE,lw=1.2,linestyle=':')
    ax.hlines(.9,6,10.3,color=LINE,lw=1.2,linestyle=':')
    ax.vlines([0,6,10],-.56,2.02,color=LINE,lw=1,linestyle=':')
    ax.scatter([0,6],[0,.9],color=INK,s=45,zorder=5)
    ax.scatter([10],[1.25],color=ORANGE,marker='D',s=52,zorder=5)
    ax.text(.05,.47,r'original value $\Theta$',color=INK)
    ax.annotate(r'cue state $x=\theta(T)$',xy=(6,.9),xytext=(4.1,1.62),
                ha='center',color=INK,arrowprops=dict(arrowstyle='-',color=INK))
    ax.annotate(r'estimate $\widehat{x}$ of the cue state',xy=(10,1.25),
                xytext=(8.75,2.12),ha='center',color=ORANGE,
                arrowprops=dict(arrowstyle='-',color=ORANGE))
    ax.text(2.45,1.13,'one possible path',color=TEAL,fontsize=10.5)
    # Signed displacements use a pair of endpoint brackets, not time arrows.
    ax.annotate('',xy=(5.7,.9),xytext=(5.7,0),
                arrowprops=dict(arrowstyle='|-|',color=INK,lw=1.5))
    ax.text(5.44,.42,r'$s=x-\Theta$',ha='right',va='center',color=INK)
    ax.annotate('',xy=(10.4,1.25),xytext=(10.4,.9),
                arrowprops=dict(arrowstyle='|-|',color=ORANGE,lw=1.5))
    ax.text(10.57,1.075,r'$e=\widehat{x}-x$',ha='left',va='center',
            color=ORANGE,fontsize=10.5)
    arrow(ax,(0,-.52),(10.5,-.52),color=INK)
    for xpos,label in [(0,'0\nencoding'),(6,'$T$\nrecall cue'),(10,'$T+L$\nend of observation')]:
        ax.text(xpos,-.65,label,ha='center',va='top',fontsize=10.5)
    ax.text(2.9,-.35,'storage',ha='center',color=INK)
    ax.text(8,-.35,'later spikes used for readout',ha='center',color=TEAL,fontsize=10.5)
    fig.text(.10,.115,r'$V_{\mathrm{total}}=2DT+V_{\mathrm{read}}(L)$',fontsize=13)
    fig.text(.10,.063,'Constant D, no drift or boundaries; translation invariant readout.',fontsize=10)
    fig.text(.10,.020,'Locally unbiased readout and future noise independent of storage give Cov(s, e) = 0.',fontsize=9.5)
    return save(fig,'V03A',{
        'timeline_strictly_ordered':bool(0<6<10),
        'path_starts_at_original_value':bool(y[0]==0),
        'path_at_cue_equals_defined_x':bool(y[np.where(t==6)[0][0]]==.9),
        'displayed_errors_sum_to_total':bool(np.isclose((.9-0)+(1.25-.9),1.25-0)),
        'estimate_is_distinct_from_end_state':bool(not np.isclose(1.25,y[-1])),
    },{
        'trajectory_status':'Manually constructed illustrative path, not paper data or a Brownian simulation.',
        'times':{'encoding':0,'cue':6,'observation_end':10},
        'states':{'Theta':0,'cue_x':.9,'estimate_xhat':1.25,'end_state':float(y[-1])},
        'no_estimator_weight_kernel_implied':True,
        'placement':'sec:MEMORY-READOUT-SETUP',
    })


def v03b():
    fig,ax=plt.subplots(figsize=(8,4.9))
    fig.subplots_adjust(left=.13,right=.96,bottom=.18,top=.93)
    z=np.linspace(.3,7.2,1200)
    ideal=1/np.tanh(z)
    naive=z/3+1/z
    ax.set(xlim=(0,7.2),ylim=(.78,3.6))
    setup(ax,r'observation duration $z=L\sqrt{2DJ}$',
          r'readout variance $V_{\mathrm{read}}/\sqrt{2D/J}$')
    ax.axhline(1,color=LINE,ls=':',lw=1.5)
    ax.axvline(np.sqrt(3),color=LINE,ls=':',lw=1.3,ymax=.53)
    ax.plot(z,naive,color=ORANGE,ls='--',lw=2.5)
    ax.plot(z,ideal,color=TEAL,lw=2.7)
    ax.scatter([np.sqrt(3)],[2/np.sqrt(3)],color=ORANGE,zorder=5,s=45)
    ax.text(4.65,2.42,'simple averaging',color=ORANGE)
    ax.annotate('',xy=(np.sqrt(3),2/np.sqrt(3)),xytext=(2.65,1.94),
                arrowprops=dict(arrowstyle='-',color=ORANGE))
    ax.text(2.8,2.15,'minimum',color=ORANGE)
    ax.text(2.8,1.91,r'$(\sqrt{3},\;2/\sqrt{3})$',color=ORANGE)
    ax.text(5.3,1.15,'ideal readout',color=TEAL)
    ax.annotate(r'both diverge as $z\to0$',xy=(.32,3.36),xytext=(1.20,3.20),
                color=MUTED,fontsize=10.5,
                arrowprops=dict(arrowstyle='-',color=LINE))
    ax.text(6.5,.91,'limit: 1',color=MUTED,fontsize=10)
    ax.set_xticks(range(0,8)); ax.set_yticks([1,1.5,2,2.5,3,3.5])
    # Analytic derivative and an independent dense positive-grid comparison.
    root=np.sqrt(3)
    g=np.geomspace(1e-3,30,10000)
    difference=(g/3+1/g)-1/np.tanh(g)
    return save(fig,'V03B',{
        'ideal_at_or_above_one':bool(np.all(ideal>=1)),
        'ideal_below_averaging_on_dense_positive_grid':bool(np.all(difference>=-1e-10)),
        'averaging_derivative_zero_at_sqrt3':bool(np.isclose(1/3-1/root**2,0)),
        'averaging_second_derivative_positive_at_minimum':bool(2/root**3>0),
        'averaging_minimum_equals_2_over_sqrt3':bool(np.isclose(root/3+1/root,2/root)),
        'ideal_monotonic_decrease':bool(np.all(np.diff(ideal)<0)),
        'averaging_rises_after_minimum':bool(np.all(np.diff(naive[z>root])>0)),
        'plotted_domain_is_strictly_positive':bool(z.min()>0),
        'dimensionless_normalization_matches_original_ideal':bool(np.allclose(np.sqrt(.02/4)/np.tanh(np.sqrt(.02*4)*(z/np.sqrt(.02*4)))/np.sqrt(.02/4),ideal)),
        'dimensionless_normalization_matches_original_averaging':bool(np.allclose((.02*(z/np.sqrt(.02*4))/3+1/(4*(z/np.sqrt(.02*4))))/np.sqrt(.02/4),naive)),
    },{
        'curve_status':'Analytic reconstruction, not digitized data.',
        'ideal_formula':'coth(z)', 'averaging_formula':'z/3+1/z',
        'x_range':[float(z.min()),float(z.max())],
        'minimum':[float(root),float(2/root)],
        'storage_term_included':False,
        'minimum_dense_grid_averaging_minus_ideal':float(difference.min()),
        'source':'Burak and Fiete 2012 Fig. 3; SI S75 and S79-S81.',
        'placement':'sec:MEMORY-FIG3-AND-CAUTION',
    })


def integration():
    base='candidate-content/visuals/candidates/20261023'
    records=[
        dict(id='V02',visual_id='fig:MEMORY-TILTED-DECAY',
             chapter='content/chapters/02-memory-dynamics.md',
             placement_section='sec:MEMORY-LINEARIZATION',
             insert_after='Here $\\mathbf u=(1,0)^T$ and $\\mathbf v=(1,a/\\lambda)^T$. A vertical perturbation changes the final memory whenever $a\\ne0$. A perpendicular projection would miss that change. This is a teaching example of the projection geometry, not an additional network used in the paper.',
             intro='The exact trajectory in this example shows why the lasting displacement follows the flow rather than a perpendicular projection.',
             caption='Original guide construction of the tilted decay example, with dimensionless coordinates and $a/\\lambda=1/2$. The imposed jump from $(0,0)$ to $(0,2)$ relaxes toward $(1,0)$, while successive time marks crowd toward the endpoint. This illustrates the left and right zero vector construction in Burak and Fiete (2012), Supporting Text, Section II, pp. 3–4, Eqs. S10–S16; it is not a paper network simulation.',
             alt='A line of fixed points lies at y equals zero. An imposed vertical jump from zero zero to zero two is followed by a straight tilted flow toward one zero. Equal time marks crowd toward the endpoint. Perpendicular projection would return to zero zero and miss the lasting shift of one. The tangent is one zero; the left vector measures delta x plus one half delta y.',
             interpretation='The decaying part disappears, but its motion along the fixed point line leaves a shift of one; the left vector extracts that lasting shift.'),
        dict(id='V03A',visual_id='fig:MEMORY-READOUT-TIMELINE',
             chapter='content/chapters/03-memory-information.md',
             placement_section='sec:MEMORY-READOUT-SETUP',
             insert_after='The first term comes from storage. The second concerns estimation of $\\theta(T)$ from spikes after $T$. The supplement derives this decomposition for a locally translation invariant diffusion and readout model; state dependence, boundaries, informative priors, or uncertain initial encoding require corresponding changes.[^p1-read-setup]',
             intro='A timeline separates the displacement accumulated before the cue from the error in estimating the cue state afterward.',
             caption='Original guide construction of storage and cue state readout, based on Burak and Fiete (2012), Supporting Text, p. 12, Eq. S57. The illustrated path is one possible construction, and the orange estimate concerns the state at the cue rather than the state at the end of observation. With the conditions shown, storage and readout variances add because their cross covariance is zero.',
             alt='The stored value starts at Theta at encoding time zero and wanders until the recall cue at T. Its cue value is x. Later spikes, collected through T plus L, give an estimate x hat of that cue state. Storage error is x minus Theta; readout error is x hat minus x. The estimate is drawn separately from the path endpoint. Under the listed independence, unbiasedness and translation assumptions, total variance is two D T plus readout variance.',
             interpretation='Later spikes can improve the estimate of $x=\\theta(T)$; they do not reveal the particular storage displacements that separated $x$ from $\\Theta$.'),
        dict(id='V03B',visual_id='fig:MEMORY-READOUT-CURVES',
             chapter='content/chapters/03-memory-information.md',
             placement_section='sec:MEMORY-FIG3-AND-CAUTION',
             insert_after='Figure 3 isolates readout uncertainty, rescaling variance by $\\sqrt{2D/J}$ and duration by $L^*$. In these axes the ideal curve is $\\coth z$ and the naive curve is $z/3+1/z$. Both diverge like $1/z$ at short durations because too few spikes are available. The ideal solid curve approaches one. The naive dashed curve reaches $2/\\sqrt3$ at $z=\\sqrt3$, then rises because its equal weighting gives increasing importance to displaced states. The dotted vertical line marks that naive optimum. The storage delay contribution $2DT$ is not part of these rescaled curves. Figure S2 repeats the comparison for partial access, showing the rightward and upward shifts when $\\alpha=0.1$.[^p1-fig3]',
             intro='The normalized curves make the eventual cost of equal weighting visible.',
             caption='Original guide construction from the analytic readout formulas in Burak and Fiete (2012), Fig. 3 and Supporting Text, Eqs. S75 and S79–S81, rather than digitized data. Ideal readout approaches a normalized variance of one; simple averaging reaches $2/\\sqrt3$ at $z=\\sqrt3$ and then worsens. These curves contain no storage variance $2DT$.',
             alt='Readout variance divided by square root of two D over J is plotted against z equals L times square root of two D J. Both curves diverge as z approaches zero. Ideal readout coth z falls toward one. Simple averaging z over three plus one over z reaches its minimum at square root of three, two over square root of three, and then rises. The storage variance is absent.',
             interpretation='More observation keeps helping the ideal reader, with diminishing benefit, while equal weighting eventually gives too much influence to a state that has moved.'),
    ]
    for r in records:
        folder=f'{base}/{r["id"]}'
        r.update(candidate_svg=f'{folder}/figure.svg',candidate_png=f'{folder}/figure.png',
                 book_width_preview=f'{folder}/book-width.png',qa=f'{folder}/qa.json',
                 editable_source='verification/illustrations/draw_memory.py',
                 acceptance='pending independent review')
    (HERE/'memory-integration.json').write_text(json.dumps(records,indent=2,ensure_ascii=False),encoding='utf-8')


if __name__=='__main__':
    results=[v02(),v03a(),v03b()]
    integration()
    print(json.dumps([{k:r[k] for k in ['asset_id','status','checks','text_outside_canvas']} for r in results],indent=2))
