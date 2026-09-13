# Heegner cofactor-lift checkpoint

Date: 2026-09-13. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this file and heegner-cofactor-lift-attack.md.
Initial checkpoint saved before new research; its exploratory entries
below are historical. The bounded construction is now complete and
all nine sections passed [independent review](review-heegner-cofactor-lift.md)
against mathematical proof
1069acaa79900311139625292de131d1e4d380f768f6d9464cd43d42c995150d.
The reviewed checkpoint was
5c05af2ae207045245f2c50eb0ae0551e445003b63655e586f3e7dc0aa7eabe7;
the present status/link updates are editorial only.

Full BSD over Q remains the universal objective. This bounded task
seeks integral lifts or an actual point-local norm preimage for the
particular corrected Kato input, retaining the FIXED cofactor A,B and
their Bockstein defects. Changing those classes is not authorized as
a normalization unless preservation of the actual target is proved.

Inputs already completed: the reflection-field isogenies and native
CT comparison; epsilon_C of exact order p^k; no one-step coefficient
map; the combined global norm Bockstein including beta_E(A),beta_E(B).
Those do not determine the value of its particular cup.

Retain full p^k,d0, half-to-unhalved norm, compact-FIRST coefficient
pairing, contragredient point transport and all nonclean conditions.
No finite-Sha premise, selected rational Kato point, or complex/p-adic
derivative identification is supplied. Mixed/top selection remains.

Historical first checks: in the additional primitive-Heegner-class case, combine
the already proved finite Selmer structure with s_p>=3 to test whether
EVERY fixed A,B has an integral Selmer lift, without Sha finiteness.
Then test an actual thicker Heegner Shapiro quotient for a native lift,
retaining the exact old-prime residue and coefficient relations.
No old scripts, shared/completed-proof edits or new agents.
The resulting deductions have now received the review linked above.

## Historical internal progress: positive integral-lift subcase

Assume additionally that the ACTUAL two-prime class kappa has orderp^k.
The reviewed higher-residue theorem gives H=Sel_(p^k)(E/Q)=R³.
The known corank lower bound is s_p>=3. Since H is canonically
Sel_(p∞)[p^k] (global p-torsion iszero), the finitely generated
Pontryagin dual must have rank3 and no finite summand: an extra
finite summand would add nonzero p-torsion to H. Thus Sel_(p∞)
is divisible of corank3. This does NOT assert rankE=3 or finiteSha:
Sha may retain a divisible contribution.

The inverse limit with multiplication-p transition therefore gives
an actual free rank3 integral point-local Selmer lattice, with
surjective reduction at every finite level. Every FIXED A,B lifts;
no replacement or adjustment of their finite classes is made.
The actual d0-weighted cofactor consequently has an integral Selmer
lift. Its global norm obstruction is epsilon_C cup that lift, with
beta_E(A)=beta_E(B)=0 now proved in this subcase. Changing any
integral lift or scalar representative adds p^k times an integral
Selmer class, which changes this cup byzero because epsilon_C has
exact orderp^k. This gives a canonical PARTICULAR cup despite
noncanonical integral lift choices. Its vanishing remains unproved.

Outside the primitive subcase, the appropriate intrinsic lift defect
is the image in Sel_(p∞)[p^k] modulo its maximal-divisible subgroup's
p^k-torsion. Its cofactor value retains the fixed A,B images. This
is stronger than silently interpreting ordinary-global Bockstein
vanishing as point-local Selmer liftability; the distinction is
spelled out in the completed proof.

## Completed and independently reviewed nine-section construction

[heegner-cofactor-lift-attack.md](heegner-cofactor-lift-attack.md) is complete
and passed the separate review. The earlier progress text is historical.

Current results:

- Proposition2.1 constructs the canonical POINT-LOCAL integral-lift
  defect delta_n:Sel_n→F_E[n], F_E=Sel_(p∞)/Div, retaining fixed A,B.
- For nonzero actual kappa of order p^s in coefficient p^k, Kim's
  LARGER-corank plus structure formula gives exponent(F_E)≤p^(k−s),
  using the SAME Selmer-defined indices and the second displayed
  line's inequality M2−M3=a_3^-≥0 at nu2 and corank difference3.
  No initial opposite-sign error value or total-order formula is used.
  The source is2203.12161v7,12Jan2024. Ambient-H1 monotonicity is
  not substituted for these modified-Selmer divisibility indices.
- For z=d0(Dwk−aA−bB), its defect is−d0(a deltaA+b deltaB).
  Formula(9) gives an explicit annihilating exponent and formula(11)
  constructs an integral Selmer lift of exactly p^r z. No nonunit is
  canceled. In the primitive case r=0, the FIXED A,B and z all lift,
  without proving a rational-point premise or finiteSha.
- The resulting particular Prym cup epsilon_C cup w_(z,r) is
  independent of all integral lift choices, since n epsilon_C=0.
  Its vanishing and the native norm condition remain unproved.
- A genuine cubic Heegner quotient R[X_i,X_j]/(X_i^3,X_j^2) gives
  a UNIQUE actual first lift H_i of raw kappa in the ideal X_iX_j,
  identified with N_i. A single-prime cubic quotient gives eta_i,
  the plus-projected quadratic point moment with weight j_i(g)^2/2.
- Exact local H0 algebra proves H_i native at its own old i, while
  its only other-old-prime defect is the transverse TOP M_D line.
  To fix that coefficient, restriction is made GLOBALLY to the field
  H_i, where X_i² extraction is equivariant and E(H_i)[n]=0.
  Uniqueness there identifies the top with MINUS the raw j derivative
  of the actual quadratic-moment companion. This avoids inferring a
  transverse class from a noninjective LOCAL restriction.
- Howard's actual norm/congruence and raw cofactor give
  t_(i;j)=−a_j^+(eta_i), with K-Frobenius square and the fixed beta_j
  point frame. Projection of BOTH the raw moment/cofactor and its
  finite value is explicit; finite/transverse conjugation signs differ.
- Correcting by the existing b_j gives
  R_i(kappa)=−a_j^+(eta_i)G_ij. In the primitive clean case, unchanged
  z=alpha_z kappa gives R_i(z)=−alpha_z a_j^+(eta_i)G_ij, retaining d0.
  No factor is canceled or asserted zero. Nonprimitive z is not
  declared cyclic, and nonclean extra local groups are not suppressed.

Exact remaining gap: Cofactor-TP5 in§9. Control the PARTICULAR product
or canonical cup from the extra complex zero, with nonprimitive and
nonclean scope. No complex/p-adic derivative identification, finiteSha,
selected rational Kato point or mixed/top selection has been assumed.

Primary versions checked: Kim2203.12161v7 §2.1/2.3/Thm3.3,
including the second displayed line at i1, nu2, corank difference3;
BCGS2312.09301v2 CorA (not ambient-index monotonicity);
Howard1202.6340v1 §1.7 point norm/congruence and Lemma1.7.2,
with the already repaired scalar raw/standard convention.
No old script, certificate, prime scan or extra agent ran.

## Completed reciprocal reviews

The cofactor construction and both reciprocal reviews are complete.
The reciprocal asymmetric CM ray review is completed **PASS** in
[review-cm-asymmetric-ray.md](review-cm-asymmetric-ray.md), against
mathematical revision
7a9904d53c63062f29439b83b278ec28e0d6891b2aba08580268e815188804ed.
All nine sections were checked; the arithmetic tame-residue scope
was clarified, with no norm or scalar formula change.
No further expansion of the cofactor proof is currently assigned.

The next reciprocal review is completed **PASS after the integral
descent repair** in
[review-cm-local-point-comparison.md](review-cm-local-point-comparison.md),
against the coordinator's five-section proof revision
8fad3936741f7be8ff173ffb91c5da99036e94a55545eec685a21c56c975b5b8.
The audit checked the matched period, full semilocal trace, integral
derivative limits and the actual finite flat H1 injection with modulus
p^(k+1). It proves the stated exact local logarithm formula, without
asserting higher-coefficient or three-point-defect vanishing.
The checkpoint's subsequent coefficient leads and new finite-field
test are outside that verdict. No mathematical edit was made to
the cofactor proof during those reciprocal audits. Its subsequent
source repair and final review are recorded below.

## Completed cofactor source repair and final PASS

Odd's independent audit identified that the previously cited BCGS
monotonicity measured ambient H1 divisibility, while equation(7) uses
Kim's conductor-modified Selmer divisibility. The author directly
reopened Kim2203.12161v7 §2.3 and Theorem3.3. Its second displayed
line gives M2−M3=a_3^-≥0 for these exact SAME indices, so the proof
now obtains a_1^+=M3−M4≤M3≤M2≤k−s without comparing filtrations.
The M2 bound is explicitly checked by reducing the actual class
from T/I_(ell q)T to coefficient p^k and using its exact order.
This is the sole mathematical source/proof repair. All subsequent
annihilator, integral lift, local cofactor and native product formulas
are unchanged. Odd inspected the amended proof and checkpoint and
saved the final all-nine-section PASS in
[review-heegner-cofactor-lift.md](review-heegner-cofactor-lift.md),
SHA2563ce0ff3bc050890b4a69aef346a88731cf27c42cbfe8721cca2e9b9a8fc8a586.
The coordinator also read the final review and directly checked
Kim's index3 positivity. No mathematical correction remains.
No further construction is currently assigned; retain the open
Cofactor-TP5 product/cup vanishing and mixed/top selection targets.
