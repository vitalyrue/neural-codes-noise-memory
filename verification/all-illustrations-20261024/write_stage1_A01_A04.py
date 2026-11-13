"""Persist the actual independent Stage 1 judgments by /root/all_draw_eye_place.

This script records human/model judgments from viewed pixels and read sources;
it does not infer semantic approval from numerical checks.
"""
from pathlib import Path
import hashlib,json,re,math
from datetime import datetime
import numpy as np
import yaml
from scipy.stats import poisson

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
REVIEWER='/root/all_draw_eye_place'
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def claim(text,evidence):return {'claim':text,'verdict':'correct','evidence':evidence}
def scene(id,objects,relationship,contribution):
    return dict(id=id,depiction='data-representation',visible_objects=objects,relationship=relationship,teaching_contribution=contribution,verdict='pass')

CLAIMS={
'A01':[
 claim('One cell: λ=1; 20 independent cells: λ=20; Δt=.05 s; expected rate per cell20 Hz.','The chapter fixes r=20/s. Hence λ=NrΔt=N for N=1 or20. SI Eq.S43 is the product conditional Poisson likelihood with rate held locally fixed.'),
 claim('No spike: 0.368, with leader ending at the one-cell zero-count stem.','exp(-1)=0.36787944117144233. The leader visibly ends on x=0, y≈.368; the equal-height x=20 stem is the one-spike event.'),
 claim('Means20 Hz; SD20.00 and4.47 Hz.','For K/(NΔt), mean=r and variance=r/(NΔt). Independent full-support sums give means20 and20 Hz and SD20 and4.472135954999574 Hz.'),
 claim('Probability axes, per-cell rate K/(NΔt) (Hz), stems are discrete probabilities.','The one-cell support spacing is20 Hz and the20-cell spacing is1 Hz. Stem heights equal exact Poisson probability masses; no interpolation or density claim is present. Y tick marks0,.2,.4 are common across panels.'),
 claim('Only estimates through100 Hz are drawn.','The current repaired caption matches the stem support0..100. Plot axes extend to103 for margin; this is why the earlier outside-displayed-range phrase was repaired. One-cell shown mass=.9994058151824183; the unshown tail is not renormalized.'),
 claim('Conditional independence concerns fixed modeled rates, not full recurrent trains.','The following chapter paragraph states precisely this qualification. The source main p.1 uses recurrent time-varying Poisson rates and SI p.9 S43 uses the state-conditioned approximation.'),
 claim('Introduction compares distributions on the same per-cell rate scale; interpretation says averaging reduces relative spread.','Both panels use the same x scale and expected rate. SD/mean is1 versus1/sqrt(20)=.2236068. Normalization is supplied explicitly by the axis and caption. Using pooled rate estimate in the interpretation makes this unit conversion direct.'),
 claim('Alt text reports zero probability, discrete spacings, matched means and reduced spread.','All relationships in the alt agree with the viewed stems and the independent numbers above. No inaccessible extra result is claimed.'),
 claim('Navy one-cell and teal pooled-series colors, neutral axes and guides.','Exact SVG token membership was recomputed from the selected profile. Both colors denote alternative plotted conditions and are not success/failure judgments.')],
'A02':[
 claim('Seven zero-drift sample paths with initial displacement zero.','Independent reconstruction from the declared seed uses7×800 independent N(0,.0004) increments at.01 s. Every path starts at0; min/max are -1.04772391976994 and.6570867702845818 deg, within the shown limits.'),
 claim('Dashed ±sqrt(2Dt) envelope and random RMS label.','For the stated Brownian model D=.02 deg²/s, displacement variance is.04t. The envelope is an ensemble RMS scale, not a confidence/hard boundary; sample paths visibly cross it. Caption explicitly says so.'),
 claim('Bias: vt and equal at4 s: .40 deg, with leader at the curves’ crossing.','Solving sqrt(.04t)=.1t for positive t gives4 s and.4 deg. Squaring gives.16 deg² for each separate MSD contribution, consistent with the preceding chapter example.'),
 claim('Time(s), Displacement(deg), Displacement scale(deg), plotted ticks.','Shared x0..8 s; top signed coordinate, bottom nonnegative scale. Bottom tick.8 corresponds vt at8 s; random RMS is sqrt(.32)=.565685 deg there. Units are correct because D has deg²/s and v has deg/s.'),
 claim('Caption says unbounded constructed coordinates and chosen values rather than animal estimates.','Chapter FOUNDATION-DIFFUSION teaches the unbounded/local qualification. The source main p.2 treats local diffusion and removes systematic drift; the guide adds this explicit Brownian/bias teaching example.'),
 claim('A path may turn back despite growing ensemble spread; constant bias eventually exceeds square-root RMS.','Independent increments in the reconstruction have both signs in every path. RMS grows t^.5 and nonzero chosen vt grows t, so the asymptotic comparison is correct for this unbounded example.'),
 claim('Introduction and alt distinguish sample paths from exact scales.','The alt’s path count, signed envelope crossing and crossing location match the full pixels and700px preview. It does not call seven sample paths a measured variance estimate.'),
 claim('Gray sample paths, teal RMS, orange deterministic bias, neutral leader and guide.','The role distinction is consistent across panels; lines and all labels remain separate and legible at700px. No line is cut by the chosen y limits.')],
'A03':[
 claim('r_A baseline5 Hz and r_B baseline25 Hz.','Rates are5+35exp(-θ²/(2×.6²)) and25+the same peak term. Center rates40 and60 spikes/s agree with the first panel; neither rate approaches zero.'),
 claim('Same derivative for both curves, positive left of0 and negative right.','Differentiation gives -θ/.36×35exp(-θ²/.72). Center derivative0. An independent centered finite-difference check differs by at most5.50e-9 in the plotted domain.'),
 claim('Rate(spikes/s), Slope(spikes s^-1 rad^-1), Contribution(rad^-2 s^-1), θ(rad).','Rate derivative is per radian; squared derivative divided by rate has rad^-2 s^-1 treating spike count as a count. This agrees with main Eq.3 and Chapter3’s explicit FI-rate units.'),
 claim('The information contributions vanish at the rate peak and are positive on the flanks.','Computed (r′)^2/r is0 atθ0; the denominator remains strictly positive. Independent maxima over the plotted grid are53.03501906326963 and27.86875194859338, agreeing with the plotted60-unit vertical scale.'),
 claim('Adding constant baseline raises Poisson count noise and reduces local information.','For fixed h, Var(n)=rh increases while r′ is unchanged. Thus every nonzero-slope contribution decreases from j_A to j_B. This is a comparison holding the modulated part fixed, not proportional scaling of the whole rate curve.'),
 claim('Repaired caption uses (r_i^{prime})²/r_i.','Current caption attaches the derivative prime as a superscript. The earlier bare prime is recorded as a resolved notation finding; the plotted curves did not need any change.'),
 claim('Curves are analytic examples, not recorded neurons or a proven recurrent attractor.','The caption explicitly limits the construction. Main Eq.3 is used only for the instantaneous locally fixed positive-rate count model; no connectivity is inferred from the two chosen curves.'),
 claim('Intro, interpretation and alt explain slope relative to noise, not high rate alone.','The preceding proposed passage defines J and its positive-rate assumptions. All three described panels and their ordering agree with actual pixels; color identity from top legend is retained in lower contributions.'),
 claim('Zero θ guide, zero-information marker, top legend and all ticks/labels.','The marker is exactly at(0,0) in the lower panel and the guide aligns rate peak, derivative zero and information zero. Full-size/700px views show the top legend entirely visible and units readable.')],
'A04':[
 claim('b=200 activation units; τ=.1 s; coordinate is activation difference.','Chapter2 states s1=(b+θ)/2,s2=(b−θ)/2 and θ=s1−s2. Rate=s/τ, so r1,2=(200±θ)/.2. This is an activation coordinate rather than radians.'),
 claim('All displayed rates are positive on θ in[-160,160].','The minimum rate is200/s at an endpoint. The full valid interior is|θ|<200; boundaries and negative-rate extensions are excluded in caption and chapter.'),
 claim('J=2000/(40000−θ²), minimum.0500 at0 and.0667 at100.','Rate slopes are±5/s per activation unit. Direct25/r1+25/r2 gives.05 at0,1/15 at100 and.1388889 at160. The annotation leaders end on those points.'),
 claim('Actual D stays1000 activation units²/s.','The neutral projection vector is(1,−1), hence2D=r1+r2=2000/s in this coordinate convention, so D1000 throughout the valid interior. This independently agrees with Chapter2 and the source mutual-inhibition construction.'),
 claim('Lower bound1/(2τ²J), equality at0 and value750 at100.','Main Eq.4/SI S49 give the inequality. Algebra yields1000−θ²/40. Values are1000 at0,750 at100,360 at160. The bound never exceeds actualD over the displayed interval.'),
 claim('Orange vertical segment marks the actual-bound gap atθ100.','Its lower endpoint is750 and upper endpoint1000 atx100. It represents a difference, not an arrow claiming that increasing information caused the actual diffusion to fall.'),
 claim('J(unit^-2 s^-1) and Diffusion(unit²/s), tick and axis labels.','The caption and x label identify unit as activation unit. The reciprocal of τ²J is activation-unit²/s. The shown y ticks and examples are dimensionally consistent.'),
 claim('Caption and interpretation distinguish a lower permitted bound from actual diffusion.','Both explicitly say actual diffusion remains fixed. This avoids treating higher FI as a universal promise of lower observedD. The preceding derivation retains the weak-noise network assumptions.'),
 claim('Alt matches minimumJ, increasing sides, horizontalD and bound gap.','It describes precisely the two plotted panels and the markedθ100 example. No extra empirical or global boundary claim is introduced.'),
 claim('Navy actualD and J, teal lower bound, orange gap and neutral annotation leaders.','Roles match the distinct mathematical objects; all annotation endpoints and700px labels were inspected. No unexplained arrow direction or panel connection is present.')]
}
SCENES={
'A01':[scene('one-cell-count',['Poisson stems','zero-count annotation'],'One-cell mean count1 yields broad rate support and frequent no-spike intervals.','Shows why one silent interval is weak evidence for zero underlying rate.'),scene('pooled-count-normalization',['pooled Poisson stems','shared20Hz guide','rate-normalization axis'],'Twenty independent counts are pooled then normalized to the same expected rate.','Shows lower relative error while preserving the mean and keeping discrete support explicit.')],
'A02':[scene('zero-drift-ensemble',['seven irregular paths','signed RMS curves'],'Independent increments accumulate into irregular paths with a growing ensemble scale.','Separates single-path reversals and excursions from expected spread.'),scene('rms-versus-bias',['square-root RMS curve','linear bias curve','crossing at4s'],'The deterministic displacement catches and then exceeds the random RMS.','Explains why a small persistent bias can dominate long observations.')],
'A03':[scene('rate-and-baseline',['two positive rate hills','baseline legend'],'A constant20Hz shift changes rate but not its changing part.','Holds slope fixed so the effect of baseline noise can be isolated.'),scene('shared-slope',['one signed derivative curve','zero guide'],'Both rate hills have exactly the same local derivative.','Makes peak-versus-flank sensitivity visible.'),scene('individual-information',['two nonnegative double-peaked contributions','zero marker'],'Shared squared slope is divided by each curve’s own rate.','Shows that the higher-baseline curve carries less local Poisson information.')],
'A04':[scene('state-dependent-information',['J curve','two numerical markers'],'Rate imbalance increases local FI away from the balanced state.','Shows state dependence under one fixed network and coordinate convention.'),scene('constant-diffusion-and-lower-bound',['horizontal actualD','curved lower bound','gap segment'],'The lower bound falls while actualD stays constant.','Directly separates inequality slack from actual memory improvement.')]
}
OBJECTIONS={
'A01':('Independence can fail in a recurrent network, so pooling twenty complete spike trains need not obey this law.','Caption says fixed modeled rates; the following original paragraph explains conditional noise independence and recurrent correlations. No empirical independence claim is made.'),
'A02':('Seven trajectories do not establish RMS, and a dashed envelope can be mistaken for a confidence boundary.','RMS is calculated analytically, not estimated from these seven paths. Caption explicitly excludes a path boundary, and visible paths cross it. Long-time unbounded status is explicit.'),
'A03':('Changing a baseline might alter a real attractor or change tuning slopes, so this is not a general circuit intervention result.','The construction holds the changing part fixed, calculates the Poisson FI formula, and disclaims a realized attractor. The conclusion is limited to these analytic positive-rate curves.'),
'A04':('The model uses a coordinate-specific weak-noise diffusion formula, and rates vanish at the boundary.','The source chapter supplies the projection and convention; caption identifies activation units and stays strictly within positive rates. No boundary dynamics or exact finite-spiking process is claimed.')}

def main():
    rows=json.loads((HERE/'foundation-information-integration.json').read_text(encoding='utf-8'))
    # Require the two requested mathematical-caption repairs to have landed.
    assert 'Only estimates through 100 Hz are drawn.' in rows[0]['caption']
    assert '(r_i^{\\prime})^2/r_i' in rows[2]['caption']
    profile=yaml.safe_load(Path(rows[0]['review_contract']['style_profile']).read_text(encoding='utf-8'))
    allowed={v.lower() for v in profile['color'].values()}
    now=datetime.now().astimezone();start=datetime.fromisoformat('2026-10-24T18:31:14.999410+03:00')
    report=dict(stage=1,stage_name='Truth, reasoning and pixels',reviewer=REVIEWER,reviewed_at=now.isoformat(),
       root_wall_elapsed_seconds=(now-start).total_seconds(),awake_execution_time='unverified',
       scope='A01-A04 candidate figures and their current connected proposed insertions; not whole-book acceptance.',
       independence='Reviewer did not author A01-A04 and did not read earlier or other current review verdicts. A05-A08 are excluded because this reviewer authored them.',
       source_evidence=['2012 main PDF pp.1-3, Poisson model, diffusion convention, Eq.3, Eq.4 and Fig.2E-G','2012 SI PDF pp.9-11, S42-S43 and S45-S49','Guide Chapter1 Poisson/diffusion passages; Chapter3 FI/bound passages; Chapter2 mutual-inhibition projection','Current proposed sources and all four briefs; own independent numeric calculations'],
       calculation_method='Direct scipy Poisson sums, independent seeded Brownian reconstruction, finite-difference derivative test, and two-cell projection plus FI algebra. Author generator functions were read but not imported or executed for review.',figures=[])
    for row in rows:
        id=row['id'];contract=row['review_contract'];png=ROOT/row['candidate_png'];svg=ROOT/row['candidate_svg'];qa=json.loads((ROOT/row['qa']).read_text())
        assert sha(png)==qa['png_sha256'] and sha(svg)==qa['svg_sha256']
        colors=set(re.findall(r'(?:fill|stroke):\s*(#[0-9a-fA-F]{6})',svg.read_text(encoding='utf-8')))
        assert all(c.lower() in allowed for c in colors)
        paths=contract['source_files']+contract['rule_files']+[contract['style_lock'],contract['style_profile'],contract['palette_audit']]
        inputs={p:sha(Path(p) if Path(p).is_absolute() else ROOT/p) for p in paths}
        proposed=HERE/'proposed'/row['chapter'];proposed_yaml=proposed.with_suffix('.yaml')
        inputs[str(proposed.relative_to(ROOT))]=sha(proposed)
        inputs[str(proposed_yaml.relative_to(ROOT))]=sha(proposed_yaml)
        text=proposed.read_text(encoding='utf-8');assert '{{block:'+row['visual_id']+'}}' in text
        report['figures'].append(dict(id=id,visual_id=row['visual_id'],decision='pass',reviewer=REVIEWER,
           png_sha256=sha(png),svg_sha256=sha(svg),reviewed_png_sha256=sha(png),reviewed_svg_sha256=sha(svg),reviewed_book_width_sha256=sha(ROOT/row['book_width_preview']),
           reviewed_packet_fields={k:row[k] for k in ['caption','alt','intro','interpretation','source_locator','insert_after']},
           input_sha256=inputs,claim_review=CLAIMS[id],visible_label_inventory=qa['visible_labels'],
           scenes=SCENES[id],strongest_objection=OBJECTIONS[id][0],objection_resolution=OBJECTIONS[id][1],
           criteria=dict(technical_accuracy={'verdict':'pass','evidence':'See individual claim rows and independent calculations.'},
             visual_explanation={'verdict':'pass','evidence':'Each declared scene has visible calculated curves/stems and a specific teaching relation.','scenes':SCENES[id]},
             readability={'verdict':'pass','full_size_inspected':True,'reviewed_width_px':700,'evidence':'Actual original-resolution PNG and separate700px preview inspected. Legends, axes, units, numerical annotations and leader endpoints are visible and do not overlap essential content.'},
             palette={'verdict':'pass','evidence':'Independently recomputed exact SVG color membership against the locked house profile; color roles inspected on actual PNG. This is not a raster deviation audit.','outside_profile':[],'svg_tokens':sorted(colors)},
             coverage={'verdict':'not-applicable','evidence':'Internal equation/example figure, not a chapter opener.'}),
           findings=[],resolved_findings=([{'id':'A01-range','original':'Estimates above100Hz are outside the displayed range.','repair':'Only estimates through100Hz are drawn.','resolution':'Stem support and repaired caption match; axes retain margin.'}] if id=='A01' else [{'id':'A03-prime','original':'Bare prime after r_i in caption.','repair':'Derivative prime explicitly superscripted.','resolution':'Current packet and proposed YAML checked; no artwork change required.'}] if id=='A03' else [])))
    report['findings']=[]
    report['limits']=['This completes Stage1 only. Wording and connected reader-flow stages remain separate.','The artifact ledger’s final review must bind the final canonical sources after integration.','No source or image was edited by this reviewer.']
    (HERE/'stage1-A01-A04.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'at':now.isoformat(),'decisions':{r['id']:r['decision'] for r in report['figures']},'root_wall_elapsed_seconds':report['root_wall_elapsed_seconds']}))

if __name__=='__main__':main()
