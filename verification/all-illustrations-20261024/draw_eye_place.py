"""A05-A08: exact scientific plots for existing chapter equations.

Author /root/all_draw_eye_place. Root start 2026-10-24T18:31:14.999410+03:00.
Run --prepare before drawing to persist briefs and pending review contracts.
"""
from pathlib import Path
import sys
import json
from datetime import datetime
import numpy as np
import yaml
from scipy.integrate import quad
from scipy.special import gamma

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT/'verification/illustrations'))
import figure_style as style
from figure_style import plt, INK, TEAL, ORANGE, MUTED, LINE, PALE_TEAL, PALE_ORANGE, setup

style.OUT = ROOT/'candidate-content/visuals/candidates/20261024-all'
AUTHOR='/root/all_draw_eye_place'
SCRIPT='verification/all-illustrations-20261024/draw_eye_place.py'
TASK='verification/all-illustrations-20261024'
PROFILE='C:/Users/vital/.codex/skills/course-diagram-builder/references/house-graphic-v1.yaml'
RULES=[
 'C:/Users/vital/.codex/skills/course-diagram-builder/references/visual-qa.md',
 'C:/Users/vital/.codex/skills/course-diagram-builder/references/review-acceptance.md',
 'C:/Users/vital/.codex/skills/course-study-guide-builder/references/visual-integration-contract.md',
 'C:/Users/vital/.codex/skills/course-study-guide-builder/references/pedagogy-language-contract.md']

def packet(id, visual, stem, section, anchor, intro, caption, alt, interpretation, source, pdf, page, scenes, params):
    candidate=f'candidate-content/visuals/candidates/20261024-all/{id}'
    brief=f'{TASK}/{id}-brief.yaml'
    chapter=f'content/chapters/{stem}.md'
    contract=dict(schema_version=1,figure_role='quantitative-figure',route='vector',unit_scope='chapter',author=AUTHOR,
        role_reason='Internal mathematical detail figure using calculated curves, not an opening map or experimental plot.',
        source_files=[chapter,f'content/chapters/{stem}.yaml',SCRIPT,brief,'verification/illustrations/figure_style.py',pdf],
        rule_files=RULES,style_lock='source-maps/book-style-lock.yaml',style_profile=PROFILE,reference_images=[],
        palette_audit=f'{candidate}/qa.json',vector_spec=SCRIPT,insertion_width_px=700,required_scene_ids=scenes,
        coverage=dict(applicable=False,reason='Internal explanation of specific equations; no chapter-opening coverage claim.'))
    return dict(id=id,visual_id=visual,stem=stem,chapter_path=chapter,placement=section,section_id=section,anchor=anchor,insert_after=anchor,
        intro=intro,caption=caption,alt=alt,interpretation=interpretation,source_locator=source,
        source_link=f'../../{pdf}#page={page}',source_pdf=pdf,candidate=candidate,
        paths=dict(svg=f'{candidate}/figure.svg',png=f'{candidate}/figure.png',book_width=f'{candidate}/book-width.png',qa=f'{candidate}/qa.json'),
        author=AUTHOR,spec=SCRIPT,generator=SCRIPT,brief=brief,insertion_width_px=700,review_status='pending independent review',
        review_contract=contract,guide_only_parameters=params,root_task_started_at='2026-10-24T18:31:14.999410+03:00',awake_execution_time='unverified')

def packets():
    eye='assets/papers/ben-shushan-2022-fixational-drift.pdf'
    place='assets/papers/mainali-2025-universal-statistics.pdf'
    p=[]
    p.append(packet('A05','fig:EYE-SHARED-PRIVATE-VARIANCE','04-eye-drift','sec:EYE-CHI',
        'One cell explains $R^2\\simeq2.89\\%$ of displacement variance after linear rescaling, while the common signal supplies 82% of actual displacement variance. The larger, poorly predicted part of the single cell signal is private prediction noise.',
        'The constructed variance example above gives a small correlation even though the common command supplies most of the movement variance.',
        'The same common variance enters movement and the single cell predictor, but the predictor has much more private noise. Increasing only private predictor variance lowers correlation R while the common movement fraction χ stays at 0.82. The marked point uses the chapter’s constructed example. Calculations assume unit common gain and mutually uncorrelated contributions; they are not recorded cell data. Based on Ben-Shushan et al. (2022), main p. 10, Eqs. 11–15.',
        'Horizontal stacked bars use one variance axis in degrees squared: movement has common variance 0.00820 and other variance 0.00180; the single cell prediction has the same common variance and private variance 0.22446. A curve shows R falling as private predictor variance increases, reaching 0.170 at the constructed point, while χ remains 0.820.',
        'Private prediction noise enlarges the denominator of R without changing the covariance. The bars use the same physical scale, so the equal common pieces have equal lengths.',
        'Ben-Shushan et al. (2022), main p. 10 / PDF page 10, Eqs. 11–15; Chapter 4 EYE-CHI constructed 0.17/0.82 example.',eye,10,
        ['variance-components','correlation-denominator'],{'Var(C)':0.00820,'Var(eta)':0.00180,'Var(epsilon)':0.22446,'units':'deg^2','origin':'Exact constructed chapter example, not empirical cells.'}))
    p.append(packet('A06','fig:EYE-MSD-MEASUREMENT-OFFSET','04-eye-drift','sec:EYE-MEASUREMENT-NOISE',
        'For instance, a constructed measured MSD of $0.0014$ deg$^2$ with an estimated noise contribution $0.0010$ deg$^2$ leaves $0.0004$ deg$^2$. A $0.0001$ deg$^2$ uncertainty in the subtraction is already 25% of that result. This is why a corrected short lag point needs an uncertainty assessment as well as a positive value. If measurement errors were temporally correlated, the correction would instead be $2[\\sigma_m^2-C_\\nu(\\ell)]$, where $C_\\nu$ is their covariance at lag $\\ell$; a constant subtraction would then need revision.',
        'For a constructed Brownian movement with $D=0.010$ deg$^2$/s, adding independent position measurement errors with $2\\sigma_m^2=0.0010$ deg$^2$ shifts every positive-lag MSD upward by the same amount.',
        'For positive lags, independent measurement error adds $2\\sigma_m^2$ to the movement MSD, here $M(\\ell)=2D\\ell$. The isolated point at zero lag stays zero because each sample is subtracted from itself. At 20 ms, subtracting 0.0010 from 0.0014 deg² leaves 0.0004 deg²; the shown ±0.0001 deg² subtraction uncertainty is 25% of that remainder. Original analytic example, not experimental data, using Ben-Shushan et al. (2022), main p. 10, Eqs. 18–19.',
        'Movement MSD rises linearly from zero. For all strictly positive lags, observed MSD is higher by 0.0010 degrees squared. The observed curve has an open endpoint at lag zero, above the actual zero-lag point at zero. At 20 milliseconds the observed and corrected values are 0.0014 and 0.0004 degrees squared, with a bracket showing the subtraction and an uncertainty bar on the corrected value.',
        'The offset comes from two independent position errors, one at each endpoint. Its removal changes the average MSD; it does not recover each trajectory’s unknown error. The Brownian movement is chosen only to make the constant offset visible.',
        'Ben-Shushan et al. (2022), main p. 10 / PDF page 10, Removal of measurement noise, Eqs. 18–19; Chapter 4 EYE-MEASUREMENT-NOISE subtraction example. Brownian M=2Dℓ is the guide’s earlier diffusion model.',eye,10,
        ['positive-lag-offset','zero-lag','subtraction-uncertainty'],{'D_deg2_per_s':.01,'sigma_m2_deg2':.0005,'lag_example_s':.02,'offset_uncertainty_deg2':.0001,'origin':'Chosen analytic movement and chapter subtraction example, not fitted data.'}))
    p.append(packet('A07','fig:PLACE-GP-TO-FIRING','05-place-fields','sec:PLACE-GP',
        'Thus $\\sigma$ compares typical height with typical slope and has units of distance. In an isotropic field, the same definition applies along any unit direction. For the smooth Gaussian covariance $C(\\Delta x)=\\sigma_h^2\\exp[-\\|\\Delta x\\|^2/(2\\sigma^2)]$, it is exactly the parameter in that exponent. The paper uses a Gaussian covariance for its simulations. Other smooth covariances can share this local scale while having different longer distance structure.[^p3-scale]',
        'A simulated Gaussian input map with covariance $C(\\Delta x)=\\exp[-(\\Delta x/\\sigma)^2/2]$ gives the firing map below when $q=0.8$ and $a=6$ Hz. Position is shown in units of $\\sigma$.',
        'One fixed Gaussian input draw becomes a nonnegative firing map through $F(x)=a[z(x)-q]_+$. Values below $q$ become zero; values above $q$ keep their relative heights after subtraction and scaling. The shaded connected intervals are the model fields. This is a simulated teaching map with chosen parameters, not a recorded cell. Based on Mainali et al. (2025), Fig. 1A and STAR Methods Eqs. 2–3, p. e1.',
        'The upper plot shows one fixed smooth input against spatial position, with a threshold at 0.8 and shaded intervals above it. The lower plot uses the same positions and plots six times the positive excess above the threshold in hertz. Its connected positive intervals align with the upper shading; all other positions have zero firing.',
        'Thresholding changes the distribution of values and can separate one smooth input curve into several fields. Both panels describe the same fixed map over space, so neither curve is a trajectory over time.',
        'Mainali et al. (2025), Fig. 1A, p. 1112 / PDF page 4; STAR Methods Model details, Eqs. 2–3, p. e1 / PDF page 13; supplement Methods S1, printed p. 8 / PDF page 9.',place,13,
        ['input-map','thresholded-rate'],{'q':.8,'gain_a_Hz':6,'sigma_distance_unit':1,'track_length_sigma':24,'grid_points':601,'numpy_seed':16,'covariance':'exp(-0.5*(dx/sigma)^2)','numerical_diagonal_jitter':1e-10,'origin':'Finite-grid multivariate Gaussian simulation with fixed seed; no fit or experimental data.'}))
    p.append(packet('A08','fig:PLACE-SIZE-DENSITY-COLLAPSE','05-place-fields','sec:PLACE-SIZE-LAW',
        'Size has units of distance to the power $d$, while $\\beta$ has units of inverse distance squared in every dimension. This makes $\\beta s^{2/d}$ dimensionless, and makes $p_d(s)$ a density per unit size. These checks catch mistakes in changing variables.',
        'Writing dimensionless size as $w=\\beta^{d/2}s$ removes the size scale. The dimensional size laws then differ in shape, while the transformed variable $U=\\beta s^{2/d}=w^{2/d}$ has the same exponential law.',
        'The limiting size densities differ with spatial dimension: one dimensional length is Rayleigh, two dimensional area is exponential, and three dimensional volume has a density that rises without bound as size approaches zero, while its integral remains one. Their survival probabilities, the probabilities of exceeding a threshold, coincide after transformation to $U=\\beta s^{2/d}$, where $\\Pr(U>u)=e^{-u}$. These are exact calculations from the high-threshold limiting law, not finite-threshold simulations or measured histograms. Based on Mainali et al. (2025), main Eq. 1, p. 1111, and Methods S3.',
        'Three density curves against dimensionless size w show the one dimensional curve starting at zero, the two dimensional curve starting at one, and the three dimensional curve rising without bound toward zero size. An arrow marks the unbounded end. In the second panel, three differently styled survival curves coincide on exp(-u) after U=w^(2/d).',
        'Removing units does not erase the difference between length, area, and volume distributions. The nonlinear transformation to U removes that shape difference; its shared exponential law is the assumption used in the change of variables.',
        'Mainali et al. (2025), main p. 1111 / PDF page 3, Eq. 1; supplement Methods S3, printed p. 12 / PDF page 13, high-threshold distributions and moment relation before S18. Chapter 5 PLACE-SIZE-LAW corrects the printed S18 mean-scale algebra.',place,3,
        ['dimension-densities','exponential-survival'],{'dimensionless_w':'beta^(d/2)*s','dimensions':[1,2,3],'density_formula':'(2/d)*w^(2/d-1)*exp(-w^(2/d))','survival_formula':'exp(-u)','origin':'Analytic limiting law only; no chosen finite q or fitted beta.'}))
    for item in p:
        if item['id'] in ['A07','A08']:
            item['review_contract']['source_files'].append('assets/papers/mainali-2025-supplement.pdf')
        if item['id']=='A06':
            item['review_contract']['source_files'] += ['content/chapters/01-foundations.md','content/chapters/01-foundations.yaml']
    return p

def prepare():
    p=packets()
    palette=yaml.safe_load(Path(PROFILE).read_text())['color']
    for it in p:
        src=(ROOT/it['chapter_path']).read_text(encoding='utf-8')
        assert src.count(it['anchor'])==1,(it['id'],'anchor is not unique')
        brief=dict(asset_id=it['id'],visual_id=it['visual_id'],author=AUTHOR,created_at=datetime.now().astimezone().isoformat(),
            teaching_goal=it['intro'],source_locator=it['source_locator'],source_files=it['review_contract']['source_files'],
            guide_only_parameters=it['guide_only_parameters'],required_scene_ids=it['review_contract']['required_scene_ids'],
            route='deterministic-scientific-vector',style_lock='source-maps/book-style-lock.yaml',
            palette_family={'id':'technical-editorial-blueprint','version':'1.0.0'},
            style_profile={'path':PROFILE,'id':'house-graphic-v1','version':'0.1.0'},
            palette_colors_and_roles=palette,palette_gate='Exact SVG token membership; not a raster pixel-deviation claim.',
            forbidden_claims=['No experimental-data claim','No full chapter coverage claim','No self approval'],
            insertion_width_px=700,review_contract=it['review_contract'])
        brief['brief']={'asset_id':it['id']}
        brief['style_contract']=dict(palette_family_id='technical-editorial-blueprint',palette_family_version='1.0.0',
            route='vector',profile_id='house-graphic-v1',profile_version='0.1.0',profile_path=PROFILE,
            palette={'allowed_special_purpose_colors':[],'check':'Exact SVG token membership in selected profile.'})
        (ROOT/it['brief']).write_text(yaml.safe_dump(brief,sort_keys=False,allow_unicode=True),encoding='utf-8')
    ledger=dict(schema_version=1,visual_ledger_version=1,visuals=[])
    for it in p:
        pending=dict(schema_version=1,status='pending',reviewer=None,reviewed_sha256=None,policy_sha256=None,context_sha256=None,input_sha256={},source_scope_sha256={},strongest_objection=None,objection_resolution=None,
            checks={k:dict(verdict='pending',evidence=[]) for k in ['technical_accuracy','visual_explanation','readability','palette','coverage']})
        pending['checks']['visual_explanation'].update(reference_comparison=None,scenes=[dict(id=s,depiction=None,visible_objects=[],relationship=None,teaching_contribution=None) for s in it['review_contract']['required_scene_ids']])
        pending['checks']['readability'].update(full_size_inspected=False,reviewed_width_px=None)
        pending['checks']['coverage'].update(covered_ids=[],visible_evidence={})
        ledger['visuals'].append(dict(visual_id=it['visual_id'],block_id=it['visual_id'],asset=it['paths']['png'],status='candidate',embedded=False,
            origin='Original analytic or simulated teaching construction; not experimental data.',source_status=it['source_locator'],
            rights='Original guide figure',generator=SCRIPT,vector_source=it['paths']['svg'],placement=it['placement'],
            caption=it['caption'],accessibility_description=it['alt'],teaching_introduction=it['intro'],interpretation=it['interpretation'],
            review_contract=it['review_contract'],diagram_review=pending))
    (HERE/'eye-place-integration.json').write_text(json.dumps(p,indent=2,ensure_ascii=False),encoding='utf-8')
    (HERE/'pending-ledger-eye-place.yaml').write_text(yaml.safe_dump(ledger,sort_keys=False,allow_unicode=True),encoding='utf-8')
    checkpoint('briefs and pending contracts written before drawing')

def checkpoint(stage):
    now=datetime.now().astimezone()
    start=datetime.fromisoformat('2026-10-24T18:31:14.999410+03:00')
    path=HERE/'eye-place-checkpoints.jsonl'
    previous=None
    if path.exists(): previous=json.loads(path.read_text().strip().splitlines()[-1])['timestamp']
    data=dict(timestamp=now.isoformat(),stage=stage,root_wall_elapsed_seconds=(now-start).total_seconds(),
        since_previous_checkpoint_seconds=(now-datetime.fromisoformat(previous)).total_seconds() if previous else None,awake_execution_time='unverified')
    with path.open('a',encoding='utf-8') as f: f.write(json.dumps(data)+'\n')
    print(json.dumps(data))

def a05():
    c=.0082;eta=.0018;eps=.22446; y=c+eta;x=c+eps
    fig,axs=plt.subplots(1,2,figsize=(9,4.3),gridspec_kw={'width_ratios':[1.1,1]})
    ax=axs[0];setup(ax,r'variance (deg$^2$)')
    ax.barh([1,0],[c,c],color=TEAL,height=.45,label='common C')
    ax.barh([1,0],[eta,eps],left=c,color=PALE_ORANGE,edgecolor=ORANGE,height=.45,label='other / private')
    ax.set(yticks=[0,1],yticklabels=['cell predictor X','movement Y'],xlim=(0,.25),ylim=(-.5,1.65),xticks=[0,.1,.2])
    ax.text(.118,1.04,r'$\chi=0.820$',color=TEAL,ha='center')
    ax.annotate('',xy=(y,1),xytext=(.065,1),arrowprops=dict(arrowstyle='->',color=TEAL,lw=1.1))
    ax.text(.11,.02,'private prediction noise',ha='center',va='center',fontsize=10.5,color=ORANGE)
    ax.legend(frameon=False,loc='upper center',bbox_to_anchor=(.46,-.19),fontsize=10.5,ncol=1)
    ax=axs[1];setup(ax,r'private predictor variance (deg$^2$)','fraction / correlation')
    e=np.linspace(0,.25,501);r=c/np.sqrt(y*(c+e));chi=c/y
    ax.plot(e,r,color=INK,label='correlation R')
    ax.axhline(chi,color=TEAL,ls='--',label=r'common fraction $\chi$')
    ax.plot(eps,c/np.sqrt(x*y),'o',color=INK)
    ax.annotate('R = 0.170',xy=(eps,c/np.sqrt(x*y)),xytext=(.115,.32),fontsize=11,color=INK,arrowprops=dict(arrowstyle='-',color=INK,lw=1))
    ax.text(.13,.86,r'$\chi=0.820$',color=TEAL,ha='center')
    ax.set(xlim=(0,.25),ylim=(0,1),xticks=[0,.1,.2],yticks=[0,.5,1])
    ax.legend(frameon=False,loc='upper center',bbox_to_anchor=(.5,-.19),fontsize=10.5)
    fig.subplots_adjust(left=.16,right=.97,bottom=.27,top=.94,wspace=.48)
    return style.save(fig,'A05',{'example_R':bool(abs(c/np.sqrt(x*y)-.17)<1e-5),'example_chi':abs(chi-.82)<1e-12,'common_bar_lengths_equal':True,'R_decreases':bool(np.all(np.diff(r)<0))},
        {'Var_C_deg2':c,'Var_eta_deg2':eta,'Var_epsilon_deg2':eps,'R':c/np.sqrt(x*y),'chi':chi,'construction':'Chapter exact variance example and analytic variation of private predictor variance only.'})

def a06():
    D=.01;offset=.001;ell=np.linspace(0,.12,601);m=2*D*ell;obs=m+offset
    fig,ax=plt.subplots(figsize=(8.6,4.8));setup(ax,'lag ℓ (ms)',r'MSD (deg$^2$)')
    ax.plot(ell*1000,obs,color=INK,label='observed, positive lags')
    ax.plot(ell*1000,m,color=TEAL,label='movement')
    ax.axhline(offset,color=ORANGE,ls=':',lw=1.5,label=r'measurement term $2\sigma_m^2$')
    ax.plot(0,offset,marker='o',color=INK,mfc='white',mec=INK,ms=7,zorder=5)
    ax.plot(0,0,'o',color=MUTED,ms=6,zorder=5)
    ax.annotate('zero lag: 0',xy=(0,0),xytext=(14,.00014),fontsize=11,color=MUTED,arrowprops=dict(arrowstyle='-',color=MUTED,lw=1))
    lag=.02;true=2*D*lag;measured=true+offset
    ax.plot([20,20],[true,measured],ls='none',marker='o',color=INK,ms=5)
    ax.annotate('',xy=(20,measured),xytext=(20,true),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=1.6))
    ax.text(25,.00116,'subtract 0.0010',fontsize=11,color=ORANGE,va='center')
    ax.errorbar(20,true,yerr=.0001,fmt='o',color=TEAL,capsize=5,elinewidth=2,zorder=6)
    ax.annotate('0.0004 ± 0.0001',xy=(20,true),xytext=(48,.00038),fontsize=11,color=TEAL,arrowprops=dict(arrowstyle='-',color=TEAL,lw=1))
    ax.text(20,measured+.00014,'0.0014',fontsize=11,color=INK,ha='center')
    ax.set(xlim=(-3,124),ylim=(-.00012,.00375),xticks=[0,20,40,60,80,100,120],yticks=[0,.001,.002,.003])
    ax.ticklabel_format(axis='y',style='plain',useOffset=False)
    ax.legend(frameon=False,loc='upper left',fontsize=11)
    fig.subplots_adjust(left=.14,right=.97,bottom=.17,top=.95)
    return style.save(fig,'A06',{'positive_lag_offset':bool(np.allclose(obs-m,offset)),'subtraction_example':abs(measured-.0014)<1e-12,'uncertainty_fraction':abs(.0001/true-.25)<1e-12,'zero_lag_explicitly_separate':True},
        {'D_deg2_s':D,'single_position_error_variance_deg2':offset/2,'positive_lag_noise_term_deg2':offset,'example_lag_s':lag,'true_MSD_deg2':true,'observed_MSD_deg2':measured,'construction':'Analytic Brownian movement plus independent sampled position measurement errors; no measured data.'})

def a07():
    x=np.linspace(0,24,601);q=.8;a=6.;cov=np.exp(-.5*(x[:,None]-x[None,:])**2)
    z=np.linalg.cholesky(cov+1e-10*np.eye(len(x)))@np.random.default_rng(16).standard_normal(len(x))
    rate=a*np.maximum(z-q,0)
    fig,axs=plt.subplots(2,1,figsize=(8.6,5.7),sharex=True,gridspec_kw={'height_ratios':[1.15,1]})
    ax=axs[0];setup(ax,ylabel='normalized input z(x)')
    ax.plot(x,z,color=INK)
    ax.axhline(q,color=ORANGE,ls='--',lw=1.5)
    ax.fill_between(x,q,z,where=z>q,color=PALE_TEAL,interpolate=True)
    ax.text(24.2,q+.14,'q = 0.8',color=ORANGE,va='bottom',fontsize=11)
    ax.set(ylim=(min(z)-.25,max(z)+.45),yticks=[-2,0,2])
    ax.text(.02,.88,'one fixed simulated map',transform=ax.transAxes,color=MUTED,fontsize=11)
    ax=axs[1];setup(ax,r'position / $\sigma$','firing rate F(x) (Hz)')
    ax.plot(x,rate,color=TEAL);ax.fill_between(x,0,rate,color=PALE_TEAL)
    ax.text(.02,.88,r'$F(x)=6[z(x)-0.8]_+$',transform=ax.transAxes,color=TEAL,fontsize=12)
    ax.set(xlim=(0,26.5),ylim=(-.3,max(rate)+1.7),xticks=[0,4,8,12,16,20,24])
    # Shared positions keep thresholded components aligned, without a flow arrow.
    fig.subplots_adjust(left=.13,right=.92,bottom=.13,top=.96,hspace=.23)
    components=int(np.count_nonzero(np.diff((z>q).astype(int))==1)+(z[0]>q))
    return style.save(fig,'A07',{'rate_nonnegative':bool(np.all(rate>=0)),'threshold_support_exact':bool(np.array_equal(rate>0,z>q)),'same_map_and_positions':True,'multiple_components':components>=2,'covariance_unit_variance':bool(np.allclose(np.diag(cov),1))},
        {'q':q,'gain_Hz':a,'seed':16,'grid_size':len(x),'grid_spacing_sigma':float(x[1]-x[0]),'diagonal_jitter':1e-10,'components_on_grid':components,'input_min':float(z.min()),'input_max':float(z.max()),'construction':'A fixed finite-grid Gaussian draw with covariance exp(-dx^2/2), not a measured cell.'})

def a08():
    fig,axs=plt.subplots(1,2,figsize=(9,4.5));styles=[(1,INK,'-'),(2,TEAL,'--'),(3,ORANGE,':')]
    w=np.geomspace(.0005,5,1800)
    ax=axs[0];setup(ax,r'dimensionless size $w=\beta^{d/2}s$','density of w')
    for d,color,ls in styles:
        density=2/d*w**(2/d-1)*np.exp(-w**(2/d))
        ax.plot(w,density,color=color,ls=ls,label=f'd = {d}')
    ax.annotate('unbounded\nas w → 0',xy=(.018,2.4),xytext=(.82,2.12),fontsize=10.5,color=ORANGE,arrowprops=dict(arrowstyle='->',color=ORANGE,lw=1.1))
    ax.set(xlim=(0,5),ylim=(0,2.55),xticks=[0,1,2,3,4,5],yticks=[0,1,2])
    ax.legend(frameon=False,loc='center right',fontsize=11)
    ax=axs[1];setup(ax,r'$u=\beta s^{2/d}=w^{2/d}$',r'survival probability Pr(U > u)')
    u=np.linspace(0,5,501)
    # Different widths/dashes make the coincident laws visible, not offset curves.
    for (d,color,ls),width in zip(styles,[4,2.5,1.8]):
        ax.plot(u,np.exp(-u),color=color,ls=ls,lw=width,label=f'd = {d}')
    ax.text(2.1,.69,r'$\Pr(U>u)=e^{-u}$',color=INK,fontsize=12)
    ax.set(xlim=(0,5),ylim=(0,1.04),xticks=[0,1,2,3,4,5],yticks=[0,.5,1])
    ax.legend(frameon=False,loc='center right',fontsize=11)
    fig.subplots_adjust(left=.085,right=.97,bottom=.20,top=.95,wspace=.38)
    integrals={d:quad(lambda v:2/d*v**(2/d-1)*np.exp(-v**(2/d)),0,np.inf)[0] for d,_,_ in styles}
    means={d:quad(lambda v:v*2/d*v**(2/d-1)*np.exp(-v**(2/d)),0,np.inf)[0] for d,_,_ in styles}
    return style.save(fig,'A08',{'density_normalization':all(abs(v-1)<1e-7 for v in integrals.values()),'mean_gamma_identity':all(abs(means[d]-gamma(1+d/2))<1e-7 for d in means),'survival_collapse':all(np.allclose(np.exp(-(u**(d/2))**(2/d)),np.exp(-u)) for d,_,_ in styles),'d3_divergence_marked_not_zero':True},
        {'normalization_integrals':integrals,'dimensionless_means':means,'density_formula':'(2/d)*w^(2/d-1)*exp(-w^(2/d))','survival':'exp(-u)','construction':'Exact high-threshold limiting densities. The d=3 density diverges integrably as w approaches zero; display is clipped at y=2.55 and explicitly marked.'})

if __name__=='__main__':
    if '--prepare' in sys.argv: prepare()
    else:
        assert all((HERE/f'{i}-brief.yaml').exists() for i in ['A05','A06','A07','A08']), 'Prepare briefs/contracts before drawing.'
        results=[a05(),a06(),a07(),a08()]
        (HERE/'eye-place-calculation-results.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
        checkpoint('four candidates drawn; local pixel inspection and independent review still pending')
        print(json.dumps({r['asset_id']:r['status'] for r in results}))
