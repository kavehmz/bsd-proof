# Independent review of the arithmetic theta forcing and doubling domain

Date: 2026-09-12. Reviewer /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Reviewed [the partial construction](theta-doubling-arithmetic-attack.md),
§§1–4 and the source-scope statements in§5, together with its
[checkpoint](theta-doubling-arithmetic-checkpoint.md).

**PASS for this bounded scope.** No mathematical correction to
the four saved sections is required. The actual Bost class and
its normalized coefficientwise pairings are justified. This review
does NOT promote the proposed hyperbolic Green inverse, its spectral
multiplier, an SSY diagonal identity, or a rational BSD comparison.

Reviewed proof SHA256:
9c3d0cf2f0330d841398220ef32b7e858b480ff89634ab82bad5ca5d5145d457.
Reviewed checkpoint SHA256:
5fe207d4fd3062d98ba2ca82f95821c72c9fb4ecd6ce5546c7274512964d37d3.
Any later mathematical section requires a separate review; editorial
PASS/header updates do not change this verdict.

## 1. The fixed-z source identity really is proved

I inspected [Alfes, arXiv1209.5197v2](https://arxiv.org/pdf/1209.5197v2),
Theorem5.1 and its proof on printed pp23–25. The theorem's
headline assumes a particular weakly holomorphic source lift.
That is not an assumption available for the present F.

The k=0 proof, however, explicitly treats the opposite lift of a
holomorphic weight3/2 cusp form with z fixed. It proves that the
weight-zero Laplacian in z annihilates that lift: the kernel's
Laplacian identity transfers to the holomorphic input, and the
truncated-boundary terms tend to zero. It then shows that the
resulting harmonic function is constant and that its cusp limit
is zero. The fixed-z kernel pairing is therefore zero. This is an
actual intermediate result of the proof, independent of whether
our F belongs to its headline source space.

The same identity is displayed and used in
[Du2412.00688v1, Proposition3.4, equation(3.7)](https://arxiv.org/pdf/2412.00688v1).
The Weil representation and untwisted KM kernel match the present
one. Changing a common nonzero scalar normalization of this kernel
would not affect its zero-pairing assertion.

The new Fubini argument is sufficient for the actual F. On a
source cusp strip,
\[
 q_z(A)\ge c\|A\|^2/y^2,\qquad p_A^2\le2q_z(A).
\]
Absorbing the polynomial in the Gaussian yields the stated
rank-three lattice bound C(1+y/sqrt(v))^3, including its zero vector.
On the metaplectic fundamental domain v has a positive lower bound.
The cusp form b decays exponentially as v tends to infinity, and
the actual F decays exponentially in BOTH source cusp heights.
Thus multiplying this bound by |F||b|v^(3/2), with both hyperbolic
measures, is integrable. Compact cores contribute finite integrals.

It follows that
\[
 \langle I_L(F),b\rangle
 =\int_YF(z)\langle\Theta_{\rm KM}(\,\cdot\,,z),b\rangle=0.
\]
The previously reviewed nonzero Eisenstein-second-derivative
pairing proves that I_L(F) itself is not zero. This separates
zero HOLOMORPHIC cusp projection from zero of the actual lift.
It does not assert that every Maaß cusp projection is zero.

## 2. The scheme cover and arithmetic divisor model

The generic cover degree checks independently from the congruence
indices. For M=5N with N prime,
\[
 [\operatorname{SL}_2(\mathbf Z):\Gamma_1(M)]
   =M^2(1-5^{-2})(1-N^{-2})=24(N^2-1).
\]
Since minus identity is absent from Gamma_1(M), its EFFECTIVE
index is12(N²−1). The effective index of Gamma_0(N) is N+1.
Thus the degree of X_1(5N)→X_0(N) is12(N−1)=4656.
The equivalent moduli count divides the24(N−1) generating
choices by the target's generic automorphism of order two.
It does not divide a second time.

The fine curve is defined over Q and has no elliptic stabilizers
on its open complex uniformization. Its smooth projective generic
curve admits a projective flat integral model; normalizing such
a closure gives the projective integral normal arithmetic surface
required here. Smoothness of every arithmetic fiber is unnecessary.

I checked [Bost1999, §§5.1–5.3](https://www.numdam.org/article/ASENS_1999_4_32_2_241_0.pdf).
In particular §5.2 explicitly uses WEIL divisors on a projective
integral normal arithmetic surface. Thus taking the closure of
the pulled-back generic theta divisor is allowed; the argument
does not silently require that every such closure be Cartier.
Section5.3 defines the intersection in this normal setting.
The paper's §5.5 real-divisor-coefficient version is also available;
its footnote explicitly distinguishes this version from simply
tensoring the integral arithmetic Chow group with R.

Only the generic map and the complex pullback are needed for this
construction. No extension of h to a chosen pair of arithmetic
models, and no unproved stack version of Bost's theorem, is used.
Possible vertical extensions are not claimed canonical.

## 3. The actual finite-energy forcing and source Green coefficients

The cusp expansion
\[
 F_R=\frac{1-N}{4\pi^2}\Re(q)(\log|q|)^2
             +O(|q|^2(\log|q|)^2)
\]
was independently checked in the preceding projection review.
It is not C¹. Its weak gradient nonetheless has size at most
C(1+|log r|)^2, and
\[
 \int_0^\epsilon r(1+|\log r|)^4\,dr<\infty.
\]
It is also continuous and square-integrable. Its pullback is smooth
at the former elliptic orbifold points, and finite ramification
at cusps preserves finite conformal Dirichlet energy.

For the actual theta Green coefficients, their specified divisor
logarithms are subtracted first. The remaining loglog cusp term
has gradient of size O(1/(r|log r|)), giving the convergent energy
\[
 \int_0^\epsilon\frac{dr}{r(\log r)^2}.
\]
The other remainders are smooth on the appropriate uniformizing
charts. Pullback matches the algebraic logarithms with the generic
pulled-back divisor, including ramification multiplicities.
Thus these coefficients define the stated Bost classes after
closure. This is a coefficientwise construction, not convergence
of the whole theta series in an arithmetic Chow topology.

Complex conjugation causes no missing imaginary metric. The actual
F satisfies F(cz)=conjugate(F(z)), so F_R is real and invariant.
The real scalar coefficients of the KM kernel are c-invariant by
the actual lattice involution already checked in the projection
note. Hence I_L(F)=I_L(F_R) coefficientwise; the c-odd imaginary
part has zero integral. The auxiliary variable tau is not conjugated
in this argument.

In particular A_F=(0,2h^*F_R) is a metrized trivial line with metric
norm exp(−h^*F_R), in Bost's enlarged category. The prior withdrawal
of a SMOOTH Gillet–Soulé class remains correct. These are different
regularity categories, not inconsistent assertions.

## 4. Continuity, vertical choices and the exact intersection factor

Bost(5.4) extends the INTEGRAL of the star product continuously
under W^(1,2) changes of the Green remainders. It does not require
the raw product of two distributional Green currents to exist.

To see why no unjustified point evaluation is hidden here, write
a fixed Green coefficient as g_0+psi, where g_0 is a usual smooth
Green function for its divisor and psi is W^(1,2). Its curvature
is omega_0+ddc psi. Pairing a pure metric u uses the continuous
functional
\[
 \frac12\left(\int u\,\omega_0+\int u\,dd^c\psi\right);
\]
the second term is defined by the Dirichlet pairing. Evaluation
of an arbitrary W^(1,2) representative at a divisor point is not
needed. This is exactly the extension mechanism in Bost5.1.

The smooth cutoffs converge in W^(1,2): the derivative-of-cutoff
term at a cusp has squared norm O(epsilon² log^4(epsilon)), and
the removed gradient and L² norms also tend to zero. If coarse
elliptic-point cutoffs are retained, the positive-power estimates
from the preceding review give the same convergence after pullback.
Thus intersection with each fixed theta coefficient converges.

For a smooth cutoff u=2chi_epsilon h^*F_R, the pure-metric
intersection is one-half the curvature integral. The explicit2
cancels this one-half. Change of variables for the finite generic
cover then gives
\[
 d^{-1}\langle A_{F,\epsilon},Z_C\rangle
       =\int_X\chi_\epsilon F_R\,c_1(Z).
\]
Passing to the continuous Bost pairing recovers the previously
proved cutoff limit and hence the actual scalar series H.
A vertical divisor has zero complex part and has zero intersection
with a divisor whose finite part is zero. Thus its choice does not
alter this equality. There is no further central-stabilizer factor:
d is already the effective generic degree, and the theta divisor
multiplicities and curvature are the previously fixed ones.

With the source convention ddc=(i/(2pi))partial bar-partial, a
real function u satisfies
\[
 \int u\,dd^c u=-\frac1{4\pi}\int|\nabla u|^2\,dx\,dy.
\]
Bost's arithmetic star integral carries the factor1/2. Therefore
\[
 A_F^2
 =\frac12\int_C (2h^*F_R)\,dd^c(2h^*F_R)
 =-\frac1{2\pi}\int_C|\nabla h^*F_R|^2
 =-\frac d{2\pi}\int_X|\nabla F_R|^2.
\]
Sobolev integration by parts follows by the same approximation.
The last integral is positive because the cusp expansion is
nonconstant. This proves the claimed negative nonzero
self-intersection, with no factor-two discrepancy. The generic
finite divisor is still zero, so its point projection is zero.

## 5. The scalar spectral jets are outside this category

The actual constant-term expansion gives
\[
 j_1=b_N(1)y\log y+O(y)+O((\log y)^2),
\]
\[
 j_2=\tfrac12 b_N(1)y(\log y)^2+O(y\log y)+O((\log y)^3),
 \quad b_N(1)=\pi(N^2-1)/6\ne0.
\]
These follow by differentiating b_N(s)y^s. The scattering term's
simple pole contributes the lower polynomials in log y, whose
y-derivatives are of smaller order.

An algebraic cusp logarithm is only a constant multiple of y.
After any such subtraction, the squared y-derivatives therefore
give divergent integrals of (log y)^2 and (log y)^4 respectively.
Conformal invariance of the two-dimensional Dirichlet integral
makes this the W^(1,2) obstruction in the algebraic cusp coordinate.
Divisors supported elsewhere do not change this local obstruction.

For clarity, the full Gamma-completed coefficient tested in the
preceding source is
\[
 \widetilde j_2=j_2+\gamma_1j_1+\gamma_2j_0+\gamma_3R_N,
 \qquad \Gamma(1+t)=1+\gamma_1t+\gamma_2t^2+\gamma_3t^3+\cdots.
\]
The constant-pole term is retained. None of the added terms cancels
the leading y(log y)^2. Thus the stated exclusion is valid also
for this completed coefficient. Scalar convergence against the
rapid forcing does not make it a Bost Green function.

This exclusion concerns scalar Green functions for finite divisors
on the compact curve. It does not exclude a different mixed or
relative Deligne construction, a regularized spectral operation,
or a higher arithmetic cycle with extra boundary data.

## 6. Source scope and the unreviewed proposed mechanism

Du0.10–0.11 and3.2 apply to holomorphic cusp inputs of weight3/2.
Their Mordell–Weil-valued lift and arithmetic inner-product formula
cannot be applied by replacing the present nonzero H with its
zero holomorphic cusp projection.

I also checked the cached primary
[SSY45-page revision](https://home.cc.umanitoba.ca/~sankaras/ArithSW-rev1.pdf),
§§2.3–2.5. Equations(41)–(43) do define an arithmetic intersection
and degree. Its indefinite nondegenerate genus-two archimedean
coefficient uses the specific superconnection integral(64)–(66).
The reviewed draft correctly does not equate this to an uncorrected
product of two genus-one Green functions, or infer a full diagonal
arithmetic identity merely from the existence of both series.
The quoted older division-Shimura-curve diagonal statement is not
being used as a full modular-curve theorem.

The checkpoint's hyperbolic Green construction, change of volume,
joint cusp estimate, proposed spectral strip and predicted
multiplier are all expressly UNPROVED. This review establishes
none of them. In particular Du3.9 uses the Laplacian for a chosen
smooth volume form; its inverse cannot be identified with the
hyperbolic inverse without further analysis. A subsequent actual
doubling/source test must receive a separate review.

No numerical certificates were rerun. The only owned mathematical
output of this review is this file. Full universal BSD and the
rational second-derivative comparison remain unresolved.

For the normalization audit I downloaded the primary Bost PDF to
/tmp/review-theta-bost1999.pdf, SHA256
b8153e541bd5b8b7112ec911bcb0a81c79b614926c869512131d062c7e968532.
The web OCR misread the denominator in(5.8). I extracted its printed
p274 with pypdf and rendered it using the native sips PDF renderer:
the displayed coefficient is exactly1/2. The page image is
/tmp/review-theta-bost-p274.png. The download completed successfully;
no source download or numerical process remains running.


## 7. Separate review of the new Poisson construction, §§5–8

**Additional verdict: PASS after the Poisson-sign correction.**
This supplements, and does not replace, the earlier §§1–4 verdict.
The new argument was initially saved with the opposite sign for
ddc(J_N). I reported that error, the author corrected every affected
formula and checkpoint passage, and I inspected the saved repair.

Reviewed corrected proof SHA256:
5e92a0d20118c9486dadea5f9439a40e79c4cdd38bc679d1926bcb346b0d462d.
Reviewed corrected checkpoint SHA256:
5b2b5f839672e6a257876c6f72d8be397ca0d720535745b05b187a2924b4ad35.

The previous proposed pointwise hyperbolic Green/doubling identity
is BYPASSED. This verdict concerns the actual scalar Poisson
potential, its theta lift and the source Hodge-height series.
It does not prove a genus-two arithmetic product identity or
a rational BSD frame.

### 7.1. Actual Poisson summation and the global L¹ bound

I independently computed the Fourier transform in the actual
a-coordinate. Let kappa=Ny², a'=a−2Nbx+Ncx² and b'=b−cx.
Then
\[
 Q=ca'-Nb'^2,\quad
 q_z=a'^2/\kappa+\kappa c^2+2Nb'^2,\quad
 p_A^2=(a'+\kappa c)^2/\kappa.
\]
These identities follow directly by expanding the displayed lattice
and majorant, so no auxiliary positive-definite model has been
substituted.

For fixed b,c, the a'-integrand is
\[
 \left(\frac v\kappa(a'+\kappa c)^2-\frac1{2\pi}\right)
 e^{-\pi v a'^2/\kappa}e^{2\pi icu a'}.
\]
At Fourier frequency m, put k=m−cu. Its transform is
\[
 -(\kappa/v)^{3/2}(k+icv)^2
                       e^{-\pi\kappa k^2/v}.
\]
The remaining c-Gaussian multiplies the absolute value by
e^(−pi v kappa c²), leaving precisely
\[
 (\kappa/v)^{3/2}|m-c\tau|^2
                    e^{-\pi\kappa|m-c\tau|^2/v}.
\]
The shift of a' contributes only a unit complex phase. This also
matches the primary Poisson calculation in
[Du–Yang1702.07917v2, printed p10](https://arxiv.org/pdf/1702.07917v2),
after the corresponding sign/reindexing of the matrix coordinate.

The b'-Gaussian sum is bounded independently of its shift because
v≥1. The term m=c=0 is identically zero. The lattice Z+tau Z is
uniformly separated for |u|≤1/2,v≥1; a disk-packing estimate, or
the direct lower bound by a constant times m²+c²v², bounds the
remaining polynomial Gaussian uniformly by Ce^(−cy²/v) when
y≥sqrt(v). Thus the asserted cusp estimate
C(y/sqrt(v))³e^(−cy²/v) is valid in every discriminant component.

For y≤sqrt(v), subtracting the actual zero vector gives
Ce^(−cv/y²). Integrating with dy/y² gives O(v^(-1/2)).
For y≥sqrt(v), substitution y=sqrt(v)t gives the same bound;
the added constant contributes O(v^(-1/2)) on that tail.
The compact source core gives exponential decay. Fricke transports
the second cusp with the stated width-one normalization.
This proves Lemma5.1, including its global absolute-value norm.

The same argument works uniformly for tau in compact subsets of
the fundamental domain, where v is bounded away from zero. Thus
the source integrations and pointwise limits used afterward are
also justified there.

### 7.2. The critical-strip extension has the right exponents

For bounded h of exact mean zero, the zero-vector contribution
cancels before taking absolute values. Lemma5.1 yields
I_L(h)=O(v^(-1/2)). The Petersson density v^(3/2)dmu_tau is
v^(-1/2)du dv. The two Eisenstein constant powers therefore give
integrands bounded by
\[
 v^{(\Re(s)-3)/2},\qquad v^{-1-\Re(s)/2},
\]
which are integrable exactly for0<Re(s)<1. Nonconstant terms
decay exponentially, locally uniformly in s away from poles.

The exact-mean cutoffs are legitimate: use chi_R h and subtract
its integral times one fixed compactly supported bump of integral1.
The correction tends to zero because h is bounded and Y has finite
volume. All approximants are uniformly bounded and compactly
supported. The global L¹ bound gives a uniform majorant for their
theta transforms. On the source side J_N(s) is L¹ in this strip,
as its cusp powers are y^s and y^(1−s). Dominated convergence
passes both sides of the prior adjoint identity to h.

This argument does not unfold an Eisenstein Poincaré sum outside
its convergence half-plane. It extends a previously proved
identity by two justified dominated limits. The result retains
the exact earlier negative multiplier r_N(s).

### 7.3. The local potential and global normalization are actual

With alpha_0=a(q)dq and beta_0=(b_(-1)/q+b_hol(q))dq,
write A'=a, B'=b_hol, A(0)=B(0)=0. Direct differentiation gives
\[
 dd^c\left[\pi\Re\{\overline{b_{-1}}A\log|q|^2
                                      +A\overline B\}\right]
  =\Re\left(\frac i2\alpha_0\wedge\overline{\beta_0}\right).
\]
The factor pi is exact. The potential's possible cusp delta term
is multiplied by A(0), so there is no atom. Its size is
O(r|log r|), its gradient is O(1+|log r|), and it has finite
Dirichlet energy.

The modular one-forms themselves descend to holomorphic
differentials at the coarse elliptic points; hence their product
is a smooth two-form there. After subtracting cutoff versions of
these explicit cusp potentials, the remaining two-form is smooth
on the compact curve and has zero total integral. Compact Poisson
solvability applies. Adding the cusp potentials back and fixing
the HYPERBOLIC mean gives the stated bounded W^(1,2) solution.

Any two distributional solutions differ by a harmonic distribution
on a compact connected curve, hence by a constant. The specified
mean makes the solution unique, independently of the auxiliary
smooth compact Green operator used for its construction.
Fricke equivariance follows by uniqueness. For conjugation, the
orientation sign of the two-form cancels the sign in pulling back
ddc; the real equation is preserved, again giving uniqueness.
Thus the two cusp values are a common q_c, and the remainders
and fixed hyperbolic derivatives decay exponentially times a
polynomial in the cusp height.

### 7.4. The confirmed sign correction

In the conventions explicitly fixed throughout the project,
\[
 dd^c=\frac i{2\pi}\partial\bar\partial,\qquad
 dd^c u=\frac1{4\pi}(u_{xx}+u_{yy})\,dx\,dy.
\]
Consequently
\[
 dd^c(y^s)=+\frac{s(s-1)}{4\pi}y^s\,d\mu,\qquad
 dd^cJ_N=+\frac{s(s-1)}{4\pi}J_N\,d\mu.
\]
The initial negative sign was false. It also contradicted the
already checked identity ddc(j2)=(j1+j0)dmu/(4pi).

For0<Re(s)<1, compact Stokes with truncated cusps now gives
\[
 \int_Y q_FJ_N(s)d\mu
             =+\frac{4\pi}{s(s-1)}M_F(s).
\]
The boundary terms vanish: q_F is bounded with exponentially
small derivatives, while the normal derivatives of the two
Eisenstein cusp powers tend to zero in this strip. All terms
are absolutely integrable. For Fricke-even q_F the plus-cusp
average J_N^+ can be replaced by the original J_N.

Combining this corrected positive Poisson factor with the
negative earlier adjoint factor gives
\[
 P_F(s)=\langle I_L(q_F),\mathcal E_L(\bar s)\rangle
                =-\frac{4\sqrt N}{\pi}\xi(s)M_F(s).        \tag{R1}
\]
I inspected the author's saved corrections to(6.4),(6.5),
(7.1),(7.3) and the checkpoint. The earlier direct
second-derivative formula and r_N(s) were unchanged.

### 7.5. The exact tail and the zero cusp constant

I checked the primary identities
I_L(1)=2Ecal_L(1)/(N−1) and the arithmetic degree formula in
[Du–Yang, Theorems1.3 and1.6](https://arxiv.org/pdf/1702.07917v2).
There is also a direct independent check of the two-cusp tail
coefficient, avoiding a transcription of its square root.

At one width-one cusp the b=c=0 sum is
\[
 S(x^2)=\sum_{a\in\mathbf Z}
       (x^2a^2-1/(2\pi))e^{-\pi x^2a^2},
 \qquad x=\sqrt{v/N}/y.
\]
If vartheta(x²)=sum_a e^(−pi x²a²), then
\[
 S(x^2)+\frac1{2\pi}
     =-\frac1{2\pi}\frac d{dx}\{x(\vartheta(x^2)-1)\}.
\]
The bracket tends to1 at zero and to0 at infinity. Its integral
is therefore1/(2pi). Changing variables in dy/y² gives
sqrt(N)/(2pi sqrt(v)) from each cusp. Nonzero transverse lattice
coordinates and the compact core give exponentially small errors.
Thus both cusps together produce exactly
\[
 I_L(1)=-\frac{\operatorname{vol}Y}{2\pi}e_0
          +\frac{\sqrt N}{\pi\sqrt v}e_0+O(v^Be^{-cv}).
\]
There is no missing sign or factor two.

The rapid function q_F−q_c has mean −q_c volY. Its zero-vector
term cancels the constant term in q_c I_L(1). The remaining lift
therefore has the exact tail asserted in(6.7).

The source's raw Eisenstein leading coefficient is2a_N(s),
where a_N(1)=−(N²−1)/24. Its pairing against
q_c sqrt(N)/(pi sqrt(v)) gives
\[
 2a_N(s)\frac{q_c\sqrt N}{\pi}
       \int_1^\infty v^{(s-3)/2}\,dv,
\]
whose residue at1 is −4a_N(1)q_c sqrt(N)/pi.
The opposite constant power is integrable near1, and the rapid
remainder is holomorphic there. Equation(R1), together with
M_F(1+t)=M t²+O(t³), has no pole. Hence q_c=0.
This makes q_F an actual rapid test, not merely a formal
regularized potential.

As an independent consistency check, in the same strip Stokes
gives int_Y J_N(s)dmu=0. Thus int q_FJ_N=int(q_F−q_c)J_N.
The latter rapid-test integral has residue
−q_c volY Res(J_N)=−q_c b_N(1), since
Res(J_N)=(N−1)/2. The corrected Poisson formula has no pole,
again forcing q_c=0. This check is compatible with the proof's
separately established theta-tail argument.

### 7.6. The first derivative and arithmetic Hodge series

The completed xi has residue1 at s=1 in this normalization.
Consequently(R1) has linear leading coefficient
−4sqrt(N)M/pi. Since q_F is rapid, differentiating its ordinary
Petersson integral is justified near1. The repaired formulas are
\[
 \langle I_L(q_F),\mathcal E_L(1)\rangle=0,\qquad
 M=-\frac{\pi}{4\sqrt N}
             \langle I_L(q_F),\mathcal E_L'(1)\rangle.       \tag{R2}
\]
There is no factorial2: the simple xi pole reduces the quadratic
zero to a first-order term.

The source Hodge-height formula is exactly
\[
 R_\omega=\frac1{N-1}
  \left(\mathcal E_L'(1)-\frac{N\log N}{N-1}\mathcal E_L(1)\right).
\]
Its lower correction vanishes in this pairing by(R2), giving
\[
 M=-\frac{\pi(N-1)}{4\sqrt N}
                       \langle I_L(q_F),R_\omega\rangle.   \tag{R3}
\]
The Hodge line and vertical correction are those of the original
Du–Yang source. No arbitrary vertical extensions on the cover
are identified with a pullback of the entire two-factor height.

The new pure metric class A_q=(0,2h^*q_F) is in Bost's category
by its proved finite energy. Its normalized coefficientwise theta
pairings follow from the same continuity and pure-metric argument
already reviewed for A_F. The ordinary intersection with a
pulled-back Petersson Hodge line is nevertheless
\[
 d^{-1}\langle A_q,\widehat\omega_C\rangle
      =\frac1{4\pi}\int_Yq_F\,d\mu=0,
\]
because its curvature is dmu/(4pi). Thus(R3) is the specified
theta/Petersson operation on two actual arithmetic-intersection
series, not the ordinary intersection of those two classes.

The corrected new §§5–8 pass. They construct a canonical real
arithmetic Poisson input and a first-derivative Hodge-height-series
representation of the original mass. They do not identify the
Petersson functional with a rational motivic regulator, the fixed
point/K2/Tate determinant, or an integral BSD coefficient. The
bypassed genus-two/pointwise-Green mechanism remains unproved.
No old numerical calculation was rerun for this additional review.
