# Rigorous analytic-rank certificates for 389a1 and 5077a1

Date: 2026-09-12. See the [independent review](review-analytic-certificates.md).
This upgrades the earlier numerical analytic-rank estimates
to certificates with explicit error bounds. It concerns BSD(rank), not full BSD.

## 1. The statement and exact lower bounds

**[THEOREM, computational verification]**
$$
\operatorname{rank}389a1(\mathbb Q)=\operatorname{ord}_{s=1}L(389a1,s)=2,
\qquad
\operatorname{rank}5077a1(\mathbb Q)=\operatorname{ord}_{s=1}L(5077a1,s)=3.
$$

These examples are not new cases of BSD(rank). The contribution here is a
reproducible certificate that does not infer exact rank from small approximate
values of lower derivatives.

**[THEOREM]** If the analytic rank of an elliptic curve over $\mathbb Q$ is
zero or one, its Mordell–Weil rank is the same. This is the modularity and
Gross–Zagier–Kolyvagin rank theorem used throughout the repository. In particular,
two independent rational points rule out both analytic ranks zero and one.
The functional equation then gives analytic rank at least two if the root
number is $+1$, and at least three if it is $-1$.

The script obtains exact descent bounds from `ellrank`, using the given
Weierstrass coefficients, and computes the root number from local reduction.
It requires equal algebraic rank bounds, either two or three, and the matching
root number. No conjecture that algebraic and analytic ranks agree is used.

## 2. The completed Mellin integral

Put $c=2\pi/\sqrt N$, $f(z)=\sum_{n\ge1}a_n e^{2\pi inz}$, and
$$\Lambda(E,s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(E,s).$$
The newform functional equation gives
$$
\Lambda(E,s)=\int_1^\infty f(iu/\sqrt N)
                         (u^{s-1}+w u^{1-s})\,du.
$$
**[THEOREM, Mellin transform calculation]** Differentiation at $s=1$ gives
$$
\Lambda^{(k)}(E,1)
=(1+w(-1)^k)\sum_{n\ge1}a_n\int_1^\infty e^{-cnu}(\log u)^k\,du.
$$
Exponential decay justifies all exchanges. We take $w=(-1)^k$, so the factor
is two. After $t=cu$, truncate the coefficient sum at $M$ and the integral at $T$:
$$
J_{M,T}=\frac2c\int_c^T
       \left(\sum_{n=1}^M a_ne^{-nt}\right)(\log(t/c))^k\,dt.
$$

The modular Mellin transform and classical analytic-rank theorem are recalled in
[Stein–Wuthrich, §§1–2](https://www.wstein.org/papers/shark/shark.pdf);
the repository also derives the completed-integral expression in
[`F-analytic-side.md`, §3.3](../approaches/F-analytic-side.md).

## 3. Explicit infinite-tail bounds

The Euler factors and Hasse bound give $|a_n|\le d(n)\sqrt n$.
Pairing divisors below and above $\sqrt n$ gives $d(n)\le2\sqrt n$, so
$|a_n|\le2n$. This elementary majorant is sufficient.

**[NEW, elementary bound; independently reviewed]** The omitted
coefficients contribute at most
$$
B_M=\frac{4k!}{c^{k+1}(M+1)^k}
                  \frac{e^{-c(M+1)}}{1-e^{-c}}.
$$
*Proof.* For $u\ge1$, $0\le\log u\le u-1$, so
$$\int_1^\infty e^{-cnu}(\log u)^kdu
\le\frac{k!e^{-cn}}{(cn)^{k+1}}.$$
Multiply by $2|a_n|\le4n$, use $n^{-k}\le(M+1)^{-k}$ for $n>M$,
and sum a geometric series. $\square$

**[NEW, elementary bound; independently reviewed]** For $T\ge c$, the
omitted integration range contributes at most
$$
B_T=\frac{4k!}{c^{k+1}}\frac{e^{-T}}{(1-e^{-T})^2}
                          \sum_{j=0}^k\frac{T^j}{j!}.
$$
*Proof.* Bound the truncated polynomial by the full majorant
$\sum_{n\ge1}2ne^{-nt}=2e^{-t}/(1-e^{-t})^2$ and use
$0\le\log(t/c)\le t/c$ for $t\ge T\ge c$. The denominator is bounded below
by $(1-e^{-T})^2$. Repeated integration by parts gives
$\int_T^\infty e^{-t}t^kdt=k!e^{-T}\sum_{j=0}^kT^j/j!$. $\square$

Therefore $|\Lambda^{(k)}(E,1)-J_{M,T}|\le B_M+B_T$.
Overcounting the intersection of the two omitted ranges is harmless.

## 4. Certified quadrature and conclusion

`ComplexBallField.integral` computes a rigorous enclosure of $J_{M,T}$.
The integrand is evaluated with ball arithmetic, using Horner evaluation of
the exact coefficient polynomial. The logarithm is passed the integrator's
`analytic` flag, which is essential for valid handling of complex balls near
its branch cut. The two tail bounds are separately added to the enclosure.
See the [Sage integration documentation](https://doc.sagemath.org/html/en/reference/rings_numerical/sage/rings/complex_arb.html#sage.rings.complex_arb.ComplexBallField.integral).

The resulting completed derivatives are strictly positive. Together with the
exact lower bounds in §1, this proves the analytic ranks are precisely two
and three. Since the lower derivatives vanish,
$$L^{(k)}(E,1)/k!=c\Lambda^{(k)}(E,1)/k!.$$
In particular the output certifies the simple rational enclosures
$$
\frac{759}{1000}<\frac{L''(389a1,1)}2<\frac{760}{1000},\qquad
\frac{1731}{1000}<\frac{L'''(5077a1,1)}6<\frac{1733}{1000}.
$$

The full output includes exact dyadic rational endpoints, quadrature enclosure,
both tail bounds, precision, truncation parameters, descent output, and root numbers.
These intervals concern the analytic derivatives. No regulator or period
rationality and no finiteness of the entire Tate–Shafarevich group follow from them.

## 5. Reproduction and checks

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_mellin.py
```

Script: [`certify_mellin.py`](../../compute/scripts/certify_mellin.py).
Output: [`analytic_rank_certificates.json`](../../compute/data/analytic_rank_certificates.json).
The default uses 128-bit balls and $T=80$, with $M=\lceil80/c\rceil$.
An independently truncated run with 96-bit balls, $T=60$, and
$M=\lceil60/c\rceil$ gives overlapping positive enclosures.
The coefficient bounds, analytic branch handling, normalization, and both
infinite-tail estimates are the substantive checks; ordinary floating-point
agreement is not used as an error bound.
