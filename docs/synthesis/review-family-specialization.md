# Independent review of family specialization

Date: 2026-09-12. Reviewer: `/root/higher_period_integrality`,
GPT-6 Astra, xhigh reasoning. Review commissioned by the coordinator.

## Verdict

**PASS after the two requested corrections.** The revised Lemma 1 uses
global affinoid coordinates, and §6 now explicitly assumes the exact
Bockstein descent relation (8b), retaining the Iwasawa main-conjecture
hypothesis if BKS (7.3.2) is its source. Both changes were inspected after
the author saved them. No BSD conclusion is being accepted from the
family argument.

Reviewed source SHA-256:
`2d2de479adee091b18dd47cd53224d4ef90d19a49e5e401855a12a9afaa0f4e7`.

Read the complete [family-specialization attack](family-specialization-attack.md).
The specific comparison-space and strict-criticality questions were checked
directly in the cited [BKS published PDF](https://kurihara.math.keio.ac.jp/bks4.pdf)
and [Fouquet published PDF](https://www.numdam.org/item/10.5802/jep.38.pdf).
Other primary-source searches were not repeated.

## 1. Lemma 1: equality of full determinant sections

**[NEW, independent verification]** Let A be the affinoid algebra of X.
Reduced irreducibility makes A a domain. The invertible sheaf corresponds
to a projective rank-one A-module M. Embed M as a direct summand of A^d.
The meromorphic difference sigma-tau lies in M tensor_A Frac(A). Choose
one nonzero a in A clearing its finitely many coordinates. Then
a(sigma-tau) is an element of M whose image in A^d has regular coordinate
functions.

On the dense set of agreement, outside the proper zero locus of a and
the possible pole loci, those functions vanish. That intersection remains
Zariski dense: in an irreducible space a dense set meets every nonempty
Zariski open, also after intersecting with a fixed nonempty open. Hence
all the coordinate functions vanish, which proves equality.

This global argument avoids assuming that the original dense set remains
dense in every rigid analytic affinoid subdomain. The local sentence in
the first draft needed that repair; the lemma's statement does not need
an additional hypothesis.

Equality of germs gives equality modulo every power of the maximal ideal,
and hence equality of the initial forms. For a perfect complex, take a
bounded projective representative. Its determinant is an alternating
tensor product of top exterior powers and commutes with base change.
This is a statement about the determinant line of the complex, not the
flatness of its individual cohomology modules.

Thus full, exact sections in a common line do specialize through rank
jumps. The lemma neither creates a second section from unrelated fiber
values nor identifies its period at the special point.

## 2. Lemma 2: special directions and determinant orientation

**[NEW, independent verification]** Over R_0=L[[U]], each Smith block
with nonzero diagonal U^e has injective differential. Its first
cohomology is zero, and its second is R_0/(U^e), or zero when e=0.
At U=0, a block with e>0 becomes a zero differential and contributes
one dimension in each degree. Zero rows and columns give the stated
free ranks. This reconstructs all four formulas in (3).

The long cohomology sequence of the triangle C --U--> C --> C tensor^L L
gives

$$
0\longrightarrow H^1(C)/UH^1(C)
\longrightarrow H^1(C\otimes^L L)
\longrightarrow H^2(C)[U]\longrightarrow0.
$$

On a positive Smith block the connecting map sends its special kernel
generator to a nonzero multiple of U^(e-1) in R_0/(U^e). Therefore that
special direction cannot lift to a family cycle. The note correctly
identifies it as a Tor/base-change contribution rather than an additional
generic family class.

The determinant orientation is explicit and correct. For source basis v
and target basis w with Dv=U^e w, the inverse alternating line used in the
note is det(source) tensor det(target)^(-1). Its acyclic trivialization
sends v tensor w^(-1) to U^e. The usual alternating determinant would
have the inverse scalar; the note has deliberately chosen the former.
Restoring the specified change-of-basis determinants is necessary for an
exact formula and is retained.

## 3. Lemma 3 and the topology/chain-rule tests

**[NEW, independent verification]** The conormal map records exactly
the T-coefficient F_1(U,A), so its kernel is T^2 B[[T]]. Every derivative
in U or A still only accesses that same coefficient function. Under odd
symmetry, the residual ambiguity is exactly T^3 B[[T^2]]. In
characteristic zero the logarithmic coordinate log(1+T) is an invertible
formal change with linear coefficient one and makes inversion odd, as
used in the note.

For k_n=2+(p-1)p^n the odd-prime lifting-the-exponent calculation gives
v_p((1+p)^(k_n-2)-1)=n+1. The same positive rational integers diverge
in the real topology. This suffices to reject an automatic complex limit
inferred from this p-adic weight limit.

The chain-rule formula (7) follows from the commuting differential
operator partial_w+(1/2)partial_s. It includes all mixed derivatives with
the stated binomial coefficients. No fixed-motive derivative can be
extracted by discarding those terms without a further identity.

## 4. Proposition 4: all relevant data can agree while c varies

**[NEW, independent verification]** Direct expansion gives

$$
\det\begin{pmatrix}cT&U&0\\-U&T&0\\0&0&T\end{pmatrix}
=(cT^2+U^2)T.
$$

The transpose identity D_c(U,T)^t=-D_c(U,-T) is exact. At T=0 and
generic U, the upper 2-by-2 block is invertible and both first and second
cohomology are represented by e_3. Over L[[U]] the two other cokernel
summands are killed by U, matching Lemma 2. At U=T=0 all three directions
appear in each cohomological degree.

The first T-connecting map on generic cohomology sends e_3 to e_3; its
height is therefore one in the stated dual bases. Thus the class Ue_3
has self-height U^2, precisely the first normal coefficient of the
determinant, independently of c.

The tangent matrix J has J_12=1 and all J_13,J_23 zero. Its Pfaffian
cofactor vector in the specified convention is e_3, agreeing exactly with
the leading U-coefficient of the class. Nevertheless the pure normal
third coefficient is c, and the special normal pairing is diag(c,1,1).
Its determinant also equals c.

The example therefore does what is claimed: the displayed rank-one
height and tangent Pfaffian data do not determine the special pure
normal coefficient, even inside a perfect complex with fixed bases.
It does not satisfy equality of the **full** sections F_c for different
c, so there is no conflict with Lemma 1. The note explicitly refrains
from claiming an elliptic-curve realization. A full special normal height
matrix would recover c, which is also stated.

## 5. Proposition 5: strict criticality really fails under (8)

**[THEOREM, exact source check]** In the BKS published paper, Hypothesis
2.2 and equations (2.2.1)–(2.2.2), printed p. 866, give
H^1(Z_S,V)=E(Q) tensor Q_p, localization inside H_f^1(Q_p,V), and the
exact sequence from the one-dimensional E_1(Q_p)^* into
(E(Q) tensor Q_p)^*, with quotient H^2(Z_S,V). The dimensions are r
and r-1, respectively.

**[NEW, independent deduction]** The local dual exponential annihilates
the finite local condition. Thus the global dual exponential on this
H^1 is zero and cannot be an isomorphism to the one-dimensional filtered
de Rham target. In addition, H^2 is nonzero for r>=2.

Fouquet's exact definition in §2.1.1, printed p. 50, requires both the
global dual exponential to be an isomorphism and global étale cohomology
to vanish outside degree one. Hence the two failures in Proposition 5
are justified under (8). This does not contradict Fouquet's arithmetic
fundamental-line specialization theorem: that theorem is distinct from
applicability of the strict-critical period formula at the special point.

## 6. Comparison-space types and the remaining descent premise

The BKS period-regulator map is an isomorphism between Cp-lines:

$$
\lambda:\mathbb C_p\otimes\bigwedge^r H^1(Z_S,V)
\xrightarrow{\sim}
\mathbb C_p\otimes
\left(H_1(E(\mathbb C),\mathbb Q)^{+,*}
\otimes\bigwedge^{r-1}H^2(Z_S,V)\right).
$$

This is the map displayed on BKS p. 866. It uses the fixed abstract
embedding of R into Cp for the height and real period factors; it is
not a continuous real-to-p-adic specialization. The family note retains
the x and Betti factors, so its equation (9) is well-typed after the
assumed determinant and exterior-power identifications.

BKS Proposition 4.14, printed p. 882, is precisely the vector comparison
(8a). The source's nonzero Bockstein-regulator criterion implies
injectivity because the source exterior power is a line. Thus equality
of its Bockstein images implies equality of the two exterior elements
when that regulator is nonzero.

However, the arithmetic element must actually satisfy

$$
\operatorname{Boc}_{\infty,x}(\eta_x^{\rm Kato})=\kappa_\infty. \tag{R1}
$$

BKS equation (7.3.2) gives (R1); the published §7.3 is under Hypothesis
2.2 and Conjecture 7.1. An attempted family proof may instead make the
existence of its normalized determinant element and the exact relation
(R1) explicit compatibility premises. It must not silently obtain them
from the first conormal Gross–Zagier identity. The revised note adds
this premise explicitly as (8b) and invokes it in both directions.
The stated implications between (9) and (8a) are consequently valid in
the claimed nondegenerate vector case.

## 7. Completion and scope

No computation certificates needed rerunning: all checks were algebraic
or targeted primary-source type checks. The only review file edited is
this file. The revised auxiliary-twist paragraph is also explicitly
conditional on having chosen a rank-one twist with the required local
conditions; its product leading-coefficient identity is then elementary.
No unresolved mathematical issue with Lemmas 1–3, Proposition 4, or
Proposition 5 remains in the reviewed version.

Equality of full determinant sections and equality of first normal jets
must remain distinct in future applications. The former preserves every
jet under specialization; the latter leaves the precise kernel displayed
in Lemma 3. The matrix model is an algebraic test of that distinction,
not an elliptic-curve example. The arithmetic specialization and complex
period comparison are still explicitly unproved.

Coordinator metadata note: after this review, only the source note’s review-status introduction was updated to link this PASS. The displayed source hash records the reviewed version before that header-only edit; the mathematical proof body was unchanged.
