# Heegner Prym norm checkpoint

Date: 2026-09-13. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this file and heegner-prym-norm-attack.md.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-prym-norm.md](review-heegner-prym-norm.md).
Reviewed mathematical revision:
9e0f63b5420e6608c0214a4a216a46580948c47922a4f2353653abfc709a9c4a.
All seven sections passed without a mathematical correction.
The particular norm/CT vanishing, native local preimage and selected
Kato-point comparison remain unproved. Full universal BSD remains active.

The reciprocal Poisson review is also complete in
[review-poisson-iterated-source.md](review-poisson-iterated-source.md).
No further expansion of the present proof is assigned. A next bounded
task should start from the exact Prym-TP5 obstruction recorded below.

## Historical initial checkpoint (2026-09-12)

The initial and material-development entries below preserve earlier
research snapshots. Their pending-review wording is historical;
the current completed verdict and scope are stated above.
Initial checkpoint saved before new research.

Full BSD for all elliptic curves over Q remains the objective.
The completed native-height proof identifies the actual obstruction
with CT_C(xi_i(z),upsilon_i)=−R_i(z)/p^k, using two specified isogeny
torsors. This task seeks a new point-preimage, divisible-torsor or
orthogonality construction that controls that value from the extra
complex zero. Do not rebuild the completed isogenies or finite inverse.

Keep full p^k, d0, the half-norm convention, compact-FIRST coefficient
pairing, dual point transport, and all nonclean local conditions.
The point subcase is additional: its actual residual is
−j_P partial_Norm(2P), with local/global norm congruences.
No selected-point premise for Kato is available. The marked E[p^k]
inclusion has no nonzero elliptic-map extension, and the finite tame
coordinate has no Z_p character lift. These are completed constraints.

Next: read the current next plan and completed isogeny proof/review;
construct and test a genuine norm/cohomological correspondence on
the actual torsors, retaining any integral kernel or cokernel.
Every new deduction requires separate review. No old runs, new
agents or shared/completed-proof edits. Mixed/top selection remains
unresolved even after hypothetical first-pairing vanishing.

## Historical material construction before review

The native quotient factors through the right-reflection-plus summand.
For L=F_i^(c), degree p^e over Q, A^+=Res_(L/Q)E therefore realizes
the SAME marked finite sequence by smaller isogenies B^+→C^+→A^+.
The images of actual local point groups agree, because the norm and
restriction for F_i/L have composite2, a unit at p. The corresponding
CT value is unchanged with the contragredient dual map. The norm
augmentation on A^+ is unhalved; its embedding into the full A doubles
the norm, recovering the previous half-norm convention. Its rational
representation has trivial plus each nontrivial dihedral constituent
ONCE and no E^D constituent.

An actual integral coefficient obstruction is now being computed.
Let G=Gal(F_i/Q), H=<c>, Lambda=Z_p[G/H], Lambda0=ker aug,
and Lambda_C=Lambda+(1/p^k)Lambda0. The Tate lattice of C^+ is
T_pE tensor Lambda_C. Scaling by p^k identifies Lambda_C with
Lambda'=ker(Lambda→Z/p^k via aug). Shapiro gives H1(G,Lambda)=0;
the invariant norm vector has augmentation p^e=0 modp^k.
Hence H1(G,Lambda_C)=Z/p^k, with the marked finite kernel inclusion's
Bockstein represented by (g e_H−e_H)/p^k and of EXACT order p^k.
This computes the integral obstruction to extending the permutation
coefficient map; a one-step p-power lift also appears impossible.
Do not promote until the exact finite coefficient diagram is checked.

For a global integral T_pE cocycle w, the resulting Bockstein of its
marked image in C^+[p^k] is the ACTUAL cup epsilon_C cup w: lift by
e_H tensor w and differentiate. For the corrected actual input z,
an integral lift is not assumed; the ordinary T_pE Bockstein of the
cofactor contains the Bockstein defects of the fixed A,B. These terms
must remain in the final comparison.

The point-subcase norm quotient should be computed on the ACTUAL
Mordell–Weil lattice E(F_i) tensor Z_p via Tate cohomology and c-plus
projection. This is a proposed arithmetic norm test, not a point
premise for Kato or a full-Sha finiteness assumption.

## Completed and independently reviewed proof

heegner-prym-norm-attack.md contains seven complete sections,
all checked in the separate coordinator PASS review linked above.
The review reconstructed the marked reflection maps, full-order
coefficient class, all-equivariant one-step obstruction, global
cochain/cofactor defects and actual selected-point norm quotient.

Completed reviewed constructions:
- The smaller reflection-field isogenies B^+→C^+→A^+ realize the SAME
  native marked finite sequence and exact dual conditions. Their CT
  value is still −R_i/n; the maps to the original torsors use f and
  f^dual. The norm is unhalved on A^+; embedding into the full field
  doubles it, so the old half-norm is retained exactly.
- The actual rational representation of A^+ has no E^D constituent.
  Hom_Q(E^D,C^+)=0. This does not prove any torsor vanishing.
- Lambda_C=Lambda+(1/n)Lambda0 is the actual Tate coefficient lattice
  of C^+. Its H1(G,Lambda_C)=Z/n and epsilon_C=(g e_H−e_H)/n is a
  GENERATOR. The marked finite kernel inclusion does not lift even
  one p-level. Full inherited torsion image, dihedral/torsion-field
  disjointness and matrix centralizers extend this to ANY equivariant
  map E[p^(k+1)]→C^+[p^(k+1)], not just an elliptic homomorphism.
- The actual integral sequence0→T_C→T_A→E[n]→0 gives B_i,n(z), the
  global obstruction to a cohomological norm preimage from L. Its
  cochain is epsilon_C cup tilde z + e_H tensor beta_E(z). The terms
  are not separately called cocycles without an integral z lift.
  For the actual corrected Kato input, beta_E(z) retains precisely
  the fixed A,B Bocksteins in formula(20); only beta_E(w_k)=0 is known.
- If z has an integral lift w_z, the obstruction is exactly
  epsilon_C cup w_z. No value of this particular cup is proved zero
  or nonzero. Even its vanishing leaves all point-local conditions.
- The actual base-restriction candidate has norm p^e w0, hence zero
  modulo n; cyclotomic coefficient extraction does not remove p^e.
- In the separate selected-point subcase, the norm obstruction is
  the actual finite Tate quotient Hhat^0(G,E(F)tensorZ_p)^(c=+)/n.
  This lattice is not replaced by an abstract module. No selected
  rational point for the Kato input has been supplied.

Exact remaining task: Prym-TP5 in§7. Construct a point-local integral
norm preimage or the specific CT orthogonality from the extra complex
zero. The coefficient obstruction, ordinary-global cohomology criterion,
selected-point norm congruence and native local conditions are distinct.
No p-adic/complex derivative identification, Sha finiteness or mixed/top
selection was assumed. Full universal BSD remains unresolved.

Primary sources checked: Morgan–Smith2103.08530v2 (marked exact
sequence duality/CT naturality), Dokchitser–Dokchitser1104.5031v1's
explicit Serre lifting lemma in the inherited p>=5 surjective range,
and the finite-group Shapiro/norm definitions used in the displayed
complete proofs. The abelian quotients/Cartier duals are unchanged
primary Milne inputs from the completed reviewed isogeny proof.
No mathematical script, old certificate, prime scan or extra agent ran.
