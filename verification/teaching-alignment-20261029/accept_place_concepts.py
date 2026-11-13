import json,pathlib,re,hashlib
O=pathlib.Path('C:/dev/clsc/burak-papers/guide/verification/teaching-alignment-20261029')
I=json.loads((O/'concept-index-flow-input.json').read_text(encoding='utf-8-sig'))
R=json.loads((O/'final-place-stage3.json').read_text(encoding='utf-8'))
RUN=R['run_id']; passages={p['id']:p for p in I['passages']}
relations=[];sets=[];concepts={}
def relation(c,p,role,evidence,adequacy='adequate',needle=None,need='required'):
    concepts.setdefault(c,{'id':c,'aliases':[]})
    text=passages[p]['text']
    if needle is None:
        spans=[(m.start(),m.end()) for m in re.finditer(r'<!--[\s\S]*?-->',text)]
        start=0;end=len(text)
        while True:
            while start<end and text[start].isspace():start+=1
            hit=next((b for a,b in spans if a==start),None)
            if hit is None:break
            start=hit
        while True:
            while end>start and text[end-1].isspace():end-=1
            hit=next((a for a,b in spans if b==end),None)
            if hit is None:break
            end=hit
    else:start=text.index(needle);end=start+len(needle)
    assert 0<=start<end<=len(text)
    item={'concept_id':c,'passage_id':p,'role':role,'span':[start,end],'status':'reviewed','review':RUN,'evidence':evidence,'passage_sha256':passages[p]['sha256']}
    if role=='teach':item['adequacy']=adequacy
    if role=='use':item['need']=need
    relations.append(item)
def teach(c,p,e,adequacy='adequate',needle=None):relation(c,p,'teach',e,adequacy,needle)
def use(c,p,e,needle=None,need='required'):relation(c,p,'use',e,needle=needle,need=need)
def together(c,ps,e):sets.append({'concept_id':c,'passage_ids':ps,'adequacy':'adequate','status':'reviewed','review':RUN,'evidence':e})

teach('spatial-tuning','ch:FOUNDATIONS/p24','Defines expected rate as a function of represented angle, with baseline/slope units and a nonnegative-rate limit.')
teach('spatial-tuning','ch:FOUNDATIONS/p38','Explains place cells, connected fields and the spikes/time estimator for a spatial rate map, including extraction uncertainty.')
use('spatial-tuning','ch:PLACE-FIELDS/p9','The input interpretation is compared with recordings of firing rates; the earlier map explanation supplies the observed object.')
use('spatial-tuning','ch:PLACE-TESTS/p248','Fixed u_i profiles are rates indexed by position, using the foundations tuning-map meaning.')
use('spatial-tuning','ch:SYNTHESIS/p33','Composing a fixed f_i with x(t) requires the tuning-curve interpretation, explicitly supplied in foundations24.')

teach('poisson-counts','ch:FOUNDATIONS/p51','Names counts over a fixed interval and introduces the adjacent displayed Poisson probability law at lines54-57.','partial')
teach('poisson-counts','ch:FOUNDATIONS/p59','Defines lambda as dimensionless expected count and introduces the adjacent equal-mean/variance identities at61-64.','partial')
together('poisson-counts',['ch:FOUNDATIONS/p51','ch:FOUNDATIONS/p59'],'The setup and adjacent probability/mean displays teach the count law, its parameter and its interpretation before the place chapter conditions it on N>=1.')
use('poisson-counts','ch:PLACE-FIELDS/p229','The rare spatial-event passage extends the count law only under high threshold and decaying dependence, not merely stationarity.')
use('poisson-counts','ch:PLACE-FIELDS/p237','Conditioning observed cells on at least one field needs the already taught count probability and zero probability.')

teach('covariance-and-correlation','ch:FOUNDATIONS/p133','The visible passage explains joint above/below-average changes, normalization by spread and private-noise effects.','partial')
teach('covariance-and-correlation','ch:FOUNDATIONS/p137','Defines centered displacements before the adjacent covariance formula at139-141.','partial')
teach('covariance-and-correlation','ch:FOUNDATIONS/p149','Introduces the adjacent normalized-covariance formula at151-153.','partial')
together('covariance-and-correlation',['ch:FOUNDATIONS/p133','ch:FOUNDATIONS/p137','ch:FOUNDATIONS/p149'],'Visible interpretation plus the mathematical fold defines the centered product and normalized association. The same operations are restated locally in synthesis50 and81.')
use('covariance-and-correlation','ch:PLACE-FIELDS/p23','Covariance describes joint map variation at two positions; the physical interpretation is recalled here before formal functions.')
use('covariance-and-correlation','ch:PLACE-TESTS/p268','Input overlap explains the covariance sum using shared weights at two positions.')
use('covariance-and-correlation','ch:SYNTHESIS/p50','The local centered-product operation derives rate covariance from one shared displacement.')
use('covariance-and-correlation','ch:SYNTHESIS/p81','Correlation minus one is interpreted as opposite changes with one shared source; the earlier normalization gives its meaning.')

teach('diffusion-variance','ch:PERSISTENCE/p90','Gives increment variance2D delta t and units, within the preceding independent zero-mean increment setup.','partial')
teach('diffusion-variance','ch:PERSISTENCE/p102','Uses t=n delta t to state2Dt variance growth and gives Brownian increment assumptions.','partial')
together('diffusion-variance',['ch:PERSISTENCE/p90','ch:PERSISTENCE/p102'],'Independent increments are specified at88-89 and the intervening sum/variance display derives growth. The interpretation and convention precede synthesis.')
use('diffusion-variance','ch:SYNTHESIS/p43','The local displacement variance2Dt is explicitly assumed, with small displacement and fixed x0.')
use('diffusion-variance','ch:SYNTHESIS/p68','The worked example converts D and elapsed time into coordinate variance before rate variance.')

teach('gaussian-process','ch:PLACE-FIELDS/p23','Visible physical teaching describes an ensemble of maps, mean, spatial covariance and a fixed draw.','partial')
teach('gaussian-process','ch:PLACE-FIELDS/p27','The mathematical-definition fold states the finite jointly Gaussian criterion and introduces the mean/covariance functions.','partial')
teach('gaussian-process','ch:PLACE-FIELDS/p36','Explains ensemble averaging, jointly Gaussian vectors and the zero-covariance independence property.','partial')
together('gaussian-process',['ch:PLACE-FIELDS/p23','ch:PLACE-FIELDS/p27','ch:PLACE-FIELDS/p36'],'The visible map interpretation and earlier formal fold jointly define the random function before its distributional properties are used. The visible crossing calculation repeats its needed independence result at157.')
use('gaussian-process','ch:PLACE-FIELDS/p157','The factorization requires jointly Gaussian height and derivative as well as zero covariance; the same sentence supplies the operative rule.')
use('gaussian-process','ch:PLACE-SIZES/p212','Restriction to a line uses the earlier finite-joint definition: selected values remain jointly Gaussian.')
use('gaussian-process','ch:PLACE-TESTS/p254','The finite-vector weighted-sum argument matches the earlier Gaussian-process definition.')

teach('excursion-component','ch:PLACE-FIELDS/p79','Introduces the excursion set; the adjacent set display at81-83 selects positions z>q.','partial')
teach('excursion-component','ch:PLACE-FIELDS/p85','Defines fields as connected pieces, assigns dimension-dependent size and distinguishes peaks from components.','partial')
together('excursion-component',['ch:PLACE-FIELDS/p79','ch:PLACE-FIELDS/p85'],'The set and its connected pieces define the geometric object before boundary counts, slices and topology.')
use('excursion-component','ch:PLACE-FIELDS/p177','The finite-track identity counts intersecting connected components, not just peaks.')
use('excursion-component','ch:PLACE-SIZES/p216','The slice has its own connected intervals or patches; an original component need not remain one piece.')
use('excursion-component','ch:PLACE-TESTS/p13','Changes in connected components and holes require the excursion-set meaning already taught.')

teach('local-spatial-scale','ch:PLACE-FIELDS/p98','Explains the covariance derivative sign and introduces the adjacent definition sigma=sqrt(-C(0)/C double-prime(0)) with normalized slope variance.','partial')
teach('local-spatial-scale','ch:PLACE-FIELDS/p105','Interprets height/slope ratio, units, isotropic direction and the Gaussian covariance example; local scale does not fix all dependence.','partial')
together('local-spatial-scale',['ch:PLACE-FIELDS/p98','ch:PLACE-FIELDS/p105'],'The displayed definition and its interpretation establish both the number and physical distance scale before the crossing density uses it.')
use('local-spatial-scale','ch:PLACE-FIELDS/p157','The derivative variance is sigma^-2, needed for the Gaussian slope integral.')
use('local-spatial-scale','ch:PLACE-SIZES/p28','Isotropy and this local scale determine height-Hessian covariance.')
use('local-spatial-scale','ch:PLACE-TESTS/p286','The circuit interpretation distinguishes normalized spatial width from covariance amplitude.')

teach('crossing-slope-weight','ch:PLACE-FIELDS/p125','Sets a simple regular crossing and linearized height change before the band argument.','partial')
teach('crossing-slope-weight','ch:PLACE-FIELDS/p131','Explains inverse-slope band width and slope multiplication yielding one crossing.','partial')
teach('crossing-slope-weight','ch:PLACE-FIELDS/p139','Interprets the joint density and why a typical slope would miss the correct weighting.','partial')
together('crossing-slope-weight',['ch:PLACE-FIELDS/p125','ch:PLACE-FIELDS/p131','ch:PLACE-FIELDS/p139'],'The local geometry and averaging explanation teach the crossing measure before slope-selected distributions reuse it.')
use('crossing-slope-weight','ch:PLACE-SIZES/p259','The slope-law derivation explicitly retains each v contribution from the crossing integral.')
use('crossing-slope-weight','ch:PLACE-TESTS/p49','The determinant is interpreted as the multidimensional volume conversion analogous to the previously explained slope.')

teach('hessian','ch:PLACE-SIZES/p28','Defines the second-derivative matrix and its principal-curvature meaning before conditioning.')
use('hessian','ch:PLACE-SIZES/p35','The conditional-mean rule is applied to each Hessian entry, using the definition at28.')
use('hessian','ch:PLACE-TESTS/p37','The critical-point theorem requires invertible Hessians, whose matrix and curvature meaning is already taught.')
teach('gaussian-conditioning','ch:PLACE-SIZES/p35','States the conditional-mean rule and derives it by a zero-covariance independent remainder.')
use('gaussian-conditioning','ch:PLACE-SIZES/p43','Relative high-peak curvature fluctuations and gradient conditioning rely on the preceding Gaussian conditioning explanation.')
use('gaussian-conditioning','ch:PLACE-TESTS/p63','The determinant calculation decomposes the conditional Hessian into its mean and centered remainder.')

for cid,pid,why in [
 ('stationarity','ch:PLACE-FIELDS/p47','Translating the observation window preserves the law and gives separation-only covariance.'),
 ('isotropy','ch:PLACE-FIELDS/p50','Rotating separation preserves covariance, independent of the preceding translation condition.'),
 ('sample-smoothness','ch:PLACE-FIELDS/p52','Derivative existence and nondegeneracy are explained with the different requirements of crossings and peaks.')]:teach(cid,pid,why)
use('stationarity','ch:PLACE-FIELDS/p151','The constant-variance derivative justifies zero height-slope covariance.')
use('isotropy','ch:PLACE-SIZES/p28','Rotation symmetry gives the direction-independent height-curvature relationship.')
use('sample-smoothness','ch:PLACE-FIELDS/p125','The local crossing linearization needs differentiability and nonzero slope, explicitly assumed here.')
use('stationarity','ch:PLACE-TESTS/p280','The uniform-input construction is interpreted as supplying spatial stationarity away from boundaries.')

teach('normalization-and-gain','ch:PLACE-FIELDS/p66','Defines unit-variance z, dimensionless q and rate gain a after the displayed normalization and firing rule.')
use('normalization-and-gain','ch:PLACE-FIELDS/p68','The parameter comparison separates input amplitude, threshold and gain effects.')
use('normalization-and-gain','ch:PLACE-TESTS/p139','Converting a firing cutoff t into q+t/a requires the already taught gain units and threshold definition.')

teach('high-peak-excess-and-size','ch:PLACE-SIZES/p45','Sets peak excess and zero gradient before the local parabola and radius displays.','partial')
teach('high-peak-excess-and-size','ch:PLACE-SIZES/p57','Explains the peak-counted tail ratio, rather than using a spatial-point Gaussian tail without weighting.','partial')
teach('high-peak-excess-and-size','ch:PLACE-SIZES/p73','States the exponential scaled excess result and its high-dimensional and proof limits.','partial')
teach('high-peak-excess-and-size','ch:PLACE-SIZES/p79','Defines full width as twice radius and introduces the adjacent square-root-U relation.','partial')
together('high-peak-excess-and-size',['ch:PLACE-SIZES/p45','ch:PLACE-SIZES/p57','ch:PLACE-SIZES/p73','ch:PLACE-SIZES/p79'],'The local parabola, radius, field-counted excess and full-width conversion jointly supply the size-law input. All are visible before the geometric density section.')
use('high-peak-excess-and-size','ch:PLACE-SIZES/p90','The length distribution follows from the already derived scaled square root of an exponential excess.')
use('high-peak-excess-and-size','ch:PLACE-SIZES/p117','The dimensional ball-size conversion uses the preceding radius and U law.')

teach('gamma-function','ch:PLACE-SIZES/p115','Defines gamma by its integral and factorial relation before the unit-ball and mean calculations rely on it.')
use('gamma-function','ch:PLACE-SIZES/p147','The displayed mean and inverse-scale equations use gamma(1+d/2).')
teach('gamma-and-size-moments','ch:PLACE-SIZES/p115','The gamma integral supplies the tool for the size mean.','partial')
teach('gamma-and-size-moments','ch:PLACE-SIZES/p147','The adjacent main-text display supplies the mean and inverse beta formula.','partial')
together('gamma-and-size-moments',['ch:PLACE-SIZES/p115','ch:PLACE-SIZES/p147'],'Gamma definition and visible mean relation are sufficient to interpret and use the numerical mean example. The optional156 derivation supplies normalization and higher moments for checking the steps.')
teach('gamma-and-size-moments','ch:PLACE-SIZES/p156','The optional moment fold uses U substitution and the adjacent integral to derive every positive moment; the main mean was already visible.')
use('gamma-and-size-moments','ch:PLACE-SIZES/p188','The common-q/sigma examples apply the mean across dimensions, using the visible mean and gamma relation.')
teach('weibull-distribution','ch:PLACE-SIZES/p184','Defines survival, scale and shape and explains why the 3D density singularity is not a zero-volume atom.')
relation('weibull-distribution','ch:GLOSSARY/p112','reference','The glossary retrieves the earlier taught distribution; it does not supply the first teaching.')

teach('slice-sampling','ch:PLACE-SIZES/p212','Restriction explains the lower-dimensional Gaussian law and commuting threshold operation.','partial')
teach('slice-sampling','ch:PLACE-SIZES/p222','Explains size-biased hits and off-centre cuts, separating spatial cuts from uniform field selection.','partial')
together('slice-sampling',['ch:PLACE-SIZES/p212','ch:PLACE-SIZES/p222'],'The restriction law and sampling distinction together explain why correct full volumes do not automatically imply correct slice lengths.')
use('slice-sampling','ch:PLACE-SIZES/p242','The spherical alternative is judged by slice distributions beyond its fitted full volumes.')
teach('crossing-slope-law','ch:PLACE-SIZES/p259','Constructs the slope-selected density by normalizing the earlier crossing contribution.','partial')
teach('crossing-slope-law','ch:PLACE-SIZES/p267','Explains height cancellation, exact q independence, downward boundaries and rate gain.','partial')
together('crossing-slope-law',['ch:PLACE-SIZES/p259','ch:PLACE-SIZES/p267'],'The derivation and interpretation establish the exact law before the independent width check.')
use('crossing-slope-law','ch:PLACE-SIZES/p279','The optional width check changes variables in the already derived boundary-slope law.')

for p,e in [('ch:PLACE-TESTS/p17','Names the statistic before cases.'),('ch:PLACE-TESTS/p19','Gives connected interval count in1D.'),('ch:PLACE-TESTS/p21','Uses disks and a ring to explain the negative hole contribution.'),('ch:PLACE-TESTS/p23','Uses ball, tunnel and cavity examples to give3D signs.'),('ch:PLACE-TESTS/p25','Names these counts as Betti numbers after their concrete meaning.')]:teach('euler-and-betti',p,e,'partial')
together('euler-and-betti',['ch:PLACE-TESTS/p17','ch:PLACE-TESTS/p19','ch:PLACE-TESTS/p21','ch:PLACE-TESTS/p23','ch:PLACE-TESTS/p25'],'The dimension-specific examples and count names jointly teach the signed statistic before its negative-value interpretation and formula.')
use('euler-and-betti','ch:PLACE-TESTS/p35','Interprets the negative value in the constructed2D example as more holes than components.')
use('euler-and-betti','ch:PLACE-TESTS/p129','The high-threshold approximation identifies EC with count only when components are solid and hole-free.')
teach('critical-points-and-morse','ch:PLACE-TESTS/p37','Defines critical points and states the signed-count theorem with Hessian and boundary conditions, explicitly without proving it.')
use('critical-points-and-morse','ch:PLACE-TESTS/p39','The Gaussian calculation replaces absolute determinant by its Morse-signed version after the theorem role is stated.')
use('critical-points-and-morse','ch:PLACE-TESTS/p99','The finite-box construction adds face and corner contributions using that boundary-count framework.')

teach('log-size-moments','ch:PLACE-TESTS/p165','Defines centered moments, skew, excess kurtosis and a Gaussian log-size reference before explaining simulated sampling fluctuations.')
use('log-size-moments','ch:PLACE-TESTS/p183','The sensitivity discussion uses log-length moments defined at165.')
teach('curvature-statistics','ch:PLACE-TESTS/p183','Defines average/product principal curvature with sphere/saddle meanings and states they are extra shape measurements.')
relation('curvature-statistics','ch:GLOSSARY/p40','reference','Retrieves the previously explained product of principal curvatures.')
relation('curvature-statistics','ch:GLOSSARY/p64','reference','Retrieves the previously explained average of principal curvatures.')
teach('fitted-versus-tested','ch:PLACE-TESTS/p165','Explains why fitting mean length and gap leaves histogram shape as an additional comparison.','partial')
teach('fitted-versus-tested','ch:PLACE-TESTS/p169','Limits the comparisons to in-sample model selection and cell-matched simulation uncertainty.','partial')
together('fitted-versus-tested',['ch:PLACE-TESTS/p165','ch:PLACE-TESTS/p169'],'The map parameters, added statistics and comparison limits establish how to count empirical support before the synthesis reuses the distinction.')
use('fitted-versus-tested','ch:PLACE-TESTS/p229','The cell-threshold extension identifies both correlations as fitting targets and length/gap distributions as extra comparisons.')
use('fitted-versus-tested','ch:SYNTHESIS/p105','The summary distinguishes fitted arrangement/gain parameters from additional statistics and high-threshold checks.')
teach('random-sum-construction','ch:PLACE-TESTS/p248','Defines profiles, random fixed weights, zero means and the ensemble for the weighted sum.','partial')
teach('random-sum-construction','ch:PLACE-TESTS/p254','Explains the finite-vector Gaussian limit and active-contribution/normalization/no-dominance conditions.','partial')
teach('random-sum-construction','ch:PLACE-TESTS/p268','Interprets spatial covariance through shared weights and input-profile overlap.','partial')
together('random-sum-construction',['ch:PLACE-TESTS/p248','ch:PLACE-TESTS/p254','ch:PLACE-TESTS/p268'],'Roles, Gaussian-limit conditions and overlap interpretation jointly explain the construction before the continuum or biological-identification discussion.')
use('random-sum-construction','ch:PLACE-TESTS/p272','Uniform translated profiles turn the discrete overlap sum into the spatial covariance integral.')
use('random-sum-construction','ch:PLACE-TESTS/p299','The construction is treated as sufficient rather than a unique recovered biological mechanism.')

teach('local-rate-covariance','ch:SYNTHESIS/p33','Sets a hypothetical moving represented coordinate composed with fixed expected-rate functions.','partial')
teach('local-rate-covariance','ch:SYNTHESIS/p43','Defines the local zero-mean2Dt displacement and Taylor approximation conditions.','partial')
teach('local-rate-covariance','ch:SYNTHESIS/p50','Uses centered products and the adjacent equation to convert displacement variance into a slope-product rate covariance.','partial')
teach('local-rate-covariance','ch:SYNTHESIS/p58','Limits the result to expected rates, fixed starting position, small displacements and the isolated shared source.','partial')
together('local-rate-covariance',['ch:SYNTHESIS/p33','ch:SYNTHESIS/p43','ch:SYNTHESIS/p50','ch:SYNTHESIS/p58'],'All physical roles, local assumptions, result and limits precede the optional numerical example; no essential step is supplied only by the fold.')
use('local-rate-covariance','ch:SYNTHESIS/p68','The worked numbers apply the visible general relationship.')
use('local-rate-covariance','ch:SYNTHESIS/p138','The proposed experiment tests the already derived alignment of fluctuation covariance with map slopes.')

teach('path-integration','ch:SYNTHESIS/p121','The local definition says updating a position estimate from movement before describing the velocity-driven grid model.',needle='updating a position estimate from movement.')
use('path-integration','ch:SYNTHESIS/p121','The following model sentence explains the movement-to-state update after its definition.',needle='In its model, velocity drives recurrent population activity, and errors accumulate in the position estimate.')
teach('dendrite','ch:SYNTHESIS/p128','The appositive identifies branching input structures before their electrical events are connected to plasticity.',needle='the branching input structures of neurons,')
use('dendrite','ch:SYNTHESIS/p128','The causal continuation describes what electrical events in those structures can do.',needle='can induce changes in synaptic strength and form CA1 place fields.')

teach('fisher-information-rate','ch:MEMORY-INFORMATION/p17','Visible neural interpretation explains why local rate change relative to spike noise matters for distinguishing nearby values.','partial')
teach('fisher-information-rate','ch:MEMORY-INFORMATION/p40','Defines score as the change of log likelihood and relates its second moment to the count model.','partial')
teach('fisher-information-rate','ch:MEMORY-INFORMATION/p48','Names the expected squared score and divides by observation duration; adjacent display gives the rate.','partial')
together('fisher-information-rate',['ch:MEMORY-INFORMATION/p17','ch:MEMORY-INFORMATION/p40','ch:MEMORY-INFORMATION/p48'],'The physical distinction and mathematical quantity are both taught before synthesis114 asks what a bound test would measure.')
use('fisher-information-rate','ch:SYNTHESIS/p114','The proposed bound comparison requires the appropriate instantaneous information rate as well as diffusion and time constants.')

scope={a['unit_id'].split('::')[1] for a in R['assessments']}
sections={};section_judgments=[]
for s in I['sections']:
    if s['anchor'] not in scope:continue
    a=next(a for a in R['assessments'] if a['unit_id'].endswith('::'+s['anchor']))
    dep=a['fields']['Prerequisites, first use, and first teaching location']['evidence']
    essential=a['fields']['Essential explanation beyond the checklist']
    sections[s['id']]='reviewed'
    section_judgments.append({'section_id':s['id'],'anchor':s['anchor'],'status':'reviewed','review':RUN,'completeness':'adequate','evidence':dep+' Reasoning chain checked: '+essential['reasoning chain'],'passage_ids':s['passage_ids'],'unresolved':[]})
assert len(sections)==22
assert all(0<=r['span'][0]<r['span'][1]<=len(passages[r['passage_id']]['text']) for r in relations)
report={'schema_version':1,'run_id':RUN,'reviewer_id':'/root/accept_place','stage':'understanding_flow','context':'reviewer_continuation','started_at':R['started_at'],'completed_at':None,'input_hash':R['input_hash'],'review_contract_hash':R['review_contract_hash'],'concept_index_input':'concept-index-flow-input.json','concept_index_sha256':hashlib.sha256((O/'concept-index-flow-input.json').read_bytes()).hexdigest(),
 'audience':{'status':'reviewed','description':'Undergraduate calculus, basic probability and linear algebra, as stated at reading-guide74. Neuroscience and the additional random-field, information and filtering ideas are not silently assumed. The two-foundations-then-place route was checked for its needed prior teaching.','assumed_concepts':['undergraduate calculus','basic probability','linear algebra'],'review':RUN,'evidence':'Reading-guide74 and99-105; foundations24/38/51/133-155; persistence86-102. Specific further concepts are taught at the passages below.'},
 'concepts':list(concepts.values()),'sections':sections,'section_judgments':section_judgments,'relations':relations,'teaching_sets':sets,
 'method':'Current connected reading preceded the location-led relation decisions. Neutral leads supplied locations only. Each span selects actual current text, excluding outer hidden controls. Where the concept extractor omits display math, the evidence explicitly identifies the adjacent equation read in the source. A teaching set can combine such prose with its intervening displayed result. Glossary relations are reference-only, not late first teaching.',
 'frontmatter_promise':R['frontmatter_promise'],
 'limits':['This is a bounded group judgment, not review of all unassigned chapters.','The coordinator will merge groups and run the mechanical prerequisite-order check; that check cannot decide teaching adequacy.','Guide pixels remain deferred.'],
 'counts':{'concepts':len(concepts),'relations':len(relations),'teaching_sets':len(sets),'assigned_sections':len(sections)}}
(O/'final-place-concept-judgments.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report['counts']))
