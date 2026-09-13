# Independent review of spectral cusp jets and regular-singular expressions

Date: 2026-09-12. Reviewer: /root/uniform_witness, GPT-6 Astra/xhigh.
Reviewed [proof](spectral-regular-singular-attack.md) and
[checkpoint](spectral-regular-singular-checkpoint.md).

**PASS after the two recorded closure/chart repairs.**
The Fourier/Bessel identities, remainder bounds, coefficient-field
lemma, functional exclusion and canonical biextension inclusion
are verified in their final stated scope. No correction remains.
The exclusion concerns literal functions in the specified class.
It is not an exclusion of motives realizing the same integrated scalar.

Initial reviewed proof SHA256:
5102b6c16a49f7f3a70a91efad5b3cffd7b1b7b65ee247ee024b1330fe2fa437.
After the first closure correction:
366daef52cfda5da5dd776d5d123a6fe5c8ab19294c28a2abf94ac7c1c2dec89.
Final reviewed proof SHA256:
48aff42380152a3c965ed62889fca23ce05bc5c0bf7e7a3a163698e03cc3e097.
Final reviewed checkpoint SHA256:
ef5766ac8035b4036312a822df25b207e2e92f53278b9ca3f5658196339c60cd.
Subsequent PASS links and checkpoint status updates are editorial.

## 1. Fourier factors at both cusps

The level-one normalization and width-one cusp scalings are the
inputs already checked in [review-mellin-variation.md](review-mellin-variation.md).
The present level conversion has the right factors. In the term
$N^sE(Nz,s)$, replacing the Fourier index by n/N contributes
$N^{1/2-s}$, while the square-root height contributes $\sqrt N$.
Their product with $N^s$ is N. This accounts for the first
numerator of (2.2). In the cusp-zero formula, the unsubsidized
$E(Nz,s)$ contributes $N^{1-s}$ instead. The indicator
$1_{N\mid n}$ is necessary and retained.

The elementary formula
$K_{1/2}(2\pi ny)=e^{-2\pi ny}/(2\sqrt{ny})$ changes the
prefactor $2\sqrt y\,n^{s-1/2}$ to $n^{s-1}$, so (2.3)
is the coefficient of one positive Fourier sign, with no
missing factor two from the corresponding cosine.

At n=1, $\xi(2)=\pi/6$ gives both constants in (2.4).
Differentiating the logarithm of $H_a(s)$ reproduces $\beta_a$
and $\lambda$ in (2.5); specifically, the second derivative of
$-\log(N^{2s}-1)$ is
$4N^{2s}(\log N)^2/(N^{2s}-1)^2$.
The difference $\beta_0-\beta_\infty=\log N$ is correct.
$h_{a,2}$ is a Taylor coefficient and hence contains the factor
one-half displayed in the proof.

Expanding the exact zero mode
$\delta_{a\infty}y^{1+t}+
(R/t+c_a+d_at+e_at^2+\cdots)y^{-t}$ verifies (2.6).
The spatially constant pole subtraction does not affect any
nonzero Fourier coefficient. No zero-mode scattering constant
is being used as the asserted obstruction.

## 2. Bessel order derivatives and rigorous remainders

The primary integral
[DLMF 10.32.8](https://dlmf.nist.gov/10.32.E8)
applies at positive argument and $\operatorname{Re}\nu>-1/2$.
With $\nu=1/2+t$ and argument Z/2, first replace its integration
variable by $1+2v/Z$. Dividing by $K_{1/2}(Z/2)$ gives exactly
the gamma integral (3.2). For small complex t its differentiated
integrands are bounded by $e^{-v}$ times fixed powers of v,
$1+v$, and $|\log v|$, all integrable in the required range.
The first derivative reduces to
$\int_0^\infty e^{-v}\log(1+v/Z)\,dv$ because the normalized
gamma integral has constant value one. Integration by parts
gives J. This also agrees with
[DLMF 10.38.7](https://dlmf.nist.gov/10.38.E7).

For the second derivative the normalized differential equation
is correct:
$$
 \mathcal K_{ZZ}-\mathcal K_Z
       -\frac{t+t^2}{Z^2}\mathcal K=0.
$$
The first derivative satisfies $J'=J-1/Z$. Therefore
$H'=-J/Z$ and
$H''-H'=(1+J)/Z^2$, precisely half the equation for the
second order derivative. Both solutions tend to zero at
positive infinity, as follows by dominated convergence in
the gamma integral. Their difference solves $u''-u'=0$;
neither a nonzero constant nor a nonzero multiple of $e^Z$
tends to zero. This proves (3.1) for the actual functions.

The finite identity
$$
 \frac1{Z+v}=\sum_{j=0}^{M-1}\frac{(-v)^j}{Z^{j+1}}
             +\frac{(-v)^M}{Z^M(Z+v)}
$$
gives the stated J remainder bounded by $M!/Z^{M+1}$.
Integrating this bound against $du/u$ from Z to infinity
gives $M!/((M+1)Z^{M+1})$ for H. This is a legitimate
finite remainder calculation; no infinite divergent series
was differentiated or integrated as a convergent expansion.

The $t^2$ coefficient of $\mathcal K$ is H, so multiplying
by $h_0+h_1t+h_2t^2$ gives all of (4.1) with the right
factor. The inverse-Z coefficient for the second jet is
$( -1)^{k-1}(k-1)!(h_1+h_0/k)$.
If $h_1\ne0$ its bracket is bounded away from zero for large
k; if $h_1=0$, the remaining division by k does not remove
factorial growth. Replacing $h_1$ by $h_1+ch_0$ covers every
constant lower-jet correction. The nonzero h0 at both cusps
is what makes the conclusion uniform in those corrections.

## 3. The coefficient-field convergence lemma

For $u=z^{1/e}$, write
$r=P(u,\log u)/Q(u,\log u)$ with P,Q polynomial in the
second variable and convergent meromorphic coefficients
in u. Expand formally in u over the field $\mathbb C(T)$.
For any finite truncation the formal division also gives
an asymptotic expansion along positive u: its leading
denominator polynomial in $\log u$ is eventually nonzero,
and positive powers of u dominate all fixed logarithmic
factors. Possible finitely many initial Laurent powers
can be handled before the nonnegative expansion begins.

Suppose the resulting function has the full integer-power
expansion in z in Lemma 5.1. If the first coefficient in
the u-expansion differing from the prescribed constant
series were a nonzero rational function of $\log u$,
comparison one positive u-order farther would require
that rational function to decay like a positive power
of u. Its Laurent behavior at $\log u=-\infty$ forbids
this. Thus every formal coefficient equals the prescribed
constant or zero, according to its exponent.

Writing this constant formal series as A(u), the identity
P=QA holds in $\mathbb C(T)((u))$. Comparing coefficients
of T gives $P_j(u)=Q_j(u)A(u)$. Choose any nonzero Q_j:
then A is the quotient of two convergent meromorphic
germs. Hence its formal series actually converges.
Only powers divisible by e occur, which proves the
claimed convergence in z. The argument does not assume
that the earlier division in u over $\mathbb C(T)$ was
itself an infinite convergent expansion.

After angular Fourier extraction, total exponential
order one and angular frequency one uniquely force
$(a,b)=(1,0)$, even when a or b individually can be
negative. The remainder after that order is exponentially
smaller, hence has zero power asymptotic expansion in
1/y to every order. Lemma 5.1 would make the remaining
coefficient's power expansion convergent, contradicting
the factorial coefficients. This proves the exclusion
in Proposition 5.2 for the correctly defined sector class.

## 4. Closure correction and the chart condition

The original definition imposed separate lower bounds
$a,b\ge-M$ in (5.2). That is not preserved by the stated
rational inverses. For example
$$
 \frac1{q+\bar q^2}
  =\sum_{j\ge0}(-1)^j q^{-j-1}\bar q^{2j}.
$$
The leading denominator is the monomial q times the
nonzero coefficient one; the remaining geometric
parameter has absolute value $|q|$ uniformly in angle.
This is an allowed single-valued inverse, but its
first exponent has no lower bound.

The author has repaired the definition to require only
$a+b\ge-M$, retaining the discrete exponent lattice,
finitely many terms at each total order, normal
convergence, and uniform exponential remainder bounds.
The example has total orders j-1 and belongs to this
corrected class. The proof in §3 above confirms that
the Fourier exclusion survives this enlargement.

The second clarification has also been applied: every chosen
leading denominator must remain nonzero on the whole angular
strip with a uniform power/log lower bound. Being a
nonzero polynomial in both logarithmic variables alone
does not imply that: it can vanish at a fixed angle.
The final proof explicitly imposes
$|D_0(x,y)|\ge C y^{-A}(1+\log y)^{-B}$ on that full strip
for all sufficiently large y. This chart condition makes the geometric
inverse expansion and its uniform tails valid.
The canonical biextension construction below already
provides the stronger property by reducing its pivot
polynomials to functions of y alone.

## 5. Canonical biextensions and uniform angular control

The primary Hodge inputs were read in
[Schmid, Invent. Math. 22 (1973), Theorem 4.9, printed p. 231](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/schmid.pdf)
and
[Brosnan-Pearlstein, arXiv:1701.05527, §2](https://arxiv.org/html/1701.05527#S2).
Schmid supplies holomorphic untwisting, the nilpotent
orbit, and its exponentially small approximation
uniformly in horizontal strips for polarized variations.
Brosnan-Pearlstein equation (48) gives the admissible
mixed local form, with holomorphic $\Gamma(q)$ vanishing
at zero; its applicability after a finite cover retains
the quasi-unipotent hypothesis.

Finite regular-singular period matrices, after killing
their finite monodromy, have a meromorphic untwisted
matrix times a finite polynomial in $\log q$.
Finite linear algebra on these matrices and their
conjugates gives rational log coefficients in each
exponential sector, subject to the declared inversion
charts. A nonzero rational function of an angular
logarithm cannot be periodic under a nonzero translation.
More generally, finitely many distinct angular
exponentials are independent over rational functions
of the angle. Thus single-valuedness removes angular
logarithms coefficientwise and retains only the integral
angular frequencies on the original cusp.

For an admissible biextension, the finite intersections,
sums and kernels defining the Deligne bigrading can be
computed by Gaussian elimination in fixed rank charts.
The grading Y is consequently rational in the period
and conjugate-period entries. The operator $\delta$
has Hodge bidegrees with both indices negative.
With weight interval [-2,0], it can only decrease
weight by two; its square and higher commutators here
vanish. Since $[\delta,Y]=2\delta$, source equation
(37) becomes
$$
 \bar Y=Y-4i\delta,\qquad
 \delta=(Y-\bar Y)/(4i).
$$
Definition 40, equation (41), is exactly
$2\pi\delta=h\eta$ for the declared extreme frames.
No general transcendental operation on a period
entry is required by this height calculation.

For the local form
$F(x+iy)=e^{xN}e^{iyN}e^{\Gamma(q)}F_\infty$,
the factor $e^{xN}$ is real, preserves W, and induces
the identity on the two framed extreme graded lines.
It is therefore an isomorphism of real biextensions,
in the precise scope of Brosnan-Pearlstein Lemma 42(b).
The height is unchanged on removing that factor.
This does not assert that N is a morphism of a
single fixed Hodge structure.

On the remaining nilpotent orbit the relevant matrices
are polynomial in y. Nonzero pivot minors are eventually
nonzero polynomials, so a single rank chart works for
all sufficiently large y, with polynomial bounds for
its inverse pivots. Multiplication by the holomorphic
q correction changes those matrices by an exponentially
small quantity times a power of y, uniformly for x
in a whole cusp period. It preserves the same chart.
This establishes uniform angular control, rather than
only a calculation on the imaginary axis.

Hodge projections and a fixed polarization similarly
give norm matrices by finite rational linear algebra.
A nonzero positive nilpotent-orbit norm in the stated
chart has rational-in-y leading coefficient. Its
logarithm is a multiple of $\log|q|$ plus $\log P(y)$
and a convergent positive-exponential remainder.
The latter logarithm belongs to the coefficient field
by factoring $P(y)=cy^d(1+O(1/y))$. Further inverses
are subject to the stated nonzero leading-coefficient
condition; arbitrary real-analytic operations and
arbitrary arithmetic metrics remain outside this claim.

## 6. Scope retained

The proof tests equality of the actual cusp functions
$A_1$ and $A_2+cA_1+dA_0$ with the explicitly defined
finite period/height expressions. Its obstruction is
the factorial nonzero Fourier sector, not the permitted
zero-mode powers of logs or inverse logs.

It does not exclude a motive with the same integrated
scalar, a comparison using further currents, or the
separate arithmetic-metric realization on the model.
No finite-Sha input, p-curvature conjecture, BSD
rationality, or full BSD conclusion is used.
Only this review file was written; no old numerical
certificate was rerun and no agent was spawned.
