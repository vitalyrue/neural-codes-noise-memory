from pathlib import Path
import json, math, numpy as np
from scipy.integrate import quad
root=Path('C:/dev/clsc/burak-papers/guide/verification/teaching-alignment-20261029')
r={}
r['poisson']={'mean':20*.05,'pzero':math.exp(-1),'pooled_sd':math.sqrt(20),'pooled_relative_sd':1/math.sqrt(20),'rate_sd_single':math.sqrt(1)/.05,'rate_sd_population':math.sqrt(20)/(20*.05)}
r['attractor']=[{'rates':(a,b),'x':(a+b)/2-40,'theta':(a-b)/4} for a,b in [(50,30),(53,33),(53,27)]]
r['brownian']={'var_035':2*.02*.35,'rms_035':math.sqrt(2*.02*.35),'arcmin_035':60*math.sqrt(2*.02*.35),'rms_1':math.sqrt(2*.02),'crossing_time':2*.02/.1**2,'variance_at_crossing':.16,'ring_limit':math.pi**2/3}
r['tilted']={'a_over_lambda':.5,'initial':[0,2],'endpoint':[1,0]}
r['inhibition']=[]
for b,tau,theta in [(20,.1,0),(200,.1,0),(200,.1,100)]:
 rates=np.array([(b+theta)/(2*tau),(b-theta)/(2*tau)]); slopes=np.array([1/(2*tau),-1/(2*tau)]);J=float(np.sum(slopes**2/rates));D=float(np.sum(rates)/2)
 r['inhibition'].append({'b':b,'tau':tau,'theta':theta,'rates':rates.tolist(),'J':J,'D':D,'lower_bound':1/(2*tau*tau*J)})
tau=.1;theta=100;r['linear_exponential_converse_counterexample']={'D':theta/(4*tau),'J':2/(tau*theta),'2DJ':(theta/(2*tau))*2/(tau*theta),'tau_inverse_squared':tau**-2}
r['readout']={}
D=.005;J=10000;tau=.1
for alpha in [1,.1]:
 Jo=alpha*J;L=1/math.sqrt(2*D*Jo);v=math.sqrt(2*D/Jo)
 r['readout'][str(alpha)]={'Lstar':L,'limiting_variance':v,'Lnaive':math.sqrt(3)*L,'naive_minimum':2/math.sqrt(3)*v,'storage_T2':2*D*2,'total_T2':2*D*2+v}
r['coth_ratios']=[1/math.tanh(z) for z in [1,2,3]]
r['naive_sd_ratio']=math.sqrt(2/math.sqrt(3))
r['strict_printed_bound']={'2DJ':2*.005*40000,'ideal_term':math.sqrt(2*.005/40000),'2Dtau':2*.005*.1,'ideal_total':.02+math.sqrt(2*.005/40000),'printed_total':2*.005*(2+.1)}
r['finite_bin_vs_continuum']=[]
D=.3;J=4;L=1.2
for n in [100,400]:
 h=L/n;t=np.arange(1,n+1)*h;C=2*D*np.minimum.outer(t,t)+np.eye(n)/(J*h);one=np.ones(n);exact=1/(one@np.linalg.solve(C,one));limit=math.sqrt(2*D/J)/math.tanh(math.sqrt(2*D*J)*L)
 r['finite_bin_vs_continuum'].append({'n':n,'variance_from_covariance_inverse':float(exact),'continuous_formula':limit,'difference':float(exact-limit)})
r['double_integral_min']=quad(lambda t:2*quad(lambda s:s,0,t)[0],0,1.7)[0];r['L3_over_3']=1.7**3/3
(root/'memory-stage1-recomputations.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps(r,indent=2))
