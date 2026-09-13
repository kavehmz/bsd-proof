# Independent review of the CM regulator tensor attempt

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed file: [CM regulator tensor](cm-regulator-tensor-attack.md).
**PASS after the recorded rationality repair and direct source derivation.**
The constructions, restricted moment formula, and polynomial identity
below pass. The new analytic-rank certificate is independently verified.

## 1. Scope and arithmetic inputs

The curve is the explicit minimal equation y²=x³+39x, not a database
label silently identified with a different isogeny model. The points
P=(3,12), Q=(27,144) satisfy its equation, and their sum is
(1/4,25/8): the chord slope is 11/2 and the rational group law gives
the asserted coordinates. The note records exact descent and all-prime
saturation, rather than treating the source's suggested points as an
automatically full basis.

The CM decomposition is correct. Conjugation anticommutes with [i], so
[i] interchanges the plus and minus rational eigenspaces. The projector
denominator is two, hence the same argument works on the free modules
over Z_p for odd p. It yields rank four over Q(i), or CM rank two.
It does not make the two-point regulator a rank-one bilinear form.

## 2. Sigma and the actual regulator

The reviewer fetched [Stein–Wuthrich, published §4.1](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf)
and checked its canonical height formula (4.1), eigenvector convention,
and factor of two. No Sha-finiteness premise is used there.

**[NEW, independent reconstruction]** At a good split prime the [i]
eigenvalues on ω and xω are distinct, namely i and −i. The unit-root
complement is [i]-stable and different from the Hodge line, so it is
exactly the xω line. The corresponding weight-two correction is zero.
Over C, invariance of the square lattice under multiplication by i
makes the regularized weight-two Eisenstein value zero as well.
The reviewer checked the reduced-theta convention in
[Bannai–Kobayashi, Example 1.9](https://arxiv.org/html/math/0610163v4).
Thus the two normalized sigma power series coincide in the Néron
logarithmic coordinate. This assertion concerns a fixed rational
power series; it does not claim integral coefficients in that coordinate.

Direct substitution into (x')²=4x³+156x gives b₁=−39/5. The denominator
in (4) is 4·3=12, so the first sigma coefficient is −b₁/12=13/20,
exactly as stated in the note. The equation
uses exponents 4n−2 for x and 4n for log(σ/z).

The reviewer fetched [BFK, Theorem 1.2 and Definition 5.1](https://arxiv.org/html/0807.4007v2).
On the zero residue disc, the Coleman logarithm is defined by the
formal reduced theta composed with the elliptic logarithm. Its
discriminant constant is retained and cancels exactly in F_p.

**[NEW, independent reconstruction]** The allowed multiplier sends
each point into the formal group and each bad identity component.
The product 8 of Tamagawa numbers kills every component quotient.
Non-anomalousness makes #E(F_p) prime to p. The three quantities
2A,2B,2C are therefore the genuine quadratic heights of P,Q,P+Q,
and polarization gives the off-diagonal entry C−A−B. Their determinant
is 4AB−(C−A−B)². Taking the logarithm of the theta addition quotient
gives the stated Poincaré-section formula with its denominator terms.
This checks both the factor four and independence of the multiplier.

## 3. Precision and the normalized ratio

**[NEW, independent reconstruction]** Put a=X−1 and b=Y−1. For p≥5,
the logarithm remainder after degree two lies uniformly in p³Z_p.
Squaring (a−b)−(a²−b²)/2 gives
(X−Y)²(3−X−Y) modulo p⁴. Its expansion is
3X²−6XY+3Y²−X³+X²Y+XY²−Y³. Division by (p−1)² is valid.
An integral measure preserves the uniform error. Thus (11)–(12)
hold independently of the remaining audit of closed moment values.

For regulator valuation three, dividing a p⁴ error gives a p error;
a p³ error would not suffice. This conclusion does not require a
leading coefficient to be a unit or predict how often it is a unit.

The coefficient normalization in (10) follows algebraically from
the stated comparison with u(0)=1: c₂=M/(2g²), multiplication by
c_cmp, removal of the torsion/Tamagawa factor 1/2 and Euler factor,
then division by Reg_p/g². This gives c_cmp M/(4 e_p Reg_p).
The constant f₀ varpi_E=156i follows by multiplying the specified
complex numbers. The source comparison, including u(0)=1, was read
in [Banwait, Lemma 3.5](https://arxiv.org/html/2609.08431v1), and its
underlying BK normalization was subsequently reconstructed directly,
as described in §5 below.

## 4. Independent analytic verification

The coordinator reconstructed every Fourier coefficient through 1405
from direct finite-field point counts at good primes, the verified
additive Euler factors at 2,3,13, prime-power recurrences, and
multiplicativity. They agree exactly with the coefficients used in
the author's first Mellin call.

The reviewed Mellin algorithm applies to this new equation with its
exact conductor, root number and descent bounds. A second call at
112 bits and cutoff 48, with Fourier cutoff 1686, gives a strictly
positive second completed derivative. The exact leading interval is
strictly inside the first call's interval at 96 bits/cutoff 40.
No small numerical value was used to establish lower vanishing:
exact algebraic rank two excludes analytic ranks zero and one by
Gross–Zagier–Kolyvagin. The nonzero second derivative gives the upper bound.

Full output: [CM-39 certificate](../../compute/data/cm39_analytic_rank_certificate.json).
Exact reproducer: [certify_cm39.py](../../compute/scripts/certify_cm39.py).
It ran successfully with the command in its docstring. The file records
the unchanged Mellin script's hash and all rigorous tail bounds.

## 5. Required repair and completed source review

The first gap formulation used an arbitrary embedding of the real
BSD quotient into C_p. The reviewer requested an arithmetic target
instead: first prove that quotient rational, then compare its canonical
image in Q_p. The author accepted and applied this repair.

The reviewer read the new direct proof in §6.1 of the CM note and
reconstructed its normalization, without treating compressed source
displays as interchangeable. The fixed-lattice theta measure is the
integral formal-coordinate measure. Its restricted transform is
unchanged by replacing a pole correction with any correction depending
on just one variable: the unit projector in the other variable kills
that difference. Thus the four full Laurent theta functions may be
used after restriction, as in BK Lemma 3.4. This does not prove the
corresponding unrestricted moment statement.

For a partial ideal class a⁻¹, put q=ψ(a). The tilde measure has
prefactor q and sends (u,v) to (qu,Fv/bar q). Definition 3.8 contributes
Ω_p/X and the central character contributes q⁻¹X. Their product
cancels q exactly. The global coordinate substitution sends a test
function H to H(u,(Fv)⁻¹). This proves the extra period factor Ω_p
and the inverse second coordinate for the full restricted measure.
The sum is once per ray class. Replacing it with every residue unit
would repeat each summand four times for Q(i); the proof does not do so.

Returning the three nontrivial distribution terms to the original
lattice gives factors π^k/barπ^(l+1), π^l/barπ^(k+1), and their product.
The inverse lattice contributes the essential +1 in each denominator.
The second class permutation uses the integral CRT representative
β=ε/barπ, with ε≡1 modulo f and 𝔭 and ε≡0 modulo bar𝔭.
Its action on the torsion point is valid modulo the original lattice;
literal division of an arbitrary complex representative is not a
substitute. These maps permute the ray classes and give exactly the
two Euler factors in (13). The regular Laurent coefficient contributes
the factorial, sign and F^l, and logarithmic differentiation contributes
Ω_p^(k+l). Together with the previous Ω_p this proves the stated formula.

The reviewer also checked BK Lemma 3.4, Proposition 3.5 and the
homogeneity scaling directly. The source's shorthand all-residue sum,
displayed Theorem 3.7 period exponent, and Proposition 3.13 expression
are not inputs to this reconstruction. Equation (9) is separately
fixed by Corollary 3.12 and compatible roots of unity; changing that
system multiplies by a group element with constant term one.

The two variable moment proof therefore passes with its explicit
restricted-measure normalization. The polynomial congruence and the
sigma regulator identity remain independent of this source issue.

The coordinator subsequently read all eight sections of the separate
[independent source check](cm-moment-source-check.md). The nonzero
fourth moment has factorial 24, period power five and an absolutely
convergent nonzero ideal L-series. At p=5 its Euler factor is 4 modulo
5. The weighted second-degree test has coefficient 8P_(0,3), also
nonzero by its absolutely convergent ideal Euler product, and gives
different exact multipliers for the literal v4 display and the direct
restriction formula (3 versus 2 modulo 5). These calculations pass.
The discrepancy is specific to the stated source display and is not
a BSD counterexample or a failure of the reconstructed restricted measure.

Even after this check, the note constructs two operations on a common
theta function; it does not prove the rational moment-to-regulator
identity CM-Theta, regulator nondegeneracy at every prime, or finite
Sha. These are retained as actual missing arithmetic statements.
