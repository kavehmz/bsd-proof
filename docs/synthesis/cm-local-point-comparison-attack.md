# The exact local CM point map and its Taylor coefficients

Date:2026-09-13. Author: root/coordinator. **All six sections independently reviewed.**
[Restart](cm-local-point-comparison-checkpoint.md).
Full BSD over Q remains active and unresolved. The companion
[asymmetric construction](cm-asymmetric-ray-attack.md) and its norm/local
inputs have passed review. The core proof has a separate
[five-section PASS](review-cm-local-point-comparison.md), and §6 has its
own [arithmetic PASS](review-cm-local-taylor-certificate.md), including the
additional refinement proved in that review's §8. No global nonvanishing
or BSD comparison is inferred from the local conclusion.

## 1. Original data and an exact local Tate frame

Keep E:y²=x³+39x, omega=dx/(2y), the original good split prime range,
p=pi barpi, and the completion K_pi=Qp. Write alpha=barpi in this
completion, an ordinary p-adic unit. The opposite ray field is
B_m=K(f barp^m), and beta_m=Omega_infinity/(f0 barpi^m).
All original conductor, character and primitive-ray conventions remain.
Set

    Theta_a=Delta_E^(a²-1) psi_a^-12,
    rho=(Psi^c)^-1,  q_a=12(a²-u_a),  u_a=Psi^c((a))=±a,

with a=5 except a=7 at p=5. Thus q_a is a p-unit. It is the original
Kato scalar normalization, not the point-isogeny smoothing operator.

Let W be the ring of integers of the completed maximal unramified
extension of Qp. The actual formal group Ehat has height1 and admits
an integral isomorphism to Gmhat over W. In the notation of
[Bannai–Kobayashi math/0610163v4, §3.1](https://arxiv.org/html/math/0610163v4#S3.SS1),
such an isomorphism has the form

    eta(t)=exp(log_E(t)/Omega_eta)-1,  Omega_eta in W^times.

Here and below a composition of formal series is evaluated only in its
justified convergence domain. In particular one cannot substitute a
connected p-power torsion point into a nested exponential/logarithm and
deduce that the integral formal isomorphism sends it to1.

We MATCH this isomorphism to the ORIGINAL coefficient identification
j:Zp(1) tensor Zp(rho)->T_pi and its prescribed basis t_rho.
Choose eta_j so its inverse on compatible p-power roots of unity is
exactly zeta->j(zeta tensor t_rho). This fixes it uniquely. Existence
follows from any integral height-one isomorphism: the two Tate-module
isomorphisms differ by a unit in Zp, and composition with that integral
formal unit endomorphism makes them equal. Denote the resulting period
by Omega_j. It is a unit and

    phi(Omega_j)=rho(phi)Omega_j=alpha^-1 Omega_j,           (1.1)

for local arithmetic Frobenius. This also follows by applying phi to the
matched formal isomorphism and taking its tangent. If one starts from
the previously fixed Katz period Omega_p instead, retain the exact unit
e_(j,eta)=Omega_j/Omega_p determined by these two Tate frames. It is not
set to1 without checking that the chosen Katz isomorphism has that frame.
No value of a BSD scalar selects Omega_j or e_(j,eta).

The formal logarithm is an isomorphism E_1(Qp)->pZp. By the already
reviewed nonanomalous CM local table and integral Kummer saturation,
projection of the point Kummer map is an isomorphism

    kappa_pi:E_1(Qp) -> H1(Qp,T_pi).                        (1.2)

The completion of the whole E(Qp) has the same image because its
reduction group has p-unit order. Thus we use the exact coordinate
Log_omega=log_E compose kappa_pi^-1, valued in pZp.
This is a local point coordinate; it does not select a rational global point.

## 2. A coefficientwise integral limit from actual theta norms

Put D=D_omega, the invariant derivation defined by df=(Df)omega.
For d>=1 define the rational function

    L_(a,d)=D^(d-1)(D Theta_a/Theta_a).

It is regular and integral on every residue disc of g beta_m.
Indeed the good model's invariant derivation is integral, Theta_a is a
unit on that disc, and reduction of g beta_m is outside E[a]. The latter
uses its nonzero tame f-part and the etale opposite p-power direction.
We do not evaluate D log at its zeros or poles.

Let G_m=Gal(B_m/K), and choose ANY integral lifts r_m(g) of rho(g) modp^m.
The character modulo p^m is defined on this actual quotient. For d>=1 set

    C_(m,d)= (Omega_j/q_a) alpha^(-md)
                    sum_(g in G_m) r_m(g) L_(a,d)(g beta_m). (2.1)

Use the fixed pi-adic embedding for these values. The sum is over the
FULL global ray group, or equivalently over every component of the
semilocal algebra B_m tensor_K Qp, followed by its full local trace.
There is no normalization by its degree.

**[NEW] Proposition2.1.** The limits C_d=lim_m C_(m,d) exist, belong to Zp,
and are independent of all lifts r_m(g). More precisely,

    C_(m+1,d)-C_(m,d) in p^m W,
    C_d-C_(m,d) in p^m W.                                 (2.2)

The bound is uniform in d.

*Proof.* All evaluated L_(a,d), the character lifts, alpha and Omega_j
are integral, and the last two are units. The exact theta norm for
the degree-p opposite ray step gives, as an identity of rational
functions in a point variable X near O,

    product_(h in ker(G_(m+1)->G_m))
       Theta_a(gh beta_(m+1)+X)
                 =Theta_a(g beta_m+[barpi]X).

Take d invariant logarithmic derivatives at X=O. The result is

    sum_h L_(a,d)(gh beta_(m+1))
                         =alpha^d L_(a,d)(g beta_m).       (2.3)

For every h in that kernel, rho(h)=1 modp^m. Therefore replacing
r_(m+1)(gh) by r_m(g) changes each weighted derivative sum by an element
of p^m W. Equation(2.3) cancels the extra alpha^(-d) and proves(2.2).
Changing any r_m(g) has the same bound. Completeness proves existence
and independence. These are integral sums, not normalized averages.

Local Frobenius permutes the embedded g beta_m by left multiplication.
Equation(1.1) and r_m(phi)r_m(g)=r_m(phi g) modp^m imply
phi(C_(m,d))-C_(m,d) in p^m W. The limit is fixed by phi. Since
W^(phi=1)=Zp, this proves C_d in Zp. QED.

The bounds do not say that any C_d is nonzero. In particular they are
not an interpolation assertion identifying C_d with an L-value.

## 3. A convergent analytic formula for the actual cohomology class

For z in pZp let exp_E(z) be the point inverse to the formal logarithm.
The local unit family in the asymmetric proof is

    U_(a,m)(R)=Theta_a(beta_m+exp_E(alpha^-m log_E R))/Theta_a(beta_m).

It is in1+p of the full semilocal integer ring and has exact relative
norm U_(a,m+1)(R)->U_(a,m)(R). Its original twisted finite Kummer
transfers define the integral class U_pi(R).

**[NEW] Theorem3.1.** The PARTICULAR local point map has the exact formula

    Log_omega(U_pi(R))=F_a(log_E R),
    F_a(z)=sum_(d>=1) C_d z^d/d! .                        (3.1)

The series converges on pZp and takes values in pZp. Its finite normed
approximation

    F_(a,m)(z)=(Omega_j/q_a) sum_g r_m(g)
       log_p[Theta_a(g beta_m+exp_E(alpha^-m z))/Theta_a(g beta_m)]

satisfies F_a(z)-F_(a,m)(z) in p^(m+1)W uniformly on pZp.

*Proof of the analytic assertions.* Taylor expansion using the invariant
derivation gives F_(a,m)(z)=sum_d C_(m,d)z^d/d!. Its coefficients have
the bound v_p(C_(m,d))>=0. Since p>=5, v_p(z^d/d!) tends to infinity
and is at least1 for every d>=1 and z in pZp. Equation(2.2) then gives
uniform convergence with the asserted error. The limits C_d in Zp
give the claimed rational local coefficients and image pZp.

*Proof of the cohomological comparison.* We spell out the integral
comparison so the rank-one target is not used to guess a map. At a
finite unramified local extension L on which rho modp^k is trivial,
the matched Tate identification extends to an isomorphism
mu_(p^k)->E[p^k]^connected over O_L. One can check this by Cartier
duality: both duals are finite etale, and the prescribed generic
isomorphism is the same unramified module. The formal Kummer torsor
of a unit v in1+pO_L therefore has formal point coordinate

    Omega_j log_p(v) mod p^(k+1)W.                        (3.2)

To see its descent and the modulus directly, the inverse matched
formal isomorphism over W sends v to log_E^-1(Omega_j log_p v).
For an automorphism fixing L, the period changes by an element of
p^kW, because rho is1 modulo p^k; multiplying log_p v in pO_L
makes the point change by p^k times a formal point. Witt coordinates give
(W/p^(k+1))^(phi^[L:Qp])=O_L/p^(k+1), so this logarithm has an actual
descended class in pO_L/p^(k+1)O_L. Choose a lift of that class in pO_L
and let P_L be its inverse formal logarithm. Its difference from the
W-point displayed above is p^k times a formal point over W.

The required torsor descent is checked by INJECTIVITY, not by faithful
flatness alone. Through the prescribed finite flat isomorphism, the map
H1(O_L,E[p^k]^connected)->H1(W,E[p^k]^connected) is the Kummer map
O_L^times/(O_L^times)^(p^k)->W^times/(W^times)^(p^k).
Both rings have Picard groupzero. Their prime-to-p/Teichmuller unit
parts are p^k-divisible, and logarithms identify this map with the
INJECTION pO_L/p^(k+1)O_L->pW/p^(k+1)W.
Over W, the matched integral formal isomorphism identifies the unit
torsor with the formal Kummer torsor of the displayed W-point, hence
with that of P_L. The injection therefore identifies their original
torsors over O_L as well. This proves(3.2) with its exact integral modulus.

Under corestriction, point Kummer classes use the actual group trace.
Applying log_E gives the sum over embeddings. The coefficient vector
in a conjugate term is g(t_rho)=rho(g)t_rho, so the resulting finite
coordinate is exactly F_(a,m)(log_E R) modulo p^(k+1), whenever m>=k.
This description also covers a product of unramified fields, by adding
the trace from each component. It does not replace the full semilocal
trace by that from a single chosen factor.

The compatible local Kummer construction of U_pi(R), followed by(1.2),
is uniquely determined by these coordinates at every k. Taking limits
and the analytic calculation proves(3.1). QED.

All coefficient-frame changes are visible through Omega_j. The equality
is not merely up to a p-adic unit, and it does not identify that period
with an independently chosen Katz period without its frame comparison.

## 4. What must vanish for a proper linear point comparison

The fact that all C_d are integral gives a useful exact bound. For
z in p^rZp, r>=1,

    F_a(z)-C_1 z in p^(2r)Zp,
    F_a(z)/z in Zp for nonzero z.                         (4.1)

Indeed dr-v_p(d!)>=2r for d>=2 and p>=5. This is a proved error bound,
not a linearity theorem.

**[NEW] Proposition4.1.** The actual map R->U_pi(R) is additive on
E_1(Qp), or equivalently equals c kappa_pi(R) there for one c in Zp,
if and only if

    C_1=c,  C_d=0 for all d>=2.                           (4.2)

*Proof.* Apply the isomorphisms(1.2) and log_E. A continuous additive
map pZp->pZp is multiplication by an element of Zp: first use integer
multiples of p and then density of Z in Zp. The analytic identity
F_a(z)=c z on the disc forces every higher Taylor coefficient tozero.
The converse follows immediately from(3.1). QED.

For the three ORIGINAL finite-height points R_P=n_pP, R_Q=n_pQ and
R_(P+Q)=n_p(P+Q), put x=log_E R_P and y=log_E R_Q. These are nonzero,
and x+y is nonzero, by injectivity of the rational point group in the
local group and the non-torsion logarithm argument already reviewed.
A single integral c works at all three points if and only if BOTH

    y F_a(x)-x F_a(y)=0,
    F_a(x+y)-F_a(x)-F_a(y)=0.                             (4.3)

The first equality gives the same scalar at P and Q, the second at
their sum, and integrality follows from(4.1). Without dividing a
nonunit in finite cohomology, their exact analytic defects are

    y F_a(x)-x F_a(y)
      =xy sum_(d>=2) (C_d/d!)(x^(d-1)-y^(d-1)),
    F_a(x+y)-F_a(x)-F_a(y)
      =sum_(d>=2) C_d sum_(j=1)^(d-1) x^j y^(d-j)/(j!(d-j)!).

Equations(4.2) and(4.3) are distinct: three-point agreement does not
prove the full map linear. Neither set of higher coefficients or
particular defects is asserted zero in this note.

## 5. Exact next arithmetic task

The local map is now described by specific limits of algebraic theta
derivative sums, with uniform integral error, its full prescribed Tate
frame, and a convergent Taylor expansion. It has not been replaced by
an arbitrary multiple of the point Kummer map. The proper-line scalar
ambiguity in the asymmetric proof can only absorb its actual linear
part; matching it at the specified points requires(4.3), and uniformly
on the formal group requires(4.2).

The next step is to evaluate these specific sums or prove identities
among them, with their primitive-ray terms and all characters retained.
The p-adic polylogarithm/limit-formula sources may help do that, but no
torsion-specialization L-value theorem is applied to these non-torsion
points without a comparison. No global boundary counterterm, rational
frame, original c2,p nonvanishing or universal BSD identity follows yet.

The independent core review checked the matched period and Frobenius convention,
the derivative norm(2.3), coefficientwise convergence/invariance, the
finite flat formal Kummer argument and its p^(k+1) modulus, full semilocal
trace, and the separation between linearity and three-point compatibility.
No old certificate, prime scan or numerical period calculation was rerun.

## 6. A NEW exact quadratic coefficient test at p=5

**Additional section: passed its OWN independent arithmetic review.**
The five-section proof above passed its separate review. The NEW
[Sage script](../../compute/scripts/cm_local_taylor_mod5.py) and its
[exact finite-field output](../../compute/data/cm_local_taylor_mod5.json)
test the local Taylor coefficient C_2. This symbol is NOT the original
cyclotomic c_(2,p). No old BSD certificate was rerun.

At p=5 use i=3 in the residue field, pi=-1+2i, alpha=barpi=-1-2i,
a=7, and q_a=12(49+7)=672. At level m=1 the Gaussian annihilator is

    mu=f0 barpi=234+78i,  Norm(mu)=60840.

The script constructs the actual CM image modulo mu from Frobenius at
the twelve displayed good split primes. For each prime ell, direct
finite-curve point counting determines trace a_ell. Ordinary CM makes
Frobenius one of a_ell/2±i sqrt(ell-(a_ell/2)²). The script distinguishes
them on a point over F_(ell²) not killed by twice that square root,
by comparison with its coordinate Frobenius. Thus each generator is an
ACTUAL CM Frobenius with its selected prime embedding. Its original
rho value modulo5 is the inverse of its conjugate Gaussian value at i=3.

Closure in (O_K/(mu))^times gives a subgroup H of order4608, the exact
degree of B_1/K. These genuine Galois elements therefore generate its
full image. The weight is checked consistently around EVERY generated
relation. H intersects the four Gaussian units only in1. The total
unit group has order18432, so those units give all four H cosets.

The finite-field model is E over F_(5^24), with the irreducible modulus
and exact point coordinates retained in the JSON. Since

    pi^24=32125393-242017776 i,
    (pi^24-1)/mu=-186720-972024 i,

the indicated Gaussian endomorphism constructs a mu-torsion point B.
The script verifies [mu]B=0 and [mu/lambda]B!=0 for each Gaussian prime
lambda=1+i,3,3+2i,3-2i,barpi dividing mu. Hence its EXACT annihilator
is(mu). It also checks [pi]B=(x(B)^5,y(B)^5), and that the H orbit has
4608 distinct points. The isogeny[mu] is etale at the selected pi prime,
so reduction identifies its characteristic-zero torsion with this orbit
over the maximal unramified field.

The rational invariant derivatives are evaluated directly, without
theta-function approximation. In characteristic5, write f=x³+4x,
psi=psi_7(x). If L_d=A_d(x)+yB_d(x), then

    A_1=0,  B_1=-24 psi'/psi,
    A_(d+1)=(3x²+4)B_d+2f B_d',  B_(d+1)=2A_d'.          (6.1)

These are exactly D^d log Theta_7 for omega=dx/(2y). Every denominator
is checked nonzero on the orbit. The weighted sums

    S_d=sum_(g in H) rho(g)L_d([g]B),  1<=d<=4,

give the exact zero/nonzero pattern

    S_1=0,  S_2!=0,  S_3!=0,  S_4=0.                    (6.2)

The full polynomial-basis values are in the certificate; in particular
S_2 has nonzero constant coefficient1. The additional identity
S_d^5=3S_d holds for all four sums, independently checking their local
Frobenius/character direction.

A random primitive point need not be the reduction of the fixed complex
beta_1 in its original embedding. This does NOT affect the asserted test:
any two generators of the O_K/(mu) module differ by a unit, and every
such unit is epsilon h with epsilon a Gaussian unit and h inH.
The rational identity Theta_a(epsilon Z)=Theta_a(Z) gives
L_d(epsilon Z)=epsilon^-d L_d(Z). Reindexing by h therefore multiplies
S_d by epsilon^-d rho(h)^-1, a nonzero scalar. Accordingly(6.2) tests
ZERO/NONZERO for the original beta_1 without declaring the point choice
or period comparison numerically identical. Equation(2.2) at m=1, with
the unit factors Omega_j/q_a and alpha^-d, now gives

    C_1=0 mod5,  C_2 in Z5^times,  C_3 in Z5^times,
    C_4=0 mod5.                                          (6.3)

**[NEW, independently reviewed] Corollary6.1.** The actual
local map U_pi is not additive at p=5. More strongly, for ALL nonzero
x,y in5Z5,

    v5(F_a(x+y)-F_a(x)-F_a(y))=v5(x)+v5(y).               (6.4)

*Proof.* In the exact additivity defect in§4, the degree-two term is
C_2 x y. Its coefficient is a unit by(6.3). Every term of degree at
least3 has valuation at least v5(x)+v5(y)+1: for integers n>=1,
(n-1)r-v5(n!) iszero at n=1 and positive at n>=2 when r>=1.
Apply this separately to the two positive exponents in that term.
Thus no higher term cancels C_2xy, proving(6.4). QED.

In particular one scalar c cannot match the three ORIGINAL points
64P,64Q,64(P+Q) through c kappa_pi. At least one of their three selected
local classes is nonzero. This is a result for these new local classes,
not for an unproved global Selmer specialization or the old c_(2,5).
An additional exact rational group-law check gives

    v5(t(64P))=1,  v5(t(64Q))=1,  v5(t(64(P+Q)))=2,
    t=-x/y.

On this formal subgroup v5(log_E R)=v5(t(R)). Thus the particular
three-point defect has logarithm valuation exactly2 and, under(1.2),
has divisibility exactly5 in the integral local H1 lattice. It is
nonzero modulo25 in that lattice. The rational point-valuation check
is reproduced by multiplying the three stated rational points by64;
no analytic numerical logarithm or old height test is needed.

There is a sharper consequence, separately proved in §8 of the arithmetic
review. Since C1 is divisible by5 and v5(x+y)=2, F_a(x+y) is in125Z5.
The defect has valuation2, so F_a(x)+F_a(y) has valuation exactly2.
Each summand is in25Z5 by(6.3) and v5(x)=v5(y)=1. Consequently at
least one of the TWO classes U_pi(64P), U_pi(64Q) is divisible by5
but not by25 in H1(Q5,T_pi). The sum-point class is zero modulo25
in that lattice. This does not determine which of P or Q gives the
nonzero class. No additional coefficient or arithmetic run is used.

This rules out the specific attempt to select one proper boundary-line
scalar by identifying this entire local norm family with the point map
at those three points. It does not rule out additional boundary data,
a different source, higher operations or the BSD comparison itself.
The arithmetic audit independently verified all these implications,
including the sharper two-point alternative. Its separate verifier and
output are preserved in the repository. The exact reviewed revisions
are recorded in the two review files; the added refinement has its own
proof in the arithmetic review's §8.
