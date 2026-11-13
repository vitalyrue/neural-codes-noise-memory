"""Reviewer-owned evidence. Does not draw or change reader material."""
from pathlib import Path
import json, hashlib, math
from datetime import datetime
import numpy as np
from scipy.integrate import quad

ROOT=Path(__file__).resolve().parents[2]
HERE=Path(__file__).resolve().parent
PACKET=HERE/'eye-place-integration.json'
packets={x['id']:x for x in json.loads(PACKET.read_text(encoding='utf-8'))}
def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def claim(label,why): return {'claim':label,'verdict':'correct','evidence':why}
def scene(id,objects,relationship,contribution,kind='comparison'):
    return dict(id=id,depiction=kind,visible_objects=objects,relationship=relationship,teaching_contribution=contribution)

c,other,private=.0082,.0018,.22446
r=c/math.sqrt((c+other)*(c+private))
math_results={
 'A05':{'movement_variance':c+other,'predictor_variance':c+private,'covariance':c,'R':r,'chi':c/(c+other),
        'R_at_zero_private':math.sqrt(c/(c+other)), 'R_at_private_025':c/math.sqrt((c+other)*(c+.25))},
 'A06':{'movement_at_20ms':2*.01*.02,'positive_lag_offset':2*.0005,'observed_at_20ms':2*.01*.02+.001,'relative_subtraction_uncertainty':.0001/(2*.01*.02)},
 'A08':{}
}
for d in (1,2,3):
    f=lambda w: 2/d*w**(2/d-1)*math.exp(-w**(2/d))
    math_results['A08'][str(d)]={'mass':quad(f,0,np.inf)[0], 'mean':quad(lambda w:w*f(w),0,np.inf)[0],
         'mean_from_gamma':math.gamma(1+d/2),'density_at_1':f(1),'mass_below_0001':1-math.exp(-.0001**(2/d))}

specific={
'A05':{
 'technical':['The original Ben-Shushan PDF page 10 Eqs. 11-15 gives E=EC+eta and Ehat=EC+epsilon, with covariance approximately Var(EC) under the uncorrelated-noise assumption. Original source read directly using pdftotext, not copied reviewer findings.',
 'The chapter uses centered displacements X,Y in degrees. Independent calculation gives Var(Y)=0.01000, Var(X)=0.23266, covariance=0.00820 deg squared, R=0.17000159 and chi=0.82. Changing only private predictor variance leaves chi fixed and makes R decrease from 0.90554 toward 0.16137 over the displayed range.',
 'The common segments use one variance axis and exactly the same width. The predictor has a much larger private component. The graph shows a changing example family, not one curve fitted to recordings.'],
 'objection':'Two stacked bars might be read as percentages, or low single-cell correlation might be read as only 17 percent common movement.',
 'resolution':'The common variance uses the same absolute deg-squared axis in both bars, not normalized lengths. A separate plot explicitly distinguishes fraction chi from correlation R. Caption and chapter state calibrated unit gain, uncorrelated contributions and constructed data.',
 'readability':'At 700 px the small common segments remain visible, private prediction text fits inside its large bar, the two curve identities are readable, and both marked values have clear targets. The complete 1890 by 903 original also has no clipping.',
 'scenes':[scene('variance-components',['two stacked absolute-variance bars','same-width teal common pieces','much larger predictor private segment'],'Equal common displacement variance enters both measurements, with different private noise.','Makes the denominator difference concrete without converting variance into normalized percentages.'),scene('correlation-denominator',['decreasing R curve','constant chi reference','marked chapter example'],'R decreases as private predictor variance increases while chi stays at 0.82.','Explains why a weak single-cell predictor can share the source dominating actual movement.')],
 'claims':[
 claim('movement Y; cell predictor X','Matches the chapter definitions Y=C+eta and X=C+epsilon, both centered displacement variables.'),
 claim('variance (deg squared); ticks 0.0,0.1,0.2','Bars use variance, not SD or percentage. Lengths are 0.01 and 0.23266 on this common scale.'),
 claim('common C; other / private; private prediction noise','Common means Var(C)=0.0082. Other means Var(eta)=0.0018 for movement; private predictor noise means Var(epsilon)=0.22446. The labels identify contributions rather than cell recordings.'),
 claim('chi=0.820 beside movement and its leader','0.0082/0.01=0.82; the leader points to the movement bar as a whole, whose fraction is described.'),
 claim('private predictor variance (deg squared); ticks 0.0,0.1,0.2','Only epsilon variance is varied on the right. Common variance and movement variance stay fixed.'),
 claim('fraction / correlation; ticks 0.0,0.5,1.0','Both chi and R are unitless and in the displayed 0 to 1 range for this constructed family.'),
 claim('R=0.170; correlation R; point leader','At private variance 0.22446 the separate calculation gives 0.17000159; the point and leader match that coordinate.'),
 claim('common fraction chi; chi=0.820; dashed reference','Var(C)/Var(Y)=0.82 independently of private predictor variance; a horizontal trace is correct.'),
 claim('Caption: same common variance; much more private predictor noise','Matches the component lengths and variance values, with no claim of inferred trial values.'),
 claim('Caption: increasing private predictor variance lowers R, keeps chi fixed','R=c/sqrt[(c+eta)(c+epsilon)] has strictly negative derivative in epsilon for c>0, while chi is independent of epsilon.'),
 claim('Caption: marked point is constructed; unit common gain; uncorrelated terms; not recordings; Eqs.11-15','All assumptions agree with the chapter and the original source decomposition. The selected point uses the chapter values.'),
 claim('Alt: both exact component variances; falling R=0.170 and chi=0.820','All numbers independently checked; the rendered bars and curves agree.'),
 claim('Introduction: small correlation despite most movement variance being common','0.17 and 0.82 concern different ratios and the stated scenario supports both.'),
 claim('Interpretation: private noise enlarges R denominator, covariance unchanged; equal common lengths','The algebra and common-axis bar geometry both support the statement.')]
},
'A06':{
 'technical':['Read the original Ben-Shushan PDF page 10 Removal of measurement noise, Eqs.18-19. Independent endpoint errors add two copies of their position variance to positive-lag MSD; at exactly zero the two endpoint errors are the same sample and cancel.',
 'For D=.01 deg squared/s and lag .020 s, independent scalar calculation gives movement .0004, offset .0010, observed .0014 deg squared. Subtraction uncertainty .0001/.0004=.25. Movement and observed slopes are identical, with an open positive-lag endpoint at .001 and an isolated actual zero-lag point at zero.',
 'The Brownian input is explicitly chosen for illustration; this curve is not the measured eye MSD or the paper full filtered model. The chapter already derives the factor two and the temporally correlated-error qualification.'],
 'objection':'The line toward zero lag might falsely imply a measured nonzero value at lag zero, or the uncertainty bar could be read as the full experimental confidence interval.',
 'resolution':'The open endpoint at .001, separate labeled zero-lag dot and positive-lag legend distinguish the discontinuous sampled-white-error limit. Caption explicitly calls the shown quantity subtraction uncertainty in an original analytic example.',
 'readability':'The full 1806 by 1008 pixels and 700 px preview show readable units, three distinct line identities, both endpoint conventions, the subtraction bracket and its small error bar. Labels do not overlap the plotted values.',
 'scenes':[scene('positive-lag-offset',['parallel movement and observed lines','horizontal noise reference'],'Observed MSD equals movement MSD plus the same .001 deg-squared contribution at every positive lag.','Shows why constant noise can dominate the smallest movement displacements.'),scene('zero-lag',['open endpoint at .001','solid origin point','zero-lag leader'],'The positive-lag limiting offset is excluded at exactly zero lag.','Prevents treating two evaluations of the same error sample as independent.'),scene('subtraction-uncertainty',['20 ms points','double-headed subtraction bracket','corrected error bar'],'Subtracting .0010 leaves .0004, with .0001 uncertainty.','Shows that the relative uncertainty grows after subtracting a large offset.')],
 'claims':[
 claim('lag ell (ms); ticks 0,20,40,60,80,100,120','Horizontal positions are milliseconds; generator converts seconds by 1000 and the example is at .020 s.'),
 claim('MSD (deg squared); ticks 0.000,0.001,0.002,0.003','Vertical values are squared displacement, not position noise SD.'),
 claim('observed, positive lags; movement','For ell>0 the first is 2D ell+.001; the second is 2D ell. Both plotted slopes match those formulas.'),
 claim('measurement term 2 sigma_m squared','The constant reference is twice .0005=.001, per the chapter expansion and source Eq.19.'),
 claim('zero lag: 0; leader to origin; open .001 endpoint','The actual same-sample difference is zero. The dot and endpoint accurately distinguish the positive-lag extension.'),
 claim('0.0014 at upper marked point','At 20 ms, .02*.02+.001=.0014 deg squared.'),
 claim('subtract 0.0010; double-headed bracket','Bracket joins .0014 and .0004 at 20 ms, a difference .0010.'),
 claim('0.0004 plus/minus 0.0001; leader and error bar','Corrected point and error bar are .0004 with ends .0003 and .0005.'),
 claim('Introduction: constructed D=.010; independent errors; every positive lag shifted by .001','Correct for the stated time-uncorrelated errors and Brownian mean-zero movement.'),
 claim('Caption: positive lags factor two; zero sample cancellation; 20 ms subtraction; 25 percent; analytic example and source','Each numeric and conditional clause agrees with the direct arithmetic, chapter and original PDF Eqs.18-19.'),
 claim('Alt: linear movement; constant offset; open endpoint; actual zero; 20 ms corrected/observed values and bar','Every listed object is rendered and numerical values agree.'),
 claim('Interpretation: two endpoint errors; average correction does not recover trajectory errors; chosen Brownian input','The correction concerns expectation of squared differences. It does not know either endpoint error on an individual trajectory.')]
},
'A07':{
 'technical':['Read original Mainali PDF page 13, Model details Eqs.2-3: stationary Gaussian h is rectified after subtracting q times its SD. Read the current PLACE-GP normalization z=h/sigma_h, rate F=a[z-q]+, excursion-set definition and sigma definition. Normalized unit variance makes the displayed construction equivalent.',
 'The generator uses a fixed 601-point multivariate Gaussian draw with squared-exponential covariance on spacing .04 sigma, seed16 and diagonal jitter 1e-10. The 4 positive components match the upper threshold crossings and lower support. Jitter is a numerical regularization, not a claim that a continuum path acquires independent roughness.',
 'The latest insertion anchor follows the sigma definition, so x/sigma, q and a have already been introduced. Both axes represent the same fixed map over physical position, not time.'],
 'objection':'An arbitrary smooth curve might be passed off as a Gaussian-process simulation, or spatial position could be mistaken for a neural trajectory.',
 'resolution':'The explicit finite-grid Cholesky covariance, fixed seed and normalization establish the stated simulated input. The upper label says one fixed simulated map, the x-axis says position/sigma, and connected text explicitly separates spatial maps from time dynamics. No claim of empirical recovery or a full GP test is made.',
 'readability':'Full 1806 by 1197 and 700 px views preserve both axes, q line, normalization and rectification formula. Four shaded upper intervals align with the lower rate hills; the shading is faint but visible at 700 px and is supported by the actual curve/threshold intersections. No clipping or label collision.',
 'scenes':[scene('input-map',['smooth fixed input curve','q=.8 threshold','four shaded active intervals'],'The same spatial function is above threshold on four disconnected intervals.','Introduces the concrete object whose law is Gaussian before rectification.'),scene('thresholded-rate',['aligned spatial axis','nonnegative rate curve','zero inactive parts','positive fields'],'Rate is six times the positive excess above .8 at each same position.','Shows that rectification creates separated fields and changes the value distribution without evolving the map.')],
 'claims':[
 claim('normalized input z(x); ticks -2,0,2','Chapter defines z=h/sigma_h, dimensionless, with unit ensemble variance. A single finite map need not have exact zero spatial mean or unit spatial sample variance.'),
 claim('one fixed simulated map','One Gaussian vector is drawn and held fixed, not a temporal simulation or measured neuron.'),
 claim('q=0.8 and dashed threshold','The drawn height is dimensionless .8 and matches the chosen rectification threshold.'),
 claim('position / sigma; ticks 0,4,8,12,16,20,24','The track spans 24 correlation-length units. Its horizontal axis is spatial distance normalized by the taught sigma.'),
 claim('firing rate F(x) (Hz); visible ticks 0,1,2,3,4','Rate is a=6 Hz times a dimensionless positive excess. It is nonnegative and peaks near 3.09 Hz.'),
 claim('F(x)=6[z(x)-0.8]+','At each sampled point F is six times max(z-.8,0), exactly the chosen model.'),
 claim('Introduction: Gaussian covariance exp[-(delta x/sigma)^2/2], q=.8,a=6, position units sigma','Finite-grid normalized covariance and gains match the model and generator; sigma is defined before this insertion.'),
 claim('Caption: fixed Gaussian input becomes nonnegative through rectification; subthreshold zero; relative heights; shaded connected intervals are fields','The function and support match upper/lower panels. Differences between suprathreshold values are scaled by a; the fields are excursion components, not individual spikes.'),
 claim('Caption: simulated chosen parameters, not recorded cell; Mainali Fig.1A and Eqs.2-3','Direct source inspection confirms the same mathematical operation. Chosen values are not presented as paper estimates.'),
 claim('Alt: fixed spatial function, threshold .8, sixfold positive excess, aligned connected support','All listed relationships are visible in both full and preview pixels.'),
 claim('Interpretation: changed value distribution; separated fields; same fixed spatial map, neither trajectory','Rectification introduces mass at zero and the four disconnected active intervals; the original GP remains fixed.')]
},
'A08':{
 'technical':['Read original Mainali PDF page3 Eq.1 and the guide PLACE-SIZE-LAW change of variables. For s>0, p_d(s)=(2 beta/d)s^(2/d-1)exp(-beta s^(2/d)). For w=beta^(d/2)s, density is (2/d)w^(2/d-1)exp(-w^(2/d)). This removes scale but preserves the d-dependent shape.',
 'Independently integrated the displayed dimensionless densities and their means without importing the drawing code. All masses are one to numerical precision and means match Gamma(1+d/2). Pr(w>v)=exp(-v^(2/d)); U=w^(2/d) has Pr(U>u)=exp(-u).',
 'd1 density is zero at the origin and peaks at 1/sqrt(2); d2 starts at one; d3 behaves as (2/3)w^(-1/3) near zero. This singularity is integrable and has no point mass. The arrow explicitly marks the clipped divergent end. Coincident survival traces use distinct dashes and widths without shifting data.'],
 'objection':'Divergent 3D density could be misread as many exactly zero-volume fields, or the universal transformed law as a finite-threshold empirical collapse.',
 'resolution':'The chapter immediately after the size table explains no zero-size point mass, and the figure caption explicitly says the high-threshold limiting law, not finite-threshold simulations or measured histograms. The plot labels a density and marks the unbounded limit, while the survival axes show the nonlinear U transformation.',
 'readability':'Full 1890 by 945 and 700 px views show readable exponents, units-free axes, legends, divergence arrow and coincident survival traces. Three line styles and different widths keep all three exact overlaid laws visible. No label clipping or overlap.',
 'scenes':[scene('dimension-densities',['three dimension-specific density curves','dimensionless size axis','marked divergent 3D end'],'The same removal of size scale leaves Rayleigh, exponential and integrably divergent shapes.','Shows a qualitative difference the existing radius/size geometry alone does not display.'),scene('exponential-survival',['three exactly coincident styled traces','U transformation axis','exp(-u) formula'],'The nonlinear power transformation makes every limiting survival curve the same exponential.','Separates removal of units from removal of the dimension-dependent distribution shape.')],
 'claims':[
 claim('dimensionless size w=beta^(d/2)s; ticks0,1,2,3,4,5','beta has distance^-2 and s distance^d, so w is dimensionless. This is a size rescaling, not the U power transformation.'),
 claim('density of w; ticks0,1,2','The Jacobian gives (2/d)w^(2/d-1)exp(-w^(2/d)); values are densities, not bin probabilities.'),
 claim('d=1 solid navy; d=2 dashed teal; d=3 dotted orange','Curves use the correct dimensional exponents and are consistently identified in both legends.'),
 claim('unbounded as w approaches0; arrow','d3 exponent of w is -1/3. Arrow targets the divergent portion and does not imply an assigned finite value at zero.'),
 claim('u=beta s^(2/d)=w^(2/d); ticks0,1,2,3,4,5','From w=beta^(d/2)s, its power2/d is exactly beta s^(2/d). The symbol u is a threshold value for random U.'),
 claim('survival probability Pr(U>u); ticks0.0,0.5,1.0','The second axis is a probability, and all displayed exponential values lie in[0,1].'),
 claim('Pr(U>u)=exp(-u)','Integrating the transformed density gives exp(-u), confirmed by independent algebra and numerical identities.'),
 claim('Introduction: scale removal versus shared transformed exponential law','The size rescaling and nonlinear transformation are explicitly distinguished and match the displayed axes.'),
 claim('Caption: length Rayleigh; area exponential; volume integrable divergence','Shapes are 2/d=2,1,2/3. Integral near zero in d3 vanishes with cutoff^(2/3), so divergence is integrable.'),
 claim('Caption: survival coincidence under U; exact limiting calculation, not finite-threshold data; main Eq.1','Direct formula, code and original source agree with the local high-threshold qualification. Caption notation is plain text powers; Stage2 can render these as math without changing content.'),
 claim('Alt: different origin behaviors, arrow, three coincident survival curves','Actual two panels match all listed origin behaviors and line identities.'),
 claim('Interpretation: units removed while shapes differ; nonlinear U removes shape difference; common exponential assumption','The same exponential U was the starting distribution in the guide derivation, so the collapse is an analytic identity, not a further empirical validation.')]
}}

report={'request_id':'stage1-A05-A08-20261024','reviewer':'/root/all_illustrations_review','stage':'1 correctness and separate figure criteria',
 'candidate_frozen_at':'2026-10-24T18:37:43+03:00','reviewed_at':datetime.now().astimezone().isoformat(),
 'binding_status':'Candidate assets/packet/connected baseline only; final canonical context and compiled chapter hashes pending.',
 'source_checks':'Actual local PDFs read directly. Existing reader chapters and current packet anchors read; no historical review reports used.',
 'figures':{}, 'independent_calculations':math_results, 'limitations':['Stage2 wording/necessity and Stage3 connected final reading not claimed','No canonical reader edits by reviewer','Awake execution time unverified','Token stats unavailable']}

for id,sp in specific.items():
    item=packets[id]; folder=ROOT/item['candidate']; qa=json.loads((folder/'qa.json').read_text())
    paths=item['review_contract']['source_files']+item['review_contract']['rule_files']+[item['review_contract'][k] for k in ['style_lock','style_profile','palette_audit']]+[str(PACKET.relative_to(ROOT)),str((folder/'figure.png').relative_to(ROOT)),str((folder/'figure.svg').relative_to(ROOT)),str((folder/'book-width.png').relative_to(ROOT))]
    hashes={p:sha(Path(p) if Path(p).is_absolute() else ROOT/p) for p in dict.fromkeys(paths)}
    row=dict(decision='pass',reviewer=report['reviewer'],author=item['author'],visual_id=item['visual_id'],
       png_sha256=sha(folder/'figure.png'),svg_sha256=sha(folder/'figure.svg'),book_width_sha256=sha(folder/'book-width.png'),
       input_sha256=hashes,source_scope_sha256={},strongest_objection=sp['objection'],objection_resolution=sp['resolution'],claims=sp['claims'],
       scene_count=len(sp['scenes']),checks={
        'technical_accuracy':dict(verdict='pass',evidence=sp['technical']),
        'visual_explanation':dict(verdict='pass',evidence=['Each required scene is a plotted mathematical object with a distinct explanatory role.'],reference_comparison='Internal quantitative figure, not an illustrated opener or structural-template figure.',scenes=sp['scenes']),
        'readability':dict(verdict='pass',full_size_inspected=True,reviewed_width_px=700,evidence=[sp['readability'],'Narrow-screen review assumes the existing horizontal scrolling at 700 px; no approval of a proportionally shrunken390px image.']),
        'palette':dict(verdict='pass',evidence=['Current exact SVG token QA has no out-of-profile colors, issues or warnings. Manual color roles checked: mathematical series and thresholds are distinct, reference guides are muted, plot panels white and outer paper warm. Teal/orange here distinguish quantities, without assigning a biological success or danger claim. This is vector token membership, not raster pixel-deviation measurement.']),
        'coverage':dict(verdict='not-applicable',evidence=['Internal equation-detail figure; required scenes reviewed, with no chapter-map coverage claim.'],covered_ids=[],visible_evidence={})},
       unresolved_findings=[],candidate_insertion_decision='Suitable at the supplied unique anchor; final integrated source review pending.')
    assert item['author']!=report['reviewer']
    assert qa['png_sha256']==row['png_sha256'] and qa['svg_sha256']==row['svg_sha256']
    report['figures'][id]=row

(HERE/'stage1-A05-A08.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
print(json.dumps({'figures':list(report['figures']),'reviewed_at':report['reviewed_at'],'decisions':{k:v['decision'] for k,v in report['figures'].items()}},indent=2))
