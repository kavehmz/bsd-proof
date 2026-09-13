# Relative modular cycle checkpoint

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Model: GPT-6 Astra, xhigh reasoning. The parent objective remains full BSD.

Current status: completed and [independently reviewed PASS](review-relative-modular-cycle.md).
The initial candidate and progress sections below are historical; resume
from the completed construction and RM-389, not the earlier verification tasks.

Owned files for this bounded task:

- `relative-modular-cycle-attack.md` (complete; independent review PASS).
- `relative-modular-cycle-checkpoint.md` (this file).

## Historical initial candidate — completed

Use the full basis P=(-1,1), Q=(0,-1) on389a1 and the already verified
regular plane-cubic model with every fiber irreducible. Set R=P+Q=(4,8).
For each basis point P_i form the degree-zero divisor D_i=(P_i)-(O),
and its translated representative D_i^R=(P_i+R)-(R). The supports of
each original divisor and each translated divisor are disjoint.
Explicit expected translated points: 2P+Q=(-51/25,-68/125),
P+2Q=(1/16,-9/64), to be checked by exact group law.

Construct the arithmetic Deligne/Poincare pairings of these four divisor
pairs, with canonical Green functions and finite intersections, and form
their alternating determinant tensor. First verify the precise height
normalization. Then combine with the relative cusp path from X0(389)
and identify a genuine relative/secondary regulator chain rather than
declaring its real period to be the desired central derivative.

The arithmetic model has no reducible fibers, so the usual vertical
orthogonality correction for degree-zero divisors should be zero; this
must be checked against the chosen intersection convention. No new
regulator comparison or integrality is claimed at this checkpoint.

The subagent get_goal remains null by documented scope. Existing research
and certificates are preserved; no old computation has been restarted.

## Material findings saved before further comparison

Exact rational group law confirmed R=(4,8), S=R+P=(-51/25,-68/125),
T=R+Q=(1/16,-9/64). Primitive projective coordinates are
O=(0,1,0), P=(-1,1,1), Q=(0,-1,1), R=(4,8,1),
S=(-255,-68,125), T=(4,-9,64).
The gcd of pairwise 2x2 minors gives all section intersections:
P with S,T,R:1,1,1; Q with S,T,R:3,1,1; O with S,T,R:5,4,1.
Therefore finite Neron-symbol matrix for D_i versus D_j^R is
I=[[-log5,-log4],[log3-log5,-log4]]. Every fiber of the regular
model is irreducible, so degree-zero divisor vertical correction=0.

Construct A={O,P,Q}, B={R,S,T}. H1(E\A,B;Z) is a rank6 integral
relative mixed Hodge structure with weights -2,-1,0, rank2 in each.
The exact algebraic third-kind differentials are
rho_P=(y+2)/(x+1)*omega and rho_Q=y/x*omega,
omega=dx/(2y+1). Their residues are +1 at P or Q and -1 atO.
For the real-normalized third-kind differential eta_i (all periods
pure imaginary), the matrix B_ij=Re integral_R^(R+P_j) eta_i
gives h_BSD(P_i,P_j)=B_ij-I_ij by Faltings-Hriljac.
Müller arXiv:1105.1719 Definition3.1 matches our BSD height:
limit 4^-n h_x(2^nP), with bilinear polarization divided by2.
Primary period/biextension comparison checked in Amini-Bloch-Burgos-Fresan
arXiv:1512.04862, authorPDF Theorems4.10-4.11/Prop4.12, and
Bloch-deJong-Sertoz arXiv:2206.01220 Theorem2.9.

Next comparison test: modular path image has a real elliptic logarithm
lift with both endpoints0 because L(E,1)=0. P,Q lie in the nonidentity
real component. A small imaginary translate of that lifted loop lies
in a simply connected horizontal strip avoiding all translates of A.
If verified fully, its holonomy for any descended flat connection is
identity, so even literal iterated regulators on this punctured E
cannot transport the nonzero Mellin second derivative. Must retain
scope to this specified pushed/regularized path and rational connections;
this is not a general impossibility theorem for secondary motives.

## Final construction and exact comparison test

Complete note saved. The principal corrections have been made into
actual rational cycles, not just torus-coordinate labels:

h1=1-332/(27(x-4))+1040y/(27(x-4)^2),
h2=1-41/(3(x-4))+20y/(3(x-4)^2),
Z1=(S)-(R)+div(h1), Z2=(T)-(R)+div(h2).

Their values at O,P,Q are (1,5,5/3) and (1,4,4), respectively.
Principal-divisor intersection shows i_p(D_i,Z_j)=0 at EVERY prime.
Vertical discrepancies between closure of generic div(h) and integral
div(h) are full fibers and pair to zero with D_i. The resulting actual
1-motive [Z²→J(E,A)] has free integral rank6 Betti lattice; its
real-normalized period matrix is exactly the full BSD height matrix.
The height sign and factor are fixed by Neron symbols with -log|f|
at the real place, matching Müller1105.1719v3 Def3.1/Thm3.2.

Full period formula: choose omega0=omega/omega1, tau=i t0, and
A_i=integral_a rho_i, B_i=integral_b rho_i.
eta_i=rho_i-(Re A_i-i Re B_i/t0)*omega0 has imaginary periods.
For boundary gamma_j=Z_j, h_BSD(P_i,P_j)=Re integral_gamma_j eta_i.
The target line detX⊗detL⊗Z gamma_R⊗Zomega sends its generator to
Omega_E*Reg_BSD, with gamma_R=2a retaining two real components.

Pullback to X0(389) gives actual noncuspidal modular cycles and
period matrix40H. The natural pushed cusp loop regularized as
F(y)+i epsilon contracts by (1-s)F(y)+i epsilon inside the strip
0<Im z<Im omega2/2. All flat holonomy and all holomorphic Chen-word
periods vanish on that specified loop. This does not cover other
path regularizations or higher objects retaining X0 data.

Further comparison test: any 1-motive map from the torsion-cusp
motive Mc=[Z→J0] to [Z²→E] has zero lattice map. Even Mc_Q tensor²
cannot map nontrivially to the top of wedge²M_Q: its weight0 splits,
whereas the target's first extension class is P⊗e2-Q⊗e1≠0.
These proofs are §§8–9; the remaining higher comparison is RM-389.

No L-value was used to choose cycles or their rational functions.
No leading-term rationality/integrality or full BSD was proved.
The independent review passed and the parent inspected its proof and scope.
The full-period Betti line's index two and the lifted chains' puncture
avoidance are explicit. No old certificate was rerun. The current next
task is the higher analytic-frame comparison RM-389.
