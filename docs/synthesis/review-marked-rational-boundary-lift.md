# Independent review of the marked rational boundary test

Date: 2026-09-13. Reviewer: root/coordinator.
**PASS for all nine sections in their stated scope.**
Reviewed [proof](marked-rational-boundary-lift-attack.md), mathematical
SHA256 `0da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2`.
The verdict does not assert vanishing of the full motivic obstruction.

I read the entire proof and checkpoint, inspected the predecessor's
coefficient construction and the completed compact right-cup review,
and independently reconstructed the cone signs, exterior coefficient,
localization degrees, higher-Chow cycle types and geometric Tate projector.
No old numerical certificate was rerun.

## 1. Actual coefficient maps and the two signs

In the fixed relative differential D(a,b)=(da,r(a)-db), lifting the
positive boundary (0,+beta) produces boundary differential -epsilon beta.
Since beta has degree2, tensoring the extension with beta introduces no
additional swap sign. The obstruction is indeed -j_B(chi_beta,0).
The relative exact sequence identifies its zero with an actual global
restriction preimage of (chi_beta,0). A global diagonal restriction is
available but does not give that preimage.

I reconstructed the kernel coefficient from the octahedron for
1->P_U->q_*1: dualizing gives
G=(Cofib(1->P_U)[1])^dual as in the proof. The two-step tensor filtration
then has successive terms wedge²G, G tensor L and wedge²L. On the
DECLARED alternating generator e1 tensor e2-e2 tensor e1, the middle
connecting coefficient is eta1 tensor e2-eta2 tensor e1. The target
identifies g tensor e-e tensor g with g tensor e, so no extra factor2
survives. The model-enhanced filtration is covered by
[Guletskii math/0306297v1, Proposition19](https://arxiv.org/pdf/math/0306297v1),
which I opened and checked in the indicated revision.

For the second sign, write j_B chi=e0 external chi. Its RIGHT cup with
the degree-one unit requires moving chi of degree r past that unit.
The scalar base trace is the already established +388. Thus the full
formula is (-1)^r388 chi. At the actual r=3 it is negative; the minus
from the coefficient obstruction cancels it. The necessary boundary
condition therefore has +388 chi_D on its left side. No coefficient
realization-faithfulness claim enters this calculation.

## 2. Cycle degrees and actual rational corrections

Curve duality H=h1_coho(E_s)(1)[1] sends
H_M³(E_t,H(2)) to the indicated h1 part of H_M⁴(E_s×E_t,Q3).
This is CH³(E_s×E_t,2), exactly the degree of point divisor times beta2.
The Miller identity gives
div(h_j/m_(R,P_j))=Z_j-([P_j]-[O]). Its function-graph chain times beta2
has one more cubical degree and the asserted boundary. It is used on the
proper source factor; it does not remove the relative puncture data.

For {u,A_ij}, the stipulated tame convention gives residue
A_ij(c)^(ord_c u)=1 at the old cusps, and u(s)^(-ord_s A_ij) at the new
points. Localization has kernel H_M⁰(k,Q1)=0. This proves unique rational
extension and injectivity into the generic field. Projection formula then
proves its full transfer iszero from the inherited exact Norm_pi(u)=±1.
The minus in the new residue matrix is necessary and is present.

The isolated variable toric family splits at its old cusp fibers because
all A_ij equal1 there. A positive boundary lift for that family is valid.
It is explicitly kept separate from the fixed semiabelian extension.

## 3. Added boundary and trace

The old proper cusp equality tensored with the CONSTANT D coefficient
gives the asserted proper-pair injection. It is not applied on the new
open curve. Purity for Sigma×E_t of codimension1 changes degree/twist by
(2,1); hence the kernel is exactly the image of H_M²(Sigma×E_t,D1).
The compact curve trace and this Gysin shift cancel, leaving the actual
right cup with u(s), followed by the finite field trace.

For a pulled-back pattern, the multiplicity e_s is retained both in the
Gysin input and in specialization of the field norm. Projection formula
combines the terms into the Kummer class of ±1, which is rationallyzero.
This rules out only those patterns as corrections to a nonzero chi_D.
It does not rule out all boundary corrections or prove chi_D nonzero.

I checked the open-boundary distinction in
[MVW, Theorem7.16 and its proof](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf):
the relative Picard relation requires boundary values equal to1. The
principal divisor on the proper curve therefore cannot erase the actual
u|Sigma tuple. The proof correctly preserves the added Poincare fibers.

## 4. The Tate projection, including the Koszul sign

I checked the actual motivic symmetric-square input in
[Ancona–Enright-Ward–Huber1312.4171v2, Theorem4.2.3 and
Proposition4.3.5](https://arxiv.org/pdf/1312.4171v2).
For the homological elliptic motive the categorical symmetric square of
its h1 is Q(1)[2]. Dualizing gives Sym²(h1_coho)=Q(-1)[-2], as used here.
This is an identity of motives, not an inference from Betti dimensions.

The point divisor's non-h1 components vanish by degreezero and
H_M²(Q,Q1)=0. The non-h1 beta2 components are H_M²(Q,Q2) and H_M⁰(Q,Q1).
The former iszero rationally: the direct-sum tame localization and
K2(Z)=Z/2 in [Weibel, III5.2.2 and
III6.5.1](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf)
show K2(Q) is torsion. A DIRECT SUM of finite groups is sufficient; no
false statement that the group itself is finite is needed.

Consequently the geometric PLUS part of each actual product has group
Hom(1,Q(-1)[-2](3)[4])=H_M²(Q,Q2)=0. The remaining geometric MINUS
part realizes the ordinary rank-three Sym² of H¹ because interchanging
the two degree-one factors introduces a minus sign. The proof gets both
the rational projector and this realization distinction right.

## 5. Verdict limits

The exact obstruction, explicit toric correction, added-unit condition,
pulled-back tracezero and Tate projection vanishing pass. The full
point×K2 class in the remaining summand is still uncomputed. No global
restriction preimage, full rational lift, spectral rationality or BSD
coefficient follows from this review. The ordinary Somekawa degree
comparison is used only to reject an inapplicable shortcut, not as a
positive vanishing input. The next mathematical step must address the
actual remaining class and full coefficient boundary.
