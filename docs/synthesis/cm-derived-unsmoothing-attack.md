# Actual coefficient cones and higher CM point augmentation

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: all eight sections completed with a
[full independent PASS review](review-cm-derived-unsmoothing.md).
Reviewed mathematical revision:
c37c8b717bea884135fc5a241a6318383f9bfc59c726449821be6bbfe9ac80df.
Completion links are editorial; the reviewed mathematics is unchanged.
Restart: [checkpoint](cm-derived-unsmoothing-checkpoint.md).
This uses the completed [division-torsor construction](cm-symbol-point-reciprocity-attack.md)
and [its review](review-cm-symbol-point-reciprocity.md).
Full BSD over Q remains the objective.

The new construction is an actual single-point coefficient cone and
its canonical class. Its relation to the joint norm-root object
identifies a genuinely higher augmentation layer. The exact p²
tower norm then kills every fixed point jet at sufficiently large
depth, even with full p^k coefficients. A separate actual higher
relative class is nonzero with exact order p^k; its local boundary
and CM branch explain why that nonvanishing is not the desired
unsmoothed comparison. Rational renormalization is constructed only
in its genuine unbounded coefficient lattice.

## 1. Fixed arithmetic source and finite coefficients

Keep
\[
 E:y^2=x^3+39x,\quad K=\mathbf Q(i),\quad
 P=(3,12),\ Q=(27,144),\quad R\in\{P,Q,P+Q\},
\]
with the Néron differential dx/(2y) and the full basis P,Q.
Use f_0=39(1+i)^3, f=(f_0), Omega_infinity=(1+i)Omega_E/2,
\[
 p\ge5,\quad p\equiv1\pmod4,\quad p\nmid2\cdot3\cdot13,\quad
 F_m=K(f p^m),\quad \tau_m=\Omega_\infty/(f_0p^m).
\]
Fix compatible p^m-division points only when writing coordinates.
All torsors and the maps between them below exist without those
choices. Put K_n=K Q_n, where Q_n is the nth cyclotomic layer.

The fixed rational function Theta_a is the twelfth power in the
preceding proof, with a=5 unless p=5, when a=7. Its exact full-fiber
norm is
\[
 N_{[p]}\Theta_a=\Theta_a.
\]
This is [Kato1.3(1)(ii),(4)](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
with constant one. It is distinct from taking only primitive
ray orbits. The preceding proof established the full split Cartan
over F_0, the full (Z[i] tensor Z_p)-basis P,Q, and
\[
 \operatorname{Gal}(F_m(P_m,Q_m)/F_m)=E[p^m]^2.
\]
The single-point field M_m^R=F_m(R_m) has degree p^(2m).

Let A_k=Z/p^k, and always impose
\[
                         m\ge\max(k,n+1).                  \tag{1}
\]
Set T_k=T_pi E/p^k. Retain rho=(Psi^c)^(-1),
mu_(p^k) tensor rho=T_k, and the compatible vector prescribed
by gamma_CM=2pr_rho(gamma_E^+). It is trivialized over F_m,
as required for the finite twisting operation.

Write G_n=Gal(K_n/K), gamma for its fixed generator, and
g_p=log_p(1+p). The image in A_k[G_n] of the OLD smoothing unit is
\[
 q_{a,n,k}
 =12\left(a^2-u_a\gamma^{\,2\lambda_a}\right),\quad
 u_a=\Psi^c((a)),\quad\lambda_a=\log_p(a)/g_p.                 \tag{2}
\]
The exponent uses the cyclotomic QUOTIENT X,Y→T. This is not
the diagonal-subgroup generator and introduces no factor1/2.
The exponent in the finite group is defined by reducing the
p-adic integer2lambda_a modulo p^n.

Its constant augmentation is the previously checked p-unit,
so(2) is invertible in the finite group ring. The tame degree
1152(p−1)^2 is still handled by UNNORMALIZED corestriction.
We use(2) to retain the given normalization, without asserting
that the new point construction is independent of a.

The preceding iota_p, u(0), Smith/polarization frame factors and
c_cmp,p=(156i Omega_p)^(-1) are not reset to1. None defines a
map from a new coefficient module merely by its being a unit.

## 2. An actual single-point coefficient extension and its unique class

Let Y_(R,m)=[p^m]^(-1)(R), a finite étale K_n-scheme of degree
p^(2m). Its permutation module is
\[
 {\cal P}_{R,m,k}=A_k[Y_{R,m}],\quad
 {\cal I}_{R,m,k}=\ker({\cal P}_{R,m,k}\xrightarrow{\mathrm{aug}}A_k).
\]
The exact coefficient extension is
\[
 0\to{\cal I}_{R,m,k}\otimes T_k
 \to{\cal P}_{R,m,k}\otimes T_k
 \xrightarrow{\mathrm{aug}}T_k\to0.                         \tag{3}
\]
All tensor products here are over A_k; T_k is free of rank one.

Over F_m the coordinate algebra of Y_(R,m) is the actual field
M_m^R. The function
\[
                     u_{R,m}(S)=\Theta_a(\tau_m+S)           \tag{4}
\]
is an invertible element of that algebra. Its Kummer class,
through finite étale Shapiro, is a class in
H¹(F_m,P_(R,m,k) tensor mu_(p^k)). Twist there by the prescribed
rho vector, then corestrict and normalize:
\[
 {\cal A}_{R,n,m,k}
  :=q_{a,n,k}^{-1}\operatorname{Cor}_{F_m/K_n}
           \bigl(\delta_k(u_{R,m})\otimes t_{\rho,k}\bigr)
  \in H^1(K_n,{\cal P}_{R,m,k}\otimes T_k).                  \tag{5}
\]
The permutation coefficients in(5) are not deleted.

**[NEW deduction] Theorem2.1.** There is a UNIQUE class
\[
 \eta_{R,n,m,k}\in H^1(K_n,{\cal I}_{R,m,k}\otimes T_k)        \tag{6}
\]
whose image in(5) is A_(R,n,m,k).

*Proof.* Its augmentation is exactly the complete single-point
transfer already computed:
\[
 q_{a,n,k}^{-1}\operatorname{Cor}_{F_m/K_n}
       \bigl(\delta_k(w_R)\otimes t_{\rho,k}\bigr)=0,\qquad
                         w_R=\Theta_a(\tau_0+R)\in F_0^\times.
\]
The actual ray homothety with p-components(−1,−1) fixes F_0
and K_n, whereas it acts as−1 on rho. Corestriction is invariant
under that element, and2 is a unit; this is the preceding exact
zero, not a newly assumed local condition.

Moreover H⁰(K_n,T_k)=0 because that same homothety acts by−1.
The long exact sequence of(3) therefore injects H¹(I tensor T_k)
into H¹(P tensor T_k), with image the augmentation kernel.
Existence and uniqueness of(6) follow. ∎

The coefficient extension(3), or its mapping cone, precedes any
derivation. It supplies the class without choosing a primitive
to force a desired scalar. Standard finite continuous cochains,
Shapiro and this exact-sequence construction are the primary
formalism in [Nekovář§§3.4,6.1,8.1](https://www.numdam.org/item/AST_2006__310__R1_0.pdf).
No Sha-finiteness, Selmer-corank or nonzero-c2 hypothesis occurs.

There is an explicit cochain formula. Choose an origin R_m and
let A(g) represent(5), with e(g)=aug A(g). The zero augmentation
class and H⁰(T_k)=0 give a unique v in T_k such that e=dv.
For any h whose action on T_k is−1,
\[
                             v=-e(h)/2.                    \tag{7}
\]
Lifting v as v e_(R_m), the corrected cocycle
A−d(v e_(R_m)) lies in I tensor T_k and represents(6).

Modulo I², the extension P/I² is the ACTUAL point-Kummer
extension: g e_(R_m)=e_(R_m)+kappa_(p^k)(R)(g).
Thus its first moment is
\[
 A_1(g)-g(v)\otimes\kappa_{p^k}(R)(g)
             \quad\hbox{in }T_k\otimes E[p^k].              \tag{8}
\]
Here A_1 is the first weighted moment in the chosen origin.
The plus point-Kummer sign in the coefficient action is explicit;
it is not the old inverse cyclotomic sign−c_gamma.
Changing roots, transfer representatives or origin changes(8)
by a coboundary, as also follows from uniqueness in(3).
In particular v in(7) is not a free point correction.

## 3. The actual p² tower law

The point torsor map [p]:Y_(R,m+1)→Y_(R,m) gives the
Galois-equivariant coefficient projection
\[
 \pi_{m+1,m}:{\cal P}_{R,m+1,k}\to{\cal P}_{R,m,k},
                  \qquad e_S\mapsto e_{[p]S}.              \tag{9}
\]
It preserves augmentation.

**[NEW deduction] Proposition3.1.** For fixed n,k and m satisfying(1),
\[
 \pi_{m+1,m,*}{\cal A}_{R,n,m+1,k}
                         =p^2{\cal A}_{R,n,m,k},\qquad
 \pi_{m+1,m,*}\eta_{R,n,m+1,k}
                         =p^2\eta_{R,n,m,k}.                \tag{10}
\]

*Proof.* Over F_(m+1), projection(9) is the norm on each
p-division fiber of the point. Its theta product is u_(R,m)
by the EXACT identity N_[p]Theta_a=Theta_a, because
[p]tau_(m+1)=tau_m. Corestricting next from F_(m+1) to F_m
multiplies this pulled-back unit class by p². Indeed that
ray extension has degree p², and rho modulo p^k is already
trivial on G_(F_m), so its vector is unchanged in this step.
Transitivity of corestriction and the fixed unit(2) give the
first equality.

Equivalently the actual single-point tower M_(m+1)^R/M_m^R
has degree p^4. Its p² point translates each occur p² times,
so the full field norm is u_(R,m)^(p²). This is consistent
with the two-step calculation, not the joint tower's p^4
multiplicity.

By the commuting augmentation sequence, both sides of the
second equality map to the first one. The H¹ map in(3) is
injective, so uniqueness gives the second equality. ∎

This keeps all p^k information. It is not a norm-compatible
integral Iwasawa class with the p² factor suppressed.

## 4. Every fixed point jet vanishes at a stated finite depth

The powers I^j are well-defined for a permutation torsor:
choose an origin to identify its module with the group ring
of E[p^m]. Changing origin multiplies by a group unit, so
the subspaces I^j do not change. Galois affine transformations
preserve this filtration.

**[NEW deduction] Theorem4.1.** Fix n,k and a jet order d≥1. Choose
\[
 r\ge\max\{n+1,\ k+\lfloor\log_p d\rfloor\},\qquad
                         m\ge r+\lceil k/2\rceil.           \tag{11}
\]
Then the image of the ACTUAL class(6) is zero in
\[
 H^1\left(K_n,
   ({\cal I}_{R,m,k}/{\cal I}_{R,m,k}^{\,d+1})\otimes T_k
          \right).                                        \tag{12}
\]
This holds for P,Q,P+Q and every p in the stated good split range.

*Proof of stable coefficient jets.* With compatible origins
and Tate bases the group ring has the presentation
\[
 A_k[X_1,X_2]/
       ((1+X_1)^{p^r}-1,(1+X_2)^{p^r}-1).
\]
For1≤j<p^r,
\[
 v_p\binom{p^r}{j}=r-v_p(j).
\]
Indeed binom(p^r,j)=(p^r/j)binom(p^r−1,j−1), and the second
factor is a p-unit, as follows by expanding(1+X)^(p^r−1)
modulo p. Condition(11) makes every coefficient of degree
1 through d divisible by p^k; it also gives d<p^r.
The point jets at all levels m≥r are therefore identified,
by their actual projection, with
A_k[X_1,X_2]/(X_1,X_2)^(d+1), and similarly for the
augmentation submodule. These identifications are
Galois-equivariant since the torsor projections are.

Iterating(10) gives
\[
                    \pi_{m,r,*}\eta_m=p^{2(m-r)}\eta_r.
\]
The right side is zero over A_k under(11). After the
Galois-equivariant jet identification this proves(12). ∎

These are maps of finite coefficient modules and their cohomology.
No equality H¹(C) tensor A=H¹(C tensor^L A) is presumed;
possible base-change/Tor terms are not discarded. The theorem
does not set the entire coefficient module, the full relative
class, or all operations of growing order to zero.

For example, at k=1 the first point-layer(8) vanishes for
m≥max(n+1,1)+1. The statement over ALL k matters: a vanishing
modulo p alone could not exclude an output divisible by p.
Here every fixed finite-precision, fixed-order point-jet
realization of this tower is eventually zero.

## 5. The genuinely higher layer in the original joint norm-root object

This section works first modulo p, where its exact filtration
degree can be computed without a false integral graded-ring
simplification. Let q=p^m and
H_m=E[p^m]^2 be the JOINT translation group from the prior proof.
For R=P,Q,P+Q let K_R be the kernel of its projection to the
R-coordinate. It is a copy of E[p^m], of rank two over Z/p^m.

The finite étale quotient from the joint division torsor to
Y_(R,m) gives the intrinsic replication map
\[
 j_R:\mathbf F_p[Y_{R,m}]
               \hookrightarrow\mathbf F_p[Y_{P,m}\times Y_{Q,m}].
\]
Its image, after an origin is chosen, is multiplication by the
FULL norm element N_(K_R)=sum_(t in K_R)[t].

**[NEW deduction] Proposition5.1.** Put D_m=2(p^m−1). The actual
repeated-root cocycle of the previous canonical joint norm-root
torsor lies in I_joint^(D_m). Its leading class is
\[
        \delta_p(w_R)\otimes\nu_{K_R}
        \quad\text{in }H^1(F_m,\mu_p\otimes
                                  I^{D_m}/I^{D_m+1}),       \tag{13}
\]
where nu_(K_R) is the canonical leading norm element.
After the SAME rho twist, unnormalized corestriction and
normalization(2), the class lifts canonically to degree D_m+1;
that lift is j_R(eta_(R,n,m,1)).

*Proof.* In characteristic p,
\[
 \mathbf F_p[(\mathbf Z/q)^2]
    =\mathbf F_p[X,Y]/(X^q,Y^q),\qquad
                   N_{K_R}=X^{q-1}Y^{q-1}.                 \tag{14}
\]
This follows from
sum_(j=0)^(q−1)(1+X)^j=((1+X)^q−1)/X=X^(q−1).
Thus the norm is in exact augmentation degree D_m.

The specified roots in the preceding joint norm-root torsor
were repeated in the unused direction. Their cocycle is
exactly j_R of the single-point Kummer permutation cocycle,
not merely congruent to it after a different norm root.
The sum of the single-point root cocycle is delta_p(w_R).
Equations(13),(14) follow.

The norm element is invariant under automorphisms of K_R.
Its leading line remains invariant under the ray homothety;
translation acts trivially on associated graded. The
rho-twisted leading transfer in(13) is therefore zero by
the actual homothety argument, with w_R fixed in F_0.
More concretely(5) is the image of eta from(3), so applying
j_R already puts the class in I_joint^(D_m+1).
The original homothety acts on the entire grade D_m by
(−1)^(D_m)=+1, and by−1 on T_pi/p. Hence H⁰ of that
twisted grade over K_n is zero; its coefficient exact sequence
makes this lift unique. This also checks the canonical identification. ∎

The first candidate in this ORIGINAL CM branch is thus a degree
D_m+1 layer with the explicit active point moment(8), not the
old degree-one augmentation. Its coefficients still contain
E[p] tensor T_pi/p, with types Psi² and chi_cyc.
The canonical Weil contraction maps this tensor to mu_p;
it is an actual map to Kummer cohomology H¹(mu_p), not an
identification with H¹(T_pi).

Theorem4.1 makes this active first moment, its Weil contraction,
and EVERY fixed finite band of active point jets eventually
zero. For a fixed band the replication map multiplies by the
canonical norm element(14); no p^(2m) or point period is divided.
A claimed fixed-order comparison from this source to the old
nonzero integral w_0 at5 would fail at some finite p^k by(12).
This does not exclude a growing-order or differently normalized
arithmetic operation, or the original primitive-ray construction
whose norm multiplicity is one.

## 6. A rational norm-compatible alternative and its actual lattice

The rational normalization can be stated precisely. Before the
rho twist, the single-point Kummer classes give the ACTUAL system
\[
 \bar\kappa_m^R=p^{-2m}\delta_{\mathbf Q_p}(u_{R,m})
        \in H^1(M_m^R,\mathbf Q_p(1)).
\]
Its field norms are compatible by Proposition3.1.
Similarly the joint source has the norm-compatible rational
system p^(-4m)delta_Qp(u_(R,m)) over M_m.

These are rational multiples of actual unit Kummer extensions.
Their indicated coefficient lattices are respectively
p^(-2m)Z_p(1) and p^(-4m)Z_p(1), with unbounded denominators
in the fixed Tate line. They have not been proved to lie in
Q_p tensor an integral Iwasawa inverse limit. Rationalizing
a finite A_k module would give zero; it is not the operation
just defined in rational cohomology.

Both systems have the same norm to the ray field:
\[
 \operatorname{Cor}_{M_m^R/F_m}\bar\kappa_m^R
   =p^{-2m}\delta_{\mathbf Q_p}(w_R)
   =\operatorname{Cor}_{M_m/F_m}
                    (p^{-4m}\delta_{\mathbf Q_p}(u_{R,m})). \tag{15}
\]
Thus even this rational alternative retains a specific fixed-base
norm, not an unidentified primitive ray unit.

There is a further coefficient issue before using the original
rho. At finite level a genuine Kummer extension has endpoints
Q_p and Q_p(1). Tensoring it with the CM line rho gives an
extension of rho by T_pi, not of Q_p by T_pi.
The actual finite construction(5) uses the rho vector only where
it is trivialized modulo p^k, requiring m≥k.
An unbounded normalization p^(-2m) would require greater absolute
precision before reduction; it cannot be justified from that
finite trivialization by dividing a class modulo p^k.

It remains possible that a precisely constructed rational or
locally analytic coefficient object carries a suitable further
comparison. No such boundedness, character-evaluation or integral
descent theorem is claimed here. Applying the finite tame part of
rho AFTER the complete trace(15) already gives zero by the
homothety. Twisting the full character only after throwing away
the other ray direction is not the original Kato construction.

This is the authorized higher-augmentation alternative to a
formal derivative of a²−a^(2+s). No log_p(a) is divided.
The OLD smoothing unit(2) acts on its specified module; it
does not invert the zero isogeny-smoothing eigenvalue on
canonical point heights.

## 7. A nonzero actual higher relative class, with its boundary and branch

The previous cubical norm supplied fixed rational numbers L_5,L_7.
Keep EXACTLY those numbers and their Néron normalization; no
coefficient is chosen from a desired regulator value.
For a=5 or7 their displayed reduced ratios show
\[
                          v_a(L_a)=-12.                    \tag{16}
\]
The only new arithmetic check here is integer division of those
saved ratios: their numerator has a-valuation0 and denominator
a-valuation1 before the twelfth power. No psi value or old
certificate was recomputed.

Use the constant unit L_a on the actual joint division-torsor
algebra B_m over F_m and the SPECIFIED norm root
\[
                     r_{a,m,k}=L_a^{p^{4m-k}},\qquad k\le m.
\]
The equations v^(p^k)=L_a and Norm(v)=r_(a,m,k) define a
genuine torsor under the SAME norm-one torus p^k-module.
Denote its class by c_(a,m,k).

For transfer to K_n use the norm torus of the actual JOINT
division scheme over K_n; its base change to F_m is the torus
just used. Corestriction after twisting therefore retains that
global norm-kernel coefficient tensored with rho. It is not a
map that deletes the kernel and calls its target T_pi.

**[NEW deduction] Proposition7.1.** This class has exact order p^k
at EVERY prime in(1), with a chosen as in§1. Modulo p its
first nonzero coefficient layer is the top degree4(p^m−1):
\[
                      \delta_p(L_a)\,N_{H_m}.               \tag{17}
\]
Its complete rho-twisted transfer to the original ray branch
is nevertheless zero.

*Proof of nonvanishing and degree.* The smoothing prime a
is distinct from p and from2,3,13. The field F_m and the
joint point-division field M_m are unramified at a:
the ray modulus is prime to a, the elliptic curve has good
reduction there, and its p^m-division torsors extend finite
étale over the local integer ring since p is invertible.
Thus(16) remains valuation−12 in M_m. The Kummer class of
L_a there has exact order p^k, because p does not divide12.
The forgetful image of c_(a,m,k) is that class under finite
étale Shapiro, so the relative class also has exact order p^k.

Choose the same p-th root of L_a in every joint coordinate.
Its total product is exactly the specified root, since there
are p^(4m) coordinates. The cocycle is delta_p(L_a) times
N_(H_m). In the actual group algebra of H_m≃(Z/p^m)^4,
\[
                  N_{H_m}=\prod_{j=1}^4X_j^{p^m-1}.
\]
It is nonzero in exact degree4(p^m−1). Its scalar Kummer
class is nonzero by the valuation just proved, so(17) is
a nonzero class in that graded coefficient line. The same
local valuation proves its nonzero image in the full
relative cohomology.

The full norm element is fixed under all affine permutations
of the joint torsor. The Kummer class of L_a is defined over
Q. The ray homothety fixes that class and acts by−1 on rho.
Its unnormalized twisted corestriction therefore vanishes,
as in the earlier trace test. ∎

This example distinguishes the results: higher relative classes
are not all zero, and(17) is uniformly nonzero. However its
norm line is invariant, so its CM character is the wrong one
for the original transferred branch. It also has an explicit
nonzero tame boundary at the GOOD prime a: the residue is
−12 times the constant norm vector in the norm-kernel module.
No finite local condition has erased this residue. It is not
an ordinary Selmer class merely because its coefficient torus
and its global Kummer origin are genuine.

## 8. Exact scope and the first remaining arithmetic comparison

Theorem2.1 constructs a genuine cone class and(8) its explicit
corrected point moment. Theorem4.1 tests all fixed jets with a
full finite coefficient threshold, and Proposition5.1 locates
that class in an actually higher layer of the original joint
norm-root object. Proposition7.1 supplies an actual nonzero
higher comparison class and computes its local and CM-branch
failure. The rational norm system in§6 has its unbounded
lattice stated; it has not been promoted to an integral class.

No ordinary local Selmer conditions on the new tensor/permutation
coefficient modules have been inferred from the old conditions
on d_pi,d_barpi. The translated theta units have their fixed
S-unit boundary from the preceding proof, potentially at primes
beyond the original S={2,3,13,p}. Any new contraction or
regulator map must retain those local terms. The Weil map
in§5 has its true H¹(mu_(p^k)) target.

**[GAP CM-Derived-Unsmoothing].** Construct an arithmetic
comparison using the ORIGINAL primitive ray branch and retained
point extension data that avoids the proved fixed-jet loss, or
give the rational normalization in§6 a proved character evaluation
and adequate integral lattice. It must produce the actual
unsmoothed point determinant and its original unit coefficient,
not the zero isogeny-smoothing defect or the auxiliary class(17).

In particular it must still compare with the established
conditional identity
\[
 c_{2,p}=\varepsilon_p\,\#\operatorname{Sha}[p^\infty]\det B_p,
 \qquad
 \varepsilon_p=
 \frac{(-1)^b\iota_pu(0)}
      {\det U\det V\,(\det C)^2\det J},
\]
which identifies full Sha and the point space only AFTER c2,p≠0.
The required single rational frame must have local coefficient
c2,p/(2e_p det B_p), e_p=(1−alpha^(-1))², and real realization
(L''(E,1)/2)/(2Omega_E). Neither its rationality nor uniform
nonvanishing/index control is assumed. Bad/nonsplit primes and
the universal BSD objective remain open.

The new proofs use the actual Kato theta norm and finite étale
Kummer/Shapiro constructions already primary-source checked,
and the elementary coefficient calculations are included in full.
Only the new a-adic valuations of the saved rational cube numbers
were checked. No prime scan, old certificate rerun, extra agent
or shared/completed-proof edit occurred. The
[independent review](review-cm-derived-unsmoothing.md) passed all
eight sections, including the exact cone class, full finite-coefficient
jet threshold, higher layer, rational lattices, and separate higher
class with its retained local boundary and CM branch. The coordinator
also inspected the full proof/review and the new valuations.
