# Higher even-index Heegner classes in the signed residue presentation

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own only heegner-higher-residue-attack.md and this checkpoint.
Status: completed and independently reviewed **PASS** in
[review-heegner-higher-residue.md](review-heegner-higher-residue.md).
All eight sections of the [proof](heegner-higher-residue-attack.md) passed.
Reviewed mathematical revision:
627ab2762db0c56c94ee8eac3cff963e2dfb21ed2b0e5c89419df89adfc900f6.
The coordinator also checked the corrected proof and reconstructed the
joint-image and conditional cyclicity arguments. No further mathematical
task is assigned this round. The exact HR-TP5 comparison below remains open.

## Historical assignment snapshot

The following initial checkpoint was saved before source research;
its instructions record the completed assignment, not pending work.

The parent objective remains full BSD for every elliptic curve over Q.
This bounded task uses actual higher even-index Kolyvagin classes in
the independently reviewed signed Gysin residue presentation. Compute
their full-p^k residue vectors, with raw/standard scalars, declared
tame generators and the Q/K factor two, and relate them to the actual
trace-zero cofactors B2 from the preceding level-Nv construction.

Read next-research-plan.md §1 and heegner-gysin-bridge.md with its
review and signed-convention correction before using the presentation.
The reviewed Theorem6.3 now removes the earlier full-image restriction;
do not preserve that old restriction as if still necessary.

Aim at the actual B2 reduction vanishing under analytic rank >=5.
Do not count the old norm, parity, denominator or character-height
calculations again as new progress. If the higher-class operation
leaves a term, compute it on the actual classes, not a model module.

Verify primary inputs and save full arguments plus the first exact
unresolved step. All new deductions require separate review.
No shared synthesis edits, new agents or old numerical reruns.
Root separately studies the integral arithmetic K2 divisor.

## Completed, reviewed construction

The main proof is now saved in heegner-higher-residue-attack.md §§1–8.
All formulas and the conditional strict Selmer cyclicity proof are
written there and have received independent PASS review.

The corrected signed Gysin proof/review and next plan§1 were read.
The previously full-image-only detection is now available under the
original irreducible O5 assumptions by reviewed Theorem6.3.
Primary Lawson–Wuthrich1505.02940v2 and Howard1202.6340§1.7
were opened directly; the proof uses their exact scopes.

Exact residue calculation for an even fresh subset J of T:
b_J is the Q-descent of raw κ_(m productJ), which lies in B_T.
For v∈J, set n_v=m product(J minus v) (odd number of factors).
Use the actual cofactor B_(n_v,v)=((v+1)Y−a_vP_(n_v))/p^k.
Let ζ_v=δ(v)(σ_v), a primitive root, and let y_v:μ_(p^k)→V_v^−
be the Weil-dual of the chosen plus functional. If
Bbar_(n_v,v)=h_(J,v)y_v(ζ_v), then the POSITIVE tame residue
of b_J is −h_(J,v)y_v. Thus
sum_(v∈J) h_(J,v)[G_v(y_v)]=0 in the strict Selmer dual.
Pairing the base raw κ gives sum h_(J,v)a_v=0 modp^k,
where a_v is its actual K-local toric test. Before multiplying
by the p-unit2, the pairing is divided by2p^k.
All higher standard signs are u_(2+|J|); for four primes u4=+1,
whereas u2=u3=−1. Tensors are stripped only for coordinates.

Completed concrete operation:
If base κ has orderp^k, choose a detecting v_i so a_i is a unit.
The actual three-prime class κ_(m v_i) has minus sign and orderp^k.
Joint Chebotarev chooses v_j with base a_j=0 and the minus
finite value of κ_(m v_i) a unit. The four-prime residue relation
then forces h_ij=0 and gives [G_j]=0 in the strict dual; [G_i]
survives because its pairing with κ is a unit/p^k.
Adding an arbitrary second strict Selmer class to that joint
Chebotarev construction proves S_m^str=Rκ in this full-order
case (Theorem6.1). Its proof subtracts the unit-localization
multiple ofκ, then uses a triple joint Frobenius choice and
the actual four-prime relation to exclude a nonzero difference.
This is a finite Euler-system upper-bound reconstruction, not
rank-five vanishing. No divided class is substituted for an
actual raw Heegner class in the nonprimitive case.

Joint image proof under irreducibility: K is disjoint from the
torsion field. The image of G_K contains a matrix acting as complex
conjugation; its two idempotents and irreducibility yield all
matrix units overR. For classes spanning an internal direct sum
of cyclic modules of ordersp^(s_j), restriction injectivity and
the double-annihilator identity force joint translation image
product_j p^(k−s_j)V. Their plus/minus rational descents then
allow simultaneous hτ Frobenius prescriptions.

Nonprimitive case retained: if κ has orderp^s, a_i has exact
orderp^s, and κ_(m v_i) has orderp^(s') withs'≥s, choose v_j
with a_j=0 and h_ji of exact orderp^(s'). Reciprocity gives
h_ij∈p^sR, not h_ij=0. These are explicit higher-cofactor
terms; no division by a nonunit is allowed.

There is always an actual free R subgroup in strict Selmer:
the reviewed s_p≥3 suppliesR^3 in Sel_(p^k), and the two old
good-prime Kummer targets each have rankone overR. Their kernel
containsR. Therefore higher relation vectors cannot span all
the fresh generators of the strict dual. The desired additional
rank-five control of the specific surviving κ remains missing.

Exact remaining HR-TP5: supply a rank-sensitive comparison using
the additional untwisted central derivatives to kill the specified
cofactor reduction, not the entire necessarily nonzero strict group.
The present residue relations and conditional cyclicity use only
the already-known odd-rank-three inputs. In the primitive case the
surviving value is the actual unit a_i=−lambda_i pr+ Bbar_(m,v_i);
in the nonprimitive case the explicit higher-cofactor term h_ij
is only known to lie in p^sR.

Independent review is complete for all new claims, including the
joint translation-image lemma under irreducibility, the exact
signed residue vector, and the conditional finite cyclicity proof.
There is no remaining review repair. Any future continuation must address
HR-TP5 rather than repeat the completed residue or cyclicity calculations.
Root identified and the author corrected the inline characteristic-
polynomial sign in Proposition3.1:
(a_v−F_v)(F_v²−1)=(v+1)F_v−a_v.
The cofactor definition, its reduction −F_v x, and all residue
and pairing formulas are unchanged.
No old computation was rerun and no shared synthesis edited.
