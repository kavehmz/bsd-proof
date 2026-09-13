# A certified archimedean BSD interval for 389a1

Date: 2026-09-12. This supplies the numerical prerequisite in
[Proposition 6.1 of the derived-comparison note](derived-comparison-attack.md#6-the-units-can-be-bypassed-a-one-sided-and-archimedean-reduction).
New deductions below passed independent coordinator review: the Bézout tail, finite point search, lattice bound, period normalization, and interval calculation were checked on the page. A second run with seven regulator doublings gives strictly narrower overlapping enclosures.

**[THEOREM, exact and interval computational certification]** For
$$
E:\ y^2+y=x^3+x^2-2x,
\qquad
n_E=\frac{L''(E,1)/2}{\Omega_{\rm full}\operatorname{Reg}_{\rm BSD}},
$$
where $\Omega_{\rm full}=\int_{E(\mathbb R)}|\omega|$ and the regulator is
taken on the full Mordell–Weil lattice, the script proves
$$
\boxed{\quad
\frac{533217021}{536870912}\ \leq\ n_E\ \leq\
\frac{541003931}{536870912},\qquad 0<n_E<2.
\quad}\tag{1}
$$
In particular $0.9931<n_E<1.0077$. These decimal endpoints are deliberately
outward; the fractions in (1) are the certificate endpoints.
The exact torsion order and Tamagawa product are both one, so this is
exactly the quotient $\ell_Et^2/(\Omega_E R_\infty C)$ in that proposition.

This is a statement about a positive real number. No rationality,
integrality, finiteness of $\operatorname{Sha}$, or BSD leading-term equality is assumed
or concluded. The algebraic and analytic ranks are already proved to be
two by [the analytic-rank certificate](analytic-rank-certificates.md).

## 1. Reproduction and numerical inputs

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_bsd_interval.py
```

The source is
[`certify_bsd_interval.py`](../../compute/scripts/certify_bsd_interval.py),
and the complete output is
[`bsd_archimedean_interval.json`](../../compute/data/bsd_archimedean_interval.json).
The run used Sage 10.7, eclib 20250627, FLINT 3.3.1, and 128-bit Arb balls.
The output includes exact rational interval endpoints, both polynomial
Bézout identities, all finite-search point heights, exact saturation
relations, the finite doubling heights, and explicit tail bounds.

The one imported numerical input is the rigorous interval for
$\ell_E=L''(E,1)/2$ from
[`analytic_rank_certificates.json`](../../compute/data/analytic_rank_certificates.json):
$$
\ell_E\in
[0.75931650028842677023019260789\ \mathord\pm\ 7.06\cdot10^{-30}].
\tag{2}
$$
The script reads its exact rational endpoints, not the displayed decimal
midpoint and radius, and records the input file's SHA-256 digest. The
positivity and rank justification belong to the cited analytic certificate.
Every period and height used here is computed independently of (2).

**[THEOREM, arithmetic invariants]** The integral model has
$\Delta=389$, $c_4=112$ and minimal discriminant $389$. It is good away
from $389$ and has type $I_1$ there, giving $c_{389}=1$. Direct enumeration
gives
$$\#E(\mathbb F_2)=5,\quad\#E(\mathbb F_3)=6,\quad\#E(\mathbb F_5)=9.$$
The prime-to-residue-characteristic torsion-injection theorem at good
reduction now proves $E(\mathbb Q)_{\rm tors}=0$: the counts at $2,3$
exclude every odd torsion prime, and the odd count at $5$ excludes $2$.
The script enumerates all pairs $(x,y)$ over these three fields.

## 2. Height convention and a completely explicit error bound

For $x(P)=A/B$ in lowest terms with $B>0$, put
$$h_x(P)=\log\max(|A|,B).$$
Use the BSD/Cremona normalization
$$
H(P)=\lim_{k\to\infty}4^{-k}h_x(2^kP),\qquad
\langle P,Q\rangle=\frac{H(P+Q)-H(P)-H(Q)}2.
\tag{3}
$$
**[THEOREM, normalization]** This quadratic height is the one used by
Sage/PARI for the BSD regulator over $\mathbb Q$. It is **twice** the
canonical height normalized as $\tfrac12\lim4^{-k}h_x(2^kP)$ in
Silverman's convention. Consequently using that smaller height without
compensation would divide a rank-two regulator by four. The explicit
normalization and limit are verified in the
[Sage point-height documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_point.html#sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_number_field.height)
and in the installed source. No value returned by its ordinary floating
point `height()` function is used as an interval certificate here.

For this curve the exact homogeneous duplication polynomials are
$$
\begin{split}
F(X,Z)&=X^4+4X^2Z^2-2XZ^3+3Z^4,\\
G(X,Z)&=4X^3Z+4X^2Z^2-8XZ^3+Z^4.
\end{split}\tag{4}
$$
Thus $x(2P)=F(A,B)/G(A,B)$, followed by cancellation. The following
integer identities can be checked just by multiplication:
$$
\begin{split}
A_XF+B_XG&=389X^7,&
A_ZF+B_ZG&=389Z^7,\\
A_X&=389X^3+188X^2Z-520XZ^2+66Z^3,\\
B_X&=-47X^3-212X^2Z+108XZ^2-198Z^3,\\
A_Z&=-48X^2Z-32XZ^2+144Z^3,\\
B_Z&=12X^3-4X^2Z+40XZ^2-43Z^3.
\end{split}\tag{5}
$$
The combined sums of absolute coefficients in $(A_X,B_X)$ and
$(A_Z,B_Z)$ are $1728$ and $323$. The corresponding maximum for $F,G$
is $17$.

**[NEW] Lemma 2.1.** For every rational point with finite coordinates
through the indicated duplication,
$$
|h_x(2P)-4h_x(P)|\leq\log1728.
\tag{6}
$$
Consequently
$$
\left|H(P)-4^{-k}h_x(2^kP)\right|
\leq\frac{\log1728}{3\cdot4^k},
\qquad |H(P)-h_x(P)|\leq\log12.
\tag{7}
$$
The projective interpretation also covers the point at infinity; the
nonzero points in this certificate are nontorsion and never reach it.

*Proof.* Let $T=\max(|A|,B)$, let
$M=\max(|F(A,B)|,|G(A,B)|)$, and let $d$ be the positive gcd of these
two values. The identities (5) and $\gcd(A,B)=1$ imply $d\mid389$.
The coefficient bounds give $M\leq17T^4$. If $T=|A|$ use the first
identity; if $T=B$ use the second. In either case
$$389T^7\leq1728T^3M.$$
The height of the reduced pair is therefore bounded by
$$\frac{T^4}{1728}\leq\frac M d\leq17T^4.$$
Taking logarithms proves (6). Writing the difference between successive
terms of $4^{-k}h_x(2^kP)$ and summing the geometric series gives
$$\sum_{j=k}^\infty\frac{\log1728}{4^{j+1}}
 =\frac{\log1728}{3\cdot4^k}.$$
This proves (7), since $1728=12^3$. $\square$

The script independently constructs (5) by solving its rational linear
system, clears denominators, and verifies the polynomial identities
exactly. It also checks each repeated rational duplication against Sage's
exact group law. For the three regulator heights it uses $k=6$, giving
an error of less than $0.000607$ per height. The last logarithm and this
error are evaluated with Arb's outward rounding and combined as a ball.

## 3. A full basis certified without an unproved saturation index

Take
$$P=(-1,1),\qquad Q=(0,-1),\qquad P+Q=(4,8).$$
Their height balls from (7) give the Gram determinant
$$
R_{P,Q}=H(P)H(Q)
 -\left(\frac{H(P+Q)-H(P)-H(Q)}2\right)^2
\in(0.15129,0.15351).
\tag{8}
$$
These decimals are outward simplifications of the exact endpoints in
the JSON. Positivity proves independence. The already-certified rank
upper bound of two makes their subgroup a lattice of finite index in
the full group. Its index is now certified by a finite argument.

**[NEW] Lemma 3.1 (minimum height).** Every nonzero point in $E(\mathbb Q)$
has $H(P)>3/10$.

*Proof.* If $H(P)\leq3/10$, (7) would imply
$$h_x(P)\leq3/10+\log12<\log17.$$
The last inequality is checked by an outward Arb interval comparison.
Thus, in reduced coordinates, $\max(|A|,B)\leq16$.

The script enumerates **every** coprime pair
$-16\leq A\leq16$, $1\leq B\leq16$: there are 319 such rational
$x$-values. It checks exactly whether
$$4x^3+4x^2-8x+1$$
is a square in $\mathbb Q$, the necessary and sufficient condition
for a rational $y=(-1\pm\sqrt{4x^3+4x^2-8x+1})/2$.
There are precisely the following 13 points up to negation:
$$
\begin{gathered}
(-2,0),\ (-1,1),\ (0,0),\ (1,0),\ (3,5),\ (4,8),\ (6,15),\\
(-3/4,7/8),\ (5/4,5/8),\ (-11/9,28/27),\\
(1/9,-8/27),\ (10/9,8/27),\ (1/16,-9/64).
\end{gathered}
$$
For each, exact duplication with $k=5$ and error
$\log1728/(3\cdot4^5)$ gives a lower bound strictly above $3/10$.
The smallest of the 13 certified lower endpoints occurs at $(0,0)$ and is
$$
\frac{110291777509685053501951483560582268803}
 {340282366920938463463374607431768211456}>0.3241>3/10.
$$
Every candidate's finite height integer and rational interval endpoints
are recorded in the JSON. Negation preserves $x$ and $H$, so the other
sign of $y$ requires no new test. This contradicts the putative bound.
The point at infinity was excluded in the statement. $\square$

**[NEW] Lemma 3.2 (rank-two lattice bound).** A rank-two Euclidean lattice
whose shortest nonzero squared length is $\lambda$ has Gram determinant
at least $3\lambda^2/4$.

*Proof.* Choose a shortest vector $u$, which is primitive and can be
extended to a basis $u,v$. Add an integer multiple of $u$ to $v$ until
the component of $v$ along $u$ has absolute length at most $\|u\|/2$.
The vector $v$ is nonzero and thus $\|v\|\geq\|u\|$. Its perpendicular
component consequently has length at least $\sqrt3\|u\|/2$. The squared
covolume is at least $3\|u\|^4/4=3\lambda^2/4$. $\square$

**[NEW: application]** Apply this to the full Mordell–Weil group with the
positive definite pairing (3). Lemma 3.1 gives
$$\operatorname{Reg}_{\rm BSD}\geq\frac34(3/10)^2=27/400.$$
If the index of $\mathbb ZP+\mathbb ZQ$ were an integer $h\geq2$, the
change-of-lattice formula would give
$$R_{P,Q}=h^2\operatorname{Reg}_{\rm BSD}\geq27/100.$$
This contradicts (8). Therefore $h=1$, and (8) is already the
**saturated** BSD regulator. This certification uses finite exact point
enumeration, the explicit height error, and elementary lattice geometry;
it does not rely on a floating point saturation-index estimate.

**[THEOREM, independent software cross-check]** In addition, the script
passes the original PARI points $A=(-2,0)$, $B=(4,8)$ to
`mwrank_MordellWeil.saturate(max_prime=-1,min_prime=2)` and requires the
returned triple `(True,3,'[ ]')`. The
[primary Sage/eclib documentation](https://doc.sagemath.org/html/en/reference/libs/sage/libs/eclib/interface.html#sage.libs.eclib.interface.mwrank_MordellWeil.saturate)
states that success with `max_prime=-1` certifies saturation at all primes.
This is stronger than saturation only below a user-chosen cutoff.
The resulting basis is $(0,-1),(4,8)$, and the exact identities
$$A=-P+2Q,\qquad B=P+Q$$
have determinant $-3$. They also prove the old raw lattice's exact index
three independently, once the full-basis result above is known. A regulator
on that raw lattice would be nine times too large.

## 4. Full real period, including both components

Complete the square by setting $u=y+1/2$. Then
$$u^2=f(x)=x^3+x^2-2x+1/4,\qquad\omega=\frac{dx}{2u}.$$
The three roots $e_3<e_2<e_1$ lie respectively in
$$(-3,-1),\qquad(0,1/4),\qquad(1/2,1).$$
All endpoint signs of $4f$ are opposite in each bracket. The disjoint
brackets therefore each contain one root and exhaust this cubic's roots.
The script uses 160 exact rational bisections per bracket; no approximate
root finder is used for certification.

**[NEW: period reduction]** Since there are three real roots, the real
curve has two components. Translation identifies their invariant
differential measures. On the identity component, accounting for its
two branches gives
$$
\Omega_0=\int_{e_1}^\infty\frac{dx}{\sqrt{f(x)}}.
$$
Let $a=e_1-e_3$ and $m=(e_2-e_3)/a\in(0,1)$. Substitute
$x=e_3+a/t^2$, then $t=\sin\theta$, to obtain
$$
\Omega_0=\frac2{\sqrt a}\int_0^{\pi/2}
       \frac{d\theta}{\sqrt{1-m\sin^2\theta}},
\qquad\Omega_{\rm full}=2\Omega_0.
\tag{9}
$$
All substitutions are on positive real branches and the endpoint
singularities are integrable.

**[THEOREM: Gauss AGM identity]** For $0<m<1$ the integral in (9) is
$\pi/(2\operatorname{AGM}(1,\sqrt{1-m}))$; see
[NIST DLMF, equations 19.8.1–19.8.5](https://dlmf.nist.gov/19.8#E5).
Starting from $a_0=1$, $b_0=\sqrt{1-m}$, form
$$a_{j+1}=(a_j+b_j)/2,\qquad b_{j+1}=\sqrt{a_jb_j}.$$
The arithmetic iterates decrease, the geometric iterates increase, and
$b_j\leq\operatorname{AGM}\leq a_j$. The script performs eight iterations
using Arb balls and encloses the AGM between the lower endpoint of the
last geometric ball and the upper endpoint of the last arithmetic ball.
Thus the uncomputed infinite iteration is covered by a proved bracket.
The resulting enclosure is
$$
\Omega_{\rm full}=\frac{2\pi}{\sqrt a\operatorname{AGM}(1,\sqrt{1-m})}
\in[4.980425121710110150642715583884604920\
      \mathord\pm\ 8.13\cdot10^{-37}].
\tag{10}
$$
The least positive real period is half this number. Its use in place of
the full period would multiply $n_E$ by two and spoil the intended bound.

## 5. Final interval and what remains

**[NEW: interval deduction]** Multiplying the positive balls (8) and
(10), with the exact torsion and Tamagawa factors, gives
$$
0.75351<\Omega_{\rm full}\operatorname{Reg}_{\rm BSD}<0.76452.
$$
Dividing the positive leading-coefficient ball (2) by this positive
denominator gives the exact rational endpoints (1). The implementation
also asserts the comfortable rational bounds $9/10<n_E<11/10$.
Outward rounding is used for all real operations, including the
logarithms, square roots, divisions, and determinant. The explicitly
bounded doubling tail and the AGM bracket account for their respective
infinite limits. Repeating an ordinary floating point computation is
not part of the proof.

The archimedean prerequisite of Proposition 6.1 is therefore complete for
this curve. To apply that proposition as a BSD proof still requires its
other hypotheses: rationality of the quotient, finiteness of every
$\operatorname{Sha}[p^\infty]$, and the stated one-sided valuation inequality at every
prime. A narrow real interval around one proves none of those statements.
