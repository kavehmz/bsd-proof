# Independent review of the finite-coefficient Bott construction

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. Own only this review file. The coordinator owns
`bott-comparison-attack.md`; no root proof is edited here.

**PASS for all sections of [the construction](bott-comparison-attack.md),
including Proposition 3.2 on genuine Quillen $K$-theory.** The final
version explicitly restricts the later Quillen nonlifting and Bockstein
claims to $p\ge5$, matching their definition in §3.2. Motivic claims
retain the stated scope of all odd primes. This scope clarification was
checked directly in the saved file; no remaining correction is required.

Reviewed complete-file SHA256:
`b5f1425427f5545e210714f85d046cb45feebaf12ecbcd0869db3b533a2a6fe0`.
Subsequent review-link or checkpoint changes are editorial.

## 1. Finite coefficients and the weight-one cokernel

Voevodsky's Theorem 6.17(1) has the stated comparison range for arbitrary
finite modulus, not just a prime. Applying it to the pointed scheme
$E_+$ and using invertibility of $m$ in characteristic zero gives the
needed étale coefficients. This does not give an isomorphism in degree
two at weight one; that distinction is correctly retained.
Source: [arXiv:0805.4430v2, Theorem 6.17](https://arxiv.org/html/0805.4430v2).

The divisor resolution of $\mathbb G_m$ on a regular curve computes
its Nisnevich cohomology in degrees zero and one, with no higher group.
Together with $\mathbb Z(1)=\mathbb G_m[-1]$, the coefficient sequence
therefore gives $H_M^2(E,\mathbb Z/m(1))=\operatorname{Pic}(E)/m$.
The cycle map is Kummer $c_1$, whose cokernel is exactly
$\operatorname{Br}(E)[m]$.

For $w=\varphi(p^r)$, replacement of a primitive root $\zeta$ by
$a\zeta$ multiplies its tensor power by $a^w=1$ modulo $p^r$.
Thus the tensor is independent of its generator and is Galois invariant.
It is a basis, so its inverse is an isomorphism of coefficient sheaves,
not a motivic division operation. The degree-zero comparison uniquely
lifts it to $b_{p,r}$, including for $r>1$ when the cyclotomic transfer
degree is divisible by $p$.

The coefficient/cycle diagram proves (4) exactly. Multiplication by
$b_{p,r}$ carries $c_1(L)$ to its high-weight product, and untwisting
its cycle returns the same Kummer class. Hence injectivity and the
full Brauer cokernel both follow from the original Kummer sequence.
For 389a1, the previously reviewed rank/determinant description of
$K_0(E)$ turns it into (5), with precisely the rank summand as kernel.

## 2. The actual spectral sequence and Adams summand

The cited Weibel inputs supply the spectral sequence for smooth schemes,
its finite-coefficient product for odd modulus, the pairing with integral
$K$-theory, and Adams action on the rows. The proof uses the finite
coefficient spectral sequence itself, not only a rational Adams
decomposition. See [K-book VI, Theorem 4.2, Addendum 4.2.1, §4.9](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.VI.pdf).
The smooth characteristic-zero field and curve here satisfy the hypotheses.

Here is the full degeneration check. Higher-Chow dimension bounds give
$H_M^i(Y,\mathbb Z/m(j))=0$ for $i>j+\dim Y$. In the remaining
range on a curve, the cycle map is an isomorphism or injection into
étale cohomology. The latter vanishes for $i>4$ by the geometric-curve
bound and $\operatorname{cd}_p(\mathbb Q)=2$. On the field the bound
is $i>2$. Negative cohomological degrees vanish under the comparison,
and negative weights have no cycle terms.

A $d_s$ changes cohomological degree by $2s-1$ and weight by $s-1$.
All $s\ge3$ differentials therefore have zero source or target. For
$s=2$, commuting with $A=\psi^2$ annihilates the differential's image
by $2^j-2^{j+1}=-2^j$, which is a unit modulo the odd modulus.
This also kills all possible incoming $d_2$ maps. Hence the actual
spectral sequences degenerate, with finite filtrations on each relevant
total degree; no unknown extension is erased at this step.

On total degree $2w$, the field has weights $w,w+1$, corresponding
to cohomological degrees $0,2$. Their $A$ eigenvalues are $1,2$.
The two-step filtration implies $(A-1)(A-2)=0$. Therefore $2-A$
is an actual idempotent and its image maps isomorphically onto the
weight-$w$ quotient. This proves existence and uniqueness of the Bott
lift with the stated edge generator. Pullback to $E$ preserves it.

For $E$, the three pieces have weights $w,w+1,w+2$ and eigenvalues
$1,2,4$. Applying the matching commuting factors in filtration order
proves $(A-1)(A-2)(A-4)=0$ on the entire group. For $p\ge5$, their
pairwise differences are units; polynomial Chinese remaindering gives
a splitting of the actual group, not merely of its associated graded.
In particular
$$e_2=\frac{(A-1)(A-4)}{(2-1)(2-4)}
     =-\tfrac12(A-1)(A-4)$$
is idempotent, and its image maps canonically to the middle graded
piece $H_M^2(E,\mathbb Z/m(w+1))$. This is the claimed genuine
Quillen summand.

On $K_0(E)/m$, $A$ is one on rank and two on the Picard ideal.
Indeed $([L]-1)^2=0$ on this regular curve implies
$[L^2]-1=2([L]-1)$. The product spectral sequence identifies the
middle edge of $\mathfrak b([L]-1)$ with $b c_1(L)$. Since
$\mathfrak b$ is an $A=1$ eigenvector, its product with rank stays
in that eigenpiece, and its product with the Picard ideal stays in
$A=2$. There is no unaccounted weight-$w+2$ product term. This
verifies the final assertion of Proposition 3.2 on actual $K$-classes.

## 3. Raw cokernel and Selmer restriction

The unprojected Bott map has full image in the weight-$w$ piece and
the injective $b\operatorname{Pic}/m$ image in weight $w+1$. There
is no image in weight $w+2$. The last piece is
$$H^4_{\rm et}(E,\mu_m^{\otimes(w+2)}).$$
In its Hochschild–Serre spectral sequence, total degree four has only
$(a,b)=(2,2)$. The geometric trace identifies the inner module with
$\mu_m^{\otimes(w+1)}$. There is no differential to or from this
term, so untwisting by $b$ identifies the group with
$H^2(\mathbb Q,\mu_m)=\operatorname{Br}(\mathbb Q)[m]$.
The actual Adams splitting therefore gives the direct sum in (10).
This accounts for two distinct places where constants can occur;
$\operatorname{Br}(E)[m]$ itself already contains its zero-section
split copy of the base Brauer group.

Prescribing local invariants $1/p$ and $-1/p$ at two finite primes
proves that the extra base Brauer term is nonzero for every odd $p$.
Thus it cannot be treated as a BSD obstruction or annihilated uniformly
by a fixed nonzero integer as $p$ varies.

The previously reviewed normalized Hochschild–Serre identification
uses both geometric degree zero and evaluation at the zero section.
With those conditions, it gives $H^1(F,E[m])$. The high-weight cycle
isomorphism and coefficient untwisting commute with every localization.
Hence the inverse image specified in §4 is exactly the full Selmer
group, not a weakened collection of local conditions. Quotienting its
global Kummer subgroup gives exactly $\operatorname{Sha}[p^r]$.

## 4. Transfers, minimum weight and primitive lifting

For the low-weight cyclotomic test, Galois acts on the root factor by
$a\in\mathbb F_p^\times$ while it fixes the restricted class $z$.
The sum of these eigenvalues is zero. Restriction is injective on the
corestriction target because the extension degree $p-1$ is invertible
modulo $p$, or one may apply the coefficient projection formula and
the injective weight-two cycle map. Thus (7) is valid motivically.
The root class to power $p-1$ instead has invariant character, giving
the negative transfer in (3) with its correct sign.

For odd $p$, the cyclotomic image is the entire cyclic group
$(\mathbb Z/p^r)^\times$. A primitive vector at weight $t$ is
invariant precisely when every unit satisfies $a^t=1$, equivalent
to $\varphi(p^r)\mid t$. At $w=\varphi(p^r)$, elementary lifting
of the binomial identity gives
$$v_p((1+p)^w-1)=r.$$
Thus no unit modulo $p^{r+1}$ can be invariant at this same weight.
The coefficient reduction maps are compatible with the cycle and
field edge maps, proving both motivic and Quillen fixed-degree
nonlifting claims in their stated prime ranges.

## 5. Exact integral Bockstein orders

For a fixed $w>0$, degree-zero comparison identifies the inverse
system with the cyclotomic invariant modules. The inverse limit is
$H^0(\mathbb Q,\mathbb Z_p(w))=0$: multiplication by
$(1+p)^w-1\ne0$ is injective on the torsion-free rank-one module.
Every integral motivic class has compatible reductions, so its image
at each finite level is zero. The coefficient sequence therefore makes
the motivic Bockstein injective on the entire finite degree-zero
group. The element $b_{p,r}$ has order $p^r$, so its Bockstein does too.

For clarity, the Quillen assertion can also be proved directly by
restricting to $\overline{\mathbb Q}$. Its positive even integral
$K$-groups are uniquely divisible, so their reductions modulo $m$
vanish. The finite-coefficient edge map there is an isomorphism with
the root-of-unity tensor. Naturality shows that the field edge map
over $\mathbb Q$ is zero on every integral reduction. These are
the e-invariant facts cited in Weibel VI.4.3 and Example 4.5(ii).

If $a\,\delta_K(\mathfrak b)=0$, the universal coefficient sequence
makes $a\mathfrak b$ an integral reduction. Its edge must then vanish,
so $a b=0$. Since $b$ has order $m$, $m\mid a$. The coefficient
sequence also kills $\delta_K(\mathfrak b)$ by $m$, proving exact
order $m$. This is an order argument on a genuine $K$-theory class;
it does not identify all integral $K$-theory with motivic cohomology.
Compatibility of the motivic connecting map with multiplication by
an integral $c_1(L)$ gives the final displayed Bockstein product.
Its nonvanishing for arbitrary $L$ is correctly left unasserted.

## 6. Arithmetic fiber and source hypotheses

Quillen's finite-field calculation gives positive odd groups of order
$p^j-1$ and zero positive even groups for $\mathbb F_p$.
These orders are prime to $p$, so universal coefficients give zero
in every positive degree modulo $p^r$, while degree zero remains
$\mathbb Z/p^r$. See [Weibel IV, Corollary 1.13](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.IV.pdf).
Consequently any positive-degree Bott class extended from the
arithmetic base restricts to zero there. Inverting that zero action
kills the whole coefficient module, including its nonzero degree-zero
term. The conditional formulation does not assume such an extension
already exists, nor that localization preserves the original model.

The Geisser source scope is accurate: Proposition 4.5 assumes a global
function field, and Proposition 4.4 obtains the number-field conclusion
under Lichtenbaum's conjecture. See
[Hasse principles for étale motivic cohomology, §4](https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/hasse-principles-for-etale-motivic-cohomology/A110C67AE909A10FA22E066E7985D661).
No unconditional number-field finite-generation conclusion is imported.

The final missing division criterion is exactly a uniform annihilator
of the Selmer quotient $\operatorname{Sha}[p^r]$. The constructed
Bott classes, the canonical projected $K$-summand and the coefficient
isomorphism prove none of that annihilator, the complex leading-term
comparison, or full BSD. No old computation was rerun.
