# A support-retaining secondary Kummer operation on the higher cycle

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Completed bounded construction; all [NEW] deductions passed
[independent review](review-secondary-kummer-theta.md).
Restart: [checkpoint](secondary-kummer-theta-checkpoint.md).
Full BSD over Q remains the parent objective.

The constructed operation is a product with an actual fiber-dependent
Kummer function, followed by its localization residue and a proper push
from its divisor. It is designed from the independently given rational
eta unit, not from the desired real leading coefficient.

## 1. Spaces, coefficient and boundary specified first

Keep N=389, X=$X_0(N)$, $Y=X\setminus\{0,\infty\}$,
$E=389a1$ and its degree-40 map $\pi:X\to E$. The exact input is
$$u=N^{-6}\Delta(z)/\Delta(Nz)\in\mathcal O(Y)^*,\qquad
\pi(0)=\pi(\infty)=O,\quad \pi W_N=[-1]\pi,\quad W_N^*u=u^{-1}.
\tag{1.1}$$
These are the reviewed identities of the
[elliptic projection proof](theta-elliptic-projection-attack.md).
No unknown leading coefficient is used to choose u.

Over the connected full-level 35N fine modular curve S of the
[higher-cycle construction](higher-arithmetic-theta-attack.md), let
$\mathscr E/S$ be the universal elliptic curve,
$U=\mathscr E\setminus\mathscr E[5]$,
$A=\mathscr E^3_S$, and $W=A\setminus A[5]$. Use its actual class
$$\Xi=\sum_{j=1}^3(i_j)_*\xi_j\in H^5_M(W,\mathbb Q(3)),\qquad
\xi_\sigma=\frac1{2100}[F_\sigma],\quad
\operatorname{div}F_\sigma=2100(\sigma-0). \tag{1.2}$$
The supports are $(x,\tau,\upsilon),(0,y,\upsilon),(0,0,z)$.
The three Tate twists and all denominators in (1.2) are inputs,
not suppressed. Pull u back to S without changing its name.

Choose a nonzero 7-torsion section $\rho$. The function
$$b_u(x)=1+(u-1)\frac{x(\sigma)-x(\rho)}{x-x(\rho)}
       \quad\text{on }\mathscr E \tag{1.3}$$
is intrinsic: all x-differences have the same frame scaling and
are unaffected by a common affine change of Weierstrass x-coordinate.
It satisfies
$$b_u(0)=1,\qquad b_u(\sigma)=u.$$
Regard b as $b_u\circ\operatorname{pr}_1$ on A. In particular its
restriction to the second and third supports in (1.2) is one.
This fiber-dependent coefficient distinguishes the two endpoints
of the first support, unlike the invariant polarization.

Here are the precise additional open and boundary data. In a short
Weierstrass frame put
$$x_u=x(\rho)-(u-1)(x(\sigma)-x(\rho)).$$
Remove from S the loci where u=1, where $x_u$ equals the
x-coordinate of any nonzero 5-torsion point, or where $x_u$
is the x-coordinate of a NONZERO 2-torsion point. Call the remaining
open $S^\circ$. These are finite algebraic sets. The conditions
are frame invariant and can be defined by the corresponding
finite torsion polynomials without choosing all individual points.
No one of these conditions holds identically: at an infinity
cusp u has leading power $q^{1-N}$ in the level-one q parameter
(with the cusp ramification retained on S), while torsion x-coordinates are
bounded in a Tate frame. Choose $\rho=1/7$ in that cusp chart;
the limiting difference $x(\sigma)-x(\rho)$ is nonzero.
For horizontal 5-torsion this follows from the distinct
$\csc^2(\pi a/5)$ and $\csc^2(\pi/7)$ limits, and for the other
5-torsion points the limit differs from the horizontal 7-torsion
limit. Thus $x_u$ has a pole, whereas all the excluded torsion
coordinates are bounded. This also proves $S^\circ$ is nonempty.

Over $S^\circ$ the zero and pole divisors of b are disjoint and
reduced. The poles on the first elliptic factor are $\rho,-\rho$;
the zeros have x-coordinate $x_u$. Each is a finite étale
degree-two divisor over the base. Write
$$D=D_+\amalg D_-\subset A_{S^\circ},\qquad
\operatorname{div}b=D_+-D_- . \tag{1.4}$$
Here each component is the indicated finite étale divisor on the
first factor times the other two COMPLETE elliptic factors.
It is smooth and proper over $S^\circ$, of relative dimension two,
and is disjoint from $A[5]$. Therefore D is wholly inside W.
This proper divisor, rather than the punctured W, will be pushed.

## 2. An actual residue–push operation with a nonzero output

Products and proper pushforwards below are those of rational higher
Chow groups. Their projection formula is Levine,
[*Bloch's higher Chow groups revisited*, Theorem 5.2 and
Corollary 5.3](https://www.numdam.org/article/AST_1994__226__235_0.pdf).
For localization and transfer signs use the Milnor-coefficient
description in Rost,
[*Chow groups with coefficients*, §§1–4](https://emis.muni.cz/journals/DMJDMV/vol-01/16.pdf),
especially the normalized residue in §1 and proper residue
compatibility in Proposition 4.4. We fix its convention
$$\partial\{\varpi,a\}=\{\bar a\},\qquad
\partial\{a,b\}=
 \left\{(-1)^{v(a)v(b)}\frac{b^{v(a)}}{a^{v(b)}}\right\}. \tag{2.1}$$
Thus the Kummer factor is placed FIRST. Reversing the factors
would negate the answer.

Define the operation in the following typed order:
$$\begin{aligned}
\{b\}\cup\Xi|_{W\setminus D}
 &\in H^6_M(W\setminus D,\mathbb Q(4))
                          =\operatorname{CH}^4(W\setminus D,2)_{\mathbb Q}\\
&\xrightarrow{\ \partial_D\ }
 H^5_M(D,\mathbb Q(3))
                          =\operatorname{CH}^3(D,1)_{\mathbb Q}\\
&\xrightarrow{\ (p_D)_*\ }
 H^1_M(S^\circ,\mathbb Q(1))
                          =\mathcal O(S^\circ)^*\otimes\mathbb Q .
\end{aligned} \tag{2.2}$$
The residue has shift (-1,-1) in cohomological degree and twist;
the proper map has relative dimension two and shift (-4,-2).
All spaces are smooth in this construction. Denote the result by
$\mathcal P_b(\Xi)$. There is no proper pushforward from W.

**[NEW] Proposition 2.1.**
$$\boxed{\mathcal P_b(\Xi)=\{u\}.} \tag{2.3}$$
In particular this support-retaining operation is nonzero and its
output extends uniquely from $S^\circ$ to the given unit on S.

*Proof.* Use the projection formula to compute the product on
each support of (1.2). On $i_1$ it is the actual Milnor symbol
$\{b_u,F_\sigma\}/2100$. On $i_2,i_3$ it is zero because b=1.
At a point of the zero or pole divisor of b, $F_\sigma$ is a unit,
and (2.1) gives the unit $F_\sigma^{\operatorname{ord}b}$.
Proper push includes its residue-field norm to the base.

Compute at the generic fiber over the field k(S). The only other
tame symbols are at $\sigma$ and zero, where the divisor of
$F_\sigma$ is nonzero. At $\sigma$ formula (2.1) gives
$b_u(\sigma)^{-2100}=u^{-2100}$, and at zero it gives one.
Weil reciprocity, in its normed tame-symbol form, therefore says
$$\prod_{P\in\operatorname{div}b_u}
 \operatorname{Norm}_{k(P)/k(S)}
     F_\sigma(P)^{\operatorname{ord}_P b_u}=u^{2100}.$$
Divide in the rational unit group by 2100 to prove (2.3) at
the generic point. Every expression in (2.2) is an actual unit
on $S^\circ$, so equality at the generic point proves equality
on that open. The right side is the previously specified unit
on S; it has zero valuation at every removed finite base point.
It therefore supplies its unique extension to S. This does not
claim that every individual divisor in (1.4) extends smoothly
across those points. $\square$

This also explains why the operation is not the already zero
polarization product. The class $\partial_D(\{b\}\cup\Xi)$ maps
to zero under the Gysin map into $H^7_M(W,\mathbb Q(4))$ by
localization. Nevertheless its proper push from D is nonzero:
its nullhomotopy in W has the explicit missing symbol
$u^{-2100}$ at the deleted partial-torsion endpoint. Pushing
that nullhomotopy through nonproper W would be invalid.

The calculation is unchanged for any coefficient with the same
values at $\sigma,0$ and the required divisor conditions.
Only an independently given rational unit has been recovered;
no real period was used to choose the coefficient. Over the
fine cover the output is exactly the pullback of u. Field/level
corestriction followed by division by its actual finite degree
therefore descends it to $\mathcal O(Y)^*\otimes\mathbb Q$.
This degree is retained as a rational denominator, not declared
an integral unit. The descended output is the explicitly known
u itself, so no unknown Galois-period descent is needed.

## 3. Canonical regulator and the exact nonconstant source interface

Use the real regulator convention of Kings–Rössler1412.2925v2:
Kummer units map to $\log|\cdot|$, and codimension-two Gysin
maps give the three twists and the (2,2) current representative
of $\Xi$. On A it is the canonical GLOBAL current class
$$G_\Xi=-\tfrac12(T_{-a}^*\mathfrak g_{A^\vee}
                            -\mathfrak g_{A^\vee}),\qquad
a=(\sigma,\tau,\upsilon).$$
No extension from W is chosen. Use the canonical conormal-wavefront
current model: its representatives and allowed exact primitives
have wavefront along the zero and translated zero sections.
Since D avoids both sections, their pullbacks to D exist and
are smooth there. The pairings below are taken in this admissible
category, not on arbitrary distribution representatives of an
unrestricted current quotient. Compact Stokes makes admissible
exact changes integrate to zero; compactness alone would not
define restriction of an arbitrary singular current.

The regulator of the residue–push (2.2) is
$$\boxed{\int_{A_s}G_\Xi\wedge
       (\delta_{D_{+,s}}-\delta_{D_{-,s}})
                         =\log|u(s)|,\qquad s\in S^\circ.} \tag{3.1}$$
Indeed naturality of the regulator under the defined pullback
to D permits using the three Gysin-pushed unit representatives
of the source's product formula. These are also admissible:
their supports meet D transversely, and their logarithmic
singularities are disjoint from D. Only $i_1$ meets D.
Their transverse intersections give precisely the
logarithm of the normed product in Proposition 2.1, including
the factor 1/2100. Its two other terms are zero. The integrand
has type (3,3) before integrating the relative threefold,
and its result is the real degree-one Kummer regulator after
the residue and twist shifts in (2.2).

At the excluded finite base points, the RESULT extends as
$\log|u|$, which is smooth there because u remains nonzero.
This proves that no atom or extra norm factor is silently
introduced in the output. At the compactified modular cusps
its logarithmic singularity and divisor are still exactly
those of $N^{-6}\Delta/\Delta_N$. We next construct a different
compact space and a cycle whose boundary cancels there; we
do not apply the abelian-scheme theorem across cusp fibers.

## 4. A compact graph-unit cycle with a proved cusp boundary

Let $V=X\times E$, a smooth projective surface over Q. The unit
obtained above gives the integral higher Chow cycle
$$\boxed{Z_u=(\Gamma_\pi,u)-(\Gamma_O,u)
                 \in\operatorname{CH}^2(X\times E,1),} \tag{4.1}$$
where $\Gamma_O=X\times\{O\}$. This is an actual sum of
function graphs; it is not the inverse evaluation of a real
regulator. Its cohomological degree and twist are
$H^3_M(X\times E,\mathbb Q(2))$ after rationalization.

*Boundary check.* On X,
$\operatorname{div}u=(N-1)([0]-[\infty])$.
The higher Chow boundary of (4.1) is therefore
$$\sum_{c\in\{0,\infty\}}\operatorname{ord}_c(u)
                   \bigl([(c,\pi(c))]-[(c,O)]\bigr)=0. \tag{4.2}$$
It cancels point by point by (1.1). No arithmetic vertical
extension of the universal threefold is claimed. The compact
graph-unit cycle is constructed separately on this actual
surface using its exact rational functions and boundary.

In the real current regulator convention, its representative is
$$G_{Z_u}=\log|u|(\delta_{\Gamma_\pi}-\delta_{\Gamma_O}). \tag{4.3}$$
The usual function-graph regulator and its Tate normalization
are described by Kerr–Lewis–Müller-Stach,
[*The Abel–Jacobi map for higher Chow groups*,
math/0409116, §§5.1–5.6](https://arxiv.org/pdf/math/0409116).
Taking the real regulator gives (4.3) with the same unit convention
used in (3.1). The current has type (1,1), and (4.2) makes
$dd^cG_{Z_u}=0$. Its logarithms on the two complete curves are
locally integrable, including their meeting points at the cusps.

Let $\omega$ be the fixed rational Néron differential on E and
$\alpha=\pi^*\omega=c_\pi2\pi ifdz$. Projection of this CURRENT
with its explicitly named de Rham coefficient gives
$$\boxed{(p_X)_*(G_{Z_u}\wedge p_E^*\omega)
                                      =\log|u|\,\alpha.} \tag{4.4}$$
This follows by the projection formula on each graph;
$\Gamma_O^*p_E^*\omega=0$. It is not an assertion that
$\log|u|\alpha$ is a closed scalar cohomology class.
Multiplying (4.4) by its fixed factor and differentiating gives
$$\eta=-\frac{i}{4\pi^2c_\pi}\log|u|\,\alpha,\qquad
d\eta=F\,d\mu. \tag{4.5}$$
Both are exactly the original forcing transgression, with
$F=y^2f\bar g$, $g=(2\pi i)^{-1}d\log u/dz$.
The two Tate twists of (4.1), the trace in (4.4), the rational
differential and its explicit $2\pi i$ comparison are distinct
operations; no scalar Betti frame is implicitly identified with
a de Rham frame. Near a cusp the product is $O(\log|q|)\alpha$,
so its boundary integral tends to zero and (4.5) has no cusp atom.

The contraction (4.4) is a formula for this specified regulator
representative. Modifying a (1,1) current by an exact Deligne
representative can alter its nonclosed scalar transgression.
Thus nonvanishing of (4.5) alone is not claimed to prove
nonvanishing of $Z_u$ in motivic cohomology.

## 5. The actual elliptic push of this cycle is rationally zero

**[NEW] Proposition 5.1.** For $q=\pi\times\operatorname{id}_E$,
$$q_*Z_u=(\Delta_E,c)-(E\times O,c),\qquad
c=\operatorname{Norm}_\pi(u)\in\{1,-1\}. \tag{5.1}$$
It is killed by two integrally and is zero rationally.

*Proof.* Proper push of a function-graph higher cycle uses the
function-field norm on its image curve. Both restrictions of q
in (4.1) have degree40 and are the map $\pi$ to the indicated
image, so both functions push to $\operatorname{Norm}_\pi(u)$.
Its divisor is zero because the two cusps both map to O.
It is therefore a constant in $\mathbb Q^*$.
Taking norms in $W_N^*u=u^{-1}$ and using $\pi W_N=[-1]\pi$
gives $c^{-1}=[-1]^*c=c$. Hence c=±1. A constant function
graph of a root of unity is torsion of the same dividing order
in the higher Chow group. This proves (5.1). $\square$

There is also an exact rational coefficient test before this push.
Let $\Pi_1^E=\Delta_E-E\times O-O\times E$ be the elliptic
degree-one Chow projector. The graph relations give
$$ (W_N\times1)^*Z_u=-(1\times[-1])_*Z_u.$$
Since $[-1]\Pi_1^E=-\Pi_1^E$, the E-degree-one projection of
$Z_u$ is Fricke EVEN on X. Therefore the Fricke-odd projector
$(1-W_N)/2$ on X kills it. In particular that specified pure
f-factor projection cannot produce the desired elliptic frame.
The current transgression (4.4) remains Fricke even and need
not vanish. Neither this parity nor the norm push removes
the original full modular radial decoration.

## 6. Retaining the radial factor: exact interface and obstruction

The surviving unit output in (2.3) gives an arithmetic source
for the complete original analytic family:
$$\int_YFJ_N(z,s)d\mu
 =\frac{i}{4\pi^2c_\pi}
       \int_Y\operatorname{cyc}_{\rm an}(\mathcal P_b(\Xi))
                       \,d_zJ_N(z,s)\wedge\alpha. \tag{6.1}$$
This is the reviewed Stokes identity with its logarithm now
recovered by an actual product–residue–proper-push operation.
All nonzero heat modes, both cusps and the pole of
$J_N=\xi(2s)(N^{2s}-1)E_\infty$ remain. The derivative kills
its constant residue, and the paired residue is zero by
$\int F=0$, rather than by omitting it from the family.
The cusp boundary vanishes because $\alpha$ decays exponentially.

This identity does not make the radial factor algebraic.
There is a specific obstruction to simply weighting (4.3)
by its second Laurent coefficient j2. On the open Y,
$$dd^c(j_2l)=l\,dd^cj_2+
 \frac{i}{2\pi}
   \left(\partial j_2\wedge\bar\partial l+
                         \partial l\wedge\bar\partial j_2\right),\qquad
l=\log|u|, \tag{6.2}$$
since $dd^cl=0$ there. With our Laplacian and
$dd^c=(i/2\pi)\partial\bar\partial$,
$$dd^cj_2=\frac{j_1+j_0}{4\pi}d\mu.$$
The residual (6.2) is not zero. At infinity,
$$j_2l=
 \frac{\pi^2(N-1)(N^2-1)}6\,y^2(\log y)^2
                         +O(y^2\log y)+O(y(\log y)^4). \tag{6.3}$$
Its Laplacian has the nonzero leading term minus twice
the displayed constant times $y^2(\log y)^2$.
Thus $j_2G_{Z_u}$ fails the closed real-Deligne regulator
condition already on the interior, where its two graph
supports are distinct. It needs a proved correcting term.

At the cusps one must not write an undefined product
$j_2\delta_{\operatorname{div}u}$. The function $j_2l$ has
a canonical locally integrable extension as a function,
but its distributional derivative is not thereby an allowed
arithmetic Chow class or a motivic nullhomotopy.
For the FULL completed second coefficient use
$$\widetilde j_2=j_2+\gamma_1j_1+\gamma_2j_0+\gamma_3R_N,\qquad
\Gamma(1+t)=1+\gamma_1t+\gamma_2t^2+\gamma_3t^3+\cdots.$$
Its gamma-pole term is retained. The lower terms do not
change the leading obstruction (6.3), though they do
belong to the unpaired current. The paired coefficient
is still exactly
$$\mathcal M=-\frac{3N(N-1)}{2\pi^3}\ell L(E,2).$$

The coordinator's separate adjoint-theta calculation proposes
a target-side test involving $\mathcal E_L''(1)$ instead
of multiplying forward theta lifts. It is not assumed in
any proof here. Formula (6.1) supplies its precise arithmetic
coefficient interface; even an analytic adjoint would still
need an arithmetic operation correcting (6.2) and a rational
comparison in the point-height determinant line.

**[GAP SKT-389]** Construct that correction/secondary arithmetic
map for the retained radial family, with the original
f-weighted pairing and target
$D_{\rm pt}\otimes B_2\otimes\mathbb Q(1)^{-2}$.
The coefficient $6N(N-1)n_E$ must remain a conclusion.
The nonconstant Kummer output and compact graph cycle are
actual constructions; they do not prove its rationality or
integral primitivity. Full BSD over Q remains unresolved.
