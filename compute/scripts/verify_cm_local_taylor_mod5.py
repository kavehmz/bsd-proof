"""Independent reproduction of the NEW CM local Taylor calculation.

Uses a different primitive point i*B, a different ideal normal form,
direct Legendre counts, deterministic Frobenius witnesses, and invariant
Taylor flow with Hasse derivatives instead of the author's A+yB recurrence.
The project certificate and script are read only.
"""
from pathlib import Path
import json, hashlib
from math import isqrt, comb, factorial
from fractions import Fraction
from sage.all import GF, EllipticCurve, PolynomialRing

ROOT = Path('/Users/kaveh/bsd-conjecture')
cert_path = ROOT/'compute/data/cm_local_taylor_mod5.json'
author_script = ROOT/'compute/scripts/cm_local_taylor_mod5.py'
cert = json.loads(cert_path.read_text())
assert hashlib.sha256(cert_path.read_bytes()).hexdigest() == '900a9060c40de02e5d541276d358938a7929b6538f4fef23db31f6954462c307'
assert hashlib.sha256(author_script.read_bytes()).hexdigest() == '0fffae4120bc9a2632bc174444832fea0bb3f91450bdc984e594d2ee0e336586'

def mul(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])

def mod_mu(v):
    # mu=78(3+i), O/(3+i)=Z/10 via i -> -3.
    aa,bb=v
    return (aa%78+78*((aa//78-3*(bb//78))%10),bb%78)

def quotient(a,b):
    x,y=mul(a,(b[0],-b[1])); n=b[0]**2+b[1]**2
    assert x%n==0 and y%n==0
    return (x//n,y//n)

def action(P,a,ii):
    if not P:return P
    return a[0]*P+a[1]*P.curve()(-P[0],ii*P[1])

def deterministic_frob(ell):
    # Count points independently, without E.cardinality().
    charsum=0
    for xx in range(ell):
        v=pow((xx**3+39*xx)%ell,(ell-1)//2,ell)
        charsum += -1 if v==ell-1 else v
    trace=-charsum
    aa=trace//2
    assert 2*aa==trace
    bb=isqrt(ell-aa*aa)
    assert aa*aa+bb*bb==ell
    i0=min(i for i in range(ell) if i*i%ell==ell-1)
    base=GF(ell)
    ring=PolynomialRing(base,'v')
    # Build a deterministic quadratic field with a nonsquare constant.
    ns=next(c for c in range(2,ell) if pow(c,(ell-1)//2,ell)==ell-1)
    ext=GF(ell**2,'v',modulus=ring.gen()**2-base(ns))
    v=ext.gen(); ee=EllipticCurve(ext,[0,0,0,39,0])
    for b in range(ell):
        for a in range(ell):
            xx=ext(a)+ext(b)*v
            rhs=xx**3+39*xx
            if not rhs.is_square():continue
            P=ee(xx,rhs.sqrt())
            if not P or not 2*bb*P:continue
            fp=ee(P[0]**ell,P[1]**ell)
            pp=action(P,(aa,bb),ext(i0))==fp
            mm=action(P,(aa,-bb),ext(i0))==fp
            assert pp!=mm
            psi=(aa,bb if pp else -bb)
            weight=pow((psi[0]-3*psi[1])%5,-1,5)
            return dict(ell=ell,trace=trace,i_mod_ell=i0,psi=list(psi),rho_mod5=weight)
    raise RuntimeError('no deterministic witness')

gens=[deterministic_frob(g['ell']) for g in cert['frobenius_generators']]
assert gens==cert['frobenius_generators']
H={mod_mu((1,0)):1}; todo=list(H)
for h in todo:
    for g in gens:
        z=mod_mu(mul(h,g['psi']))
        w=H[h]*g['rho_mod5']%5
        if z in H:assert H[z]==w
        else:H[z]=w;todo.append(z)
assert len(H)==4608
gaussian_units=[(1,0),(-1,0),(0,1),(0,-1)]
assert [u for u in gaussian_units if mod_mu(u) in H]==[(1,0)]
assert H[mod_mu((-1,2))]==2
phi=1
for modulus,norm in [(2,2),(9,9),(13,13),(13,13),(5,5)]:
    pass
unit_order=60840
for qn in [2,9,13,13,5]:
    unit_order=Fraction(unit_order*(qn-1),qn)
assert unit_order==18432
z=(1,0)
for frob_order in range(1,97):
    z=mod_mu(mul(z,(-1,2)))
    if z==(1,0):break
assert frob_order==24
print('Independent counts/Frobenius/subgroup PASS; order 4608, Frobenius order 24',flush=True)

R=PolynomialRing(GF(5),'v')
mod=R(cert['field_modulus'])
assert mod.degree()==24 and mod.is_irreducible()
F=GF(5**24,'v',modulus=mod)
E=EllipticCurve(F,[0,0,0,39,0]); ii=F(3)
def from_coeffs(coeffs):
    return sum((F(c)*F.gen()**j for j,c in enumerate(coeffs)),F(0))
oldB=E(from_coeffs(cert['primitive_point']['x']),from_coeffs(cert['primitive_point']['y']))
B=E(-oldB[0],ii*oldB[1]) # Different Gaussian-unit orbit from the original point.
assert B!=oldB and mod_mu((0,1)) not in H
mu=(234,78)
assert not action(B,mu,ii)
primes=[(1,1),(3,0),(3,2),(3,-2),(-1,-2)]
assert all(action(B,quotient(mu,p),ii) for p in primes)
assert action(B,(-1,2),ii)==E(B[0]**5,B[1]**5)
power=(1,0)
for _ in range(24):power=mul(power,(-1,2))
assert list(power)==cert['frobenius_pi24']
assert list(quotient((power[0]-1,power[1]),mu))==cert['point_projector']
# Independent integer trace recurrence, no set_order or large point count.
tr0,tr1=2,-2
for n in range(2,25):tr0,tr1=tr1,-2*tr1-5*tr0
assert 5**24+1-tr1==cert['curve_order']

P=PolynomialRing(GF(5),'x'); x=P.gen()
f=x**3+4*x; fprime=3*x*x+4
psi3=3*x**4+4*x*x+4
psi4_no_y=x**6+1
psi5=2*f*f*psi4_no_y-psi3**3
psi7=psi5*psi3**3-3*f*f*psi4_no_y**3
assert psi7.degree()==24
assert psi7(-x)==psi7(x)
coeffs=psi7.list()
hasse=[P([comb(i,j)*coeffs[i] for i in range(j,len(coeffs))]) for j in range(5)]

# Direct invariant Taylor flow: x(z)=x+2yz+(3x²+4)z²+4xyz³+2xz⁴ modz⁵.
# Hasse expansion of psi7(x(z)) followed by the truncated logarithm.
def log_derivatives(xx,yy):
    p0,p1,p2,p3,p4=(h(xx) for h in hasse)
    assert p0
    ff=xx**3+4*xx; fp=3*xx*xx+4
    u1=(p1*2*yy)/p0
    u2=(p1*fp+p2*4*ff)/p0
    u3=(p1*4*xx*yy+p2*4*yy*fp+p3*3*ff*yy)/p0
    u4=(p1*2*xx+p2*(fp*fp+xx*ff)+p3*2*ff*fp+p4*ff*ff)/p0
    logs=[u1,u2-u1*u1/F(2),
          u3-u1*u2+u1**3/F(3),
          u4-u1*u3-u2*u2/F(2)+u1*u1*u2-u1**4/F(4)]
    return [F(-12*factorial(j+1))*a for j,a in enumerate(logs)]

ap=[E(0)]
for _ in range(779):ap.append(ap[-1]+B)
IB=E(-B[0],ii*B[1]); bp=[E(0)]
for _ in range(77):bp.append(bp[-1]+IB)
sums=[F(0)]*4; orbit=set()
for (a,b),w in H.items():
    T=ap[a]+bp[b]
    assert T
    xx,yy=T[0],T[1];orbit.add((xx,yy))
    vals=log_derivatives(xx,yy)
    for j in range(4):sums[j]+=F(w)*vals[j]
assert len(orbit)==4608
old_sums=[from_coeffs(c) for c in cert['derivative_sums_mod5']]
assert all(sums[j]==ii**(-(j+1))*old_sums[j] for j in range(4))
assert [bool(s) for s in sums]==[False,True,True,False]
assert all(s**5==3*s for s in sums)
print('Independent invariant-Taylor sums PASS on i*B: zero/nonzero = F,T,T,F',flush=True)

def add_Q(A,B):
    if A is None:return B
    if B is None:return A
    xx,yy=A; xx2,yy2=B
    if xx==xx2 and yy==-yy2:return None
    slope=(3*xx*xx+39)/(2*yy) if A==B else (yy2-yy)/(xx2-xx)
    x3=slope*slope-xx-xx2
    return x3,slope*(xx-x3)-yy
P0=(Fraction(3),Fraction(12));Q0=(Fraction(27),Fraction(144))
PQ=add_Q(P0,Q0)
assert PQ==(Fraction(1,4),Fraction(25,8))
def ord5_int(a):
    a=abs(a); assert a
    n=0
    while a%5==0:a//=5;n+=1
    return n
def ord5(a):
    return ord5_int(a.numerator)-ord5_int(a.denominator)
vals=[]
for name,A in [('64P',P0),('64Q',Q0),('64(P+Q)',PQ)]:
    for _ in range(6):A=add_Q(A,A)
    t=-A[0]/A[1]; vv=ord5(t); vals.append(vv)
    vals_mod={'valuation':vv,'normalized_t_mod5':int((t/Fraction(5**vv)).numerator%5)*pow(int((t/Fraction(5**vv)).denominator%5),-1,5)%5}
    print(name,vals_mod,flush=True)
assert vals==[1,1,2]
def el(z):return [int(c) for c in z.polynomial().list()]
out=dict(author_certificate_sha256=hashlib.sha256(cert_path.read_bytes()).hexdigest(),
         author_script_sha256=hashlib.sha256(author_script.read_bytes()).hexdigest(),
         independent_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         different_point='[i]B, outside the original H orbit',
         point_x=el(B[0]),point_y=el(B[1]),cm_image_order=len(H),
         frobenius_order=frob_order,gaussian_unit_group_order=int(unit_order),
         frobenius_generators=gens,
         derivative_method='invariant Taylor flow and Hasse polynomial expansion, not A+yB recurrence',
         derivative_sums=[el(s) for s in sums],
         nonzero_pattern=[bool(s) for s in sums],
         exact_gaussian_scaling_verified=True,point_t_valuations=vals)
dest=Path('/tmp/cm_local_taylor_independent.json')
dest.write_text(json.dumps(out,indent=2)+'\n')
print('Independent reproduction saved:',dest,flush=True)
