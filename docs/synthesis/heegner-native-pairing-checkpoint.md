# Heegner native pairing checkpoint

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own this file and heegner-native-pairing-attack.md only.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-native-pairing.md](review-heegner-native-pairing.md).
Reviewed mathematical revision:
e67fb3c138b5425cf3b95fa41feb0349f62a8c59ffc23e9fd9eff126da19bcfd.
All seven sections and the exact dual twist transport passed.
NP-TP5 and the full universal BSD objective remain open.

The separate radial graph review is also completed **PASS** in
[review-radial-graph-correction.md](review-radial-graph-correction.md),
against mathematical revision
e843569799237cf2022f0103527046e091390379055aef65ea1e13d597c8cf99.
Its rational spectral lift remains open. No further expansion of
the present proof is assigned; the next bounded construction should
start from the exact native scalar NP-TP5 retained below.

## Historical initial and progress checkpoints

The entries below preserve the initial checkpoint and research
handoff. References below to pending review are historical;
the completed verdict and current assignment are stated above.
The initial checkpoint was saved before research.

Universal objective: full BSD for every elliptic curve over Q.
This bounded task constructs an actual transverse twist test generator
or presentation and evaluates the compact pairing for the corrected
Kato input. Global first cup annihilation is completed work.

Retain the full p^k coefficient, extra p∤h_K hypothesis, native
point-image conditions, compact-FIRST Weil product, d0 valuation
and its surjective/Manin scope, all nonclean J_i,v groups, and
the p-relaxed twist zeta defect. A clean twist Selmer-zero case
still has transverse test group R. Do not replace it by zero.

Next: read next-research-plan section2 and the reviewed tame proof,
construct a normalized actual generator, and calculate its particular
pairing value. Native and mixed-lift ambiguities must remain explicit.
No finite Sha hypothesis for E, p-adic/complex derivative identification,
shared synthesis edit, extra agent or old certificate rerun is allowed.
Every new deduction requires independent review.

## Material construction under development

In the clean case Sel_(p^k)(E^D)=0, finite Poitou–Tate
gives an actual isomorphism
H1(U,M_D) -> direct-sum_v H1(Q_v,M_D)/F_v.
Proof: its local image K and the product finite group F
are self-annihilating, K∩F=0, and the global localization
kernel is a subgroup of the zero Selmer group. Hence
K+F is the entire local group and the map is bijective.

The unique inverse C constructs b_i as the inverse of
the vector with prescribed primitive singular coordinate
at old i and zero at every other place. Local isotropy
forces its finite component at i to be zero. This is
the actual transverse generator, with no arbitrary scalar.

For a global first primitive t and the native local
primitives tau_v, let delta_v=tau_v-loc_v(t).
Correct t by C(q(delta)), where q is the quotient by
the classical finite condition at every place. All
remaining differences are finite. The native obstruction
is then a SINGLE old finite Frobenius coordinate, paired
with b_i; other local terms vanish by finite self-duality.
This coordinate is invariant under changing t or native
local representatives. It is not yet proved zero.

A finite arithmetic localization matrix gives its exact
Schur-complement/bordered-determinant expression whenever
the local quotient groups are free; otherwise retain their
Smith presentations and solve congruences without nonunit
division. This removes the unspecified global three-cochain
from the prior pairing formula but does not yet identify
the remaining entry with a complex central derivative.

The actual rank-zero Kato class should furnish the p-coordinate
generator after proving the local Coleman augmentation is a
primitive pairing with exp(delta0). In the clean surjective
case d0 is a p-unit, so this normalization divides only a
proved unit. Its cross-local coefficients are then tied,
by global reciprocity, to the local formal logarithm of b_i.
This local normalization/source check is the current next step.

## Full proof saved for independent review

heegner-native-pairing-attack.md §§1–7 is now saved.
All new deductions remain unpromoted.

Completed constructions:
- A unique actual finite localization inverse C in the
  clean classical twist Selmer-zero case.
- A normalized transverse generator b_i, and the actual
  p-generator b_p=z_D0/d0. The primitive local pairing is
  proved without CM splitting; the explicit Kato p-Euler
  factors cancel with k_alpha^(-1) to give d0 exactly.
- The pairing equals R_i(z)/p^k, where R_i is ONE old
  finite Frobenius coordinate after the global correction
  C(q(delta)). Its finite localization-matrix expression
  is a bordered determinant divided only by a proved unit.
  Nonfree local groups retain Smith presentations.
- Actual cross-local coefficients satisfy skew reciprocity.
  The p cross coefficient is minus the formal logarithm
  coordinate of b_i at p. A proposed z_D0 correction
  changes the old term and p-term by opposite amounts,
  so its net effect on the native value is EXACTLY ZERO.
- The finite norm cokernel at the old ramified prime has
  mod-p^k quotient R². Thus BD1995's local norm-surjectivity
  hypothesis fails on this actual extension; its
  universal-norm height theorem cannot kill this test.
- If native values vanish, permitted first-lift changes
  are the actual lambda_i b_i. Their mixed old-local
  coefficients are the actual G_ell,q and G_q,ell with
  opposite signs; nonunits remain uncancelled. A global
  E-valued obstruction and actual top Heegner ambiguity
  remain after local corrections.

The particular coefficient R_i(d0 P_AB(w_k)) has NOT
been proved zero from L'''(E,1)=0. This is recorded
explicitly as NP-TP5, not hidden by the finite evaluation
formula. No finite Sha assumption for E is used.

Primary source checks: Milne ADT2 local and finite
Poitou–Tate duality; BKS1910.07404v2 delta_n/finite
Coleman normalization; BCGS2312.09301v2 Theorem3.2.2;
Bertolini–Darmon, Derived p-adic heights, published
AJM117(1995), pp1517–1554 (39-page PDF with cover),
§§1.1–1.2. Its exact norm hypothesis was read directly.

Next: higher_period_integrality independently reviews
this proof. The author will review the assigned stable
radial-graph-correction-attack.md in the separately
owned review-radial-graph-correction.md. No old script
or shared synthesis was edited.

Reviewer normalization precision applied: the inherited
class map is A=u_iota^(-1)iota_*, while the first-slot
point frame is A^(-dagger)=u_iota iota_*. Lemma3.1
is first proved on T_D; all M_D formulas then use
these dual transports. The local point in(14) is
explicitly the inverse-dual-transport of loc_p(b_i).
The exact pairing remains d0, with no unit suppressed.
