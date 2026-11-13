"""V01: compare time-indexed fluctuations with a fixed spatial tuning map."""
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from figure_style import *

def draw():
    fig=plt.figure(figsize=(8.0,6.8),layout=None)
    grid=fig.add_gridspec(3,2,width_ratios=[3.6,1.6],left=.12,right=.97,top=.96,bottom=.10,hspace=.65,wspace=.19)
    rng=np.random.default_rng(2012)
    t=np.linspace(0,1,121)
    wandering=np.r_[0,np.cumsum(rng.normal(0,.032,120))]
    a=fig.add_subplot(grid[0,0]); setup(a,'Time','Stored value')
    a.plot(t,wandering,color=INK)
    a.axhline(0,color=LINE,lw=1,ls='--')
    a.scatter([0],[0],color=INK,s=24,zorder=4)
    a.set_xticks([]); a.set_yticks([])
    a.text(.03,.9,'Value wanders over time',transform=a.transAxes,fontsize=11.5,color=INK)
    a.set_xlim(0,1); a.set_ylim(wandering.min()-.12,wandering.max()+.20)
    n=fig.add_subplot(grid[0,1]); n.axis('off')
    n.text(0,.7,'How quickly is\nmemory lost?',fontsize=13,color=INK,va='top',weight='bold')
    n.text(0,.15,'2012 paper\nChapters 3–6',fontsize=11,color=MUTED,va='top')

    a=fig.add_subplot(grid[1,0]); a.set_xlim(0,10); a.set_ylim(0,3); a.axis('off')
    a.plot(np.linspace(.3,2.4,121),1.3+wandering,color=INK)
    a.text(1.3,2.45,'Command',ha='center',fontsize=11.5,color=INK)
    a.annotate('',xy=(4.1,1.45),xytext=(2.8,1.45),arrowprops={'arrowstyle':'->','color':TEAL,'linestyle':'--','lw':2.1})
    a.text(3.45,2.0,'proposed',ha='center',fontsize=10.5,color=TEAL)
    for y in [.95,1.35,1.75]:
        a.plot([4.4,5.5],[y,y+.12],color=TEAL,lw=3.5,solid_capstyle='round')
    a.text(4.95,.28,'Muscles',ha='center',fontsize=11.5)
    a.annotate('',xy=(7.5,1.45),xytext=(5.9,1.45),arrowprops={'arrowstyle':'->','color':TEAL,'lw':2.1})
    a.add_patch(Ellipse((8.45,1.45),1.35,1.50,edgecolor=INK,facecolor=PALE,lw=1.6))
    a.add_patch(Ellipse((8.75,1.45),.28,.8,edgecolor=INK,facecolor=TEAL,lw=1.3))
    a.plot([8.4,9.5],[1.45,1.95],color=INK,lw=1.6)
    a.text(8.5,.28,'Eye position',ha='center',fontsize=11.5)
    n=fig.add_subplot(grid[1,1]); n.axis('off')
    n.text(0,.7,'Where does eye\ndrift begin?',fontsize=13,color=INK,va='top',weight='bold')
    n.text(0,.15,'2022 paper\nChapters 7–9',fontsize=11,color=MUTED,va='top')

    a=fig.add_subplot(grid[2,0]); setup(a,'Physical position','Expected rate')
    x=np.linspace(0,10,601)
    rate=1.5*np.exp(-((x-2.8)/.8)**2)+2.1*np.exp(-((x-7.3)/1.2)**2)
    a.plot(x,rate,color=TEAL)
    p=2.8; r=float(np.interp(p,x,rate))
    a.scatter([p],[r],color=ORANGE,s=35,zorder=5)
    a.annotate('Same place, same rate\non two visits',xy=(p,r),xytext=(4.25,1.90),fontsize=10.5,
        arrowprops={'arrowstyle':'-','color':MUTED,'lw':1},ha='left',color=TEXT)
    a.set_xticks([]);a.set_yticks([]);a.set_xlim(0,10);a.set_ylim(0,2.65)
    n=fig.add_subplot(grid[2,1]);n.axis('off')
    n.text(0,.7,'Why these field\nsizes and shapes?',fontsize=13,color=INK,va='top',weight='bold')
    n.text(0,.15,'2025 paper\nChapters 10–12',fontsize=11,color=MUTED,va='top')
    return save(fig,'V01',{'spatial_curve_finite':bool(np.isfinite(rate).all()),
        'temporal_curve_finite':bool(np.isfinite(wandering).all())},
        {'role':'comparison inside foundations, not an opening map','trace':'one illustrative random walk, seed2012',
         'spatial_curve':'constructed smooth fixed expected-rate curve, not a GP sample or data',
         'arrow_semantics':'dashed proposed changing command; solid muscle-to-eye mechanical action'})

if __name__=='__main__':
    result=draw()
    record=[{
      'id':'V01','visual_id':'fig:FOUNDATIONS-PAPER-MAP','stem':'01-foundations',
      'placement':'sec:FOUNDATIONS-RANDOMNESS',
      'anchor':'The following chapters develop the dynamical calculation first, then the experiment that tests a possible consequence, and finally the spatial statistics.[^f-place]',
      'intro':'The three questions can now be placed beside the kind of variation each paper studies.',
      'caption':'Memory loss and eye drift concern changes over time; place-field statistics concern variation across a fixed spatial map. The eye pathway shows the proposed changing-command mechanism. Original guide schematic based on the three papers, with illustrative traces rather than recorded data.',
      'alt':'Three separate rows compare a wandering stored value over time, a proposed changing command passing through muscles to eye position, and one fixed spatial rate curve evaluated twice at the same place. They link to the 2012 memory, 2022 eye-drift and 2025 place-field papers respectively.',
      'interpretation':'The rows compare different questions; they do not establish a single circuit connecting all three papers.',
      'author':'/root','candidate':'candidate-content/visuals/candidates/20261023/V01',
      'source_locator':'Foundations footnotes f-memory, f-eye and f-place; each identifies the corresponding paper and figure-reading scope.'
    }]
    (ROOT/'verification/illustrations/orientation-integration.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
