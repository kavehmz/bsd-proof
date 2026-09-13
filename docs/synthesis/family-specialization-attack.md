# Family specialization and the fixed-motive leading term

Date: 2026-09-12. This continues the
[derived-comparison attack](derived-comparison-attack.md), rather than
repeating its valuation-only interpolation counterexamples. The target
is full BSD over $\mathbb Q$; no proof or counterexample to that conjecture
is obtained here. The new algebraic deductions below are elementary and
passed the [independent review](review-family-specialization.md) after two
explicit hypothesis/proof repairs.

The attempt establishes two precise limits on an otherwise valid
continuation argument. Exact identities of sections of a determinant line
do specialize through a rank jump. However, some new special-fiber Selmer
directions need not lift to family cohomology, and the universal
Gross–Zagier identity controls only a first cyclotomic conormal derivative.
Its weight and anticyclotomic derivatives do not determine the higher pure
cyclotomic derivative. Even supplying that derivative would still require
the fixed-motive complex period comparison stated in §6.

## 1. Primary theorem and correction actually checked

The primary source is Daniel Disegni, *The universal $p$-adic Gross–Zagier
formula*, [arXiv:2001.00045](https://arxiv.org/abs/2001.00045), read in the
[86-page author PDF](https://disegni-daniel.perso.math.cnrs.fr/univ.pdf).
Theorem D is on p. 14, Conjecture Pf on p. 66, and the correction is
Appendix B on p. 82. Page numbers here are the printed PDF page numbers.

**[THEOREM, Disegni Theorem D, with Appendix B]** On a locally
distinguished Hida-star family $\mathscr X$, there is an exact identity
$$
\frac{h_{\mathscr V/\mathscr V^\sharp}
 (\mathscr P(f_1),\mathscr P^\iota(f_2))}
 {((f_3,f_4))}
=d^\sharp\mathscr L_p(\mathscr V^\sharp)\,
 \mathscr Q\!\left(\frac{f_1\otimes f_2}{f_3\otimes f_4}\right).
\tag{1}
$$
It is an equality of functionals valued in the cyclotomic conormal
module, over the function field of the family; all constructions exist
on an open set containing its classical points. Theorem C constructs
and interpolates the universal Heegner class. Neither statement has a
Sha-finiteness hypothesis.

**Correction retained.** At a $p$-adic place nonsplit in the auxiliary
CM extension, Appendix B imposes inertness and an unramified Hecke
character; $p$-adic ramification in the extension is excluded. Theorem D
therefore applies to the corresponding Hida-star families. For the
rational elliptic-curve test below, choose $p$ split in the auxiliary
imaginary quadratic field, making these extra conditions vacuous.

**Normalizations retained.** In (1), $\mathscr Q$ is the specified product
of local toric pairings from §§1.2.6 and 4.4; the toric measure has global
volume one. The global pairing is fixed by Poincaré duality and the
factor involving the dimension of the algebraic representation and the
degree of the Hodge bundle in §1.2.7 and (4.1.7). The interpolation of
$\mathscr L_p$ is the exact formula of Theorem 1.4.1, including its
$e_{p\infty}$ factors. We retain these quantities, rather than replacing
them by unspecified pointwise units or identifying the source's
automorphic normalization with a Néron period without comparison.

**[CONJECTURE, Disegni Conjecture Pf]** At a classical point $z$, let
$\widetilde r=\dim\widetilde H_f^1(K,V_z)$. The source conjectures
vanishing of the universal class to order at least
$\lfloor\widetilde r/2\rfloor$ and a leading term given by a Pfaffian
regulator for the tangent height pairing. Its initial formulation is
modulo the coefficient field's multiplicative group. Remark 7.3.3
separately discusses the integral normalization needed to improve that
ambiguity. This leading-class assertion is not a conclusion of
Theorem D. Its discussion of some higher-rank comparisons also expressly
assumes primary Sha finiteness.

## 2. Variables and the precise local form of the candidate

Fix an ordinary weight-two point associated to $E/\mathbb Q$, and an
auxiliary imaginary quadratic field $K$ satisfying the local toric
conditions, with $p$ split in $K$. Work on a smooth local chart, or on
a chosen smooth slice after pullback. This smooth-chart choice is a
hypothesis for the following local calculation, not a claim that every
Hida branch is étale over weight space.

Use a coefficient field $L/\mathbb Q_p$ and completed local rings
$$
B=L[[U,A]],\qquad R=B[[T]],\qquad J=(T).
$$
Here $U$ is a weight-direction parameter, $A$ an anticyclotomic
parameter, and $T$ the normal cyclotomic parameter. More tangent
variables can be included without changing the arguments. If a slice
has fewer dimensions, omit the unused variables. A ramified weight
map does not permit replacing a uniformizer $U$ by $k-2$ without
tracking its ramification.
No global product decomposition of the eigenvarieties is assumed.

The self-dual locus is $T=0$. In the locally distinguished sign-minus
case, $\mathscr L_p$ vanishes on that locus. After fixing test vectors
in (1) with nonzero denominator and nonzero toric factor at the point,
put
$$
\mathscr E(U,A)=((f_3,f_4))\,
\mathscr Q\!\left(\frac{f_1\otimes f_2}{f_3\otimes f_4}\right).
$$
It is then a specific invertible local function. Identify $J/J^2$ with
$B\cdot T$ by the chosen cyclotomic generator. Equation (1) becomes
$$
[T]\mathscr L_p(U,A,T)
=\mathscr E(U,A)^{-1}
 h_{\mathscr V/\mathscr V^\sharp}
 (\mathscr P(f_1),\mathscr P^\iota(f_2)).
\tag{2}
$$
This is the verified candidate family identity. There is no unproved
complex continuity step in (2); it is already a $p$-adic theorem.

The normal derivative $T$, a derivative in $U$ or $A$, and a derivative
in the complex variable $s$ of the fixed function $L(E,s)$ are different
operations. The following lemmas keep those distinctions explicit.

## 3. What exact continuation through a determinant line does prove

**[NEW, exact specialization lemma] Lemma 1.** Let $X$ be a reduced
irreducible affinoid space over $L$, let $\mathscr D$ be an invertible
sheaf, and let $\sigma,\tau$ be meromorphic sections. Suppose their
values agree on a Zariski-dense set of points where both are regular.
Then $\sigma=\tau$. If both are regular at $x\in X$, their images in
$$
\mathscr D_x\otimes_{\mathcal O_{X,x}}
 \mathcal O_{X,x}/\mathfrak m_x^{n+1}
$$
agree for every $n\ge0$. In particular their orders and their nonzero
initial forms in
$\mathscr D(x)\otimes\mathfrak m_x^n/\mathfrak m_x^{n+1}$ agree.

The conclusion applies to
$$
\mathscr D=\det\mathscr C
$$
for a perfect complex $\mathscr C$, even if its cohomology dimensions
jump at $x$. It does not require cohomological flatness.

*Proof.* Write $X=\operatorname{Sp}(A)$ and let $P$ be the invertible
$A$-module corresponding to $\mathscr D$. Since $A$ is a domain,
the meromorphic sections lie in $P\otimes_A\operatorname{Frac}(A)$.
Choose a single nonzero $a\in A$ clearing their denominators, so
$v=a(\sigma-\tau)\in P$. Embed the finite projective module $P$
as a direct summand of $A^n$. Every coordinate of $v$ vanishes on
the given globally Zariski-dense set, and hence is zero in $A$.
Therefore $v=0$, and inverting $a$ gives $\sigma=\tau$.
This argument does not assume that global Zariski density restricts
to every affinoid subdomain. Equality of
their germs implies equality modulo every power of the maximal ideal.
The least nonzero graded image is consequently the same. For a bounded
complex of finite projective modules, its determinant is the alternating
tensor product of their top exterior powers. Exterior powers commute
with base change, including derived specialization computed from that
projective complex. This proves the determinant assertion independently
of the dimensions of its cohomology. $\square$

This gives a valid continuation step stronger than equality of ideals:
if exact, coherently normalized determinant sections exist and agree
at dense points, the special section and every jet are fixed exactly.
Rank jumping alone does not obstruct this conclusion. It does not
construct the second section from fiberwise complex numbers.

**[NEW, rank-jump base-change lemma] Lemma 2.** Let
$R_0=L[[U]]$ and let
$C=[R_0^a\xrightarrow{D}R_0^b]$ be in degrees one and two. Suppose
$D$ has generic rank $q$. Over this discrete valuation ring choose
Smith bases with nonzero diagonal entries
$U^{e_1},\ldots,U^{e_q}$, $e_i\ge0$, absorbing the explicitly recorded
units into the basis changes. Let $k$ be the number of positive $e_i$.
Then
$$
\begin{aligned}
H^1(C)&\simeq R_0^{a-q},\\
H^2(C)&\simeq R_0^{b-q}\oplus
             \bigoplus_{e_i>0}R_0/(U^{e_i}),\\
\dim_L H^1(C\otimes^L L)&=a-q+k,\\
\dim_L H^2(C\otimes^L L)&=b-q+k.
\end{aligned}
\tag{3}
$$
There is a natural exact sequence
$$
0\to H^1(C)/UH^1(C)\to H^1(C\otimes^L L)
\to H^2(C)[U]\to0.
\tag{4}
$$
On each positive-exponent Smith block, the new kernel direction
does not lift to an element of $H^1(C)$.

*Proof.* A nonzero diagonal block is the complex
$[R_0\xrightarrow{U^{e_i}}R_0]$. It has zero first cohomology and
second cohomology $R_0/(U^{e_i})$ if $e_i>0$, and is acyclic if
$e_i=0$. The remaining zero blocks give the displayed free parts.
At $U=0$, each positive block has zero differential and contributes
one dimension in both degrees. This proves (3). The exact triangle
$C\xrightarrow{U}C\to C\otimes^L L$ gives (4). On a positive block,
a constant basis vector reduces to a special-fiber cycle, but no
nonzero vector is a cycle over $R_0$, since $U^{e_i}$ is not a zero
divisor. $\square$

**Determinant content.** With the displayed Smith bases and compatible
determinant orientations, use the line
$\Delta_C=\det(R_0^a)\otimes\det(R_0^b)^{-1}$, the inverse alternating
determinant for the chosen placement in degrees one and two.
The acyclic trivialization on the generic
fiber of a positive block sends the determinant basis to $U^{e_i}$.
The product of these contributions is $U^{\sum e_i}$. To express it in
the original bases, retain the determinants of the basis changes;
they are specific units, not disposable constants in an exact formula.
Thus this lemma also tracks higher-order rank jumps when some $e_i>1$,
beyond a nondegenerate first-Bockstein calculation.

For a concrete rank-one example, take
$$
C=[R_0^r\xrightarrow{\operatorname{diag}(U,\ldots,U,0)}R_0^r].
\tag{5}
$$
Its generic kernel has rank one, but its special kernel has dimension
$r$. Every family cohomology section lies in the final coordinate;
ordinary derivatives of these sections still give only that direction.
The other $r-1$ special directions enter through (4). A proposed
construction of $r$ independent special classes by differentiating a
generic rank-one class therefore does not follow from perfectness,
base change, or exact family interpolation alone.

This is a calculation about perfect complexes. It is not an assertion
that (5) is a Selmer complex of an elliptic curve, or a counterexample
to BSD. In an arithmetic application, identifying the Tor directions
with rational points would require additional arithmetic input.

## 4. The first normal derivative loses the required higher normal jet

**[NEW, conormal-kernel lemma] Lemma 3.** For $R=B[[T]]$, the map
$$
d_N:(T)\longrightarrow (T)/(T^2),\qquad F\longmapsto F\bmod T^2
$$
has kernel $(T^2)$. Hence exact knowledge of $d_NF$ as a function on
the entire tangent family, including every derivative in $U$ and $A$,
does not determine $[T^m]F(0,0,T)$ for $m\ge2$.

If one additionally imposes the exact odd functional equation
$F(U,A,-T)=-F(U,A,T)$, the ambiguity within odd series is
$T^3B[[T^2]]$. Thus the first missing pure normal jet is degree three
in that symmetry class.

*Proof.* Expand $F=\sum_{j\ge1}F_j(U,A)T^j$. The map records only
$F_1T$, proving its kernel assertion. Adding $cT^m$ changes the
desired pure normal coefficient by an arbitrary $c\in L$ without
altering $F_1$, or any tangent derivative of $F_1$. In the odd case
only odd powers occur; taking $m=3,5,\ldots$ proves the second
assertion. $\square$

One may use the formal coordinate $t=\log(1+T)$ over $L$ to make the
cyclotomic involution linear. The change has nonzero linear term, so
it preserves orders and the distinction between tangent and normal
directions. If the original normalization has a nontrivial functional-
equation factor, all identities above can instead be tested after
assuming the stronger exact odd symmetry; even that stronger condition
does not remove the kernel just calculated.

**Application to (2).** The universal theorem determines all coefficients
of the form $U^iA^jT$ in a scalarized local chart. It does not provide
the coefficients of $T^3,T^5,\ldots$ at the fixed weight-two point.
Conjecture Pf concerns leading terms in directions *along*
$\mathscr X$; inserting it into (2) would supply corresponding mixed
tangent/normal derivatives. The source itself describes such
multivariable consequences in Remark 7.3.3. They are not automatically
the pure cyclotomic derivative of the fixed elliptic curve.

If an auxiliary rank-one twist satisfying the Heegner conditions has
been chosen for a rank-two rational curve, its complex base-change function has
rank three and leading term
$$
[s^3]L(E/K,1+s)=[s^2]L(E,1+s)\,L'(E^K,1).
\tag{6}
$$
Even granting every needed $p$-adic factorization and period conversion,
the fixed-motive coefficient on the base-change side is a *pure normal*
degree-three coefficient. Lemma 3 explains why differentiating (2)
twice in weight does not supply it. This failure already occurs before
any issue of an unknown integral unit.

This is not a counterexample to uniqueness from full exact interpolation
of $\mathscr L_p$. Such interpolation can determine the whole function.
The lemma concerns what is lost by passing from that function to the
first conormal derivative appearing in Gross–Zagier.

**[NEW, compatible rank-jump model] Proposition 4.** Even imposing the
first-normal height identity, an exact tangent Pfaffian-class identity,
and a determinantal realization simultaneously does not remove the
lost pure-normal coefficient.

*Proof by an explicit family of complexes.* For any $c\in L^\times$,
on $L[[U,T]]$ take the two-term complex with differential
$$
D_c(U,T)=
\begin{pmatrix}
cT&U&0\\
-U&T&0\\
0&0&T
\end{pmatrix},\qquad
F_c(U,T)=\det D_c(U,T)=U^2T+cT^3.
\tag{6a}
$$
All determinant bases are fixed. The matrix satisfies
$D_c(U,T)^{\mathsf t}=-D_c(U,-T)$: its tangent differential is
skew-symmetric and its first normal differential is symmetric.
On $T=0$, the generic first and second cohomology each have rank one,
represented by $e_3$; at $U=0$ their dimensions are three.
The first normal connecting map induces height
$h_U(e_3,e_3)=1$ on the generic rank-one cohomology.
Set $\mathscr P(U)=Ue_3$. Then for every $c$ the **same exact identity**
holds:
$$
h_U(\mathscr P,\mathscr P)=U^2=[T]F_c(U,T).
\tag{6b}
$$
At the special point the tangent matrix is
$$
J=\partial_UD_c(0,0)=
\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}.
$$
Its Pfaffian cofactor vector, with convention
$(J_{23},-J_{13},J_{12})$, is exactly $e_3$, also the coefficient
of $U$ in $\mathscr P$. Thus the rank-three, order-one tangent
Pfaffian identity holds with coefficient one, independently of $c$.
Nevertheless
$$
[T^3]F_c(0,T)=c.
$$
The full special normal height is the matrix
$\partial_TD_c(0,0)=\operatorname{diag}(c,1,1)$, of determinant $c$.
The first two directions are precisely the directions contributed
by the $U$-torsion in Lemma 2. The generic rank-one height does not
record their normal pairing. $\square$

This model respects the relevant tangent/normal symmetry and exhibits
the lost information inside a perfect complex, rather than merely
varying the valuations of an unrelated power series. It is not claimed
to arise from an elliptic curve. If the full special height matrix is
additionally known, it does recover the coefficient $c$, in agreement
with determinant descent. It still supplies a $p$-adic height
determinant, not its comparison with a fixed complex leading term.

## 5. Testing the strongest proposed analytic continuation step

Suppose exact normalized identities have been established at classical
weights accumulating $p$-adically at weight two. Lemma 1 then extends
them if both sides are already sections of a common line. It does
not show that the special value of one such section is the fixed
weight-two complex leading term.

Two direct tests make the missing argument explicit.

**[NEW, topology test]** For odd $p$, set
$k_n=2+(p-1)p^n$. These classical integer weights tend to two
$p$-adically but tend to infinity as real numbers. In the conventional
weight coordinate
$$
U_n=(1+p)^{k_n-2}-1,
$$
one has $v_p(U_n)=n+1$, while $U_n\to+\infty$ in the real embedding.
The valuation formula follows from the lifting-the-exponent identity
for odd $p$. Even the polynomial section $1+U$ therefore has values
converging $p$-adically to one and diverging in the real topology along
this sequence. No complex limit at weight two follows from this
interpolation topology.

For the actual motives, changing the modular weight changes their
Hodge realization. After a critical self-dual twist, this variation
does not disappear; the Hodge–Tate weights still vary. Consequently
the classical complex first derivatives concern different motives and
different archimedean regulator spaces. They are not derivatives of
one fixed function $L(E,s)$.

**[NEW, even a hypothetical complex family is insufficient without a
derivative comparison]** If a holomorphic function $F(w,s)$ existed
near $(2,1)$, then
$$
\frac{d^m}{dw^m}F(w,w/2)\Big|_{w=2}
=\sum_{j=0}^m\binom mj2^{-j}
 \partial_w^{m-j}\partial_s^jF(2,1).
\tag{7}
$$
This follows by iterating the commuting derivation
$\partial_w+\tfrac12\partial_s$. Thus a central-critical-line
derivative would still contain weight derivatives of the varying
motive. It equals a fixed-motive $s$-derivative only after controlling
all the other terms. A Hida family supplies neither this hypothetical
complex holomorphic family nor the required vanishing of its mixed
derivatives.

These tests rule out the proposed immediate limiting argument. They
do not rule out an additional arithmetic theorem relating the two
realizations. Such a theorem is the target of the next section.

## 6. The first fixed-motive comparison still needed

To avoid concealing the answer inside a period normalization, fix the
published BKS conventions. Let $p$ be odd, $T_pE$ the Tate module,
$S$ contain $p$, infinity and the bad primes, and suppose explicitly:
$$
r=\operatorname{rank}E(\mathbb Q)=\operatorname{ord}_{s=1}L(E,s)\ge2,
\quad H^1(\mathbb Z_S,T_pE)\text{ is free},\quad
\Sha(E/\mathbb Q)[p^\infty]\text{ is finite}.
\tag{8}
$$
The last two conditions and positive algebraic rank are BKS Hypothesis
2.2. They are hypotheses for this comparison attack, not consequences
of the family height theorem.

Let $I$ be the cyclotomic augmentation ideal and
$Q^{r-1}=I^{r-1}/I^r$. Fix a Néron differential $\omega$ and the
Betti choice $\xi$ used by BKS, with its actual period $\Omega_\xi$.
Let $R_\infty$ be the Néron–Tate regulator on a full Mordell–Weil
basis, and let $L_S^*(E,1)$ be the leading Taylor **coefficient** of
the $S$-imprimitive complex function, so factorials and removed Euler
factors are already included. The source keeps
$\Omega^+=v_\xi\Omega_\xi$ explicit in (4.3.3); no silent replacement
by a full real period is made here.
Choose also a nonzero
$x\in\bigwedge^{r-1}_{\mathbb Q_p}H^2(\mathbb Z_S,V_pE)$,
as in the definition of $\eta_x^{\rm BSD}$.

The arithmetic objects $\kappa_\infty$ and $R^{\rm Boc}_\omega$ are
respectively BKS's derived Kato class and its Bockstein regulator
(published Definition 4.10). The exact requested identity is
$$
\boxed{
\kappa_\infty
=\frac{L_S^*(E,1)}{\Omega_\xi R_\infty}
 R^{\rm Boc}_\omega
\quad\text{in }\mathbb C_p\otimes H^1(\mathbb Z_S,T_pE)
                      \otimes Q^{r-1}.}
\tag{8a}
$$
An abstract embedding $\mathbb R\hookrightarrow\mathbb C_p$ is fixed
as in BKS. Equation (8a) is the exact interpretation in their
Proposition 4.14 of Conjecture 4.8,
$\kappa_\infty=\operatorname{Boc}_{\infty,x}(\eta_x^{\rm BSD})$.
Source: [BKS, published PDF, pp. 866–867 and 881–883](https://kurihara.math.keio.ac.jp/bks4.pdf),
J. Math. Soc. Japan **76** (2024), 855–919,
[DOI 10.2969/jmsj/90699069](https://doi.org/10.2969/jmsj/90699069).

Here is the precise missing *specialization identity* in the proposed
family proof of (8a). Suppose a family arithmetic determinant section
$\mathbf z_p$ has been constructed and its derived specialization at
the elliptic point has been identified with BKS's determinant class
$\eta_x^{\rm Kato}$. These are additional arithmetic compatibility
premises; equation (1), by itself, concerns Heegner classes and does
not establish this Kato identification. Impose also the separate,
exact arithmetic descent premise
$$
\operatorname{Boc}_{\infty,x}(\eta_x^{\rm Kato})=\kappa_\infty.
\tag{8b}
$$
One source of (8b) is BKS (7.3.2), whose descent argument assumes
Hypothesis 2.2 **and Conjecture 7.1, the integral Iwasawa main
conjecture**. If that source is invoked, those hypotheses must be
retained. Alternatively (8b) is an explicit additional premise of
the proposed specialization implication; it is not inferred merely
from naming a family datum compatible.
Let $\lambda_{\infty,E}$ be
the fixed-motive period-regulator map of BKS §2.2, built from the
Néron–Tate pairing, the local logarithmic/dual-exponential comparison,
and integration of $\omega$ against the fixed Betti cycle.

In the following formula $\operatorname{sp}^{\det}_E$ includes
determinant base change and the fixed $x$- and Betti-factor
identifications just specified; its target is the exterior-power
line containing $\eta_x^{\rm Kato}$.

**[GAP FS, precisely quantified identity]** For each ordinary-family
datum of §2 and $E,p,S,\xi,x$ satisfying (8), and any such compatible
family determinant section,
prove
$$
\lambda_{\infty,E}\bigl(\operatorname{sp}^{\det}_{E}(\mathbf z_p)\bigr)
=\lambda_{\infty,E}(\eta_x^{\rm BSD}).
\tag{9}
$$
Both sides lie in the same one-dimensional comparison space of
BKS §2.2; the right side is its specified $L_S^*(E,1)$ value, with
the $x$- and Betti factors retained. Equivalently, after those
trivializations, the scalar on the left must be the fixed-motive
complex leading coefficient with its exact period and regulator.
This is not an assertion that the two sides generate the same ideal.

If (9) holds, the invertibility of $\lambda_{\infty,E}$ identifies
the determinant elements. Applying Bockstein and using the explicit
premise (8b) then gives (8a). Conversely,
when $R^{\rm Boc}_\omega\ne0$, BKS's Bockstein map is injective on
the rank-one exterior-power source. Under (8b), (8a) therefore implies
(9) for a family section with the asserted Kato specialization. Thus in that
nondegenerate vector case the missing specialization identity cannot
be weaker merely because it has been written in family notation.

## 7. Attempt to derive (9), and the exact outcome

The most favorable continuation attempt is to transport every
classical period-regulator-normalized complex leading term into the
fiber of $\det\mathscr C$, identify it with $\mathbf z_p$ there using
a Gross–Zagier theorem, and then use density to deduce (9).

The proved part is Lemma 1: **if these transported values extend as
a regular section $\mathbf z_\infty$ and its special fiber is
$\eta_x^{\rm BSD}$, then density identifies it with $\mathbf z_p$**.
This remains true through arbitrary cohomological rank jumps.

The attempted construction of $\mathbf z_\infty$ fails at an exact
step. On a local determinant frame $e$, the arithmetic section is
$f e$ for an already determined $p$-adic analytic function $f$.
Dense classical formulas determine $f$. One can therefore define a
section with those values simply as $f e$, but its fixed-motive
period image is then the *left* side of (9). Declaring that its
special fiber is the complex BSD element assumes (9); it does not
follow from the construction. Lemma 2 explains why replacing this
step by ordinary interpolation of generators misses the additional
special cohomology directions, while (7) explains why a weight
derivative does not repair the complex realization.

Trying instead to differentiate the already constructed family
$p$-adic $L$-function is useful but reaches a different object. Its
full exact interpolation can determine the pure cyclotomic leading
coefficient. Equation (2) alone loses that coefficient by Lemma 3;
adding Conjecture Pf still initially gives tangent mixed derivatives
and only a coefficient-field scalar ambiguity. Even granting an exact
refinement of Pf and recovering every $p$-adic derivative, no proved
identity in this argument identifies the result with
$L_S^*(E,1)/(\Omega_\xi R_\infty)$. That remaining assertion is (9),
or the equivalent fixed-motive comparison (8a) under the stated
compatibilities.

### A further test against motivic fundamental-line specialization

The directly relevant primary result is Fouquet,
*$p$-adic properties of motivic fundamental lines*, J. Éc. polytech.
Math. **4** (2017), 37–86,
[DOI 10.5802/jep.38](https://www.numdam.org/item/10.5802/jep.38.pdf).
Theorem 1.1, under Assumption 4.1's ring, residual irreducibility,
local Frobenius-polynomial, and purity hypotheses, proves compatibility
of the $p$-adic fundamental line with pure monodromic specializations.
Corollary 1.2 specializes a basis to a basis. These are arithmetic
control results of precisely the kind permitted by Lemma 1.

The source distinguishes this from the motivic fundamental line
*equipped with both period maps*: that triple is defined in §2.2.2.
Its complex leading-value and integral-lattice requirements are the
two separate assertions in Conjecture 2.11. The unconditional explicit
period-map construction there is for **strictly critical** motives.
The definition in §2.1.1 requires the global dual exponential to be
an isomorphism and global étale cohomology to vanish outside degree
one, in addition to the archimedean criticality condition.

**[NEW, arithmetic hypothesis test] Proposition 5.** Under (8), the
weight-two representation in the BKS comparison does not satisfy
these strict-criticality conditions.

*Proof.* BKS (2.2.1) identifies its global $H^1$ with
$E(\mathbb Q)\otimes\mathbb Q_p$, of dimension $r$. Its localization
at $p$ lies in the finite local condition, so the dual exponential
annihilates it. In particular the global dual exponential is not an
isomorphism to the one-dimensional filtered de Rham space. Moreover
BKS (2.2.2) gives $\dim H^2=r-1$, which is positive when $r\ge2$.
This violates the second cohomological condition as well. $\square$

Therefore invoking pure-motivic *line* compatibility does not make
the strict-critical period formula applicable at this point. A
derived period-regulator construction is needed there, and its
fixed-motive value is exactly what (9) asks to identify. This is a
specific failed hypothesis check, not an objection to Fouquet's
specialization theorem.

For completeness, the related Hecke-algebra preprint
[Fouquet, arXiv:1604.06411, §2.3.2](https://arxiv.org/html/1604.06411)
was also checked at its interpolation formulation (2.3.2.1)–(2.3.2.2).
Those equations interpolate critical **values** through localization
and period maps; they do not supply the higher central Mellin
derivative and the new Néron–Tate regulator required in (9). Its
introduction expressly identifies its cyclotomic assertion with
Kato's Iwasawa main conjecture. The title's use of “ETNC” must not
be substituted for a verification of the missing period identity.

The outcome is therefore a valid determinant specialization lemma,
an explicit description of the missing special-fiber directions, and
a precise separation of normal jets from the derivatives supplied by
the universal theorem. No Sha-finiteness premise has been discharged,
no complex BSD coefficient has been identified, and no family
comparison theorem proving (9) has been established. The next useful
arithmetic step must construct the fixed-motive comparison of the
determinant section, including its Betti and height normalization;
density alone has now been pushed as far as the stated lemmas permit.
