"""Exact local tuning and shared-displacement geometry from Chapter 6."""
from pathlib import Path
import json, sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'verification/illustrations'))
import figure_style as style
style.OUT = ROOT / 'candidate-content/visuals/candidates/20261024-all'

def draw():
    dx = np.linspace(-0.3, 0.3, 501)
    baseline, k1, k2, variance = 10.0, 2.0, -1.0, 0.01
    r1, r2 = baseline+k1*dx, baseline+k2*dx
    fig, axes = plt.subplots(2, 1, figsize=(8.2, 7.5), gridspec_kw={'height_ratios':[1,1.1]})
    fig.subplots_adjust(left=.16, right=.96, top=.90, bottom=.10, hspace=.60)
    ax=axes[0]
    style.setup(ax, r'Position displacement $\delta x$ (m)', 'Expected rate (Hz)')
    ax.plot(dx,r1,color=style.INK,label=r'$f_1$: slope $+2$ Hz/m')
    ax.plot(dx,r2,color=style.TEAL,label=r'$f_2$: slope $-1$ Hz/m')
    ax.axvline(0,color=style.LINE,lw=1,ls=':')
    ax.axvline(.1,color=style.LINE,lw=1,ls='--')
    ax.scatter([0],[10],color=style.MUTED,s=24,zorder=5)
    ax.scatter([.1],[10.2],color=style.INK,s=32,zorder=5)
    ax.scatter([.1],[9.9],color=style.TEAL,s=32,zorder=5)
    ax.annotate(r'$+0.2$ Hz',xy=(.1,10.2),xytext=(.15,10.46),fontsize=11,
                arrowprops={'arrowstyle':'-','color':style.MUTED,'lw':1})
    ax.annotate(r'$-0.1$ Hz',xy=(.1,9.9),xytext=(.15,9.59),fontsize=11,
                arrowprops={'arrowstyle':'-','color':style.MUTED,'lw':1})
    ax.set_xlim(-.3,.3);ax.set_ylim(9.3,10.75)
    ax.set_xticks([-.3,-.1,0,.1,.3]);ax.set_yticks([9.5,10,10.5])
    ax.legend(loc='upper left',ncol=2,frameon=False,bbox_to_anchor=(-.02,1.20),fontsize=10.7)
    ax=axes[1]
    style.setup(ax,r'Rate 1 change $\delta R_1$ (Hz)',r'Rate 2 change $\delta R_2$ (Hz)')
    ax.plot(k1*dx,k2*dx,color=style.INK,label='Common position change only')
    ax.axhline(0,color=style.LINE,lw=1);ax.axvline(0,color=style.LINE,lw=1)
    ax.scatter([0,.2],[0,-.1],color=[style.MUTED,style.INK],s=[24,42],zorder=5)
    ax.plot([.2,.2,0],[0,-.1,-.1],color=style.LINE,ls='--',lw=1)
    ax.annotate(r'$\delta x=+0.1$ m',xy=(.2,-.1),xytext=(.14,.18),fontsize=11,
                arrowprops={'arrowstyle':'-','color':style.MUTED,'lw':1})
    ax.set_xlim(-.65,.65);ax.set_ylim(-.34,.34)
    ax.set_xticks([-.6,-.2,0,.2,.6]);ax.set_yticks([-.3,-.1,0,.1,.3])
    ax.legend(loc='upper left',frameon=False,bbox_to_anchor=(-.02,1.18),fontsize=11)
    checks={
      'positive_rates_in_shown_range':bool(np.min([r1.min(),r2.min()])>0),
      'example_rate_changes':bool(np.allclose([k1*.1,k2*.1],[.2,-.1])),
      'variances_and_covariance':bool(np.allclose([k1*k1*variance,k2*k2*variance,k1*k2*variance],[.04,.01,-.02])),
      'rank_one_covariance':bool(np.isclose(np.linalg.det(variance*np.outer([k1,k2],[k1,k2])),0)),
      'correlation_is_minus_one':bool(np.isclose(k1*k2/abs(k1*k2),-1)),
      'all_points_on_shared_change_line':bool(np.allclose(k2*dx,-.5*k1*dx))}
    result=style.save(fig,'A09',checks,{'role':'two quantitative plots of a chapter calculation',
      'baseline_chosen_for_visualization_Hz':10,'slopes_Hz_per_m':[2,-1],
      'D_m2_per_s':.01,'duration_s':.5,'position_variance_m2':variance,
      'rate_variance_Hz2':[.04,.01],'rate_covariance_Hz2':-.02,'correlation':-1,
      'limits':'Local expected-rate changes from one shared displacement only; no private spike variability or inferred neural connection. Not experimental data.'})
    print(json.dumps({'id':'A09','status':result['status'],'issues':result['issues']}))

if __name__=='__main__':draw()
