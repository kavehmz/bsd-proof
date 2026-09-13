# Independent review of the higher-period integrality attack

Date: 2026-09-12. Reviewed the `[NEW]` deductions in
[higher-period-integrality-attack.md](higher-period-integrality-attack.md).

**Review result: PASS for the propositions and their stated limited scope.**
No actionable error was found in the anchored Chen normalization,
translation-orbit argument, ordinary higher-cohomology vanishing, eta
second-jet formula, or real determinant-line construction. This review
checks those proofs; it does not independently audit every cited research
paper's proof.

## 1. Anchored Chen integral

On the imaginary axis, $\alpha=2\pi i f(z)\,dz=-2\pi f(iy)\,dy$ and
$\beta=dy/y$. For either orientation, the ordered simplex with $r$
identical beta letters has value $\log(y/y_0)^r/r!$. Thus
$$
I_{iy_0}^{0}(\beta^r\alpha)-I_{iy_0}^{i\infty}(\beta^r\alpha)
=\frac{2\pi}{r!}\int_0^\infty
 f(iy)\log(y/y_0)^r\,dy.
$$
The Mellin transform has the same order at one as $L(E,s)$ and the
nonvanishing prefactor takes the value $2\pi$ there. Vanishing of the
lower moments removes every term involving $\log y_0$. This proves the
sign, factorial and anchor independence in Proposition 2.1. The cusp
decay bounds dominate every finite logarithmic power at both ends,
so each anchored improper integral converges. The argument never
requires the separate integral of beta to a cusp to converge.

Lemma 2.2 also passes: identical alpha letters give the corresponding
power of the ordinary integral divided by the factorial, and alpha
is absolutely integrable at both cusps.

## 2. Translation and finite coefficient systems

The residue argument for the distinct rational poles of $dz/(z+n)$
proves linear independence. For the logarithmic jets, after division
by $f$ on its nonzero locus, the identity theorem extends the relation
to the upper half-plane. At $z=-n+i\epsilon$, the selected logarithmic
power is unbounded while every other term stays bounded. This proves
the asserted independence for every positive integer jet order and
every constant $c$.

A vector of finitely many scalar forms transforming through a constant
matrix has finite-dimensional orbit, so the contradiction in the
horizontal trivialization is valid. The note appropriately excludes
claims about other gauges, corrected cocycles, or all possible motives.
The modular-unit asymptotic in Lemma 3.2 follows by taking logarithms
of a Laurent expansion with nonzero leading coefficient. Its distinction
from Petersson norms is necessary and correctly retained.

## 3. Ordinary higher group cohomology

The Bass–Serre tree of $C_2*C_3$ is a contractible one-dimensional
complex. Its pullback action by any subgroup of $\mathrm{SL}_2(\mathbb Z)$
has finite stabilizers and preserves the two vertex types, so no edge
inversion occurs. Over a characteristic-zero field, the trivial module
of each finite stabilizer is projective by averaging. The induced
permutation modules, including arbitrary direct sums over orbits, are
therefore projective. The augmented cellular sequence is a length-one
projective resolution of the trivial module.

It follows that $H^j(\Gamma,V)=0$ for every coefficient module $V$
and every $j\ge2$. A distinguished higher cocycle may still have
nonzero values while representing zero in this ordinary cohomology.
The conclusion concerns ordinary cohomology and does not discard
relative or secondary data. Proposition 4.1 passes with this scope.

## 4. Eta correction and Fricke normalization

For root number $+1$, the weight-two Fricke eigenvalue is $-1$.
Consequently
$f(i/(Ny))=Ny^2f(iy)$ and
$\rho(-x)=\rho(x)$ for $x=\log(\sqrt N y)$.
The positive-axis eta inversion formula gives
$$
u(1/(Ny))=u(y)+\log(\sqrt N y)=u(y)+x,
$$
so $U(-x)=U(x)$ exactly. The eta product's exponential cusp growth
and the cusp form's exponential decay give a genuine holomorphic
germ $J(s)$ near zero and justify differentiating twice.

The mixed term in $\rho(U-x/2)^2$ is odd and integrable. Hence
$$
J''(0)=\int\rho U^2+\frac14\int\rho x^2.
$$
The two zero Mellin moments give
$L''(E,1)/2=\pi\int\rho x^2$. Therefore the coefficient $4\pi$
and the minus sign in the correction formula are correct. The
correction is even; symmetry alone does not make it vanish.

The Petersson-log interpretation also passes: the absolute value of
$\eta(z)\eta(Nz)$ transforms with weight one under $\Gamma_0(N)$,
and the added half logarithm of the imaginary part cancels that
transformation.

## 5. Determinant normalization and follow-up

The determinant of the real height pairing is alternating in each
point list and induces the stated isomorphism of real lines. The
sum of oriented real components integrates to the full real period;
its use preserves the factor at two. Squaring the Mordell–Weil
determinant removes the sign of an integral basis change, while
reversing the Néron differential reverses the Betti cycle too.
The rational and integral lattice-membership statements in §7 thus
have their asserted meanings.

The follow-up test is now completed in the separate
[eta correction certificate](eta-correction-certificate.md):
$110<\int\rho(x)U(x)^2\,dx<111$ for 389a1. It uses the even
Fricke fold, exact Fourier coefficients, the convergent eta-product
logarithm, and explicit errors, with the normalization checked here.
This additional calculation refutes the uncorrected second-jet
shortcut on the actual curve; the analytic review itself did not
assume that nonvanishing.
