# Two-prime Heegner height attack: restart checkpoint

Date: 2026-09-12. Agent /root/uniform_witness, GPT-6 Astra/xhigh.
Own only [two-prime-heegner-height-attack.md](two-prime-heegner-height-attack.md)
and this checkpoint. This bounded construction is completed and passed
[independent coordinator review](review-two-prime-heegner-height.md).

The parent objective is full BSD for every elliptic curve over Q.
This bounded task attacks the O5 target in odd-rank-selmer-bridge.md:
under its full hypotheses, analytic rank at least five should force
the actual two-auxiliary-prime Heegner/Kolyvagin class to vanish.

Completed construction:

- Read O5, ledger §3, state/report and primary Howard §1.7,
  BCGS §1.1.2, Cai-Shu-Tian Theorem 1.1.
- Fixed m=ell*q, k=min(v_p(ell+1),v_p(a_ell),v_p(q+1),v_p(a_q)).
  The actual derivative point is P_m=S_G D_ell D_q y_m in E(H_m),
  for a declared class-group transversal and compatible CM points.
- Proved E(H_m)[p]=0 directly: H_m/Q is Galois and unramified at p;
  irreducibility and the ramified Weil-pairing determinant exclude
  any p-torsion. Hence exact Kummer descent and cocycle (8) work
  under O5 without adding Howard's older surjectivity hypothesis.
- Retained the local finite-singular map and the full p-power
  coefficient. Root's normalization audit found that Howard's
  compressed global-Xi wording should not be imported directly.
  The source/cohomology repair is now saved as Proposition 2.2:
  genuine complex conjugation gives raw eigenvalue
  epsilon_r=(-w(E))(-1)^r; local Xi_v=Frob_v at finite Kummer
  evaluation, whereas conjugation acts by minus Frob_v on the
  transverse evaluation. Scalar units
  u_r=(-w(E))^r(-1)^(r(r-1)/2) normalize every edge. In particular
  the normalized two-prime class is minus the raw class, with
  the declared tensor generators, so vanishing is preserved.
  No non-G_K-equivariant coefficient map is applied globally.
- Formula (16) is the exact height of this specified point.
  Each primitive ring-class character has its exact conductor,
  trace factors product a_r, derivative evaluations, class-degree
  denominator, parametrization degree and Petersson normalization.
  Heights use the unchanged Cai-Shu-Tian h_K convention.
- Untwisted central vanishing kills only the trivial character
  through this formula. The remaining terms have conductor ell,
  q, or ell*q and involve their own first derivatives.

Completed and independently reviewed positive integral deduction:

Let e_ell=v_p(ell+1), e_q=v_p(q+1), O_max the maximal order
of Q_p[Gal(H_m/K)], M=E(H_m) tensor Z_p and M_max=O_max M.
Proposition 5.1 proves A_m=S_GD_ell D_q lies in
p^(e_ell+e_q-1) O_max by exact root-of-unity evaluations.
Consequently Q_max=(A_m/p^k)y_m is in M_max.
Its residue theta_m in the actual finite C_m=M_max/M satisfies

  theta_m in C_m[p^k]^G intersect p^(e_ell+e_q-1-k) C_m,
  theta_m=0 iff the full two-prime Heegner class is zero.

The exact sequence (23) identifies the residue with the original
Kummer class. The elementary general bound
p^(v_p(h_K)+e_ell+e_q) C_m=0 misses the sufficient exponent
by v_p(h_K)+k+1. No rank-five improvement has been proved.

Exact remaining target TP5, equation (26): under O5, descend the
constructed Q_max from M_max to M for every auxiliary pair.
The actual finite-character pairing formulation (27) is equivalent;
no complex higher-derivative comparison computing those finite
values has been constructed.

Root's final PASS covers all seven sections, including raw descent,
the primitive-conductor Gross-Zagier scalar, lattice §§5–6 and
the explicit normalization repair in Proposition 2.2.
Reviewed mathematical revision:
9491533a6e28ede69570563e8354267c6d206b2ab4d20c7388060b8dfab91d51.
The subsequent PASS links and checkpoint updates are editorial.
No height or lattice formula was changed by the normalization repair.

Next mathematical construction target remains TP5: prove the
specific theta_m vanishes by descending Q_max into the actual
Mordell-Weil lattice. No such vanishing has been obtained.
No old numerical computation has been rerun.

Do not repeat the existing formal norm-relation countermodel.
Seek an actual geometric vanishing argument or an exact comparison
sufficient for it. No new agents and no old numerical reruns.
Any further new deduction needs independent review. The active goal is
owned by root; no child goal manipulation. A fresh child goal
check returned null, which is not cancellation of the root goal.
