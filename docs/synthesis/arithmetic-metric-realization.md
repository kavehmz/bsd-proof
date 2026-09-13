# The actual arithmetic Chow class of the decorated Mellin current

Date: 2026-09-12. Owner: coordinator. New deductions passed
[independent review](review-arithmetic-metric.md). The objective remains full BSD over Q.

This note constructs the decorated Mellin current as an arithmetic Chow
class on the actual regular model. It also computes that entire Chow
group and the relevant product. The construction retains arbitrary real
metric data; an additional map into the fixed rational determinant line
is still required for BSD.

## 1. The model and the primary definitions

Let X be the regular projective flat arithmetic surface

$$Y^2Z+YZ^2=X^3+X^2Z-2XZ^2$$

with generic elliptic curve E=389a1. Its zero section is O. The
[reviewed ordinary K-theory calculation](k-theory-lattice-attack.md)
proves CH₀(X)=CH²(X)=0. Its proof uses the actual étale fundamental
group and arithmetic class field theory, without finite Sha. We use
that established result; it is not a statement that Pic(E) vanishes.

Write S=Spec Z and f:X→S. The complex fiber E(C) is a compact connected
curve, and f has smooth generic fiber, as required for arithmetic
pushforward.

**[THEOREM, arithmetic Chow inputs]** In
[Gillet–Soulé, *Arithmetic intersection theory*, PMIHES 72 (1990), 93–174](https://www.numdam.org/article/PMIHES_1990__72__93_0.pdf),
DOI 10.1007/BF02699132, use the Green-current quotient in §§1.2.1–1.2.3,
Definitions 3.2.1 and 3.3.3–3.3.4,
the exact sequence in Theorem 3.3.5(i), pushforward Theorem 3.6.1(ii),
and the degree normalization in §3.4.3. In particular

$$\widetilde A^{1,1}(X_{\mathbb R})
 \xrightarrow{a}\widehat{\mathrm{CH}}^2(X)
 \longrightarrow\mathrm{CH}^2(X)\longrightarrow0,\tag{1.1}$$

where a sends a form to the class (0,form). Real (1,1) forms satisfy
c*η=−η for complex conjugation c and are taken modulo im∂+imbar∂.
The same Green-current quotient gives their current representatives.
Arithmetic degree is deg∘f*, with

$$\widehat{\deg}\,a(\eta)=\frac12\int_{E(\mathbb C)}\eta.
\tag{1.2}$$

No integer-valued claim is built into the word arithmetic degree.

## 2. Computation of the entire top arithmetic Chow group

Choose the invariant probability form

$$\mu_E=\frac{i}{2\omega_1b}\,\omega\wedge\overline\omega,
\qquad\int_{E(\mathbb C)}\mu_E=1,$$

using the rectangular periods ω₁>0, ib with b>0. It satisfies
c*μ_E=−μ_E.

**[NEW] Lemma 2.1.** Integration identifies

$$\widetilde A^{1,1}(X_{\mathbb R})\simeq\mathbb R.$$

*Proof.* An exact ∂ or bar∂ term has integral zero on the compact
curve. Conversely, for a real (1,1) form η with zero integral, the
scalar Poisson equation gives a smooth real function h with η=dd^c h.
This lies in im∂+imbar∂. The function can be chosen invariant under
c: averaging with its conjugate preserves the equation, since both
dd^c and a real (1,1) form acquire the appropriate minus sign under
antiholomorphic pullback. Finally λμ_E realizes every integral λ. ∎

**[NEW] Proposition 2.2.** There is an isomorphism of abelian groups

$$\boxed{\widehat{\deg}:\widehat{\mathrm{CH}}^2(X)
 \overset\sim\longrightarrow\mathbb R,\qquad
 q\longmapsto a(2q\mu_E)\text{ for its inverse}.}\tag{2.1}$$

It holds before tensoring with Q and hence also after tensoring with Q.

*Proof.* CH²(X)=0 makes a in (1.1) surjective. Under Lemma 2.1,
its composition with arithmetic degree is λ↦λ/2 by (1.2), which
is injective. Thus a is injective as well. This proves (2.1), including
its factor two. The additive group R is uniquely divisible, so tensoring
this isomorphism with Q leaves R. ∎

In particular this arithmetic group is not finitely generated over Z
or Q. Its classes can be represented by zero algebraic cycles together
with metric currents. Forgetting that metric part kills the whole group
on this model. Choosing harmonic representatives does not remove the
continuous parameter: λμ_E is already harmonic.

**[NEW] Corollary 2.3.** For every j≥3,

$$\widehat{\mathrm{CH}}^j(X)=0.$$

*Proof.* There are no algebraic cycles of codimension j>dim X=2.
The prospective Green current has type (j−1,j−1), which is zero
on a complex curve when j≥3. Thus even the group of arithmetic
cycles in that codimension is zero. ∎

The rational arithmetic intersection ring therefore has no positive
codimension above two. This dimension statement does not make its
top arithmetic degrees rational.

## 3. The decorated current is an actual class in this group

Keep the [reviewed Mellin trace current](mellin-trace-comparison.md)

$$\mathcal T=\pi_*(A_2F d\mu),\qquad
F=y^2f(z)\overline{g(z)},$$

where π:X₀(389)→E has degree 40 and A₂ is the fixed second Laurent
coefficient of the infinity Eisenstein series. Its mass is the proved
real number

$$M=\int_E\mathcal T
=-\frac{9\cdot389}{\pi^4\cdot390}\,\ell_E L(f,2)\ne0.
\tag{3.1}$$

**[NEW] Proposition 3.1.** The current defines a genuine arithmetic
Chow class

$$\mathfrak t=[(0,2\operatorname{Re}\mathcal T)]
 \in\widehat{\mathrm{CH}}^2(X),\qquad
\widehat{\deg}(\mathfrak t)=M.\tag{3.2}$$

It is exactly a(2Mμ_E) in this group.

*Proof.* Let α=π*ω=c_π2πifdz and l=log|v|, with c_π the retained
nonzero rational differential factor. The previous proof gives

$$Fd\mu=-\frac{i}{4\pi^2c_\pi}d(l\alpha).$$

Since π, ω and v are defined over R, complex conjugation sends α
to barα and fixes l. It therefore sends Fdμ to −conjugate(Fdμ).
The cusp Eisenstein family is fixed by the real involution; this
follows either by reindexing its defining sum under z↦−bar z or
from its real cosine Fourier expansion. Its fixed Laurent coefficient
A₂ is consequently invariant. Hence c*T=−bar T, so 2Re T is
a real (1,1) current with the required sign.

On a complex curve dd^c of a (1,1) current is identically zero by
degree. The zero codimension-two algebraic cycle has no complex
support. Thus (0,2Re T) satisfies the original Green-current equation
with zero smooth curvature. No new theory of singular arithmetic
metrics is required for this top-degree current. Its current quotient
has a smooth representative: the mean-zero part differs from zero by
dd^c of a distribution, obtained by the compact Green operator.
Equivalently its class is 2Mμ_E by the current version of Lemma 2.1.
The local integrability and the absence of extra cusp atoms were
already proved in the trace construction.

Formula (1.2) gives degree M, and (2.1) identifies the class with
a(2Mμ_E). This proves every assertion in (3.2). ∎

The derivative term in the trace formula has not been deleted. It
contributes exactly the nonzero mass M. Passage to top arithmetic
Chow theory records that mass and forgets the rest of the current
modulo exact terms. It does not furnish a new arithmetic equation for M.

## 4. An equivalent explicit hermitian line construction

The elementary example that an arbitrary constant metric gives an
arbitrary real arithmetic degree was already recorded in the
[arithmetic Green note](arithmetic-green-comparison.md). Here it gives
an exact representative of the newly computed class on X.

For q∈R, let L_q be the free line Z on S with norm ||1||=exp(−q).
Its arithmetic first Chern class is a(2q). Choose any smooth invariant
hermitian metric on the algebraic line H=O_X(O). Its complex curvature
has integral one. The arithmetic product formula gives

$$f^*\widehat c_1(\overline L_q)\,
 \widehat c_1(\overline H)
=a(2q\,c_1(\overline H))=a(2q\mu_E).\tag{4.1}$$

The last equality follows from Lemma 2.1, or from (2.1) and degree q.
The first is the standard product of a metric class with a Chern class;
it also follows directly from the star-product definition with first
algebraic divisor zero and constant Green function 2q. In particular
(4.1) at q=M is exactly the class t in (3.2).

Every algebraic object used in (4.1) is defined integrally over Z.
Its metric, however, has the real parameter q. This construction works
for every q, without a denominator bound or a rationality condition.
It explicitly explains why realizing T as an arithmetic Chow class,
even before rationalizing its cycle coefficients, does not put its
degree in Q or in the fixed BSD period–regulator lattice.

## 5. The regulator determinant is a different operation

Let H_ij be the already realized full BSD height matrix for P,Q.
One may represent each entry by the actual class

$$\lambda_{ij}=a(2H_{ij}\mu_E)
 \in\widehat{\mathrm{CH}}^2(X).$$

Equivalently take the negative of the corresponding arithmetic
intersection of the reviewed point divisors and their Green functions,
whose finite corrections have been fixed. Its degree is H_ij, so
Proposition 2.2 makes it the same class.

**[NEW] Proposition 5.1.** The literal cup-product determinant is zero:

$$\lambda_{11}\lambda_{22}-\lambda_{12}\lambda_{21}=0
 \quad\text{in }\widehat{\mathrm{CH}}^4(X)_{\mathbb Q}.\tag{5.1}$$

But the determinant of their degrees is strictly positive:

$$\det(\widehat{\deg}\lambda_{ij})=\det H
=\operatorname{Reg}_{\rm BSD}(E)>0.\tag{5.2}$$

*Proof.* Equation (5.1) is Corollary 2.3. Equation (5.2) is the
previously certified positive regulator of the full independent
Mordell–Weil basis. No certificate is rerun for this deduction. ∎

Thus the specified secondary determinant in the relative 1-motive
construction cannot be replaced by an ordinary cup determinant of
these top arithmetic Chow classes. This is a statement about an
explicit attempted operation, not a prohibition on secondary products
or higher arithmetic constructions.

## 6. Exact remaining arithmetic requirement

The construction (3.2) completes one natural meaning of “an arithmetic
realization of the decorated current”. It does not complete GAP MT-389:
that gap also requires a map defined over the specified rational
motivic data to the fixed point-determinant tensor the L(f,2) regulator
line, with the exact real realization. It is that map and its rational
structure which would imply the desired BSD rationality.

The distinction is now explicit on the actual model. An arithmetic
Chow class with Q-cycle coefficients can contain any real metric
parameter; on this model its top group is precisely R. An arbitrary
map defined by its real degree is not a rational motivic comparison.
The existing finite-dimensional framed point motives retain that
additional structure and cannot be replaced by (3.2) alone.

**[GAP AM-389].** Construct a rational motivic lift and comparison
for t, preserving the complete decorated trace and the fixed finite
point and regulator frames, whose real regulator is M and whose
division by the specified L(f,2) factor is an operation on those
rational realizations. The rationality of the BSD quotient must follow
from the construction; it is not a condition silently imposed on
the metric parameter in (4.1).

No uniform Sha bound, full leading-term formula or BSD counterexample
is obtained from this arithmetic metric construction.
