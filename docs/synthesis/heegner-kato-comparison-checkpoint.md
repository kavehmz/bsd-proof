# Heegner–Kato comparison checkpoint

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this file and heegner-kato-comparison-attack.md.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-kato-comparison.md](review-heegner-kato-comparison.md).
Reviewed mathematical revision:
84297adc102effbcc5a1d92bafef70330b832bd970c58b31913555e72aa0a64e.
All eight sections and the final old-prime cup map passed after
the cohomology-comparison repair recorded below.

## Historical assignment

The following initial checkpoint was saved before source work;
its action instructions describe the completed assignment.

The universal objective is full BSD for every elliptic curve over Q.
This bounded task seeks an actual comparison from the reviewed raw
two-prime Heegner class/cofactor, with its signed Gysin tests, to a
normalized cyclotomic Kato derivative or modular element. The full
p^k coefficient, primitive-character sectors, local conditions,
raw/standard signs and Q/K factor two must remain visible.

Read the current next plan and completed higher-residue proof/review.
Do not repeat total-residue-span: the actual strict Selmer group
contains a free R direction. The target is the specified Heegner
class, not vanishing of that whole group.

Next: inspect primary generalized Perrin–Riou/explicit reciprocity
comparisons and construct their actual source and target maps.
Retain conditional rank or Sha hypotheses; a p-adic derivative
is not identified with a complex derivative without proof.
If a comparison leaves a term, compute it on the actual objects.

No shared synthesis edits, agents or old numerical reruns.
Every new deduction requires separate review before promotion.

## Completed reviewed constructions

The full proof heegner-kato-comparison-attack.md §§1–8 is saved
and independently reviewed PASS.

Actual positive constructions:

- Kato12.4–12.5, global cohomology/base-change saturation and
  the known s_p>=3 give integral z_infinity=X²w_infinity.
  Kato18.4 gives F_E∈X³, so w0 is an integral Selmer class.
  The explicit normalization first uses the nonanomalous range.
- Published BDV22 Theorem4.2 gives the actual normalized BF
  class F_D z_E e_plus+F_E z_D e_minus. Its second plus
  coefficient is d0w0; its third minus coefficient is c3z_D0.
  The latter is zero over Qp exactly when c3=[X³]F_E is zero.
  d0 and the BF geometric normalization are not assumed units.
  The next plus jet retains a cyclotomic Bockstein cochain.
- Actual old-local determinants give a denominator-free map
  P_ab(w)=[a,b]w−[w,b]a−[a,w]b into strict Selmer. In the
  primitive-Heegner case its coefficient in Rκ is the exact
  ratio of fresh local tests(15); changing the old sections
  changes it by −t l_ell(w)−s l_q(w). No unit is proved.
- In the additional subrange p∤h_K, the genuine two-factor
  ring-class representation admits the quotient
  R[Y_ell,Y_q]/(Y_ell²,Y_q²). The Shapiro Heegner class is
  exactly Y_ellY_qκ_raw at full p^k. Actual norm factors
  kill its three lower coefficients; restriction injectivity
  and the top-ideal injection are proved.
- Attempting to extend the BF second cyclotomic jet in that
  tame representation produces actual twist-H² cup
  obstructions a_i cup(d0w_k), then the mixed cochain
  −a_ell cup t_q−a_q cup t_ell−a_ell,q cup(d0w_k).
  Neither these nullhomotopies nor their local conditions
  have been constructed. This is the explicit missing map.

The original O5 hypotheses do not guarantee p∤h_K or the
nonanomalous condition; their restricted uses are labeled.
The full irreducible Heegner/Gysin range is preserved.

Source findings that must survive restart:

- BDV is the published50pp Advances398(2022)108172 PDF,
  not the41pp preprint. Primary equations23–30/Theorems4.2–4.3
  were read. PDF4536fcf4... is /tmp/heegner-kato-bdv22.pdf;
  text extraction is the matching .txt.
- Kato primary cached PDF3c6e14b1... was inspected in
  Sections12.4–12.6 and18.4. The latter bounds the p-adic
  order by SELMER corank, so no main-conjecture equality
  or finite-Sha assumption is needed for F_E∈X³.
- BKS1910.07404v2 Hyp2.2 assumes finite Sha and uses
  r_alg−1. Its L_S^* is the actual leading term, not
  L'''/3! in a hypothetical rank mismatch.
- Longo–Vigni DOI10.1007/s40687-026-00646-7 was inspected
  directly: its p-TNC proof is analytic rank1 with specified
  regulator/AJ assumptions. It supplies no rank5 comparison.

Self-checks and separate review are complete. The exact
remaining mathematical target is HK-TP5 in proof§7.
No old script was rerun, no agent was spawned, and
no shared synthesis was edited.

## Final local refinement and reciprocal review

Self-checks and the last local calculation are saved.
Proposition6.3 proves that cup with the actual primitive
tame a_i identifies the old finite Kummer line with the
twisted local H² line. Thus the first BF lifting obstruction
at ell,q is exactly d0 times w_k's old local coordinates.
The determinant correction cancels those local terms but
leaves the global obstruction and other local conditions.
The Q/K trace factor2 is explicitly retained.

The assigned independent review by higher_period_integrality
is complete PASS. The reciprocal review of the higher
arithmetic theta construction is also complete PASS in
[review-higher-arithmetic-theta.md](review-higher-arithmetic-theta.md).
There is no pending review repair or further assigned
mathematical task this round.

Reviewer requested an explicit comparison omitted from §2:
Kato's j_*T Iwasawa complex and the full Galois complex are
compared at(X) using the bad-prime localization complexes.
Their rational augmentation fibers are acyclic by local
duality/Euler characteristic and the unramified/inertia
sequence; derived Nakayama then gives the isomorphism at(X).
The integral X-saturation argument separately uses the
full Galois coefficient sequence(5). This is now written.
No derivative, sign, or coefficient formula changed.
The third minus BF coefficient is also explicitly labeled
p-relaxed rather than a classical Selmer class.
The reviewer inspected both precisions and recorded no
remaining mathematical correction. The universal BSD goal
remains active; HK-TP5 and HAT-389 remain open.
