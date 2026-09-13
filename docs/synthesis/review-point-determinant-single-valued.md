# Independent review of the geometric point-determinant coefficient

Date: 2026-09-12. Reviewer /root/higher_period_integrality,
GPT-6 Astra/xhigh. Own only this review file.

**PASS after inspecting the numerical-level notation precision.**
All six sections of
[point-determinant-single-valued-attack.md](point-determinant-single-valued-attack.md)
and its [checkpoint](point-determinant-single-valued-checkpoint.md) were read.
Reviewed mathematical proof SHA256:
88ef905fb2dbcfbf8381166dfd78b80ea2a0d2f8d8593ab51b7a2d844be8f843.
Reviewed checkpoint SHA256:
c78daf70d5690aa53bb245494aea3f802905c738ddca569c734e0e2b6de70be5.
Subsequent PASS links and completion-status edits are editorial.
The separate additional Section7 verdict is recorded at the end
of this review; it does not replace this original six-section audit.

The note constructs the stated rational geometric framed object
and computes its canonical Deligne-conjugation coefficient.
It does not construct a rational map from the spectral class,
turn the quadratic invariant into an ordinary scalar height,
or prove the BSD formula.

## 1. Fixed arithmetic input and direct Deligne lift

I inspected the relevant portions of the completed
[relative point proof](relative-modular-cycle-attack.md).
Its corrected Z_j are actual degree-zero rational divisors.
They avoid A={O,P,Q} because the modifying functions are
regular and nonzero there. Their Picard classes remain the
independent full-basis points P,Q. The finite height symbols
are already proved to vanish prime by prime on the specified
model. That earlier theorem and its height normalization
are inputs; no old calculation was rerun.

The new construction retains the FULL support B* of these
corrected divisors, including the additional points coming
from their principal modifications. It does not replace
B* by the old uncorrected endpoints. The one-motive and
its marking are therefore precisely the earlier objects.

The dual F¹ space has basis omega0,rho1,rho2:
the residue maps of rho1,rho2 are independent, and omega0
is the remaining holomorphic form. Hence annihilating
these forms is exactly the stated homological F⁰ condition.

Write v_j=r_j+s_j tau with real r_j,s_j and tau=i t0.
The real Betti vector gamma'_j has zero omega0 period.
Subtracting k_ij t_i/(2pi i) gives zero rho_i periods
as well, proving that e_j^D lies in F⁰.
Its conjugate differs only in the puncture-loop subspace.
The Deligne-bigrading characterization therefore places it
in I^(0,0); uniqueness follows from its fixed graded lift.
In particular an added compact Hodge vector could not meet
this same conjugation condition modulo the Tate subspace.

The normalization identity can be checked directly:
if a_i=Re A_i and b_i=Re B_i, then
Re((a_i-i b_i/t0)(r_j+i t0 s_j))=r_j a_i+s_j b_i.
Thus Re k_ij equals exactly H_ij^ht from the earlier period
formula, with no extra factor two.

Scalar conjugation fixes the Betti vectors gamma'_j,t_i,
so
$$
 \overline{e_j^D}-e_j^D
 =\frac{k_{ij}+\overline{k_{ij}}}{2\pi i}t_i
 =-\frac{i}{\pi}\sum_i H_{ij}^{ht}t_i.
$$
The weight/Hodge pattern permits only the negative-bidegree
map I^(0,0)→I^(-1,-1). It is zero on W_(-1) and squares
to zero. The identity bar e=exp(-2i delta)e then gives
delta(e_j^D)=sum H_ij^ht t_i/(2pi), with the sign stated.

This calculation distinguishes scalar conjugation on the
Betti realization from geometric real Frobenius. It does
not identify the result with an unspecified de Rham
single-valued involution.

## 2. Primary Hodge and relative-geometry sources

I directly read
[Burgos Gil–Goswami–Pearlstein2410.17167v3](https://arxiv.org/html/2410.17167v3),
the 67-page revision dated July9,2026:
§§2.1–2.3, Proposition2.16, Definitions2.14 and2.19.
The source fixes the functorial bigrading and real negative
operator delta. Proposition2.16 gives exactly
bar e=exp(-2i delta)e. Its two heights are the imaginary
part of the extreme conjugation coefficient and the
linear-delta extreme coefficient. Neither is the full
quadratic coefficient computed in the note.

I also checked
[Sertöz–Ouaknine–Worrell2505.20397v1, §6.5,
Proposition6.5.43](https://arxiv.org/html/2505.20397v1).
Its marked push/pull realization uses the ordinary boundary
condition on the relative chain and the residue/puncture
map. The displayed period pairing has the term
2pi i times the torus pairing, exactly as used here.
Only this realization theorem is imported; no conclusion
from its transcendence algorithm is used.

Finally I read
[Deligne, Hodge III](https://www.numdam.org/item/10.1007/BF02685881.pdf),
Proposition8.2.10, printed p40, and §§8.3.8–8.3.9,
printed pp43–44. They give Künneth compatibility and
the relative mixed-Hodge structures/filtered cones.
The relative product is consequently a morphism of the
stated rational Hodge structures, not merely an isomorphism
of unfiltered singular groups.

## 3. Relative exterior geometry and the integral factor two

For the connected punctured curve U=E minus A, H²(U,Z)=0
and H¹ is free. Because B* is finite and nonempty,
H₀(U,B*)=0. The relative long exact sequence shows that
all relative homology is concentrated in degree one,
and that group is free. Therefore the relative Künneth
map has exactly the tensor-square term in degree two,
with no Tor contribution or additional graded summand.

The marking map L→Div⁰(B*) is injective integrally:
a relation between Z_1,Z_2 would give the same relation
between P,Q in Pic⁰(E), and these are independent.
Thus the marked pullback lattice maps injectively to
the relative homology, with precisely its specified
integral lattice. The proof does not need saturation
inside every larger unmarked relative lattice.

In the chain cross-product, interchange of two degree-one
cycles has the Koszul sign minus. Hence geometric
interchange is minus the ordinary tensor swap.
Its PLUS rational projector is indeed the usual
antisymmetrizer, giving the exterior square.

For a free basis of V_Z, invariance under minus-swap
requires zero diagonal tensor coefficients and opposite
off-diagonal coefficients. These are exactly the image
of j(x wedge y)=x tensor y-y tensor x.
Thus the abstract exterior lattice is identified with
the geometric invariant lattice by the INTEGRAL map j.
The rational projector still has denominator two.
The ordinary tensor-to-exterior quotient takes j to
twice the original wedge, so it cannot serve as its
integral inverse. The note correctly uses j on BOTH
top and bottom frames and loses no factor two.

The graded ranks are independently checked:
1 in weight0; 2·2=4 in weight-1;
2·2+choose(2,2)=5 in weight-2;
2·2=4 in weight-3; and1 in weight-4.

## 4. Quadratic coefficient, two zero heights and the collapse test

The tensor derivation
delta_V tensor1+1 tensor delta_V is real, strictly
negative in bidegrees and makes the tensor filtration
real split after exponentiation. Uniqueness identifies
it with the Deligne operator on the tensor realization;
it commutes with the exterior projector.

Thus on e_N=e_1^D wedge e_2^D,
$$
 \delta_N^2 e_N
   =2\,\delta_Ve_1^D\wedge\delta_Ve_2^D
   =\frac{\det H^{ht}}{2\pi^2}\,t_1\wedge t_2 .
$$
The factor two comes from the two orders in the derivation,
and is consistent with the integral map j above.
A third application is zero.
The first application lies in weight-2, so its bottom
weight-4 coefficient is zero.

The exponential is 1-2i delta_N-2 delta_N².
Its bottom coefficient is therefore -Reg_E/pi².
It is real, so the first scalar height is zero.
The second scalar height uses only delta_N, hence is
also zero. This agrees with the source's definitions
and, as an extra check, its Proposition2.21 when delta³=0.
The quadratic invariant with the explicit 2pi² factor
recovers Reg_E, as stated.

For a two-step target B supported in weights0 and-4,
delta_B²=0. Naturality gives f delta_N²=0 for a map
N→B; the image of delta_N² is the entire nonzero bottom
line, so that map must kill the bottom frame.
For a map B→N, delta_N²f=0. On N its kernel is W_(-1),
because it is zero there and nonzero on the one-dimensional
top quotient. Hence the map has zero top graded map.
This proves the claimed two-direction obstruction.
It applies to the named two-step category, not all
possible secondary motives or arithmetic operations.

The canonical projections and delta are real Hodge
operations. They are not promoted to rational MHS
morphisms merely because the underlying geometric
object and graded frames are rational.

## 5. Actual rational K2 extension and tensor coefficient

The source's §1.4 identifies the real regulator with
the real extension class. Its §5.1 also gives the
underlying geometric rational construction; I checked
both, rather than infer rationality from a real Ext group.

More explicitly, take a refined rational higher cycle
Z representing the given beta2, with p=n=2. On
E times(P1)^2, remove the t_i=1 divisors and use the
0/infinity faces as the relative boundary. The support
class cl(Z) is a rational weight-zero class in degree4
with support, and maps to zero in the ambient relative
degree4 group. The latter identifies with H²(E,Q(2)),
of negative weight. Semipurity gives no degree3 support
kernel. Therefore pulling the localization extension
back along the ACTUAL rational class cl(Z) gives
$$
 0\longrightarrow H^1(E,\mathbb Q(2))
   \longrightarrow B_\beta
   \longrightarrow\mathbb Q(0)\longrightarrow0.
$$
This is a rational geometric subquotient of relative
cohomology. Clearing the finite coefficients of beta2
and retaining their rational scalar does not choose
a new extension from an arbitrary real period.
The source's Proposition5.1 and its following regulator
comparison identify its real extension with the same
Beilinson regulator.

The pure bottom K has weight-3 and types(-1,-2),(-2,-1).
Its F⁰ is zero, giving a unique top Deligne lift.
The only negative operator maps the top to K, so it
squares to zero and
U_beta=bar e_beta-e_beta=-2i delta_beta e_beta.
This is a full bottom vector, not a scalar in a guessed
rational de Rham basis.

On N tensor B_beta, the bottom weight-7 can be reached
only as weight-4 tensor weight-3. Tensor compatibility
of the Deligne bigrading therefore gives
-Reg_E/pi² times1(2)_B tensor U_beta,
exactly(5.3). Every other weight combination misses
the bottom. This verifies the full vector equation
and its actual K(2) type.

## 6. Final period and scope

The specified mixed period retains the full real cycle
2a and its period Omega_E=2omega1, the quadratic
Reg_E invariant, the fixed beta2 regulator L(E,2)/pi,
and (2pi i)^(-2). Multiplication gives
-Omega_E Reg_E L(E,2)/(4pi³).
There is no additional real-period factor and no
ordinary scalar-height replacement for the quadratic
operation.

The requested notation precision is present in the
reviewed final file: §6 explicitly distinguishes the
exterior object N from numerical level389, and its
level constants are written388 and6·389·388.
This changes no mathematical value.

The exact rational map from the spectral relative
class or its compact cup/trace projection to this
geometric tensor has not been constructed. The
note leaves that comparison and the integral lattice
statement open. A formal rescaling of real periods
or the two ordinary height vanishings does not settle
them. Full BSD remains unresolved.

No numerical script or old certificate was rerun.
Only this assigned review file was written.

## 7. Separate audit of the new relative-extension transport test

**Additional verdict: PASS for Lemma7.1 and Theorem7.2,
with precisely their literal-morphism scope.**
Reviewed the newly added §7 of
point-determinant-single-valued-attack.md at mathematical SHA256
5f96f1d7823d5c97346644a9e04ec9ccc1f6d7150924383f05df3efec3c3945a.
The earlier six-section PASS and its reviewed revision above remain
separate. Subsequent status links and completion wording are editorial.

### Proper-pair weights

Write X=X0(389), V0=X times E, B0=two copies of E.
On cohomology the restrictions kill positive-degree X factors and
are the identity on the E factors at both cusps. Thus the H¹
restriction has image the diagonal H¹(E); its cokernel is H¹(E).
The H² restriction has image the diagonal H²(E), and its kernel is

    H²(X) tensor H⁰(E)  plus  H¹(X) tensor H¹(E).

These facts give exactly(7.2).
The left and right groups have pure weights1 and2 before twisting.
Consequently D=H²(V0,B0,R(2)) has weights-3 and-2.
Both graded pieces really occur; there is no suppressed weight-1
or weight-zero term.

For H³, the preceding H² boundary cokernel is one copy of
R(-1), while H³(B0)=0 because B0 consists of curves.
The exact sequence is therefore precisely(7.3), with the
other term H³(V0) pure of weight3. After the twist its
weights are-2 and-1. This calculation uses the actual pair,
not a general claim about all open surfaces.

### Deligne-to-extension identification from this cone

The relative mixed-Hodge structure and its strict Hodge filtration
are supplied by the proper-pair filtered cone, as in
[Deligne, Hodge III, §§8.3.8–8.3.9](https://www.numdam.org/item/10.1007/BF02685881.pdf).
Applying the total Deligne cone to that filtered complex gives
the exact sequence

    0 → D_C/(F⁰D_C + D_R) → H_D³(V0,B0,R(2))
      → H³(V0,B0,R(2)) ∩ F⁰H³(V0,B0,C(2)) → 0.

This is the cone long exact sequence, using strictness to
identify the filtered cohomology with F⁰ of cohomology.
The right group is zero. Indeed a real vector in F⁰ supplies
a filtered map R(0) to H³(V0,B0,R(2)); because all target
weights are strictly negative, strictness of MHS morphisms
forces that map to be zero. Equivalently, its nonzero
highest-weight graded image would be real and in F⁰,
impossible in a negative-weight pure Hodge structure.

The left quotient has the claimed extension interpretation
WITHOUT invoking an unrestricted equivalence with absolute
Hodge cohomology. In a real extension of R(0) by D, choose a
real lift e_R and an F⁰ lift e_F of1. The difference defines
a class modulo D_R+F⁰D_C. Conversely, for v in D_C take
the real vector space D_R plus R e_R and define its Hodge
filtration by adding the lift e_R+v in levels p<=0;
the higher levels are those of D. The graded weight pieces
are those of D and R(0), so this is a mixed Hodge structure.
Changing v by the two quotient subspaces produces exactly
the isomorphic extension. These two constructions are inverse.

Thus(7.1) is justified for this pair by an explicit quotient,
and every class has a REAL extension B_c with weights0,-2,-3.
It is not asserted that every such extension is rational.
Every negative Deligne bidegree lowers weight by at least2,
so delta can map its top into D but cannot act nontrivially
within D, whose two weights differ by1. Hence delta_Bc²=0.

### The square and cubic tests

The previously checked delta_N² kills W_(-1)N and is nonzero
on its one-dimensional weight-zero top. Naturality therefore
forces the top graded map of every real MHS morphism B_c→N
to vanish. This requires no choice of a top lift.

On N tensor B_beta, tensor compatibility gives

    delta³ = 3 delta_N² tensor delta_beta,

since delta_N³=0 and delta_beta²=0. The right side kills
W_(-1): in every such tensor either the first factor lies
in W_(-1)N or the second lies in K.
It is nonzero on the one-dimensional top. The first
factor is nonzero because Reg_E>0; the second is nonzero
because the SAME beta2 has nonzero real regulator and its
two-step extension would be real split if delta_beta were zero.

Thus the kernel of this cubic operator is exactly W_(-1)
of the tensor target. Naturality and delta_Bc³=0 force
zero top map for B_c→N tensor B_beta as well.
No additional component of the operator or possible
intermediate-weight image is overlooked.

Twisting only the target by Q(-2) raises its top weight
to4. Since B_c=W0 B_c, any MHS morphism lands in W0 of
the target and cannot meet that top quotient.
Twisting both sides preserves the nilpotence argument,
as Tate structures have zero Deligne splitting operator.
The proof does not claim that every map to the twisted
target vanishes; only its top-frame part is excluded.

### Scope of the additional verdict

This is a genuine obstruction to the tested ordinary real
MHS transports. It also applies to the real extension arising
from a hypothetical rational motivic lift through this
relative group. It does NOT show that no rational motivic
lift exists: that lift need not produce either forbidden
ordinary MHS morphism. General coefficient extensions,
derived or secondary operations, and arithmetic comparisons
of evaluations remain outside this literal-map test.

The full K2 projection has a square-zero extension with
bottom H¹(E,R(2)); that is compatible with this obstruction
and does not supply the missing quadratic or cubic data.
No BSD disproof, impossibility theorem for secondary motives,
or proof of rationality is inferred.
