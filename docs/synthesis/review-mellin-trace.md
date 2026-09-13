# Independent review of the Mellin trace comparison

Date: 2026-09-12. Reviewer `/root/higher_period_integrality`,
GPT-6 Astra/xhigh. Own only this review file for the trace audit.

**PASS for all five sections of [the proof](mellin-trace-comparison.md).**
No mathematical correction is required. The checkpoint still describes
some proved consequences as being written or checked; root can now replace
that editorial status with this PASS verdict while preserving GAP MT-389.

Reviewed proof SHA256:
`81447f8515712231dae8abad0747db8ae68a6e34f54ad289149e2c725323ff37`.
Reviewed checkpoint SHA256:
`b78ecc50aed653a2e96670e2edfcf454a848c23526c13ded31aa017c25132998`.
Later review links and status changes are editorial.

## 1. Constants and types of pushforward

The proof deliberately uses $\alpha=\pi^*\omega=c_\pi2\pi i fdz$,
unlike the unscaled $f$-differential in parts of the earlier notes.
This factor has been retained correctly. Since
$\bar\partial\log|v|=-\pi i\bar g\,d\bar z$, direct multiplication gives
$$\alpha\wedge\bar\partial\log|v|
 =2\pi^2c_\pi f\bar g\,dz\wedge d\bar z
 =-4\pi^2i c_\pi Fd\mu.$$
Then $d(l\alpha)=-\alpha\wedge\bar\partial l$ because $\alpha$ is
holomorphic and closed. Its inverse scalar is exactly
$-i/(4\pi^2c_\pi)$ as in (2.1).

The two uses of proper pushforward have the correct degrees. A function
viewed as a degree-zero current is tested against top forms. Off the
branch locus, changing variables in $\int_Xu\,\pi^*\eta$ shows that
its pushforward is the fiber sum $\operatorname{Tr}_\pi(u)$. Limiting
branches account for ramification multiplicities in the trace of a
continuous function. A two-current is instead tested against scalar
functions; its density therefore has the corresponding inverse-Jacobian
factors when written in coordinates. No unweighted trace of a two-form
density is substituted for this operation.

Both commutations with $d$ and $dd^c$ follow directly by applying the
definitions to test forms and using that pullback commutes with these
operators. Projection with the smooth form $\omega$ gives
$\pi_*(l\pi^*\omega)=\operatorname{Tr}_\pi(l)\omega$ in degree one.
There is no division by 40 in this identity or in the mass of a pushed
two-current. The separate factor $1/40$ in the earlier point-height
formula had a different purpose: undoing pullback of both divisors.

## 2. Compactification, norm and vanishing

At a cusp, $l=O(\log|q|)$ and $\alpha$ is a holomorphic differential
on the compact coarse curve. The boundary integral of $l\alpha$ is
bounded by a positive power of the radius times $|\log|q||$, so it
vanishes. Its derivative is locally integrable and has no cusp atom.
At elliptic points, both $v$ and $\alpha$ come from the coarse curve;
$v$ is a holomorphic unit there. Thus the two-form in Proposition 2.1
is smooth in a coarse interior coordinate as well. The orbifold and
degree-194 cover conventions are consistent with this coarse current.

Off finitely many branch or divisor images, the identity
$\operatorname{Tr}_\pi(l)=\log|\operatorname{Norm}_\pi(v)|=0$ follows
by taking the logarithm of the product over the fiber. The trace is
locally integrable, so equality almost everywhere is equality of currents
globally. This does not require pointwise subtraction of divergent cusp
logarithms at $O$. The projection formula and commutation with $d$ now
prove $\pi_*(Fd\mu)=0$ exactly.

The pairing with a smooth pulled scalar vanishes by definition. A
single-log Green potential whose divisor avoids $O$ is bounded near
$O$ and has only logarithmic singularities elsewhere. Its pullback
has the same integrable singularity, multiplied by ramification order.
The forcing two-form is smooth at these interior points, so logarithmic
cutoffs converge absolutely. Applying the smooth identity to those
cutoffs, then passing to the limit, proves Corollary 2.2. In particular
the moved divisors in the second-variation note satisfy exactly the
needed support condition.

## 3. The Green solution and its constant trace

The forcing $F$ is in $L^2(Y)$, has integral zero and decays exponentially
at both cusps. The reviewed positive-Laplacian inverse on the complement
of constants therefore defines $u=GF$. The Fourier-mode argument in
Proposition 3.1 gives the necessary extra boundary information: the
zero mode solves an ordinary second-order equation with exponentially
decreasing forcing, so it is a constant plus a linear term and a decaying
part. The linear term is excluded by $L^2$. In nonzero modes the growing
homogeneous solution is also excluded. The remaining modes and their
derivatives decay, with the usual polynomial factors in a resonant mode.
Consequently $u$ is bounded at each cusp and its boundary flux tends
to zero. No compactified cusp atom is introduced by $dd^c$.

The local sign is
$$dd^cu=\frac{\partial_x^2u+\partial_y^2u}{4\pi}dx\,dy
       =-\frac1{4\pi}Fd\mu.$$
After proper pushforward its right-hand side is zero. Hence
$dd^c\operatorname{Tr}_\pi(u)=0$ as a distribution on compact $E$.
Elliptic regularity and compact connectedness make it a constant.
The proof correctly does not claim that this constant is zero: the
upstairs mean and the fiber trace use different measures.

Evaluation on a degree-zero divisor removes the constant. The divisor
pullback includes its local ramification indices, so its evaluation
against $u$ is exactly evaluation of the fiber trace. This proves (3.1).
The alternate proof is also valid: use the already normalized identity
$G\delta_{\pi^*D}=(\pi^*g_D)/(2\pi)$ up to a constant, symmetry of
the reduced Green kernel, and the vanishing in Corollary 2.2. Logarithmic
point sources have disjoint-support/evaluation interpretations as in
the reviewed second-variation construction; no $L^2$ norm of a delta
distribution is invoked.

## 4. Decorated transgression and nonzero mass

The strongest cusp term in $A_2l$ is polynomial in $y$ and $\log y$,
equivalently in $\log|q|$ and $\log|\log|q||$. It is locally integrable.
Multiplying by the holomorphic $\alpha$ makes the primitive boundary
integral tend to zero. The same growth calculation makes
$l\,dA_2\wedge\alpha$ locally integrable. At elliptic points an
orbifold-smooth invariant $A_2$ may only be Hölder in a coarse coordinate,
but its first distributional derivatives are locally integrable; the
finite uniformizer verifies the same product rule without an atom.

The direct identity
$$A_2d(l\alpha)=d(A_2l\alpha)-l\,dA_2\wedge\alpha$$
therefore holds for the compact currents under consideration. Multiplying
by $-i/(4\pi^2c_\pi)$ and pushing forward gives (4.1), including the
positive sign on its second term and the weighted trace
$\operatorname{Tr}_\pi(A_2l)$. The latter is not the logarithm of
the ordinary norm of $v$; the factors $A_2$ vary across a fiber.

Proper pushforward preserves the total mass of this two-current.
Consequently the reviewed Mellin identity gives exactly
$$M=-\frac{9\cdot389}{\pi^4\cdot390}\,\ell_E L(f,2).$$
There is no additional $c_\pi$ or degree factor in this formula,
since it is the integral of the original $A_2Fd\mu$. The earlier
certificate gives exact analytic order two, and the convergent Euler
product gives $L(f,2)>0$, so the mass is nonzero. A derivative of a
global one-current on compact $E$ has zero mass by testing against one.
Thus the second term in (4.1) carries all of this nonzero value.

Subtracting $M\mu_E$ makes the current degree zero and permits an
ordinary analytic Green solution on the compact curve. That procedure
uses the already determined scalar $M$; it does not make that scalar
rational or identify its class with an arithmetic determinant lattice.

## 5. Scope of the completed calculation

The proof establishes a stronger concrete failure than merely saying
that smooth spectral and point-charge sources are different: this
undecorated forcing and its Green solution have zero pairing with the
specified pulled point potentials and degree-zero point charges. The
argument is not applied to the distinct sources $D_wA_a$ in the
scattering Hessian.

The decorated source remains nonzero and its additional derivative term
is explicit. Constructing a rational arithmetic realization linking it
to the point determinant and the $L(f,2)$ regulator factor is still
GAP MT-389. The proof makes no unsupported assertion of algebraicity,
integrality, a uniform Sha annihilator, a BSD counterexample or full BSD.
No old computation was rerun during this review.
