# Independent review of the second character variation

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed [the complete proof](spectral-second-variation-attack.md), §§1–7.
**PASS after a displayed-notation repair and an explicit orbifold
multiplicity clarification.** Reviewed mathematical revision SHA256:
`cdcb7128079cf50a2022b3a375d000175ce135dba55bbf1021692ceeeec3dadd`.
Subsequent review links and checkpoint changes are editorial.

This review validates the actual scattering Hessian, its finite part,
and the new formula for the point-height matrix. It does not validate
an arithmetic identification of their sources or a BSD leading term.

## 1. Gauge, operator and cusp normalization

The character convention checks directly by replacing the summation
variable γ with γγ₀: the stated Eisenstein series transforms by χ(γ₀).
Multiplication by the primitive's inverse exponential makes the family
invariant. The additional constant at the incoming cusp makes that
coefficient exactly one for every character parameter. At an outgoing
cusp the remaining factor is precisely exp(2πiε(F_b−F_a)). Its first
two derivatives give every term in (2.3), including the negative square.
For the specified 389 cusp lifts the winding integral is zero from
L(f,1)=0, so both primitive limits vanish. This is not asserted for
arbitrary lifts or other curves.

Direct differentiation of exp(2πiεF)u with the positive Laplacian gives
L₁=−4πiD_w and L₂=8π²|w|². Harmonicity removes the zeroth-order term
linear in ε. The factor one-half in the operator Taylor expansion is
correct; dots later denote derivatives, not coefficients.

The primary analytic inputs were checked in
[Petridis–Risager, arXiv:1703.09526v3](https://arxiv.org/html/1703.09526v3),
Corollary 4.5, Proposition 4.6, Lemma 5.1 and Theorems 5.2–5.4.
These supply continued resolvent recurrences, decay/weighted-space
control and the conversion of cusp phases. The proof derives its own
signs for the opposite Laplacian convention. Theorem 6.3 concerns a
Dirichlet generating function with an additional gamma quotient;
the note correctly keeps that function distinct from the scattering entry.

## 2. Resolvent and boundary calculation

For real s>1 the eigenvalue s(1−s) is negative. The positive Laplacian
has a unique bounded inverse on L² at this parameter. The differentiated
families have no incoming term and their outgoing terms are L². The
cuspidal harmonic form makes the two source expressions decay, so (3.2)
follows from the differentiated equation with no added homogeneous term.

On each truncated cusp, Green's identity for the positive Laplacian
has boundary H∂_yE−E∂_yH. Substituting the two constant terms leaves
(2s−1) times the outgoing second derivative; outgoing–outgoing terms
cancel. This verifies the sign and denominator in (3.3). The harmonic
vector field has zero divergence, so D_w is antisymmetric for the
bilinear integral. Two factors −4πi, followed by that integration by
parts, give the positive coefficient 16π². This yields (1.1) exactly.
All integrations by parts are justified first for s>1; the identities
then continue meromorphically. Complex conjugation is not inserted
into the bilinear spectral formula.

The same calculation gives the first scattering derivative from the
previously reviewed first-response integral. Its vanishing has precisely
the curve, direction and cusp normalization stated. With a=2πi and
T=exp(aε)−1, one has ddot D=a²(D_TT+D_T) and dot D=aD_T. Therefore
the T² coefficient is −ddot D/(8π²)−dot D/(4πi), as displayed.

## 3. Laurent coefficients and Hodge matrix

The constant eigenprojection of the resolvent is P₀/(t+t²). On its
orthogonal complement there is an analytic inverse near t=0, with value
G. The source D_wE_a has mean zero by the divergence calculation and
has no pole because D_w kills the constant residue. Thus the resolvent
pairing contributes no negative powers and its constant term is J_ab.
Expanding the other pairing gives R²W/t²+RC_ab/t+Q_ab. Multiplication
by 1−2t+4t² verifies all three coefficients of (4.2), including the
finite terms 2RC_ab−4R²W. No Laurent constant can be changed after
this calculation without changing its normalization.

The elliptic Hodge calculation is also exact. Conformal invariance
reduces the energies to du/ω₁ and dv/b on a rectangle of area ω₁b.
Their Gram matrix is diagonal with entries b/ω₁ and ω₁/b. Holomorphic
pullback multiplies energy by the map's degree, 40, including ramified
points. Hence the displayed determinant is 1600. The two forms have
integer periods as stated; no claim that their pullbacks form a saturated
lattice on the modular curve is needed. The degree-194 cover convention
has already been included by working on the effective orbifold.

The comparison with the earlier height certificate refutes only the
literal assignment of these columns to P,Q with the same matrix. It
does not exclude a new map or extension. No numerical height or L-value
certificate was rerun during this review.

## 4. Moving functions and exact arithmetic checks

I independently substituted the displayed P,Q,V,W,R,S,T into
y²+y=x³+x²−2x using rational arithmetic. All lie on the curve. The
first denominator line passes through V,P,−W, and the second through
V,Q,−P. Comparing their divisors with the two numerator vertical lines
proves div(u_i)=D'_i−D_i with the displayed orientation.

The h_j values at V,W are nonzero; the previously reviewed avoidance
at P,Q,O and the new distinctness from R,S,T prove the required support
disjointness. Weil reciprocity is therefore applicable without an
unrecorded common-support term. Applying it before factoring either
h_j gives the exact expression used for u_i(Z_j).

The independent calculation used Python Fraction arithmetic, with
the h_j formulas from the earlier relative-cycle proof. It verified
all four products, obtaining

    [[11337/596372, -3599/9025], [-405/1652, 6/25]].

Thus the stated rational logarithm matrix does not depend on floating
point evaluation or on fitting a canonical height. The negative entries
are correctly placed inside absolute values at the real place.

## 5. Distributional Green normalization

With the stated dd^c, a direct local coordinate calculation gives
dd^c g=−(Δg/4π)dμ. Poincaré–Lelong for the single logarithm then makes
the degree-zero Néron Green potential satisfy Δg=2πδ_D. Consequently
it is 2πGδ_D up to a constant, with local singularity −log|z| at a
simple smooth point. The symbol normalization agrees with the reviewed
relative-cycle proof: a principal divisor contributes −log|u| and
the BSD height is the negative of the complete Néron symbol.

The added orbifold clarification is necessary and correct. Coarse
multiplicity m at a point with stabilizer e becomes logarithmic
coefficient em in a uniformizer. Orbifold integration divides by e,
leaving the defined distributional mass m. Pullback to the fine cover
therefore agrees with the degree-normalized calculation.

The moved point divisors avoid the images of the cusps. Their pulled
Green functions are bounded there and logarithmic only at interior
points, hence L². A degree-zero source has mean zero. Subtracting its
mean-zero Green solution leaves an L² harmonic function, which is
constant on this connected finite-volume curve. Evaluation on the
degree-zero second divisor removes the constant. Projection along π
then contributes exactly the factor 1/40 in (6.3).

Finally, div(u)=D'−D implies g_D=g_D'+log|u| up to a constant.
The original finite symbols vanish; the moved pair need not have that
property. Keeping −log|U_ij| in (6.3) retains their principal correction.
This proves the exact sign, factor 2π/40 and all four logarithms.

## 6. Remaining scope

The same reduced inverse Laplacian now occurs in both constructions.
The spectral sources are smooth in the interior; the marked divisor
sources have nonzero atoms. This verifies the stated failure of their
literal identification as distributions. It does not imply that no
further arithmetic relation can connect their evaluations.

GAP SV-389 still asks for that actual relation, including its rational
structure, point corrections, spectral subtraction and the L(f,2)
regulator factor. Neither this review nor the common Green operator
provides rationality, integrality, a Sha bound or universal BSD.
