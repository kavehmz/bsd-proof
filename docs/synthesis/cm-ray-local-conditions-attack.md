# Both actual CM ray derivatives satisfy the finite local conditions

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: all eight sections independently reviewed PASS by the coordinator;
see the [source and deduction review](review-cm-ray-local-conditions.md).
The review inspected mathematical revision
39275d6deea6e97e3370e7ee1599a5001a386767e0bf89140499644b3343de34;
this PASS header is editorial and changes no formula.
The objective remains full BSD over Q. Both constructed ray derivatives,
and their difference, are proved Selmer below. This leaves the rational
global determinant comparison and Sha finiteness unproved.

## 1. The actual classes and the stronger method

Keep E:y²=x³+39x, K=Q(i), the full basis P=(3,12), Q=(27,144),
and the good split scope of the reviewed
[two-variable construction](cm-two-variable-jet-attack.md).
Write $T_\pi=T_{\mathfrak p}E$, V_π=T_π⊗Q_p, and T=T_pE,
V=T⊗Q_p. Its actual integral classes are
$$d_\pi,d_{\bar\pi}\in H^1(G_{K,S_K},T_\pi),\qquad
\widetilde d_\pi=\operatorname{Sh}(d_\pi),\quad
\widetilde d_{\bar\pi}=\operatorname{Sh}(d_{\bar\pi})
\in H^1(G_{\mathbb Q,S},T). \tag{1}$$
Here Sh is the fixed integral identification
Ind_K^Q T_π=T_pE and its Shapiro map, and
S={2,3,13,p,∞}. It is applied to each actual base-field
cohomology class, not merely to their sum.

The previous theorem proved
$$\widetilde d_\pi+\widetilde d_{\bar\pi}=w_0. \tag{2}$$
This note does not infer individual local conditions from (2).
Instead it pairs EACH class with the fixed rational point P
using global Weil/Tate reciprocity. This is a different pairing
from the ordinary c_π cup d_π relations and from a p-adic height.
It supplies the following general positive-rank statement over Q.

## 2. A positive-rank global cohomology class is already finite locally

For a local field F of characteristic zero, let
E(F)^∧p=lim_m E(F)/p^mE(F), and define
$$H^1_f(F,V)=\operatorname{im}\bigl(E(F)^{\wedge p}
\otimes_{\mathbb Z_p}\mathbb Q_p\to H^1(F,V)\bigr). \tag{3}$$
For an elliptic curve this is the Bloch–Kato finite condition.
The local Kummer and orthogonality statements are verified in
[Rubin, Euler Systems, I §6.4 and Remark6.6](https://swc-math.github.io/aws/1999/99RubinES.pdf);
the local duality is TheoremI.4.1. The underlying local abelian
duality and point-group structure are proved in
[Milne, Arithmetic Duality Theorems, I.3.2–I.3.5](https://www.jmilne.org/math/Books/ADTnot.pdf).

**[NEW] Lemma 2.1.** For every elliptic curve E/Q and odd prime p,
$$H^1(\mathbb Q_\ell,V)=0\quad(\ell\ne p),\qquad
\dim_{\mathbb Q_p}H^1(\mathbb Q_p,V)=2,\quad
\dim_{\mathbb Q_p}H^1_f(\mathbb Q_p,V)=1. \tag{4}$$
The last line is its own annihilator for local Weil/Tate duality.

*Proof.* E(F) has a torsion-free open formal subgroup and compact
quotient, so its p-primary torsion is finite for every fixed finite
extension F of Q_ℓ. Hence H⁰(F,V)=0. Principal polarization
identifies V∨(1) with V, and local duality gives H²(F,V)=0.
For ℓ≠p, the local Euler characteristic, equivalently Rubin
CorollaryI.3.3, then gives H¹=0. For F=Q_p the Euler
characteristic is −dim V=−2, giving dimension two.
The p-adic completion of E(Q_p) has Z_p-rank one, since its
open formal subgroup has dimension one; Kummer is injective,
so (3) has dimension one. Local abelian duality identifies
this finite subgroup with its exact annihilator. ∎

**[NEW] Theorem 2.2 (positive algebraic rank over Q).** Suppose
E(Q) contains a non-torsion point P₀, p is odd, and S is a finite
set containing p,∞ and all bad primes. Then
$$H^1(G_{\mathbb Q,S},V)=H^1_f(\mathbb Q,V), \tag{5}$$
where the right side imposes the point-Kummer finite conditions
at every place. No analytic rank or Sha-finiteness hypothesis is needed.

*Proof.* Let z be a class on the left and let κ(P₀) be its global
point-Kummer class. Global reciprocity gives
$$\sum_v\bigl(\operatorname{loc}_v\kappa(P_0),
\operatorname{loc}_v z\bigr)_v=0. \tag{6}$$
These are the usual local Weil/Tate cup pairings into Q_p(1)
followed by the local invariant, not Selmer-height pairings.
One can obtain (6) directly from finite coefficients: clear a
p-power denominator of z, take the cup into μ_{p^m} at every m,
apply the global sum-of-invariants reciprocity law, and pass to
the compatible limit. The global orthogonality assertion is also
the finite Poitou–Tate statement in Rubin TheoremI.7.3.
Outside S the two unramified classes have zero invariant, so
only a fixed finite sum occurs.

By Lemma2.1 every finite summand except p is zero rationally.
The real odd-p term is zero. Thus
$$\bigl(\operatorname{loc}_p\kappa(P_0),
\operatorname{loc}_p z\bigr)_p=0. \tag{7}$$
The local logarithm of P₀ is nonzero. Indeed its kernel on the
compact p-adic Lie group E(Q_p) is torsion: a multiple of any
point enters a sufficiently small formal subgroup, where the
logarithm is injective. If a rational non-torsion point became
torsion over Q_p, the same rational multiplication relation
would hold over Q, a contradiction.
Therefore loc_pκ(P₀) spans the one-dimensional space in (3).
Its annihilator is that same finite line. Equation (7) proves
the finite condition for z at p, and the other conditions follow
from (4) and the real vanishing. The reverse inclusion in (5)
is the defining unramified global inclusion. ∎

The assertion is specifically over Q: one point need not span
the larger collection of local finite spaces over an arbitrary
number field. Nor does (5) identify global cohomology with the
Mordell–Weil space; possible Tate-module Sha classes remain.

## 3. Integral saturation, with torsion retained

The passage from rational finite conditions to finite coefficients
requires an integral argument. It must not divide a point logarithm
or an Euler factor modulo p^m.

**[NEW] Lemma 3.1.** For a finite extension F of Q_ℓ,
$$H^1(F,T)/E(F)^{\wedge p}\simeq T_pH^1(F,E). \tag{8}$$
The right side is p-torsion-free. Consequently the inverse image
of H¹_f(F,V) in H¹(F,T) is EXACTLY the integral point-Kummer
image E(F)^∧p, including its possible finite torsion.

*Proof.* Take inverse limits of the finite Kummer sequences
$$0\to E(F)/p^mE(F)\to H^1(F,E[p^m])
\to H^1(F,E)[p^m]\to0.$$
The left transition maps are surjective; these local point
quotients and finite-coefficient cohomology groups are finite.
Thus the Mittag–Leffler condition gives (8), with the ordinary
continuous-cohomology identification of the middle inverse limit.

For any abelian group A, multiplication by p is injective on T_pA:
if x=(x_m) is killed by p, then x_m=p x_{m+1}=0 for all m.
Therefore T_pA embeds in its tensor product with Q_p.
Rationalizing (8) and using (3) shows that the kernel of
H¹(F,T)→H¹(F,V)/H¹_f(F,V) is its stated Kummer image.
Continuity and rationalization of cohomology are the ones in
Rubin AppendixB §§2–3; no local Sha assumption is involved. ∎

**[NEW] Corollary 3.2.** Under Theorem2.2's hypotheses, every
z∈H¹(G_Q,S,T) has integral local point-Kummer images. Its
reduction in H¹(Q,E[p^m]) belongs to the full classical
Selmer_{p^m}(E/Q) for every m.

*Proof.* Apply Theorem2.2 to z⊗Q_p and then Lemma3.1 at
every finite place. Reduction of a point-completion class is
the corresponding finite local point-Kummer class. At the real
place the finite odd-p condition is zero. ∎

This does not say that every finite global H¹ class is Selmer,
or that every finite class lifts to integral T-cohomology. The
ray classes do have such compatible integral lifts by their
actual construction, which is what permits this application.

## 4. Application to the actual ray classes at both CM primes

The fixed integral Shapiro map in (1) satisfies
$$\operatorname{pr}_{\mathfrak p}
\operatorname{res}_{K/\mathbb Q}
\operatorname{Sh}(d)=d. \tag{9}$$
This is the counit in the same induced-representation identification
used in the original normalization; it has no degree-two averaging.
Local restriction of point-Kummer classes remains point-Kummer.
The integral CM idempotent preserves those images, since CM
endomorphisms act on local points and on their p-completions.
Thus the corresponding local statements transfer to T_π.

**[NEW] Theorem 4.1.** Both actual classes d_π and d_barπ
are Selmer for the CM component, and both Shapiro images
in (1) are in the integral Selmer group over Q. The same is
true of their difference and every integral linear combination.
Each finite d_π,m,d_barπ,m satisfies the propagated finite
point-Kummer conditions, and its Shapiro image belongs to the
full classical Selmer_{p^m}(E/Q).

*Proof.* P=(3,12) is a non-torsion rational point in the
already certified full basis. The classes in (1) are actual
integral global cohomology classes, so Corollary3.2 applies
to EACH of them. Equation (9) and the preceding local
functoriality give the component statements. Their finite
classes are the reductions of those integral classes, not
arbitrary finite cohomology lifts. Linearity proves the
assertion for their difference and other combinations. ∎

Here is the exact rational local table. The labels of the split
primes are those of the two-variable proof: the first Tate
character Ψ is the formal component at $\mathfrak p$. Put
α the ordinary unit root and β=p/α. Then

| Place for T_π | Local type | φ on D_cris(V_π) | dim H¹ | H¹_f |
| --- | --- | --- | --- | --- |
| $K_{\mathfrak p}\simeq\mathbb Q_p$ | Formal CM component | β⁻¹ | 1 | All H¹ |
| $K_{\bar{\mathfrak p}}\simeq\mathbb Q_p$ | Unramified CM component | α⁻¹ | 1 | 0 |

The ordinary connected/étale sequence and the integral CM
idempotents give these two one-dimensional components. The labels
can be checked without guessing a reciprocal Frobenius root:
[π] has degree p and acts on the tangent by π. At mathfrak p
its reduction is purely inseparable of degree p, whereas [barπ]
has invertible tangent map and étale kernel. At the conjugate
place the roles reverse.
Their tangent dimensions are one and zero, respectively.
They have no rational H⁰, nor does their local Tate dual,
so local Euler characteristic gives the two H¹ dimensions.
The finite dimensions follow from Kummer/Bloch–Kato and those
tangent dimensions. Equivalently, they are the formal and
étale components of the local Shapiro decomposition of V.

In particular Theorem4.1 computes, for j=π,barπ,
$$\operatorname{loc}_{\mathfrak p}d_j\bmod H^1_f=0,\qquad
\operatorname{loc}_{\bar{\mathfrak p}}d_j=0
\quad\text{in rational }H^1. \tag{10}$$
The first localization itself need not be zero; it is finite.
No point or scalar has been added to either derivative to
arrange (10).

The Frobenius dictionary is the previously audited one.
On ordinary H¹_dR the absolute cohomological F has
Fω=βω and F(xω)=αxω; on D_cris(V_pE), φ=F/p.
Thus φω=α⁻¹ω and φ(xω)=β⁻¹xω. The formal local
Tate component corresponds to the latter line under the
polarization identification, and the unramified component
to the former. The contradictory reciprocal label in the
printed SW§4.1 is not reused. The primary check is
[Mazur–Stein–Tate,§3.2](https://wstein.org/papers/pheight/pheight.pdf)
together with BKS Lemma6.9 and the fixed CM action.

## 5. Integral zero at the unramified prime: the anomalous distinction

Rational zero in the second row of (10) need not be integral
zero in general. For an unramified rank-one lattice T_π with
arithmetic Frobenius α≠1, the long exact sequence for
0→T_π→V_π→V_π/T_π→0 gives
$$H^1(K_{\bar{\mathfrak p}},T_\pi)_{\rm tors}
\simeq (V_\pi/T_\pi)^{G_{K_{\bar{\mathfrak p}}}}
\simeq(\alpha-1)^{-1}\mathbb Z_p/\mathbb Z_p. \tag{11}$$
Thus (10) alone only places an integral localization in this
possibly nonzero torsion subgroup. Lemma3.1 still puts it
in the integral finite condition, which is the correct
conclusion at an anomalous prime.

For the actual E:y²=x³+39x the stronger integral zero follows
at every allowed good split p. The rational two-torsion point
(0,0) has nonzero reduction at every good odd p, so #E(F_p)
is even. For p≥7 Hasse gives 0<#E(F_p)<2p; the only
possible nonzero multiple of p in that interval is the odd
integer p. Hence p does not divide #E(F_p). At p=5 the
already recorded exact coefficient a₅=−2 gives #E(F₅)=8;
see the [fixed CM data](cm-regulator-tensor-attack.md#1-the-actual-curve-and-source-hypotheses).
This uses no rerun of the old numerical certificates.

Since #E(F_p)=(1−α)(1−β) and 1−β is a p-unit, α−1 is
a p-unit in this actual scope. The torsion group in (11)
vanishes. Therefore
$$\operatorname{loc}_{\bar{\mathfrak p}}d_\pi
=\operatorname{loc}_{\bar{\mathfrak p}}d_{\bar\pi}=0
\quad\text{integrally, and after reduction at every }p^m.
\tag{12}$$
The finite-condition quotient at mathfrak p is also zero,
by Theorem4.1; its finite localization is not asserted zero.

## 6. The exact Coleman obstruction scalar is zero

The preceding argument also evaluates the local Coleman
augmentation obstruction with all the old constants retained.
Use the fixed Néron differential ω=dx/(2y), and the BKS
vector ν with φν=β⁻¹ν and [ω,ν]=1. Set
$$k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1}),\qquad
\delta_0=\frac1p\left(-\varphi^{-1}
 +(p-1)(1-\varphi)^{-1}\right)\nu=k_\alpha^{-1}\nu.
\tag{13}$$
These formulas and the following local functional were checked
directly in [BKS,1910.07404, Lemma6.9, (6.3.1)–(6.3.2), the
Coleman definition and the proof following Lemma6.14](https://arxiv.org/pdf/1910.07404).
No Sha hypothesis from their later determinant theorem is
needed for these local exponential identities.

For ξ∈H¹(Q_p,V) define the exact augmentation functional
$$\mathcal O_p(\xi)
=[\exp^*(\xi),\delta_0]
=(\exp(\delta_0),\xi)_p. \tag{14}$$
It is the n=0 Coleman formula, defined on a local class
whether or not a separate cyclotomic Iwasawa lift of that
class has been chosen. Its kernel is H¹_f(Q_p,V).
The fixed point P has the identity
$$\operatorname{loc}_p\kappa(P)=k_\alpha\log_\omega(P)\exp(\delta_0).
\tag{15}$$
Here log_ω(P) is nonzero. For each actual ray class,
Theorem2.2's reciprocity calculation therefore gives the
explicit arithmetic obstruction formula
$$\boxed{\quad
\mathcal O_p(\operatorname{loc}_p\widetilde d_j)
=\frac{(\operatorname{loc}_p\kappa(P),
              \operatorname{loc}_p\widetilde d_j)_p}
 {k_\alpha\log_\omega(P)}
=0,\qquad j=\pi,\bar\pi.\quad} \tag{16}$$
If exp*ξ=b_ξω, then (14) is k_α⁻¹b_ξ; thus (16)
is an exact zero of the normalized singular coordinate.
It is not equality only up to an unspecified p-adic unit.

The division in (16) is in Q_p. It is not a claim that
log_ω(P) or k_α is invertible modulo p^m. Integral and
finite-coefficient conclusions were instead proved by the
torsion-free Kummer quotient (8), and integral zero at the
unramified prime by (11)–(12). This distinction prevents
loss of local torsion.

## 7. Source normalizations and Tor terms remain unchanged

The classes whose obstructions were evaluated are the original
ones. In particular the source still uses the unnormalized
tame norm of degree |Δ|=1152(p−1)², the tau-odd branch,
and the exact divisor
$$q_a(X,Y)=12\left(a^2-u_a(1+X)^{\lambda_a}
 (1+Y)^{\lambda_a}\right),\quad
u_a=\Psi^c((a))=\pm a,\quad \lambda_a=\log_p(a)/g_p.
\tag{17}$$
The coefficient vector is 2pr_ρ(γ_E⁺), g_p=log_p(1+p),
and the quotient sends X,Y to T. Finite ray exponents
remain at least m+1. We have neither averaged away Δ
nor changed a ray generator or an individual class.

Consequently the formerly known framed sum remains
$$\mathcal B_p^{-1}\left(
\frac{p}{2\#E(\mathbb F_p)}
\operatorname{pr}_W\bigl(
(\widetilde d_\pi+\widetilde d_{\bar\pi})\otimes T\bigr)\right)
=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}\Xi,
\tag{18}$$
with c_cmp,p=(156iΩ_p)⁻¹ and e_p=(1−α⁻¹)².
The known inverse-map and regulator-nondegeneracy scope is
unchanged. Although each derivative is now Selmer, no
separate formula for its projected arithmetic scalar is
inferred from the formula for the sum. In particular an individual
projection has not been shown to lie in the one-dimensional
image of B_p; only the sum is known to lie there.

The two-variable edge still contains
Tor₂(H²_Iw,Z_p)→H¹_Iw/I and Tor₁(H²_Iw,Z_p) on the
other side, and cyclotomic base change still retains
H²_Iw[X−Y]. Selmer membership of the base classes proves
none of these terms zero and does not establish I-divisibility,
flatness or a new lift in the Iwasawa H¹ module.

## 8. Completed local result and exact remaining comparison

Both individual actual derivatives, their difference and their
integral combinations satisfy the finite local conditions.
At the formal CM prime the singular quotient is zero; at
the unramified CM prime their actual localizations are zero
rationally, and also integrally for this nonanomalous curve.
The exact Coleman obstruction is (16), so no correction
chosen after the fact is necessary.

This does not identify the two classes with rational points
or eliminate their possible Tate-module Sha contributions.
Neither their nonvanishing nor their independence is proved.
The construction gives no new full Sha-finiteness statement.

**[GAP CM-Ray-BSD].** Construct an arithmetic comparison
producing one rational element Z_alg in the fixed CM
determinant line whose allowed p-localizations are (18),
with the established undivided identities where required,
and whose real realization is
$$R_\infty(Z_{\rm alg})=\frac{L''(E,1)/2}{2\Omega_E}. \tag{19}$$
Its rational coefficient would then equal n_E as a conclusion.
The newly proved individual Selmer conditions do not supply
this rational global element or its complex comparison.
Universal BSD remains unresolved.

Primary inputs were inspected at the exact locations cited
above. The new proof uses actual global ray classes, usual
Weil/Tate reciprocity and the fixed local Coleman functional;
it does not postulate a new two-variable big-log factorization.
No old numerical script was rerun and no new agent was created.
Independent review is required before promoting these deductions.
