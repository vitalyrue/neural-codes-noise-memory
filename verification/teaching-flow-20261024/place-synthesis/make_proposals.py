from pathlib import Path
import re, json, hashlib, difflib, yaml
from datetime import datetime

TASK = Path(__file__).resolve().parents[1]
BASE = TASK / 'baseline' / 'content' / 'chapters'
OUT = TASK / 'proposed' / 'content' / 'chapters'
HERE = Path(__file__).resolve().parent
OUT.mkdir(parents=True, exist_ok=True)
def sha(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
changes=[]
titles=[]
folds=[]

# Each decision is local to the corresponding complete section, not a word rule.
DECISIONS = {
'ch:PLACE-FIELDS': ('A thresholded Gaussian map predicts field sizes and shapes', 'The whole chapter connects one spatial-input model to sizes, slices, slopes and topology; its opening limits this to distributions, not field locations.'),
'sec:PLACE-GP': ('Thresholding a smooth Gaussian input produces place fields', 'The section defines the probability law, covariance, assumptions, normalization and connected active regions; the heading states the model transformation.'),
'sec:PLACE-KAC-RICE': ('Upcrossings count fields, with an endpoint correction', 'The crossing identity and finite-track equation establish this exact count under the stated regularity and counting convention.'),
'sec:PLACE-INFERENCE': ('Mean field and gap lengths separate threshold from scale', 'The two stationary mean formulas lead to separate inversions for q and sigma; the finite-sample and selection caveats remain visible.'),
'sec:PLACE-RARE-PEAKS': (None, 'The existing title already states the learned limiting shape; the section explains why relative curvature fluctuations vanish at high threshold.'),
'sec:PLACE-SIZE-LAW': ('Geometry gives different size laws in each dimension', 'The ball-volume conversion and change of variables explain why the limiting length, area and volume histograms differ.'),
'sec:PLACE-SLICES': ('Slices test spatial structure beyond field volume', 'Gaussian restriction and the spherical-field comparison show what the slice measurements add after volume fitting.'),
'sec:PLACE-SLOPES': (None, 'The existing title states the derived law; the visible explanation keeps the crossing-selection weighting and exact-model conditions.'),
'sec:PLACE-TOPOLOGY': ('Holes distinguish maps with the same field count', 'The opening counterexample and Euler characteristic explain the extra observable; the title avoids equating signed topology with positive counts.'),
'sec:PLACE-DATA': (None, 'The existing title is the section contribution: it distinguishes fitted summaries, extra comparisons and processing choices.'),
'sec:PLACE-WIRING': ('Random input weights can generate Gaussian maps', 'The weighted-sum model and central-limit conditions give a sufficient mechanism; can preserves the visible non-uniqueness limit.'),
'ch:SYNTHESIS': ('Spatial maps and memory dynamics need separate tests', 'The chapter separates the three claims, derives one possible connection and proposes measurements that would test it.'),
'sec:SYNTHESIS-QUESTIONS': ('The three papers constrain maps, dynamics, and movement', 'The section attaches each question to its mathematical object and observable; it preserves the difference between memory state and physical location.'),
'sec:SYNTHESIS-JOINT-CALCULATION': (None, 'The existing title states what the construction teaches: time-varying rates arise when a moving estimate passes through fixed maps.'),
'sec:SYNTHESIS-COVARIANCE-EXAMPLE': (None, 'The example title gives its concrete learned result; opposite slopes explain negative covariance without implying inhibition.'),
'sec:SYNTHESIS-EVIDENCE': ('Each model needs a test matched to its claim', 'The section contrasts extra spatial predictions, shared movement covariance and a mathematical inequality, rather than suggesting one test fits all three.'),
'sec:SYNTHESIS-RELATED': ('Related studies change assumptions and leave circuit choices open', 'Each paragraph identifies what nearby research adds or changes, while preserving what the three main papers have not uniquely measured.'),
'sec:SYNTHESIS-NEXT': ('A joint test would compare tuning maps with population fluctuations', 'The proposed procedure measures both maps and dynamical alignment; would makes the unperformed status explicit.'),
}

def replace_one(text, old, new, file, reason, kind='connection'):
    assert text.count(old)==1, (file,old[:90],text.count(old))
    changes.append(dict(file=file,kind=kind,before=old,after=new,reason=reason))
    return text.replace(old,new,1)

def fold_span(text, start, end, title, file, why, visible, later, destination=None):
    i=text.index(start); j=text.index(end,i)+len(end)
    body=text[i:j]
    assert '{{block:' not in body and 'definition-term' not in body
    assert not re.search(r'^#{1,6} ',body,re.M)
    wrapper='::: {.publisher-clarification-note .publisher-fold-always title="'+title+'"}\n\n'+body+'\n\n:::'
    if destination is None:
        result=text[:i]+wrapper+text[j:]
    else:
        remainder=text[:i]+text[j:]
        k=remainder.index(destination)+len(destination)
        result=remainder[:k]+'\n\n'+wrapper+remainder[k:]
    folds.append(dict(file=file,title=title,source_start=start,source_end=end,exact_body=body,body_sha256=sha(body),visible_premise_result_conditions=visible,later_dependent_uses=later,closed_path_reason=why,moved_after=destination))
    changes.append(dict(file=file,kind='fold' if destination is None else 'move-and-fold',before=body,after=wrapper,reason=why,moved_after=destination))
    return result

for stem in ['05-place-fields','06-synthesis']:
    fn=stem+'.md'; original=(BASE/fn).read_text(encoding='utf-8'); text=original
    for m in list(re.finditer(r'^(#{1,6}) (.+) \{#([^}]+)\}$',original,re.M)):
        level,old,ident=m.groups(); new,reason=DECISIONS[ident]; new=new or old
        titles.append(dict(file=fn,id=ident,old=old,new=new,decision='retain' if old==new else 'change',contribution=reason,support='Complete section at baseline lines '+str(original[:m.start()].count('\n')+1)+' onward.'))
        if old!=new: text=replace_one(text,m.group(0),f'{level} {new} {{#{ident}}}',fn,reason,'title')
    if stem=='05-place-fields':
        # Secondary derivation follows the visible mean formula, so closing it
        # leaves the result, its units and the shortest numeric comparison intact.
        text=replace_one(text,'In particular,\n\n$$\n\\mu_s=', 'The mean and its corresponding scale are\n\n$$\n\\mu_s=',fn,'The general moment proof moves behind the mean, so replace a connector that otherwise points backward to hidden material.')
        dest='\\beta=\\left[\\frac{\\Gamma(1+d/2)}{\\mu_s}\\right]^{2/d}.\n$$'
        text=fold_span(text,'Normalization needs no special integral:', '=\\beta^{-kd/2}\\Gamma(1+kd/2).\n$$','Derivation: normalization and higher size moments',fn,'The limiting density, U transformation and mean formula stay visible; later units, dimensionless curves and mean examples need those formulas, not the general kth-moment integral.','High-threshold conditions and size law are visible above; the mean/scale equations precede the fold.','Units; dimensionless size; numeric means and approximation error.',dest)
        text=fold_span(text,'**Reading the supplement carefully.**','they do not establish that the simulation code or empirical fits used the same mistakes.[^p3-corrections]','Source check: three printed steps in the supplement',fn,'The corrected derivation, exact-versus-asymptotic distinction and numerical error remain visible. The printed-step comparison is an optional source check, and no following argument requires its text.','The reconstructed argument was labeled before derivation and the corrected size-law constants have been derived visibly.','No later dependency on the printed-step comparison.')
        text=fold_span(text,'There is also an independent check on the high threshold width constant.','the same constant as the peak calculation for $v_1=2$.','Independent check: recover field width from its boundary slope',fn,'The visible peak argument already establishes the width constant, and the exact crossing-slope law is taught just before this fold. The later measurement paragraph requires only the slope law.','Smooth stationary Gaussian conditions, Rayleigh crossing slopes, and high-threshold peak/width result are visible.','Finite-difference slope measurement; no use of the alternative proof.')
        # State eta before its optional Gaussian algebra, preserving all steps.
        old='For example, differentiate $-q\\phi(q)$ to get $(q^2-1)\\phi(q)$, which verifies the second integral using its vanishing upper endpoint. Combining the determinant, gradient density, and integral yields'
        new='For example, differentiate $-q\\phi(q)$ to get $(q^2-1)\\phi(q)$, which verifies the second integral using its vanishing upper endpoint. Combining the determinant, gradient density, and integral gives the signed densities above.'
        text=replace_one(text,old,new,fn,'The optional Gaussian algebra moves after its result. Point its final sentence to that visible result.')
        dest='These are signed densities per length, area, and volume, not three formulas for positive field counts.'
        text=fold_span(text,'Here are the Gaussian algebra steps behind the determinant average.',new,'Derivation: the Gaussian determinant average and its integrals',fn,'The signed-count mechanism, assumptions, eta integral, resulting eta formulas and signed-density meaning stay visible. Boundary factors use eta values, not the canceled fourth-derivative constant or determinant expansion.','Smooth compact-domain critical-point assumptions, signed Kac-Rice expression, phi and lambda, and all three eta formulas appear before the fold.','Box face factors; exact box expectations; high-threshold count approximation; cutoff interpretation.',dest)
        # Keep an explicit visible lead into eta after moving the original lead.
        marker='$$\n\\eta_1=\\frac{e^{-q^2/2}}{2\\pi\\sigma},'
        text=replace_one(text,marker,'The resulting signed densities are\n\n'+marker,fn,'The moved derivation previously supplied the lead into eta. Supply that connection on the visible reading path.')
    (OUT/fn).write_text(text,encoding='utf-8',newline='\n')
    # Patch only title scalar lines; preserve every original block byte for byte.
    yfn=stem+'.yaml'; ytext=(BASE/yfn).read_text(encoding='utf-8')
    data=yaml.safe_load(ytext)
    for row in titles:
        if row['file']!=fn or row['decision']=='retain': continue
        if row['id'].startswith('ch:'):
            old='title: '+data['title']; new='title: '+row['new']
        else:
            sec=next(s for s in data['section_list'] if s['id']==row['id'])
            old='  title: '+sec['title']; new='  title: '+row['new']
        ytext=replace_one(ytext,old,new,yfn,'Match the individually reviewed Markdown title.','sidecar-title')
    # Summaries are unchanged first paragraphs and still match the source.
    assert ytext.split('blocks:\n',1)[1]==(BASE/yfn).read_text(encoding='utf-8').split('blocks:\n',1)[1]
    yaml.safe_load(ytext)
    (OUT/yfn).write_text(ytext,encoding='utf-8',newline='\n')
    (HERE/(stem+'.diff')).write_text(''.join(difflib.unified_diff(original.splitlines(True),text.splitlines(True),fromfile='baseline/'+fn,tofile='proposed/'+fn)),encoding='utf-8')

(HERE/'title-decisions.json').write_text(json.dumps(titles,ensure_ascii=False,indent=2),encoding='utf-8')
(HERE/'fold-decisions.json').write_text(json.dumps(folds,ensure_ascii=False,indent=2),encoding='utf-8')
(HERE/'exact-changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'titles':len(titles),'changed_titles':sum(r['decision']=='change' for r in titles),'folds':len(folds),'outputs':[str(p) for p in OUT.glob('0[56]-*')]}))
