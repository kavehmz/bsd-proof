# Independent review of the moving marked coefficient extension

Date: 2026-09-13. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Reviewed the full [marked coefficient construction](marked-coefficient-extension-attack.md)
and its [checkpoint](marked-coefficient-extension-checkpoint.md).

**PASS after the recorded type and source-scope precisions.**
All eight sections pass in their final stated scope. I inspected
the separation of Betti logarithm from de Rham residue, the
additional Tate twist, and the narrowing of the motivic-lift
claim. No numerical formula or residue required correction.

Reviewed mathematical proof SHA256:
0b8ce84dc7b834977458fbb21a14dea75976f1b7872f007a93929a1eb011c6b3.
Reviewed checkpoint SHA256:
8614f4e66a65a66fe0e3d0cad79ffa4fbf4cfeb2c9e7a27f501d3685a6fd844c.
Subsequent PASS/header/status edits are editorial.

The actual one-motive family, geometric realization, connection,
monodromy and real Deligne obstruction are constructed. A specified
motivic coefficient realization and top map, a rational spectral
input, and motivic obstruction vanishing remain additional steps.
The coefficient family alone does not establish BSD rationality.

## 1. The full algebraic marking and its moving realization

I checked the actual curve law on y²+y=x³+x²−2x. For distinct
points the slope lambda gives
x_(U+V)=lambda²−1−x_U−x_V and
y_(U+V)=−y_U−lambda(x_(U+V)−x_U)−1.
It gives
\[
 R=(4,8),\quad S=(-51/25,-68/125),\quad T=(1/16,-9/64)
\]
from P,Q as asserted.

The fixed corrections are precisely the rational h1,h2 from the
[reviewed relative point proof](relative-modular-cycle-attack.md),
with denominator3 in h2. Their values at(O,P,Q) are
(1,5,5/3) and(1,4,4). The original finite symbol matrix and
these principal evaluations cancel PRIME BY PRIME on the
irreducible-fiber regular model. In particular denominator primes
in h1,h2 are not excluded from the correction argument: the
difference between a generic divisor closure and the full model
divisor is vertical, and degree-zero D_i has zero intersection
with a full fiber.

The new construction keeps the ENTIRE support of the corrected
Z1,Z2. The set Sigma_E={a−Z} is finite and Galois-stable, and it
does not contain O because the fixed supports avoid A={O,P,Q}.
On its complement the translated divisors still avoid A and
have the same Picard classes P,Q. Thus their Abel–Jacobi values
give actual algebraic sections of the constant semiabelian
group G=J(E,A). The family [L→G] is consequently defined over Q.

The translated support is a finite étale marked family in
(E minus A)×S_E. Pulling back its relative homology by the
full two divisor markings gives rank six with graded ranks
2,2,2 in weights0,−1,−2. The prescribed integral lattice is
the pullback lattice, not an asserted saturation inside an
unmarked larger group.

I checked the relevant primary realization statements:
[Sertöz–Ouaknine–Worrell, §6.5, Proposition6.5.43](https://arxiv.org/html/2505.20397v1)
keeps the boundary lattice, torus residues and2pi i in the
period pairing. [Milne, IV§2, Proposition2.4](https://www.jmilne.org/math/articles/1990aT.pdf)
gives the general one-motive Betti/de Rham comparison.
The construction uses those general realizations, without
assuming that this varying marking is a symmetric polarized
degeneration of the more restrictive kind.

Pullback by the actual pi is legitimate. Both original cusps
map to O, which is not in Sigma_E, so their fibers are the
original M0 with its original markings. The extra collision
points remain an actual interior boundary.

## 2. The Miller function, torus coordinate and full divisor

Use the chord with coefficient1 on y, divided by the vertical
line through A+x. Its divisor in w is
[A]+[x]−[A+x]−[O]; the third chord intersection cancels the
other point of the vertical line. The quotient
m_(R,x)/m_(A_j,x) therefore has divisor
T_x((A_j)−(R))−((A_j)−(R)).
Multiplication by h_j(w−x)/h_j(w) gives exactly
T_x Z_j−Z_j, with the stated function order.

At w=O both normalized Miller functions have leading term
−t_w^(-1). Their quotient has leading coefficient1. Since
h_j(O)=1, its normalized evaluation gives exactly
\[
 a_{ij}(x)=
 \frac{m_{R,x}(P_i)}{m_{A_j,x}(P_i)}
          \frac{h_j(P_i-x)}{h_j(P_i)h_j(-x)}.
\]
Possible rational factors depending only on the base x cancel
between the evaluations at P_i and O. As x tends to O, the
Miller functions have the same leading behavior, and the
remaining ratio tends to1. Thus a_ij(O)=1, including at
apparent degeneracies of the generic Miller expression.

The torus sign is consistent with the fixed generalized-Jacobian
framing: the principal divisor contributes F(D_i)=F(P_i)/F(O).
It agrees with the real-normalized third-kind identity
Re integral_(div F) eta_i=log|F(P_i)/F(O)|. No inverse torus
coordinate has been inserted.

Intersecting the actual moving graphs with the two fixed sections
w=P_i and w=O gives
\[
 \operatorname{div}_x a_{ij}
 =\sum_Zn_{j,Z}([P_i-Z]-[-Z]).
\]
The fixed divisors do not meet these sections, and vertical
base divisors meet them with the same multiplicity and cancel.
Each moving graph is a translate, so its intersection multiplicity
is the retained coefficient n_(j,Z). This proves the divisor formula
including every point from the principal corrections.

It follows that the a_ij are units on S_E. Their nonconstancy
argument is also valid: a nonzero finite divisor cannot be
invariant under translation by the non-torsion P_i. Such invariance
would give an infinite orbit in its finite support. The divisor
[-1]_*Z_j is nonzero since its Picard class is non-torsion.

## 3. The exact new rational values and residue matrix

I independently evaluated the displayed functions using rational
Fraction arithmetic, separately from the author's computation:
\[
 (h_1(S),h_2(S))=(505109/205209,72126/22801),
\]
\[
 (h_1(T),h_2(T))=(14977/3969,1945/441).
\]
All four are nonzero.

At R=(4,8) and−R=(4,−9), x−4 is a local parameter because
2y+1 is respectively17 and−17. The leading numerators of
h1 are8320 and−9360, and those of h2 are160 and−180.
Thus both functions have pole order two at both points.
The coefficient of Z_j at R is−3 and at−R is−2. The new
values just checked give Z1(S)=1,Z2(S)=0,Z1(T)=0,Z2(T)=1.

The divisor formula now gives
ord_(-R)(a_ij)=n_(j,P_i+R)−n_(j,R), hence
\[
                  (\operatorname{ord}_{-R}a_{ij})
                      =\begin{pmatrix}4&3\\3&4\end{pmatrix}.
\]
Its determinant is7. No normalization by a period or L-value
entered these rational evaluations.

These were new targeted checks of the asserted residue construction.
No old analytic, rank, regulator or certificate routine was rerun.

## 4. Connection, height variation and the exterior factors

The marking equality is a Baer sum with the pushed Kummer
extension whose columns are(a_1j,a_2j). Therefore the connection
in the specified Baer-sum de Rham frame is
\[
 \nabla e_j=-\sum_i d\log a_{ij}\,t_i,\qquad
                         \nabla|_{H_{\rm dR}(G)}=d.
\]
The horizontal Kummer vector is e_j+sum log(a_ij)t_i.
Positive continuation around a zero changes this by
2pi i times the order. With t_i^B corresponding to
2pi i t_i^dR, the integral Betti monodromy adds
sum ord(a_ij)t_i^B to e_j^B. This verifies both signs.
The constant M0 comparison and its nontrivial point extensions
are retained; this frame does not split M0 as a Hodge structure.

All these connection matrices map the top lattice to the torus
and vanish on the lower part. Their products vanish on the
rank-six representation, so the connection is flat with
nilpotent logarithmic residues. Its exterior connection remains
flat by functoriality.

The principal-period identity gives the actual moving
archimedean block H_ij(x)=H_ij+log|a_ij(x)|.
The completed Deligne-lift calculation then yields
delta_V(e_j^D)=sum H_ij(x)t_i^B/(2pi), with delta_V²=0.
Tensor derivation gives
\[
 \delta_{\wedge^2V}^{\,2}(e_1^D\wedge e_2^D)
      =\frac{\det H(x)}{2\pi^2}t_1^B\wedge t_2^B.
\]
The quadratic term in exp(−2i delta) is minus2 delta²,
giving the stated conjugation coefficient−det H(x)/pi².
There is no missing exterior factor two.

The abstract integral wedge embeds by x∧y→x⊗y−y⊗x.
Geometric exchange on degree-one cross degree-one introduces
the Koszul minus sign, so its rational PLUS projector realizes
this wedge. No integral inverse of that projector is used.

At x=O, det H(x)=Reg_E. Near−R its leading term is
7(log|t|)², so the specified neighborhoods have nonzero
quadratic component. No nonvanishing at every fiber follows.
At a moving rational x, the additional finite symbol is
v_p(a_ij(x))log p. The global convention subtracts the
sum of these finite symbols from the archimedean term.
The product formula therefore keeps the GLOBAL point-height
matrix fixed. The moving archimedean determinant is not
misidentified with the full global regulator.

For the actual K2 extension B_beta, delta_beta²=0 and its
nonzero regulator supplies delta_beta≠0. Thus on the tensor
the cubic operator is3delta_W² tensor delta_beta, nonzero
on the specified top frame wherever det H(x)≠0.
This is a coefficient realization constructed before a
spectral scalar is evaluated.

## 5. Boundary monodromy and the exact residue conventions

At s above−R the residue matrix acquires the ramification
factor e_s. On the Betti exterior representation the two
orders of the derivation give
\[
 \Lambda_s^2(e_1\wedge e_2)=14e_s^2(t_1\wedge t_2).
\]
The bottom component of T_s−1 is half of that, namely
7e_s²(t_1∧t_2). These are integer matrices with their
native Betti Tate frames.

There is no invariant top lift. The weight−2 component of
(T_s−1)e_12 is nonzero, while applying T_s−1 to a lower-weight
correction lands in still lower weight and cannot cancel it.
This is an obstruction in the NEW varying coefficient, not
a claim about every derived lift of the original input.

I requested and inspected the explicit de Rham/Betti distinction:
the logarithmic operator is q d/dq−N_dR, with
Res(nabla)=−N_dR, whereas
T_s=exp(2pi i N_dR) in comparison coordinates and
Lambda_s=log T_s=2pi i N_dR. Thus the positive coefficient
operator is nI−N_dR. Its inverse is a finite nilpotent series
in N_dR/n and preserves the radius of an analytic power series.
Only the constant coefficient remains in the local logarithmic
complex. Its sign and nonzero2pi i scalar do not change
kernel or cokernel.

The rational Betti boundary complex [W→(T_s−1)W] in degrees0,1
is the actual circle-cochain model. The rank-six monodromy is
J2⊕J2⊕J1⊕J1 over Q. Its exterior square is
J3⊕J2^4⊕J1^4: dimension15, rank(T_s−1)=6, and kernel and
cokernel dimensions nine. The top quotient is visible in the
coinvariants even though it has no invariant lift.
No integral change of basis dividing7 is claimed.

## 6. The real coefficient triangle and its precise rational scope

The coefficient complex is the actual relative Betti/de Rham
and real Deligne complex for(S×E_t,B_cusp), with the
geometric variation W(2). The restriction of the original
real radial class is an ordinary relative-cohomology
open pullback. Deleting Sigma does not turn it into a
compact-support restriction.

The exact top quotient W→Q(0) and F=W_(-1)W give the
coefficient triangle and its connecting class
O_W(c_S) in H_D^4(K_F(2)). The long exact sequence proves:
a real lift exists exactly when that class vanishes, and
the choices form a torsor under the IMAGE of H_D^3(K_F(2)).
It is not necessary to assume this image is the full group.

The top transition formula follows by taking the wedge of
e_j^(b)=e_j^(a)+sum n_ij^(ab)t_i. Its quadratic bottom term
is exactly det(n^(ab))t_1∧t_2. The de Rham transition term
comes from the displayed connection, and a scalar two-form
multiplies it with a PLUS sign because its form degree is two.
The constant point-extension Hodge comparison remains present.
Consequently these formulas specify the actual cochains
needed for the connecting class; the monodromy matrix alone
does not evaluate it.

The source's ordinary Betti degree-three component of the
original Deligne input is already zero. Using only that
component would indeed miss its filtered and comparison
data. The construction correctly makes no assertion that
the full real connecting class vanishes.

I also requested and inspected the explicit Tate accounting.
Here K=H¹(E,Q(2)) already has weight−3. Unshifted W⊗B_beta
has bottom K(2), weight−7. The ADDITIONAL overall twist(2)
in the analogous coefficient complex gives K(4)=H¹(E,Q(6)),
weight−11. W(2) itself has bottom Q(4). These different
objects are no longer conflated.

Finally, the initial sentence asserting a rational motivic
version of the coefficient triangle was narrowed. An actual
algebraic one-motive and its geometric variation are available,
but a specified motivic coefficient object/top map in a chosen
motivic category is an ADDITIONAL construction. Rational
spectral input and motivic obstruction vanishing are also
needed. None is inferred merely from the VMHS or a real
vanishing statement. I inspected this exact repair in§6;
it is consistent with the final stated gap.

## 7. The added Poincaré boundary is genuinely nontrivial

The actual graph line is
O(Gamma_pi−C×O)=d^*O_E(O) tensor p_E^*O_E(O)^(-1),
where d(z,w)=w−pi(z). Restriction at a cusp gives the
canonical trivial line because pi(c)=O. At a new fiber s
the restriction is O_E(pi(s)−O). For s above−R this is
the non-torsion point class−R.

That line remains nontrivial after every field extension:
its image in Pic^0 over an algebraic closure is the same
nonzero point. It also remains nonzero after rationalizing
Pic^0 because the point is not torsion. Thus no assignment
of zero trivializations on all added fibers can make this
particular graph line a class in the corresponding usual
relative Picard group.

The proposed repair retains the ACTUAL tuple of boundary
line bundles and forms the homotopy fiber of Picard
restriction over that tuple. The given graph line, its
old cusp trivializations and its identity boundary
restrictions are an actual rational object there.
Two choices differ by a line with trivialized boundary,
so this is the stated torsor for relative Picard data.

This matches [MVW, Definition7.10 and the subsequent relative
Picard sequence](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).
A real normalization of a Green potential does not replace
an algebraic trivialization of the nonzero degree-zero line.
The proof does not use a nonexistent proper push from the
ordinary nonproper open to avoid this boundary.

## 8. Verdict and remaining comparison

The final construction retains a nonconstant rational marked
family, its integral torus and point frames, every principal
finite correction, a nonzero residue matrix and the quadratic
and cubic Deligne components. Its boundary complex keeps
the information that an invariant-stalk truncation would lose.

The remaining lifting class and nontrivial Poincaré boundary
are explicit and unevaluated. Their existence does not
construct a rational spectral lift or the scalar
6·389·388 n_E. The required motivic coefficient construction,
arithmetic comparison and integral lattice statement are
still conclusions to prove.

Only the new exact function values and the associated group-law
coordinates were checked here with rational arithmetic.
No old certificate, prime scan or numerical period calculation
was rerun. This assigned review is the only file edited for
the marked-family audit. No mathematical correction remains
in the reviewed scope, and full universal BSD remains open.


## 9. Separate additional verdict for the motivic construction and real lift

**PASS for the additional §§9–10**, after inspecting the explicit
alternating top-frame clarification. This is a separate verdict from
the original eight-section review above. The former motivic-object
qualification was correct for that earlier version; new§9 now
constructs that object and its top map. New§10 proves REAL lift
existence for the particular input, with no canonical or rational
lift inferred.

Reviewed additional proof SHA256:
30b53a2840611c14e3f40d0a7f2a124fa3c18b33ba80dd72ada0051a659de451.
Reviewed additional checkpoint SHA256:
873c5d8740a9854a8a984d1a0f4abbdb241623f5e6843f51a65357af6b569b4b.
No further mathematical correction is required in these additions.

### 9.1. Primary motivic formalism applies to these actual objects

I directly read [Cisinski–Déglise, 8September2019 author version](https://deglise.perso.math.cnrs.fr/docs/2019/DM.pdf),
especially2.4.31,2.4.50,14.2.9–11,14.4.1,15.2.1,
16.2.18 and17.2.18–22. The base and all schemes used here
are regular finite-type Q-schemes and hence satisfy the
quasi-excellence hypotheses for constructible direct images.
The HB-module presentation supplies a stable enhancement;
the fibers, cofibers and maps of diagrams can be formed
there without invoking a motivic t-structure.

The six operations and rational absolute purity give the
stated localization triangle for the CONSTANT proper elliptic
curve with its three puncture sections:
\[
 (p_A)_*1(-1)[-2]\longrightarrow\bar p_*1
                            \longrightarrow p_*1_U.
\]
The codimension-one term is(-1)[-2], not an omitted Tate
term or a compact-support substitute for p_*.
Smooth proper motives are strongly dualizable, and their
cohomological duals p_*1 are therefore strongly dualizable.
Finite étale objects are as well. The thick-subcategory
argument then proves dualizability of the particular open,
relative, dual and marked objects used here.

This is a direct argument for these objects. It does not
assume that every constructible motive over a positive-dimensional
base is rigid. Proper base change applied to the first two
terms also identifies the open cohomology motive with
the constant open-curve motive. No arbitrary improper base
change theorem is needed for its fibers.

I checked the Hodge realization scope separately in
[Tubach2407.02256v3, Theorem1.4 and Remark1.2](https://arxiv.org/html/2407.02256v3).
It gives a six-functor-compatible Hodge realization on finite-type
C-schemes, whose rational underlying functor is Betti.
CD16.2.18 gives the required rational étale/Beilinson comparison.
Applying this AFTER base change to C is justified.
The speculative arithmetic-MHM generalization in Tubach
Remark1.3 is not assumed.

### 9.2. Artin splitting, positive marking and the shift/dual

The moving support is exactly B*×S as a finite étale scheme
over S; its embedding into the constant punctured elliptic
curve varies. If its geometric degree is b, the finite étale
trace composed with the unit is multiplication by b.
Hence
\[
 e_B=1-b^{-1}\operatorname{unit}\circ\operatorname{tr}
\]
is an idempotent whose image identifies with the cofiber
of the constant-function unit. This division is explicitly
rational. It does not assert an integral direct summand.

The cofiber map
A_B→C_rel[1] comes from the actual commutative unit/restriction
diagram. I independently checked its sign in the declared
relative complex:
\[
 D(a,c)=(da,i^*a-dc).
\]
The canonical cofiber boundary sends beta to(0,−beta).
A relative path functional has coordinates(gamma,−Z):
it annihilates D(a,0), since its two evaluations are
a(partial gamma) and−Z(a). Pairing(gamma,−Z) with
(0,−beta) gives +Z(beta). Thus the dual map is the
POSITIVE relative-homology boundary as required.

On each closed-point component the weighted trace lambda_j
has geometric value n_(j,Z) at every conjugate point.
Its composite with the unit is deg(Z_j)=0, including all
residue-field degrees. Its dual therefore gives precisely
the original divisor marking L→A_B^vee. There is no
division of individual divisor multiplicities by their
residue degrees.

The relative cohomological fiber has only H¹:
H⁰(U)→H⁰(B) is injective, U is the noncompact punctured
curve with H²(U)=0, and B has no positive cohomology.
Thus C_rel[1] has relative H¹ in ordinary degree zero,
and its tensor dual V_all has relative H1 in degree zero.
Its boundary onto Div0(B)_Q is surjective. Consequently
\[
 \operatorname{Fib}(V_{\rm all}\oplus L
                          \xrightarrow{\partial-\mathrm{mark}}A_B^\vee)
\]
realizes an ordinary pullback, with no unwanted degree-one
cohomology. Its kernel has rank4 and its quotient L has
rank2. This reconstructs the actual marked rank-six
one-motive, including the complete h_j divisor support.

The same maps of algebraic de Rham complexes, their
evaluation at the moving support and their integration
comparison give the previously calculated connection.
No constant splitting of the nontrivial variation is
inferred from the constancy of the open underlying curve.

### 9.3. Exterior frame, top map and the coefficient triangle

The realizations are symmetric monoidal and preserve the
rational antisymmetrizer. Since V_marked realizes a vector
space in ordinary degree zero, (1−tau)/2 gives its ordinary
exterior square. The earlier shift[1] is essential: exchange
on the unshifted geometric degree-one factors has an extra
Koszul minus. This agrees with the previous PLUS geometric
interchange; no exterior sign has changed.

I requested and inspected the explicit top-frame statement.
The target image line in L tensor² is framed by
e1 tensor e2−e2 tensor e1, mapped to1, using the same
alternating tensor frame on the source. The raw projector
of e1 tensor e2 is half this generator. With the stated
frames the induced top map has coefficient one, not two.
The denominators b and2 in the rational projectors remain
visible; no integral motivic primitivity is concluded.

Its fiber F_mot is an ACTUAL motivic fiber of this top map.
On realizations the map is surjective in ordinary degree zero,
and its kernel is exactly W_(-1)W. Thus it realizes the
coefficient F from§6 without requiring a motivic weight
truncation functor.

The pushforward/relative fiber in(9.8) is now a specified
object of DM_B(Q). Exactness of the six operations and of
finite homotopy limits supplies its coefficient triangle.
Taking Hom(1,K[j]) defines the claimed motivic groups and
their actual connecting map. Its Hodge realization has a
natural map to the real Deligne cone by forgetting to the
Betti/filtered comparison complex. This is not a general
identification of absolute Hodge with ordinary Deligne
cohomology for a nonproper coefficient object.

The localization
j_!W_mot→j_*W_mot→i_*i^*j_*W_mot
is also an actual triangle. Its realization keeps the
previous local invariants/coinvariants complex. It does
not trivialize any of the nonzero added Poincaré fibers.

## 10. Separate audit of real lift existence

The proof of Proposition10.1 passes. Its noncompact base and
its use of the PARTICULAR proper-origin class are substantive.

### 10.1. Relative cohomological dimension and the product

Sigma is nonempty because−R is in Sigma_E and pi is finite
surjective. Thus S=C minus Sigma is a connected noncompact
finite-type complex curve. It has a finite graph spine which
can contain the two old cusps as vertices. This gives a
relative CW model of dimension one for(S,B0).

For every finite-rank local system A, H^i(S,B0;A)=0 for
i≥2. Also H⁰(S,B0;A)=0: a horizontal section zero at
one marked point is zero on the connected curve. These
arguments do not use semisimplicity or constant monodromy.

For0→F→W→Q→0, the relative long exact sequence therefore
surjects H¹(S,B0;W_C) onto H¹(S,B0;C).
Relative Künneth for the actual coefficient pulled back
from S gives
\[
 H^2(S\times E,B_0\times E;W_C(2))
      =H^1(S,B_0;W_C)\otimes H^1(E,C)(2).
\]
The missing degree-zero and degree-two base summands
vanish by the preceding statements. Tensoring the
surjection with H¹(E,C) proves the asserted surjection
on full COMPLEX degree-two cohomology. The twist is
on the whole coefficient, exactly as written.

This H¹ lifting is compatible with the earlier absence
of an invariant top lift at the new punctures. H⁰ of
a local boundary stalk and H¹ of a noncompact relative
base are different tests.

### 10.2. Why the particular real Deligne class lifts

For any of these Deligne coefficient cones there is a
natural map a_D from H² of its complex cochain term
to H_D³, by inclusion of that term shifted by−1.
This map exists independently of whether the nonproper
Hodge filtration is strict on cohomology. It is functorial
for the actual top quotient and the open-pair restriction.

The original proper-pair result was independently checked
against its completed proof and review. Before twisting,
H³(C×E,B0×E;R) is an extension of one R(−1) by
the pure weight-three H³(C×E). After twist2 its weights
are−2 and−1. The proper relative filtered cone and
strict Hodge filtration therefore have no next real
F⁰ Hodge-class term. Accordingly every class in its
degree-three real Deligne group, including C_j2, is
a_D(w) for some complex degree-two class w.

This is stronger than saying only that its ordinary
Betti component is zero. It is also a statement about
the ORIGINAL proper pair; the proof does not assert
a_D is surjective for every nonproper coefficient
complex or for every class on the open pair.

Restrict w, lift that complex class through the
surjection in10.1, and apply the natural a_D.
Commutativity gives exactly c_S as its top image.
Thus the REAL connecting class O_W(c_S) is zero.

If the arithmetic real involution is required, the
Q-defined geometry and maps give the compatible
real-linear involution on these Deligne cones.
Averaging a lift with its conjugate preserves its
invariant top image. This does not create a rational
motivic class or select a canonical lift.

### 10.3. What the additions close

The motivic coefficient object and its top map are
now constructed, and the actual real input has some
real coefficient lift. These two substeps are completed.

The proof does NOT construct a rational motivic class
whose regulator is c_S. If such an input is constructed,
its specified motivic connecting class in degree four
still needs to vanish, and a boundary-compatible
rational lift still needs selection and comparison.
The real lift torsor remains the image torsor from§6,
without a preferred point. Its existence does not make
the added Poincaré boundary zero or yield the scalar
6·389·388 n_E in the point/K2/Tate determinant lattice.

The original eight-section verdict remains preserved
above; this separate PASS records precisely the new
motivic-object and real-existence results. No numerical
certificate or prior rational arithmetic was rerun for
this additional source/derived-cohomology audit.

