# Tracing the actual Mellin source and its Green potential

Date: 2026-09-12. Owner: coordinator. The new deductions passed
[independent review](review-mellin-trace.md), including the compactified
current and Green normalizations. The objective remains full BSD over Q.

This calculation tests a specific comparison between the actual Mellin
source and the point-height Green pairing. The undecorated source has
zero trace on the elliptic curve. Retaining its spectral decoration gives
a nonzero current there, with an explicit extra derivative term. Neither
operation identifies that current with a rational arithmetic class.

## 1. Fixed inputs and normalizations

Let X=X₀(389) be the compact coarse modular curve, Y its effective
two-cusp orbifold, and π:X→E the degree-40 modular parametrization.
Both cusps map to O. Retain the nonzero rational differential factor

$$\alpha=\pi^*\omega=c_\pi\,2\pi i f(z)dz.$$

The [reviewed Mellin construction](mellin-variation-attack.md) supplies

$$v=389^{-6}\frac{\Delta(z)}{\Delta(389z)},\qquad
g(z)=E_2(z)-389E_2(389z),\qquad F=y^2f\overline g,$$
$$d\log v=2\pi i g(z)dz,\qquad
\operatorname{Norm}_\pi(v)=c\in\{1,-1\}.$$

Write l=log|v|, a locally integrable function on X, and
dμ=dxdy/y² on Y. For a function u on X, its trace is the sum over
the finite fibers, including ramification multiplicities at limiting
points. For distributions this is the proper pushforward of degree-zero
currents. Pushforward of a two-current is characterized by testing
against pulled scalar functions. The two operations have different
coordinate Jacobians but both commute with d and dd^c in their respective
current degrees. The projection formula with a smooth pulled form holds.

All integrals over Y use the effective orbifold convention; equivalently
divide the corresponding integral on the fine cover by 194. No extra
generic factor is inserted when passing to the coarse curve's currents.

## 2. Exact trace of the forcing current

**[NEW] Proposition 2.1.** As currents on the compact curves,

$$F d\mu=-\frac{i}{4\pi^2c_\pi}\,d(l\alpha),\qquad
\pi_*(F d\mu)=0.\tag{2.1}$$

*Proof.* On Y one has
bar∂l=−πi conjugate(g)dbar z. Consequently

$$\alpha\wedge\bar\partial l
=2\pi^2c_\pi f\overline g\,dz\wedge d\bar z
=-4\pi^2i c_\pi Fd\mu.$$

Since α is holomorphic and closed, d(lα)=−α∧bar∂l, proving the
first equality away from cusps. At a cusp with local coordinate q,
l=O(log|q|), while α is a holomorphic differential on X. Thus lα
is locally integrable, and its boundary integral around |q|=ε is
O(ε^e|log ε|) for some e≥1 after a uniformizer is chosen. It tends
to zero. The differentiated current has no extra cusp atom, so the
identity extends across the compactification. Elliptic points are
handled in a finite uniformizer with the usual stabilizer factor.

Away from the finite branch and divisor images, the logarithm of the
field norm is the fiber trace of l. Hence trace(l)=log|c|=0. Both
sides are locally integrable currents, so this equality holds globally.
The projection formula gives π_*(lα)=ω·trace(l)=0. Commuting proper
pushforward with d proves the second equality. No value of c_π other
than its nonvanishing is needed. ∎

**[NEW] Corollary 2.2.** For every smooth function h on E,

$$\int_Y (\pi^*h)F d\mu=0.\tag{2.2}$$

It also holds for h=g_D, the single-log Néron Green potential of a
degree-zero divisor D whose support avoids O. Indeed g_D is bounded
near O and has only logarithmic singularities elsewhere. At those
finitely many interior points F is smooth as a two-current and the
product is integrable. Cutting out small discs, or approximating the
logarithms in L¹ locally, extends (2.2). The trace equality holds off
these points and no point mass is present.

In particular the moved point divisors D'_i and Z_j of the
[reviewed second-variation construction](spectral-second-variation-attack.md)
satisfy this vanishing. This is an exact vanishing of the specified
Mellin-source/point-potential pairing, not a comparison of two numerical
approximations.

## 3. The reduced Green solution also has constant trace

Let Δ be the positive hyperbolic Laplacian on Y and G its inverse on
mean-zero L² functions. The Mellin source F lies in L² and has integral
zero, so u=GF is defined. Constants at cusps and logarithmic local
coordinates are treated on the compact coarse curve as above.

**[NEW] Proposition 3.1.** The function trace(u) is constant on E.
Consequently, for every degree-zero divisor D supported away from O,

$$\langle\delta_{\pi^*D},GF\rangle=0.\tag{3.1}$$

*Proof.* The spectral gap above the constant eigenfunction gives the
L² inverse on the mean-zero subspace. Elliptic regularity makes u
smooth in the interior. Its cusp equation has exponentially decreasing
forcing. The zero Fourier mode is a constant plus a term linear in y
and an exponentially decreasing particular solution; L² excludes the
linear term. The nonzero modes have only decreasing solutions in L².
Thus u is bounded at each cusp. Its first derivatives have no residual
boundary flux; equivalently its compactified distributional Laplacian
has no cusp point mass.

With dd^c=(i/2π)∂bar∂ the equation is

$$dd^c u=-\frac1{4\pi}F d\mu.$$

Proper pushforward and Proposition 2.1 give dd^c trace(u)=0 on the
compact E, in the distributional sense. A distribution annihilated by
the elliptic scalar Laplacian is smooth and harmonic. On a compact
connected curve it is constant. The value of this constant need not
be zero: mean zero upstairs used hyperbolic volume, whereas trace uses
fiber multiplicities. Evaluation at a degree-zero divisor removes it.
That evaluation equals the left side of (3.1) by the finite-map
projection formula, including ramification. ∎

Equivalently, the symmetric Green pairing of F with the pulled point
source is zero. One can see this directly from (2.2) and the identity
Gδ_(π*D)=(π*g_D)/(2π) up to a constant. This second proof uses only
the already reviewed point-potential formula, and avoids attributing
smoothness at the compactified cusps to the hyperbolic inverse.

The conclusion concerns this forcing F. It says nothing similar about
the different sources D_wA_a in the scattering Hessian, or about an
additional arithmetic extension joining those sources to point data.

## 4. Keeping the spectral decoration produces an extra current

Let A₂ be the u=1 second Laurent coefficient of E_∞(z,u), with
the fixed pole subtraction and both cusp expansions from the Mellin
note. Define the actual two-current on E

$$\mathcal T=\pi_*(A_2 Fd\mu),\qquad
\mathcal B=\operatorname{Tr}_\pi(A_2 l).$$

The Laurent cusp expansions grow at most polynomially in y and log y.
The cusp form in α and F makes all current products below locally
integrable on X. In a compactifying coordinate, their primitive
boundary integrals are a positive power of |q| times powers of
log|q| and log|log|q||, and hence tend to zero. Thus the product rule
does not discard a boundary atom.

**[NEW] Proposition 4.1.** The exact transgression is

$$\mathcal T=-\frac{i}{4\pi^2c_\pi}\,
 d(\omega\mathcal B)
 +\frac{i}{4\pi^2c_\pi}\,
 \pi_*(l\,dA_2\wedge\alpha).\tag{4.1}$$

Its total mass is nonzero and equals

$$M:=\int_E\mathcal T
=-\frac{9\cdot389}{\pi^4\cdot390}\,
 \ell_E L(f,2).\tag{4.2}$$

*Proof.* Multiply (2.1) by A₂ and apply
A₂d(lα)=d(A₂lα)−l dA₂∧α. Push forward and use the projection formula
π_*(A₂lα)=ω trace(A₂l). This proves (4.1), with both terms retained.
Equation (4.2) is exactly the independently reviewed Mellin coefficient
identity. Its factors are nonzero by the certified analytic order two
and the absolutely convergent positive Euler product at two. ∎

The first term of (4.1) has total mass zero on compact E. Thus the
second term carries all of M. Replacing the weighted trace with
log|Norm(v)| would erase precisely the decoration that produces this
nonzero mass. The norm computation alone cannot justify that step.

For completeness, fix a smooth probability two-form μ_E on E. The
degree-zero current T−Mμ_E has a Green solution; this is an ordinary
analytic construction by inverting the compact Laplacian on its
zero-mean subspace. Its normalization already uses the scalar M.
It does not prove that the de Rham class M[μ_E], or a determinant
comparison normalized by it, is defined over the required rational
arithmetic lattice. Assigning such a rational class would be additional
work, not a consequence of solving the analytic Poisson equation.

## 5. Precise remaining comparison

**[GAP MT-389].** Construct a rational arithmetic realization of the
decorated current (4.1), with its exact Mellin scalar and the required
map to the noncuspidal point determinant tensor the L(f,2) regulator
line. Retain the second derivative term in (4.1), both cusp conditions,
the rational differential factor, the finite point corrections and
the full real period. Its regulator should equal the current pairing
without presupposing the rationality of the BSD quotient.

The [arithmetic metric construction](arithmetic-metric-realization.md)
now realizes the current in the actual top arithmetic Chow group.
That group contains unrestricted real metric data. The remaining map
in MT-389 must preserve the specified finite rational motivic frames;
existence of an arithmetic Chow class with rational cycle coefficients
alone does not meet that requirement.

This note constructs and traces both actual currents. It proves the
vanishing of the direct undecorated comparison and isolates the
nonzero decorated term. It proves neither that the gap has no solution
nor a counterexample to BSD, a uniform Sha bound, or a leading formula.
