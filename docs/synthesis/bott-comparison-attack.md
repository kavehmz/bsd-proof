# A finite-coefficient Bott construction and its arithmetic division problem

Date: 2026-09-12. Owner: coordinator. The `[NEW]` deductions passed
[independent review](review-bott-comparison.md), including the actual
Quillen summand and the stated prime ranges. The objective remains full BSD over Q.

This note constructs genuine finite-coefficient motivic lifts of finite
Selmer classes using the proven motivic–étale comparison. It then computes
the missing division back to weight one. The result retains the whole
Sha[p^r] cokernel. A separate calculation determines the minimum rational
Tate weight of the required Bott trivialization and its failure to lift
primitively at fixed weight. No uniform annihilator is obtained.

## 1. The exact comparison input and the weight-one boundary

Write H_M^i(Y,Z/m(q)) for Nisnevich motivic cohomology of a smooth
scheme over a characteristic-zero field. We use products, pullbacks,
and finite-field-extension transfers with their usual compatibilities.

**[THEOREM, finite-coefficient comparison]** For q≥0, the cycle map
$$H_M^i(Y,\mathbb Z/m(q))\longrightarrow
H^i_{\rm et}(Y,\mu_m^{\otimes q})$$
is an isomorphism for i≤q and injective for i=q+1.
This is [Voevodsky, arXiv:0805.4430v2, Theorem 6.17(1)](https://arxiv.org/html/0805.4430v2),
with étale motivic coefficients identified with μ_m tensor powers;
see also his [earlier Z/2-coefficient paper, Theorem 6.1](https://numdam.org/item/10.1007/s10240-003-0010-6.pdf)
for that coefficient identification. The later full theorem applies to
every m invertible in the field, not just prime coefficients.

Let E/Q be an elliptic curve with zero section O. Weight one is
Z(1)=G_m[−1] on the Nisnevich site. On this regular curve, the
divisor resolution gives H²_Nis(E,G_m)=0. Consequently
$$H_M^2(E,\mathbb Z/m(1))=\operatorname{Pic}(E)/m.$$
Its cycle map is precisely Kummer c₁ and fits into
$$0\to\operatorname{Pic}(E)/m\to H^2_{\rm et}(E,\mu_m)
\to\operatorname{Br}(E)[m]\to0.\tag{1}$$
Degree two is just outside the comparison's isomorphism range in
weight one. It is inside that range in every weight at least two.

The motivic construction is connected to an actual Quillen K-theory
summand in §3.2 below. The filtration and Adams projector are specified;
no high K-group is silently identified with one motivic cohomology group.

## 2. A canonical rational Bott trivialization at every finite level

Fix an odd prime p, r≥1, and put
$$m=p^r,\qquad w=\varphi(p^r)=p^{r-1}(p-1),\qquad q=w+1.$$
Regard roots of unity as free rank-one Z/m-modules in the usual tensor
notation. If ζ is any primitive m-th root, then
$$b_{p,r}^{\rm et}=\zeta^{\otimes w}
\in H^0(\mathbb Q,\mu_m^{\otimes w})\tag{2}$$
is independent of ζ and is a basis of that rank-one coefficient module.

**[NEW] Proposition 2.1.** There is a unique class
$$b_{p,r}\in H_M^0(\mathbb Q,\mathbb Z/m(w))$$
with cycle class (2). Multiplication by its étale realization identifies
μ_m with μ_m tensor power q, over Q and every completion.

*Proof.* Another primitive root is aζ in additive module notation,
where a is a unit modulo m. Euler's theorem gives a^w=1 modulo m,
so its w-th tensor power is unchanged. The same calculation gives
Galois invariance. It is a basis because ζ is a basis. The degree-zero
comparison in §1 uniquely lifts this invariant coefficient section to
motivic cohomology. Products and restriction commute with the cycle map. □

For r=1 there is also a concrete transfer construction. On
L=Q(ζ_p), let τ_ζ∈H_M^0(L,Z/p(1)) be the root-of-unity class.
Then
$$b_{p,1}=-\operatorname{Cor}_{L/\mathbb Q}
                     (\tau_\zeta^{p-1}).\tag{3}$$
Indeed restriction of the right side is −(p−1)τ_ζ^(p−1), hence is
τ_ζ^(p−1) modulo p. The comparison in degree zero checks equality.
For r>1 this averaging argument cannot divide by the field degree,
which is divisible by p; Proposition 2.1 instead uses the actual
invariant section and the proven comparison.

## 3. The actual motivic Bott cokernel

Let
$$B_{p,r}=H_M^2(E,\mathbb Z/m(q)).$$
The comparison is an isomorphism here because 2≤q. Compose it with
the inverse coefficient isomorphism in Proposition 2.1 and denote the
result by
$$\theta_{p,r}:B_{p,r}\overset\sim\longrightarrow H^2_{\rm et}(E,\mu_m).$$

**[NEW] Proposition 3.1.** The following sequence is exact:
$$0\to\operatorname{Pic}(E)/m
\xrightarrow{b_{p,r}\,c_1}B_{p,r}
\xrightarrow{\theta_{p,r}}\operatorname{Br}(E)[m]\to0,\tag{4}$$
where the last arrow includes the Kummer quotient in (1).

*Proof.* The coefficient diagram formed by the two cycle maps and
multiplication by b commutes. Its right vertical map is an isomorphism
of coefficient sheaves, its upper high-weight cycle map is an
isomorphism, and its weight-one cycle image is Pic(E)/m. Thus
θ(bc₁(L))=c₁(L). Apply (1) to get exactness, including injectivity. □

For the curve 389a1, ordinary K₀(E)=Z⊕Pic(E)=Z⁴ by the curve
rank/determinant theorem and the full basis calculation. Its restriction
from the [integral arithmetic model](k-theory-lattice-attack.md) is an
isomorphism. Thus (4) is equivalently the actual sequence
$$0\to\mathbb Z/m\to K_0(E)/m
\xrightarrow{b_{p,r}\,c_1}B_{p,r}
\to\operatorname{Br}(E)[m]\to0.\tag{5}$$
Producing the higher-weight motivic class is automatic from the theorem;
dividing it by b inside weight-one motivic cohomology is exactly the
Brauer obstruction. Inverting the corresponding étale coefficient is
not that motivic division.

### 3.2. The actual Quillen K-theory summand

For this subsection assume p≥5. We use the motivic spectral sequence
$$E_2^{a,b}=H_M^{a-b}(Y,\mathbb Z/m(-b))
\Longrightarrow K_{-a-b}(Y;\mathbb Z/m),\tag{8}$$
its product, and its Adams action: ψ² acts by 2^j in weight j=−b.
These inputs are [Weibel, K-book VI, Theorem 4.2, Addendum 4.2.1
and §4.9](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf).
The coefficient modulus is odd, so the stated multiplicative structure
applies. Write A=ψ².

**[NEW] Proposition 3.2.** There is a canonical pure-Adams Bott class
$$\mathfrak b_{p,r}\in K_{2w}(\mathbb Q;\mathbb Z/m)$$
whose edge image is b_{p,r}^{et}, with A acting as 1. On the elliptic
curve the operator
$$e_2=-\tfrac12(A-1)(A-4)\tag{9}$$
is an idempotent on K_(2w)(E;Z/m), and its image is canonically
$$e_2 K_{2w}(E;\mathbb Z/m)
\simeq H_M^2(E,\mathbb Z/m(w+1))=B_{p,r}.$$
The map e₂(𝔟·−) on K₀(E)/m is exactly (5).

*Proof.* For Q, finite-coefficient étale cohomology vanishes above
degree two at odd p. For E it vanishes above degree four, by
Hochschild–Serre and the geometric curve's cohomological dimension two.
Motivic cohomology on a curve vanishes for i>j+1 by the higher-Chow
dimension bound; in the remaining range the comparison in §1 is an
isomorphism or injection. Hence its nonzero cohomological degrees in
(8) are between zero and four. For the field they are between zero
and two. Negative cohomological degrees vanish by the same comparison.

A d_s differential raises cohomological degree by 2s−1 and weight
by s−1. All s≥3 vanish for dimensional reasons. For s=2, commuting
with A shows that its image is killed by 2^j−2^(j+1)=−2^j, a unit
modulo m. Thus d₂ also vanishes. The spectral sequences degenerate.

On K_(2w)(Q;Z/m) the only graded pieces have weights w and w+1,
with cohomological degrees zero and two. Since 2^w=1 modulo m,
A acts on these pieces by 1 and 2. Their difference is a unit, so
the weight-one-eigenvalue summand maps isomorphically onto
H⁰(Q,μ_m^⊗w). The unique lift of its canonical generator is 𝔟.
It can be obtained from any edge lift by applying 2−A.

For E the only graded pieces of K_(2w) have weights w,w+1,w+2,
with cohomological degrees 0,2,4. Their eigenvalues are 1,2,4.
The product (A−1)(A−2)(A−4) is zero: successively applying its
commuting factors lowers the three-step filtration. All pairwise
differences are units because p≥5. Lagrange interpolation therefore
splits the filtration, and (9) is exactly its middle projector.
On that piece the cycle comparison is the stated isomorphism.

On K₀(E)/m, A acts by 1 on rank and by 2 on Pic/m. For the latter,
ψ²([L]−1)=[L²]−1=2([L]−1), since the rank ideal is square zero
on a regular curve. Multiplicativity and the product in (8) show
that e₂𝔟 kills the rank summand and sends L to bc₁(L). This proves
the final assertion. □

The ordinary, unprojected Bott map is also explicit. With the same
Adams splitting it is injective, and has cokernel
$$\operatorname{Br}(E)[m]\ \oplus\ \operatorname{Br}(\mathbb Q)[m].\tag{10}$$
Indeed its image is all the weight-w piece and the Pic/m subspace
of the middle piece. The weight-(w+2) piece is
H⁴_et(E,μ_m^⊗(w+2)); untwisting by b and using Hochschild–Serre
identifies it with H²(Q,μ_m)=Br(Q)[m]. These statements follow
directly from the three degenerate graded pieces just computed.

In particular a fixed scalar cannot annihilate the full raw Bott
cokernel for every p, even for a curve whose BSD is already proved:
Br(Q)[p] is nonzero for every p, by the Brauer invariant sequence
(take invariants 1/p and −1/p at two finite places). The zero section
injects this constant part into Br(E). The Selmer restriction in the
next section is essential; constant Brauer classes are not the BSD gap.

## 4. Retaining exactly the Selmer local conditions

Let A_m(F) denote the simultaneous kernel of geometric restriction and
evaluation at O in H²_et(E_F,μ_m). The
[reviewed Hochschild–Serre computation](hecke-brauer-annihilator-attack.md)
identifies it with H¹(F,E[m]), for Q and its completions. Its global
subgroup satisfying the local Kummer conditions is Sel_m(E/Q).

Define B_{p,r}^{Sel} as the inverse image under θ of that precise
subgroup. This definition is in the constructed motivic group B; it
retains normalization, geometric degree zero, and every local condition.

**[NEW] Corollary 4.1.** There are natural identifications and an exact
sequence
$$B_{p,r}^{Sel}\simeq\operatorname{Sel}_{p^r}(E/\mathbb Q),$$
$$0\to E(\mathbb Q)/p^r E(\mathbb Q)
\xrightarrow{b_{p,r}\,c_1}B_{p,r}^{Sel}
\to\operatorname{Sha}(E/\mathbb Q)[p^r]\to0.\tag{6}$$

*Proof.* Naturality makes θ compatible with localization. Under the
Hochschild–Serre identification, its specified inverse image has exactly
the defining Selmer conditions. Quotienting the global Kummer subgroup
gives Sha[p^r]. Products identify that Kummer subgroup with the indicated
motivic Bott image. □

This proves a finite-coefficient motivic realization for every finite
Selmer class. It does not claim that each class is the reduction of an
integral higher Chow class: the coefficient Bockstein can obstruct that
additional lift as well. Nor does it create a rational-point class
before the division in (6).

## 5. An explicit low-weight transfer test

At r=1 one can first pass to L=Q(ζ_p) and use the degree-one Bott
class τ_ζ. The weight-two comparison yields, for
z∈H²_et(E,μ_p), the class
$$u_\zeta(z)=\mathrm{cl}^{-1}
       (\zeta\cup\operatorname{res}_{L/\mathbb Q}z)
\in H_M^2(E_L,\mathbb Z/p(2)).$$
For a∈Gal(L/Q)=F_p^×, this class transforms by multiplication by a.
Consequently
$$\operatorname{Cor}_{L/\mathbb Q}(u_\zeta(z))=0.\tag{7}$$

*Proof.* The restriction of z is invariant and ζ transforms by a.
The sum of a over F_p^× is zero for odd p. Alternatively the
projection formula gives transfer equal to z times Tr(ζ), and
H⁰(Q,μ_p)=0. Compatibility of transfers with the injective weight-two
comparison proves (7) motivically. □

Thus ordinary transfer of this genuine low-weight lift kills the class.
Multiplying by τ_ζ^(p−2) before transfer returns to (3) and the higher
weight q=p, up to the explicitly invertible scalar p−1. It does not
give weight-one division. For Sel_p the p-prime-to-degree descent
along L/Q is valid, but the χ-eigencondition and its twist must remain;
discarding them is not rational descent of the desired point class.

## 6. The minimum weight and failure of primitive lifting

Here primitive means a generator of the free rank-one Z/p^r coefficient
module, equivalently an element not divisible by p.

**[NEW] Proposition 6.1.** A primitive element of
H⁰(Q,μ_{p^r}^{⊗t}) exists for a positive integer t if and only if
φ(p^r) divides t. In particular no fixed positive t works for all
primes, or for arbitrarily large r at one prime.

*Proof.* The cyclotomic Galois image over Q is the full cyclic group
(Z/p^r)^×, of order φ(p^r). A primitive vector is fixed exactly when
a^t=1 modulo p^r for every a in that group, equivalent to the stated
divisibility. The full cyclotomic image follows from irreducibility of
the cyclotomic polynomial; see [Milne, ANT, Theorem 6.4](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
The two final assertions follow since these orders are unbounded. □

**[NEW] Proposition 6.2.** At its weight w=φ(p^r), b_{p,r} does not
lift to a motivic class modulo p^(r+1) with the same primitive reduction.

*Proof.* A lift would give such an invariant coefficient lift under
the degree-zero comparison. But a Galois element with cyclotomic value
1+p acts on the coefficient by (1+p)^w. For odd p,
$$v_p((1+p)^{p^{r-1}(p-1)}-1)=r.$$
This follows by the binomial expansion at r=1 and successive p-th
powers. Multiplication by this difference does not annihilate a unit
modulo p^(r+1). Hence no primitive invariant lift exists. □

For p≥5, the actual Quillen class 𝔟_{p,r} likewise has no primitive lift in
the same degree modulo p^(r+1): its natural field edge map would
give the forbidden coefficient lift.

**[NEW] Corollary 6.3 (integral Bockstein retained).** The integral
coefficient Bockstein of b_{p,r} has exact order p^r in
H_M¹(Q,Z(w)). For p≥5, the corresponding K-theory Bockstein of 𝔟_{p,r}
has exact order p^r in K_(2w−1)(Q). In particular neither Bott
class is supplied by reducing an integral class in its even degree.

*Proof.* For any fixed positive w,
$$\varprojlim_s H_M^0(\mathbb Q,\mathbb Z/p^s(w))
=H^0(\mathbb Q,\mathbb Z_p(w))=0.$$
The first equality follows from the degree-zero comparison and the
definition of continuous invariants. The second follows because an
element with cyclotomic character 1+p acts nontrivially on this
torsion-free rank-one Z_p module. Reductions of an integral motivic
class form such a compatible family, so their image at every level
is zero. The coefficient exact sequence therefore makes the integral
Bockstein injective on H_M⁰(Q,Z/p^r(w)), proving the first assertion.

For Quillen K-theory, the natural field edge/e-invariant vanishes
on K_(2w)(Q)/m; this is Weibel VI.4.3 and Example 4.5(ii).
Its value on 𝔟 is the order-m generator b. If a nonzero multiple
of order less than m of the K-Bockstein vanished, that same multiple
of 𝔟 would lift integrally and have zero edge image, a contradiction.
The universal coefficient sequence gives the asserted exact order. □

For an integral line bundle L, compatibility of the connecting map
with products also gives
$$\delta(b_{p,r}c_1(L))=\delta(b_{p,r})\,c_1(L)
\in H_M^3(E,\mathbb Z(w+1)).$$
This formula does not assert that the product on the right is nonzero
for every L. It identifies the extra integral-lifting question rather
than suppressing the coefficient Bockstein.

Weight zero avoids this obstruction but supplies no positive-weight
shift into the comparison's isomorphism range. Over a fixed cyclotomic
extension one may make additional Tate choices; their arithmetic descent
and the weight changes above must still be justified.

## 7. The integral arithmetic fiber must also be retained

**[THEOREM, finite-field K-theory]** For a finite field F_q,
K₀(F_q)=Z, positive even K-groups vanish, and
K_(2j−1)(F_q)=Z/(q^j−1). Thus universal coefficients give
$$K_i(\mathbb F_p;\mathbb Z/p^r)=0\ (i>0),\qquad
K_0(\mathbb F_p;\mathbb Z/p^r)=\mathbb Z/p^r.$$
This is Quillen's finite-field computation, as recalled in
[Weibel, K-book IV, §1.13](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf),
also recalled at the start of VI §1.

If a positive-degree K-theory Bott element is extended from the arithmetic
base, its restriction to F_p is therefore zero. Localizing at it kills
the finite-field coefficient K-theory, although its degree-zero group
before localization is nonzero. This is a precise reason not to treat
a Bott-localized comparison as preserving the complete integral model
and its p-fiber conditions. It does not rule out a more selective
arithmetic lifting procedure for (6).

The familiar motivic weight finiteness argument also has a base-field
hypothesis: [Geisser, Hasse principles for étale motivic cohomology,
Proposition 4.5](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/hasse-principles-for-etale-motivic-cohomology/A110C67AE909A10FA22E066E7985D661)
assumes a global **function field**. His number-field statement in
Proposition 4.4 assumes Lichtenbaum's finite-generation conjecture.
Neither supplies an unconditional uniform bound here.

## 8. Exact remaining lifting statement

**[GAP Bott-389]** For E=389a1, construct one nonzero integer a,
independent of p,r, such that every class u∈B_{p,r}^{Sel} satisfies
$$a u\in b_{p,r}c_1(E(\mathbb Q)/p^r E(\mathbb Q))$$
for every odd prime p and every r≥1. With a=1 this gives vanishing
of every odd primary Sha group; with fixed a it gives a uniform
annihilator, and the already proved 2-primary result completes finiteness.

The construction of u, and the coefficient-level inverse of b, have
been proved. The uniform **motivic division** in this statement has
not. The minimum-weight and lifting calculations test this exact
method without claiming that all other integral comparisons are impossible.
The real leading coefficient and the universal BSD objective remain
additional requirements; finite coefficient classes alone do not provide
their rational framed analytic element.
