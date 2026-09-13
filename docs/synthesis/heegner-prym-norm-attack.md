# The actual Prym norm lattice and the next integral lifting obstruction

Date: 2026-09-12. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
**Completed bounded construction, independently reviewed PASS** in
[review-heegner-prym-norm.md](review-heegner-prym-norm.md) on2026-09-13.
All seven sections passed against mathematical revision
9e0f63b5420e6608c0214a4a216a46580948c47922a4f2353653abfc709a9c4a.
Subsequent status and review-link changes are editorial.
Restart: [checkpoint](heegner-prym-norm-checkpoint.md).
Full BSD over Q remains the objective.

The native pairing can be realized on a smaller Weil restriction
from the reflection-fixed field. Its exact integral Tate lattice
then exposes a new obstruction: the marked finite kernel map has
a connecting class of full order p^k and does not lift even one
p-power level. We compute the corresponding global obstruction
for the actual corrected Kato class, retaining the cofactor classes'
own lifting defects. In the separate point subcase we identify the
remaining global norm quotient on the actual Mordell–Weil lattice.
Neither obstruction has been shown to vanish from the extra
complex zero.

## 1. Marked inputs and scope

Use the completed
[isogeny construction](heegner-native-height-comparison.md) and
[its review](review-heegner-native-height.md).
Keep n=p^k, R=Z/n, T=T_pE, M=E[n], M_D=M tensor epsilon_K,
the actual first-order sequence
$$
 0\longrightarrow M_D\longrightarrow N_i
       \xrightarrow{\pi}M\longrightarrow0,
 \qquad i\in\{\ell,q\},
 \tag{1}
$$
and the actual corrected input
$$
 z=d_0\{[A,B]_m w_k-[w_k,B]_m A-[A,w_k]_m B\}.
 \tag{2}
$$
Here A,B are the FIXED finite Selmer classes from the preceding
proof, and w_k is the reduction of the actual integral Kato
second derivative w0. They are not replaced by point classes.
The bracket is the determinant of the two old finite coordinates.

The hypotheses are the inherited ordinary nonanomalous p>=5,
surjective residual representation and Manin-unit range for d0,
the auxiliary imaginary quadratic K with D prime to Np,
the Heegner splitting conditions, L(E^D,1) nonzero, and the
additional p not dividing h_K for the independent tame coordinate.
Let F=F_i, G=Gal(F/K)=C_(p^e), e=v_p(i+1)>=k, and
$$
 \mathscr G=\operatorname{Gal}(F/\mathbb Q)
      =G\rtimes\langle c\rangle,\qquad cgc^{-1}=g^{-1}.
 \tag{3}
$$
The chosen reflection c is the one in the fixed induced basis.
All local places of S={v:v divides NpD ell q} and the real
Tate convention remain. The actual d0 is never canceled as
a nonunit. Its valuation and all nonclean local images remain
as in the previous proof.

For the single normalized b_i and scalar R_i, impose the same
additional clean conditions: p-unit Tamagawa and Sel_n(E^D)=0.
Without them use every test in the exact dual isogeny Selmer
group and the full local sum.
The known equality, with compact-FIRST coefficients, is
$$
 \operatorname{CT}_{\mathcal C}(\xi_i(z),\upsilon_i)
                   =-{\cal R}_i(z)/n .
 \tag{4}
$$
No particular value in(4) is known to be zero.

## 2. An actual reflection-field reduction of the same pairing

Put L=F^(<c>), so [L:Q]=p^e, and
$$
 A^+=\operatorname{Res}_{L/\mathbb Q}E,\qquad
 A=\operatorname{Res}_{F/\mathbb Q}E.
 \tag{5}
$$
No assertion that L is totally real is needed.
There are genuine restriction and norm homomorphisms
I:A^+→A and J:A→A^+, with JI=[2].
On the permutation lattices these maps send
[g<c>] to [g]+[gc], and [g] to [g<c>], respectively.

The existing quotient rho:A[n]→N_i is invariant under right
multiplication by c. Indeed its coefficient generator is e_+,
which c fixes, in the fixed sum/difference basis.
Define
$$
 \rho^+=\rho I:A^+[n]\twoheadrightarrow N_i,\qquad
 \rho=\tfrac12\rho^+J\quad\text{on }A[n].
 \tag{6}
$$
The displayed half is the inherited finite-coefficient half-norm,
not a new abelian-variety division. Surjectivity follows because
e_+ and its nontrivial tame translate generate N_i.

Quotient A^+ by ker(rho^+) and then by its marked M_D subgroup.
This constructs actual isogenies
$$
 B^+\xrightarrow{\psi_1^+}C^+
       \xrightarrow{\psi_2^+}A^+,
 \qquad
 \ker\psi_1^+=M_D,\quad \ker\psi_2^+=M.
 \tag{7}
$$
The finite subgroup quotient existence and Cartier duality are
the already inspected Milne AV v2.0 inputs used in the predecessor.
Both degrees in(7) are n² and dim(C^+)=p^e.

**[NEW] Proposition2.1.** The kernel sequence of(7), with its
actual isogeny local conditions, is exactly the same marked
decorated sequence(1).

*Proof.* On every local point group, Kummer naturality and(6)
show that the image through rho is contained in the image
through rho^+: the norm J takes actual F-points to actual
L-points, and multiplication by1/2 acts on the finite image.
Conversely I gives every image through rho^+ as an image
through rho. Since the groups are annihilated by odd n,
the factor1/2 preserves them exactly.
Thus the two native local images in N_i coincide.
Their preimages on M_D and images on M coincide as well.
This proof uses all semilocal point factors; no diagonal
restriction or local norm-surjectivity hypothesis is inserted.
Square.

Let xi_i^+(z) and upsilon_i^+ be the actual isogeny torsors
on C^+ and (C^+)^dual defined from z and lambda_D(b_i),
with lambda_D(b)(m)=e_n(m,b).
The identical decorated sequence and
[Morgan–Smith2103.08530v2, Theorem1.3 and §6.1](https://arxiv.org/html/2103.08530v2)
give
$$
 \boxed{\operatorname{CT}_{C^+}(\xi_i^+(z),\upsilon_i^+)
                  =-{\cal R}_i(z)/n.}
 \tag{8}
$$
No extra factor2 appears: the finite maps on M and M_D
are the identities with the marked normalizations.
The induced map f:C^+→C satisfies
xi_i(z)=f_*xi_i^+(z) and upsilon_i^+=f^dual_*upsilon_i.
These use contragredient dual maps, not the same map twice.

The rational representation underlying A^+ is the permutation
representation on \mathscr G/<c>. It decomposes as the trivial
representation once and each nontrivial two-dimensional
Ind_K^Q(chi) once. The quadratic epsilon_K is absent.
Consequently the complete L-function is
$$
 L(C^+/\mathbb Q,s)
  =L(E/\mathbb Q,s)
       \prod_{\{\chi,\chi^{-1}\},\,\chi\ne1}L(E/K,\chi,s).
 \tag{9}
$$
This is the actual reflection-field Artin decomposition;
all local Euler factors are retained.
Moreover Hom_Q(E^D,C^+) is zero: Weil adjunction reduces
the assertion for A^+ to Hom_L(E^D,E)=0.
The odd-degree L does not contain K, and in the non-CM case
any such homomorphism over LK is an integer multiple of the
twist isomorphism, negated by the nontrivial K/L automorphism.
It cannot descend unless zero. Isogeny of C^+ and A^+ gives
the same statement for C^+.
Thus the rank-zero twist factor used for d0 is not a
characteristic-zero abelian constituent controlling these torsors.

## 3. The exact integral norm lattice and its full-order class

Write d=p^e, H=<c>, and let
$$
 \Lambda=\mathbb Z_p[\mathscr G/H],\quad
 \Lambda_0=\ker(\operatorname{aug}:\Lambda\to\mathbb Z_p),\quad
 \Lambda_C=\Lambda+\tfrac1n\Lambda_0\subset\mathbb Q_p[\mathscr G/H].
 \tag{10}
$$
Use a different symbol from the cyclotomic Iwasawa algebra.
Let e_H be the basis vector of H. The norm t:A^+→E is now
the UNHALVED sum. Its kernel P_0^+ is connected, since the
geometric sum map has connected kernel. Equations(6)–(7) give
$$
 C^+=A^+/P_0^+[n],\qquad
 T_pA^+=T\otimes\Lambda,\qquad
 T_pC^+=T\otimes\Lambda_C .
 \tag{11}
$$
Indeed quotienting by P_0^+[n] enlarges its Tate lattice by
(1/n)T_pP_0^+, and the latter is T tensor Lambda0.
In the common rational space, psi2^+ acts by n.
Thus there is the actual integral coefficient sequence
$$
 0\to T\otimes\Lambda_C\xrightarrow{\,n\,}
       T\otimes\Lambda\xrightarrow{\operatorname{aug}\bmod n}
       E[n]\to0.
 \tag{12}
$$
Its quotient identification is the marked one.

Inside C^+[n]=(T/n) tensor (Lambda_C/nLambda_C), the marked
inclusion of E[n] is
$$
 j_n(x)=x\otimes\bar e_H .
 \tag{13}
$$
Any other coset vector gives the same class because their
difference lies in Lambda0, which is contained in nLambda_C.
This is a Galois-equivariant map at the finite level.

**[NEW] Proposition3.1.** The integral connecting class of
bar e_H in(13) is
$$
 \epsilon_C(g)=\frac{g e_H-e_H}{n}\in\Lambda_C,\qquad
 [\epsilon_C]\in H^1(\mathscr G,\Lambda_C)
                       \simeq\mathbb Z/n,
 \tag{14}
$$
and is a GENERATOR of that group.

*Proof.* Multiplication by n identifies Lambda_C with
Lambda'=Lambda0+nLambda=ker(Lambda→Z/n by augmentation).
The exact sequence
0→Lambda'→Lambda→Z/n→0 therefore applies.
Shapiro gives H1(\mathscr G,Lambda)=H1(H,Z_p)=0.
The invariant vectors in Lambda are multiples of the
sum of all d cosets, whose augmentation d is zero modulo n.
The connecting map Z/n→H1(\mathscr G,Lambda') is consequently
an isomorphism. It sends1 to g e_H-e_H.
Scaling back by n proves(14), including its exact order.
Square.

These are cohomology groups of the actual permutation lattice
of the constructed variety, not a formal norm-relation model.
The Shapiro and connecting arguments also prove the assertion
without any semisimplicity at finite p-power coefficients.

**[NEW] Corollary3.2.** The invariant vector bar e_H has no
invariant lift from Lambda_C/p^k to Lambda_C/p^(k+1).

*Proof.* A lift has a representative e_H+n y, y in Lambda_C.
Invariance modulo pn would require
epsilon_C+dy=pz for an integral cochain z.
Its differential is zero, since Lambda_C is torsion-free;
thus z is a cocycle. This would put [epsilon_C] in
pH1(\mathscr G,Lambda_C), contradicting that it generates Z/n.
Square.

## 4. This excludes every equivariant one-step coefficient lift

The following strengthens the geometric nonextension from
the predecessor. It does not rule out cohomological operations
which add an actual nullhomotopy or new coefficient object.

**[NEW] Proposition4.1.** There is no G_Q-equivariant homomorphism
$$
 E[p^{k+1}]\longrightarrow C^+[p^{k+1}]
 \tag{15}
$$
whose reduction by multiplication p gives(13).

*Proof of the image/disjointness input.* In the inherited
surjective residual range, the p-adic image is GL2(Z_p)
for p>=5. This is Serre's lifting lemma, explicitly recalled
in the primary research note
[Dokchitser–Dokchitser1104.5031v1, opening paragraph](https://arxiv.org/html/1104.5031v1),
dated26April2011. It is used only in this range.

The torsion field Q(E[p^r]) is linearly disjoint from F
for every r. To verify this, any common quotient is a
solvable quotient of GL2(Z/p^r), since \mathscr G is dihedral.
The group SL2(Z/p^r) is perfect for p>=5: elementary
transvections generate it, and conjugation by diag(u,u^-1)
expresses every transvection as a commutator when u²-1
is a unit (take u=2).
Thus a solvable quotient kills SL2 and is abelian.
The only nontrivial abelian quotient of the odd dihedral
group is its quadratic quotient K/Q.
But K ramifies at a prime of D outside Np, whereas the
elliptic torsion field is unramified outside Np.
So that common quadratic field is impossible.

The joint Galois action at level p^(k+1) is therefore the
direct product of the full matrix group and \mathscr G.
Commuting with the matrix group makes any map(15) equal
to x mapping to x tensor v, for a coefficient
v in Lambda_C/p^(k+1). This follows directly by commuting
its coefficient matrix with diag(2,1) and the two elementary
unipotents: the off-diagonal entries vanish and the two
diagonal entries agree.
Commuting with \mathscr G then requires v invariant.
Reduction to(13) requires v to lift bar e_H, which is
excluded by Corollary3.2. Square.

In particular, simply applying the marked finite inclusion
to higher integral Kato coefficients cannot produce a
compatible p-divisible torsor system on the fixed C^+.
The obstruction disappears after tensoring(14) with Q_p,
but it has full order n integrally. No p-isogeny is inverted
to erase it.

## 5. The global obstruction for the ACTUAL corrected input

The coefficient sequence(12) gives a canonical connecting map
$$
 {\cal B}_{i,n}:H^1(U,E[n])
               \longrightarrow H^2(U,T\otimes\Lambda_C)[n].
 \tag{16}
$$
Here U is the actual complement of S. By Shapiro and the
augmentation, its preceding map is reduction modulo n of
corestriction from H1(U_L,T). Thus
$$
 {\cal B}_{i,n}(z)=0
 \quad\Longleftrightarrow\quad
 z\text{ is the reduction of }\operatorname{cor}_{L/Q}(w_L)
 \text{ for some }w_L\in H^1(U_L,T).
 \tag{17}
$$
This is a GLOBAL Galois cohomology criterion. It does not
impose the local point conditions on w_L; those remain
necessary for a native point-image lift.

Naturality of(12) with the coefficient multiplication-n
sequence on T_pC^+ identifies(16) with the ordinary
Bockstein of j_n(z). This also proves that j_n(z), which
is finite locally because xi_i^+(z) is locally trivial,
is an actual class in Sel_n(C^+).

There is an explicit cochain expression, retaining a
possible coefficient-lifting defect. Choose a continuous
T-valued lift tilde z of the finite cocycle z and put
$$
 b_E(z)=d\widetilde z/n\in Z^2(U,T),\qquad
 [b_E(z)]=\beta_E(z).
 \tag{18}
$$
The combined formula for(16), with Lambda coefficient first,
is
$$
 {\cal B}_{i,n}(z)=
 \left[
   (g,h)\longmapsto
    \epsilon_C(g)\otimes g\widetilde z(h)
       +e_H\otimes b_E(z)(g,h)
 \right].
 \tag{19}
$$
Indeed lift z to e_H tensor tilde z in T tensor Lambda,
differentiate, and divide by n using(12).
The result is closed and independent of the lifts.
When tilde z is not a cocycle the two displayed terms
need not be closed separately; only their sum is asserted
to be a class.

For the actual input(2), exact R-linearity gives
$$
 \boxed{\quad
 \beta_E(z)=
 -d_0\{[w_k,B]_m\,\beta_E(A)
             +[A,w_k]_m\,\beta_E(B)\}.
 \quad}
 \tag{20}
$$
The omitted w_k term is zero because w_k comes from the
actual integral class w0. The terms involving the FIXED A,B
are not deleted: finite Selmer classes need not lift to the
integral Selmer lattice. All scalar products in(20) are
in n-torsion cohomology, so choosing Z_p representatives
of their residues has no effect.

In the additional subcase that z has an integral cocycle
lift w_z, formula(19) simplifies to the exact cup
$$
 {\cal B}_{i,n}(z)=[\,\epsilon_C\cup w_z\,].
 \tag{21}
$$
Even this need not be zero merely because epsilon_C has
zero rational image. Conversely its nonzero coefficient
class does not prove that this particular cup is nonzero.
Equations(19)–(21) compute the first residual of the
attempted integral Kato-to-isogeny lift, not the desired
complex-derivative comparison.

If one constructs w_L in(17) with actual integral local
point conditions everywhere, its finite reduction followed
by rho^+ supplies a GLOBAL native lift of z in N_i.
It then proves R_i(z)=0. Mere vanishing of(16), without
those local conditions, does not suffice.

The obvious candidate obtained by restricting the existing
Kato class to L has exact corestriction
$$
 \operatorname{cor}_{L/Q}\operatorname{res}_{L/Q}w_0
                 =p^e w_0 .
 \tag{22}
$$
The same identity holds for the corrected finite input,
giving zero modulo n. Restriction of the actual cyclotomic
Euler class before taking its second derivative has the
same multiplicity: L is disjoint from the cyclotomic tower,
and norm and coefficient extraction commute.
This candidate does not provide the requested preimage
of z unless z itself is zero. Dividing the multiplicity
p^e is not an integral operation.

## 6. The selected-point problem on the actual norm lattice

This section remains an ADDITIONAL point subcase.
No point representing(2) has been constructed.
Suppose z=Kum_n(P), P in E(Q). The unhalved augmentation
on A^+ gives, by the same explicit norm-fiber cocycle
calculation as in the predecessor,
$$
 \xi_i^+(\operatorname{Kum}_nP)
        =-j_{P,+\,*}\partial_{\operatorname{Norm}_{L/Q}}(P).
 \tag{23}
$$
Here j_(P,+):P0^+→C^+ is the pushout inclusion with
q2^+|P0^+=j_(P,+)[n].
The local point conditions are exactly
$$
 P\in\operatorname{Norm}_{L/Q}E(L\otimes Q_v)+nE(Q_v)
                     \quad\text{for every }v,
 \tag{24}
$$
and xi_i^+=0 is equivalent to the GLOBAL counterpart.
Under the embedding into the full field construction,
Norm_F I=2Norm_L; thus(23) maps to
-j_P partial_NormF(2P), precisely the previously proved formula.
No half-norm factor is lost.

Let
$$
 {\cal M}_F=E(F)\otimes\mathbb Z_p,\qquad
 {\cal L}_Q=E(Q)\otimes\mathbb Z_p .
 \tag{25}
$$
These are actual Mordell–Weil lattices, without a Sha
finiteness premise. The disjointness in Proposition4.1
gives E(F)[p]=0.
In fact E(Q) is p-saturated in E(F): if pR is rational
and R is in E(F), every Galois difference gR-R is
p-torsion in E(F), hence zero. Iteration gives the
same assertion for all powers.
This saturation does not say that norms are surjective.

**[NEW] Proposition6.1.** There is a canonical equality of
finite norm quotients
$$
 \boxed{\quad
 \frac{{\cal L}_Q}
      {\operatorname{Norm}_{L/Q}(E(L)\otimes\mathbb Z_p)}
   \simeq
       \widehat H^0(G,{\cal M}_F)^{c=+}.
 \quad}
 \tag{26}
$$
It is killed by p^e. After quotienting by n, it is the
exact obstruction to the global point congruence in(24).

*Proof.* Flatness of Z_p and finite generation make
invariants commute with tensoring here, so
M_F^G=E(K) tensor Z_p and M_F^c=E(L) tensor Z_p.
The norm from L is N_G=the sum of g in G on M_F^c.
The operator N_G commutes with c. Since2 is invertible,
its image on the plus part is exactly (N_G M_F)^+.
Taking plus parts is exact, and hence its cokernel is
(M_F^G/N_G M_F)^+, the definition of the right side.
The diagonal points show p^e L_Q is in the norm image.
Reduction modulo n gives the final assertion. Square.

For orientation, the definition of Tate Hhat0 is the
norm cokernel, as in
[Kedlaya, Class Field Theory, Homology and Tate groups](https://kskedlaya.org/cft/sec_homology.html).
Formula(26) is proved above on the actual E(F) lattice;
no abstract module is introduced as a counterexample.

The integral trace-zero subspace and the invariant subspace
split after inverting p^e. That rational decomposition
does not compute(26): the quotient measures their integral
interaction. In particular the completed no-elliptic-map
argument is not repaired by a rational isogeny decomposition.
An actual selected point for(2), followed by a proof that
its class in(26)/n is zero, would solve this sufficient
point-preimage problem. Neither step is presently proved.

## 7. What the extra complex zero still has to control

The new constructions are concrete:
the same torsor pairing on C^+ with the rank-zero twist
constituent removed; the full-order integral class(14);
the no-one-step coefficient-lift theorem; the exact global
cochain residual(19), including the actual cofactor defects(20);
and the selected-point norm quotient(26).

The rational image of epsilon_C is zero, whereas its
integral order is p^k. Therefore a rational height or
Artin-factor computation cannot simply cancel this term.
This observation is not a proof that no arithmetic comparison
can control it. It identifies the precise integral data which
a successful new comparison must retain.

**[OPEN, Prym-TP5].** Use L'''(E,1)=0 to construct, for the
ACTUAL z in(2), an integral norm preimage with all point-local
conditions, or a valid selected-point comparison and global
norm congruence, or the specific weaker orthogonality
CT_(C^+)(xi_i^+(z),upsilon_i^+)=0.
The original finite local tests and their contragredient
point transport remain in force. No p-adic/complex
derivative identification or finite-Sha premise is supplied.

Even vanishing of both first pairings leaves the reviewed
mixed/top Heegner choice problem. No class selecting that
top coefficient has been constructed here. The full universal
BSD objective remains unresolved.

All new calculations are algebraic/cohomological and passed
the separate review linked above. No old numerical computation, certificate,
prime scan, shared-file edit or additional agent was used.
