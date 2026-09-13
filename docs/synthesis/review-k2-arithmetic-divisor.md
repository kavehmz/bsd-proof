# Independent review of the arithmetic noncentral K2 divisor

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Reviewed [the seven-section proof](k2-arithmetic-divisor-attack.md) and
[its checkpoint](k2-arithmetic-divisor-checkpoint.md).

**PASS.** The actual rational class has a unique lift in
CH²(X,2)⊗Q, integral restriction is injective, and the stated finite
data give a sufficient integral multiple. No mathematical correction
is required. The proof uses the arithmetic IMAGE theorem, not equality
of regulator images. Its integral assertions concern Bloch higher
Chow groups, not an integral Adams decomposition.

Reviewed proof SHA256:
ad0bd821520518592dbee0023e4119199cf790ea626ccedee3cf019f4d4d463a.
Reviewed checkpoint SHA256:
a99cc46529ac8ef17abf016bab9318a5c680a03d4044f10fdf36060b9a73a013.
The local-at-389 source-scope clarification is included in this
inspected revision. Subsequent PASS links and checkpoint completion
are editorial.

The arithmetic spectral-to-height map remains unconstructed.
Neither rationality of the BSD quotient nor full BSD is proved.

## 1. The fixed class and the exact arithmetic-image theorem

I read the predecessor's finite construction and its
[independent review](review-integrated-spectral-comparison.md), then
checked the new arithmetic input directly in
[Schappacher–Scholl](https://ncatlab.org/nlab/files/SchappacherScholl.pdf),
1.1.0–1.1.3 and 7.3–7.4. Definition 1.1.0 uses the image of
weight-two K2 of a regular arithmetic model. Definition 1.1.1
places unramified modular-unit symbols in Q_K⊂P_K.
Theorem 1.1.2(iii) puts P_K in that arithmetic image. Thus it
applies to the class itself, rather than to its regulator modulo
an unknown regulator kernel.

The temporary hypothesis in 7.3.0 is real: its full level must
factor into coprime integers at least three. Here 3·389 meets it.
Pullback preserves the modular-unit symbols and unramifiedness;
push-pull is the finite degree. Division by that degree is valid
in the rational group. Remark 7.3.2 gives the descent by the
graph correspondence. The final theorem already covers arbitrary
compact-open level. Section 7.4 expressly rejects the stronger
integral modular-unit premise; the draft does not use it.

The finite map h:C→E is a Chow correspondence.
[Scholl 0710.5453, §1](https://arxiv.org/pdf/0710.5453) recalls
model independence and functoriality of the rational arithmetic
subspace for Chow motives. Consequently h_* preserves the
arithmetic image. This requires no integral extension of h to
the particular displayed arithmetic models. The finite rational
linear combination with coefficients q_ab stays in that image.

Expanding the predecessor's coefficient trace gives exactly
the displayed q_ab: its k_chi contributes d_chi times the two
character coefficients, and its normalization contributes
N/(2(N−1)b_chi). The trace is on scalars of fixed rational
classes. It is neither a field norm on curves nor a replacement
of the original beta_2 by some class with the same regulator.

## 2. Arithmetic localization and the rational comparison scope

I checked the exact statements of
[Geisser 2004](https://www2.rikkyo.ac.jp/web/geisser/Dedekind.pdf),
Theorem 3.2, Corollaries 3.3–3.4 and Lemma 2.4.
Although the paper's introductory convention often assumes smoothness,
these localization statements explicitly allow schemes essentially
of finite type over the stated DVR or Dedekind base. They therefore
apply to the regular arithmetic surface at its nonsmooth nodal fiber.
Corollary 3.3 identifies cycle cohomology with the relevant
hypercohomology locally on the base; the generic-fiber triangle
retains the direct sum of closed-fiber support terms.
Taking the required degrees gives precisely
\[
 \bigoplus_r\operatorname{CH}^1(X_{\mathbb F_r},2)
 \longrightarrow\operatorname{CH}^2(X,2)
 \longrightarrow\operatorname{CH}^2(E,2)
 \longrightarrow\bigoplus_r\operatorname{CH}^1(X_{\mathbb F_r},1).
\]
This uses no smooth purity theorem at the node.

[Geisser's Handbook chapter](https://www2.rikkyo.ac.jp/web/geisser/Handbook.pdf),
§1.4.4, explicitly treats finite-type schemes over a DVR by the
higher-Chow-to-K′ spectral sequence. Its rational degeneration
and Adams weights give the rational comparison. For our REGULAR
model, coherent K′-theory agrees with vector-bundle K-theory.
No such integral Adams identification follows or is used.
The smooth weight-one formula from §1.2.2 is used only on the
smooth opens and good fibers.

The author's final revision uses precisely this source scope.
Restrict the arithmetic
K-class from §1 to the regular model over Z_(389). Apply the
rational comparison there, including its generic restriction.
It follows that the CH boundary of beta_2 at 389 is zero rationally.
Every other rational CH boundary is already zero by the good-fiber
calculation below. The GLOBAL Bloch localization sequence then
puts beta_2 in CH²(X,2)⊗Q. This proves the needed global
arithmetic-image statement without silently treating X as smooth
over Z, and without needing a stronger global comparison theorem.
The fiber calculation and localization are independent of the
arithmetic-image proposition, so its forward reference is not circular.

On a smooth generic curve C, localization to its function field gives
\[
 0\longrightarrow\operatorname{CH}^2(C,2)
 \longrightarrow K_2^M(\mathbb Q(C))
 \longrightarrow\bigoplus_{x\in C^{(1)}}\kappa(x)^*.
\]
The initial zero follows from CH¹(κ(x),2)=0, and the two field
identifications are the usual weight-two Milnor and weight-one
comparisons. This verifies the INTEGRAL tame-kernel assertion;
there is no additional integral Quillen-weight claim.

## 3. The nodal fiber, including its nonzero free boundary direction

I reconstructed the normalization calculation algebraically.
The equation w²=u²(u+120) gives t=w/u away from the node and
u=t²−120, w=t(t²−120). The two preimages of the node are
t=148 and −148=241 in F_389. Both are rational and distinct.
Thus the smooth complement is P¹ minus these two points.
The displayed coordinate z=(t−148)/(t−241) identifies it with
G_m and sends the retained point at infinity to 1.

For the closed node s, localization gives
\[
 \operatorname{CH}^0(s,2)\to\operatorname{CH}^1(D,2)
                  \to\operatorname{CH}^1(\mathbb G_m,2).
\]
The outside terms are zero. For the next term it gives an injection
of CH¹(D,1) into k[z,z⁻¹]^*, because CH⁰(s,1)=0.
Its boundary is computed by the valuations on the normalization,
pushed to the single node. The two residue degrees are one:
\[
 \partial_s(cz^j)=j+(-j)=0.
\]
Consequently every c z^j is in the image, and restriction gives
\[
 \operatorname{CH}^1(D,2)=0,\qquad
 \operatorname{CH}^1(D,1)\simeq k^*\times z^{\mathbb Z}.
\]
This argument works without the node being a regular embedding
in D. The field localization theorem is enough.

For good fibers, smooth weight one gives zero in degree two
and the global units in degree one. Proper geometric integrality
makes those units F_r^*. The calculation on D is different:
its higher-Chow degree-one group has a free summand even though
ordinary global units on the proper singular curve are just k^*.
The draft explicitly preserves this distinction.

## 4. Integral injectivity and the unique rational lift

All the preceding fiber degree-two groups vanish integrally.
The left term of arithmetic localization is therefore zero,
which proves A→A_E injective, including on torsion.
Its image is the kernel of the actual displayed vertical boundary.
This proves exactly the assertions in Theorem 4.1; it does not
assert surjectivity onto that boundary group.

Tensoring the direct sum of finite F_r^* with Q gives zero,
while the nodal exponent survives as Q. Hence
\[
 \operatorname{im}(A\otimes\mathbb Q)
 =\ker(\operatorname{ord}_z\partial_{389}).
\]
The arithmetic-image theorem annihilates this exponent for the
SPECIFIED beta_2. This supplies existence of its rational lift.
Integral injectivity, followed by rationalization, supplies
uniqueness. Neither property uses injectivity of a real regulator,
an assumed rank for K2, or Sha finiteness.

## 5. Horizontal denominators and the factor two

I also checked the required modular-unit scope directly in
[Brunault's thesis](https://arxiv.org/pdf/math/0602186),
Proposition 86 and (3.95). These concern the rationally normalized
units supported on the specified infinity cusps; the rational model
and cusp action are fixed in §3.4. The predecessor's X_mu(N)
model has rational P_a. It is essential to keep this model when
bounding torsion tame values. The usual bare notation X_1(N)
without its rational-model convention would not justify that step.

A common multiple M of the finitely many cusp-divisor orders
produces actual V_a with div(V_a)=M(P_a−P_1). Normalization at
the fixed rational cusp makes their classes exactly M U_a.
Bilinearity then multiplies every symbol by M².

Rational unramifiedness says the tame symbols of {V_a,V_b}
are torsion. Where both functions have order zero the tame
symbol is already 1. Every possible remaining support point
is a rational P_a, so its residue-field torsion lies in
Q^*_{tors}={±1}. Multiplication by TWO kills it integrally.
This justifies an integral CH²(C,2) class for each doubled symbol.
It does not assume the individual tame signs equal +1.

After clearing the FINITE coefficient list by D_c, integral proper
pushforward gives the specified preimage
\[
 b=\sum_{a,b}(D_cq_{ab})h_*(2\{V_a,V_b\})\in A_E,\qquad
 b\otimes1=2M^2D_c\,\beta_2.
\]
Thus D_0=2M²D_c is sufficient. The expression b=D_0 beta_2
means this chosen integral preimage, not a canonical lifting
of every rational element through A_E→A_E⊗Q.
No covering degree is inverted in this integral pushforward.

## 6. Spreading and killing every remaining finite boundary

A cycle representative uses finitely many equations and finitely
many face intersections. Its closures, and the asserted equality
of their boundaries, become admissible after excluding finitely
many primes S_0. Equivalently this follows directly by taking the
filtered generic-fiber limit of the Bloch complexes. Thus the actual
class b has zero boundary outside one fixed finite S_0.

At a good r in S_0 its boundary lies in F_r^*, so r−1 kills it.
At 389 its integer z-exponent is zero because the rational
boundary of D_0 beta_2 is zero; rational zero in a Z summand
is integral zero. Its remaining boundary lies in F_389^*,
of order 388. If 389 is outside S_0 its boundary was already zero.
Therefore
\[
 D_1=\operatorname{lcm}_{r\in S_0}(r-1)
\]
kills every boundary, including the bad-fiber torsion.
Localization gives B∈A restricting to D_1 b, and the proven
integral injection makes B unique for that specified class.
Its rationalization is D_0D_1 times the unique rational lift.

This is a sufficient denominator formula in terms of finite inputs,
not a computed numerical denominator or a primitivity theorem.
The construction fixes D independently of any later coefficient
prime or exponent. Nonzero regulator makes ZB free of rank one;
it does not make it saturated or prove finite generation of the
intersection of its rational line with all of A.

## 7. Normalizations and the exact surviving gap

Restriction of B has regulator D L(E,2)/pi by linearity from the
fixed predecessor normalization. No additional regulator factor
arises from arithmetic extension. The coefficient trace, map h,
negative-conjugation cycle b, and Tate factor Q(1)^(-2) are unchanged.
The distinction between the frame beta_2 and its integral multiple
B is preserved; D is not treated as an integral unit.

The positive result completes arithmetic extension of this
NONCENTRAL divisor. It does not construct a rational arithmetic
class for the full theta source or its map to
D_pt⊗Q beta_2⊗Q(1)^(-2). That map would have the prescribed
coefficient 6N(N−1)n_E and requires further integral control.
Neither a rational spectral image nor integrality of n_E follows
from the present lift and denominator.

Only this review was written for the K2 task. The separately
owned CM local-condition proof/checkpoint received editorial
PASS updates after its independent review. No old mathematical
certificate was rerun, and no subagent was created.
