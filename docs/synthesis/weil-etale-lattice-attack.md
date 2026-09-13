# Testing an integral Weil–étale lattice on the actual arithmetic surface

Date: 2026-09-12. Owner: coordinator. The objective remains full BSD over Q.
The `[NEW]` deductions below passed [independent review](review-weil-etale-lattice.md). This note constructs
the regular model and its Picard lattice explicitly, then tests the proposed
passage to a perfect integral complex. It does not assert Brauer finiteness
or the BSD leading-term equality.

## 1. The exact integral model

Let $\mathcal E\subset\mathbb P^2_{\mathbb Z}$ be
$$Y^2Z+YZ^2=X^3+X^2Z-2XZ^2.$$
Its generic fiber is 389a1, with section $O=[0:1:0]$. On the affine chart
write $F(x,y)=y^2+y-x^3-x^2+2x$.

**[NEW, explicit model calculation] Proposition 1.1.** This is a regular,
proper, flat arithmetic surface. Every fiber is geometrically integral. Its
only singular fiber is a split nodal cubic at389, with multiplicity one.

*Proof.* The integral invariants are
$$\Delta=389,\qquad c_4=112,\qquad c_6=-856.$$
The discriminant is a unit at all other primes, so those fibers are smooth
genus-one curves. At infinity the derivative with respect to Z is a unit
at O. Modulo389 the only affine singular point is $(299,194)$; it is
obtained by solving $F=F_x=F_y=0$.

Set $x=299+u$, $y=194+v$. At the integer lift,
$$F(299,194)=-389\cdot68848,\qquad -68848\equiv5\pmod{389}.$$
In the regular ambient local ring with maximal ideal $(389,u,v)$, the
linear part of F modulo its square is consequently a nonzero multiple
of389. The hypersurface local ring is regular. At every other point,
smoothness of the fiber gives regularity of the total space.

The tangent cone of the special fiber is $v^2-120u^2$ over $\mathbb F_{389}$;
its distinct slopes are148 and241. It is a split node. In translated
coordinates the cubic is
$$v^2=u^2(u+120),$$
so its normalization has parameter t, with $u=t^2-120$ and $v=tu$.
This proves geometric integrality and describes the two rational points
above the node. Properness follows from projectivity. For flatness, let G
be the homogeneous cubic. Its reduction is nonzero at every prime p. If
ph=Gk in Z[X,Y,Z], reduction modulo p forces k=pk_1, hence h=Gk_1.
Thus Z[X,Y,Z]/(G) is torsion-free over Z; so are the localized degree-zero
rings of its Proj, and these are flat over Z.
The displayed fiber is reduced and irreducible, hence has multiplicity one.
$\square$

The [integer check](../../compute/scripts/arithmetic_surface_check.py)
verifies the node, its tangent slopes, and the regularity residue. It also
counts exactly389 projective points on the singular fiber over
$\mathbb F_{389}$. These computations are in
[`arithmetic_surface_389a1.json`](../../compute/data/arithmetic_surface_389a1.json).

## 2. The Picard lattice exists without finiteness of Sha

**[NEW] Proposition 2.1.** Restriction gives
$$\operatorname{Pic}(\mathcal E)\simeq\operatorname{Pic}(E)
\simeq\mathbb Z\oplus E(\mathbb Q)\simeq\mathbb Z^3.$$
Also $\Gamma(\mathcal E,\mathcal O)^\times=\{\pm1\}$.

*Proof.* A divisor on the generic fiber extends by closure to a Weil divisor
on the regular surface, hence to a Cartier divisor. Thus restriction on
Picard groups is surjective. A line bundle which is generically trivial is
represented by a vertical divisor. Each fiber has just one component, of
multiplicity one, so every vertical divisor is an integral combination of
full fibers. The fiber at p is the principal divisor of p. This proves
injectivity.

The rational point O splits the degree map on $\operatorname{Pic}(E)$.
The usual degree-zero identification with E is defined over Q; the rational
point also kills the obstruction to representing a rational divisor class
by a line bundle. The [earlier rank and basis certificates](bsd-archimedean-bound.md)
give $E(\mathbb Q)\simeq\mathbb Z^2$ with no torsion.

A global regular function restricts to a constant in Q on the proper,
geometrically integral generic fiber. It is integral at every prime by
restriction along O, so is an integer. Conversely every integer is global.
This proves the unit assertion. $\square$

Thus there really is a fixed, finitely generated integral Picard module;
its construction is not the missing part of this approach. The obstruction
appears one cohomological degree later.

## 3. The arithmetic Brauer group, including the real place

The [Hecke–Brauer proof](hecke-brauer-annihilator-attack.md) verifies the
following source inputs without any Sha-finiteness assumption: for a proper
regular model over Z, its Brauer group injects into the generic-fiber Brauer
group and consists of classes trivial on the generic curve over every finite
completion; with a rational section, the normalized generic Brauer group is
$H^1(\mathbb Q,E)$. Adding the real local condition identifies the kernel
with $\operatorname{Sha}(E/\mathbb Q)$.

For this model the real local condition is automatic.

**[NEW] Proposition 3.1.** There is a natural isomorphism
$$\operatorname{Br}(\mathcal E)\simeq\operatorname{Sha}(E/\mathbb Q).$$

*Proof.* The section O makes every integral Brauer class normalized, since
$\operatorname{Br}(\mathbb Z)=0$. Let $Q=(0,-1)$, another section over Z.
The real roots of $4x^3+4x^2-8x+1$ lie in $(-3,-1)$, $(0,1/4)$,
and $(1/2,1)$. Consequently Q lies on the nonidentity real component,
whereas O is on the identity component. Both section evaluations of an
integral Brauer class are zero in $\operatorname{Br}(\mathbb Z)$.

For a normalized class on $E_{\mathbb R}$, evaluation at Q equals the
local Tate pairing of its $H^1(\mathbb R,E)$ class with Q. This pairing is
perfect against $E(\mathbb R)/N E(\mathbb C)$. The norm image is exactly
$E(\mathbb R)^0$: it is connected and contains $2E(\mathbb R)^0$, which
is all of that circle. Thus Q generates the norm quotient of order two.
Its zero evaluation makes the normalized real Brauer class zero. The
constant real class is also zero by evaluation at O.

All finite local conditions already hold for an integral Brauer class, so
it gives a Sha class. Conversely a Sha class, viewed as a normalized Brauer
class of E, is trivial at all finite completions and therefore extends to
$\mathcal E$ by the stated regular-model theorem. $\square$

The local pairing and Brauer-evaluation identity, with their primary
references and the full model theorem, are checked in the linked
Hecke–Brauer note. The proof above does not turn pointwise zero evaluations
at all places into a global Brauer vanishing statement; it uses them only
to identify the still-unknown group with Sha.

## 4. The finite-generation hypothesis contains exactly this missing group

**[THEOREM, weight-one motivic complex]** On a regular scheme,
$\mathbb Z(1)\simeq\mathbb G_m[-1]$ in the étale topology. Thus here
$$
H^1_{\mathrm{et}}(\mathcal E,\mathbb Z(1))=\{\pm1\},\qquad
H^2_{\mathrm{et}}(\mathcal E,\mathbb Z(1))=\mathbb Z^3,\qquad
H^3_{\mathrm{et}}(\mathcal E,\mathbb Z(1))=\operatorname{Br}(\mathcal E).
$$
The last group is torsion; regularity embeds it in the function-field
Brauer group. Lower degrees vanish.

**[NEW] Corollary 4.1.** The condition that these étale motivic cohomology
groups be finitely generated in degrees at most three is equivalent to
finiteness of $\operatorname{Sha}(389a1)$.

*Proof.* The first two groups were computed unconditionally. A torsion
abelian group is finitely generated if and only if it is finite. Apply
Proposition 3.1 to the third group. $\square$

This is the precise hypothesis $\mathbf L(\mathcal E_{\mathrm{et}},1)$ in
Flach–Morin's construction: [Conjecture3.2 and Lemma3.3, pp.18–19 of the
author PDF](https://www.math.u-bordeaux.fr/~bmorin/flach-morin-169.pdf),
[arXiv:1605.01277](https://arxiv.org/abs/1605.01277).
Lemma3.3 accounts for the finite two-primary difference from the
Artin–Verdier compactification. In the self-dual case dimension2, n=1,
the dual finite-generation hypothesis is the same one.

The independent arithmetic-surface treatment states this reduction
explicitly: [Flach–Siebel, arXiv:1909.07465v1, §4](https://arxiv.org/html/1909.07465)
reduces that hypothesis to finite Brauer group and the known finite
generation of Pic. Its introduction distinguishes the conjectural
special-value identity from the theorem $C(\mathcal X,1)=1$ about the
correction factor. The preprint's comparison also records an intersection-
pairing compatibility; no stronger scope is inferred here from its abstract.

In particular, Flach–Morin Proposition3.4's finite self-dual middle group
is not an independent proof of finite Brauer group. It is in the section
assuming the finite-generation hypotheses, and its proof uses them. The
exact place where the proposed automatic perfect-complex argument would
be circular is now the explicit group in Corollary4.1.

## 5. The arithmetic zeta function is also explicit

**[NEW] Proposition 5.1.** As meromorphic functions,
$$\zeta(\mathcal E,s)=\frac{\zeta(s)\zeta(s-1)}{L(E,s)}.$$
It has a pole of order three at one, with leading coefficient
$$\lim_{s\to1}(s-1)^3\zeta(\mathcal E,s)=-\frac{1}{2\ell_E},
\qquad\ell_E=L''(E,1)/2.$$

*Proof.* At a good prime q, the fiber zeta factor is
$P_q(q^{-s})/((1-q^{-s})(1-q^{1-s}))$, where
$L_q(E,s)=P_q(q^{-s})^{-1}$. At389, normalization of the split nodal cubic
replaces its node by two rational points. Therefore it has $389^m$ points
over $\mathbb F_{389^m}$ and its zeta factor is $(1-389^{1-s})^{-1}$.
This also equals the displayed quotient of local factors, since the
split multiplicative elliptic factor is $(1-389^{-s})^{-1}$.

Multiplying in the absolutely convergent half-plane $\Re s>2$ proves the
identity there. Modularity supplies the meromorphic continuation of the
right side. The already certified double zero of L(E,s), the residue one
of zeta at one, and $\zeta(0)=-1/2$ give the pole and coefficient. $\square$

Thus in this example both the Picard rank and the analytic pole order
are unconditionally known. They do not establish finite H^3 or the
integral leading-term lattice. The script records an exact interval for
the last coefficient from the existing rigorous interval for $\ell_E$;
it does not impose a rational value on that coefficient.

## 6. A direct attempt using all finite coefficients

Finite-coefficient duality and finite Selmer groups are tempting inputs
for proving the missing finite generation by passage to a limit. The
Tate-module sequence shows exactly which information such a passage keeps.

**[NEW] Lemma 6.1.** Define the compact p-adic Selmer module by
$\mathcal S_p=\varprojlim_n\operatorname{Sel}_{p^n}(E)$, using multiplication
by p on geometric torsion. There is an exact sequence
$$0\to E(\mathbb Q)\otimes\mathbb Z_p\to\mathcal S_p
\to T_p\operatorname{Sha}(E)\to0.$$
If $\operatorname{Sha}(E)[p^\infty]$ is finite, the last term is zero.

*Proof.* Take inverse limits of the finite Kummer sequences. The
Mordell–Weil quotients have surjective transition maps, so their first
derived inverse limit vanishes. The Sha transition maps are multiplication
by p, giving its Tate module. For a finite p-group this inverse limit is
zero: each fixed coordinate is the image of arbitrarily high p-powers.
$\square$

Even equality $\mathcal S_p=E(\mathbb Q)\otimes\mathbb Z_p$ at every p
would not prove full Sha finiteness. The torsion group
$\bigoplus_p(\mathbb Z/p\mathbb Z)^2$ has finite n-torsion for every n and
zero Tate module at every p, but is infinite. It also has compatible
nondegenerate alternating pairings on every finite prime-support piece,
using $(ab'-ba')/p$ on each summand. Its induced map to its compact dual
has dense proper image. Thus finite-level perfection must not be promoted
to a perfect self-duality of the whole discrete group without proving the
needed global finiteness/closedness property.

This is a limit calculation, not an elliptic-curve counterexample. It
explains why the known finite-coefficient input cannot simply be substituted
for Corollary4.1. The full integral complex must retain the degree-three
torsion, not discard it by taking Tate modules or rational cohomology.

## 7. Remaining construction problem

**[GAP WE-389].** Prove finite generation of
$H^3_{\mathrm{et}}(\mathcal E,\mathbb Z(1))$, or construct a perfect integral
comparison retaining that full group and prove its compatibility with the
arithmetic model. The group must not first be replaced by its rationalization,
its Tate modules, or a finite truncation selected in advance.

This is precisely full Sha finiteness for the test curve, not a newly
weakened target. The actual model, Picard lattice, and zeta factorization
are completed inputs. A special-value comparison with the period and full
height determinant is still required after finiteness, and a solution for
this model alone would still leave the universal BSD objective.
