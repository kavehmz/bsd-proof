# Independent review of the ordinary K-theory lattice

Date: 2026-09-12. Reviewer: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Reviewed: [proof](k-theory-lattice-attack.md) and
[checkpoint](k-theory-lattice-checkpoint.md), together with the relevant
regular-model/Picard/Brauer inputs in the previously reviewed
[arithmetic-surface note](weil-etale-lattice-attack.md).

**PASS.** The proof establishes the full étale fundamental-group
vanishing, CH₀(X)=0, the ordinary K₀ ring, and the exact first-Chern
sequence with the stated scope. No substantive correction is required.
No old numerical certificate was rerun. The elementary three point
counts and the uniform choice of Frobenius were checked directly.

Reviewed SHA-256: proof
`8296aa626413a46821f07ca9850a5995ced16f3ca208f58aeb57bea68bbbec94`;
checkpoint
`74e0ba39f764d1121c631687154ba254d0cd6b3ede974f058930fcd70047b1a9`.

## 1. Proper homotopy and the full fundamental group

The exact morphism X→Spec Z is projective, flat and finitely presented.
The prior model calculation proves that every geometric fiber is
integral and reduced; the one singular fiber is a reduced nodal cubic.
Thus the hypotheses of
[Stacks, Proposition 58.15.2](https://stacks.math.columbia.edu/tag/0BUM)
hold literally. Smoothness of every fiber is not a hypothesis of that
proposition. Its geometric point may be the geometric generic point.

The theorem consequently gives
$$\pi_1(E_{\overline{\mathbb Q}})\longrightarrow\pi_1(X)
\longrightarrow\pi_1(\operatorname{Spec}\mathbb Z)\longrightarrow1.$$
The base group is trivial by Minkowski: a connected finite étale
cover of Spec Z would be the ring of integers of a number field
unramified at every finite prime. The exact formulation was read in
[Milne, Algebraic Number Theory, Theorem 4.9](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
It does not require an additional real-splitting assumption to exclude
such a field.

By Riemann existence, the geometric group of E in characteristic zero
is the profinite completion of the lattice of its complex torus. The
multiplication covers identify it Galois-equivariantly with
$\prod_\ell T_\ell E$. The comparison source was checked in
[Milne, Étale Cohomology, Theorem 3.4](https://www.jmilne.org/math/CourseNotes/LECc.pdf).
In particular this source group is abelian. Since it surjects onto
$\pi_1(X)$, the entire target is abelian; this argument precedes,
and is stronger than, merely computing its abelianization.

The integral zero section supplies the commutative diagram of generic
and integral fundamental groups. The subgroup $G_{\mathbb Q}$ supplied
by the generic section maps through $\pi_1(\operatorname{Spec}\mathbb Z)$
and hence maps trivially into $\pi_1(X)$. For $g\in G_{\mathbb Q}$ and
$t\in\prod T_\ell E$, conjugation therefore gives equal images for
$g(t)$ and $t$. The quotient map factors through continuous Galois
coinvariants. There is no assertion here that the generic arithmetic
fundamental group itself is trivial.

## 2. The all-prime coinvariant argument

The equation is $y^2+y=x^3+x^2-2x$. Counting y-solutions at q=2,3,5,
and adding the point at infinity, gives 5,6,9 respectively. For q=3
the affine counts are 2,2,1; for q=5 they are 2,2,0,2,2. All three
primes are good.

For each ℓ, the stated Frobenius choice makes $1-F_q$ an automorphism
of $T_\ell E$: its determinant is 5 for ℓ≠2,5, is 6 for ℓ=5, and
is 9 for ℓ=2. In each case q≠ℓ, so the unramified Tate-module
Frobenius and its determinant formula apply. This includes ℓ=389
and all other primes without an unspecified exception set.

The passage to the product is also valid. Embed $T_\ell E$ as the
single supported component of the full product. For any vector v
there, solve v=(1−F_q)w in that component. The corresponding global
Galois element gives exactly that difference in the product, with
every other component zero. Thus the closed difference subgroup
contains every single primary component. Their direct sum is dense
in the product, so its closure is the product. Continuous coinvariants
are therefore zero. This proves $\pi_1(X)=1$ as a full profinite group.

## 3. Arithmetic zero-cycles

The primary statement in
[Schmidt, math/0204330v1, introduction](https://arxiv.org/pdf/math/0204330)
was read directly. Its unramified class-field theorem identifies
ordinary CH₀ of a regular connected proper flat arithmetic scheme,
with projective generic fiber, with the modified abelian étale
fundamental group; both groups are finite. The modification imposes
splitting of real points. All those scheme hypotheses hold here.

Since the full fundamental group is already zero, its modified
abelian quotient is zero. The theorem therefore gives CH₀(X)=0.
The relative theorem and the empty-boundary convention are consistent
with this direct application, but are not needed to add hypotheses.
No finite-Brauer, finite-Sha, or leading-term conjecture occurs in
this class-field theorem.

One notation distinction is useful: Schmidt's SK₀ is a cokernel in
the zero-cycle complex, whereas the SK₀ in Weibel's discussion below
is the rank-and-determinant kernel. The proof uses the explicit map
between the cycle group and the latter kernel; it does not simply
identify differently defined symbols.

## 4. The map from CH₀ to ordinary SK₀

[Weibel, K-book II, Theorem 8.2 and Example 8.2.2](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.II.pdf)
give the Cartan comparison and show that the rank-and-determinant
kernel on a regular surface is generated by closed-point classes.
Here projectivity supplies an ample line bundle and the resolution
property, while regularity supplies bounded locally free resolutions;
thus K₀ of vector bundles equals G₀ of coherent sheaves in the precise
situation used. Rank and determinant are surjective by II.8.1.

The cycle map CH₀(X)→SK₀(X) does not require an extra Gersten
conjecture in mixed characteristic. There is also a direct proof of
the needed rational-equivalence compatibility. Normalize any integral
curve C in X; its normalization is finite because X is excellent.
On the resulting regular curve, write the divisor of f as D₊−D₋.
The line bundles O(−D₊) and O(−D₋) are isomorphic, so their two
effective-divisor exact sequences give
$$[\mathcal O_{D_+}]-[\mathcal O_{D_-}]=0\quad\text{in }G_0(\widetilde C).$$
Proper pushforward to X makes the associated residue-degree-weighted
sum of closed-point classes zero. This is exactly the rational
equivalence generated by div_C(f). Hence the point-class map factors
through CH₀ and is onto the stated SK₀. The same conclusion follows
from the terminal coniveau filtration in the author's proof; no
claim of degeneration of the entire spectral sequence is needed.

It follows that SK₀(X)=0. The reviewed Picard computation yields
$$K_0(X)\simeq\mathbb Z\oplus\operatorname{Pic}(X)
\simeq\mathbb Z^4.$$
The tensor-product determinant formula gives
$$(r,L)(s,M)=(rs,sL+rM).$$
Thus the rank-zero ideal is square zero, and the four displayed
classes in the proof form an integral basis. This is a ring statement
about ordinary K₀, not a vanishing statement for arithmetic intersections
or metrized line bundles.

## 5. The Chern sequence and its exact scope

Fppf Kummer theory applies for every n, including residue characteristics
dividing n. With c₁ defined through the determinant, the ordinary K₀
calculation and the reviewed Br(X)=Sha(E/Q) identification give
$$0\to\mathbb Z/n\to K_0(X)/n\xrightarrow{c_1}
H^2_{\mathrm{fppf}}(X,\mu_n)\to\operatorname{Sha}(E/\mathbb Q)[n]\to0.$$
The kernel is exactly the rank summand, because Pic(X)/n injects
by Kummer theory. The cokernel is the full n-torsion Sha group,
including the real-place information already treated in the model note.

A single nonzero m annihilating all these cokernels would annihilate
the whole torsion group Sha; it would then equal its finite m-torsion
subgroup, finite by descent. Thus the proposed uniform lifting target
has the claimed consequence. Computing the ordinary K₀ lattice does
not prove that uniform lifting, and does not imply that a twisted
K₀ class has unrestricted twisted rank. The subsequent Azumaya
argument must retain that separate obstruction.

Only this review file was written. No proof of full Sha finiteness,
of the complex leading coefficient, or of universal BSD is asserted.
