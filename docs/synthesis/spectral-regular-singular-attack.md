# Spectral cusp jets and finite regular-singular expressions

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
The `[NEW]` deductions below passed
[independent review](review-spectral-regular-singular.md). The goal remains
full BSD over Q; no obstruction to an integrated BSD period is proved.

## 1. Result and exact scope

The first Fourier mode of each spectral jet $A_1,A_2$ of
$E_\infty(z,s)$ at $s=1$ contains a factorially divergent inverse-height
sector. We compute that sector exactly at both cusps of $X_0(389)$.
It persists in $A_2+cA_1+dA_0$ for all constant $c,d$.

We then prove a functional exclusion for a specified class of finite
regular-singular period expressions. The class permits rational operations,
inverse powers of $\log|q|$, logarithms of Hodge norms, and convergent
Puiseux series in inverse height. It includes the canonical height of an
admissible finite biextension variation in the explicit local charts
verified in §6. It does not include arbitrary arithmetic metrics or
inverse-Laplacian operations by definition.

The conclusion is about equality of the actual functions $A_1,A_2$
near a cusp. It does not exclude a motive with the same integrated scalar,
a different regulator identity, or root's separate construction using an
arbitrarily specified arithmetic metric. The real leading-term comparison
remains open.

## 2. Exact Fourier coefficients at the two cusps

Use the same effective orbifold, width-one cusp scalings and Laurent
subtraction as in [the reviewed Mellin note](mellin-variation-attack.md).
Put $N=389$, $q=e^{2\pi i z}$ and
$$\xi(v)=\pi^{-v/2}\Gamma(v/2)\zeta(v).$$
The normalized level-one Fourier expansion has nonzero mode $n\ne0$
$$\frac{2\sqrt y}{\xi(2s)}|n|^{s-1/2}
 \sigma_{1-2s}(|n|)K_{s-1/2}(2\pi|n|y)e^{2\pi inx}.$$
The factor two counts one Fourier sign; the positive cosine sum has
factor four. The normalization was derived by Poisson summation in the
Mellin note. Its exact level identities are
$$E_\infty(z,s)=\frac{N^sE(Nz,s)-E(z,s)}{N^{2s}-1},\qquad
E_\infty(\sigma_0z,s)=E_0(z,s)
 =\frac{N^sE(z,s)-E(Nz,s)}{N^{2s}-1}. \tag{2.1}$$

For $n\ge1$, define
$$\begin{aligned}
S_{\infty,n}(s)&=
 \frac{N\,1_{N\mid n}\sigma_{1-2s}(n/N)-\sigma_{1-2s}(n)}{N^{2s}-1},\\
S_{0,n}(s)&=
 \frac{N^s\sigma_{1-2s}(n)-N^{1-s}1_{N\mid n}\sigma_{1-2s}(n/N)}{N^{2s}-1},\\
h_{a,n}(s)&=\frac{n^{s-1}S_{a,n}(s)}{\xi(2s)}.
\end{aligned} \tag{2.2}$$
At cusp $a$, the $n$th Fourier coefficient is exactly
$$e^{-2\pi ny}h_{a,n}(s)
 \frac{K_{s-1/2}(2\pi ny)}{K_{1/2}(2\pi ny)}. \tag{2.3}$$
Indeed replacing $z$ by $Nz$ contributes $\sqrt N$ to the square-root
factor and $N^{1/2-s}$ from the Fourier index. Together with $N^s$
in (2.1), this gives the factor $N$ in the first numerator of (2.2).
The second formula follows by the same substitution without that factor.

For the first Fourier mode put $H_a(s)=h_{a,n=1}(s)$ and write
$H_a(1+t)=h_{a,0}+h_{a,1}t+h_{a,2}t^2+O(t^3)$,
where the second subscript on the right denotes the Taylor order.
The coefficients needed below are completely fixed:
$$h_{\infty,0}=-\frac6{\pi(N^2-1)},\qquad
h_{0,0}=\frac{6N}{\pi(N^2-1)}, \tag{2.4}$$
$$\begin{aligned}
\beta_\infty&=-2\frac{\xi'(2)}{\xi(2)}
                      -\frac{2N^2\log N}{N^2-1},\qquad
\beta_0=\beta_\infty+\log N,\\
\lambda&=-4(\log\xi)''(2)
                    +\frac{4N^2(\log N)^2}{(N^2-1)^2},\\
h_{a,1}&=h_{a,0}\beta_a,\qquad
h_{a,2}=\tfrac12h_{a,0}(\beta_a^2+\lambda).
\end{aligned} \tag{2.5}$$
These formulas retain the level and gamma/zeta derivatives. They do
not depend on a choice of finite part of the Eisenstein pole: the
pole is constant in $z$ and affects only the zero Fourier mode.

For completeness, with $R=3/[\pi(N+1)]$ and the exact scattering
coefficients $R/t+c_a+d_at+e_at^2+\cdots$, the zero-mode jets remain
$$\begin{aligned}
(A_1)_a^{(0)}&=\delta_{a\infty}y\log y+d_a-c_a\log y
                                      +\tfrac R2(\log y)^2,\\
(A_2)_a^{(0)}&=\tfrac12\delta_{a\infty}y(\log y)^2+e_a-d_a\log y
                     +\tfrac12c_a(\log y)^2-\tfrac R6(\log y)^3.
\end{aligned} \tag{2.6}$$
The scattering functions defining $c_a,d_a,e_a$ are (2.2) of the
Mellin note. Nothing in the test below removes these constants or
uses their log-log terms as the obstruction.

## 3. The actual order derivatives of the Bessel factor

For $Z>0$ put
$$\mathcal K(t,Z)=\frac{K_{1/2+t}(Z/2)}{K_{1/2}(Z/2)},\qquad
J(Z)=e^Z E_1(Z)=\int_0^\infty\frac{e^{-v}}{Z+v}\,dv,$$
where $E_1(Z)=\int_Z^\infty e^{-u}du/u$.

**[NEW] Proposition 3.1 (two exact order derivatives).**
$$\partial_t\mathcal K(0,Z)=J(Z),\qquad
\partial_t^2\mathcal K(0,Z)=2H(Z),\qquad
H(Z)=\int_Z^\infty\frac{J(u)}u\,du. \tag{3.1}$$

*Proof.* The real integral for $K_\nu$ gives, after two changes of
variables,
$$\mathcal K(t,Z)=\frac1{\Gamma(1+t)}
       \int_0^\infty e^{-v}v^t(1+v/Z)^t\,dv. \tag{3.2}$$
For $t$ in a small complex neighborhood of zero the integral and its
first two $t$ derivatives are dominated by an integrable function.
The derivative of $v^t/\Gamma(1+t)$ integrates to zero. Hence the
first derivative is $\int e^{-v}\log(1+v/Z)dv$. Integration by
parts gives $J(Z)$.

The Bessel differential equation, after this normalization, reads
$$\partial_Z^2\mathcal K-\partial_Z\mathcal K
                         -\frac{t+t^2}{Z^2}\mathcal K=0.$$
Writing $J_2=\partial_t^2\mathcal K(0,Z)$ gives
$J_2''-J_2'=2(1+J)/Z^2$. Since $J'=J-1/Z$, the function $2H$
in (3.1) satisfies the same equation. Formula (3.2) shows $J_2\to0$
as $Z\to\infty$, and $H\to0$ there as well. The difference solves
$v''-v'=0$, whose only solution tending to zero is zero. This proves
the second equality. $\square$

The integral used in (3.2) is
[DLMF 10.32.8](https://dlmf.nist.gov/10.32.E8), with
$\Re\nu>-1/2$ and positive argument. The first derivative also agrees
with [DLMF 10.38.7](https://dlmf.nist.gov/10.38.E7). The second
derivative and the following remainder bounds are proved above and below;
no unverified differentiation of an infinite asymptotic series is needed.

**[NEW] Proposition 3.2 (factorial asymptotics with bounds).** For
every integer $M\ge1$,
$$\begin{aligned}
J(Z)&=\sum_{k=1}^M\frac{(-1)^{k-1}(k-1)!}{Z^k}+r_M(Z),
&|r_M(Z)|&\le\frac{M!}{Z^{M+1}},\\
H(Z)&=\sum_{k=1}^M\frac{(-1)^{k-1}(k-1)!}{kZ^k}+s_M(Z),
&|s_M(Z)|&\le\frac{M!}{(M+1)Z^{M+1}}.
\end{aligned} \tag{3.3}$$

*Proof.* Expand $1/(Z+v)$ by the finite geometric identity with
remainder $(-1)^Mv^M/[Z^M(Z+v)]$. Integrating against $e^{-v}$
gives the first formula and bound. Integrate that bound after division
by $Z$, from $Z$ to infinity, to obtain the second formula and bound.
$\square$

In particular these are genuine Poincaré asymptotic series but have
zero radius of convergence as power series in $1/Z$.

## 4. The nonzero Fourier sector cannot be cancelled by lower jets

Let $a_j(y)$ be the positive first Fourier coefficient of $A_j$ at
one of the two cusps, and put $Z=4\pi y$. Equations (2.3) and
(3.1) give
$$\begin{aligned}
e^{2\pi y}a_0(y)&=h_{a,0},\\
e^{2\pi y}a_1(y)&=h_{a,1}+h_{a,0}J(Z),\\
e^{2\pi y}a_2(y)&=h_{a,2}+h_{a,1}J(Z)+h_{a,0}H(Z).
\end{aligned} \tag{4.1}$$
The last formula uses a Taylor coefficient, so the factor $1/2$ on
the second order derivative in (3.1) has already been applied.

For $k\ge1$ the inverse-$Z$ coefficient in the last line is
$$(-1)^{k-1}(k-1)!\left(h_{a,1}+\frac{h_{a,0}}k\right). \tag{4.2}$$
Since $h_{a,0}\ne0$ at both cusps, these coefficients have unbounded
$k$th root. If $h_{a,1}\ne0$ this follows from the first summand;
if $h_{a,1}=0$ the remaining factorial divided by $k$ still has that
property. Replacing $A_2$ by $A_2+cA_1+dA_0$ only replaces
$h_{a,1}$ in (4.2) by $h_{a,1}+ch_{a,0}$. The same argument
therefore applies for every pair of constants $c,d$. The remainder
bounds in (3.3) prove this conclusion for the actual functions, not
only for a formally written Bessel series.

## 5. A period-expression class allowing inverse logs and Hodge norms

This section states the function-space hypothesis before using it.
Let $z=1/y>0$. Write
$$\mathcal L=\bigcup_{e\ge1}\mathbb C(\{z^{1/e}\})(\log z), \tag{5.1}$$
where $\mathbb C(\{z^{1/e}\})$ is the field of convergent meromorphic
Puiseux germs. The final parentheses mean rational functions of
$\log z$, with such germs as coefficients. In particular $\mathcal L$
contains $y$, $1/y$, $\log y$, arbitrary rational functions of those,
and $\log P(y)$ for every eventually positive nonzero rational function
$P$: factor $P(y)=c y^d(1+O(1/y))$ and use the convergent logarithm
of its last factor. No factorially divergent formal series is admitted
as a convergent germ.

Call a single-valued cusp function *finite logarithmic-sector type* if,
after a finite ramified cusp cover if needed, it has a normally convergent
expansion
$$\sum_{a,b\in e^{-1}\mathbb Z,\ a+b\ge-M}
          q^a\bar q^b\,r_{ab}(y),\qquad r_{ab}\in\mathcal L, \tag{5.2}$$
with these precise additional conditions. Terms of any fixed total
exponential order are finite in number. After truncation at any such
order, the remainder, uniformly in the angular variable, is bounded
by the next exponential order times a power of $y$ and $\log y$.
Coefficients with a nonintegral angular frequency vanish when the
function is viewed on the original cusp. These conditions are part of
the class; they are not inferred from the phrase “real analytic”.
The lower bound is on total order, not on the exponents separately:
the permitted inverse $1/(q+\bar q^2)$ expands as
$\sum_{j\ge0}(-1)^j q^{-j-1}\bar q^{2j}$, whose total orders are
$j-1$ although its first exponent is unbounded below.

**[NEW] Lemma 5.1 (no divergent pure-power expansion inside $\mathcal L$).**
If $r\in\mathcal L$ admits a Poincaré asymptotic expansion in integer
powers of $z$ to every order, with constant coefficients and no logarithms,
then that power series converges near zero.

*Proof.* Choose $u=z^{1/e}$ so that
$r=P(u,\log u)/Q(u,\log u)$ with polynomial dependence on the second
variable and convergent meromorphic coefficients. Formal division in
$u$ gives coefficients that are rational functions of $\log u$.
For a fixed truncation this is also an asymptotic expansion: the leading
coefficient of $Q$ is a nonzero polynomial in $\log u$, which has no
zeros for sufficiently small positive $u$, and the next $u$ term is
smaller than it by a positive power times a log power.

Compare successively with the assumed pure-power expansion. A nonzero
rational function of $\log u$ cannot be bounded by any positive power
of $u$. Thus each formal coefficient must equal the prescribed constant
at exponents divisible by $e$, and must be zero otherwise. Let $A(u)$
be this formal series. The formal identity $P=QA$ holds as a polynomial
identity in the independent variable $\log u$. Choose a nonzero
coefficient $Q_j(u)$ of that polynomial; then
$A(u)=P_j(u)/Q_j(u)$ is a convergent meromorphic germ. Its nonnegative
series has only powers divisible by $e$, and so is a convergent power
series in $z$. $\square$

**[NEW] Proposition 5.2 (functional exclusion).** Neither $A_1$ nor
$A_2+cA_1+dA_0$ is of finite logarithmic-sector type, for any constants
$c,d$. This holds at each of the two cusps.

*Proof.* Extract the first angular Fourier mode in (5.2). Any terms
with decay slower than $e^{-2\pi y}$ must vanish: a nonzero coefficient
in $\mathcal L$ has at most power/log growth or decay and cannot
cancel a distinct exponential order. The term of order $e^{-2\pi y}$
has $a=1,b=0$, and its coefficient is an element $r_{10}\in\mathcal L$.
All subsequent terms are smaller by a fixed positive exponential,
times power/log factors. Therefore $r_{10}$ has the same all-orders
inverse-$y$ expansion as the normalized coefficient (4.1). That
expansion is factorially divergent by §4, contradicting Lemma 5.1.
$\square$

## 6. Which finite regular-singular constructions satisfy the hypothesis?

The following inclusion identifies an actual geometric class to which
Proposition 5.2 applies; it is not a claim about every possible metric.

For a finite regular-singular connection with quasi-unipotent monodromy,
pass to a finite cusp cover to make its monodromy unipotent. A fundamental
period matrix has the form
$$P(q)=H(q)\exp((\log q)N), \tag{6.1}$$
where $N$ is a constant nilpotent matrix and $H$ is a convergent
meromorphic matrix germ. This also follows directly from the logarithmic
connection model: its solutions have moderate growth; untwisting the
unipotent monodromy gives a single-valued holomorphic matrix on the
punctured disc with moderate growth, hence only a finite pole at zero.
The nilpotent exponential is a finite polynomial in $\log q$.

We allow finite sums, products and rational matrix operations on finitely
many such period matrices and their conjugates. For an inverse operation
we require its leading denominator, after factoring a monomial in
$q,\bar q$, to be a nonzero polynomial in the logarithmic variables.
The residual leading denominator must also satisfy a uniform lower bound
$|D_0(x,y)|\ge C y^{-A}(1+\log y)^{-B}$ for all $x$ in a full
cusp period and all sufficiently large $y$, for some $C>0$ and finite
$A,B\ge0$. A nonzero polynomial that vanishes at one angle does not
satisfy this chart condition. The inverse is expanded by the convergent
geometric series in the positive exponential remainder only after this
uniform condition is checked. For logarithms of positive Hodge norms,
require that the leading norm be a nonzero positive rational function
of $y$, times a monomial $|q|^c$. These are explicit chart conditions;
they allow poles and inverse log powers. They do not allow inversion
across a denominator whose residual nilpotent-orbit value, after the
specified monomial factor, vanishes identically, or
an arbitrary real-analytic function applied to a period entry.
After the permitted norm logarithms have been taken, further rational
operations are also allowed when their leading coefficient is a nonzero
element of $\mathcal L$. Such a coefficient has only power/log growth
or decay, so dividing a positive exponential remainder by it still
gives a convergent geometric expansion. In particular rational operations
on $\log y$ itself, such as $1/(1+\log y)$, are not excluded.

**[NEW] Lemma 6.1 (closure for these finite constructions).** A
single-valued scalar obtained by these operations satisfies (5.2).

*Proof.* Before inversion, its expansion has convergent $q,\bar q$
coefficients polynomial in $\log q,\log\bar q$. Inverting the specified
denominator makes each coefficient rational in these logarithms. For
each fixed exponential order only finitely many terms of a geometric
inverse or logarithm series contribute. The remainder estimates follow
because an exponential times any fixed log polynomial tends to zero.

Single-valuedness removes dependence of each coefficient on the angular
logarithm: a rational function periodic under
$(\log q,\log\bar q)\mapsto(\log q+2\pi i,\log\bar q-2\pi i)$
is independent of their difference. One can check coefficientwise
uniqueness by fixing a total exponential order: its finitely many
angular exponentials are linearly independent over rational functions
of the angle, as follows by analytic continuation to imaginary angle
and successive comparison of exponential growth. Thus the coefficients
before the extra norm logarithms are rational functions of $y$.
The logarithm of the leading norm is $c\log|q|+\log P(y)$, which
belongs to $\mathcal L$; positive exponential terms of its logarithm
have rational-in-$y$ coefficients. Further permitted sums, products
and inverses retain coefficients in $\mathcal L$. This proves the
class conditions and their uniform remainder bounds. $\square$

For period maps of polarized variations, the needed holomorphic
untwisting and validity of the nilpotent orbit are the one-variable
theorem [Schmid, Invent. Math. 22 (1973), Theorem 4.9](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/schmid.pdf).
For admissible graded-polarized mixed variations, the local form
$F(\tau)=e^{\tau N}e^{\Gamma(q)}F_\infty$ with holomorphic $\Gamma$
is recorded in [Brosnan–Pearlstein, §2, equation (48)](https://arxiv.org/html/1701.05527).
The nilpotent orbit remains in the appropriate period domain for
sufficiently large $y$.

Here is a checked canonical-height application. In a finite biextension
mixed Hodge structure with weights $0,-1,-2$, the Deligne bigrading
can be computed by finite sums, intersections and kernels of the
filtrations $F,\bar F,W$. Explicitly,
$$I^{p,q}=F^p\cap W_{p+q}\cap
 \left(\bar F^q\cap W_{p+q}
       +\sum_{j\ge1}\bar F^{q-j}\cap W_{p+q-j-1}\right).$$
Only finitely many summands are nonzero. In a fixed rank chart these are rational
matrix operations, obtained by Gaussian elimination. Its grading $Y$
is consequently rational in those period and conjugate-period entries.
Since the splitting operator $\delta$ lowers weight by two and there
are only three weights, its defining equation reduces to
$$\bar Y=e^{-2i\operatorname{ad}\delta}Y=Y-4i\delta,
\qquad\delta=\frac{Y-\bar Y}{4i}. \tag{6.2}$$
The canonical biextension height is the scalar in $2\pi\delta=h\eta$
for the fixed extreme frames. These identities are the definitions
and equation (37) in Brosnan–Pearlstein §2, Definition 40.

The required rank charts can be chosen on the nilpotent orbit itself.
For a biextension height, first remove the real factor $e^{xN}$:
it is an isomorphism of real mixed Hodge structures preserving both
extreme frames, so the height is unchanged. The remaining nilpotent
orbit is $e^{iyN}F_\infty$. Its ranks are the fixed Hodge numbers,
so each chosen nonzero pivot minor is a polynomial in $y$. It stays
nonzero for all sufficiently large $y$. The holomorphic $q$ correction
is exponentially smaller, uniformly for $x$ in a full cusp period,
and hence preserves those same pivots. This supplies the uniform chart
condition in Lemma 6.1, rather than only a calculation on the ray $x=0$.
Hodge norm matrices are likewise obtained from Hodge projections and
the fixed polarization by finite rational linear algebra. On a chart
with nonvanishing nilpotent-orbit norm, their logarithms are precisely
the permitted norm logarithms. Finite products and determinants of
these canonical biextension heights satisfy the same inclusion.

This justifies applying Proposition 5.2 to these canonical finite
biextension/period expressions. It does not assert that arbitrary
metrics on an arithmetic line bundle are functions of a period matrix,
or that an integrated regulator must retain this pointwise cusp shape.

## 7. Consequence for the current comparison problem

The obstruction here is the nonzero Fourier sector (4.2), not the
zero-mode powers of $\log y$. The latter are allowed in (5.1), as
are $1/y$, $\log y$, rational operations on them, and logarithms
of nonvanishing nilpotent-orbit Hodge norms.

Thus a literal equality of $A_2$, or its constant lower-jet corrections,
with the specified finite canonical period/height expression would
contradict its computed Fourier coefficient. This strengthens the earlier
homogeneous-Casimir test in a delimited direction: the present class
includes rational operations and the explicitly justified biextension
splitting/height functions.

It does not rule out root's actual arithmetic-metric construction,
which can prescribe a real-analytic metric outside this canonical
period-expression class. Nor does it rule out a different motive or
secondary cycle producing the integrated scalar
$\ell_E L(f,2)$, or a comparison after adding further currents and
boundary data. The exact MT-389 rational determinant comparison
therefore remains required; full BSD is neither proved nor disproved.
