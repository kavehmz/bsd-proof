# Independent review of the analytic-rank certificates

Date: 2026-09-12. Reviewed
[the derivation](analytic-rank-certificates.md),
[the implementation](../../compute/scripts/certify_mellin.py), and the
[128-bit output](../../compute/data/analytic_rank_certificates.json).

**Review result: no actionable mathematical or implementation error found.**
The stated certificates prove the analytic ranks of $389a1$ and $5077a1$
are two and three, respectively, using the exact descent results and the
classical analytic-rank-zero/one theorem as inputs. The argument does not
prove full Sha finiteness or the BSD leading-term formula.

The review independently rederives both infinite-tail bounds and the
normalization, checks the installed numerical-library semantics, and checks
every Fourier coefficient by a separate elementary computation. It does
not repeat the entire quadrature computation.

## 1. Exact lower bounds

**[THEOREM, reviewed implication]** The lower-bound argument is valid.
The theorem that analytic rank zero or one implies the same algebraic rank
has the contrapositive
$$
\operatorname{rank}E(\mathbb Q)\ge2
\quad\Longrightarrow\quad
\operatorname{ord}_{s=1}L(E,s)\notin\{0,1\}.
$$
For $389a1$, this already gives analytic rank at least two. For $5077a1$,
the exact root number $-1$ forces odd analytic rank, hence at least three.
This uses no parity conjecture for the Mordell–Weil rank: the parity here
is the parity of the order of an analytic function satisfying its functional
equation.

The recorded PARI outputs are
$$
[2,2,0,[[-2,0],[4,8]]],\qquad
[3,3,0,[[-3,0],[-1,3],[11,35]]].
$$
The installed PARI documentation for `ellrank` explicitly states that its
descent and Cassels-pairing quantities are computed unconditionally and that
the first two entries bound the Mordell–Weil rank. Its algorithm description
therefore supports both exact algebraic ranks without a GRH assumption.
See [PARI's elliptic-curve documentation, `ellrank`](https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html#ellrank),
also read locally in `.tools/sage/share/pari/doc/usersch3.tex`.

## 2. Independent normalization calculation

Put $F(u)=f(iu/\sqrt N)$ and $c=2\pi/\sqrt N$. Termwise Mellin integration
in its initial domain of absolute convergence gives
$$
\int_0^\infty F(u)u^{s-1}\,du
 =N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s)=\Lambda(E,s).
$$
For weight two, the Fricke eigenvalue is $-w$. Thus the Fricke relation
on the imaginary axis reads $F(1/u)=wu^2F(u)$. Splitting the integral at
one and substituting $v=1/u$ in its lower part gives
$$
\Lambda(E,s)=\int_1^\infty F(u)(u^{s-1}+wu^{1-s})\,du.
$$
Both integrals have exponential decay at infinity after this substitution,
so differentiation at the center and summation over coefficients are valid.
For $w=(-1)^k$,
$$
\Lambda^{(k)}(E,1)=2\sum_{n\ge1}a_n
             \int_1^\infty e^{-cnu}(\log u)^k\,du.
$$
The change of variables $t=cu$ produces exactly the integrand
$$
\frac2c\left(\sum_{n=1}^M a_ne^{-nt}\right)(\log(t/c))^k
$$
used in the script. There is no missing $\sqrt N$, $2\pi$, or factorial.

The analytic prefactor $A(s)=N^{s/2}(2\pi)^{-s}\Gamma(s)$ satisfies
$A(1)=1/c$. Section 1 supplies the exact vanishing of every lower derivative
of $L$ before conversion of the leading term. Leibniz's rule therefore gives
$$
\frac{L^{(k)}(E,1)}{k!}
=\frac{c\Lambda^{(k)}(E,1)}{k!}.
$$
**[THEOREM, reviewed calculation]** The completed normalization and the
leading-coefficient conversion are correct.

## 3. Independent rederivation of the errors

The Hasse bound and the good-prime Euler-factor recurrence give
$|a_{\ell^e}|\le(e+1)\ell^{e/2}$. At a bad prime the local coefficients
satisfy the same upper bound. Multiplicativity gives
$|a_n|\le d(n)\sqrt n\le2n$.

For the coefficient tail, write $v=u-1$ and use
$\log(1+v)\le v$. Then
$$
\int_1^\infty e^{-cnu}(\log u)^k\,du
\le e^{-cn}\int_0^\infty e^{-cnv}v^k\,dv
=\frac{k!e^{-cn}}{(cn)^{k+1}}.
$$
Hence the contribution of $n>M$ is bounded by
$$
\frac{4k!}{c^{k+1}}
\sum_{n>M}\frac{e^{-cn}}{n^k}
\le
\frac{4k!}{c^{k+1}(M+1)^k}
\frac{e^{-c(M+1)}}{1-e^{-c}}=B_M.
$$

For the integration tail of the finite polynomial, use the majorant
$\sum_{n\le M}|a_n|e^{-nt}\le2e^{-t}/(1-e^{-t})^2$ and
$\log(t/c)\le t/c$ for $t\ge T\ge c$. This gives
$$
\frac2c\int_T^\infty
  \left|\sum_{n\le M}a_ne^{-nt}\right|(\log(t/c))^k\,dt
\le\frac4{c^{k+1}(1-e^{-T})^2}\int_T^\infty e^{-t}t^k\,dt.
$$
For integer $k\ge0$, integration by parts evaluates the last integral as
$k!e^{-T}\sum_{j=0}^kT^j/j!$, giving exactly the claimed $B_T$.

**[THEOREM, reviewed bounds]** Both tail inequalities are valid, so the
two elementary bounds marked for review in the certificate derivation pass
this independent review. Their sum is a valid total error. No estimate
depends on cancellation among the omitted coefficients.

## 4. Library and coefficient checks

The installed Sage 10.7 source was inspected at these functions:

* `EllipticCurve_rational_field.anlist` calls PARI `ellan` and returns exact
  integers, including the index-zero sentinel.
* `ComplexBallField.integral` promises a rigorous enclosure and accepts
  ball endpoints. Its callback contract requires the `analytic` flag for
  branch-cut functions.
* `ComplexBall.log(analytic=True)` returns an indeterminate ball if the
  argument ball meets its cut. The callback in the certificate passes this
  flag correctly. The exponential and finite polynomial are entire.
* `RealBall.add_error` adds an upper bound for its ball-valued argument to
  the radius. Thus it correctly incorporates both error balls, including
  their rounding uncertainty.
* `RealBall.lower` and `upper` round outwards before conversion to exact
  rational numbers. The JSON endpoints are therefore valid outward bounds.

The public integration contract is in the
[Sage complex-ball documentation](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_arb.html#sage.rings.complex_arb.ComplexBallField.integral).

The Horner loop evaluates $q\sum_{j=1}^M a_jq^{j-1}$, where $q=e^{-t}$,
which is exactly the required polynomial. The factors $2/c$ and the
$k$th power of the logarithm are applied once.

**[THEOREM, independent exact computational check]** Every Fourier
coefficient used in the recorded run was rebuilt independently as follows.
For each prime below the cutoff, the curve was constructed from the JSON's
integer Weierstrass coefficients, and its points over $\mathbb F_\ell$ were
counted directly. For odd $\ell$, the number of roots in $y$ was computed
from the quadratic discriminant
$$
(a_1x+a_3)^2+4(x^3+a_2x^2+a_4x+a_6)
$$
for each $x$; at $\ell=2$ all pairs were enumerated. All these primes are
good for the respective curves. The good-prime recurrence and
multiplicativity then reconstructed the full coefficient vectors.

| Curve | Primes counted directly | Coefficients checked | Result |
|---|---:|---:|---|
| $389a1$ | 54 | $a_1,\ldots,a_{252}$ | All agree |
| $5077a1$ | 155 | $a_1,\ldots,a_{908}$ | All agree |

This is an independent point-count check, not a comparison between two
wrappers calling the same coefficient routine.

The following reproduces that check from the repository root without
rerunning the quadrature:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python - <<'PY'
import json
from fractions import Fraction
from sage.all import EllipticCurve, prime_range, factor

records = json.load(open('compute/data/analytic_rank_certificates.json'))['records']
for z in records:
    E = EllipticCurve(z['ainvs'])
    a1, a2, a3, a4, a6 = z['ainvs']
    M = z['coefficient_cutoff']
    actual = list(map(int, E.anlist(M)))
    ap = {}
    primes = list(prime_range(M + 1))
    for l0 in primes:
        l = int(l0)
        assert z['conductor'] % l
        if l == 2:
            number = 1 + sum(
                (y*y + a1*x*y + a3*y - x*x*x - a2*x*x - a4*x - a6) % 2 == 0
                for x in range(2) for y in range(2))
        else:
            number = 1
            for x in range(l):
                d = ((a1*x + a3)**2 + 4*(x**3 + a2*x*x + a4*x + a6)) % l
                number += 1 if d == 0 else (2 if pow(d, (l-1)//2, l) == 1 else 0)
        ap[l] = l + 1 - number
    rebuilt = [0]
    for n in range(1, M + 1):
        val = 1
        for l0, e0 in factor(n):
            l, e = int(l0), int(e0)
            prev, current = 1, ap[l]
            for i in range(2, e + 1):
                prev, current = current, ap[l]*current - l*prev
            val *= current
        rebuilt.append(val)
    assert rebuilt == actual
    lo, hi = map(Fraction, z['completed_derivative_rational_endpoints'])
    assert 0 < lo < hi
    leadlo, leadhi = map(Fraction, z['L_leading_rational_endpoints'])
    coarse = {
        '389a1': (Fraction(759, 1000), Fraction(760, 1000)),
        '5077a1': (Fraction(1731, 1000), Fraction(1733, 1000)),
    }[z['label']]
    assert coarse[0] < leadlo < leadhi < coarse[1]
    assert int(E.root_number()) == z['root_number']
    print(z['label'], 'prime counts:', len(primes), 'coefficients:', M, 'PASS')
PY
```

## 5. Output and conclusion

The JSON was parsed using exact rational arithmetic. Both completed
derivative lower endpoints are strictly positive. Its leading-coefficient
endpoints also satisfy, strictly,
$$
\frac{759}{1000}<\frac{L''(389a1,1)}2<\frac{760}{1000},\qquad
\frac{1731}{1000}<\frac{L'''(5077a1,1)}6<\frac{1733}{1000}.
$$
Thus the completed derivatives do not vanish, giving the required analytic
upper bounds. Combined with §1 this proves the exact analytic ranks and
therefore the stated BSD rank equalities for these two curves.

The checked script has SHA-256
`09e1f3993300e4403532792ec728e3fa4653646cf397ab32d25a34f6f2fe06b0`;
the checked 128-bit JSON has SHA-256
`6752e42e19c7cd5d4d3d8ba48e3c267cd8113dbd2ba2c3c47b2f071b0a1fcc0f`.
The secondary $96$-bit, $T=60$ output was subsequently inspected at
`.tools/research-2026-09-12/analytic_rank_check.json`, with SHA-256
`fc4ad3582fcb0c88ec13f77e58e87ea1bf8552cae2f3d2a7572b7f03e8eda3ba`.
Exact rational comparison shows that its two completed-derivative intervals
and its two leading-coefficient intervals are positive and strictly contain
the corresponding $128$-bit intervals. The second output can be regenerated
using `--bits 96 --cutoff 60 --out <chosen-path>`. It is a consistency check;
the $128$-bit enclosure with proved error bounds supplies the certificate.
