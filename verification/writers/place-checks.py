"""Small mathematical checks for chapter 5; no experimental reproduction."""
import json, math, statistics
from datetime import datetime

normal = statistics.NormalDist()
def props(q, sigma):
    Q=normal.cdf(-q)
    nu=math.exp(-q*q/2)/(2*math.pi*sigma)
    return dict(q=q,sigma=sigma,occupancy=Q,density=nu,
                mean_length=Q/nu,mean_gap=(1-Q)/nu,
                rare_mean=math.sqrt(2*math.pi)*sigma/q)

checks=[]
for q in (1.1,2.4,5.0):
    v=props(q,2.4)
    m,g=v['mean_length'],v['mean_gap']
    qi=normal.inv_cdf(g/(m+g))
    si=(m+g)*math.exp(-qi*qi/2)/(2*math.pi)
    assert abs(qi-q)<1e-8 and abs(si-2.4)<1e-8
    v['track_200_expected_fields']=200*v['density']+v['occupancy']
    v['relative_rare_mean_error']=v['rare_mean']/v['mean_length']-1
    checks.append(v)

lam=1.0
observed=lam/(-math.expm1(-lam))
assert abs(observed-1.5819767068693265)<1e-14
conditioned=dict(lam=lam,observed_mean=observed,excluded_fraction=math.exp(-lam))

# Midpoint integration in u=beta*s**(2/d). Exponential tail beyond 30 <1e-13.
laws=[]
N=200000
du=30/N
for d in (1,2,3):
    sigma,q=1.,5.
    vd=math.pi**(d/2)/math.gamma(1+d/2)
    beta=q*q/(2*sigma*sigma*vd**(2/d))
    mean=math.gamma(1+d/2)*beta**(-d/2)
    integral=sum(math.exp(-(i+.5)*du)*du for i in range(N))
    numeric=sum((((i+.5)*du/beta)**(d/2))*math.exp(-(i+.5)*du)*du for i in range(N))
    assert abs(integral-1)<1e-7
    assert abs(numeric/mean-1)<1e-6
    # Mean volume also follows occupancy divided by rare component density.
    geometric=(2*math.pi)**(d/2)*sigma**d/q**d
    assert abs(geometric/mean-1)<1e-12
    laws.append(dict(d=d,beta=beta,mean=mean,numeric_mean=numeric,normalization=integral))

# Exact upcrossing slope density gives same rare length beta as peak geometry.
q,sigma=5.,1.
beta_from_slope=(q/(2*sigma*sigma))**2/(2/sigma**2)
assert beta_from_slope==q*q/(8*sigma*sigma)

# EC low/high level limits for a cube and d=1,2,3.
def ec(q,r,d):
    densities=[normal.cdf(-q),math.exp(-q*q/2)/(2*math.pi),
               q*math.exp(-q*q/2)/(2*math.pi)**1.5,
               (q*q-1)*math.exp(-q*q/2)/(2*math.pi)**2]
    return sum(math.comb(d,j)*r**j*densities[j] for j in range(d+1))
ecs=[]
for d in (1,2,3):
    assert abs(ec(-12,10,d)-1)<1e-20
    assert abs(ec(12,10,d))<1e-25
    ecs.append(dict(d=d,q0=ec(0,10,d),low=ec(-12,10,d),high=ec(12,10,d)))

report=dict(timestamp=datetime.now().astimezone().isoformat(),means=checks,
            conditioned=conditioned,size_laws=laws,ec=ecs,
            corrected_si={'S18':'beta=(Gamma(1+d/2)/mean_s)**(2/d)',
                          'S23':'s=2*sigma*sqrt(2*height/q)',
                          'S25':'exp(-q*height-height**2/2)'})
print(json.dumps(report,indent=2))
