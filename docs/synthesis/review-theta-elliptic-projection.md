# Independent review of the theta elliptic projection and metric adjoint

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Reviewed [the construction](theta-elliptic-projection-attack.md) and
[its checkpoint](theta-elliptic-projection-checkpoint.md).

**PASS after the compactification correction.** All eight sections
pass. The original forcing is not smooth at the algebraic cusp;
the author replaced the invalid single smooth metric class by
actual smooth cutoff classes and a proved pairing limit. I
inspected the saved repair, including the optional coarse
elliptic-point cutoffs. No mathematical correction remains.

Reviewed proof SHA256:
530e386d819e2e972b132c985311e8d331b1d7cd1798f3fff35e122d0487fd91.
Reviewed checkpoint SHA256:
4e3c234b510c462c375f7a9f3b2e99377606b5f1c513afdc2c8332ba55c2b8aa.
Subsequent PASS links and checkpoint completion are editorial.
The final rational spectral-to-BSD comparison remains unproved.

## 1. Actual Fricke action and the coefficientwise point cycles

I checked [Du–Yang1702.07917v2](https://arxiv.org/pdf/1702.07917v2),
the lattice and cycle definitions (1.1)–(1.5), the quadratic
kernel (2.3)–(2.8), Proposition2.2, the metric definitions in
§4, and the actual decomposition in §8. In particular the
positive divisor is the sign-symmetric Heegner divisor in
their rational model, and the source retains effective
multiplicities 2/|Aut|. N=389 meets its squarefree hypothesis.

Direct matrix multiplication gives
\[
 W_N\begin{pmatrix}b&-a/N\\c&-b\end{pmatrix}W_N^{-1}
 =\begin{pmatrix}-b&-c/N\\a&b\end{pmatrix}.
\]
This preserves the displayed lattice and quadratic form and
sends μ_r to μ_(−r). Conjugation by W_N/√N has the same
action and lies in SL₂(R), so equivariance of the majorant
and the pairing with the positive line applies exactly.

Both the squared pairing and the quadratic exponential in
the actual kernel are even in the lattice vector. Thus its
μ and −μ components agree by a bijection of the FULL lattice
sums. The differential-form factor is unchanged by the
holomorphic Fricke action. This proves componentwise kernel
invariance, not just equality after summing the discriminant
components.

For n>0, A and −A determine the same positive real line.
Fricke conjugation and vector negation give bijections of
the relevant orbit sets and preserve stabilizers. Hence the
actual weighted CM divisors are Fricke invariant, including
imprimitive indices. No auxiliary Gross–Zagier theorem is
needed for this argument.

The actual quotient satisfies pi∘w=−pi: its differential
is zero after adding pi, and evaluating at infinity gives
pi(0)=O. That cusp image is zero by the torsion cusp relation
and the known torsion-free E(Q). Thus a Fricke invariant
generic divisor has point projection equal to its negative
after subtracting degree times the infinity cusp. The
basepoint change contributes no point.

## 2. All nonpositive arithmetic coefficients and projection scope

The projection (3.1) is well-defined. A principal arithmetic
divisor restricts to a principal generic divisor; its proper
pushforward is principal. Vertical and pure Green classes
have zero generic part. For rational coefficients it is a
map to E(Q)⊗Q, extended to real coefficients as declared.

At positive indices the Fricke argument gives zero.
At negative indices the finite part is zero or cusp-supported.
At zero the correction includes the naive cuspidal class,
the Hodge class, vertical components and a pure metric term.
The last two project to zero by definition. Generically
the Hodge bundle to the twelfth power has the rational
section Delta, with divisor supported on cusps, so its
rational point projection vanishes as well.

This covers the entire ACTUAL theta series. The degree-zero
generic class used in Du–Yang's Theorem8.4 agrees with the
projection here after applying pi; the source's other terms
are kept separate. No assertion of full arithmetic Fricke
invariance of every metric and vertical representative is
required. The result concerns this particular Fricke-negative
elliptic quotient; it does not set the entire Jacobian-valued
series or every theta variant to zero.

Corollary3.2 is then immediate: the canonical point-height
pairings vanish because the projected point classes are
zero. It does not make metric intersections vanish.

## 3. The forcing and transgression have the opposite conclusion

The constant N^(−6) in v is necessary. The two discriminant
transformation formulas give v(wz)=v(z)^(-1), without an
extra real constant. Hence l is Fricke odd. Both alpha and
g have Fricke eigenvalue −1, so F=y² f bar(g) and l alpha
are even.

The coefficient in the transgression also checks directly.
Using alpha=c_pi2πif dz, the proposed eta is
eta=l f dz/(2π). Since
bar∂l=−πi bar(g)dbar(z) and dbar(z)∧dz=2i dx∧dy,
\[
 d\eta=f\bar g\,dx\wedge dy=F\,d\mu.
\]
Thus the exact nonzero spectral pairing is not killed by
Fricke symmetrization of this input. The one-form is
generally not closed; no cohomology class is inferred
merely by tensoring its two arithmetic factors.

## 4. Actual Kummer 1-motive and the Tate/connection signs

I checked [Deligne, Théorie de Hodge III](https://www.numdam.org/item/10.1007/BF02685881.pdf),
§10.1, especially10.1.3,10.1.5 and10.1.10 for the Betti,
finite/Tate, and relative-scheme realizations. The displayed
[Z→G_m], 1↦v, is an actual 1-motive over the open rational
modular curve. It exists also where v=1. Its integral
realizations do not require an extension of v as a unit
over every bad arithmetic fiber.

The homological realization has weight-zero lattice and
weight-minus-two torus/Tate part. Inverting the torus and
fixing the lattice sends w^*K_v to K_v, and its square
is literally the identity. At finite level x↦x^(-1)
on roots negates the μ_n subgroup and respects transitions.

The Betti fiber description exp(z)=v^r gives the same map
(r,z)↦(r,−z) without choosing a global logarithm branch.
The local connection ∇e_0=−dlog(v)e_1 has horizontal
vectors e_0+log(v)e_1 and 2πi e_1. Under inversion
dlog(v) changes sign and e_1 changes sign, while e_0
is fixed; the connection and Tate comparison are preserved.
Different chart logarithms change the lift by an integral
multiple of the Tate vector, exactly as the Betti lattice
requires. No additional additive real constant is needed.

## 5. Confirmed regularity error and its precise repair

In the algebraic cusp coordinate q=e^(2πiz),
\[
 f(q)=q+O(q^2),\quad g(q)=1-N+O(q),\quad
 F_R(q)=\frac{1-N}{4\pi^2}\Re(q)(\log|q|)^2
                +O(|q|^2(\log|q|)^2).
\]
Along q=r>0 its first derivative is unbounded. Thus F_R
is not even C¹ at this cusp. The reviewed Borel–Serre
flatness in 1/y is correct but does not imply C^infty
regularity in q on the algebraic compactification.

The initial assertion that (0,2F_R) is a single smooth
Gillet–Soulé class is therefore false. It also does not
satisfy the stronger local shape adopted in Du–Yang§4:
after its log/loglog terms the remainder there is smooth
on the disk. Since F_R tends to zero, no such nonzero
leading singular term can absorb this derivative failure.

The inspected final repair takes real conjugation-invariant
smooth cutoffs chi_epsilon, zero near the cusps and one
away from shrinking cusp neighborhoods. Each
a(2chi_epsilon F_R) is an actual smooth metric class.
The intended adjoint is the LIMIT of their pairings, not
a newly asserted single class in the same arithmetic group.

The following independent bounds justify that repair.
With r=|q| and L=1+|log r|,
\[
 F_R=O(rL^2),\quad \nabla F_R=O(L^2),\quad
 dd^cF_R=O(L/r+L^2)\,dx\,dy.
\]
The last bound is locally integrable. On an epsilon-sized
cutoff annulus, |dchi|=O(epsilon^(-1)) and
|ddchi|=O(epsilon^(-2)). Integrating the dchi·dF and
F·ddchi error terms against a bounded smooth test
function gives O(epsilon L_epsilon²), tending to zero.
The omitted ddF disk integral tends to zero as well.
The boundary integral of d^cF_R is O(epsilon L_epsilon²),
so no delta atom appears at the cusp.

The added elliptic-point check also passes. In a uniformizing
coordinate t with stabilizer order e, invariance of a holomorphic
one-form a(t)dt forces a(t) to vanish to order at least e−1.
This applies to both f dz and g dz. Their hyperbolic inner
product therefore has F_R=O(|t|^(2e−2)). In the coarse
coordinate w=t^e this is O(|w|^(2−2/e)); first and second
derivatives have orders O(|w|^(1−2/e)), O(|w|^(−2/e)).
The second derivative is locally integrable for e>1.
Both cutoff error terms are O(epsilon^(2−2/e)) and the
boundary flux tends to zero. Calculating on a finite analytic
cover retains the source's effective degree and avoids any
identification of orbifold smoothness with coarse smoothness.

## 6. Complex conjugation, the metric factor two and actual measure

Let J=diag(1,−1). It preserves L and each μ_r, while
w(cz)=−Jw(z)J^(-1) for the source's positive-line vector.
The square in the kernel removes this sign. Consequently
the scalar coefficient of each q_tau^n e_mu, relative to
the positive hyperbolic density, is real and c-invariant.
The antiholomorphic pullback reverses the two-form
orientation, but its integration density is invariant.
Therefore the c-odd Im(F) has zero integral coefficientwise:
I_L(tau,F)=I_L(tau,F_R), without conjugating tau.

The exact primary formulas are Du–Yang(4.2) and(8.4):
intersection with a(h) is one-half the integral of h
against curvature, and the arithmetic theta curvature
is the Kudla–Millson kernel. Thus for every permitted
smooth cutoff class,
\[
 \langle\widehat\phi_L,a(2\chi_\epsilon F_R)\rangle_{\rm GS}
       =\int\chi_\epsilon F_R\Theta_L.
\]
The two cancels the one-half, with no additional generic
stack factor: both sides retain the same effective convention.
Absolute convergence and dominated convergence identify
the limit with I_L(tau,F).

Equations(8.3)–(8.5) also give the claimed decomposition
using the source's ACTUAL mu_GS and smooth phi_SM.
Distributional Stokes, justified by §5's cutoff bounds,
then yields
\[
 I_L(tau,F)=
 \frac{\deg\widehat\phi_L}{\deg\widehat\Delta_{\rm GS}}
       \int F_R\mu_{\rm GS}
       +\int\phi_{\rm SM}\,dd^cF_R.
\]
The sign is positive because dd^c is self-adjoint with
these vanishing boundary contributions. The smoothness of
the source objects is read on their uniformizing charts;
the derivative of F_R is the locally integrable measure
just checked, with no atom at a cusp or elliptic point.
The known integral against hyperbolic dmu cannot replace
the first term: mu_GS is the chosen smooth curvature
measure, not silently the hyperbolic measure.

## 7. Surviving arithmetic scope

The algebraic projection theorem and the cutoff metric
limit are compatible. Pure metric cutoff classes have
zero point projection, while their intersections can be
nonzero. The construction does not turn real metric data
or a convergent limit into a rational point determinant.

It computes the theta lift of F. The desired scalar mass
still includes the separate spectral coefficient j_2.
Neither multiplying two theta lifts nor dividing by a
Petersson norm constructs the missing weighted adjoint.
The fixed logarithmic 1-motive and the actual noncentral
arithmetic K2 line remain legitimate inputs; the rational
map with coefficient6N(N−1)n_E is still unconstructed.

Only this review file is written for this task. No old
numerical certificate was rerun and no agent was spawned.
