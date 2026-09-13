# Independent review of the secondary Kummer theta construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file.

**PASS after the current-domain and nonzero-2-torsion precisions.**
All six sections of the [proof](secondary-kummer-theta-attack.md)
and its [checkpoint](secondary-kummer-theta-checkpoint.md) were read.
Reviewed proof SHA256:
eef3cc17f7b26ae2c134d8df6c7c2602c6f6e05c32fde9370a622ccc9c844ca9.
Reviewed checkpoint SHA256:
a7be78cd53eda56e2d87a515137a860bae46eb508fdbfc2feaf7a3d29b8424fa.
Subsequent PASS links and completed-status edits are editorial.

The constructed operation recovers the specified rational eta unit.
The compact graph cycle and its regulator transgression also exist.
The tested elliptic projection vanishes rationally, and the
weighted radial current needs a further correction. None of these
claims supplies the missing BSD comparison.

## 1. Actual coefficient, nonempty open and proper divisor

The function b_u is invariant under a common affine change of
x-coordinate and under its Hodge scaling, so the ratio in (1.3)
is a rational function without an unchosen Hodge frame.
The values at zero and sigma are exactly1 and u. Equality
x(sigma)=x(rho) would mean sigma=plus/minus rho, impossible
for nonzero points of orders5 and7.

The excluded loci ensure that zeros avoid all5-torsion,
that numerator and denominator have no common zero, and
that the double cover given by x is unramified at the zero
divisor. The author clarified that the2-torsion points here
are NONZERO; the zero section has no finite x-coordinate.
Both the zero and pole divisors are consequently reduced
finite etale degree-two divisors over the shrunken base.

The nonemptiness argument checks in a Tate coordinate.
All nonzero fixed-order torsion x-coordinates remain bounded.
For horizontal points their limits differ by the indicated
cosecant-squared constants; for the other5-torsion points
the limit is the constant term of the Tate x-series.
Choosing rho horizontal of order7 makes the limiting
difference x(sigma)-x(rho) nonzero in either case.
Since u has a pole at this cusp, x_u has a pole and
cannot identically equal an excluded bounded coordinate.
The zero sets are thus finite on the algebraic curve,
and the stated open is nonempty.

D_+ and D_- are each the corresponding finite etale
divisor times the other two COMPLETE elliptic factors.
They are smooth and proper over the base, of relative
dimension2, and miss A[5]. This is the proper map used
in the proof. There is no implicit proper push from W.

## 2. Localization orientation and exact output

I inspected
[Rost, Chow groups with coefficients](https://emis.muni.cz/journals/DMJDMV/vol-01/16.pdf),
especially printed p.328, the product/residue rules in
Section1 and proper compatibility4.4.
The rendered p.328 explicitly gives
partial{pi,u_1,...}={bar u_1,...}.
I also read
[Levine, Theorem5.2 and Corollary5.3](https://www.numdam.org/article/AST_1994__226__235_0.pdf)
for the product/projection maps and
[Kerr–Lewis–Müller-Stach, Section2](https://arxiv.org/html/math/0409116)
for the cubical orientation
sum(-1)^(i-1)(partial_i^0-partial_i^infinity).
It sends a uniformizer in degree1 to its POSITIVE divisor.

These conventions agree in the present calculation.
Where F is a unit, the localization module rule gives
partial({b} cup {F})=F^(ord b).
At sigma the first factor b extends, so the odd-degree
Leibniz sign gives b^(-ord F). Thus the Kummer-FIRST
order in (2.2) is essential and yields the stated
u^(-2100) term at sigma, with term1 at zero.
Codimension-two Gysin has even cohomological shift,
so it introduces no additional interchange sign.

The normed Weil reciprocity product therefore gives
u^2100 at the zero/pole divisor of b. Proper push
takes exactly those residue-field norms. Dividing
by2100 in the rational unit group proves (2.3).
The other two supports contribute zero because b=1.

The complete type sequence checks:
H_M^6(Q(4))=CH^4(-,2) goes by a divisor residue to
H_M^5(D,Q(3))=CH^3(D,1), and the relative-dimension-two
proper push gives H_M^1(S^circ,Q(1)).
There is no Tate-degree mismatch or suppressed Gysin shift.
Equality at the generic point is equality of actual
units on the open. The known unit u has zero valuation
at the removed finite points, so the output has its
unique stated extension. This says nothing about smooth
extension of every intermediate zero divisor.

The localization class can have zero Gysin image in W
and nonzero proper push from D: pushing its nullhomotopy
would require a push from the nonproper W. The deleted
endpoint term exhibits precisely why that step is invalid.
The subsequent finite-cover descent is rational transfer
with its degree retained, and recovers an already known
rational unit rather than an unknown period.

## 3. Canonical current intersection

The regulator normalization is the previously reviewed
Kings–Rössler convention: units map to log absolute value,
and the individual torsion formula is
-2cyc(pol_a)=T_-a^*g_(A^vee)-g_(A^vee).
This keeps the factor1/2100, the three twists and
the (2,2) type before intersection.

The initial draft's unrestricted assertion about current
classes required a repair. Compactness alone does not
define the restriction of an arbitrary exact singular
current to D. Root identified the same issue independently.
The final proof now works with the canonical conormal-
wavefront model and with admissible representatives and
exact primitives whose pullbacks exist. Its canonical
representative is smooth near D, which avoids zero and a.
The pushed unit currents are transverse to D, and their
logarithmic singularities are disjoint from it.
Natural Deligne pullback permits both admissible
computations; compact Stokes applies only after these
domain conditions have been checked.

Only the first graph support intersects D. Its intersection
is transverse and gives the logarithm of the exact norm
product already computed. Thus (3.1) is log|u|, including
the sign. The integrand has type(3,3), integrated over
the relative complex threefold. The final real function
is the Kummer Q(1) regulator after the two prescribed
degree shifts. It is not a twist-zero motivic scalar.

The output extends across the finite base shrink as the
same smooth log|u|. At cusps its logarithmic divisor
remains; the argument does not apply the abelian-scheme
current theorem across a generalized elliptic fiber.

## 4. Compact graph cycle and regulator contraction

On X times E, the two function graphs have exactly the
boundaries written in (4.2). Each cusp image is O, so
the cancellation is point by point and integral.
This produces an actual CH^2(X times E,1) cycle.
It does not assert its nonvanishing.

KLM Sections5.1–5.6 give the function-graph current
description. Taking the real normalized regulator with
cyc(u)=log|u| yields the stated
log|u|(delta_Gamma_pi-delta_Gamma_O).
The codimension-one push from the unit retains Q(2)
and type(1,1). Its dd^c is zero by the exact graph
boundary cancellation. The logarithms are locally
integrable even where the two curves meet at a cusp.

Contracting this SPECIFIED current with the named
de Rham differential and pushing gives l alpha.
The constant graph contributes zero since the
pullback of the differential along a constant map
is zero. The remaining factor is exactly
alpha=c_pi 2pi i f dz.
Direct calculation gives
bar partial l=-pi i bar g dbar z and therefore
$$
 d(l\alpha)=4\pi^2i\,c_\pi f\bar g\,dx\wedge dy .
$$
Multiplication by -i/(4pi^2c_pi) proves (4.5)
with positive Fdmu. The cusp boundary tends to zero
because the holomorphic cusp differential decays.
This contraction is not claimed to be a morphism
to closed scalar cohomology; the explicit limitation
about changing representatives is correct.

## 5. Exact norm and Fricke projections

Proper push along pi times id uses the field norm on
each of the two image curves, each map having degree40.
The pushed divisor is zero, so the norm is in Q^*.
The Fricke equation and the commuting norm square give
c^{-1}=[-1]^*c=c. Hence c=plus/minus1 and the resulting
graph cycles are killed by2 integrally.
No division by the modular degree enters this conclusion.

The other projection also checks as an identity of
rational Chow correspondences. Pulling the graphs by
Fricke changes pi to -pi and u to u^{-1}.
After the E degree-one projector, inversion acts by
-1, so the two minus signs make the class Fricke even.
The Fricke-odd projector on X consequently kills it.
The f-factor in question is in that odd eigenspace.
This concerns that specified motivic projection; it
does not annihilate the even transgression l alpha.

## 6. Radial obstruction and final scope

Stokes with eta=-i l alpha/(4pi^2c_pi) gives the positive
i/(4pi^2c_pi) in (6.1). The constant residue is killed
by the z-derivative and has zero paired integral;
it is not deleted from the unpaired family.

With dd^c=(i/2pi)partial bar partial,
dd^c f=-Delta(f)dmu/(4pi). The Laurent chain gives
Delta j_2=-(j_1+j_0), so the first formula in (6.2)
and its Laplacian normalization both check.
The leading constant term is
j_2=pi(N^2-1)y(log y)^2/12+lower terms.
Multiplying by l=2pi(N-1)y+O(1) yields exactly the
coefficient in (6.3).
The Laplacian of y^2(log y)^2 has leading term
-2y^2(log y)^2. The exact Eisenstein constant-term
expansion and decaying Fourier remainder justify
differentiating this asymptotic.

Thus the radial weighted graph current fails dd^c
closure on an interior open where its two supports
are distinct. The lower completed gamma terms do
not change that highest logarithmic term, although
they remain required in the full coefficient.
No product of a singular j_2 with the cusp divisor
distribution is used. Local integrability as a
function does not turn its distributional derivative
into a motivic or arithmetic Chow class.

All requested scope repairs have been applied.
The exact outstanding comparison is SKT-389;
no adjoint conjecture, real-metric choice, rational
frame or full BSD conclusion was assumed.

Primary local residue file inspected:
/tmp/review-secondary-rost.pdf, SHA256
a87d65d2e5b1744e00e7001fe29110c04c27c6e5e5a1aabc1d7b291e772e851f.
Its p.328 render is /tmp/review-secondary-rost328.png.
Levine and KLM were inspected through their primary
PDF/HTML above. Only this assigned review file was
written during the review; no old numerical script
was rerun.
