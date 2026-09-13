# CM motivic logarithm derivative: checkpoint

Date: 2026-09-12. Author `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Own only `cm-motivic-derivative-attack.md` and this checkpoint.
Parent objective remains full BSD over Q. No old certificates or new agents.
Status: bounded construction completed; all eight proof sections passed
[independent review](review-cm-motivic-derivative.md) and coordinator inspection.

## Completed construction and unchanged target

This task continued the reviewed CM-Derived construction for E:y²=x³+39x at the
same good split primes. The actual finite elliptic units and exact
normalization give z_infinity=T w_infinity; the projected local frame
is constructed when Reg_p is nonzero. A single rational framed element
with the required real realization remains unproved, and its rationality
must be a conclusion.

The rational finite-group-ring augmentation route was already tested:
its positive graded pieces vanish. This completed task instead computed
the Sen operator of the inverse cyclotomic coefficient action modulo T²,
constructed the genuine motivic logarithm/Kummer replacement on G_m and
the CM elliptic curve, and evaluated its boundary and trace on the saved
elliptic units. It then gave an exact finite-coefficient formula recovering
the first derived class. The literal finite-dimensional geometric
coefficient obstruction and its limited scope are recorded below.

## Material finding 1: coefficient deformation

Confirmed by direct calculation and the primary Berger–Colmez paper,
Théorie de Sen et vecteurs localement analytiques, Ann. ENS49 (2016),
947–970, DOI10.24033/asens.2300, §1.2 Theorem1.3/Remark1.4.
For the basis(T,1), Sen uses Theta(Q_p(1))=1 and gives
Theta(U_gamma)=−g_p^(-1)*[[0,1],[0,0]]. Tensoring V_pE gives
nonzero size-two Jordan blocks at eigenvalues0 and1. The deformation
is therefore not Hodge–Tate; its Hodge–Tate invariant dimension is2
rather than4. This does not affect the already-defined derived Selmer
class, and does not exclude a different motivic object mapping to it.
The deduction and its exclusion scope passed independent review.

Primary logarithm source read: Huber–Kings, arXiv1505.04574v1,
Definitions4.2.1/4.3.1, Lemma4.2.3, Proposition4.3.3 and
Corollary4.4.2. Its actual first logarithm motive is the Kummer
complex [Q→G_Q]; on G_m its realization extendsQ_p byQ_p(1),
and on E it extendsQ_p byV_pE. The torsion splitting principle
is rational and must not be interpreted as an integral splitting.

## Material finding 2: actual motive and exact derivative extractor

Full proof saved in `cm-motivic-derivative-attack.md` §§1–8;
all new propositions passed independent review without mathematical correction.

The actual rational family is the first G_m logarithm motive pulled
back along the saved rational function Theta_a:E\E[a]→G_m. Its
fiber at R_r is the genuine 1-motive [Z→G_m], 1↦Theta_a(R_r),
with graded motives Q and Q(1). Its boundary is the ordinary Kummer
class, and norm gives EXACT Cor(delta(Theta_a(R_r)))=delta(e_r).
The factor 12 is already in Theta and is not inserted again. The
elliptic first-log fiber at R_r instead rationally splits (R_r torsion),
and the divisor boundary has zero Abel–Jacobi class because principal.

The literal quadratic replacement Sym²K has graded Q,Q(1),Q(2).
For its Kummer cocycle k, d(−k(g)²/2)=k(g)chi(g)k(h)=k cup k.
This is an explicit degree-two/Tate-two nullhomotopy, not a derived
H¹(V) class. No assertion about all polylogarithm classes follows.

Positive finite-unit construction: for each m choose cyclotomic n≥m
and division level r≥max(m,n+1). Insert the SAME finite coefficient
t_rho,m before cyclotomic trace, use the SAME Kato smoothing factor
12(a²−Psi^c(a)sigma_a), rational Betti vector and Shapiro, then
map (Z/p^m)[Gamma_n]→(Z/p^m)[T]/T² by gamma↦1+T. The result Z_m
is exactly z_infinity mod(p^m,T²). Since E(Q)[p^m]=0 and its
augmentation vanishes, there is a UNIQUE d_m with T d_m=Z_m.
If its cocycle is f=a+Tb and a(g)=gv−v, then
d_m(g)=b(g)+c_gamma(g)gv. The plus correction cancels
db=c_gamma cup a. Uniqueness proves d_m=w0 mod p^m and compatibility.
This reconstructs the actual derivative from finite Kummer data;
the finite classes are only asserted to lie in global H¹ here.
Their rational limit has the already proved full-Selmer condition.

The exact framed output is consequently still
B_p^(-1)(p/(2#E(Fp))*pr_W((lim d_m)tensorT))
=c_cmp M_p/(4e_p Reg_p)*Xi, when Reg_p≠0. All CM periods,
Euler factors and generator logarithms are retained. No arithmetic
operation has descended these outputs to one rational framed element
with real realization ell_E/(2Omega_E). This is stated as
GAP CM-Log-Derived in §7; rationality of n_E is its conclusion.

Additional source read: Faltings, JAMS1 (1988)255–299,
DOI10.1090/S0894-0347-1988-0924705-1, III Theorem4.1 printed p298
(smooth proper with normal-crossing divisor removed). It supports the
literal finite-geometric-realization exclusion, not a claim that all
derived arithmetic operations must be Hodge–Tate.

The review verified the Sen signs/exclusion scope, the actual motivic
boundary and norm on extension classes, the exact cochain-change
cancellation in formula(17), H⁰-based uniqueness and inverse-limit
recovery, and the inverse frame map only on its one-dimensional image.
Its reviewed mathematical revision is
855395f9cd86706b30a41b7270ce370914d72514fd871e0a1f517336d28b5827;
the subsequent PASS links and this checkpoint update are editorial.

The next mathematical target remains the rational secondary comparison
in §7, including its real realization and rationality as a conclusion.
Root has not yet dispatched a new mathematical task. The prospective
direction is an actual mixed extension combining the correctly weighted
CM-twisted Kummer extension with the fixed point 1-motives; no result
from that prospective construction is asserted here. Do not restart the
completed source audit, finite-cochain proof or tested rational-vector
insertion as unfinished work.
No old scripts ran; no process or additional agent is pending.
