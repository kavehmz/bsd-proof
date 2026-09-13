# Independent review of the CM local point comparison

Date: 2026-09-13. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
**PASS after the explicit integral-descent repair.** All five sections of
[the proof](cm-local-point-comparison-attack.md) were reconstructed against
SHA256
8fad3936741f7be8ff173ffb91c5da99036e94a55545eec685a21c56c975b5b8.
The initial version was
900f97a5314d002d40143c0920812444c4144cfd4b0f8ee6111299d153e42f9e.
The [checkpoint](cm-local-point-comparison-checkpoint.md) was also read;
its snapshot at completion was
efed9af6f0e1cd21bc0c875625e117e732f820a3a87069a640c687ecda889c41.
Its subsequent coefficient leads and newly scheduled finite-field test
are operational/prospective entries, not additional results certified
by this review. No old computation or new numerical test was run here.

The preceding asymmetric construction has separately passed
[independent review](review-cm-asymmetric-ray.md). Its actual character,
theta norm and semilocal unit construction are the inherited inputs.
The present verdict proves an exact formula for that local map. It does
not prove its linearity, any higher-coefficient nonvanishing, the
particular three-point identities, global arithmetic descent, or BSD.

## 1. Primary input and exact period

I inspected [Bannai–Kobayashi, math/0610163v4, §3.1](https://arxiv.org/html/math/0610163v4#S3.SS1),
dated 11 December 2007. In its good ordinary split setting, the integral
formal isomorphism over the completed maximal unramified integer ring
has the stated exponential/logarithm expression and unit period. This
is the source input used here. No torsion-specialization interpolation
theorem from that paper is applied to the present non-torsion points.

Matching its inverse to the prescribed map
j:Zp(1) tensor Zp(rho)->T_pi is legitimate: any two such height-one
Tate-module identifications differ by a Zp-unit, realized by an
integral formal unit endomorphism. This fixes the period Omega_j.
To check the Frobenius sign directly, write s=eta_j^-1. On compatible
roots of unity the matching condition gives

    phi(s(zeta-1))=[rho(phi)]_E s(phi(zeta)-1).

Consequently phi(s)=[rho(phi)]_E s as formal maps. Taking tangent
maps gives phi(Omega_j)=rho(phi)Omega_j=alpha^-1 Omega_j.
Thus the period transforms by rho, rather than its inverse. The
declared frame ratio Omega_j/Omega_p has not been silently set to1.

The formal logarithm on E_1(Qp) has image pZp. The identification with
H1(Qp,T_pi) uses the already checked nonanomalous local Kummer table
and its integral saturation. It is not inferred just from both modules
having rank one. In this prime range the reduction group has p-unit
order, so passing from formal points to the full completed point group
does not introduce an index.

The convergence warning is essential and correct. The formal identity
involving exp and log cannot be evaluated as a nested analytic
composition at arbitrary connected p-power torsion points. The
evaluations below occur in pW or 1+pW; the torsion comparison itself
is made by finite flat group schemes.

## 2. Actual derivative sums and their integral limit

The invariant derivation D_omega preserves the integral local ring on
the good smooth model. At every conjugate of beta_m, the nonzero tame
conductor component survives reduction and places the point outside
E[a]. Theta_a and its inverse are therefore integral on the relevant
disc. This proves integrality of every evaluated
D^(d-1)(DTheta_a/Theta_a), uniformly in d; no bound for an unsmoothed
theta logarithm has been substituted here.

The inherited degree-p opposite-ray norm is an identity of rational
functions in the additional point X. Taking d invariant logarithmic
derivatives uses [barpi]^*omega=alpha omega at each step and gives

    sum_h L_(a,d)(gh beta_(m+1))=alpha^d L_(a,d)(g beta_m).

This exactly cancels the new alpha^(-d) in the normalized sum. On the
kernel of that ray step, rho is1 modulo p^m. Integral lifts of the
finite character need only respect multiplication modulo p^m, which
suffices to show

    C_(m+1,d)-C_(m,d) in p^m W.

All other factors, including q_a and Omega_j, are units. Changing
the lifts gives the same error. Summing the successive errors proves
the claimed limit and approximation, uniformly in d. These are full
integral sums; there is no division by a ray-field degree.

For rationality of the limit, local Frobenius reindexes g beta_m by
phi g. In the reindexed sum its character weight changes by
rho(phi)^-1 modulo p^m, canceling the factor rho(phi) from Omega_j.
Thus phi(C_(m,d))-C_(m,d) lies in p^m W. The limit lies in
W^(phi=1)=Zp, as is also immediate coefficient by coefficient in Witt
coordinates. Only the local Frobenius action on W is needed; this
does not posit an action of the whole global ray group on W.

## 3. Finite flat Kummer comparison: the repaired step

The original faithful-flatness sentence alone would not have proved
injectivity on H1. The repaired proof supplies the actual injection
needed for these particular torsors, and I checked it as follows.

Fix n=p^k and a finite unramified extension L/Qp on which rho modulo n
is trivial. The prescribed generic isomorphism
mu_n->G_n=E[n]^connected extends to the integer rings: after Cartier
duality both group schemes are finite etale, and their identified
generic modules are unramified. This is the chosen finite-level
identification, rather than a newly chosen scalar multiple.

For v in1+pO_L, the matched inverse formal isomorphism over W gives a
formal point P_W with

    log_E(P_W)=Omega_j log_p(v).

The right side is in pW. Because phi^[L:Qp](Omega_j)-Omega_j is in
p^kW, its class modulo p^(k+1) is fixed by that Frobenius power.
Witt coordinates give precisely

    (W/p^(k+1))^(phi^[L:Qp])=O_L/p^(k+1).

It therefore has a lift z_L in pO_L. Let P_L=exp_E(z_L). The
difference of the two logarithms is in p^(k+1)W, so P_L-P_W is
[p^k] of a formal point over W.

Both O_L and W are local rings with trivial Picard group. Their
Teichmuller unit parts are p^k-divisible. Hence the prescribed finite
flat identification and the multiplicative Kummer sequence identify

    H1(O_L,G_n) -> H1(W,G_n)

with the map on unit quotients, and the logarithm identifies that map
with the injection

    pO_L/p^(k+1)O_L -> pW/p^(k+1)W.

Over W the integral formal isomorphism identifies the mu_n Kummer
torsor of v with the connected Kummer torsor of P_W, hence of P_L.
The displayed injection then proves equality of the original torsors
over O_L. This is a finite flat cohomological comparison with its
correct modulus p^(k+1), not a pointwise Galois-invariance argument
or a dimension count. It proves equation(3.2).

## 4. Full semilocal trace and the analytic identity

The finite class must use every factor of B_m tensor_K Qp. Each
factor is unramified, and for m>=k its local Galois group fixes rho
modulo p^k. Thus the preceding comparison applies to each principal
unit component.

Corestriction of a point Kummer class is the Kummer class of the group
trace. Its logarithm is the sum of the conjugate logarithms. Within
one unramified component, conjugating Omega_j contributes rho(phi);
this is exactly the same coefficient action as
phi(t_rho)=rho(phi)t_rho. It is counted ONCE. Across the different
components, transporting the original coefficient vector contributes
the corresponding coset character. Combining the coset transports
and local traces gives the single full sum

    (Omega_j/q_a) sum_(g in G_m) rho(g)
       log_p[Theta_a(g beta_m+exp_E(alpha^-m z))/Theta_a(g beta_m)]
                                                        mod p^(k+1).

One does not apply the character a second time after this trace, nor
declare that arbitrary global g acts on Omega_j in W. Replacing the
finite weights by r_m(g) changes the coordinate by p^(k+1), since
m>=k and each logarithm is in pW. There is no averaging or omitted
semilocal factor.

Taylor expansion along the formal exponential is given by repeated
invariant differentiation, so the displayed finite sum is
sum_d C_(m,d)z^d/d!. For z in pZp, the valuations of z^d/d! tend to
infinity and are at least1. The uniform coefficient error p^m thus
gives F_a(z)-F_(a,m)(z) in p^(m+1)W, uniformly on that disc.
The limit has coefficients in Zp and values in pZp.

The compatible finite Kummer classes determine the integral class.
The already fixed point coordinate therefore gives exactly

    Log_omega(U_pi(R))=F_a(log_E R).

No additional unit, p-power division, omitted q_a, or normalization by
the transfer degree enters this identity.

## 5. Linearity and the particular three-point tests

For p>=5 and r>=1, dr-v_p(d!)>=2r for d>=2. This verifies both the
quadratic error bound and F_a(z)/z in Zp for nonzero z in pZp.
A continuous additive map pZp->pZp is multiplication by a Zp-scalar:
use integer multiples of p and density, followed by continuity.
Analytic uniqueness then shows that additivity is equivalent to the
vanishing of every C_d for d>=2, with C_1 the scalar.

The original non-torsion point inputs ensure x, y and x+y are nonzero.
The two equations(4.3) are therefore exactly the conditions for one
scalar at those three points; its integrality follows from the bound
already proved. Both displayed defect expansions follow by direct
power-series algebra and retain every factorial and mixed term.
They do not cancel a nonunit in finite cohomology.

Agreement at three points is weaker than equality of analytic maps on
the whole disc. Neither follows from the one-dimensional local
cohomology group or from norm compatibility. The proof correctly
retains this distinction and makes no coefficient or defect vanish.

## 6. Verdict and exact remaining scope

The corrected five-section proof passes. Its positive conclusion is
an exact, integrally framed local point-coordinate formula, with
explicit algebraic derivative sums and uniform p-adic approximation.
The finite flat descent omission was repaired before this verdict.

The subsequent unsmoothed coefficient lead and new finite-field
computation in the checkpoint are outside this verdict. In particular
I have not assumed integrality across growing opposite-ray torsion
levels for an unsmoothed value, verified a new numerical coefficient,
or deduced nonvanishing from an auxiliary unit.

The particular three-point defects, compatible global boundary
selection, the original cyclotomic c_(2,p), the rational arithmetic
frame comparison, and full BSD remain unresolved by this proof.
