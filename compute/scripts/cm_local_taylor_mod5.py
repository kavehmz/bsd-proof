#!/usr/bin/env python3
"""Exact NEW local theta Taylor test, p=5, opposite-ray level 1.

Run with Sage's Python. This tests nonvanishing of character-weighted
derivative sums; it does not identify an unmarked period with Omega_j.
No BSD conclusion or original c2,p value is inferred.
"""
import json
import hashlib
from pathlib import Path
from sage.all import GF, EllipticCurve, PolynomialRing, ZZ, set_random_seed

set_random_seed(20260913)

def gm(u,v):
    a,b=u; c,d=v
    return (a*c-b*d,a*d+b*c)

def gp(u,n):
    v=(1,0)
    while n:
        if n&1:v=gm(v,u)
        u=gm(u,u); n//=2
    return v

def gdiv(u,v):
    a,b=gm(u,(v[0],-v[1])); n=v[0]**2+v[1]**2
    assert a%n==0 and b%n==0,(u,v,a,b,n)
    return(a//n,b//n)

mu=(234,78) # f0*barpi =39(1+i)^3*(-1-2i)
norm=mu[0]**2+mu[1]**2

def red(u):
    a,b=u; A,B=mu
    q=(a*A+b*B)//norm; r=(b*A-a*B)//norm
    return(a-A*q+B*r,b-B*q-A*r)

def act(P,u,ii):
    a,b=u
    if P.is_zero():return P
    IP=P.curve()(-P[0],ii*P[1])
    return a*P+b*IP

def frobenius_generator(ell):
    f=GF(ell); ec=EllipticCurve(f,[0,0,0,39,0])
    tr=ell+1-int(ec.cardinality()); assert tr%2==0
    aa=tr//2; bb=int(ZZ(ell-aa*aa).sqrt())
    assert aa*aa+bb*bb==ell
    ii=min(f(-1).sqrt(all=True),key=int)
    ff=GF(ell**2,name='v'); ee=ec.change_ring(ff); jj=ff(ii)
    for _ in range(100):
        P=ee.random_point()
        if P.is_zero() or (2*bb*P).is_zero():continue
        FP=ee(P[0]**ell,P[1]**ell)
        plus=act(P,(aa,bb),jj)==FP
        minus=act(P,(aa,-bb),jj)==FP
        assert plus != minus
        ab=(aa,bb if plus else -bb)
        weight=pow((ab[0]-3*ab[1])%5,-1,5)
        return {'ell':ell,'trace':tr,'i_mod_ell':int(ii),'psi':list(ab),'rho_mod5':weight}
    raise RuntimeError('no distinguishing Frobenius witness')

gens=[frobenius_generator(l) for l in [17,29,37,41,53,61,73,89,97,101,109,113]]
H={red((1,0)):1}; queue=list(H); pos=0
while pos<len(queue):
    h=queue[pos]; pos+=1
    for g in gens:
        z=red(gm(h,tuple(g['psi']))); w=H[h]*g['rho_mod5']%5
        if z in H:assert H[z]==w,(z,H[z],w)
        else:H[z]=w;queue.append(z)
assert len(H)==4608,len(H)
units=[(1,0),(-1,0),(0,1),(0,-1)]
assert [u for u in units if red(u) in H]==[(1,0)]

F=GF(5**24,name='v'); E=EllipticCurve(F,[0,0,0,39,0]); ii=F(3)
pi=(-1,2); pi24=gp(pi,24); annihilator=(pi24[0]-1,pi24[1])
quotient=gdiv(annihilator,mu)
order=5**24+1-2*pi24[0]
E.set_order(order,num_checks=0)
factors=[(1,1),(3,0),(3,2),(3,-2),(-1,-2)]
for attempt in range(100):
    B=act(E.random_point(),quotient,ii)
    if B.is_zero():continue
    if not act(B,mu,ii).is_zero():raise RuntimeError('Frobenius annihilator failed')
    if all(not act(B,gdiv(mu,t),ii).is_zero() for t in factors):break
else:raise RuntimeError('no primitive point')
assert act(B,pi,ii)==E(B[0]**5,B[1]**5)

arange=range(min(h[0] for h in H),max(h[0] for h in H)+1)
brange=range(min(h[1] for h in H),max(h[1] for h in H)+1)
IB=E(-B[0],ii*B[1])
ap={a:a*B for a in arange}; bp={b:b*IB for b in brange}
Pr=PolynomialRing(GF(5),'x'); x=Pr.gen(); Fr=Pr.fraction_field()
psi=Pr(EllipticCurve(GF(5),[0,0,0,39,0]).division_polynomial(7))
f=x**3+4*x
A=Fr(0); BB=Fr(-24)*Fr(psi.derivative())/Fr(psi)
derivs=[]
for d in range(1,5):
    derivs.append((A,BB))
    A,BB=Fr(3*x*x+4)*BB+2*Fr(f)*BB.derivative(),2*A.derivative()
sums=[F(0) for _ in derivs]
orbit=set()
for h,w in H.items():
    T=ap[h[0]]+bp[h[1]]
    assert not T.is_zero()
    xx,yy=T[0],T[1]
    orbit.add((xx,yy))
    assert psi(xx)!=0
    for d,(a,b) in enumerate(derivs):
        sums[d]+=F(w)*(a(xx)+yy*b(xx))
assert len(orbit)==4608
# Frobenius permutation and rho(phi)=alpha^-1=2 imply S^5=3S.
assert all(s**5==3*s for s in sums)

def elt(z):return [int(c) for c in z.polynomial().list()]
out={
 'purpose':'New local Taylor coefficient nonvanishing test; no BSD conclusion',
 'p':5,'m':1,'a':7,'mu':list(mu),'norm_mu':norm,
 'pi':list(pi),'i_mod5':3,'field_degree':24,
 'field_modulus':[int(c) for c in F.modulus().list()],
 'frobenius_pi24':list(pi24),'curve_order':order,
 'point_projector':list(quotient),'primitive_point':{'x':elt(B[0]),'y':elt(B[1])},
 'primitive_annihilator_checks':True,'frobenius_generators':gens,
 'primitive_point_frobenius_check':'[pi]B=(x(B)^5,y(B)^5)',
 'cm_image_order':len(H),'image_intersects_gaussian_units_trivially':True,
 'orbit_size':len(orbit),'derivative_sums_mod5':[elt(s) for s in sums],
 'coefficient_nonzero_mod5':[bool(s) for s in sums],
 'frobenius_eigenvalue_check':'S^5=3S for every sum',
 'frame_scope':'C_d differs from the displayed sum by the matched period, q_a^-1 and alpha^-d, all units; only zero/nonzero is asserted invariant under primitive point choice',
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
}
dest=Path('compute/data/cm_local_taylor_mod5.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'cm_image_order':len(H),'orbit_size':len(orbit),'coefficient_nonzero_mod5':out['coefficient_nonzero_mod5'],'output':str(dest)},indent=2),flush=True)
