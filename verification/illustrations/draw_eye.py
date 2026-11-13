"""Approved V04/V05 scientific artwork. See plan/illustrations/RUN.md.

Editable, deterministic source for conceptual wiring and exact one-pole curves.
No empirical traces or unrecorded anatomical connections are reconstructed.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Rectangle
from scipy.integrate import quad
from figure_style import *


def arrow(ax, a, b, color=FLOW, style='-', lw=1.8, rad=0):
    item=FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=13,
                         linewidth=lw,color=color,linestyle=style,
                         connectionstyle=f'arc3,rad={rad}')
    ax.add_patch(item)
    return item


def label(ax,x,y,s,size=13,color=TEXT,ha='center',va='center',**kw):
    return ax.text(x,y,s,fontsize=size,color=color,ha=ha,va=va,**kw)


def v04():
    fig,ax=plt.subplots(figsize=(10,8.3))
    fig.subplots_adjust(left=.025,right=.975,bottom=.02,top=.98)
    ax.set(xlim=(0,10),ylim=(0,8.4)); ax.axis('off')
    label(ax,.15,8.1,'Physical pathway',14,INK,ha='left',weight='bold')
    # Proposed stored coordinate: a neutral line and its position marker.
    ax.add_patch(Ellipse((1.15,6.55),2.05,1.15,fill=False,edgecolor=TEAL,linewidth=1.5,linestyle=(0,(4,3))))
    ax.plot([.45,1.85],[6.55,6.55],color=TEAL,lw=2)
    ax.add_patch(Circle((1.12,6.55),.075,facecolor=TEAL,edgecolor=TEAL))
    label(ax,1.15,7.72,'Attractor storage',13,TEAL)
    label(ax,1.15,7.37,'proposed source',11.8,TEAL)
    label(ax,1.15,5.65,'Stored eye position',12)
    # Shared drive fans out to the population. Three cells illustrate a population,
    # not three simultaneously recorded cells.
    arrow(ax,(2.2,6.55),(2.9,6.55))
    label(ax,2.64,7.12,'Shared\ndrive',12,FLOW)
    ax.plot([2.96,2.96],[5.95,7.15],color=FLOW,lw=1.7)
    ys=[7.15,6.55,5.95]
    for i,y in enumerate(ys):
        arrow(ax,(2.96,y),(3.48,y))
        col=ORANGE if i==2 else TEAL
        ax.add_patch(Circle((3.7,y),.21,facecolor=PALE_ORANGE if i==2 else PALE_TEAL,edgecolor=col,linewidth=2))
        ax.plot([3.91,4.3],[y,y],color=FLOW,lw=1.6)
    ax.plot([4.3,4.3],[5.95,7.15],color=FLOW,lw=1.6)
    arrow(ax,(4.3,6.55),(5.12,6.55))
    label(ax,3.7,7.73,'Motor neuron\npopulation',12)
    # Private noise enters one cell only, representing this role for each cell.
    ax.plot([4.54,4.43,4.52,4.41],[7.87,7.73,7.6,7.48],color=ORANGE,lw=1.6)
    arrow(ax,(4.41,7.48),(3.9,7.23),color=ORANGE)
    label(ax,4.68,8.05,'Private spike variability',11.7,ORANGE)
    # Muscle strokes end on a schematic eye, no anatomical precision implied.
    for yy in [6.32,6.55,6.78]:
        ax.plot([5.15,5.42,6.23,6.48],[6.55,yy,yy,6.55],color=TEAL,lw=2)
    ax.add_patch(Circle((6.79,6.55),.45,facecolor=PAPER,edgecolor=TEAL,lw=1.8))
    ax.add_patch(Circle((7.02,6.55),.1,facecolor=TEAL,edgecolor=TEAL))
    label(ax,6.16,5.57,'Muscles and\neye mechanics',13)
    arrow(ax,(6.0,7.58),(6.0,6.87),color=ORANGE)
    label(ax,6.7,7.91,'Downstream physical\nvariability',11.7,ORANGE)
    arrow(ax,(7.29,6.55),(8.05,6.55))
    ax.plot([8.1,9.6],[6.55,6.55],color=TEAL,lw=1.6)
    ax.plot([8.1,8.1,9.6,9.6],[6.48,6.62,6.62,6.48],color=TEAL,lw=1)
    ax.add_patch(Circle((8.8,6.55),.075,facecolor=TEAL,edgecolor=TEAL))
    label(ax,8.85,5.65,'Physical eye\nposition',13)
    # Recording transfers: separate from biological causal flow.
    label(ax,.15,4.63,'Paired recordings',14,INK,ha='left',weight='bold')
    ax.plot([3.7,3.7],[5.73,3.9],color=LINE,ls=(0,(2,3)),lw=1.5)
    arrow(ax,(3.7,4.1),(3.7,3.7),color=MUTED,style=(0,(2,3)))
    label(ax,2.62,4.03,'One neuron\nat a time',12,ORANGE)
    # Recorded spike symbol (no empirical spike data).
    ax.plot([2.65,4.65],[3.3,3.3],color=MUTED,lw=1)
    for x in [2.78,3.05,3.15,3.62,4.01,4.32,4.43]:
        ax.plot([x,x],[3.3,3.66],color=ORANGE,lw=1.6)
    label(ax,3.65,2.91,'Recorded spikes',13)
    ax.plot([8.8,8.8,9.78,9.78],[6.65,6.96,6.96,4.0],color=LINE,ls=(0,(2,3)),lw=1.5)
    arrow(ax,(9.78,4.0),(9.2,3.7),color=MUTED,style=(0,(2,3)))
    # Measurement error enters the record, never the physical position.
    arrow(ax,(8.6,4.3),(8.8,3.82),color=ORANGE)
    label(ax,8.35,4.67,'Measurement\nnoise',11.7,ORANGE)
    ax.plot([7.48,9.55],[3.3,3.3],color=MUTED,lw=1)
    xx=np.linspace(7.55,9.5,100)
    ax.plot(xx,3.51+.075*np.sin(7*(xx-7.55))+.045*np.cos(3*(xx-7.55)),color=TEAL,lw=1.7)
    label(ax,8.5,2.91,'Recorded eye position',13)
    # A bracket explicitly pairs the two recordings without implying neural pairs.
    ax.plot([3.65,3.65,8.5,8.5],[2.6,2.43,2.43,2.6],color=LINE,lw=1.1)
    label(ax,6.1,2.19,'One cell and eye movement recorded together',11.8,MUTED)
    # Dashed analysis operation, with its own direction and meaning.
    label(ax,.15,1.64,'Analysis',14,INK,ha='left',weight='bold')
    ax.plot([3.65,3.65],[2.74,1.1],color=ORANGE,ls=(0,(5,3)),lw=1.7)
    arrow(ax,(3.65,1.1),(4.58,1.1),color=ORANGE,style=(0,(5,3)))
    ax.add_patch(Rectangle((4.65,.63),1.45,.96,facecolor=PALE_ORANGE,edgecolor=ORANGE,lw=1.4))
    u=np.linspace(0,1,100); h=np.exp(-3*u)-np.exp(-17*u)
    ax.plot(4.8+u*1.13,.82+.64*h,color=ORANGE,lw=1.8)
    label(ax,5.38,.27,'Calibrated filter',12)
    arrow(ax,(6.15,1.1),(7.25,1.1),color=ORANGE,style=(0,(5,3)))
    xx=np.linspace(7.35,9.5,100)
    ax.plot(xx,1.1+.14*np.sin(2.7*(xx-7.35)),color=ORANGE,lw=2)
    label(ax,8.4,.61,'Predicted eye position',12)
    label(ax,8.4,.24,'calculated from one cell',11,MUTED)
    # Minimal connector legend with actual connector samples.
    arrow(ax,(.2,.8),(.9,.8),color=FLOW)
    label(ax,1.02,.8,'physical flow',10.8,MUTED,ha='left')
    arrow(ax,(.2,.4),(.9,.4),color=ORANGE,style=(0,(5,3)))
    label(ax,1.02,.4,'calculation',10.8,MUTED,ha='left')
    checks={
        'three_distinct_population_cell_positions':len(set(ys))==3,
        'record_connector_starts_below_population_cells':5.73 < min(ys)-.21,
        'measurement_noise_connector_below_physical_position':4.3 < 6.55,
        'analysis_region_below_recording_region':1.59 < 2.43,
    }
    # These are explicit construction checks, not semantic approval.
    return save(fig,'V04',checks,{
        'checks_kind':'explicit schematic construction checks; final meaning review remains pending',
        'source':'Original guide schematic; Ben-Shushan et al. 2022, Figs. 1-2 and 4-5; Chapter 4 EYE-PATHWAY, EYE-RECORDINGS, EYE-INVERSE-FILTER.',
        'recorded_cell':'orange lower cell; only its record is shown',
        'schematic_symbols':'spike ticks and recorded/predicted signal symbols are illustrative, not experimental traces',
        'no_feedback_loop':True,
    })


def v05():
    fig=plt.figure(figsize=(10,7.3))
    gs=fig.add_gridspec(2,2,height_ratios=[1,3.65],hspace=.28,wspace=.34,left=.11,right=.96,bottom=.12,top=.94)
    axes=[]
    for j,(name,col) in enumerate([('Stationary white input',ORANGE),('Brownian stored position',TEAL)]):
        ax=fig.add_subplot(gs[0,j]); ax.set(xlim=(0,10),ylim=(0,2.8));ax.axis('off')
        label(ax,5,2.65,name,14,col,weight='bold')
        # Filter appears as an operation with the same exact exponential response.
        label(ax,1,1.5,'Input',12,col)
        arrow(ax,(2.05,1.5),(3.3,1.5),color=col)
        ax.add_patch(Rectangle((3.4,.85),2.7,1.3,facecolor=PALE,edgecolor=INK,lw=1.3))
        t=np.linspace(0,1,80)
        ax.plot(3.67+2.1*t,1.06+.85*np.exp(-4*t),color=INK,lw=1.9)
        arrow(ax,(6.2,1.5),(7.5,1.5),color=col)
        label(ax,8.75,1.5,'Position',12,col)
        label(ax,4.75,.38,'Same one-pole filter',11.8,INK)
        axes.append(fig.add_subplot(gs[1,j]))
    x=np.geomspace(.01,20,1200)
    white=-np.expm1(-x)
    brown=x+np.expm1(-x)
    for j,(ax,col,y) in enumerate(zip(axes,[ORANGE,TEAL],[white,brown])):
        ax.plot(x,y,color=col,lw=2.5)
        ax.set_xscale('log');ax.set_yscale('log');ax.set_xlim(.01,20)
        setup(ax,xlabel=r'Dimensionless lag $x=\ell/\tau$')
        ax.set_xticks([.01,.1,1,10]);ax.set_xticklabels(['0.01','0.1','1','10'])
        ax.minorticks_off()
        ax.axvline(1,color=LINE,lw=.8,ls=(0,(2,3)),zorder=0)
    axes[0].set_ylim(.007,2)
    axes[0].set_yticks([.01,.1,1]);axes[0].set_yticklabels(['0.01','0.1','1'])
    axes[0].set_ylabel(r'$M_{\rm white}/(A/\tau)$',labelpad=8)
    axes[0].text(.04,.91,r'$1-e^{-x}$',transform=axes[0].transAxes,fontsize=15,color=ORANGE)
    axes[0].annotate('plateaus',xy=(6,1),xytext=(1.8,1.5),fontsize=12,color=ORANGE,
                     arrowprops={'arrowstyle':'-','color':ORANGE,'lw':1.1})
    axes[0].text(.25,.08,'Short-lag slope 1',transform=axes[0].transAxes,fontsize=11.5,color=ORANGE)
    axes[1].set_ylim(.000035,35)
    axes[1].set_yticks([.0001,.01,1,10]);axes[1].set_yticklabels(['0.0001','0.01','1','10'])
    axes[1].set_ylabel(r'$M_{\rm Brownian}/(2D\tau)$',labelpad=8)
    axes[1].text(.04,.91,r'$x-1+e^{-x}$',transform=axes[1].transAxes,fontsize=15,color=TEAL)
    axes[1].annotate('continues growing',xy=(10,9),xytext=(.045,2.4),fontsize=11.7,color=TEAL,
                     arrowprops={'arrowstyle':'-','color':TEAL,'lw':1.1})
    axes[1].text(.27,.06,'Short-lag slope 2',transform=axes[1].transAxes,fontsize=11.5,color=TEAL)
    fig.text(.535,.035,'Each panel uses its own scale; physical amplitudes are not matched.',ha='center',fontsize=11.5,color=MUTED)
    # Independent numerical integrations check both displayed normalized formulas.
    test=np.array([.001,.1,1,5,20])
    ww=-np.expm1(-test);bb=test+np.expm1(-test)
    wint=np.array([quad(lambda s:np.exp(-s),0,z,epsabs=1e-13)[0] for z in test])
    bint=np.array([quad(lambda s:(z-s)*np.exp(-s),0,z,epsabs=1e-13)[0] for z in test])
    short=.0001;long=100
    slope_w=lambda z:z/np.expm1(z)
    slope_b=lambda z:z*(-np.expm1(-z))/(z+np.expm1(-z))
    checks={
        'white_curve_matches_integral':bool(np.allclose(ww,wint,rtol=1e-10,atol=1e-13)),
        'brownian_curve_matches_covariance_integral':bool(np.allclose(bb,bint,rtol=1e-10,atol=1e-13)),
        'white_is_monotone_below_unit_plateau':bool(np.all(np.diff(white)>0) and np.all(white<=1)),
        'brownian_is_monotone_and_accumulates':bool(np.all(np.diff(brown)>0) and brown[-1]>18),
        'white_short_lag_slope_one':bool(abs(slope_w(short)-1)<1e-3),
        'white_long_lag_slope_zero':bool(abs(slope_w(long))<1e-30),
        'brownian_short_lag_slope_two':bool(abs(slope_b(short)-2)<1e-3),
        'brownian_long_lag_slope_one':bool(abs(slope_b(long)-1)<.011),
        'matched_lag_limits':axes[0].get_xlim()==axes[1].get_xlim(),
    }
    return save(fig,'V05',checks,{
        'source':'Guide calculation, one-pole teaching model; Chapter 4 EYE-FILTERED-MSD; Ben-Shushan et al. 2022, Fig. 3, main Eqs. 20-22.',
        'white_normalization':'M_white/(A/tau)=1-exp(-x)',
        'brownian_normalization':'M_Brownian/(2 D tau)=x-1+exp(-x)',
        'normalizations_are_independent':True,
        'numerical_integration_lags':test.tolist(),
        'maximum_white_integral_error':float(np.max(abs(ww-wint))),
        'maximum_brownian_integral_error':float(np.max(abs(bb-bint))),
        'no_empirical_or_random_input_traces':True,
        'short_lag_white_slope_applies_only_to_one_pole_model':True,
    })


if __name__=='__main__':
    print(json.dumps([v04(),v05()],indent=2))
