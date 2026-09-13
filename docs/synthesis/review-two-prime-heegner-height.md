# Coordinator review of the two-prime Heegner construction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
**PASS for all seven sections of
[the repaired construction](two-prime-heegner-height-attack.md).**
Reviewed mathematical revision SHA256:
`9491533a6e28ede69570563e8354267c6d206b2ab4d20c7388060b8dfab91d51`.
Subsequent review links and checkpoint edits are editorial.
The raw descent, primitive toric heights, actual maximal-order lattice,
and full-p-power connection to O5 are all verified. The latter uses the
new on-page scalar normalization; it does not extend a non-equivariant
local coefficient matrix to global cohomology. No old certificate was rerun.

## Checks already completed

- The ring-class kernel factors have orders ell+1 and q+1, since the
  unit correction is one in the stated discriminant scope. No splitting
  of the class-group extension or p-prime class number is assumed.
- H_m/Q is Galois and unramified at p. A nonzero rational p-torsion
  subspace would be G_Q-stable, hence all E[p] by irreducibility; the
  Weil pairing contradicts unramifiedness via μ_p. This proves the
  exact torsion-free hypothesis for inflation-restriction, without
  importing Howard's stronger global surjectivity assumption.
- The telescoping equality, transversal invariance modulo p^k, actual
  point P_m, explicit division cocycle and equivalence of raw-class
  vanishing with p^k divisibility are valid. Choice changes in the
  transversal do not affect that residue class.
- Root read [Cai–Shu–Tian, 1408.1733v2, Theorem 1.1](https://arxiv.org/html/1408.1733).
  Its elliptic-quotient version has precisely degree(π) in the numerator
  after solving for the height, with 8π², primitive conductor c, sqrt|D|
  and Petersson norm as in the draft. The units and common-discriminant
  factors are one in the stated scope. The following BSD conjecture
  in that source is not used.
- Orthogonal character decomposition and tracing missing conductor
  primes give b_χ=product a_r, not omitted Euler factors. The trivial
  component is (a_ell a_q ell q/4)P_K; other conductor-one components
  are killed by the class-group sum. Complex fifth-order vanishing
  gives that trivial-component consequence, not a height divisibility
  criterion for an unspecified cohomology lift.
- Evaluation of the actual derivative operator in every p-adic
  character gives valuation at least e_ell+e_q−2/(p−1), hence at least
  e_ell+e_q−1 for p≥5. It therefore acts divisibly in the maximal order.
  The enlarged Mordell–Weil lattice is finite over the original lattice.
  Its Tor exact sequence injects C_m[p^k] into M_m/p^k M_m and sends
  the explicit theta_m to P_m. This proves the full-p-power equivalence
  with raw-class vanishing, including G-invariance and depth p^t C_m.
- Fourier inversion gives h_m O_max⊂Z_p[G] and the stated conductor
  exponent; its shortfall against the sufficient annihilator is
  v_p(h_K)+k+1. This is an actual lattice quotient, not the previously
  tested model module. The stronger exponent bound remains a gap.

## Exact normalization repair and final connection to O5

Root read [Howard, 1202.6340v1, §1.7](https://arxiv.org/html/1202.6340v1),
including Proposition 1.7.4 and Theorem 1.7.5, and
[BCGS, 2312.09301v2, §1.1.2](https://arxiv.org/html/2312.09301v2).
BCGS first defines the raw descended class exactly as in this note and
then mentions a slight modification without changing its notation.
The final proof now supplies its own precise scalar normalization.

The CM lattice argument verifies the conjugation sign directly. Dualizing
the degree-N CM isogeny sends the ideal class associated with N_c to the
conjugate CM point, since N^(-1)N_c equals its conjugate inverse ideal.
The Fricke action on the elliptic newform quotient is ε₀=−w(E).
Changing the base cusp adds a cuspidal torsion point, which is zero
modulo every p-power here because there is no p-primary torsion.
This proves the required relation up to an innocuous Galois translate.

Conjugation inverts every ring-class group element. The exact identity
τD_vτ^(-1)=(v+1)(N_v−1)−D_v reduces to −D_v at the full common
p-power. Inversion and a Galois translate only replace the transversal
by another transversal. Its residue class is unchanged by the earlier
invariance calculation. Hence the raw cohomology class has genuine
conjugation eigenvalue ε_r=ε₀(−1)^r. Root also checked the stated sign
against [Jetchev–Lauter–Stein, 0707.0032v1, §3.2](https://arxiv.org/html/0707.0032),
which uses exactly ε=−w(E) and ε(c)=ε(−1)^number-of-primes.
No stronger global Selmer theorem from that source is imported.

For the local coefficient map, put F=Frob_v and a=a_v. The exact
characteristic-polynomial calculation is

    a−(v+1)F = (F−a)(F²−1).

If p^kV=U is a local division point, finite Kummer evaluation is
x=(F²−1)V. Howard's finite-group operation is therefore (F−a)x=Fx
modulo p^k. This also proves its coefficient-level compatibility and
explains why it cannot simply be declared a global G_K-equivariant
coefficient endomorphism.

The proof instead uses simultaneous conjugation on cocycles:
(C_hc)(g)=h c(h^(-1)gh). Any local lift of rational Frobenius represents
the same global outer conjugation class, because it differs from τ
by an element of G_K. The latter's simultaneous action is trivial on
cohomology. At finite evaluation h², this action is F. At transverse
evaluation it is v^(-1)F=−F, since h^(-1)σ_vh=σ_v^(v^(-1)).
Coboundaries vanish at these evaluation elements because they act
trivially on E[p^k]. Thus the transverse sign is explicitly retained.

Applying finite evaluation to the raw conjugation eigenclass turns
the local finite-singular factor into ε_r on that class. Define

    u_r=ε₀^r (−1)^(r(r−1)/2).

The direct recursion u_(r+1)ε_r=u_r normalizes every edge. It is
independent of the fresh prime and compatible with every common
coefficient quotient, so it produces an actual Kolyvagin system.
Multiplication by these scalar units preserves all propagated and
transverse local conditions, zero entries and divisibility indices.
For r=2, u₂=−1. This proves the repaired equation (11) and the
vanishing equivalence used by the actual theta_m construction.

The argument establishes a valid explicit normalization of the raw
Heegner system. It makes no claim that an unspecified source convention
has exactly the same scalar at every index. Its unit equivalence is
sufficient for the previously reviewed first-nonzero-index/O5 criterion.

## Final scope

The candidate divided point now exists in the actual maximal-order
Mordell–Weil lattice, and its failure to lie in the original lattice
is exactly the finite quotient element theta_m. The Tor injection and
Kummer restriction identify its vanishing with O5 at the full p-power.
The elementary conductor bound remains too weak by the recorded exponent.
Neither the primitive character height identity nor rational character
projection controls that missing integral descent. Fifth-order untwisted
vanishing reaches the trivial character but has not been shown to kill
this quotient element.

GAP TP5 remains the stated integral divisibility for every auxiliary
pair under the analytic-rank-five hypotheses. This review proves neither
that condition nor full BSD. No height is assigned to an unspecified
cohomology lift, and no complex height is reduced modulo p^k.
