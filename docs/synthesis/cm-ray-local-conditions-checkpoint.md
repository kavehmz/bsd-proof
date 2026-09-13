# Local conditions of the actual CM ray derivatives: checkpoint

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only cm-ray-local-conditions-attack.md and this checkpoint.
The parent objective remains full BSD over Q. No new agents or old
numerical certificate reruns.

## Completed and independently reviewed

All eight sections of [the proof](cm-ray-local-conditions-attack.md)
passed the coordinator's independent [source and deduction review](review-cm-ray-local-conditions.md).
Reviewed mathematical revision:
39275d6deea6e97e3370e7ee1599a5001a386767e0bf89140499644b3343de34.
No mathematical repair was needed. Subsequent proof-header and checkpoint
completion edits are editorial. The former initial-source-work and
review-pending instructions are superseded by this completed status.

The assigned question is resolved positively: both actual integral
ray derivatives d_pi,d_barpi, their difference and every integral
combination satisfy the Selmer local conditions. This uses neither
the known Selmer property of their sum nor the ordinary global
c_pi-cup identities. No afterward chosen scalar or point correction
is introduced.

## General theorem and integral upgrade

For E/Q of positive algebraic rank and odd p, every class in
H¹(G_Q,S,V_pE) is finite locally. At each l different from p,
local H⁰ and H² vanish and the Euler characteristic gives H¹=0.
At p, the point-Kummer line has dimension one and is its own
annihilator. Global Weil/Tate reciprocity against one fixed
non-torsion rational point therefore leaves only the p-term.
The point has nonzero local logarithm and spans that finite line,
so the singular localization of every global class is zero.
This theorem is specifically over Q. It assumes no analytic rank,
Sha finiteness, or equality of global H¹ with Mordell–Weil.

The inverse-limit Kummer sequence proves the integral upgrade:
H¹(F,T_pE)/E(F)^p-completion = T_pH¹(F,E), a torsion-free group.
Thus the inverse image of rational H_f is exactly the integral
point-Kummer image, including possible local finite torsion.
Every finite reduction of an actual integral global class is Kummer.
This is not a statement about arbitrary finite global classes that
may lack compatible integral lifts.

## Exact application at both CM split places

Apply the fixed integral Shapiro map separately to d_pi,d_barpi.
The counit pr_pi res_K Sh(d)=d has no extra factor two.
Restriction and the CM projections preserve point-Kummer conditions.

At pi the T_pi component is formal and all rational H¹ is finite.
At barpi it is unramified and rational H_f is zero. Both actual
barpi localizations are therefore rationally zero. The potential
integral remainder is explicitly retained:

    H¹(K_barpi,T_pi)_tors = (alpha−1)^(-1) Z_p/Z_p.

For this actual E:y²=x³+39x, rational two-torsion and Hasse exclude
anomalous good p≥7; the saved a_5=−2 gives #E(F_5)=8.
Hence alpha−1 is a p-unit at every allowed good split prime.
Both barpi localizations are consequently zero INTEGRALLY and
at every finite level. No integral-zero conclusion at an anomalous
prime is inferred merely from rational zero in the general theorem.

The exact Coleman obstruction retains the audited normalization:

    phi nu=beta^(-1)nu, [omega,nu]=1,
    delta_0=k_alpha^(-1)nu,
    O_p(loc Sh(d_j))=[exp*loc Sh(d_j),delta_0]
       =(exp(delta_0),loc Sh(d_j))_p
       =(loc P,loc Sh(d_j))_p/(k_alpha log_omega(P))=0.

This division occurs only in Q_p. Integral and finite conclusions
come from Kummer saturation and the actual nonanomalous calculation,
not from inverting logarithms or Euler factors modulo p^m.
The absolute F versus Tate-twisted phi dictionary is unchanged.

Primary sources read and independently checked: Rubin I.3.3, I.4.1,
I.6.4/Remark6.6, I.7.3 and Appendix B; Milne ADT I.3.2–3.5;
BKS1910.07404 Lemma6.9, (6.3.1)–(6.3.2), the Coleman definition,
Lemma6.14 and the exact point/exponential equation in the next proof.
Links and precise scope are retained in the proof and review.

## Unchanged source data and remaining comparison

All actual theta norms, the UNNORMALIZED tame degree1152(p−1)²,
q_a(X,Y), the tau-odd branch, the specified ray generators,
X,Y→T, the finite exponent bound m+1, Betti coefficient and all
global Tor terms remain unchanged. No two-variable I-divisibility
or flatness is proved; the Tor₂/Tor₁ edge and N[X−Y] term remain.

The SUM still has the old exact projected determinant scalar.
Individual Selmer membership does not imply nonvanishing,
independence, or that each height projection lies on the Bockstein
determinant line. Possible Tate-module Sha directions remain.
GAP CM-Ray-BSD still requires the single rational framed element
and its real BSD realization. Rationality is a required conclusion.

This bounded task is complete. Root's separately assigned K2 draft
also passed the independent [arithmetic-divisor review](review-k2-arithmetic-divisor.md),
including the explicit local-at-389 rational comparison scope.
Any further CM construction must start beyond these proved local
conditions, without rerunning the old certificates or redoing this
global-duality argument.
