# Independent review of the relative beta2 boundary

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Own only this review file. **PASS after the recorded source, real-structure
and frame wording precisions.** All five mathematical sections and the
checkpoint were read. No mathematical correction remains.

Reviewed proof: [relative-beta2-boundary-attack.md](relative-beta2-boundary-attack.md),
mathematical SHA256
36826737cb66f2db433c49987788d456d8bbaa10d3d772d788946338b474e265.
Reviewed [checkpoint](relative-beta2-boundary-checkpoint.md) SHA256:
b5b07342b08c61bcaad056566045dc39e6f6e68177b7f2aed17ae4e89a0665cf.
Subsequent review links and completion statuses are editorial.

The bounded audit checks the actual rational higher-Chow chain and
full diagonal restriction, the resulting cokernel injection, the native
Deligne K2 product, the explicit positive boundary and cutoff scalar,
and the separation from the missing point-height determinant.
The previously reviewed rational beta2 and its regulator period are
inputs; no old certificate or construction is being rerun.

The final precisions were inspected: Voevodsky2.1.4 identifies motive
maps rather than an unspecified chain homotopy; real representatives
are obtained by averaging; the unit is explicitly Delta(z)/Delta(Nz);
and the last formal product uses Reg_E alone. The final small-loop
interpretation now explicitly uses the fixed Rost symbol: the loop
is minus its logarithm times2pi. Its unramified zero and all native,
cone and scalar formulas are unchanged. The full universal BSD
objective remains unresolved; no
optional cup/trace retraction is used.

## 1. The actual motivic relation and the full cokernel

I read [Voevodsky, Propositions2.1.4 and4.1.5](https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s5.pdf),
PDF pp.5–6 and41, and
[Levine, Theorem5.2 and Corollary5.3](https://www.numdam.org/article/AST_1994__226__235_0.pdf),
printed pp.312–316. They give the Chow-correspondence action and
proper-pair localization used here. All varieties are smooth projective
over Q, and the resolution hypothesis is satisfied.

The ambient E times V has dimension3. The support
W={(P,x,P)} has dimension2, and its rational function u(x)
has exactly the two stated divisors, each with multiplicity N-1.
Equivalently, its graph in W times the cubical line is a
codimension-two admissible precycle; its faces give the displayed
positive divisor. This is a chain producing rational equivalence,
not a claimed closed element of CH²(-,1). Thus
Gamma(i0)=Gamma(i_infinity) in CH²(E times V)_Q.
The correspondence degree is zero: both graphs have the dimension
of their source E. This identifies the actual motive maps, and hence
their pullbacks in every motivic degree and twist.

This proof does not assert a literal chain homotopy in every model
of motivic cochains. The author's source-scope clarification correctly
states equality of motive morphisms induced by the rational equivalence.
Integrally it only gives N-1 times the difference equal to zero;
the rational denominator is not canceled at its prime divisors.

The image of restriction to B is the ENTIRE diagonal:
the motive-map equality gives containment, and the actual projection
p_E gives the reverse containment because i_c^*p_E^*=id.
The exact relative sequence therefore injects its cokernel, identified
by (beta0,beta_infinity) mapping to beta0-beta_infinity.
Consequently beta mapping to partial^+(beta,0) is injective,
independent of any presentation of beta. No supplementary motivic
splitting or compact cup/trace retraction is required.

The input beta2 is already nonzero by its previously reviewed regulator.
The new relative class is therefore nonzero BEFORE evaluating its new
logarithmic scalar. This is not a new proof of nonvanishing of beta2
without using the prior period theorem, and it requires no assertion
that the full K2 group has dimension one.

## 2. Native K2 and real structures

I checked [Burgos–Goswami1712.10150v2](https://arxiv.org/html/1712.10150v2),
dated6April2018, §§4.3–4.5 and equation4.8, and
[Burgos–Feliu0907.5169v1](https://arxiv.org/html/0907.5169),
Theorem3.5 and §5. These identify the total/concise Deligne models,
their homotopic products and compatibility with the Beilinson regulator.
The following is a direct calculation in those conventions.

For x=log|f| and y=log|g| the unit triples are
(partial x-barpartial x,2partial x,x) and its y analogue.
Both are closed for d(r,f,w)=(dr,df,f-r-dw).
The chosen product has third entry
2x partial y-y partial x+y barpartial x.
Subtracting its complex conjugate and dividing by2 gives
$$
 x(\partial y-\bar\partial y)
       -y(\partial x-\bar\partial x)
   =i\,\eta_K(f,g).
$$
There is no extra 2pi factor in this projection: imaginary real
forms are the subspace R(1), and the projection takes a half-difference,
not a coefficient in an integral Tate basis.
The two degree-one unit factors are multiplied in their stated order.

For an unramified symbol, write f=t^m a and g=t^n b near a point.
Its small-loop integral is
2pi times (n log|a|-m log|b|). For the fixed Rost symbol
partial{f,g}=(-1)^(mn)b^m/a^n, this is MINUS its log absolute
value times2pi. This matches partial{t,a}=a, and corrects the
previous review sentence's identification with the opposite tame
convention. It vanishes for the actual unramified
class. The local symbol formula therefore represents the global
Deligne class, and a smooth closed representative may be used.
The finite coefficient traces and norm transfers defining beta2
are inherited from the completed integrated construction.
Neither its coefficients nor its modular degree are renormalized.

The added real-structure precision is correct: average rho to be
conjugation-invariant and eta to be anti-invariant.
The anti-invariant cohomology class is unchanged. The native
imaginary form i eta then has the required combined real involution,
as does its cutoff extension and boundary.

## 3. Relative sign and the smooth cutoff

Use exactly the displayed differential
D(c,b)=(dc,i^*c-db) and positive inclusion b mapping to(0,b).
If e=i rho eta, its relative differential is(d_D e,i^*e).
Subtracting this from(0,i eta,0) gives(-d_D e,0).
At degree2 and twist2, d_D is minus the (1,1) projection of d.
Since d eta=0, the resulting form is
$$
 i(d\rho\wedge\eta)^{1,1}.
$$
This verifies the sign without relying on an unspecified convention
for the word boundary. Using the opposite connecting map reverses
both the class and its scalar.

The earlier reviewed unit-normalized current S has native Deligne
FORM representative2pi i S. I also checked the separate GS conversion
in Burgos–Goswami Proposition7.3 and equations7.2–7.3:
an ordinary GS current T corresponds to pi i T here.
These are distinct conventions. Applying the first one to the
present native boundary gives
$$
 S_{\mathfrak b_2}=\frac1{2\pi}(d\rho\wedge\eta)^{1,1}.
$$
Using the GS metric factor here would incorrectly double the result.

The representative is smooth and zero in neighborhoods of both
boundary fibers. It is Deligne-closed since it is an absolute
Deligne differential. There is no product of singular currents
and no unproved restriction to a cusp divisor.
If rho changes with fixed cusp values, its difference is zero near B,
so the change is an ordinary relative boundary. Exact changes of eta
have zero fiber pairing with the closed holomorphic differential.

## 4. Independent scalar computation

The prescribed a-period of eta is zero, since its class is
anti-invariant and conjugation fixes a. With a dot b=1,
Riemann bilinearity gives
$$
 \int_E\omega_E\wedge\eta
       =\omega_1\int_b\eta
       =\omega_1\mathscr R_E(\beta_2).
$$
Only partial rho wedge eta^(0,1) survives multiplication by omega_E.
The fiber order in S wedge omega_E is eta wedge omega_E, so
$$
 p_{X,*}(S_{\mathfrak b_2}\wedge\omega_E)
   =-\frac{\omega_1\mathscr R_E(\beta_2)}{2\pi}\,\partial\rho .
$$
This minus sign is essential.

Put l=log|u|. The fixed dd^c=i partial barpartial/(2pi)
normalization gives partial barpartial l
=-pi i(N-1)(delta0-delta_infinity).
Integrating partial(rho barpartial l) as a current on compact X
therefore gives
$$
 \int_Y\partial\rho\wedge\bar\partial l=\pi i(N-1).
$$
Equivalently the positively oriented puncture circles, with the
boundary orientation of the complement, give the same sign.
The derivative of rho is supported away from the cusps, so the
integral has no limiting ambiguity.

Substitution into the functional with its fixed c_pi normalization
now gives, independently,
$$
 \frac{i}{4\pi^2c_\pi}
 \left(-\frac{\omega_1\mathscr R_E(\beta_2)}{2\pi}\right)
 \pi i(N-1)
 =\frac{(N-1)\omega_1 L(E,2)}{8\pi^3c_\pi}.
$$
The opposite cusp gives the negative by the diagonal relation.
No extra degree40 enters: there is no new modular-map pushforward
in this computation. The earlier construction of beta2 already
retains its norm-transfer normalization.

The functional uses the declared de Rham differential omega_E.
Its period omega1 is retained, not treated as a rational Betti
coefficient. The degrees are2 to3 for the boundary, then product
with degree2/twist1 and trace of shift(-4,-2), ending in
degree1/twist1. This verifies the stated de Rham-coefficient
functional, not a new rational scalar comparison.

## 5. What the ratio establishes

Dividing the existing Mellin value by the new evaluated boundary
gives exactly
$$
 -12Nc_\pi\,\frac{\ell_E}{\omega_1}
   =-24Nc_\pi\,\frac{\ell_E}{\Omega_E}.
$$
The factor2 uses the full real period Omega_E=2omega1.
The Neron–Tate regulator is absent. Multiplying the boundary
evaluation by Reg_E ALONE gives -(N-1)/(4c_pi) times the
target evaluation -Omega_E Reg_E L(E,2)/(4pi^3).
Multiplying by the already period-inclusive D_pt would instead
insert an additional real period and is not this identity.

All these are identities of specified evaluations. They neither
identify the spectral relative class with a rational multiple of
the boundary class nor prove the ratio rational. Equality of a
single functional value would not imply equality of the classes.
The height determinant, finite intersection data and an actual
arithmetic comparison map remain necessary parts of this proposed
route. The note does not assert this particular route is necessary
for BSD, or assume Sha finiteness, K2 finite generation, integral
primitivity or algebraicity of a spectral derivative.

No old computation was rerun and no shared synthesis or proof file
was edited by this reviewer.
