# Independent review of the integrated spectral comparison construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Reviewed [proof](integrated-spectral-comparison-attack.md) and
[checkpoint](integrated-spectral-comparison-checkpoint.md).

**PASS.** All nine sections are verified after the author's clarification
that the second lattice uses the transported *source* Hodge norm.
No formula changed with that clarification. The full theta integral,
joint endpoint estimates, relative analytic class, explicit rational
$K_2$ class and its regulator normalization check. No mathematical
correction remains. The final rational spectral-to-BSD comparison is
still unconstructed.

Reviewed proof SHA256:
039fce6861b8861bb5a62cc860b11a131b7075fd6afa4fe4679fee7732ab72c6.
Reviewed checkpoint SHA256:
1cbdf8e844fe19b2f3a238d6aad2ecc02b33b96f82f86b882dd9a32d9e00d197.
Subsequent PASS links/checkpoint status updates are editorial.

## 1. Lattice normalization and the global Mellin kernel

The coordinate transformation for the superlattice is integral with
determinant one when $c\equiv0\pmod N$:
$(m,n)\mapsto(am+cn/N,Nbm+dn)$.
Multiplication by $cz+d$ preserves the displayed normalized norm
because $\operatorname{Im}(\gamma z)=y/|cz+d|^2$.
This proves the required $\Gamma_0(N)$ invariance.

The second lattice has covolume $y/N$. Its norm $|w|^2/y$
is the source Hodge norm transported across the cyclic isogeny,
and is $1/N$ times its own principal normalized Hodge norm.
The proof now states this explicitly. It gives precisely
$\Theta'(z,u)=\Theta(Nz,u/N)$, with no missing N.
The central automorphism -1 merely permutes lattice vectors,
so the scalar theta kernel descends to the effective orbifold.

The determinant-one quadratic form has inverse integrally
equivalent to itself by the standard alternating matrix J.
Gaussian Poisson summation therefore gives
$\Theta(z,u)=u^{-1}\Theta(z,u^{-1})$. Substitution u/N
gives the second equation (2.2), including N/u.
The two zero vectors cancel in their difference.

Termwise Mellin integration for $\operatorname{Re}s>1$
gives the nonzero full lattice sum with factor
$\Gamma(s)/(2\pi^s)$. Decomposing vectors into positive
multiples of primitive pairs and then identifying the
two signs gives $\xi(2s)E(z,s)$. Thus the extra
$\Gamma(s)/2$ in (2.3) agrees with the author's
declared completed family; it is not an unexplained
gamma normalization. The level-oldform identity
then proves the entire kernel formula.

## 2. Both cusps and simultaneous heat endpoints

Fricke exchanges the two quadratic forms for z and Nz.
Both f and g have Fricke eigenvalue -1, so F is invariant.
The nonzero incoming term appears only at the infinity
cusp. Substituting the level-one constant terms gives
both formulas (3.2); the residues at s=1 are each
$(N-1)/2$ because $\xi(2s-1)$ has residue one-half
in the s-variable. None of the zero-mode constants
or completion derivatives is discarded.

On a cusp strip the least eigenvalue of either quadratic
form is bounded below by a constant times $1/y$.
The two-dimensional nonzero Gaussian sum is bounded by
$C(1+y/u)e^{-c u/y}$. The cusp factor F, after
including the hyperbolic measure, gives an additional
$e^{-c'y}$ times polynomial factors. Keeping half
that exponential and applying the arithmetic-geometric
mean inequality bounds the integral by
$e^{-c''\sqrt u}$ times a polynomial, which can be
absorbed by decreasing the exponent constant.
The same estimate applies at the other cusp by Fricke.

At small u the exact Poisson identity (3.5) isolates
the entire nondecaying term $(N-1)/u$.
The remaining joint integral has the claimed
$u^{-1}e^{-c/\sqrt u}$ bound. Differentiating the
Gaussians introduces only polynomial factors, which
are absorbed by the same estimates.

These estimates also give the stronger pointwise
corner control used later. At the large-heat/cusp
corner retain
$e^{-c_1y-c_2\sqrt u}$, and at the small-heat/cusp
corner retain $e^{-c_1y-c_2/\sqrt u}$.
Derivatives in r=1/y and u/(1+u) cost polynomial
powers only. Thus the pullback three-form is smooth
and flat at the simultaneous corners, not merely
integrable in one variable at a time. A finite fine
cover has finitely many cusp charts with constant
width rescalings, which do not affect this conclusion.

## 3. The paired entire Mellin transform and its log-square coefficient

The use of $\int F=0$ in defining $T_F$ and applying
Poisson summation is legitimate for these absolutely
convergent integrals. It gives
$T_F(u)=u^{-1}T_F(1/u)$ and
$K_F(u)=T_F(u/N)-T_F(u)$.
Both heat endpoints then decay rapidly, so $M_T(s)$
is entire and satisfies $M_T(s)=M_T(1-s)$.

Combining the already reviewed unfolding with the
displayed completion gives
$$
 M_T(s)=-\frac{12N^s\Gamma(s)\Gamma(s+1)}
                   {4^s\pi^{2s+1}}L(E,s)L(E,s+1)
       =-\frac{24}{\sqrt N}\Lambda(E,s)\Lambda(E,s+1).
$$
The bad-prime factor $(1+N^{-s})^{-1}$ is essential
in cancelling the level factors and has been retained.
The computation begins in a half-plane where
$N^s-1\ne0$ and then continues two entire functions.
It does not divide at a zero of that factor.

The exact analytic order two at s=1 forces both lower
moments to vanish. The t-squared coefficient is
$-3N\ell L(E,2)/\pi^3$ for $M_T(1+t)$.
Multiplication by $(N-1)/2$ gives the stated
$-3N(N-1)\ell L(E,2)/(2\pi^3)$.
Differentiating the gamma factor contributes only
vanished lower moments. The change u=Nw similarly
removes the constant and linear log terms and gives
both equalities in (4.4).

## 4. Relative class, chain and cutoff sign

On the effective fine cover the degree is 194, not
388: the generic central sign has already been
removed in passing to the analytic surface.
Its Borel-Serre compactification, crossed with the
compactified heat interval, is a connected compact
oriented three-manifold with corners.
The integral fundamental relative class is legitimate.
The downstairs pairing is its upstairs pairing
divided by 194, as stated.

The endpoint bounds in §2 make the cutoff-subtracted
top form a smooth relative form flat at the boundary.
The subtraction changes its paired mass by zero
because it is independent of z and $\int F=0$.
There is no claim that this smooth top-degree
de Rham class is rational merely because its
relative chain is integral.

The cutoff transgression has the right sign.
For the one-form eta with $d\eta=Fd\mu$ and
the stated b(u),
$$
 d(b(u)\,du\wedge\eta)=-b(u)\,du\wedge d\eta
                    =-b(u)\,Fd\mu\wedge du.
$$
This is exactly $\Omega_\chi-\Omega_{\chi'}$.
The primitive is supported away from both heat
ends and flat at every cusp, so is a relative
primitive. The finite eta-divisor correction
and the parametrization factor $c_\pi$ are
unchanged from the previously reviewed trace
construction.

## 5. Primary modular-unit and K2 inputs

The primary source for §7 was checked directly:
[Brunault, arXiv:math/0602186v1](https://arxiv.org/abs/math/0602186v1).
The temporary PDF's SHA256 is
8fd73faba5db08328c2884d9f35b79bc528145428766444f3eb8097f3b494fb7.
I inspected its text at printed pp. 85–98 and
the rendered pages 11, 88, 91, 97 and 101.
The overbars cannot safely be read from the
text extraction alone.

The thesis specifies its rational model
$X_\mu(N)$ at the bottom of printed p. 91.
Its cusp action in (3.93), p. 94, makes
the infinity cusps $P_a=[0,a]$ rational.
Normalized units with divisor $P_a-P_1$
therefore exist in the rational tensor of
the unit group. Manin-Drinfeld supplies a
positive multiple of each divisor; rational
descent and normalization of its leading
coefficient remove the constant ambiguity.
No claim that the divisor itself is
principal before rationalization is made.

Proposition 86 applies to these normalized
rational units supported on the stated
cusps. Their Milnor symbols are unramified
and define rational K2 classes on the
compact curve. The source's rational
localization sequence (3.86) is precisely
the one needed here; no extension to a
regular integral model at all primes is
asserted for the constructed class.

Proposition 80, (3.76), gives
$$
 \operatorname{div}u_\chi
 =-\frac{L(\chi,2)}{\pi^2}
                     \sum_a\bar\chi(a)P_a.
$$
The normalized leading coefficient fixes
the same equality in rational units with
complex coefficients. The Bernoulli
Fourier series and Gauss product then
give exactly the coefficient
$S_\chi S_{\bar\chi}/N$ in (7.3).
This eliminates the Dirichlet periods
from that displayed finite algebraic
coefficient formula before Galois
conjugation is used.

The source's (3.84) reads
$$
 L(f,2)L(f,\chi,1)
 =\frac{N\pi i}{\varphi(N)}\tau(\chi)
               r_X(\{u_{\psi\chi},u_{\bar\chi}\})(\omega_f).
$$
In particular the Gauss sum multiplies
the right side, and the second unit
has the conjugated character.
Solving for the regulator with
$\psi=1$ gives exactly (7.5).
Both the sign and the factor
$1/\tau(\chi)$ in that solved formula
are correct.

## 6. Exact modular symbols and coefficientwise rational descent

For r prime to N, the cusp r/N is
the infinity cusp on $X_0(N)$.
The path used in (7.6) is therefore
a closed integral homology class
after applying the rational
parametrization. Complex conjugation
sends that path to the -r path
with the same directed parameter.
The plus homology of this rectangular
elliptic curve is generated by the
primitive cycle a, so j_r is an
integer as asserted.

Pairing r and -r in the finite
character sum, and using the
oriented Fourier integral from
r/N to infinity, gives
$$
 \omega_1\sum_{r\in G}\bar\chi(r)j_r
       =-c_\pi\tau(\bar\chi)L(f,\chi,1).
$$
Together with
$\tau(\chi)\tau(\bar\chi)=N$,
this proves (7.7) from the
finite algebraic definition (7.6).
The limiting integral is a cusp
integral; absolute convergence
of the central Dirichlet series
is not assumed.

The prime-level Manin-span proof
at pp. 97–98 applies with trivial
nebentype: the excluded characters
are just the trivial one.
It gives at least one nontrivial
even character with nonzero
central-twist symbol on the
nonzero f-component. Such a
character is primitive because
N is prime. This justifies the
finite exact choice of the first
nonzero $b_\chi$.

The expression (7.3) is a finite
sum of fixed rational K2 classes
with algebraic coefficients.
Hence its conjugate under sigma
is exactly $k_{\chi^\sigma}$.
The integral-symbol formula gives
the corresponding covariance for
$b_\chi$, and every conjugate
is nonzero. This is the essential
descent argument: each regulator
identity is applied separately
at its own character embedding.
No automorphism is applied to
an unknown transcendental
special value.

## 7. Real regulator, transfer and the constructed divisor line

For rational units the real
regulator form is anti-invariant
under conjugation on the curve.
That remains true after linear
coefficient extension, with
coefficients held fixed under
the geometric involution.
Its a-period is zero. Its
small-loop integral is the
stated $2\pi$ times the
logarithm of the tame symbol,
which is zero here.

The direct calculation
$\omega\wedge d\arg w
=i\omega\wedge\bar\partial\log|w|$
and Stokes' theorem show that
the two regulator terms give
$r_E=-\frac i2\int_E\omega\wedge\eta_K$.
The bilinear relation with
$a\cdot b=1$ then gives
$r_E=-i\omega_1\mathscr R_E/2$.
This agrees visually with the
source's equation (3.110),
printed p. 101.

K2 pushforward is the norm
transfer and the regulator
obeys the projection formula.
Since $h^*\omega=c_\pi\omega_f$,
the transfer introduces that
factor and no inverse factor
of the degree $194\cdot40$.
Combining the checked
normalizations gives
$$
 \mathscr R_E(h_*k_\chi)
   =\frac{2(N-1)b_\chi}{N\pi}L(E,2).
$$
The normalized coefficient
trace (7.10), applied embedding
by embedding as verified in
§6, therefore constructs
$\beta_2\in K_2(E)\otimes\mathbb Q$
with regulator exactly
$L(E,2)/\pi$.

This is a specified rational
regulator line, not a claim
that it exhausts rational K2
or is integrally primitive.
Dualizing its one-dimensional
real regulator is valid
linear algebra in this
specified line. It is not
by itself a construction
of an arbitrary reciprocal
L-value as a period of a
new motive. The proof
retains the need to establish
the spectral factorization
through the comparison line.

## 8. Tate factors and remaining arithmetic comparison

The comparison period of
$\mathbb Q(1)^{-2}$ is
$(2\pi i)^{-2}=-1/(4\pi^2)$.
Multiplying the point
determinant frame, the
constructed K2 regulator
frame and this Tate factor
gives exactly
$-\Omega_E\operatorname{Reg}_E
L(E,2)/(4\pi^3)$.
The ratio of the spectral
mass to that frame is
$6N(N-1)n_E$. Formula
(8.3) also checks directly.
The full real period is
$2\omega_1$; its cycle is
2a and is not declared
primitive.

Rationality of the required
comparison coefficient
would imply rationality
of $n_E$, but integrality
of its integer multiple
does not by itself prove
integrality of $n_E$.
The author preserves
that separate lattice
issue. The analytic
theta class has not
been identified with
a rational arithmetic
class merely from its
convergence or integral
relative chain.

Only this review file
was written. No old
numerical certificate,
height, or prime scan
was rerun and no agent
was spawned. The
universal BSD objective
and GAP IS-389 remain
open.
