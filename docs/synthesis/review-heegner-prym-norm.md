# Independent review of the reflection-field Prym and integral norm lattice

Date: 2026-09-13. Reviewer root/coordinator.
**PASS for all seven sections and their stated scope.**
Reviewed [proof](heegner-prym-norm-attack.md), SHA256
9e0f63b5420e6608c0214a4a216a46580948c47922a4f2353653abfc709a9c4a,
and [checkpoint](heegner-prym-norm-checkpoint.md), SHA256
ca02fc07263e433475103cfd0c139a47c6e70cbf36b2ab240a4fece2a63112b8.
Subsequent completion/review-link changes are editorial.

I read the complete construction and reconstructed the reflection
maps, integral coefficient lattice, full-order connecting class,
one-step obstruction, actual global cochain and selected-point norm
quotient. No old computation was rerun. The particular Cassels–Tate
value is not proved zero, and the result does not prove BSD.

## 1. The smaller field preserves the actual decorated sequence

Restriction I from L=F^<c> to F and norm J back satisfy JI=[2].
On their permutation lattices the stated coset sum/projection are
the actual maps. The old quotient is invariant under the right
reflection since its marked plus generator is fixed.

With rho^+=rho I, the identity rho=(1/2)rho^+ J on finite
coefficients is exact. The inherited normalization is half the
FULL-field norm, so pi rho I is exactly the UNHALVED L-field
norm. This tracks the factor2 rather than inferring it from a
dimension count.

Kummer naturality on every semilocal point group gives both
inclusions of native local images. Multiplication by1/2 is an
automorphism of each odd-primary finite image; no local norm
surjectivity is needed. Exact preimages and images therefore
give the same marked M_D→N_i→M sequence on B^+→C^+→A^+.

The quotient construction uses the already reviewed finite
Galois-stable subgroup/isogeny and Cartier-dual results of
Milne. The exact local identity permits application of
[Morgan–Smith2103.08530v2, Theorem1.3 and §6.1](https://arxiv.org/html/2103.08530v2)
with identity finite maps. Thus the CTP remains-R_i/n.
The induced geometric torsor maps use f and its CONTRAGREDIENT
dual, consistent with the original compact-first coefficient frame.

The permutation representation on the reflection cosets contains
the trivial character and each nontrivial two-dimensional induced
representation once. The quadratic character has no reflection
invariant vector. This proves the stated complete Artin product.
For Hom_Q(E^D,C^+)=0, the proof's descent argument is valid:
L has odd degree and cannot contain K, while the non-CM twist
isomorphism is negated by the quadratic automorphism.
Isogeny to A^+ does not change this rational Hom calculation.

## 2. Actual Tate lattice and exact order of epsilon_C

Let Lambda=Z_p[mathscrG/H], with d=p^e cosets.
The connected norm kernel has Tate lattice T tensor Lambda0.
Quotienting its n-torsion enlarges the lattice to
T tensor(Lambda+(1/n)Lambda0). This is an actual geometric
isogeny lattice in the common rational representation.

The morphism psi2^+ multiplies that lattice by n into
T tensor Lambda. The quotient is E[n], identified by unhalved
augmentation. Thus the marked finite inclusion is precisely
x mapping to x tensor e_H modulo nLambda_C.
Different coset choices differ by Lambda0 contained in nLambda_C,
so the finite map is equivariant.

Scaling Lambda_C by n identifies it with
Lambda'=ker(Lambda→Z/n).
Shapiro gives H¹(mathscrG,Lambda)=H¹(H,Z_p)=0.
Its invariant norm vector has augmentation d=0 modulo n.
The long exact sequence then identifies
H¹(mathscrG,Lambda_C)=Z/n and sends1 to
epsilon_C(g)=(g e_H-e_H)/n. This is a GENERATOR, not merely
a class killed by n.

For the one-step assertion, an invariant lift has the form
e_H+n y modulo pnLambda_C. Its invariance would make
epsilon_C+dy divisible by p as an integral cochain.
The quotient cochain is closed because Lambda_C is torsion-free.
Its cohomology would make the generator epsilon_C p-divisible
in Z/n, a contradiction. This checks the finite coefficient
lifting problem, including k=1.

## 3. Full Galois disjointness and every equivariant map

I directly checked
[Dokchitser–Dokchitser1104.5031v1, opening paragraph](https://arxiv.org/html/1104.5031v1):
for elliptic curves over Q in the p>=5 surjective residual range,
Serre's lifting lemma gives the full p-adic image.
Only that stated range is used.

The disjointness proof is also direct. SL2(Z/p^r) is generated
by elementary transvections, each a commutator using
diag(2,2^-1), since 2²-1=3 is a unit. It is therefore perfect.
Any solvable quotient of GL2 kills it and is abelian.
The only nontrivial abelian quotient of the odd dihedral group
is K/Q, which ramifies at a finite prime of D outside Np.
The elliptic torsion field is unramified there, so even this
intersection is excluded.

Consequently the joint image is the direct product. A matrix
commuting with diag(2,1) and both elementary unipotents is a
scalar, also over Z/p^(k+1). Applying this coefficientwise
forces every proposed lift to be x mapping to x tensor v.
The dihedral action forces v invariant, and its reduction must
be the vector excluded above. This proves the assertion for
EVERY equivariant one-step map, not only maps arising from
abelian-variety homomorphisms.

It does not show that every PARTICULAR cohomology class fails
to lift. The proof preserves that distinction.

## 4. The actual global connecting cochain, including cofactor defects

The preceding map in the cohomology sequence is, by Shapiro,
corestriction from H¹(U_L,T) followed by reduction.
Exactness therefore proves the GLOBAL norm-preimage criterion(17).
This has not imposed native point-local conditions on the preimage.

The diagram into the multiplication-n sequence for T_pC^+
identifies the connecting map with the Bockstein of j_n(z).
The locally trivial isogeny torsor image makes j_n(z) a class
in the ordinary finite Selmer group of C^+.

I computed the lift differential directly. For
s(g)=e_H tensor tilde z(g),
$$
 ds(g,h)=(g e_H-e_H)\otimes g\widetilde z(h)
                       +e_H\otimes d\widetilde z(g,h).
$$
Dividing by n in the stated coefficient lattice yields
epsilon_C(g) tensor g tilde z(h)+e_H tensor b_E(z)(g,h),
exactly(19). When tilde z is not a cocycle, its two displayed
parts need not be individually closed; the full expression is.

Bockstein linearity and the known integral lift of w_k give
precisely(20). The fixed finite classes A,B contribute their
own beta_E terms and cannot be discarded. Scalar lifts modulo n
are harmless because the resulting cohomology is n-torsion.
Only under the ADDITIONAL integral lift of z does the formula
reduce to epsilon_C cup w_z.

Corestriction of the obvious restricted Kato class is exactly
p^e w0. Field disjointness also gives disjointness from the
cyclotomic tower, so coefficient extraction does not remove
that multiplicity. Its finite reduction iszero. No division
by p^e or finite-Sha premise is made.

## 5. The selected-point norm quotient

In the additional point subcase the half factor disappears on
A^+, giving xi_i^+(Kum_nP)=-j_(P,+) partial_NormL(P).
Its embedding into the full field doubles the norm and recovers
the earlier formula with2P. The same explicit Kummer argument
gives the local and global norm congruences.

Disjointness makes E(F)[p]=0. Thus if pR is Q-rational for
R in E(F), every Galois difference is p-torsion and hencezero:
the stated p-saturation follows. This does not imply that norms
are surjective.

On the ACTUAL finitely generated group E(F), flatness gives
M_F^G=E(K) tensorZ_p and M_F^c=E(L) tensorZ_p.
The L-field norm is N_G on the c-plus part. Since2 is invertible,
(N_G M_F)^+=N_G(M_F^+), and taking plus parts is exact.
This proves
$$
 (E(Q)\otimes Z_p)/\operatorname{Norm}_{L/Q}(E(L)\otimes Z_p)
       =\widehat H^0(G,E(F)\otimes Z_p)^+ .
$$
The diagonal rational points show that p^e kills the quotient.
Reducing by n is precisely the finite global congruence obstruction.
I checked the stated norm-cokernel convention in
[Kedlaya, Homology and Tate groups](https://kskedlaya.org/cft/sec_homology.html);
the actual lattice equality is proved in the note itself.

No selected rational point for the actual Kato/cofactor input is
supplied, and the integral norm quotient has not been calculated
to annihilate such a point. A global cohomological norm preimage
without the point-local conditions would also be insufficient.
The exact Prym-TP5 gap and the later mixed/top ambiguity remain.
