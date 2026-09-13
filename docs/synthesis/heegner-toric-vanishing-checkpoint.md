# Rank-sensitive vanishing of the actual two-prime toric coefficient

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own only heegner-toric-vanishing-attack.md and this checkpoint.
An initial checkpoint was saved before research. The bounded construction
is now completed and passed
[independent review](review-heegner-toric-vanishing.md).

The active parent objective remains full BSD for every elliptic curve
over Q. This bounded task attacks the still-open LR-TP5 vanishing,
not a replacement objective. No shared synthesis edits, agents or
old numerical reruns are authorized for this task.

Historical assignment, now completed: read research-state.md, next-research-plan.md §1,
heegner-local-reciprocity-attack.md and its review, and
two-prime-heegner-height-attack.md and its exact character-height formula.
Construct and test an actual geometric, level-raising or
derived-reciprocity operation linking the weighted two-prime
toric coefficient to the extra untwisted derivatives vanishing
at odd analytic rank >=5. Preserve primitive conductors,
missing-prime factors, full p^k coefficients, modular degree
and all residual/ramification hypotheses.

The prior construction already realizes the coefficient as a
Frobenius value of an actual cyclic p^k-isogeny cover on the
supersingular locus. Do not repeat an abstract norm-relation
model or merely restate its equivalent vanishing. If the new
operation leaves a term, compute it on this actual object.
Root separately handles the compact-support/Gysin bridge.

All source inputs must be checked in primary versions. Save
full arguments and the first exact unresolved comparison;
new deductions need independent review before promotion.

## Completed and independently reviewed construction

The complete proof is now heegner-toric-vanishing-attack.md §§1–7.
It tests an actual level-Nv degeneracy lift, not an abstract norm model.

- Lift the weighted conductor-m CM divisor to an actual z in
  J0(Nv)(H_mv), with degeneracy images P=P_m and Y=Atilde_m y_mv.
  Its norm is alpha^*Z_m + v*aug(A_m)*([1/N]−[infinity]).
  The cusp term is computed from alpha^*(infinity)=infinity+v[1/N].
- On the f-old E² block, q_v j = d_pi Delta_v with
  Delta_v=[[v+1,a_v],[a_v,v+1]], determinant d_v=(v+1)²−a_v².
  Rational projection has the exact denominators d_pi(v+1±a_v);
  the complement is not called purely v-new without a further
  valid Hecke localization. Its other-old norm term is retained.
- The actual cofactor points are
  B1=((v+1)P−a_vY)/p^k and B2=((v+1)Y−a_vP)/p^k.
  These are integer linear combinations of points. Norm B2=0.
  The cleared complementary point W=d_pi*d_v*z−p^k*j(B1,B2)
  is automatically p^k-divisible, without analytic rank five.
  Dividing its known factor once leaves −j(B1,B2) modp^k.
- For x=delta_v(Pbar), the actual reductions are exactly
  B1bar=−x and B2bar=−Frob_v*x in Etilde[p^k].
  Thus B2bar contains the entire finite toric test (with its sign),
  despite norm zero. B2 is also the specified correction term in
  the three-prime raw cocycle. u2=u3=−1 and the finite/transverse
  conjugation actions are retained.
- Attempting to prove B2 torsion by positivity leaves an exact
  Gross–Zagier character sum supported ONLY on characters ramified
  at the new prime v. Formula(19) retains d_pi,8π²(f,f),sqrt|D|,
  p^(2k)h_m², primitive conductor c_chi, and every missing-prime a_r².
  B2 has zero projection on characters trivial at v.
- The removed untwisted local Rankin Euler polynomial satisfies
  Q_v(1)=d_v/v²; under vanishing through order2,
  (L^(v))'''(1)=d_v/v² L'''(1). This is a complex identity,
  not a reduction of L''' modulo p^k. Clearing its matching
  degeneracy denominator kills every finite test automatically
  and does not eliminate the cofactor reduction.

First exact unresolved arithmetic step TV-TP5: use the extra
untwisted third-derivative vanishing to prove B2bar=0 for every
detecting fresh v. Proving B2 torsion would suffice but is
stronger than needed and has not been established; its actual
height contains the explicit v-ramified first derivatives.
No vanishing or new rank bound was proved.

Primary passages read directly again: Bertolini–Darmon
Euler systems and Jochnowitz congruences, AmerJMath121(1999)259–281,
author §2/Prop5.1; Howard1202.6340v1 §1.7;
Cai–Shu–Tian1408.1733v2 Theorem1.1.
The existing full-image hypothesis is retained only for the
reviewed detection conclusion. Root has an unreviewed possible
irreducibility-only extension using Lawson–Wuthrich; do not
promote that extension until its independent review is saved.

The final PASS review covers all seven sections, against mathematical
revision 56a1027562e985a6da108d03a3eb510bcf757f93f9c8f2960fb5945036721fc1.
Subsequent review links and status changes are editorial.
The separate assigned integrated-spectral review is also completed
PASS in review-integrated-spectral-comparison.md, including its new
rational K2 divisor construction.

Next mathematical target remains TV-TP5: an actual rank-sensitive
comparison proving the specified B2 reduction zero, while retaining
its surviving primitive v-ramified character sector. No such
comparison or vanishing was obtained. Do not rerun the completed
proof or review merely from stale earlier status wording.
No shared synthesis or old numerical scripts were edited.
