# Independent review of the CM derived-unit construction

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review. The parent objective remains full BSD over Q.
No old numerical certificate or unit scan was rerun.

**PASS after the recorded source-convention clarifications.**
Reviewed [the full construction](cm-derived-unit-attack.md) and its checkpoint.
Reviewed mathematical revision:
62458037802eb65204f90575d3b7c7194052f962f2ca4f9d196c3685a692ddb1.
Subsequent bibliography, review-link and checkpoint updates are editorial.
The applied clarifications identify the one chosen plus-branch class
with Kato's zeta submodule in the height-one inequality and explicitly
match the CM type selected by the coefficient rho. The added Frobenius
table resolves the coordinator's source-convention concern. No formula
or local coefficient changed as a result of that audit.

## 1. The finite elliptic units really are the stated tower

I checked [Schmitt's primary paper](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf),
Definitions2.1–2.7 and3.12, Proposition3.13, and the norm calculations
on printedpp47–49. K=Q(i) has class number one, the primes above p
are distinct and ordinary, and the conductor modulus has at least two
prime divisors and injects the roots of unity. These satisfy the
source conditions. The prime-power conductor theorem is not used.

For the rational ideal (a), discriminant homogeneity gives
$\Delta(a^{-1}\Gamma)=a^{12}\Delta(\Gamma)$.
Pairing U and -U changes the twelfth power of the half-torsion product
into the exponent-minus-six product over all nonzero torsion points.
This proves the displayed rational function and its divisor. On the
actual model x is the Weierstrass elliptic function for the Néron
parameter, and the algebraic discriminant has the stated value.

The source's Definition3.12 is exactly the norm from the full ray
field to the division field evaluated at
$\Omega_\infty/(f_0\pi^n\bar\pi^k)$. It is a norm-compatible system
of global units. The stated distinction between repeated primes
and a newly removed prime, and the inverse Frobenius in the latter
factor, are correct.

## 2. Finite-level twisting, smoothing and integral coefficients

The tensor character is correct:
$$\rho=\Psi\chi_{\rm cyc}^{-1}=(\Psi^c)^{-1}.$$
The division field at sufficiently high level trivializes the Tate
characters and the roots of unity modulo p^m. It contains K_n once
r>=n+1. The tensor in (5) is therefore defined, and the projection
formula for corestriction makes its value independent of higher r.
Reduction in m and norm compatibility in n give the claimed inverse
limit. The two-variable twist precedes cyclotomic specialization.

The action on a twisted group-ring factor is
$$\operatorname{Tw}_\rho(\sigma u)
 =\rho(\sigma)^{-1}\sigma\operatorname{Tw}_\rho(u).$$
Thus both the smoothing factor and the newly introduced prime factor
have the indicated inverse convention. The integral CM idempotents
and complex conjugation identify the induced representation with
T_pE; Shapiro itself does not multiply the class by two.

Schmitt's actual Coleman formula is
$12(\sigma_a-N(a))\lambda$. Its restriction to the elliptic-unit
module is injective by Proposition3.13, so the auxiliary-choice
independence argument is valid. For a=5 the possible augmentation
factors involve only2,3,5; at p=5 the choice a=7 is allowed and is
a unit. Both integers are prime to the conductor and the other
required primes. Division by the smoothing factor is thus an
integral operation in the selected cyclotomic Iwasawa algebra.

## 3. Kato's exact normalization and the Betti factor two

I read the saved full primary Kato PDF/text at
Proposition1.3, Theorems12.4–12.5, §§15.4–15.17 and Theorem16.6.
The PDF has SHA256
3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d.
Its origin is [Kato, Astérisque295(2004)](https://www.numdam.org/article/AST_2004__295__117_0.pdf).
I additionally inspected the rendered original Proposition1.3 formula
because the extracted formula is not reliably readable.

Kato's divisor-normalized function has the stated twelfth power.
In the q-product of Proposition1.3(3), its twelfth-power leading term
is $a^{-12}\Delta^{a^2-1}z^{12(a^2-1)}$.
The divisor and leading coefficient therefore identify its twelfth
power with the Schmitt function exactly. Taking twelve removes any
root-of-unity sign in the unpowered function.

Kato§15.6 divides by $N(a)-\sigma_a$, opposite to Schmitt.
Consequently the normalized Kato class is the negative of the
Schmitt-normalized class in this common coefficient convention.
The factor12 is retained rather than absorbed into an unspecified unit.

The Betti choice also checks directly. For the fixed rotated square
lattice, conjugation sends b to -ib and ib to -b. Hence
$$\gamma_E^+=\frac{b^\vee-(ib)^\vee}{2},\qquad
\operatorname{per}(\omega)^+=\Omega_E\gamma_E^+.$$
Since conjugation interchanges the CM idempotents,
$$e^+\operatorname{pr}_\rho e^+=\tfrac12e^+.$$
Thus $2\operatorname{pr}_\rho\gamma_E^+$ has exactly the required
plus part, with no remaining half-period. Its coefficients are
p-integral for the allowed odd primes. Its induced minus part is
nonzero as well, so the period normalization can be placed in
Kato's two-sign convention before choosing the cyclotomic branch.

The differential-period comparison in15.11, the specialization
formula15.12.2 and identification15.16.1 fix the rational zeta
element. The weight-two elliptic-curve setting avoids the
higher-weight motive-identification warning after15.11.
For the opposite CM type, the diagonal tower can be conjugated
explicitly: conjugation sends Omega_infinity to -i Omega_infinity
and f0 to i f0, hence sends R_(r,r) to -R_(r,r).
The rational theta function is even, so the diagonal units are fixed.
Conjugation exchanges the two coefficient lines, and their induced
plus Betti coefficient is the same. The author now states this
type/opposite-prime identification explicitly.
The ordinary Coleman translation is also exactly BKS Theorem6.10,
which states Kato16.6 in the T_pE convention. The Néron period and
the selected plus coefficient, rather than an arbitrary modular-symbol
lattice generator, fix the normalization here.

The bad Euler factors are one for this CM curve's additive bad
primes. At the trivial character the displayed p-factor simplifies
to $(1-\alpha^{-1})^2$. Thus the exact Coleman image is the MTT
series in the predecessor note, rather than an equality up to an
Iwasawa unit. The already reviewed Katz coefficient and CM period
in (9c) are retained as inputs; no complex rationality follows.

## 4. Height-one divisibility and its integral saturation

Kato12.4 gives rank-one, torsion-free H1 and torsion H2.
The direction of12.5(3)'s length inequality is the one used in the
note. Its possible local correction requires failure of potentially
good reduction at p and is absent here.

At the augmentation localization p is inverted. Rubin's condition
15.2(a) therefore suffices; no condition on the p-part of the
finite ray-class Galois group is required for this inequality.
Moreover Q(i) is not contained in Q(mu_p-infinity) for p>=5,
since the former ramifies at2. Kato15.13–15.17's indicated case
therefore applies.

Kato's inequality is initially written with the module Z(f)
generated by all Betti coefficients. The source conjugation relation
in12.5(1), after Tate twist1, selects the plus Betti line on the
chosen trivial finite cyclotomic branch. Any nonzero vector of that
one-dimensional Q_p line generates the same module after
height-one localization. Thus the individual normalized class has
the stated inequality. This clarification is now explicitly included
in the author's theorem paragraph.

The cohomological proof then works without finite Sha. Using finite
p-power coefficients and a cofinal sequence of finite layers gives
finite cohomology groups and the Mittag–Leffler condition. With
odd-p global cohomological dimension two, the Iwasawa complex has
no H3. Derived specialization consequently gives H2/T=H2_global.

The global Euler characteristic of V_pE is -1. There is no global
H0, and the two independent rational-point Kummer classes give
dimension H1>=2. Thus dimension H2>=1. Nakayama at the augmentation
prime gives positive T-primary length; the source inequality makes
the actual class T-divisible there.

The upgrade to integral divisibility is valid and necessary:
H1_Iw/T injects into H1_global(T_pE), and the latter is Z_p-torsion
free since E(Q)[p-infinity]=0. A denominator outside(T) acts on
this quotient by its nonzero augmentation in Z_p. It cannot kill a
nonzero class. Thus the integral class is actually in T H1_Iw.
H0_global=0 also makes multiplication by T injective, so the
division is unique. No residual-image hypothesis or full Selmer
corank statement is hidden in this step.

## 5. The full Selmer class and Bockstein sign

The cochain calculation with inverse cyclotomic action gives
$-c_\gamma(g)\,g f(h)T$ exactly. The chosen height uses minus the
connecting map, matching BKS's convention. The local cone terms
are functorial under the same deformation.

For the derived class w0, the Coleman augmentation vanishes because
L_p/T has zero constant coefficient. Its interpolation factor is
nonzero, so the dual exponential vanishes and w0 lies in the finite
local condition at p. At every other finite place, H1(Q_l,V_pE)=0:
local H0 is zero, local duality makes H2 zero, and the l≠p Euler
characteristic is zero. The odd-p real term vanishes as well.
This proves full Selmer membership without identifying Selmer with
Mordell–Weil.

The canonical-height restriction is compatible with
[Besser, Theorem1.1](https://arxiv.org/html/math/0209006v1), using
the same global logarithm and ordinary complement. These choices
were fixed in the preceding reviewed CM notes.
The factor g_p^-1 follows from gamma-1 mapping to log_p(1+p),
and the restricted determinant is Reg_p/g_p² times T².
It is not the determinant of the entire Selmer group.

## 6. Rubin's identity with all extra Selmer directions retained

I inspected BKS's actual diagram(6.4.1), proof of Theorem6.11 and
Lemma6.14 in [arXiv1910.07404v2](https://arxiv.org/pdf/1910.07404).
Its diagram requires y0 in the full Selmer group and H0(F^-V)=0.
The latter follows at good ordinary p from the nonexceptional unit
root. Compatibility of the two connecting maps gives
$\beta(y_0)=\delta(D(y))$ with the declared minus-Bockstein sign.

The source next identifies H2_Sel with the dual of H1_Sel and then,
under its broader standing hypotheses, with the Mordell–Weil dual.
Only the final identification is unnecessary here. Keeping the
full Selmer dual gives the same cup-product equality against rational
points and validates the argument as written.

Howard's [Theorem4.5](https://arxiv.org/html/1202.6343v1) corroborates
this full-Selmer scope. Its ordinary, ramified-above-p and finitely
decomposed-bad-prime hypotheses hold for Q_infinity/Q. It imposes
the local singular divisibility condition, not finite Sha. The
direct BKS cone calculation remains the normalization reference.

**Independent Frobenius audit.** Let F be absolute crystalline
Frobenius on ordinary H1_dR, and put eta=x omega. The primary
[Mazur–Stein–Tate paper, §3.2](https://wstein.org/papers/pheight/pheight.pdf)
states that F(omega) lies in p H1 and that the unit-root line is
transverse to omega. CM makes both omega and eta eigenlines. Therefore
the exact table is

| Line | F | phi=F/p |
|---|---|---|
| omega, the Hodge line | beta | alpha^-1 |
| eta=x omega, the ordinary complement | alpha | beta^-1 |

BKS uses the last column. Its nu is consequently on the eta line,
so [omega,nu]=1 is possible and correct. This does not exchange
the finite and singular local conditions.

The inspected SW PDF defines phi=F/p in §3.5 but prints eigenvalue
alpha^-1 for the canonical complement in §4.1. With its stated
unit-root label these two passages are inconsistent. The latter
reciprocal label must not be substituted into BKS6.9. MST's primary
unit-root construction gives eta and hence E2=0 directly, preserving
the preceding CM sigma/height result. The displayed linear-height
signs in the same SW paragraph are also inconsistent when a is
nonzero, but this CM case has a=0. No local Coleman factor is altered.
Here MST is used for its Frobenius/unit-root description, not to
import its separate height normalization involving (1/p)log_p.
The height normalization remains the one fixed by BKS, Besser and
the predecessor's chosen global logarithm.

For the local vector, the source gives
$$
\delta_0=p^{-1}\bigl(-\varphi^{-1}
 +(p-1)(1-\varphi)^{-1}\bigr)\nu
 =\frac{1-\alpha^{-1}}{1-\beta^{-1}}\nu.
$$
This uses Tr(zeta_p)=-1 and phi(nu)=beta^-1 nu.
The normalized pairing [omega,nu]=1 then gives
$x=k_\alpha\log_\omega(x)\exp(\delta_0)$.
Lemma6.14 and the coefficient of L_p/T prove (20), including
its T² target and its exact sign. The argument permits the derived
class to vanish.

## 7. The projection and the coefficient p/(2#E(Fp))

Write S_p for the full rational Selmer space and W_p for its known
two-dimensional Mordell–Weil subspace. If H_p is nonsingular, its
restriction defines a canonical projection S_p→W_p by the height
pairings against P,Q. No nondegeneracy on the complementary space
is needed. The difference pairs to zero with W_p; it is not proved zero.

The cofactor calculation is exact:
$H\operatorname{adj}(H)l=(\det H)l$ gives the stated Bockstein
vector and
$$
\operatorname{pr}_{W_p}(\kappa_p)
=\frac{g_p^2 k_\alpha c_2}{\operatorname{Reg}_p}R_{p,\omega}.
$$
The elliptic logarithm of a non-torsion rational point cannot vanish:
its local kernel is torsion, and equality to a torsion point over
Q_p would already be a rational torsion relation.
Thus the Bockstein map's one-dimensional image is nonzero under
Reg_p≠0, and the inverse is taken precisely on that image.

Finally
$$
k_\alpha e_p=(1-\alpha^{-1})(1-\beta^{-1})
=\frac{p+1-a_p}{p}=\frac{\#E(\mathbb F_p)}p.
$$
Together with $c_2=c_{\rm cmp,p}M_p/(2g_p^2)$ this proves
$$
\frac{p}{2\#E(\mathbb F_p)}
 \frac{g_p^2k_\alpha c_2}{\operatorname{Reg}_p}
=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}.
$$
The coefficient in (22) is correct. Nondegeneracy is used only
for this inverse construction, not for the earlier class or height
identity. Extra Tate-module Sha directions have not been suppressed.

## 8. Rational augmentation and the unresolved global frame

For a finite cyclic p-power group, writing t=gamma-1 gives
I/I²=Z/p^n and compatible inverse limit Z_p.
Over Q the complementary augmentation idempotent makes I²=I.
All positive rational graded pieces therefore vanish. This is an
exact test of rationalizing the specified finite-level augmentation
construction before taking its inverse limit, not a claim that all
higher motivic descent is impossible.

The construction produces separate p-adic determinant realizations
where the stated inverse is defined. It does not prove that their
scalars are localizations of one rational coefficient, or that
such a coefficient has the required complex realization.
No Rubin, Schneider, or CM theorem is used to assume the complex
BSD quotient rational. The CM-Derived gap is preserved.

The plus-branch Z(f), conjugate-CM-type and Frobenius clarifications
have been inspected in the reviewed mathematical revision. No
mathematical correction remains outstanding. The linked MST author
version has different pagination from the published version; source
references here use its section number and do not conflate those
page ranges. The integral/rational descent and complex BSD comparison
remain the explicit unresolved target.
