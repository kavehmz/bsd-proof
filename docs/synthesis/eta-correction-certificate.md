# A nonzero eta correction for the actual curve 389a1

Date: 2026-09-12. The analytic identities and normalizations in
[the higher-period note](higher-period-integrality-attack.md) passed
[independent review](review-higher-period-integrality.md). The coordinator
independently rederived the three error bounds below and the Fricke fold
before this certificate was finalized. No historical novelty is claimed.

Let $E=389a1$, $N=389$, and $f(z)=\sum_{n\ge1}a_ne^{2\pi inz}$ its
normalized newform, with $a_1=1$. Use exactly the definitions
$$
x=\log(\sqrt N y),\qquad \rho(x)=y f(iy),
\qquad U(x)=\log\bigl(\eta(iy)\eta(iNy)\bigr)+\frac x2.
$$
Both eta values on this axis are positive, so the logarithms are real.

**[THEOREM, certified calculation with reviewed analytic bounds]** The
even correction integral satisfies
$$
\boxed{110<\mathcal C_E:=
\int_{-\infty}^{\infty}\rho(x)U(x)^2\,dx<111.}
\tag{1}
$$
More precisely its certified enclosure is
$$
\mathcal C_E=110.30304955195\ \mathbin{\pm}\ 3.21\cdot10^{-12},
\tag{2}
$$
where the authoritative endpoints are the exact rational numbers in
[eta_correction_389a1.json](../../compute/data/eta_correction_389a1.json).
The decimal display in (2) is deliberately rounded outward.

Consequently the eta shortcut obtained by discarding this correction
is false on this actual elliptic curve. With
$$
J(s)=\int_0^\infty f(iy)
 \exp\!\left(s\log\bigl(\eta(iy)\eta(iNy)\bigr)\right)dy,
\qquad \ell_E=\frac{L''(E,1)}2,
$$
the already proved identity gives
$$
4\pi J''(0)-\ell_E=4\pi\mathcal C_E>0,
\qquad
\boxed{\ell_E\ne4\pi J''(0).}
\tag{3}
$$
Indeed the difference lies between $440\pi$ and $444\pi$. This refutes
that specific uncorrected second-jet identity; it is not a counterexample
to BSD or to a published first-derivative formula.

## 1. Folding and the exact eta logarithm

The functional-equation sign of $E$ is $+1$, so the weight-two Fricke
eigenvalue is $-1$. As verified in the higher-period review,
$\rho(-x)=\rho(x)$ and $U(-x)=U(x)$. Put
$$
c=\frac{2\pi}{\sqrt N},\qquad t=2\pi y,
\qquad a=\frac{N+1}{24}.
$$
The even fold and the change of variables give
$$
\mathcal C_E=\frac1\pi\int_c^\infty
 f\!\left(\frac{it}{2\pi}\right)W(t)^2\,dt,
\qquad W(t)=U(\log(t/c)).
\tag{4}
$$
There is no extra $\sqrt N$ or period factor in (4):
$\rho(x)dx=f(iy)dy$ and folding contributes two, while
$dy=dt/(2\pi)$.

For $q=e^{-t}$, the defining eta product yields the exact identity
$$
\log\eta\!\left(\frac{it}{2\pi}\right)
=-\frac t{24}-\sum_{n\ge1}b_nq^n,
\qquad b_n=\frac{\sigma_1(n)}n.
\tag{5}
$$
To verify the coefficient, expand
$-\log(1-q^m)=\sum_{j\ge1}q^{mj}/j$ and collect terms with $mj=n$.
The coefficient is $\sum_{j\mid n}1/j=\sigma_1(n)/n$.
All terms are positive and the double series is absolutely convergent
for $0<q<1$, justifying the rearrangement. Moreover
$$
0<b_n\le\frac{n+1}{2}\le n,
\tag{6}
$$
since the sum of positive divisors is at most $1+\cdots+n$.
Thus
$$
W(t)=-at+\frac12\log(t/c)
       -\sum_{n\ge1}b_n(e^{-nt}+e^{-nNt}).
\tag{7}
$$
The calculation uses the exact rational coefficients $b_n$, not a
floating-point implementation of eta.

## 2. Uniform bounds for the integrand

Write $q_0=e^{-c}$ and set
$$
B=\frac{2q_0}{(1-q_0)^2},\qquad P(t)=at+B.
$$
For an integer $K\ge1$, let $W_K$ be (7) with its sum truncated at $K$.
For this curve $a>1/(2c)$; the script checks this with real balls.
For $t\ge c$, $\log(t/c)\le t/c-1$, giving
$$
W(t)\le W_K(t)
\le-\left(a-\frac1{2c}\right)t-\frac12<0.
$$
On the other hand, the logarithmic term is nonnegative and (6) gives
$$
\sum_{n\ge1}b_n(e^{-nt}+e^{-nNt})
\le\frac{2e^{-t}}{(1-e^{-t})^2}\le B.
$$
Consequently
$$
|W(t)|\le P(t),\qquad |W_K(t)|\le P(t).
\tag{8}
$$

The eta truncation error is bounded uniformly on this half-line by
$$
|W-W_K|\le\delta_K:=
2q_0^{K+1}\left(\frac{K+1}{1-q_0}
                   +\frac{q_0}{(1-q_0)^2}\right).
\tag{9}
$$
Indeed this is twice the exact sum $\sum_{n>K}nq_0^n$, which bounds
both positive tails in (7). Combining (8) and (9),
$$
|W^2-W_K^2|\le2\delta_K P(t).
\tag{10}
$$
No additional $\delta_K^2$ is required: each of the two factors in
$|W-W_K|\,|W+W_K|$ has already been bounded directly.

Let $f_M(t)=\sum_{n=1}^M a_ne^{-nt}$. The Euler factors and Hasse
bound give $|a_n|\le d(n)\sqrt n\le2n$, as proved in the
[Mellin certificate](analytic-rank-certificates.md). Thus
$$
|f_M(t)|,\quad\left|f\!\left(\frac{it}{2\pi}\right)\right|
\le\frac{2e^{-t}}{(1-e^{-t})^2}.
\tag{11}
$$
In particular all integrals and error estimates below converge absolutely.

## 3. Three explicit errors

The finite integral evaluated by Arb is
$$
I_{M,K,T}=\frac1\pi\int_c^T f_M(t)W_K(t)^2\,dt,
\qquad T\ge c.
$$
The difference from (4) is split into omitted Fourier coefficients,
the eta approximation, and the omitted integration interval.

**[NEW, elementary bound; coordinator-reviewed] Fourier error.** Put
$P_0=ac+B$. Then
$$
E_f=\frac2\pi\frac{q_0^{M+1}}{1-q_0}
 \left(P_0^2+\frac{2aP_0}{M+1}
                     +\frac{2a^2}{(M+1)^2}\right)
\tag{12}
$$
is an upper bound for the first error.

*Proof.* For $n>M$, substituting $t=c+v$ gives
$$
\int_c^\infty e^{-nt}P(t)^2dt
=e^{-nc}\left(\frac{P_0^2}{n}
 +\frac{2aP_0}{n^2}+\frac{2a^2}{n^3}\right).
$$
Multiply by $|a_n|/\pi\le2n/\pi$, replace $n$ in denominators by
$M+1$, and sum the remaining geometric series. This bounds the
coefficient error on $[c,T]$ by bounding the larger interval. $\square$

**[NEW, elementary bound; coordinator-reviewed] Eta error.** An upper
bound for the second error is
$$
E_\eta=\frac{4\delta_K}{\pi}
 \frac{q_0}{(1-q_0)^2}\bigl(a(c+1)+B\bigr).
\tag{13}
$$

*Proof.* Apply (10) and (11), replace $(1-e^{-t})^{-2}$ by
$(1-q_0)^{-2}$, and integrate over $[c,\infty)$.
The remaining elementary integral is
$\int_c^\infty e^{-t}(at+B)dt=e^{-c}(a(c+1)+B)$. $\square$

**[NEW, elementary bound; coordinator-reviewed] Integration error.**
Writing $P_T=aT+B$, the third error is at most
$$
E_T=\frac2\pi\frac{e^{-T}}{(1-e^{-T})^2}
       \bigl(P_T^2+2aP_T+2a^2\bigr).
\tag{14}
$$

*Proof.* Use (8) and (11) on $[T,\infty)$ and bound the denominator
by its value at $T$. Substitute $t=T+v$ and integrate the quadratic
polynomial against $e^{-v}$. $\square$

It follows that
$$
|\mathcal C_E-I_{M,K,T}|\le E_f+E_\eta+E_T.
\tag{15}
$$
The use of whole half-lines for the first two upper bounds is harmless
overcounting and does not assume cancellation among Fourier coefficients.

## 4. Recorded computation and software checks

The [script](../../compute/scripts/certify_eta_correction.py) uses
Sage 10.7, 96-bit real and complex balls, $T=40$, and
$M=K=\lceil60/c\rceil=189$. It obtains

| Quantity | Certified outward bound/display |
|---|---:|
| $I_{M,K,T}$ | $110.3030495519480638493\ \pm\ 1.14\cdot10^{-20}$ |
| $E_f$ | $<7.42\cdot10^{-24}$ |
| $\delta_K$ | $<7.30\cdot10^{-24}$ |
| $E_\eta$ | $<3.72\cdot10^{-21}$ |
| $E_T$ | $<1.273\cdot10^{-12}$ |

Its exact final rational endpoints are
$$
\frac{4267142546738570554881062447}{38685626227668133590597632}
\le\mathcal C_E\le
\frac{4267142546738669025801909807}{38685626227668133590597632}.
\tag{16}
$$
Exact rational comparison verifies that these endpoints lie strictly
between 110 and 111. This proves (1).

The finite Fourier polynomial uses exact PARI coefficients through
Sage `anlist`; all these indices lie within the independently
point-counted coefficient range of
[the earlier analytic review](review-analytic-certificates.md).
The eta polynomial coefficients are computed as exact rational numbers.
Both polynomials use Horner evaluation. The only branch-sensitive
function in the finite integrand is $\log(t/c)$, and the callback
passes Arb's `analytic` flag to it. The implementation checks finite
real and imaginary enclosures, includes zero in the imaginary part,
and adds upper bounds of all three real error balls to the radius.
The integration contract and outward-endpoint semantics are the same
ones already checked in the earlier review.

No complex analytic-rank estimate, Sha order, regulator equality,
or arithmetic rationality assertion is needed for this integral
certificate. The known rank-two analytic vanishing is needed only
when applying the separately proved identity (3).

**Independent implementation check.** The coordinator ran a second
computation with `--bits 128 --cutoff 50 --decay 70`, giving
$M=K=220$. Its full correction enclosure is
$$
\mathcal C_E=110.303049551948660\ \mathbin{\pm}\ 1.53\cdot10^{-16}.
$$
The integration tail is below $8.84\cdot10^{-17}$. Exact fraction
comparison verifies that this interval is strictly contained in (16).
The secondary output is
`.tools/research-2026-09-12/eta_correction_check.json`, with SHA-256
`c3e9e74dcda5761dd41b1505037a30cb4c92aacf17c89c9f18bc7edf57e84b15`.
The principal certificate remains the reproducible JSON linked above.
In particular, the many displayed digits of the finite integral in
the table must not be treated as that many certified digits of the
full correction before adding its tail.

## 5. Reproduction and effect on the proof attempt

From the repository root:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python \
  compute/scripts/certify_eta_correction.py
```

The output path defaults to
`compute/data/eta_correction_389a1.json`. Different precision and
cutoffs can be chosen with `--bits`, `--cutoff`, `--decay`, and
`--out`. The script checks strict positivity after adding all errors.

Recorded SHA-256 values:

* Script: `5ae8b09bd1baea01ad7a67b5e1205375001cc34304c1311f0a4dd9f18750ab68`.
* Principal JSON: `296d02a17662ee81a581fefd5e8790336d0b2430478df99becc923e1999902c9`.

The correction in the higher-period note is now proved nonzero,
rather than merely not eliminated by parity. The viable eta approach
must retain the exact difference $J''(0)-\mathcal C_E$ and construct
its arithmetic regulator interpretation. The present result supplies
no rational or integral interpretation of that difference and does
not resolve BSD.
