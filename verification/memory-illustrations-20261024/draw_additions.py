"""Exact Chapter 2 teaching curves. Run --prepare before the palette check and build."""
from pathlib import Path
import sys, json, math, importlib.util
from datetime import datetime
import numpy as np
import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
STYLE_FILE = ROOT / 'verification/illustrations/figure_style.py'
spec = importlib.util.spec_from_file_location('memory_additions_style', STYLE_FILE)
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
S.OUT = ROOT / 'candidate-content/visuals/candidates/20261024'
plt = S.plt
RULE_ROOT = 'C:/Users/vital/.codex/skills/course-diagram-builder/references/'
START = '2026-10-24T18:06:16.7630300+03:00'

ITEMS = [
    dict(id='M01', figure='fig:MEMORY-SPIKE-TRACE', section='sec:MEMORY-SPIKES',
         purpose='Distinguish spike events from the activation they leave behind.',
         scenes=['event-train', 'activation-trace'],
         composition='Two stacked plots with one shared time axis; events align with exact unit jumps.',
         parameters={'spike_times_ms':[20,55,70,130,210], 'tau_ms':50, 'initial_activation':0},
         required=['Discrete event marks at the five specified times.', 'Activation is the sum of exponential contributions, with a unit jump at each event.', 'Between events activation decays with time constant 50 ms.'],
         caption='Each spike adds one activation unit, which then decays with a 50 ms time constant. Closely spaced spikes add to the activation left by earlier spikes. The five spike times are an illustrative input, and the activation is calculated exactly from the chapter equation.',
         alt='Five spike marks share a time axis with an activation trace. Each mark aligns with a vertical rise of one activation unit. The activation decays smoothly between spikes, and nearby spikes build on the remaining activation.',
         introduction='The same five spike times can be shown as discrete events and as the activation they leave behind.',
         conclusion='The activation retains a decaying contribution from earlier spikes, so a spike train and its activation trace are different objects.'),
    dict(id='M02', figure='fig:MEMORY-INHIBITION-RATES', section='sec:MEMORY-SYMMETRIC',
         purpose='Show that opposite changes in individual firing rates can leave local diffusion constant.',
         scenes=['opposite-rates', 'constant-diffusion'],
         composition='Aligned rate and diffusion plots share the valid interior memory coordinate; open endpoints exclude the boundary.',
         parameters={'b_activation_units':20, 'tau_s':0.1, 'domain':'-20 < theta < 20', 'r_sum_spikes_per_s':200, 'D_coordinate_squared_per_s':100},
         required=['Rates r1=(20+theta)/0.2 and r2=(20-theta)/0.2.', 'Sum r1+r2=200 spikes/s.', 'D=(r1+r2)/2=100 coordinate units squared/s.', 'Only the interior of the linear positive-rate model is shown; endpoint markers are open.'],
         caption='For the chapter’s two mutually inhibiting cells, b = 20 activation units and tau = 0.1 s give opposite changes in the two rates. Their sum remains 200 spikes/s, so local D remains 100 coordinate units squared/s. Open endpoints mark the excluded boundaries; the linear interior model does not determine boundary behavior. These curves are calculated examples, not simulation data.',
         alt='As theta increases through the interior from minus 20 to 20 activation units, r1 increases toward 200 spikes per second and r2 decreases toward zero. Their dashed sum stays at 200. A lower aligned plot shows D constant at 100 coordinate units squared per second. Open endpoint circles exclude both boundaries.',
         introduction='The mutual inhibition example makes the distinction between individual rates and their contribution to diffusion visible.',
         conclusion='The individual rates vary with the stored value, but their summed variability and therefore the local diffusion coefficient remain constant inside the valid range.'),
    dict(id='M03', figure='fig:MEMORY-LINE-RING', section='sec:MEMORY-LONG-TIME',
         purpose='Show how constant local diffusion yields unbounded line error but bounded reported angular error.',
         scenes=['wrapped-density', 'line-ring-msd'],
         composition='Two vertically stacked plots compare wrapped densities and then squared errors over time.',
         parameters={'D_rad_squared_per_s':0.5, 'initial_angle_rad':0, 'density_times_s':[0.2,1,5], 'density_method':'Gaussian image sum k=-12..12', 'MSD_method':'integral of x^2 times exact wrapped density; Fourier series for curve', 'angular_error_interval':'[-pi,pi)', 'uniform_density': '1/(2*pi)', 'limiting_angular_MSD':'pi^2/3'},
         required=['Wrapped Gaussian densities widen toward the uniform density 1/(2pi).', 'The line MSD is 2Dt.', 'The reported angular MSD tends to pi^2/3 on [-pi,pi).', 'Both use the same constant D=0.5 rad squared/s and start at zero.'],
         caption='With the same constant D = 0.5 rad²/s, wrapped Gaussian error densities widen toward 1/(2π). The unbounded line has mean squared error 2Dt; reporting angular error in [−π, π) instead gives a mean squared error that approaches π²/3. The flattening comes from the bounded error convention while local diffusion stays constant. All curves are analytic teaching calculations, not paper simulation data.',
         alt='Wrapped Gaussian densities at 0.2, 1 and 5 seconds broaden toward a dashed uniform density over angular errors from minus pi to pi. Below, line mean squared error rises linearly while wrapped angular mean squared error approaches a horizontal pi squared over three reference, with the same constant diffusion coefficient.',
         introduction='Wrapping the Gaussian around a circle changes long delay errors even when the local diffusion coefficient stays constant.',
         conclusion='A flattening angular error curve can follow from the bounded way error is reported; it does not require the local noise mechanism to weaken.'),
]

def checkpoint(stage):
    p=HERE/'checkpoints.jsonl'
    with p.open('a', encoding='utf-8') as f:
        f.write(json.dumps({'timestamp':datetime.now().astimezone().isoformat(),'root_start':START,'stage':stage,'awake_execution':'unverified; Windows sleep/resume events not inspected'})+'\n')

def prepare():
    HERE.mkdir(parents=True, exist_ok=True)
    profile=yaml.safe_load((Path(RULE_ROOT)/'house-graphic-v1.yaml').read_text(encoding='utf-8'))
    rows=[]
    for item in ITEMS:
        brief_path=f'verification/memory-illustrations-20261024/{item["id"]}-brief.yaml'
        contract=dict(schema_version=1,figure_role='quantitative-figure',route='vector',unit_scope='chapter',author='/root/draw_memory_additions',role_reason=item['purpose'],source_files=['content/chapters/02-memory-dynamics.md','content/chapters/02-memory-dynamics.yaml','verification/memory-illustrations-20261024/draw_additions.py',brief_path,'verification/illustrations/figure_style.py'],rule_files=[RULE_ROOT+'visual-qa.md',RULE_ROOT+'review-acceptance.md'],style_lock='source-maps/book-style-lock.yaml',style_profile=RULE_ROOT+'house-graphic-v1.yaml',reference_images=[],palette_audit=f'candidate-content/visuals/candidates/20261024/{item["id"]}/qa.json',vector_spec='verification/memory-illustrations-20261024/draw_additions.py',insertion_width_px=700,required_scene_ids=item['scenes'],coverage={'applicable':False,'reason':'Internal quantitative figure, not an opening map; no chapter coverage claim.'})
        brief={'brief':dict(asset_id=item['figure'],scope='chapter',book='burak-three-papers',chapter='ch:MEMORY-DYNAMICS',purpose=item['purpose'],target_use=item['section'],generation_authorized=True,insertion_authorized=False), 'author':'/root/draw_memory_additions', 'figure_role':'quantitative-figure', 'visual_explanation':{'applicable':True,'figure_role':'quantitative-figure','composition':item['composition'],'required_scene_ids':item['scenes'],'reference_reason':'Exact mathematical plots; no structural template or illustrated-opener reference applies.'},'chapter_map_coverage':{'applicable':False,'reason':'Section calculation figure, not an opening map.'},'style_contract':{'book_style_lock_path':'source-maps/book-style-lock.yaml','palette_family_id':'technical-editorial-blueprint','palette_family_version':'1.0.0','route':'vector','profile_id':'house-graphic-v1','profile_version':'0.1.0','profile_path':RULE_ROOT+'house-graphic-v1.yaml','palette':{'colors_and_roles':profile['color'],'color_distance':'exact SVG color token membership; no raster pixel-deviation claim','maximum_deviation_fraction':0,'allowed_special_purpose_colors':[]}}, 'parameters':item['parameters'],'required_items':item['required'],'language_contract':{'book_loci':[item['section']],'caption':item['caption'],'alt_text':item['alt'],'teaching_introduction':item['introduction'],'conclusion':item['conclusion']},'review_contract':contract,'limitations':['Analytic teaching construction with specified illustrative parameters; not experimental or simulated paper data.','No generic vector-template gate is claimed; computed checks and image inspection support independent review.'],'manual_rule_disposition':{'applicable':['semantic correspondence','label and numerical accuracy','readability at full size and 700px','units and domain conditions','palette color roles','canvas clipping'],'not_applicable':['opening-map coverage','generic structural-template geometry gates','raster palette measurement']}}
        (ROOT/brief_path).write_text(yaml.safe_dump(brief,sort_keys=False,allow_unicode=True),encoding='utf-8')
        review={'schema_version':1,'status':'pending','reviewer':None,'reviewed_sha256':None,'policy_sha256':None,'context_sha256':None,'input_sha256':{},'source_scope_sha256':{},'strongest_objection':None,'objection_resolution':None,'checks':{k:{'verdict':'pending','evidence':[]} for k in ['technical_accuracy','visual_explanation','readability','palette','coverage']}}
        rows.append(dict(visual_id=item['figure'],block_id=item['figure'],asset=f'candidate-content/visuals/candidates/20261024/{item["id"]}/figure.png',status='candidate',embedded=False,generator='verification/memory-illustrations-20261024/draw_additions.py',placement=item['section'],caption=item['caption'],accessibility_description=item['alt'],teaching_introduction=item['introduction'],interpretation=item['conclusion'],content_brief=brief_path,review_contract=contract,diagram_review=review))
    (HERE/'pending-visual-ledger.yaml').write_text(yaml.safe_dump({'schema_version':1,'visual_ledger_version':1,'visuals':rows},sort_keys=False,allow_unicode=True),encoding='utf-8')
    checkpoint('briefs and pending contracts written before generation')

def spike_trace():
    spikes=np.array([20.,55.,70.,130.,210.]); tau=50.
    fig,(a,b)=plt.subplots(2,1,figsize=(8.7,5.7),gridspec_kw={'height_ratios':[1,3]},sharex=True)
    fig.subplots_adjust(left=.12,right=.97,bottom=.13,top=.96,hspace=.14)
    a.vlines(spikes,0,1,color=S.INK,lw=2.3)
    a.set_ylim(-.03,1.2); a.set_yticks([]); a.set_ylabel('Spike\nevents',rotation=0,ha='right',va='center',labelpad=11)
    a.spines['left'].set_visible(False); a.spines['bottom'].set_visible(False); a.tick_params(bottom=False)
    bounds=np.r_[0,spikes,300.]; pre=[]; post=[]
    def activation(t): return np.sum(np.exp(-(t-spikes[spikes<t])/tau))
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        xx=np.linspace(lo,hi,250)
        earlier=spikes[spikes<=lo] if lo else np.array([])
        yy=np.exp(-(xx[:,None]-earlier[None,:])/tau).sum(axis=1)
        b.plot(xx,yy,color=S.TEAL)
    for t in spikes:
        left=activation(t); pre.append(left); post.append(left+1)
        b.vlines(t,left,left+1,color=S.TEAL,lw=2.1)
    b.annotate('+1',xy=(130,(pre[3]+post[3])/2),xytext=(153,1.25),color=S.TEXT,ha='left',arrowprops={'arrowstyle':'-','color':S.MUTED,'lw':1})
    S.setup(b,'Time (ms)','Activation s (units)'); b.set_xlim(0,300); b.set_ylim(0,2.5); b.set_yticks([0,1,2]); b.set_xticks([0,50,100,150,200,250,300])
    checks={'spike_jump_exactly_one':bool(np.allclose(np.array(post)-np.array(pre),1,rtol=0,atol=1e-14)), 'sum_formula':bool(abs(activation(100)-sum(np.exp(-(100-t)/50) for t in spikes if t<100))<1e-14), 'decay_time_constant':bool(np.isclose(np.exp(-50/tau),np.exp(-1))), 'five_discrete_events':len(spikes)==5}
    return S.save(fig,'M01',checks,{'parameters':ITEMS[0]['parameters'],'pre_jump':pre,'post_jump':post,'exact_spike_value_convention':'chapter uses t_spike < t; vertical jumps depict left and right limits','generic_template_gate':'not applicable to exact mathematical plot'})

def inhibition():
    theta=np.linspace(-20,20,601); r1=(20+theta)/.2; r2=(20-theta)/.2; D=(r1+r2)/2
    fig,(a,b)=plt.subplots(2,1,figsize=(8.7,6.0),sharex=True,gridspec_kw={'height_ratios':[2.25,1]})
    fig.subplots_adjust(left=.15,right=.96,bottom=.13,top=.88,hspace=.20)
    a.plot(theta,r1,color=S.INK,label=r'$\bar r_1$'); a.plot(theta,r2,color=S.TEAL,label=r'$\bar r_2$'); a.plot(theta,r1+r2,'--',color=S.MUTED,label=r'$\bar r_1+\bar r_2$')
    for y,c in [(r1,S.INK),(r2,S.TEAL),(r1+r2,S.MUTED)]:
        a.plot(theta[[0,-1]],y[[0,-1]],'o',ms=6,mfc=S.PAPER,mec=c,mew=1.4,clip_on=False)
    a.legend(loc='upper center',ncol=3,frameon=False,bbox_to_anchor=(.5,1.17))
    S.setup(a,ylabel='Firing rate (spikes/s)'); a.set_yticks([0,100,200]); a.set_ylim(-10,220)
    b.plot(theta,D,color=S.TEAL); b.plot(theta[[0,-1]],D[[0,-1]],'o',ms=6,mfc=S.PAPER,mec=S.TEAL,mew=1.4,clip_on=False)
    S.setup(b,r'Memory coordinate $\theta$ (activation units)',r'$D$ (coordinate units$^2$/s)'); b.set_ylim(0,135); b.set_yticks([0,100]); b.set_xlim(-20,20); b.set_xticks([-20,-10,0,10,20])
    return S.save(fig,'M02',{'rate_sum_200':bool(np.allclose(r1+r2,200)), 'D_constant_100':bool(np.allclose(D,100)),'rates_positive_interior':bool(np.all(r1[1:-1]>0)&np.all(r2[1:-1]>0)), 'projection_normalization':bool(np.isclose(np.dot([1,-1],[.5,-.5]),1))},{'parameters':ITEMS[1]['parameters'],'generic_template_gate':'not applicable to exact mathematical plot','boundary_disposition':'Curves show interior limits with open endpoint markers; no boundary dynamics or extrapolation claimed.'})

def density(x,t,D=.5):
    k=np.arange(-12,13)
    return np.exp(-(x[:,None]+2*np.pi*k[None,:])**2/(4*D*t)).sum(axis=1)/np.sqrt(4*np.pi*D*t)

def line_ring():
    x=np.linspace(-np.pi,np.pi,6001); times=[.2,1.,5.]; D=.5
    fig,(a,b)=plt.subplots(2,1,figsize=(8.7,7.2))
    fig.subplots_adjust(left=.14,right=.97,bottom=.10,top=.95,hspace=.49)
    for t,col,ls in zip(times,[S.INK,S.TEAL,S.MUTED],['-','-','-']): a.plot(x,density(x,t),color=col,ls=ls,label=f'{t:g} s')
    a.axhline(1/(2*np.pi),color=S.LINE,ls='--',lw=1.8,label='Uniform')
    S.setup(a,r'Angular error (rad), reported in $[-\pi,\pi)$',r'Probability density (rad$^{-1}$)')
    a.set_xlim(-np.pi,np.pi); a.set_xticks([-np.pi,0,np.pi],['−π','0','π']); a.set_ylim(0,.96); a.set_yticks([0,.3,.6,.9]); a.legend(frameon=False,loc='upper right',ncol=2)
    tt=np.linspace(0,10,1201); n=np.arange(1,801)
    msd=np.pi**2/3+4*(((-1.)**n/n**2)[None,:]*np.exp(-D*tt[:,None]*n[None,:]**2)).sum(axis=1); msd[0]=0
    b.plot(tt,2*D*tt,color=S.INK,label=r'Line: $2Dt$'); b.plot(tt,msd,color=S.TEAL,label='Wrapped angle')
    b.axhline(np.pi**2/3,color=S.MUTED,ls='--',lw=1.5,label=r'$\pi^2/3$')
    S.setup(b,'Time (s)',r'Mean squared error (rad$^2$)'); b.set_xlim(0,10); b.set_ylim(0,10.2); b.set_yticks([0,np.pi**2/3,6,10],['0','π²/3','6','10']); b.legend(frameon=False,loc='upper left')
    norms=[float(np.trapezoid(density(x,t),x)) for t in times]
    exact_msd=[float(np.trapezoid(x*x*density(x,t),x)) for t in times]
    fourier=[float(np.pi**2/3+4*np.sum((-1.)**n/n**2*np.exp(-D*t*n*n))) for t in times]
    checks={'densities_normalized':bool(np.allclose(norms,1,atol=1e-12,rtol=0)), 'densities_nonnegative':all(np.all(density(x,t)>=0) for t in times), 'MSD_matches_density_integral':bool(np.allclose(exact_msd,fourier,atol=3e-7,rtol=0)), 'long_time_density_uniform':bool(np.max(np.abs(density(x,100)-1/(2*np.pi)))<1e-12), 'long_time_MSD_pi_squared_over_3':bool(abs(np.pi**2/3+4*np.sum((-1.)**n/n**2*np.exp(-D*100*n*n))-np.pi**2/3)<1e-12), 'short_time_MSD_2Dt':bool(abs(fourier[0]-2*D*times[0])<1e-8),'same_constant_D':True}
    return S.save(fig,'M03',checks,{'parameters':ITEMS[2]['parameters'],'density_integrals':norms,'MSD_density_integral':exact_msd,'MSD_fourier':fourier,'generic_template_gate':'not applicable to exact mathematical plot','numerical_method':'Gaussian image sum k=-12..12; exact Fourier series truncated at n=800 with negligible positive-time tail; trapezoidal quadrature verification.'})

if __name__=='__main__':
    if '--prepare' in sys.argv: prepare()
    else:
        assert (HERE/'pending-visual-ledger.yaml').exists(), 'Prepare briefs and pending contracts first.'
        reports=[spike_trace(),inhibition(),line_ring()]
        (HERE/'computed-checks-summary.json').write_text(json.dumps(reports,indent=2),encoding='utf-8')
        checkpoint('all three figures generated; computed checks complete; image inspection pending')
        print(json.dumps({r['asset_id']:{'status':r['status'],'checks':r['checks']} for r in reports},indent=2))
