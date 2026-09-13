# Blending the CM theta Kummer extension with the two point motives

Date: 2026-09-12. Author `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Status: bounded construction completed; all ten sections passed
[independent review](review-cm-mixed-extension.md) and coordinator inspection.
The objective remains full BSD over Q. Actual mixed extensions are
constructed below. Their finite-coefficient difference recovers the
reviewed derivative, while the tested rational averaging and quadratic
period operations do not supply its rational determinant comparison.

## 1. Objects and coefficient conventions

Keep E:y²=x³+39x, K=Q(i), P₁=P=(3,12), P₂=Q=(27,144), and the
good split scope p≥5, p≡1 mod4, p outside S_E of the reviewed
[CM note](cm-regulator-tensor-attack.md). Every previous Néron, Betti,
unit, period and local-height normalization is retained. Write k=Q(i)
for the coefficient field, to distinguish it from a varying base
number field F containing K.

In the pure CM coefficient category, put
$$H=h_1(E)_k=A\oplus B,\qquad
A=M_\Psi,\quad B=M_{\Psi^c},\quad A\otimes B=k(1),\quad
R=B^\vee=A(-1).\tag{1}$$
Their weights are −1,−1,+1 respectively. The polarization fixes
the evaluation A⊗B→k(1); in a compatible basis the alternating
pairing on H is ⟨(a,b),(a',b')⟩=ab'−ba'. This convention will
fix the dual and cup signs, rather than leave a scalar unspecified.

The category used for geometric constructions is the rational
isogeny category of 1-motives with k-coefficients, together with
tensoring by the fixed invertible pure CM motives in (1). In particular
we will exhibit a 1-motive after tensoring the constructed object by B.
This does not require a conjectural category of all mixed motives.
Idempotents are used only on pure abelian pieces and through
pushout/pullback. A k-coefficient abelian factor is concretely obtained
from the projectors (1±i⊗i)/2 on E² up to isogeny; denominators can
be cleared before constructing the corresponding lattices and tori.
No CM action on a whole marked point 1-motive is assumed.

For each P_i let M(P_i)=[Z→E], with 1↦P_i. Push its extension
out along H→A to obtain
$$X_i:\quad0\to A\to X_i\to k\to0.\tag{2}$$
Take the actual dual of M(P_j), then pull it back along R=B∨→H∨:
$$Y_j:\quad0\to k\to Y_j\to R\to0.\tag{3}$$
These are operations on exact sequences, not projectors on their
marked middle objects. The correctly twisted theta Kummer motive
over each finite unit field is
$$K_R(u):\quad0\to A\to K_R(u)\to R\to0,
\qquad K_R(u)=M(u)\otimes R.\tag{4}$$
Here M(u) is the genuine G_m Kummer motive from the
[preceding construction](cm-motivic-derivative-attack.md).

**[THEOREM, constructions used]** The description of 1-motives by
a Poincaré biextension and a trivialization over the two marking
lattices is given in
[Bertolin, Biextensions of 1-motives by 1-motives, §1.2](https://arxiv.org/pdf/math/0402080).
In particular, choosing a lift of a marked abelian point into a
semiabelian extension is precisely choosing a point of the indicated
Poincaré fiber. Cartier duality exchanges the two marking maps.
For fixed adjacent extensions, the obstruction and torsor formalism
is [Bertrand, Extensions panachées autoduales, §1, Lemmas 1–2](https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/rpdf/Extpanaut_Nov10.pdf),
arXiv:1011.4685; Journal of K-Theory 11 (2013), 393–411.
Only that general formalism is used, not an unverified self-duality
or uniqueness hypothesis.

## 2. The first pullback is split in the relevant direction

**[NEW] Proposition 2.1.** The fiber product
$$F_j(u)=K_R(u)\times_RY_j\tag{5}$$
is an extension of Y_j by A, but its restriction to k⊂Y_j is
canonically A⊕k. Consequently it is not a blend of (2) and (3)
unless the lower extension (2) is split.

*Proof.* Both factors in (5) map to R. On k⊂Y_j the latter map
is zero. The fiber of K_R(u) over zero is its given subobject A.
Thus the restricted fiber product is A×k, with section t↦(0,t).
This uses the zero map k→R and is independent of u. ∎

Taking the fiber product of Y₁,Y₂ first gives the same result with
k² in place of k. It merely adjoins split lower point directions.
To construct the specified nontrivial adjacent extensions one must
solve their actual Yoneda problem.

## 3. Actual blends for all four point pairings

Write κ_A(P_i)=x_i and κ_B(P_j)=b_j for their realization classes.
The dual in (3) has class
$$y_j=-b_j\in H^1(F,B)=\operatorname{Ext}^1(R,k).\tag{6}$$
Indeed, the dual inverse-transpose of a point-extension matrix has
off-diagonal term −b_j(g)Ψ^c(g)⁻¹. Dividing by the quotient
character ρ=(Ψ^c)⁻¹ gives precisely −b_j. This fixes the sign
of the actual pulled-back dual.

A blend B_ij has graded pieces A,k,R and adjacent extensions
X_i,Y_j. Its obstruction is
$$[X_i]\circ[Y_j]\in\operatorname{Ext}^2(R,A).
\tag{7}$$
Although its tensor coefficient A⊗R∨ is k(1), we will not infer
vanishing in an arbitrary motivic Ext² from a comparison with Pic(F).
The following construction supplies actual geometric lifts.

**[NEW] Proposition 3.1.** All four pairs X_i,Y_j admit genuine
blended extensions over K with k-coefficients. After tensoring by B
these are 1-motives with weights −2,−1,0 and graded pieces
k(1),B,k. They can be assembled into one matrix blend with graded
pieces A²,k,R²; after tensoring by B its pieces are k(1)²,B,k².

*Proof.* Tensor the lower sequence (2) by B. It becomes an extension
of B by k(1). It is the Baer negative of the Cartier dual of X_i:
Cartier duality has the minus sign in its normalized cocycle, whereas
tensoring (2) by B retains +x_i. Similarly, Y_j⊗B is a point
extension of k by B with point class −b_j. Thus the two marking
maps of the required 1-motive are the negatives of the two projected
point maps. Both negatives are retained; they do not reverse the
eventual bilinear height.

Build the lower semiabelian object first as that Baer-negative
Cartier dual of X_i. It therefore already carries the required
k-action. For two lower directions take the fiber product of these
semiabelian objects over B. Its torus, including its coefficient
structure, is split over K. Its fiber over an upper marked point
has a K-rational lift: each split-torus coordinate is the nonzero
part of a one-dimensional K-vector space and has a nonzero vector.
After clearing a denominator of the marked point, this gives a
lift in G(K)⊗Q. Choose lifts for the two basis vectors of the
free upper k-lattice, then extend k-linearly using the already
constructed action on G(K)⊗Q. Clear the finitely many denominators
afterward to obtain an integral marking of an isogenous object.
This constructs the matrix coefficient 1-motive; tensor back by
R=B∨. Arbitrary fiber choices have not been claimed automatically
to confer a k-action on a completed marked object.

There is also a direct check of the projected obstruction, avoiding
any presumption that the pure CM projector lifts to a marked object.
Construct the ordinary Poincaré blends for the actual pairs
(P_i,P_j) and (P_i,iP_j), where
iP=(-3,12i), iQ=(-27,144i). They give nullhomotopies of their
Weil-paired Kummer cups. If
$$C(U,V)(g,h)=\langle\kappa(U)(g),g\kappa(V)(h)\rangle,$$
then, with [i] eigenvalues i and −i on A,B,
$$\tfrac12\bigl(C(P_i,P_j)+iC(P_i,iP_j)\bigr)(g,h)
=x_i(g)\,g b_j(h).\tag{8}$$
This is a cochain identity: the B⊗A term cancels directly. Thus a
linear combination of the two actual geometric nullhomotopies
annihilates the individual projected obstruction −x_i∪b_j in (7).
It uses two actual point motives and the fixed pure pairing. ∎

The choices just made are recorded, not claimed canonical. For fixed
adjacent extensions the full abstract blend set is a torsor under
Ext¹(R,A), by Bertrand's lemma. In the geometric Poincaré construction
the permitted changes of the four fiber trivializations form
$(F^\times\otimes_\mathbb Z k)^4$: each is an actual Kummer change.
We use this explicit subgroup/action and need no claim that every
extension in an unspecified larger category is Kummer.

For example a reference can be fixed by the rational generalized-
Jacobian markings and torus corrections in the reviewed
[CM relative construction, §§2–4](cm-biextension-cycle-attack.md).
Projected pairs involving iP or iQ use the corresponding algebraic
Poincaré pullbacks. Any necessary fiber vector is part of the
reference datum. Existence of such a reference does not assert that
theta units intrinsically select one.

## 4. Matrix cocycles and the exact action of theta units

For the chosen p-component write a(g)=Ψ(g), b(g)=Ψ^c(g), and
r(g)=ρ(g)=b(g)⁻¹; thus a(g)b(g)=χ(g). A matrix blend has action
$$G(g)=
\begin{pmatrix}
a(g)I_2&x(g)&r(g)Z(g)\\
0&1&r(g)y(g)\\
0&0&r(g)I_2
\end{pmatrix},\tag{9}$$
where x is the column (x₁,x₂), y is the row (y₁,y₂), and
Z is a two-by-two matrix with coefficient a/r=χ.

**[NEW] Proposition 4.1.** The representation condition in (9) is
equivalent to the adjacent cocycle identities and
$$dZ_{ij}(g,h)=-x_i(g)\,g y_j(h)
=x_i(g)\,g b_j(h).\tag{10}$$
Translation by K_R(u) in corner (i,j) changes Z_ij to
Z_ij+k_u, where k_u is the Kummer cocycle with coefficients Q_p(1).
The difference of two such blends is a degree-one extension of R
by A; an individual corner cochain Z_ij need not be a cocycle.

*Proof.* Multiply G(g)G(h). Dividing its upper-right block by
r(gh) gives
$$Z(gh)=Z(g)+\chi(g)Z(h)+x(g)b(g)y(h).$$
This is precisely dZ=−x∪y for the standard left-action differential.
The other blocks give dx=dy=0. If a closed cochain k_u is added
to a corner, (10) remains true. This is exactly the Baer translation
of the top-bottom extension, since the adjacent blocks are unchanged.
Conversely the difference of two solutions of (10) is closed.
Changing a central splitting changes this difference by a coboundary.
These are the matrix realizations of the blend torsor. ∎

Tensoring (9) by B multiplies the matrix by b(g), giving diagonal
characters χ,b,1 and central block Z without an additional character.
In particular the unit action becomes ordinary Kummer translation
between weights zero and minus two. No coefficient ρ is left in
the top-bottom difference after that twist.

## 5. Real and p-adic regulator blocks

First fix the secondary regulator of a reference, rather than
identifying an arbitrary torus lift with a canonical height.
For the full Q-point motive, the reviewed reference has exactly
$$H_v=I_v+\frac12\log_v
\begin{pmatrix}3/2&27/98\\27/98&243/2\end{pmatrix},
\qquad v=\infty,p,\tag{11}$$
where the logarithm is entrywise. The lattice frame is the specified
half of the doubled marking; the torus logarithm has positive sign.
At infinity use real parts and imaginary-period-normalized third-kind
forms. At p use the Coleman–Gross splitting with complement Q_p xω,
and log_p p=0. Thus det H_v=Reg_v with the full BSD height convention.
These are retained inputs, not recomputed certificates.

For clarity, the CM projection introduces a calculable half in the
GLOBAL pairing. Extend the global height to K and divide the usual
restriction/corestriction pairing by [K:Q]=2, so it restricts to H_v
on the rational points. Complex conjugation preserves this height
and fixes P_i but sends iP_j to −iP_j. Hence the normalized global
pairing h_v(P_i,iP_j) is zero. This is true for the cyclotomic
p-adic pairing as well: its global character and the canonical
ordinary local splittings are conjugation compatible. By (8), the
A⊗B component of this global bilinear height is
$$H_{v,\mathrm{glob}}^{AB}
=\tfrac12\bigl(h_v(P_i,P_j)+i h_v(P_i,iP_j)\bigr)
=\tfrac12 H_v.\tag{12}$$
The conjugate component gives the other half. Both negatives in
the marking maps of Proposition 3.1 cancel in this bilinear formula.
In particular det H_{v,glob}^{AB}=Reg_v/4. This statement includes
all places in the K-height; at p complex conjugation exchanges the
two places above p. It does not compute the secondary period of
a chosen reference blend at just one embedding of K.

Let C_v denote the actual LOCAL secondary block of the chosen
reference blend B₀⊗B, evaluated at that embedding with its specified
Poincaré lifts and local splittings. At infinity this means the
matrix formula (13) below with the coefficient real structure
retained; at p it means the corresponding Coleman–Gross splitting.
The rational half-frame is the chosen lattice frame in each case.
The equality C_v=H_v/2 has NOT been established here. In particular,
the rational Q-pair correction matrix in (11) does not supply the
additional finite and local normalization data for the pairs
(P_i,iP_j). Global conjugation invariance cannot replace those data.
No value of C_v or det C_v is inferred from (12).

The full period-matrix rule is fixed by
[Bloch–de Jong–Sertöz, arXiv:2206.01220v2, Definition 2.8, Theorem 2.9 and §5.4](https://arxiv.org/html/2206.01220v2),
J. London Math. Soc. 108 (2023), 340–361, DOI 10.1112/jlms.12747.
For the underlying rational real biextension write
$$P_{\mathcal B}=
\begin{pmatrix}b&P_H&0\\c&a&I\end{pmatrix}.
$$
Its matrix height is
$$-2\pi\left(\operatorname{Im}c-
\operatorname{Im}a
\begin{pmatrix}\operatorname{Im}P_H\\\operatorname{Re}P_H\end{pmatrix}^{-1}
\begin{pmatrix}\operatorname{Im}b\\\operatorname{Re}b\end{pmatrix}\right).
\tag{13}$$
Use the underlying rational structure when taking real/imaginary
parts; a single complex coefficient embedding alone is not that
real structure. Formula (13) applies to the marking matrices, not
only scalar biextensions.

**[NEW] Proposition 5.1 (exact regulator translation).** In the
fixed rational torus/lattice frames, changing a Poincaré lift by
the Kummer element u changes its normalized secondary period by
+log|u| at infinity and +log_p u at p. Consequently a matrix
translation J·[u], J∈M₂(Q), changes the actual local reference block
by
$$C_v\longmapsto C_v+J\ell_v(u).\tag{14}$$
Here the component functional is extended linearly to coefficient
objects, and ℓ_∞=log|·|, ℓ_p=log_p. For a field extension, (14)
is evaluated at each embedding over the chosen place. These are
local secondary periods with whatever reference corrections were
actually specified held fixed. They are not identified with the
global block (12).

*Proof.* A pure Kummer translation changes c in (13) by
log(u)/(2πi) in its designated corner, leaving a,b,P_H unchanged.
The resulting height change is
−2π Im(log(u)/(2πi))=log|u|, fixing the sign and 2π factor.
Equivalently it is integration of dz/z on the torus coordinate.
At p the same torus integration for the prescribed Coleman splitting
is log_p u. The abelian and holomorphic periods remain fixed, so
the splitting correction does not change. Additivity gives (14).
On an integer doubled marking, translation by u² gives this action
on the rational half-frame; the old factor 1/2 in (11) is not lost. ∎

For genuine global heights a change of rational Poincaré trivialization
also changes its finite-place contribution. The sum of all logarithmic
changes is zero by the product formula (or the global idèle character
for p-adic heights). One may not both add (14) and keep claiming the
result is the unchanged canonical global pairing. The fixed local
secondary functional is the one used in the next explicit test.

## 6. Rational norm descent of the actual blended unit system

The actual e_r(a) are global units in L_r=K(E[p^r]); this was
verified in the preceding construction. Fix a reference blend
B₀ over K. For a fixed corner matrix J construct, over L_r,
$$B_r=B_0|_{L_r}*(J\,[K_R(e_r(a))]),\tag{15}$$
using the blend-torsor action, with coefficients interpreted by
Baer operations. This is a genuine mixed object at every level.
With this specified reference, its transition to a lower unit field
is B₀ plus the corestriction of the difference from B₀. The actual
unit norm relation therefore makes these transitions compatible.
This reference-dependent norm transition is distinguished from the
reference-independent, degree-normalized averaging below.

**[NEW] Proposition 6.1 (the tested affine norm).** Rational affine
averaging of (15) back to K equals B₀. The unit translation is
zero after transfer, independently of r and J.

*Proof.* Tensoring by B identifies the translating extension with
the ordinary Kummer extension of e_r. Functoriality of its boundary
and norm, already proved for the actual units, gives
$$\operatorname{Cor}_{L_r/K}[K_R(e_r)]
=[K_R(N_{L_r/K}e_r)].\tag{16}$$
The norm is a unit of Z[i], hence lies in μ₄. Its rational Kummer
class is zero. Thus (16) is split, with no Sha hypothesis.

More precisely, if d=[L_r:K], the affine averaging of a blend B'
with the fixed adjacent extensions is defined relative to any
reference B₀ by
$$\operatorname{Av}(B')=B_0+rac1d
\operatorname{Cor}_{L_r/K}(B'-B_0|_{L_r}).\tag{17}$$
Here differences are extension classes in the translation group.
This is independent of the reference: replacing B₀ by B₀+e
subtracts res(e) in the parentheses, whose corestriction is de,
and the two changes cancel. It is therefore an actual operation
on this affine torsor, not an omitted degree factor. Apply (16)
to (15) to get Av(B_r)=B₀. ∎

This proof explains why the correctly twisted top-bottom extension
does not magically retain a character-weighted trace: its Ext
coefficient is A⊗R∨=k(1). A different character-weighted operation
would need a specified morphism with its own quotient and coefficient
types; it is not (16).

## 7. Determinant before trace: a stronger operation, computed

The preceding linear cancellation does not justify discarding the
determinant-before-trace possibility. Construct symmetric squares
and tensor products of the Kummer motives at the conjugate units,
and retain their rational coefficient frames. The symmetric-square
period has log(u)²/2. At infinity also take the conjugate period:
log|u|=(log(u)+overline{log(u)})/2, so its square uses the two
symmetric squares and their cross tensor, with the factor 1/4.
The imaginary branch changes cancel in this real expression.
Finite direct image and summing these framed expressions supply
the quadratic secondary regulator used below. This does not claim
that its framing is an invariant rational scalar or an ordinary
degree-one extension.

For F/K finite, d=[F:K], put
$$Q_{F,v}(u)=\frac1d\sum_{\sigma:F\hookrightarrow\overline K_v}
\ell_v(\sigma u)^2,\tag{18}$$
where embeddings extend one fixed embedding of K, with multiplicities.
Use log|·| at infinity and log_p in C_p at p. For the actual global
units whose norm to K is torsion, the corresponding mean of ℓ_v
is zero. This fixes exactly which period is being traced.

**[NEW] Proposition 7.1.** For the actual local reference block C_v,
the determinant-before-trace satisfies
$$\frac4d\sum_\sigma
\det\bigl(C_v+J\ell_v(\sigma u)\bigr)
=4\det C_v+4\det(J)Q_{F,v}(u)
\quad\text{if }N_{F/K}u\text{ is torsion}.\tag{19}$$
The quadratic term need not vanish merely because the linear mean
vanishes. It scales quadratically under u↦u^n.

*Proof.* For any two-by-two matrices C,J and scalar t,
$$4\det(C+tJ)
=4\det C+4t\operatorname{tr}(\operatorname{adj}(C)J)
 +4t^2\det J.$$
Average this identity. The linear term is zero by the norm hypothesis,
giving (19). Also ℓ_v(u^n)=nℓ_v(u), proving the scaling statement.
The factor four is an explicit rescaling; dividing the formula by
four gives the unscaled identity. It specializes to Reg_v if
C_v=H_v/2 is separately proved; no such identification of the
local baseline is claimed here. ∎

This proves an actual surviving secondary period. It does not
identify log(unit)² with the cyclotomic-character moment
M_p=∫log_p(χ_cyc)²dμ_ψ. The arguments of the two logarithms differ.
There is also a concrete norm-law problem for the proposed repair.

**[NEW] Proposition 7.2 (exact tower recurrence).** Let F'/F have
degree e and put w=N_{F'/F}u. For each embedding τ of F, let
μ_τ=e⁻¹Σ_{σ|τ}ℓ_v(σu). Then
$$Q_{F',v}(u)=e^{-2}Q_{F,v}(w)
 +\frac1{[F:K]}\sum_\tau\frac1e
 \sum_{\sigma|\tau}\bigl(\ell_v(\sigma u)-\mu_\tau\bigr)^2.
\tag{20}$$
Thus the actual unit norm relation does not by itself give norm
compatibility of the quadratic period. The extra term is explicit.

*Proof.* In each group of e embeddings, expand
ℓ_v(σu)=μ_τ+(ℓ_v(σu)−μ_τ). The mixed sum is zero and
eμ_τ=ℓ_v(τw). Averaging the pure squares proves (20), over R
or C_p alike. No positivity assertion at p is used. ∎

There is a second exact test. The finite derived-unit operation is
linear in Kummer extension classes, whereas the nonconstant term
in (19) satisfies D(u²)=4D(u). If it were the same additive
operation on all powers of the actual input, additivity would also
give D(u²)=2D(u), forcing D(u)=0. Thus (19) alone is not the
required natural linear operation whenever its quadratic term is
nonzero. This is a test of that formula, not a claim that the fixed
elliptic curve violates BSD or that an accidental equality at a
single chosen input is impossible.

Polarizing gives the genuine period
d⁻¹Σℓ_v(σu)ℓ_v(σv), linear in u for fixed v. Taking v to be the
torsion coordinate ζ_{p^r} gives zero at both real and p-adic places.
A non-torsion auxiliary v or another renormalization is an additional
arithmetic choice; no identity with M_p or the exact derivative has
been proved by making that choice.

## 8. What the mixed difference really gives at finite coefficients

The mixed construction does give the earlier derivative through a
precise operation that survives the norm issue: take a difference
before inserting the finite coefficient vector.

For this finite comparison choose J=E_ij in (15), the elementary
matrix with coefficient ONE in corner (i,j). The corresponding
difference is then exactly K_R(e_r); a general J_ij would scale
the input and every ensuing class by that coefficient.
Use the canonical integral unit-Kummer model of this difference,
tensored with the already fixed integral CM coefficient lattice.
We do not reduce an arbitrary rational blend modulo p^m. At r≥m,
that coefficient lattice modulo p^m is trivialized by the same
finite vector t_ρ,m in the division field. Pullback of this
**difference extension** along 1↦t_ρ,m gives
$$\delta_{p^m}(e_r)\otimes t_{\rho,m}
\in H^1(L_r,T_{\mathfrak p}E/p^m).\tag{21}$$
Changing the reference blend and translating its unit partner by
the same change leaves (21) unchanged. This explains both its
canonicity and why the point data cancels from the difference.
There is no invariant rational vector in R at a finite number
field; the pullback in (21) is an integral finite-coefficient step.

Apply the saved exact corestriction and Shapiro maps, use the same
Betti vector γ_CM=2pr_ρ(γ_E⁺), and divide by the same Kato factor
$$12\bigl(a^2-\Psi^c((a))\overline\sigma_a\bigr).\tag{22}$$
For n≥m and r≥max(m,n+1), send γ to 1+T in
(Z/p^m)[T]/T². The resulting class is precisely the class Z_m
in the reviewed finite construction. If its cocycle is A(g)+TD(g)
and A(g)=gv−v, its unique derivative is therefore
$$d_m(g)=D(g)+c_\gamma(g)gv,\qquad
c_\gamma(g)=\frac{\log_p\chi_{\rm cyc}(g)}{g_p},
\quad g_p=\log_p(1+p).\tag{23}$$
This is equality of the actual input classes, not a new formula
inferred merely from similar periods. The plus correction, the
factor twelve, smoothing sign and rational Betti factor two are
unchanged. The proof and H⁰-based uniqueness are in
[Proposition 6.1 of the reviewed note](cm-motivic-derivative-attack.md#6-positive-construction-the-derivative-from-finite-kummer-data).
In particular lim_m d_m=w₀ without a Sha-finiteness premise.

When Reg_p≠0 the same exact final frame operation is
$$\mathcal B_p^{-1}\left(
\frac{p}{2\#E(\mathbb F_p)}\operatorname{pr}_W
\bigl((\varprojlim_m d_m)\otimes T\bigr)\right)
=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}\Xi,
\tag{24}$$
where e_p=(1−α⁻¹)² and c_cmp,p=(156iΩ_p)⁻¹. The inverse is
only on the indicated one-dimensional image, and the projection
retains possible extra Selmer classes in its kernel. At a degenerate
point regulator use only the previously proved undivided identity.
No scalar in (24) is replaced by an unspecified unit.

## 9. The first remaining mixed-extension comparison

The actual construction has achieved three separate things: a
geometric blend of the correctly weighted point extensions; an
exact finite unit translation of that blend; and recovery of d_m
from its coefficient-one integral difference by (21)–(23). The rational affine norm of the
translated blend was computed and loses that translation. The
determinant-before-trace repair was also computed and retains a
quadratic period, with the extra variance term (20) and the wrong
additive degree for the tested linear comparison. Neither test is
a general impossibility theorem about higher mixed extensions.

**[GAP CM-Mixed-Derived].** Construct, from the actual norm-compatible
blends (15), their fixed rational point frames, and specified
arithmetic maps, one element $Z_{\rm alg}\in\mathscr L_{P,Q}$ over Q such
that its localization equals (24) for every good split prime in
the stated scope with Reg_p≠0, with compatible undivided identity
at the other such primes, and
$$R_\infty(Z_{\rm alg})=\frac{L''(E,1)/2}{2\Omega_E}.\tag{25}$$
The construction must explain how a rational secondary comparison
retains the difference in (21) without replacing its finite vector
by a nonexistent rational invariant, and must justify any use of
the quadratic/polarized periods in §7. If Z_alg=qΞ then (25)
proves q=n_E∈Q. That rationality is a required conclusion.

No such map or rational element has yet been constructed. In
particular the existence of blends, their torsor of trivializations,
and the exact local derivative do not prove full Sha finiteness,
Selmer corank two or the complex leading-term formula. Universal
BSD remains the unchanged goal.

## 10. Source and verification record

Primary new sources read were Bertolin math/0402080 §1.2;
Bertrand's November2010 author version of 1011.4685, §1 Lemmas1–2
and the tensor-Ext identification on pp.8–9; and
Bloch–de Jong–Sertöz 2206.01220v2 §§2,4,5.4. The marked-CM
construction is supplied geometrically above, rather than by
assuming a fully faithful Ext² comparison for general motives.
All new calculations are symbolic. No prior numerical certificate
was rerun and no additional agent was created. The
[independent PASS review](review-cm-mixed-extension.md) verifies all
ten corrected sections, including the local/global distinction and
the integral difference model. Subsequent status/link edits are editorial.
