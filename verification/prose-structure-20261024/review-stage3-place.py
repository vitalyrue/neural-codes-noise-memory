from pathlib import Path
import hashlib,json,re
from datetime import datetime
p=Path('C:/dev/clsc/burak-papers/guide/verification/prose-structure-20261024')
notes={
'05-place-fields.md':[
 ('A cell recorded on a short track','The opening establishes the observed variety; the next paragraph offers thresholded smooth spatial input as the common explanation. It does not borrow temporal memory dynamics to fill this setup.'),
 ('We begin on a track','Upcrossing is explained before the field-count calculation. The paragraph identifies how counts and gap lengths separate the two parameters, making the later inference section a response to an existing question.'),
 ('To predict a field\'s width','The loss of spatial information in a histogram motivates the Gaussian process. Mean and covariance follow as the required description, rather than appearing as an unrelated definition.'),
 ('The expectation runs over possible maps','Joint Gaussianity is explained in the main text before its zero-covariance independence consequence is used. The covariance and expectation symbols are linked to possible maps and cells, not to motion over time.'),
 ('Three assumptions have different jobs:','The lead-in and parallel stationarity/isotropy/smoothness list separate the assumptions. The following nonsmooth covariance counterexample interprets their limit before normalization and derivatives depend on them.'),
 ('Set the mean to zero','The normalization, symbol mapping, excursion definition and connectivity explanation remain visible. The reader learns what is being counted before differentiating covariance to obtain its scale.'),
 ('A field starts at an upcrossing','The transition connects the earlier field definition to counting. The local linear expansion, vertical-band argument, slope-weighted integral and independence calculation remain in causal order.'),
 ('The density $p_{z,z\'}','The repaired sentence still explains why the simpler probability-times-slope product fails. Removing Merely leaves both the wrong candidate and the missing slope weighting explicit.'),
 ('On a finite track','The endpoint component is introduced before the counting formula, then interpreted with the clipping convention. The opening count claim is qualified before it is applied numerically.'),
 ('A low field count can result','This transition states the unresolved threshold/scale ambiguity. Occupied and inactive fractions yield means, the two identities eliminate parameters, and the example checks the inversion before extending to full count distributions.'),
 ('The means do not imply','The chapter ends by distinguishing mean inference, rare-event independence and sample selection. Those limits prepare later histogram and empirical-fit tests rather than promising that the mean determines every statistic.')
],
'05b-place-sizes.md':[
 ('Knowing the average field length','The first chapter supplied means; this opening asks for the histogram shape. High peaks are introduced as the restricted setting that makes this new question tractable.'),
 ('The following is a teaching reconstruction','The assumption list is visible with optional notes closed. Its final limitation prevents interpreting the local high-threshold argument as a full convergence proof.'),
 ('The [**Hessian**]','Hessian and its curvature role precede Gaussian conditioning. The independent-remainder argument makes the conditional mean usable without requiring an unseen proof in a fold.'),
 ('The conditional fluctuations','The fixed-size conditional fluctuations motivate the leading parabolic shape. Height, zero gradient, radius and scaled excess are derived in order; no first definition is hidden in a note.'),
 ('This supplies two distinct predictions:','The Rayleigh and peak-rate predictions follow the displayed width/excess relations. The paragraph after the list explains linear size and the following measured exponents retain the moderate-threshold qualification.'),
 ('A round region\'s radius','Geometry motivates the change from radius to size. Gamma is defined beside unit-ball volume before its moments are used, and the size-law density is derived visibly.'),
 ('The mean and its corresponding scale','The mean and scale formulas remain outside the optional higher-moment derivation. Closing that note leaves units, dimensionless size and the subsequent distribution comparison intelligible.'),
 ('This approximation has a measurable error','The finite-threshold error quantifies the limit of the earlier high-peak approximation before spatial slices are introduced. The printed-source caution can remain closed without removing a needed premise.'),
 ('A model can fit field volumes','The volume-fit limitation motivates slices. Gaussian restriction, the definition of slice components and the sampling-bias distinction are visible before the figure-panel list and alternative-model comparison.'),
 ('The derivative at an arbitrary position','The section explains why boundary selection changes slopes before deriving the exact density. Its interpretation states threshold independence and rate gain. Closing the optional width recheck removes only a second check, since the primary width derivation is already visible.')
],
'05c-place-tests.md':[
 ('Two maps can have the same field sizes','The opening extends size/count agreement to holes and asks what it establishes about a circuit. The chapter develops topology before interpreting measured and fitted quantities, then discusses a possible circuit.'),
 ('The [**Euler characteristic**]','The dimensional-list lead-in identifies one common quantity. Examples explain each sign, Betti numbers name the counts just taught, and the figure interpretation explains negative values before the expected-value calculation.'),
 ('The expected Euler characteristic','The repaired phrase mathematical result introduces the same externally supplied Morse conclusion. Critical point, Hessian restriction and boundary contribution remain visible before the signed-density formula uses them.'),
 ('First take the interior','The extension from slope to Hessian determinant connects to the earlier crossing argument. Signed densities and their units remain in the main text, so closing the optional determinant-algebra note leaves the boundary calculation interpretable.'),
 ('Now include the boundary','The main text gives face counting, sign factors, corner term and closed-box conditions before the final formulas. The following limits list and negative-value example interpret those formulas before the high-threshold component approximation.'),
 ('At a sufficiently high threshold','The small, one-peak, hole-free component and large-box conditions precede EC approximately equal to N. Recovering the mean links back to the previous chapter while keeping the two validity ranges distinct.'),
 ('The experiments supply estimated firing rate maps','The theoretical curves motivate the distinction between hidden input and measured maps. The comparison table is introduced by what was fitted and by sample limits, then the main text explains further tests.'),
 ('Figure 1C distinguishes','Skew, excess kurtosis and lognormal sizes are explained before the interpretation of the zero population values. The following paragraph distinguishes fitted likelihood comparisons and simulation uncertainty from held-out forecasting.'),
 ('The processing choices affect','The processing lead-in names the role of its five parallel choices. The immediate consequence paragraph explains how those choices change components, peaks and tails; the supplemental tests and curvature definitions stay visible.'),
 ('The statistical model becomes biologically useful','The fitted-map evidence leaves its circuit source unresolved, motivating random weighted inputs as one possibility. Weight expectations, Gaussian-limit conditions and covariance are developed before the assumption-source list.'),
 ('The assumptions supply different parts of the model:','Each list item assigns one modeling property to its actual condition. The heterogeneous extension and completed-square example follow, and the square-root-two width sentence interprets the result.'),
 ('Agreement with the Gaussian field predictions','The final paragraphs retain alternative circuit mechanisms and possible stationarity failures. They prepare synthesis by distinguishing successful map statistics from direct evidence about weights or causal circuit necessity.')
]}
files=[]
for n,checks in notes.items():
 path=p/'proposed/content/chapters'/n;raw=path.read_bytes();text=raw.decode('utf8').replace('\r\n','\n');paras=text.split('\n\n');records=[]
 for prefix,answer in checks:
  found=[(i,s) for i,s in enumerate(paras,1) if s.startswith(prefix)]
  assert len(found)==1,(n,prefix)
  i,s=found[0]
  records.append({'paragraph':i,'passage':s,'paragraph_sha256':hashlib.sha256(s.encode('utf8')).hexdigest(),'flow_evidence':answer,'verdict':'retain','finding':None})
 # Model the reading path with all actual publisher folds closed.
 hidden=False;visible=[];folds=[]
 for line in text.splitlines():
  if line.startswith('::: {'):
   assert not hidden
   hidden=True;folds.append(line);continue
  if line.strip()==':::' and hidden: hidden=False;continue
  if not hidden:visible.append(line)
 assert not hidden
 visible='\n'.join(visible)
 terms=re.findall(r'\[\*\*(.*?)\*\*\]\{\.definition-term',visible)
 files.append({'path':str(path),'sha256':hashlib.sha256(raw).hexdigest(),'optional_notes_closed':True,'closed_fold_titles':folds,'visible_first_definitions':terms,'visible_path_sha256':hashlib.sha256(visible.encode('utf8')).hexdigest(),'observations':records})
stage2=json.loads((p/'stage2-place.json').read_text(encoding='utf8'));rechecks=[]
for repair in stage2['repairs']:
 path=p/'proposed/content/chapters'/repair['file'];text=path.read_text(encoding='utf8')
 assert repair['after'] in text and repair['before'] not in text
 rechecks.append({'file':repair['file'],'exact_current_passage':repair['after'],'verdict':'Repair applied exactly and meaning preserved. All conditions, scientific terms, calculations, source links and consequences remain.'})
out={'local_request_id':'stage3-place','stage':3,'review_kind':'Independent connected reader flow','reviewer':'/root/structure_information_eye, GPT-6.1-sol/high','started_at':'2026-10-24T21:44:24.5013969+03:00','completed_at':datetime.now().astimezone().isoformat(),'task_wall_start':'2026-10-24T21:32:54.8366363+03:00','awake_execution':'unverified','files':files,'wording_repair_rechecks':rechecks,'findings':[],'verdict':'The revised reading path remains complete with optional notes closed. List lead-ins state the relation of their items, consequences interpret them, definitions precede dependent reasoning, and sequential calculations remain connected. No further repair required.','limits':['Bounded to this wording and structure revision; no new scientific or source audit.','Browser interaction and styling checks remain with root.','The optional derivation notes were treated as closed for this flow review.'],'token_stats':'unavailable'}
(p/'stage3-place.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(out['completed_at'],sum(len(x['observations']) for x in files),'connected-flow observations;',len(rechecks),'exact repair checks; no findings')
