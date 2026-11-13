"""Reproduce V06--V08 from explicit smooth teaching constructions.

Approved exact scientific-vector route. Numeric checks are not independent
semantic acceptance. Root task start: 2026-10-23T21:56:31.9322700+03:00.
"""
from pathlib import Path
import json
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse
from scipy.optimize import brentq
from scipy.integrate import quad
from scipy.ndimage import label, binary_fill_holes
from figure_style import *


def dimension(ax, a, b, y, text, color=TEAL, offset=.055):
    ax.annotate('', xy=(b,y), xytext=(a,y), arrowprops=dict(arrowstyle='<->', color=color, lw=1.3))
    ax.text((a+b)/2,y+offset,text,ha='center',va='bottom',color=color,fontsize=12)


def v06():
    q=.2
    def z(x): return .9*np.cos(np.pi*x/2+.6*np.sin(np.pi*x/4))+.16*np.sin(np.pi*x)+.1*np.cos(np.pi*x/4)
    def dz(x): return -.9*np.sin(np.pi*x/2+.6*np.sin(np.pi*x/4))*(np.pi/2+.15*np.pi*np.cos(np.pi*x/4))+.16*np.pi*np.cos(np.pi*x)-.025*np.pi*np.sin(np.pi*x/4)
    x=np.linspace(0,10,10001); values=z(x)
    roots=[brentq(lambda t:z(t)-q,x[i],x[i+1]) for i in np.where(np.diff(np.sign(values-q)))[0]]
    up=[r for r in roots if dz(r)>0]
    edges=[0]+roots+[10]
    intervals=[(a,b) for a,b in zip(edges[:-1],edges[1:]) if z((a+b)/2)>q]
    fig=plt.figure(figsize=(8.6,7.5)); grid=fig.add_gridspec(2,2,height_ratios=[1.3,1],hspace=.70,wspace=.32)
    ax=fig.add_subplot(grid[0,:]);setup(ax,'position, x','input height, z(x)')
    ax.plot(x,values,color=INK,zorder=3)
    ax.axhline(q,color=ORANGE,lw=1.5,ls='--');ax.text(10.12,q,'q',color=ORANGE,va='center',fontsize=13)
    ax.fill_between(x,q,values,where=values>q,color=PALE_TEAL)
    for a,b in intervals: ax.plot([a,b],[-1.13,-1.13],color=TEAL,lw=7,solid_capstyle='butt')
    for n,r in enumerate(up):
        ax.plot(r,q,marker='^',ms=8,color=ORANGE,zorder=5)
        ax.annotate('upcrossing' if n==0 else 'upcrossing',xy=(r,q),xytext=(r-.22,.93),ha='center',fontsize=11.5,color=ORANGE,
            arrowprops=dict(arrowstyle='-',color=ORANGE,lw=1))
    dimension(ax,intervals[1][0],intervals[1][1],-1.49,'one full field',offset=.06)
    dimension(ax,intervals[0][1],intervals[1][0],-1.49,'gap',color=MUTED,offset=.06)
    ax.text(.08,1.07,'active at left edge',ha='left',fontsize=11.5,color=TEAL)
    ax.annotate('',xy=(.05,.62),xytext=(.7,1.02),arrowprops=dict(arrowstyle='->',color=TEAL,lw=1))
    ax.set(xlim=(-.1,10.38),ylim=(-1.8,1.25),xticks=[0,2,4,6,8,10],yticks=[-1,0,1])
    ax.text(.5,-.31,r'3 fields = 2 upcrossings + 1 active left edge',transform=ax.transAxes,ha='center',fontsize=13,color=INK)
    # Local linear bands at two of this curve's real upcrossing slopes.
    band_checks=[]; local=[]
    eps=.12
    for col,r in enumerate(up):
        a=fig.add_subplot(grid[1,col]);v=float(dz(r)); w=2*eps/v
        t=np.linspace(-.5,.5,101)
        a.axhspan(q-eps,q+eps,color=PALE_ORANGE,zorder=0)
        a.plot(t,q+v*t,color=INK)
        a.axhline(q,color=ORANGE,lw=1.2,ls='--')
        a.vlines([-eps/v,eps/v],q-eps-.12,q+eps,color=LINE,lw=1,ls=':')
        dimension(a,-eps/v,eps/v,q-eps-.12,r'$2\varepsilon/v$',offset=-.14)
        a.set(xlim=(-.5,.5),ylim=(q-.45,q+.52),xticks=[0],xticklabels=[r'$x_0$'],yticks=[q-eps,q,q+eps],yticklabels=[r'$q-\varepsilon$',r'$q$',r'$q+\varepsilon$'])
        a.set_xlabel('position near a crossing',fontsize=11.5)
        a.text(.5,1.07,'shallower slope' if v==min(dz(u) for u in up) else 'steeper slope',transform=a.transAxes,ha='center',fontsize=12,color=INK)
        a.text(.5,-.39,r'$\frac{v}{2\varepsilon}\,\frac{2\varepsilon}{v}=1$',transform=a.transAxes,ha='center',fontsize=15,color=TEAL)
        lo=brentq(lambda t:z(t)-(q-eps),r-.5,r)
        hi=brentq(lambda t:z(t)-(q+eps),r,r+.5)
        real_integral=quad(lambda t:dz(t)/(2*eps),lo,hi)[0]
        band_checks.append(abs(v*w/(2*eps)-1)<1e-12 and abs(real_integral-1)<1e-9)
        local.append({'crossing':float(r),'slope':v,'epsilon':eps,'linear_band_width':w,'weighted_integral':v*w/(2*eps),'actual_curve_band_edges':[lo,hi],'actual_curve_slope_integral':real_integral})
    fig.subplots_adjust(left=.105,right=.94,top=.94,bottom=.15)
    return save(fig,'V06',{'two_upcrossings':len(up)==2,'three_fields':len(intervals)==3,'active_left_endpoint':bool(z(0)>q),'later_fields_complete':all(a>0 and b<10 for a,b in intervals[1:]),'crossings_simple':all(abs(dz(r))>.1 for r in roots),'band_weight_is_one':all(band_checks)},
        {'construction':'z(x)=0.9 cos(pi x/2+0.6 sin(pi x/4))+0.16 sin(pi x)+0.1 cos(pi x/4), 0<=x<=10; q=0.2. Bottom panels are its local tangent approximations.','roots':roots,'upcrossings':up,'active_intervals':intervals,'linear_band_checks':local,'checkpoint':datetime.now().astimezone().isoformat()})


def v07():
    q=4.;eps=.4;sigma=1.;U=q*eps;r=np.sqrt(2)*sigma/q*np.sqrt(U)
    fig=plt.figure(figsize=(8.6,7));g=fig.add_gridspec(2,3,height_ratios=[1.2,1.05],hspace=.67,wspace=.3)
    ax=fig.add_subplot(g[0,:2]);setup(ax,'position relative to peak centre','input height')
    x=np.linspace(-.67,.67,500);z=q+eps-q*x*x/(2*sigma*sigma)
    ax.plot(x,z,color=INK);ax.axhline(q,color=ORANGE,ls='--',lw=1.5)
    ax.fill_between(x,q,z,where=z>q,color=PALE_TEAL)
    ax.vlines([-r,0,r],q-.1,[q,q+eps,q],color=LINE,lw=1,ls=':')
    ax.annotate('',xy=(0,q+eps),xytext=(0,q),arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=1.3))
    ax.text(.035,q+eps/2,r'$\varepsilon$',color=ORANGE,va='center',fontsize=14)
    dimension(ax,-r,r,q-.14,r'full width $2r_*$',offset=-.11)
    ax.set(xlim=(-.7,.7),ylim=(3.68,4.56),xticks=[0],xticklabels=['0'],yticks=[q,q+eps],yticklabels=[r'$q$',r'$q+\varepsilon$'])
    ax.text(.02,1.07,'local high-peak approximation',transform=ax.transAxes,color=MUTED,fontsize=11.5)
    f=fig.add_subplot(g[0,2]);f.axis('off')
    f.text(.05,.78,r'$U=q\varepsilon$',fontsize=15,color=INK)
    f.text(.05,.45,r'$r_*\simeq\frac{\sqrt{2}\sigma}{q}\sqrt{U}$',fontsize=16,color=TEAL)
    f.text(.05,.14,'One radius,\nthree size measures',fontsize=12,color=MUTED,linespacing=1.5)
    for j,d in enumerate([1,2,3]):
        a=fig.add_subplot(g[1,j]);a.set_aspect('equal');a.axis('off');a.set(xlim=(-1.35,1.35),ylim=(-1.9,1.4))
        if d==1:
            a.plot([-1,1],[.35,.35],color=TEAL,lw=7,solid_capstyle='butt');a.plot([-1,1],[.35,.35],linestyle='None',marker='|',color=INK,ms=19,mew=1.5)
            dimension(a,-1,1,-.05,r'$2r_*$',offset=.02)
            formula=r'$s=2r_*$'; power=r'$U=\beta s^2$';word='length (distance)'
        elif d==2:
            a.add_patch(Circle((0,.35),.85,facecolor=PALE_TEAL,edgecolor=TEAL,lw=1.8))
            a.annotate('',xy=(.85,.35),xytext=(0,.35),arrowprops=dict(arrowstyle='->',color=INK,lw=1.3));a.text(.37,.44,r'$r_*$',ha='center',fontsize=12)
            formula=r'$s=\pi r_*^2$';power=r'$U=\beta s$';word='area (distance squared)'
        else:
            a.add_patch(Circle((0,.35),.85,facecolor=PALE_TEAL,edgecolor=TEAL,lw=1.8))
            a.add_patch(Ellipse((0,.35),1.7,.5,facecolor='none',edgecolor=TEAL,lw=1.1))
            a.annotate('',xy=(.85,.35),xytext=(0,.35),arrowprops=dict(arrowstyle='->',color=INK,lw=1.3));a.text(.37,.46,r'$r_*$',ha='center',fontsize=12)
            formula=r'$s=\frac{4\pi}{3}r_*^3$';power=r'$U=\beta s^{2/3}$';word='volume (distance cubed)'
        a.text(0,-.99,formula,ha='center',fontsize=15,color=INK)
        a.text(0,-1.53,power,ha='center',fontsize=14,color=TEAL)
        a.text(0,1.48,word,ha='center',fontsize=11.5,color=MUTED)
    fig.subplots_adjust(left=.1,right=.95,top=.92,bottom=.13)
    fig.text(.5,.055,r'$U=\beta s^{2/d}$: the power is $2$, $1$, or $2/3$ as dimension increases.',ha='center',fontsize=13)
    tests=[]; vals=[]
    for d,vd in [(1,2),(2,np.pi),(3,4*np.pi/3)]:
        s=vd*r**d;beta=q*q/(2*sigma*sigma*vd**(2/d));tests.append(np.isclose(beta*s**(2/d),U));vals.append({'d':d,'size':s,'beta':beta,'recovered_U':beta*s**(2/d)})
    return save(fig,'V07',{'parabola_roots_match_radius':np.isclose(q+eps-q*r*r/(2*sigma*sigma),q).item(),'full_width_twice_radius':np.isclose((r-(-r)),2*r).item(),'dimension_conversion_matches_U':bool(all(tests))},
        {'construction':'Leading high-threshold parabola z(rho)=q+epsilon-q rho^2/(2 sigma^2); schematic interval, disk and ball are the round-region approximation.','q':q,'epsilon':eps,'sigma':sigma,'radius':r,'U':U,'dimensions':vals,'checkpoint':datetime.now().astimezone().isoformat()})


def topology_field(X,Y):
    R=X*X+Y*Y
    Z=.65*np.exp(-(R-1)**2/.08)+.60*np.exp(-X*X/.04-Y*Y/1.1)
    for a in [np.pi/2,7*np.pi/6,11*np.pi/6]:
        Z+=.85*np.exp(-((X-np.cos(a))**2+(Y-np.sin(a))**2)/.12)
    return Z


def v08():
    grid=np.linspace(-1.8,1.8,1001);X,Y=np.meshgrid(grid,grid);Z=topology_field(X,Y)
    qs=[.3,.5,.8,1.0];masks=[Z>q for q in qs];counts=[]
    fig,axs=plt.subplots(1,4,figsize=(8.9,3.6))
    for ax,q,m in zip(axs,qs,masks):
        components=int(label(m)[1]);holes=int(label(binary_fill_holes(m)&~m)[1]);counts.append((components,holes,components-holes))
        ax.contourf(X,Y,Z,levels=[q,float(Z.max()+1)],colors=[PALE_TEAL])
        ax.contour(X,Y,Z,levels=[q],colors=[TEAL],linewidths=1.4)
        ax.set_aspect('equal');ax.set(xlim=(-1.6,1.6),ylim=(-1.6,1.6),xticks=[],yticks=[])
        for side in ax.spines.values():side.set_visible(True);side.set_color(LINE);side.set_linewidth(.8)
        ax.text(.5,1.10,f'q = {q:g}',transform=ax.transAxes,ha='center',fontsize=14,color=INK)
        ax.text(.5,-.12,f'{components} component'+('s' if components!=1 else '')+'\n'+f'{holes} hole'+('s' if holes!=1 else ''),transform=ax.transAxes,ha='center',va='top',fontsize=11.5,linespacing=1.5)
        ax.text(.5,-.48,r'$\chi = $'+str(components-holes).replace('-','−'),transform=ax.transAxes,ha='center',va='top',fontsize=15,color=ORANGE)
    fig.subplots_adjust(left=.035,right=.98,top=.91,bottom=.32,wspace=.15)
    boundary=[not bool(m[0,:].any() or m[-1,:].any() or m[:,0].any() or m[:,-1].any()) for m in masks]
    nested=[bool(np.all(~masks[i+1]|masks[i])) for i in range(3)]
    # Check that counts persist at a different grid resolution.
    g2=np.linspace(-1.8,1.8,701);x2,y2=np.meshgrid(g2,g2);z2=topology_field(x2,y2);check_counts=[]
    for q in qs:
        m=z2>q;c=int(label(m)[1]);h=int(label(binary_fill_holes(m)&~m)[1]);check_counts.append((c,h,c-h))
    return save(fig,'V08',{'masks_nested':all(nested),'all_activity_away_from_domain_edge':all(boundary),'counts_match_expected':counts==[(1,2,-1),(1,1,0),(4,0,4),(3,0,3)],'counts_stable_on_701_and_1001_grids':counts==check_counts},
        {'construction':'z(x,y)=0.65 exp[-(x^2+y^2-1)^2/0.08]+0.60 exp[-x^2/0.04-y^2/1.1]+0.85 sum_a exp[-((x-cos a)^2+(y-sin a)^2)/0.12], a in {pi/2,7pi/6,11pi/6}. A fixed smooth non-Gaussian teaching map.','domain':[-1.8,1.8,-1.8,1.8],'visible_window':[-1.6,1.6,-1.6,1.6],'thresholds':qs,'components_holes_chi':counts,'grid_size':1001,'connectivity':'4-neighbour foreground and binary_fill_holes; counts separately stable on 701 grid. No component or hole touches the domain boundary.','nested_checks':nested,'checkpoint':datetime.now().astimezone().isoformat()})


if __name__=='__main__':
    for make in [v06,v07,v08]:
        d=make();print(d['asset_id'],d['status'],d['checks'],d['text_outside_canvas'])

