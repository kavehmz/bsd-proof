# Native Heegner height-comparison checkpoint

Date: 2026-09-12. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this file and heegner-native-height-comparison.md.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-native-height.md](review-heegner-native-height.md).
Reviewed mathematical revision:
75370e6e4a132e2b0311991e421770fbe97db56c2c030aed9c48ad213ab5c693.
All seven sections and the separate norm-Prym point subcase passed.
No mathematical correction was required. The particular classical
Cassels–Tate vanishing remains unproved, and the actual Kato input
is not assumed to come from a rational point. Full BSD remains active.

No further expansion of this proof is assigned. Any next bounded
construction should start from the exact torsors and pairing below,
while preserving the unresolved mixed/top Heegner ambiguity.

## Historical initial checkpoint

The initial and material-progress entries below preserve the research
handoff. Their pending-review wording and next actions are historical;
the completed verdict and current scope are stated above.
Initial checkpoint saved before the source search.

Universal objective: prove or disprove full BSD for elliptic curves
over Q. This bounded task seeks an actual derived-height, Rankin or
reciprocity comparison that evaluates the native obstruction R_i of
the corrected Kato input using the extra untwisted complex zero.

Completed inputs, not targets to rebuild: the finite localization
inverse C, bordered determinant, transverse generator b_i, primitive
p-generator, exact point-dual twist transport, and the cancellation
of a p-relaxed Kato correction in R_i. The classical BD universal
norm hypothesis fails at the actual old ramified prime.

Retain full p^k and d0, compact-FIRST Weil pairing, native transverse
old local conditions, the additional p-not-dividing-h_K coordinate
hypothesis, all nonclean local defects and source image hypotheses.
No identification of p-adic with complex derivatives, no finite-Sha
premise for E, no arbitrary old-local normalization or nonunit
cancellation is allowed. Preserve the mixed/top ambiguity until an
actual arithmetic map selects a lift.

Next: read next-research-plan section4 and the completed native proof
and review; select and check a primary derived-height or reciprocity
construction on these exact objects. Save each material calculation
and the first unresolved comparison, with independent review pending.
No extra agents, old numerical reruns or shared synthesis edits.

## Historical material construction before source/sign review

Let A_i=Res_(F_i/Q)E and use the ACTUAL fixed quotient
A_i[p^k]→N_i. If K_i is its kernel, B_i=A_i/K_i exists and
[p^k] descends to psi:B_i→A_i with kernel N_i. Kummer
naturality proves its local isogeny condition is exactly the native
Shapiro point image. This is a construction, not a hypothetical
replacement of the old local condition.

Factor psi through C_i=B_i/M_D. Then psi1:B_i→C_i has
kernel M_D and psi2:C_i→A_i has kernel M=E[p^k]. For
isogeny factorizations, the preimage of the psi-Kummer condition
on M_D is EXACTLY the psi1-Kummer condition, since both are
kernels of their maps into H1(B_i). Its image on M is EXACTLY
the psi2-Kummer condition by functoriality of point connecting maps.
Thus the completed native decorated exact sequence is the kernel
sequence of two ACTUAL isogenies. In particular b_i is an actual
dual-psi1 Selmer class, while the strict corrected z is an actual
psi2 Selmer class.

Morgan–Smith2103.08530 gives a generalized Cassels–Tate pairing for
this exact sequence. The next check is its sign and identification
with the classical pairing on Sha(C_i) times Sha(C_i^dual), using
the actual images of z and b_i. No finiteness of either Sha group
is assumed. This may provide the requested geometric comparison
without evaluating its specific value from the complex zero.

Further exact test under development: the coefficient inclusion
E[p^k]=ker(psi2)→C_i need not extend to a homomorphism E→C_i.
Using End_bar(E)=Z and the Weil restriction's diagonal map, one
can test that extension integrally rather than assume an integral
Kato Selmer class maps to the divisible subgroup of Sha(C_i).
Keep all factors2 in the full dihedral induction and quotient.

## Completed and independently reviewed construction

The seven-section proof heegner-native-height-comparison.md is saved
and passed the complete independent coordinator review linked above.
The review directly checked the primary sources, the compact-FIRST
sign, the half-norm and all point-subcase restrictions.
No value has been set to zero.

Completed new constructions:
- The actual native N_i quotient is ker(psi2 psi1) on abelian varieties
  B_i→C_i→A_i=Res_(F_i/Q)E. Exact local Kummer preimage/image identities
  identify EVERY native/dual local condition, including old transverse
  J_i,i, without removing H0 connecting terms or nonclean components.
- The fixed input z and normalized test b_i give actual torsors
  xi_i(z) in Sha(C_i)[psi2] and upsilon_i in Sha(C_i^dual)[psi1^dual].
  Morgan–Smith2103.08530v2 Definition3.2 and §6.1 prove the precise
  comparison CT_C(xi_i(z),upsilon_i)=−R_i(z)/p^k. The minus is
  global-minus-native-local with compact-FIRST coefficient evaluation.
  No finite Sha assumption is used. Quadratic base change multiplies
  both-class pairing by2; the original half-corestriction is retained.
- C_i=A_i/P0[p^k], P0=ker Norm. Using End_F(E)=Z and Weil adjunction,
  Hom_Q(E,C_i)=Z j0 with psi2 j0=diagonal. A homomorphism E→C_i whose
  E[p^k] image lies in ker psi2 is zero on E[p^k]. The required marked
  finite inclusion therefore does not extend to an elliptic morphism,
  even after denominators prime to p. Integral Kato cohomology does
  not automatically give a divisible Sha(C_i) class by that route.
- For the SEPARATE subcase z=Kum_(p^k)(P), the exact norm-Prym formula
  is xi_i(z)=−j_P partial_Norm(2P), with the2 coming from the inherited
  half-norm augmentation. Native local conditions mean2P lies in
  Norm A_i(Q_v)+p^k E(Q_v); xi_i(z)=0 iff the GLOBAL counterpart holds.
  The norm torsor itself need not be locally trivial before j_P push.
  The actual Kato input is not assumed to come from such a point.
- The tame coordinate has no Z_p-valued character lift: abelianizing
  tame Frobenius gives (i²−1)chi(sigma)=0, whereas a_i(sigma)=−1 modp^k.
  Howard1202.6343v1 and Macias Castillo–Sano2603.23978v1 height results
  therefore do not directly identify this direction with their Z_p
  tower variable or with the extra complex zero.

Exact remaining task: annihilate the PARTICULAR classical Cassels–Tate
value for the actual z using a proved arithmetic comparison from
L'''(E,1)=0; a point preimage/global norm congruence in the separate
point subcase would suffice. No such comparison is proved. The mixed
coset and actual top Heegner ambiguity remain after first vanishing.
Full BSD and NP-TP5 remain open.

Primary versions are linked in the proof: Morgan–Smith2103.08530v2
(26June2022), Milne AV172-page author notes for finite quotients/duals,
Howard1202.6343v1 and Macias Castillo–Sano2603.23978v1(25March2026).
No old scripts, certificates, shared synthesis or new agents were used.
