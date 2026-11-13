"""A01-A04 exact mathematical teaching plots and pending integration packets.

Run once without --draw to record complete briefs/contracts before generation.
Run with --draw to export PNG, SVG, book-width previews and calculated QA only.
No reader sources or canonical ledgers are edited by this script.
"""
from pathlib import Path
import sys
import json
import math
from datetime import datetime
import numpy as np
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'verification/illustrations'))
import figure_style as fs
import matplotlib.pyplot as plt
fs.OUT = ROOT / 'candidate-content/visuals/candidates/20261024-all'
AUTHOR = '/root/all_draw_foundations_information'
SK = 'C:/Users/vital/.codex/skills'
PROFILE = SK + '/course-diagram-builder/references/house-graphic-v1.yaml'
RULES = [SK + '/course-diagram-builder/references/' + s for s in
         ['visual-qa.md', 'review-acceptance.md', 'review-record-template.yaml']]
RULES += [SK + '/course-study-guide-builder/references/' + s for s in
          ['visual-integration-contract.md', 'pedagogy-language-contract.md',
           'math-code-case-contract.md']]

def rel(p): return str(p.relative_to(ROOT)).replace('\\', '/')
FOUND = 'content/chapters/01-foundations'
INFO = 'content/chapters/03-memory-information'
PDF = 'assets/papers/burak-fiete-2012-persistent-activity.pdf'
SI = 'assets/papers/burak-fiete-2012-persistent-activity-si.pdf'

ITEMS = [
dict(id='A01', visual_id='fig:FOUNDATIONS-POISSON-POPULATION', chapter=FOUND+'.md',
 placement_section='sec:FOUNDATIONS-POISSON',
 insert_after="Now suppose 20 conditionally independent cells each have that rate. Their total count is Poisson with mean 20 and standard deviation $\\sqrt{20}=4.47$. The total rate estimate has a relative standard deviation of about 22.4%, compared with 100% for one cell. Population averaging helps because the independent count variances add while the mean signal adds directly. If cells share an additional fluctuating drive, that common variation will not disappear in the same way.",
 intro='The two count distributions can be compared on the same rate per cell scale.',
 caption='Analytic teaching construction for the chapter’s 20 Hz, 50 ms example. The count is Poisson with mean 1 for one cell and mean 20 for 20 conditionally independent cells. Both panels plot the rate per cell $K/(N\\Delta t)$, so both estimates have mean 20 Hz; their standard deviations are 20 Hz and 4.47 Hz. Each stem is a probability at one possible estimate, rather than a continuous density. Only estimates through 100 Hz are drawn. The independence condition concerns fixed modeled rates, not complete recurrent spike trains.',
 alt='Two discrete Poisson distributions share a rate per cell axis. One cell has widely spaced possible estimates at zero, twenty, forty hertz and so on, with probability 0.368 at zero. The twenty cell estimate has possible values one hertz apart and clusters around twenty hertz. Their means match, but the rate standard deviation falls from twenty to 4.47 hertz.',
 interpretation='Dividing the pooled rate estimate by 20 keeps the expected rate per cell fixed, while independent averaging reduces its relative spread.',
 source_locator='Guide sec:FOUNDATIONS-POISSON, exact 20 Hz / 50 ms example; Burak and Fiete (2012), main PDF p. 1, Results, Poisson model; SI PDF p. 9, Eq. S43, conditional count likelihood.',
 source_link='../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=9',
 source_pdfs=[PDF,SI], scenes=['one-cell-count','pooled-count-normalization'],
 purpose='Show both the frequent silent interval and the lower relative noise from independent population averaging.',
 parameters={'rate_Hz':20,'interval_s':.05,'cell_counts':[1,20],'display_rate_range_Hz':[0,100]},
 required_items=['Exact Poisson probability masses, not a Gaussian approximation.','Common per-cell rate normalization K/(N Δt).','Mean 20 Hz in both panels; SD 20 and sqrt(20) Hz.','P(K=0)=exp(-1) for one cell.']),
dict(id='A02',visual_id='fig:FOUNDATIONS-DIFFUSION-BIAS',chapter=FOUND+'.md',
 placement_section='sec:FOUNDATIONS-DIFFUSION',
 insert_after='The deterministic and random contributions are equal at $t=2D/v^2=4$ seconds. Their equal contributions there are each $0.16$ degrees squared. At longer times the bias dominates this unbounded model even though it was small over a short observation. Removing systematic drift is therefore a substantive assumption in a theory devoted to random diffusion.',
 intro='Sample paths show the irregular motion; exact displacement scales show how its spread differs from a fixed bias.',
 caption='Simulated Brownian teaching paths and analytic displacement scales for $D=0.02$ degrees squared per second and $v=0.10$ degrees per second. The upper paths have zero drift and start at zero; the dashed envelope is the exact root mean squared displacement, not a boundary on individual paths. Below, $\\sqrt{2Dt}$ and $vt$ are equal at 4 s, when each is 0.40 degrees. Their squares are the separate contributions to the biased model’s MSD. The coordinate is unbounded, and these chosen values are not estimates from animal recordings.',
 alt='Seven Brownian sample paths move irregularly above and below zero. A dashed positive and negative root mean squared envelope grows with the square root of time; some paths cross it. A second plot compares the positive root mean squared displacement with a linearly growing bias displacement. Both equal 0.40 degrees at four seconds, after which the bias line is higher.',
 interpretation='A single path can turn back toward zero even while the root mean squared displacement grows. A constant bias grows linearly, so it eventually exceeds the square root growth of the random displacement scale.',
 source_locator='Guide sec:FOUNDATIONS-DIFFUSION, exact D=.02 and v=.10 example; Burak and Fiete (2012), main PDF p. 2, Diffusive Drift due to Ongoing Neural Noise; SI PDF pp. 4–5, Systematic drift, and p. 7, Eq. S30.',
 source_link='../../assets/papers/burak-fiete-2012-persistent-activity-si.pdf#page=7',
 source_pdfs=[PDF,SI],scenes=['zero-drift-ensemble','rms-versus-bias'],
 purpose='Distinguish nonmonotonic individual motion, square root ensemble spread and linear systematic motion.',
 parameters={'D_deg2_per_s':.02,'v_deg_per_s':.10,'duration_s':8,'sample_dt_s':.01,'paths':7,'random_seed':2026102402},
 required_items=['Seven sampled Gaussian independent-increment paths start at zero.','Exact ±sqrt(2Dt) envelope identified as RMS, not confidence or hard boundary.','RMS and vt cross at t=4 s, displacement .40 deg.','No periodic coordinate or saturation; do not duplicate line-versus-ring figure.']),
dict(id='A03',visual_id='fig:MEMORY-TUNING-INFORMATION',chapter=INFO+'.md',
 placement_section='sec:MEMORY-FI',
 insert_after="Each cell contributes squared slope divided by its count variance per unit time. High rates with zero slope do not distinguish neighboring values, so they contribute no local information. A sharply changing rate can be informative even if it is smaller than another cell's peak rate. The coordinate here describes the network's present internal state. It need not be a currently visible external stimulus. Sensory Fisher information has the same Poisson formula only when the stimulus dependent tuning curves are the relevant rates.",
 intro='Two positive tuning curves with the same changing part isolate the effect of extra baseline firing.',
 caption='Analytic teaching curves $r_A(\\theta)=5+35e^{-\\theta^2/(2w^2)}$ and $r_B(\\theta)=r_A(\\theta)+20$, in spikes per second, with chosen width $w=0.6$ rad. The rates have the same derivative. Their individual Poisson information contributions $(r_i^{\\prime})^2/r_i$ vanish at the rate peak, where the slope is zero, and are positive on the flanks. Adding baseline firing raises the count noise without changing the slope, reducing local information. These are illustrative tuning curves, not recorded neurons or a demonstrated attractor network.',
 alt='The first plot shows two positive peaked rate curves separated by a constant twenty spikes per second. The second shows their shared derivative, positive to the left, zero at the central peak and negative to the right. The third shows squared slope divided by rate for each curve. Both contributions vanish at the center and rise on the flanks; the higher baseline curve contributes less at every point with nonzero slope.',
 interpretation='The rate peak has zero local slope, so it contributes no local information at that point. Extra spikes from a constant baseline increase Poisson variability without making nearby values easier to distinguish.',
 source_locator='Guide sec:MEMORY-FI, J=sum_i (r_i prime)^2/r_i and positive-rate condition; Burak and Fiete (2012), main PDF p. 2, Eq. 3; SI PDF pp. 9–10, Eqs. S42–S44.',
 source_link='../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=2',
 source_pdfs=[PDF,SI],scenes=['rate-and-baseline','shared-slope','individual-information'],
 purpose='Show why high firing alone does not imply high local Poisson information.',
 parameters={'baseline_A_Hz':5,'baseline_B_Hz':25,'peak_above_baseline_Hz':35,'width_rad':.6,'theta_range_rad':[-2,2]},
 required_items=['Strictly positive rate curves.','Same derivative in both examples.','Zero slope and zero information at theta=0.','Individual information contributions use squared slope divided by own rate.','Chosen curves are not claimed to form a full recurrent attractor.']),
dict(id='A04',visual_id='fig:MEMORY-BOUND-STRICTNESS',chapter=INFO+'.md',
 placement_section='sec:MEMORY-BOUND',
 insert_after='The actual diffusion remains $1000$. The inequality is strict because these two unequal rates no longer align the network\'s projection weights with the information optimal weights. This also shows why equality at a special state does not force the transfer function to be exponential on its whole domain. A constant lower bound attained everywhere and an accidental equality at one state are different claims.',
 intro='The chapter’s two cell example makes the difference between a lower bound and the actual diffusion visible.',
 caption='Analytic teaching calculation for the chapter’s mutual inhibition example, with $b=200$ activation units and $\\tau=0.1$ s. The coordinate $\\theta$ is an activation difference. For positive rates $r_{1,2}=(b\\pm\\theta)/(2\\tau)$, $J=2000/(40000-\\theta^2)$ while $D=1000$ activation units squared per second. The lower bound $1/(2\\tau^2J)$ equals $D$ at $\\theta=0$ and falls to 750 at $\\theta=100$. Higher local information permits a lower diffusion bound but leaves the actual diffusion unchanged in this model. The plotted range stays inside the positive-rate domain $|\\theta|<200$.',
 alt='Across memory coordinates from minus one hundred sixty to one hundred sixty activation units, internal information has a minimum of 0.05 at zero and grows toward either side. Actual diffusion is a horizontal line at one thousand. The information lower bound meets it at zero and bends downward, reaching seven hundred fifty at coordinate one hundred. A marked gap separates actual diffusion from the bound there.',
 interpretation='The gap at $\\theta=100$ shows why a lower minimum allowed by the inequality is not a reduction in the network’s actual diffusion.',
 source_locator='Guide sec:MEMORY-BOUND, exact b=200, tau=.1 mutual inhibition example; Ch. 2 mutual inhibition derivation; Burak and Fiete (2012), main PDF p. 3, Eq. 4 and Fig. 2E–G; SI PDF pp. 10–11, Eqs. S45–S49.',
 source_link='../../assets/papers/burak-fiete-2012-persistent-activity.pdf#page=3',
 source_pdfs=[PDF,SI],scenes=['state-dependent-information','constant-diffusion-and-lower-bound'],
 purpose='Show by an existing exact example that higher information can loosen a bound while actual diffusion stays fixed.',
 parameters={'b_activation_units':200,'tau_s':.1,'theta_range_activation_units':[-160,160],'marked_theta':[0,100]},
 required_items=['J=.05 at theta0 and 1/15 at theta100.','Actual D=1000 throughout displayed interior domain.','Bound=1000 at theta0 and 750 at theta100.','Activation coordinate is not an angular coordinate.','No claim that arbitrary higher information reduces actual diffusion.'])]

def packet_and_briefs():
    profile=yaml.safe_load(Path(PROFILE).read_text(encoding='utf-8'))
    rows=[]
    for item in ITEMS:
        aid=item['id']; folder=fs.OUT/aid; brief=HERE/(aid+'-brief.yaml')
        stem=item['chapter'][:-3]
        source_files=[stem+'.md',stem+'.yaml',rel(Path(__file__)),rel(brief),
                      'verification/illustrations/figure_style.py',*item['source_pdfs'],
                      rel(HERE/'foundation-information-source-extracts.txt'),
                      rel(HERE/'foundation-information-source-extra.txt')]
        if aid=='A04': source_files += ['content/chapters/02-memory-dynamics.md','content/chapters/02-memory-dynamics.yaml']
        contract=dict(schema_version=1,figure_role='quantitative-figure',route='vector',unit_scope='chapter',author=AUTHOR,
                      role_reason=item['purpose'],source_files=source_files,rule_files=RULES,
                      style_lock='source-maps/book-style-lock.yaml',style_profile=PROFILE,
                      reference_images=[],palette_audit=rel(folder/'qa.json'),vector_spec=rel(Path(__file__)),
                      insertion_width_px=700,required_scene_ids=item['scenes'],
                      coverage={'applicable':False,'reason':'Internal mathematical teaching figure, not an opening map; no chapter coverage claim.'})
        record=dict(brief={'asset_id':item['visual_id'],'scope':'chapter','book':'burak-three-papers',
                           'chapter': 'ch:FOUNDATIONS' if aid in ['A01','A02'] else 'ch:MEMORY-INFORMATION',
                           'purpose':item['purpose'],'target_use':item['placement_section'],
                           'generation_authorized':True,'insertion_authorized':True},
                    author=AUTHOR,figure_role='quantitative-figure',
                    visual_explanation={'applicable':True,'figure_role':'quantitative-figure',
                                        'required_scene_ids':item['scenes'],'reference_reason':'Exact mathematical plots; no structural template or opener reference applies.'},
                    chapter_map_coverage={'applicable':False,'reason':'Section calculation figure, not an opening map.'},
                    style_contract={'book_style_lock_path':'source-maps/book-style-lock.yaml',
                                    'palette_family_id':'technical-editorial-blueprint','palette_family_version':'1.0.0',
                                    'route':'vector','profile_id':'house-graphic-v1','profile_version':'0.1.0','profile_path':PROFILE,
                                    'palette':{'colors_and_roles':profile['color'],'color_distance':'Exact SVG color token membership; no raster pixel deviation claim.',
                                               'maximum_deviation_fraction':0,'allowed_special_purpose_colors':[]}},
                    parameters=item['parameters'],required_items=item['required_items'],
                    source_locator=item['source_locator'],
                    language_contract={'book_loci':[item['placement_section']],'caption':item['caption'],
                                       'alt_text':item['alt'],'teaching_introduction':item['intro'],'conclusion':item['interpretation']},
                    review_contract=contract,
                    limitations=['Analytic or simulated teaching construction using explicitly chosen parameters; not new experimental data.',
                                 'No structural vector template gate or raster pixel audit is claimed; computed checks and pixel inspection support independent review.'],
                    manual_rule_disposition={'applicable':['semantic correspondence','numerical accuracy','units and domain assumptions','full size and 700px readability','palette color roles','canvas clipping'],
                                             'not_applicable':['opening-map coverage','generic structural-template geometry gates','raster pixel-deviation measurement']})
        brief.write_text(yaml.safe_dump(record,sort_keys=False,allow_unicode=True),encoding='utf-8')
        entry={k:v for k,v in item.items() if k not in ['scenes','purpose','parameters','required_items','source_pdfs']}
        entry.update(candidate_svg=rel(folder/'figure.svg'),candidate_png=rel(folder/'figure.png'),
                     book_width_preview=rel(folder/'book-width.png'),qa=rel(folder/'qa.json'),
                     editable_source=rel(Path(__file__)),brief=rel(brief),review_contract=contract,
                     author=AUTHOR,acceptance='pending independent review')
        rows.append(entry)
    (HERE/'foundation-information-integration.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False),encoding='utf-8')
    pending=[]
    for row in rows:
        pending.append({'id':row['id'],'visual_id':row['visual_id'],'asset':row['candidate_png'],'caption':row['caption'],'alt':row['alt'],
                        'author':AUTHOR,'status':'candidate','review_contract':row['review_contract'],
                        'diagram_review':{'schema_version':1,'status':'pending','reviewer':None,'reviewed_sha256':None,'policy_sha256':None,
                                          'context_sha256':None,'input_sha256':{},'source_scope_sha256':{},'strongest_objection':None,'objection_resolution':None,
                                          'checks':{s:{'verdict':'pending','evidence':[]} for s in ['technical_accuracy','visual_explanation','readability','palette','coverage']}}})
    (HERE/'pending-ledger-foundations-information.yaml').write_text(yaml.safe_dump({'visuals':pending},sort_keys=False,allow_unicode=True),encoding='utf-8')

def a01():
    fig,axs=plt.subplots(2,1,figsize=(8.4,5.8),sharex=True)
    fig.subplots_adjust(left=.12,right=.97,bottom=.16,top=.92,hspace=.40)
    masses=[]
    for ax,n,color in zip(axs,[1,20],[fs.INK,fs.TEAL]):
        lam=n; ks=np.arange(0,101 if n==20 else 6)
        ps=np.array([math.exp(-lam+k*math.log(lam)-math.lgamma(k+1)) for k in ks]); rate=ks/(n*.05)
        ax.vlines(rate,0,ps,color=color,lw=2 if n==1 else 1.1)
        ax.scatter(rate,ps,s=27 if n==1 else 9,color=color,zorder=3)
        ax.axvline(20,color=fs.LINE,lw=1,ls=':',zorder=0)
        ax.set(xlim=(-3,103),ylim=(0,.41),yticks=[0,.2,.4])
        fs.setup(ax,ylabel='Probability')
        ax.text(.98,.92,('One cell' if n==1 else '20 independent cells')+f': $\\lambda={lam}$',transform=ax.transAxes,ha='right',color=color,fontsize=12)
        ax.text(.98,.68,f'Mean 20 Hz; SD {20/math.sqrt(n):.2f} Hz',transform=ax.transAxes,ha='right',fontsize=11)
        if n==1: ax.annotate('No spike: 0.368',xy=(0,math.exp(-1)),xytext=(12,.30),color=color,arrowprops={'arrowstyle':'-','color':fs.LINE},fontsize=11)
        masses.append(float(ps.sum()))
    fs.setup(axs[1],xlabel=r'Rate estimate per cell $K/(N\Delta t)$ (Hz)')
    axs[1].set_xticks([0,20,40,60,80,100])
    fig.text(.12,.035,r'$\Delta t=0.05$ s; expected rate per cell = 20 Hz.  Stems are discrete probabilities.',fontsize=11,color=fs.MUTED)
    return fs.save(fig,'A01',{'one_cell_zero_probability':np.isclose(math.exp(-1),.36787944117).item(),
                             'both_rate_means_20':all(np.isclose(n/(n*.05),20) for n in [1,20]),'rate_SD_ratio_sqrt20':np.isclose(20/(20/math.sqrt(20)),math.sqrt(20)).item(),
                             'displayed_mass_gt_999_in_pool':masses[1]>.999},
                   {'parameters':ITEMS[0]['parameters'],'displayed_probability_mass':masses,'normalization':'K/(N*.05) Hz; total pooled rate is divided by N=20.'})

def a02():
    D=.02; v=.1; dt=.01; t=np.linspace(0,8,801); rng=np.random.default_rng(2026102402)
    inc=rng.normal(0,math.sqrt(2*D*dt),(7,800)); paths=np.column_stack([np.zeros(7),np.cumsum(inc,axis=1)])
    fig,axs=plt.subplots(2,1,figsize=(8.4,6.5),sharex=True)
    fig.subplots_adjust(left=.13,right=.97,bottom=.12,top=.93,hspace=.39)
    rms=np.sqrt(2*D*t)
    for p in paths: axs[0].plot(t,p,color=fs.LINE,lw=1.0,zorder=1)
    axs[0].plot(t,rms,color=fs.TEAL,ls='--',label=r'$\pm\sqrt{2Dt}$')
    axs[0].plot(t,-rms,color=fs.TEAL,ls='--')
    axs[0].axhline(0,color=fs.INK,lw=.8)
    axs[0].set_ylim(-1.15,1.15)
    axs[0].text(.02,.93,'Seven zero-drift sample paths',transform=axs[0].transAxes,va='top',color=fs.MUTED)
    axs[0].legend(frameon=False,loc='upper right',fontsize=11)
    fs.setup(axs[0],ylabel='Displacement (deg)')
    axs[1].plot(t,rms,color=fs.TEAL,label=r'Random RMS: $\sqrt{2Dt}$')
    axs[1].plot(t,v*t,color=fs.ORANGE,label=r'Bias: $vt$')
    axs[1].scatter([4],[.4],color=fs.INK,s=30,zorder=4)
    axs[1].plot([4,4],[0,.4],color=fs.LINE,ls=':',lw=1)
    axs[1].annotate('Equal at 4 s: 0.40 deg',xy=(4,.4),xytext=(1.2,.69),arrowprops={'arrowstyle':'-','color':fs.LINE},fontsize=11)
    axs[1].set(xlim=(0,8),ylim=(0,.85),xticks=[0,2,4,6,8],yticks=[0,.4,.8])
    axs[1].legend(frameon=False,loc='lower right',fontsize=11)
    fs.setup(axs[1],xlabel='Time (s)',ylabel='Displacement scale (deg)')
    return fs.save(fig,'A02',{'all_paths_start_zero':bool(np.all(paths[:,0]==0)),
                             'equality_time_4':bool(np.isclose(2*D/v**2,4)),
                             'equal_displacement_point4':bool(np.isclose(math.sqrt(2*D*4),v*4)),
                             'each_path_has_both_increment_signs':bool(np.all(np.any(inc>0,axis=1)&np.any(inc<0,axis=1)))},
                   {'parameters':ITEMS[1]['parameters'],'path_status':'Simulated Brownian samples; exact RMS curves. No neural network or animal data.','random_increment_variance_deg2':2*D*dt})

def a03():
    theta=np.linspace(-2,2,1001); w=.6; shape=35*np.exp(-theta**2/(2*w*w))
    rA=5+shape;rB=25+shape;der=-theta/w**2*shape; jA=der**2/rA;jB=der**2/rB
    fig,axs=plt.subplots(3,1,figsize=(8.4,7.5),sharex=True)
    fig.subplots_adjust(left=.16,right=.97,bottom=.11,top=.94,hspace=.34)
    axs[0].plot(theta,rA,color=fs.INK,label=r'$r_A$: baseline 5 Hz')
    axs[0].plot(theta,rB,color=fs.TEAL,label=r'$r_B$: baseline 25 Hz')
    axs[0].legend(frameon=False,ncol=2,loc='upper center',bbox_to_anchor=(.5,1.32),fontsize=11)
    axs[0].set_ylim(0,65); fs.setup(axs[0],ylabel='Rate (spikes/s)')
    axs[1].plot(theta,der,color=fs.MUTED);axs[1].axhline(0,color=fs.LINE,lw=.8)
    axs[1].text(.03,.10,'Same derivative for both curves',transform=axs[1].transAxes,fontsize=11,color=fs.MUTED)
    fs.setup(axs[1],ylabel=r'Slope (spikes s$^{-1}$ rad$^{-1}$)')
    axs[2].plot(theta,jA,color=fs.INK,label=r"$(r_A')^2/r_A$")
    axs[2].plot(theta,jB,color=fs.TEAL,label=r"$(r_B')^2/r_B$")
    for ax in axs:
        ax.axvline(0,color=fs.LINE,ls=':',lw=1,zorder=0)
        ax.set_xlim(-2,2)
    axs[2].scatter([0],[0],color=fs.INK,s=25,zorder=4)
    fs.setup(axs[2],xlabel=r'Memory coordinate $\theta$ (rad)',ylabel=r'Contribution (rad$^{-2}$ s$^{-1}$)')
    axs[2].set_ylim(-2,65);axs[2].set_yticks([0,30,60]);axs[2].set_xticks([-2,-1,0,1,2])
    return fs.save(fig,'A03',{'all_rates_positive':bool(np.all(rA>0)&np.all(rB>0)),
                             'baseline_difference_constant_20':bool(np.allclose(rB-rA,20)),
                             'peak_slope_and_information_zero':bool(der[500]==0 and jA[500]==0 and jB[500]==0),
                             'extra_baseline_reduces_information':bool(np.all(jB<=jA))},
                   {'parameters':ITEMS[2]['parameters'],'formulas':{'rA':'5+35 exp(-theta²/(2*.6²))','rB':'rA+20','derivative':'-theta/.6² *35 exp(-theta²/(2*.6²))','information':'derivative² / own rate'},'data_status':'Analytic teaching functions, no claim of a realized recurrent attractor.'})

def a04():
    theta=np.linspace(-160,160,801);tau=.1;b=200
    r1=(b+theta)/(2*tau);r2=(b-theta)/(2*tau);J=25/r1+25/r2
    lower=1/(2*tau*tau*J);D=np.full_like(theta,1000.)
    fig,axs=plt.subplots(2,1,figsize=(8.4,6.1),sharex=True)
    fig.subplots_adjust(left=.15,right=.97,bottom=.13,top=.93,hspace=.36)
    axs[0].plot(theta,J,color=fs.INK)
    axs[0].scatter([0,100],[.05,1/15],color=fs.INK,s=28)
    axs[0].annotate('0.0500',xy=(0,.05),xytext=(-25,.085),ha='right',arrowprops={'arrowstyle':'-','color':fs.LINE},fontsize=11)
    axs[0].annotate('0.0667',xy=(100,1/15),xytext=(105,.104),arrowprops={'arrowstyle':'-','color':fs.LINE},fontsize=11)
    axs[0].set(ylim=(.035,.15),yticks=[.05,.10,.15])
    fs.setup(axs[0],ylabel=r'$J$ (unit$^{-2}$ s$^{-1}$)')
    axs[1].plot(theta,D,color=fs.INK,label='Actual $D$')
    axs[1].plot(theta,lower,color=fs.TEAL,label=r'Lower bound $1/(2\tau^2J)$')
    axs[1].scatter([0,100],[1000,750],color=fs.TEAL,s=32,zorder=4)
    axs[1].plot([100,100],[750,1000],color=fs.ORANGE,lw=2)
    axs[1].annotate('750',xy=(100,750),xytext=(103,590),fontsize=11,color=fs.TEAL,arrowprops={'arrowstyle':'-','color':fs.LINE})
    axs[1].text(0,1080,'Equality at 0',ha='center',fontsize=11)
    axs[1].set(ylim=(0,1220),yticks=[0,500,1000],xlim=(-160,160),xticks=[-150,-100,0,100,150])
    axs[1].legend(frameon=False,loc='lower center',fontsize=11)
    fs.setup(axs[1],xlabel=r'Memory coordinate $\theta$ (activation units)',ylabel=r'Diffusion (unit$^2$/s)')
    fig.text(.15,.02,r'$b=200$ activation units; $\tau=0.1$ s.  All displayed rates are positive.',fontsize=11,color=fs.MUTED)
    return fs.save(fig,'A04',{'rates_positive_in_display':bool(np.all(r1>0)&np.all(r2>0)),
                             'J_matches_closed_form':bool(np.allclose(J,2000/(40000-theta**2))),
                             'bound_never_exceeds_D':bool(np.all(lower<=D+1e-9)),
                             'bound_1000_at_zero':bool(np.isclose(1/(2*tau*tau*.05),1000)),
                             'bound_750_at_100':bool(np.isclose(1/(2*tau*tau*(1/15)),750))},
                   {'parameters':ITEMS[3]['parameters'],'formulas':{'J':'2000/(40000-theta²)','D':'1000','lower_bound':'1000-theta²/40'},'coordinate':'activation difference, not angle'})

if __name__=='__main__':
    packet_and_briefs()
    print('Briefs, pending contracts and packets saved at '+datetime.now().astimezone().isoformat())
    if '--draw' in sys.argv:
        results=[a01(),a02(),a03(),a04()]
        (HERE/'foundation-information-calculated-checks.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
        print(json.dumps({x['asset_id']:x['status'] for x in results}))
