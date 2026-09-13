# CM mixed extension: checkpoint

Date: 2026-09-12. Author `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Own only `cm-mixed-extension-attack.md` and this checkpoint.
Parent objective remains full BSD over Q. No new agents or old numeric reruns.
Status: bounded construction completed; all ten sections passed
[independent review](review-cm-mixed-extension.md) and coordinator inspection.

## Completed bounded construction

This task used the actual CM-twisted theta Kummer extension
0→A→K_R→R→0, with A=M_Psi and R=A(−1), together with the
pulled-back dual point 1-motives for the fixed rational P,Q.
No CM idempotent was applied to a whole marked 1-motive.

The simple fiber product restricts canonically to A⊕Q over its
Q-subobject and therefore does not provide the required lower
point extension. Genuine blended extensions were then constructed,
their Yoneda and choice data computed, and both rational affine
norm descent and the nonlinear determinant-before-trace operation
were tested. Their finite coefficient-one difference recovers the
previous exact d_m formula. The rational frame comparison remains
open with the same good-split scope and rationality-first target.

## Completed deductions

The full proof is saved in `cm-mixed-extension-attack.md` §§1–10.
All new propositions passed independent review after the scope repair
recorded below.

The category and sign issues are explicit. With A=M_Psi, B=M_Psi^c,
R=B^dual, tensoring the lower point extension X_i by B is the Baer
negative of its Cartier dual. Tensoring the pulled-back dual Y_j by B
marks the negative projected point. Both signs cancel in the bilinear
height. After this twist the blend is an actual coefficient 1-motive
with grades k(1),B,k. Four Poincaré fiber trivializations give one
matrix blend with grades A²,k,R² before the twist. Geometric changes
of trivialization form the explicit Kummer action (F^× tensor k)^4;
no assertion that all extensions in a larger motivic category are
Kummer is made. The source is Bertolin §1.2 and Bertrand §1 Lemmas1–2.

The exact matrix action has diagonal aI₂,1,rI₂ and offdiagonal
x, r y, r Z, with y_j=−κ_B(P_j), r=b^(-1),ab=chi.
Multiplication gives dZ=−x cup y. A unit changes only Z by its
ordinary Q_p(1)-Kummer cocycle. The pure CM obstruction identity
1/2(C(P_i,P_j)+i C(P_i,iP_j))=κ_A(P_i) cup κ_B(P_j)
is an identity of cochains, not merely a use of graded commutativity.

The old full Q-point secondary reference keeps the known correction
matrix 1/2 log[[3/2,27/98],[27/98,243/2]]. Normalizing the GLOBAL
K-height by1/[K:Q], conjugation gives h(P_i,iP_j)=0, so its global
CM component is H_v/2 and its determinant is Reg_v/4. This does NOT
identify the local reference of the new blend at one embedding.
The actual local block is denoted C_v; extra finite and local
corrections for (P_i,iP_j) giving C_v=H_v/2 have not been constructed.
The real period-matrix formula uses the underlying rational real
structure. A central Kummer shift changes c by log(u)/(2pi i),
hence the local secondary height by +log|u|; at p it gives +log_pu.

Actual raw units translate a fixed reference blend B0 at every L_r.
The reference-dependent norm transitions follow the unit norms.
Reference-independent affine averaging divides by[L_r:K]; it returns
B0 because Norm(e_r) is a Gaussian unit, hence torsion. Product-formula
cancellation for genuine global heights is distinguished from local
secondary periods with the reference finite corrections held fixed.

The nonlinear repair was carried through: symmetric squares AND
conjugate cross tensors supply the real squared-log secondary period,
and the p-adic one is the squared p-adic log. If
Q_F(u)=Avg_sigma(log_v(sigma u)^2), then
4 Avg det(C_v+J log_v(sigma u))=4 det(C_v)+4 det(J)Q_F(u)
when the norm is torsion. This quadratic term survives the vanishing
linear mean. Its exact tower formula is
Q_F'(u)=e^(-2)Q_F(Nu)+Avg[(logu−fibermean)^2].
It is quadratic under unit powers, whereas the derived-unit map is
linear. A polarized version is linear after a new auxiliary choice;
using the torsion coordinate itself makes it zero. No equality with
the cyclotomic-character moment M_p is inferred from these periods.

Positive finite comparison: choose J=E_ij with coefficient1 in the
chosen corner. Its difference B_r−B0 is exactlyK_R(e_r); a general
coefficient would scale the result. Use this difference's canonical
integral unit-Kummer/CM coefficient lattice, not reduction of an
arbitrary rational blend. Pulling it back along the ACTUAL finite t_rho,m, then
using the saved smoothing/Betti/Shapiro/first-jet maps, gives precisely
the previously reviewed d_m(g)=D(g)+c_gamma(g)g v. This does not
depend on the reference chosen for the paired difference, and its
point data cancels before the final height projection. Every old
Euler, period and generator factor in the final framed expression
is retained. The construction remains p-local at that extraction step.

The remaining rationality-first target is GAP CM-Mixed-Derived §9:
one rational framed element with all stated p-adic localizations and
real regulator ell_E/(2Omega_E). No such element, no Sha finiteness,
and no Selmer-corank-two statement has been proved.

The review checked the geometric coefficient blend, dual/cup signs,
global CM half-height versus local C_v, affine norm, nonlinear tower
formula and exact finite difference comparison. No old scripts ran,
no additional agent was created, and no process is pending.

## Review correction: global height versus a chosen local block

Root and the independent reviewer identified a scope error in the first
draft's §§5–7: the normalized GLOBAL identity H_glob^AB=H/2 had
been substituted as the LOCAL reference at one chosen embedding.
Complex conjugation exchanges the two p-adic places, so that
substitution does not follow from h(P,iQ)=0. The extra local/finite
corrections for those mixed point pairs were not constructed.

The proof now separates the two quantities. The actual reference
period is C_v, its unit translation is C_v+J log_vu, and the exact
averaged determinant has base term4det(C_v), not Reg_v. A separately
established C_v=H_v/2 would suffice for that specialization, but
no identification of the local baseline is claimed. All claims about norm cancellation, the variance term
and its homogeneity survive with this corrected base term.

Two construction details were also made explicit. First construct
the lower semiabelian extension as the Baer-negative Cartier dual
of X_i, so it already has its k-action. Choose rational lifts of
the upper k-basis, extend with that action on G(K) tensorQ, and
then clear denominators. This does not impose a CM action on an
arbitrary completed marked motive. Second, the finite difference
comparison now fixes coefficient-one J=E_ij and the known integral
unit-Kummer lattice before reduction. The formula d_m and every
Euler/period/Betti factor in its framed output are unchanged.

The reviewer and root verified these corrections. The reviewed
mathematical proof revision is
30dd3934b267872465b352c189da939ef7565febd3083d0a46908439c7d6a5a4;
the later PASS links and completed checkpoint edits are editorial.
There is no outstanding source or mathematical-review repair.

Primary sources inspected: Bertolin math/0402080 §1.2; Bertrand's
November2010 author version of1011.4685, §1 Lemmas1–2 and its
tensor-Ext identification; Bloch–de Jong–Sertöz2206.01220v2
§§2,4,5.4. These completed source checks should not be restarted
as pending work.

The next mathematical target remains CM-Mixed-Derived §9:
one rational framed element with the exact localizations and real
regulator ell_E/(2Omega_E), with rationality as a conclusion.
No further bounded mathematical task has been dispatched here.
The withdrawn local identification C_v=H_v/2 must not be restored
from the separate global height identity.
