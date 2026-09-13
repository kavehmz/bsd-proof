# Independent review of the Poisson iterated source

Date: 2026-09-13. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file. **PASS for all six sections after the
recorded single-valued cusp-remainder precision.**

Reviewed [proof](poisson-iterated-source-attack.md) SHA256:
8755802d34789c32daa3c0d45770b16d48bc35d8a12f4fad006152a9496dbd8d.
Reviewed [checkpoint](poisson-iterated-source-checkpoint.md) SHA256:
d42ddf04fbcc1dceeed7b44b99470c207eff31fc9d01ab7bbb0fd56b2c09fc40.
Subsequent review links and completed statuses are editorial.

The finite real period formula reconstructs the previously proved
Poisson function, with its full genus correction and cusp normalization.
It is not promoted to a rational motivic morphism or a BSD proof.
No old computation or certificate was rerun. Only this review was edited.

## 1. Genuine rational source and word order

I directly read
[Looijenga2403.03748v2, Theorem1.1](https://arxiv.org/html/2403.03748v2),
with arXiv stamp23June2024, and
[Hain math/0109204v2, §2 and Theorems13.2,13.6,13.7](https://arxiv.org/html/math/0109204v2),
with arXiv stamp26October2001. The sources concern the actual
truncated path module, algebraic de Rham comparison and its
Hodge/weight filtrations. Their HTML generation dates are not
treated as new source revisions.

For length2 the relative pair has precisely the initial endpoint,
diagonal and terminal endpoint subspaces displayed in(1.5).
Looijenga identifies its homology with the truncated path module
when the endpoints differ; when they coincide its kernel is the
constant path line. Dualizing over Q gives the stated cohomology.
The explicit loop/constant-line distinction is therefore correct.

Looijenga indexes the product factors in the reverse order for
his categorical composition convention. The proof does not
import a scalar sign from that convention. Its own sampled
triangle is (gamma(s),gamma(t)) with ds wedge dt, s<=t.
Pulling back the two one-forms gives their EARLIEST-FIRST
Chen integral. Endpoint differentiation gives A_eta times xi,
and concatenation gives the same cross term used later.
There is no additional factor2.

All forms used for the variable words are algebraic and
holomorphic on the affine Y after their poles at the cusps
are removed. Their wedges on the curve vanish, so the
displayed length-two words are homotopy invariant.
The form rho is a specified complex linear combination of
rational algebraic de Rham forms, not claimed rational itself.
Products and conjugates of ordinary periods in Phi_b are
retained as real operations; the expression is not identified
with a single unmarked rational path period.

The reduced fiber u=2 is nonempty and finite because u is a
nonconstant map of proper curves. Over characteristic zero
its reduced finite algebra is étale. It lies in Y and need
not be an unramified fiber of the map u.
The relative pairs over its full Galois-stable finite scheme
give a rational family away from those endpoints.
Direct sum/restriction of scalars retains every conjugate
basepoint. No Galois automorphism is applied to an unknown
transcendental scalar to infer its rationality.

## 2. The finite de Rham representation of the conjugate periods

For g>=1, Riemann–Roch gives
dim H0(Omega((2g+1)infinity))=3g and
dim H0(O(2g infinity))=g+1.
Differentiation has the one-dimensional constant kernel,
so its image has dimension g. The displayed quotient
therefore has dimension2g.
All residues vanish because infinity is its only possible
pole. An exact differential in that pole space has a
primitive with no other pole and pole order at most2g.
This verifies the injection into algebraic de Rham cohomology
and, by dimensions, the required isomorphism.

The complete2g-by2g period matrix is invertible by de Rham–Betti
comparison. Thus c=P^(-1)bar a specifies rho with exactly
the conjugate compact periods. Its cusp periods vanish as
well, because its residues are zero.
Consequently bar A minus tilde A has zero monodromy on every
loop of Y and is single-valued.

This construction retains every genus direction. The matrix
inverse uses the known compact-curve comparison, not a
Mordell–Weil regulator or a conjectural arithmetic pairing.
The entries c_j remain comparison periods throughout.

## 3. Curvature and the full constant monodromy

Locally the two iterated integrals are holomorphic.
Writing 2lA=AL+A bar L isolates the only nonharmonic term.
Direct differentiation gives
$$
 dd^c\operatorname{Re}(A\bar L)
    =\frac{i}{4\pi}
       (\alpha\wedge\bar\theta+\theta\wedge\bar\alpha).
$$
Here theta=2pi i g(z)dz and alpha=2pi i c_pi f(z)dz.
Since dz wedge dbar z=-2i dx wedge dy,
alpha wedge bar theta=-8pi² i c_pi F dmu.
The other term has F replaced by bar F.
Their sum therefore gives EXACTLY
4pi c_pi Re(F)dmu, proving(3.2) with its sign.

For a loop followed by the variable path, earliest-first
concatenation adds a_gamma(L-log2) to I_(alpha,theta)
and bar(a_gamma)(L-log2) to I_(rho,theta).
After combining this with the increment of 2lA, the remaining
z-dependent term is a_gamma bar L-bar(a_gamma)L.
It is purely imaginary. The remaining real constant is
precisely(3.3).

For two loops the possible defect in additivity is minus
the real part of (a_gamma+bar(a_gamma)) times the theta
period of the second loop. That period is in2pi i Z, so
the defect is zero. Thus this is an additive real character,
not a character presumed zero.

## 4. Principal parts, removability and Riemann–Roch compatibility

I reconstructed the local expansion in Lemma4.1. Write
A=A_c+a(q), L=m log q+h(q), a(0)=0.
Integration by parts gives the expression stated in the proof.
Replacing Re(A_c bar L) by Re(bar(A_c)L), its singular
holomorphic differential is
(bar(A_c)-tilde A)theta, exactly(4.1).

More explicitly, after subtracting its meromorphic primitive,
the remaining nonconstant terms are real parts of
$$
 m\,a(q)\log|q|^2+a(q)\overline{h(q)}
      -m\int a(q)\frac{dq}{q}+\int h(q)\,da(q),
$$
together with a regular holomorphic primitive.
They are single-valued, bounded, and have a finite limit;
their vanishing logarithmic part is O(q log|q|).
This proves the author's added precision: no residual
argument-of-q branch is being treated by bounded harmonic
removability.

The principal-part datum is independent of the path to the
cusp, because bar(A_c) and tilde A acquire the same period.
Only finitely many local coefficients are needed: rho has
bounded pole order and theta has a simple cusp pole.

To establish compatibility, the proof uses the ALREADY
PROVED existence of q_F. The real function
G=Phi_b-4pi c_pi q_F is harmonic on the cover with constant
monodromy, so2partial G descends. After removing the
principal primitive, its cusp remainder is bounded and
single-valued, hence harmonic removability applies.
Thus2partial G is a global meromorphic differential with
exactly the specified principal parts; their residues sum
to zero.

The differential Mittag–Leffler criterion then gives xi_b.
Equivalently the principal-part exact sequence for
Omega(D) has obstruction H1(Omega), measured by total
residue; for a sufficiently large nonzero effective
cuspidal D, H1(Omega(D)) vanishes.
Solving that finite Riemann–Roch system uses only the
specified principal-part coefficients.

No value or period of q_F chooses xi_b. Its existence is
used solely to verify compatibility of independently
specified finite data. This is a formula for an existing
solution, not an independent proof of Poisson solvability.
The coefficients of xi_b are complex comparison numbers
in rational Riemann–Roch bases, not asserted algebraic.

## 5. Full compact correction and the normalized finite part

Subtracting Re integral xi_b kills the cusp monodromy
as well as its singular primitive. The remaining character
therefore descends to H1(X,Z).

The map from holomorphic differentials to their real
compact periods is injective: zero real periods make the
real part of a primitive a global harmonic function on
compact X, hence constant. Its differential is zero,
forcing the holomorphic form itself to vanish.
Both real dimensions are2g, so the map is an isomorphism.
The matrix [Re P_hol,-Im P_hol] in(5.3) is exactly its
matrix on real and imaginary coefficients.

The unique eta_b consequently kills the full remaining
character. An elliptic-only correction would not have
enough prescribed compact periods and is not substituted.
If xi_b is changed by a holomorphic form, eta_b changes
by its negative; this also checks that no arbitrary
Riemann–Roch choice survives.

The resulting U_b is single-valued and bounded. After
cancellation of poles and logarithms its cusp expansion
has a direction-independent finite limit.
The function (U_b-U_b(infinity))/(4pi c_pi) has the
curvature of q_F and the same normalization at infinity.
Their bounded harmonic difference extends across both
punctures and is constant on compact X; the infinity
normalization makes that constant zero.
This proves(5.5) and its independence claims.

The second cusp value and hyperbolic mean are inherited
from the previously proved q_F, not imposed as extra
conditions on an arbitrary source. Averaging the identical
formula over the reduced fiber gives the same function;
its denominator is rational, with no integrality claim.

## 6. Exact scope of the conclusion

The result is a finite formula using genuine length-one
and length-two algebraic path periods, their conjugates
and products, finite principal-part data, and two
explicit comparison matrices on the full compact curve.
It does not assert that all these real operations form
a rational motivic morphism, or that the result is one
rational linear combination of unmarked length-two periods.

The source pair and its Hodge/Betti realization are genuine;
the chosen real normalizations are not rational descent
merely because that source is rational.
No inverse unknown point regulator is used.
The original Petersson/theta operation remains the one
displayed in§6, with the earlier ordinary Hodge-intersection
zero retained. No new genus-two diagonal identity is assumed.

PI-389 remains open: an arithmetic comparison with the
actual marked-point/K2/Tate determinant must produce
the BSD coefficient and control its integral lattice.
The finite real formula does not establish rationality
or integrality of that coefficient. Full BSD remains
unresolved.
