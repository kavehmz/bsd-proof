# A canonical graph correction and its relative cusp obstruction

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Completed bounded construction; all [NEW] deductions passed
[independent review](review-radial-graph-correction.md).
Restart: [checkpoint](radial-graph-correction-checkpoint.md).
Full BSD over Q remains the objective.

The Poincaré graph bundle supplies an actual star-product correction
of the previous nonclosed current. The original scalar is preserved
by a separate relative construction with explicit zero cusp constants.
This gives a real relative Deligne class on a rational pair.
The entire natural scalar-Kummer cup subspace is then tested and has
zero original pairing. A rational source for the nonzero spectral
class is still missing; a real arithmetic metric is not that source.

## 1. Rational space, divisor and coefficient complex before evaluation

Let X=X0(389), Y=X minus its two rational cusps, E=389a1 and
pi:X→E the fixed degree40 modular map. Put
\[
 V=X\times E,\quad B=(\{0,\infty\}\times E),\quad V^\circ=Y\times E,
 \qquad D=\Gamma_\pi-(X\times O),\quad L_D=\mathcal O_V(D).
 \tag{1.1}
\]
All these objects are over Q. The morphism d:V→E, d(x,P)=P-pi(x),
gives
\[
 L_D=d^*\mathcal O_E(O)\otimes p_E^*\mathcal O_E(O)^{-1}.
 \tag{1.2}
\]
Because pi(c)=O at BOTH cusps, the two pullbacks in(1.2) agree
canonically on each component B_c. Their tensor cancellation
defines a rational trivialization epsilon_c of L_D there.
This is stronger data than saying its restriction has degree zero.
Equivalently L_D is the pullback of the rigidified Poincaré bundle,
together with the explicit base factor pi^*O_E(O).

The motivic source considered below is
\[
 H^3_{M,c}(V^\circ,\mathbb Q(2))
   =H^3_M(V,B;\mathbb Q(2)),\qquad
 M(V,B)=\operatorname{Cone}(M(B)\longrightarrow M(V)).
 \tag{1.3}
\]
Since V and B are proper, this is M^c(V^\circ). This convention
for compact supports is fixed, rather than replacing it by ordinary
cohomology of the open. The relative Picard class
\[
 c_D=c_1(L_D,\epsilon_0,\epsilon_\infty)
               \in H^2_M(V,B;\mathbb Q(1))                 \tag{1.4}
\]
is actual rational data. The relative Picard interpretation follows
also by applying the cone to Z(1)=G_m[-1].
Localization for compact motives is
[Voevodsky, Proposition4.1.5](https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s5.pdf);
the base field is Q, so its resolution premise holds.
For the rigidified Picard group see
[MVW, Definition7.10 and the following description](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).

The regulator target is the relative real Deligne complex
\[
 D_{\mathbb R}(V,B;2)=
 \operatorname{Cone}\bigl(D_{\mathbb R}(V,2)
             \longrightarrow D_{\mathbb R}(B,2)\bigr)[-1].
 \tag{1.5}
\]
Its degree-three current presentation uses real (1,1) currents
closed under dd^c, modulo the appropriate partial/barpartial
boundaries, with boundary primitives included by(1.5).
Calculations may be complexified to contract with omega_E.
A relative primitive restricts to an exact Deligne primitive on B;
it is not an unrestricted absolute-current change.

We use dd^c=(i/(2pi)) partial barpartial and the same normalized
real regulator as the preceding proofs: a unit maps to log absolute
value. A normalized (1,1) current T in degree3, twist2 corresponds
to the factor 2pi i times T in the ordinary real Deligne form frame;
a first Chern curvature Omega corresponds to 2pi i Omega.
Thus multiplying a unit regulator by a first Chern form gives
log|v| Omega in these normalized coordinates. No Tate period is
declared rational by suppressing this factor. The final logarithmic
test has degree2, twist1; the product has degree5, twist3 and
integration over the surface has degree shift(-4,-2), ending in
degree1, twist1. The contraction with the rational de Rham frame
omega_E is specified separately and retains c_pi.

The complexes and products are the Deligne models of
[Burgos–Feliu0907.5169v1, §§1.8,3.2,4–5](https://arxiv.org/html/0907.5169).
Their higher-Chow regulator is the Beilinson regulator.
We will NOT infer a motivic class merely from a cocycle in(1.5).

## 2. The canonical Poincaré Green function and exact curvature

Choose a complex uniformization E(C)=C/(Z+tau Z),
tau_2=Im(tau)>0, and write
\[
 \omega_E=\Omega_A\,dw,\qquad
 \beta=\pi^*dw=\alpha/\Omega_A,\quad
 \alpha=\pi^*\omega_E=c_\pi\,2\pi i f(z)\,dz.
 \tag{2.1}
\]
The nonzero period Omega_A belongs to this comparison frame;
it is not set equal to the full real period or canceled in a
rational lattice. The formulas below are independent of the
uniformization. Set mu_E=i dw wedge dbarw/(2tau_2), of integral1.

Let g(w) be the canonical normalized elliptic Green logarithm,
with
\[
 dd^c g=\delta_O-\mu_E,\qquad \int_E g\,\mu_E=0.
 \tag{2.2}
\]
For example it is
\[
 g(w)=\log\left|\frac{\theta_1(w,\tau)}{\eta(\tau)}\right|^2
                  -\frac{2\pi(\operatorname{Im}w)^2}{\tau_2}.
 \tag{2.3}
\]
Here theta_1 is the odd Jacobi theta with periods1,tau.
Its multipliers show that(2.3) is periodic; its simple zero gives
dd^c log|w|²=delta_0, and differentiation of its quadratic term
gives -mu_E. Jensen's formula in the theta product gives mean zero:
for 0<Im(w)<tau_2 its horizontal mean is
- pi tau_2/3+2pi Im(w)-2pi Im(w)²/tau_2, whose vertical mean is zero.
This proves(2.2), including the log-square normalization.
The canonical metric interpretation agrees with
[de Jong, Theorem1.1 and its metric construction](https://ems.press/content/serial-article-files/25976):
our g is twice the source's log of the positive Arakelov Green function.

On V define the actual logarithmic current
\[
 G(x,w)=g(w-\pi(x))-g(w).
\]
It is the log-square norm of the rational divisor section of(1.2),
with its canonical metric. Therefore
\[
 dd^cG=\delta_D-\Omega_D,\quad
 \Omega_D=\frac{i}{2\tau_2}
       \bigl(\beta\wedge\bar\beta
                     -\beta\wedge d\bar w-dw\wedge\bar\beta\bigr).
 \tag{2.4}
\]
This is also obtained directly by subtracting the two pullbacks
of mu_E. In particular Omega_D has NO purely vertical component.
It is closed, and its pullback to each B_c is zero. The metric
of epsilon_c is one: at pi(c)=O the two canonical metrics cancel.
The vertical/base component and the two mixed components in(2.4)
are all retained.

**[NEW] Lemma2.1.** For every scalar base distribution a for which
the products exist,
\[
 dd^ca\wedge\Omega_D=0,\qquad
 p_{X,*}(\Omega_D\wedge p_E^*\omega_E)=\alpha.
 \tag{2.5}
\]
The first equality is a dimension statement on X: each term has
at least three real base degrees. For the second, only
-beta wedge dbarw contributes. Since
\(\int_E d\bar w\wedge dw=2i\tau_2\), its contribution is
Omega_A beta=alpha. This proves both identities, with their signs.

## 3. The genuine star correction and its global distributional extension

For a smooth real function a on Y, the canonical correction is
\[
 S_a=a\,\delta_D-G\,dd^ca.                                \tag{3.1}
\]
On this open all products are admissible: a is a scalar smooth
coefficient and G has its specified divisor logarithms.
The actual arithmetic product of the archimedean class (0,2a)
and the metrized divisor (D,-G) has Gillet–Soulé Green current
2S_a. This factor two is the unit-log versus metric-log-square
conversion: in the ordinary Deligne form frame a GS codimension-two
Green current T corresponds to pi i T, so 2S_a corresponds to
2pi i S_a, exactly the regulator frame of §1. Its curvature is
2dd^ca wedge Omega_D, which vanishes by(2.5). Directly,
\[
 dd^c S_a=dd^ca\wedge(\delta_D-dd^cG)
                          =dd^ca\wedge\Omega_D=0.         \tag{3.2}
\]
Thus this correction does not subtract the entire graph current.
The relevant source convention and the distinction between a
cycle and a chosen Green current are
[Burgos–Goswami1712.10150v2, Definitions6.1,6.18 and
Proposition6.19](https://arxiv.org/html/1712.10150v2).
We use their ordinary Gillet–Soulé normalization as explained in
Proposition7.3 and equations(7.2)–(7.3), not the unconverted
Thom–Whitney current factors.

To extend(3.1) across the cusps, we do not multiply a singular
a by a cusp Dirac or restrict an arbitrary exact current.
Instead use the identity on the interior
\[
 S_a=a\Omega_D+\partial U_a+\bar\partial\overline{U_a},
 \quad U_a=\frac{i}{4\pi}
                    (a\,\bar\partial G-G\,\bar\partial a).
 \tag{3.3}
\]
Indeed partial U_a+barpartial barU_a equals
a dd^cG-G dd^ca. This explicit calculation fixes the minus
sign in(3.1).

Let a have polynomial/logarithmic hyperbolic cusp growth,
as do j2, the full completed coefficient, and their products
with log|u|. In an algebraic cusp coordinate q assume
\[
 |a(q)|\le C(1+|\log|q||)^A
                   (1+\log(2+|\log|q||))^B,
\]
with the corresponding bound for q partial_q a and
barq partial_barq a. The actual Laurent coefficients
satisfy these bounds at both cusps. Write
P(q)=pi(q)=O(q^m) in a local elliptic parameter, m>=1.

**[NEW] Proposition3.1.** The coefficients of U_a are locally
integrable on the compact V. Defining S_a by(3.3) gives a
global closed degree-three real Deligne current, agrees with
(3.1) on the interior and has no added cusp-fiber atom.

*Proof.* The gradient of g is integrable on E, since its only
singularity is O(1/|w|). Translation and the fundamental theorem
along a segment give
\[
\|g(\,\cdot-P)-g\|_{L^1(E)}\le C|P|.
 \tag{3.4}
\]
The analogous derivative difference has the bound
C|P|(1+|log|P||): split into disks of radius 2|P| around
the two singularities, where the gradient integral is O(|P|),
and their complement, where the Hessian is O(1/|w|²).
Integrating that Hessian bound gives O(|P| log(1/|P|)).
Consequently G barpartial a has fiberwise L1 norm at most
C |q|^(m-1) times a polynomial in logarithms. For barpartial G,
its vertical coefficient has uniformly bounded fiberwise L1
norm, and its horizontal coefficient has norm at most
C|P'(q)|=O(|q|^(m-1)). Multiplication by a preserves local
integrability in q. These estimates prove the assertion for U_a.
The form aOmega_D is also locally integrable.

All derivatives in(3.3) are now derivatives of defined global
currents. Applying dd^c kills both exact terms, and
dd^c(aOmega_D)=dd^ca wedge Omega_D=0 distributionally.
For a cusp cutoff at radius epsilon, the error terms involving
its derivative and a horizontal coefficient have integrated
norm O(epsilon^m times a polynomial in |log epsilon|);
the vertical coefficients give O(epsilon times such a polynomial).
Both tend to zero. Thus no extra fiber-supported boundary current
appears in the limit. This proves the claimed extension without
a product G delta_B or a delta_div(u).
The derivative-difference bound also shows that the tangential
vertical part of U_a tends to zero in L1 on B_c. Thus the
homotopy between S_a and aOmega_D has the prescribed zero
boundary trace, rather than an unrecorded fiber constant.

At coarse elliptic points a is interpreted as the descended
locally bounded orbifold coefficient. One may either use these
locally integrable currents or remove small disks first.
On the uniformizer the coefficient is smooth and invariant;
its descended first derivatives have integrable power bounds.
The same cutoff argument gives no added point atom. No
arbitrary singular-current pullback is used. Square.

This is a current/Deligne construction, not a convergence assertion
inside an arithmetic Chow group. For smooth cutoffs a_epsilon,
twice(3.1) is the Green current of the arithmetic star product
just specified. The proof constructs the normalized current
limit and its real Deligne class. It does
not make the spectral metric rational motivic data.
In particular a=j2 is not a finite-energy scalar metric, even
after subtracting a finite cusp logarithm. At infinity its
leading term is A y(log y)², A=pi(N²-1)/12; for every constant b,
the integral of |partial_y(j2-by)|² dy diverges. The mixed form
aOmega_D instead has Lp coefficients in the algebraic cusp
coordinate for every finite p. These are different degree and
regularity statements; no scalar Sobolev arithmetic theorem
is applied to j2.

**[NEW] Proposition3.2.**
\[
 p_{X,*}(S_a\wedge p_E^*\omega_E)=a\alpha                 \tag{3.5}
\]
as global currents, including the two cusp limits.

*Proof.* The term aOmega_D gives aalpha by(2.5).
The barU_a wedge omega term has vertical holomorphic degree2
and hence pushes to zero. In U_a wedge omega only the vertical
barpartial_E G term could survive. Its fiber integral is zero
by Stokes on the compact E, since G is integrable and omega is
holomorphic. Thus p_*(U_a wedge omega)=0 as an L1 current.
Proper push and partial/barpartial commute, proving(3.5).
The already proved global L1 extension prevents an extra
boundary-supported contribution. Square.

For a=j2 log|u| this corrects exactly the nonzero interior
residual of j2 G_Z in the preceding proof. Preserving that
transgression alone would NOT prove preservation of the
original mass: d(j2 log|u|alpha) has two product terms.
The next section uses the separate correct scalar test.

## 4. Original scalar and the precise absolute-class boundary defect

Keep
\[
 u=N^{-6}\Delta/\Delta_N,\quad l=\log|u|,\quad
 m_\infty=1-N,\quad m_0=N-1,\quad
 F\,d\mu=-\frac{i}{4\pi^2c_\pi}d(l\alpha).
\]
For a=j2, or its full completed version, the original functional is
\[
 {\cal P}(S_a)=\frac{i}{4\pi^2c_\pi}
       \int_Yp_*(S_a\wedge\omega_E)\wedge\bar\partial l
       =\int_YaF\,d\mu.                                  \tag{4.1}
\]
The sign follows from d(lalpha)=barpartial l wedge alpha.
This is absolutely convergent: alpha is holomorphic in the
algebraic cusp coordinate, a has only logarithmic power growth,
and barpartial l has a simple logarithmic pole.
For j2 the value is EXACTLY the nonzero M already certified.
The same identity holds with smooth cutoffs before passage to
the limit, with the preceding bounds controlling both ends.

The test omega_E wedge barpartial l is closed on V^\circ and
logarithmic at B. It comes from the independently given rational
unit and the named rational de Rham differential. Its boundary
residue retains m_c and the elliptic differential. It is not
silently replaced by a smooth absolute test.

**[NEW] Proposition4.1.** Under an absolute Deligne-exact change
whose omega contraction is partial b, with b smooth on X, the
functional changes by
\[
 -\frac1{4\pi c_\pi}\sum_{c=0,\infty}m_c b(c).
 \tag{4.2}
\]
Hence(4.1) does not descend to an unrestricted absolute
Deligne class.

*Proof.* With the present dd^c, the distribution identity is
dd^c l=(1/2)sum m_c delta_c, or
partial barpartial l=-pi i sum m_c delta_c.
Stokes therefore gives
\[
 \int_X\partial b\wedge\bar\partial l
                  =\pi i\sum_c m_c b(c).
\]
Multiplication by i/(4pi²c_pi) proves(4.2).
The same result follows by integrating around the deleted cusp
circles; their orientation is clockwise for the punctured X.

These changes really occur. Given b, a smooth (0,1) primitive
U=b\,p_E^*\bar\omega_E/
\(\int_E\bar\omega_E\wedge\omega_E\)
satisfies p_*(U wedge omega_E)=b.
Adding partial U+barpartial barU preserves the absolute real
Deligne class, and its second summand has zero omega push
by type. Choosing unequal cusp values yields a nonzero(4.2).
This is an actual representative ambiguity, not a formal
power-series example. Square.

## 5. A concrete relative regulator homotopy retaining the mass

The rational trivializations in(1.2) select zero boundary values.
Here is an explicit realization in the relative complex, including
the singular spectral coefficient.

Work on a small cusp disk with beta=h(q)dq. The coefficients
a h and a|h|² lie in L^p for every finite p>1, because a has
only logarithmic-power growth. Using the conjugate Cauchy kernel
for partial on a slightly larger disk, choose weak solutions
\[
 \partial_q u_1=a h,\quad u_1(0)=0,\qquad
 \partial_q u_0=a|h|^2.                                  \tag{5.1}
\]
One first extends the coefficients by a compactly supported cutoff,
convolves with 1/(pi barq), and subtracts the value at zero
from u1. For p>2, the Cauchy transform is W^(1,p), hence continuous
by the two-dimensional Sobolev estimate. Thus this value and its
zero normalization are defined. Away from the cusp the solutions
are smooth. No integration of an unknown real leading scalar
is used to choose the constant.

Put
\[
 U^{\rm loc}=\frac{i}{4\tau_2}u_0\,d\bar q
                    -\frac{i}{2\tau_2}u_1\,d\bar w .
 \tag{5.2}
\]
A direct differentiation, using a real and
barpartial bar u1=a bar h, gives
\[
 a\Omega_D=\partial U^{\rm loc}
                 +\bar\partial\overline{U^{\rm loc}}.     \tag{5.3}
\]
Its restriction as a tangential primitive on the cusp fiber
is zero: dbarq restricts to zero and u1(0)=0.
This explicitly supplies the missing boundary homotopy.

Choose a real cutoff rho equal to one near the cusp and supported
in this disk. Subtract the two derivatives of rho U^loc from
aOmega_D. Do this at both cusps. The resulting closed (1,1)
representative is zero near B. At coarse elliptic points the
same local partial/barpartial solution smooths the locally
bounded coefficient; those disks have no boundary marking.
The result is a smooth closed Deligne representative T_a^rel
vanishing near B, defining
\[
 {\cal C}_a\in H^3_{\cal D}(V,B;\mathbb R(2)).
 \tag{5.4}
\]
Equivalently use the prescribed weak relative current and its
explicit smoothing just constructed.

**[NEW] Proposition5.1.** This class is independent of the
cutoffs, local Cauchy inverses and charts with the stated zero
tangential constants, and
\[
 \frac{i}{4\pi^2c_\pi}\int_{V^\circ}
          T_a^{\rm rel}\wedge\omega_E\wedge\bar\partial l
                         =\int_Y aF\,d\mu.               \tag{5.5}
\]

*Proof.* Two choices differ by partial/barpartial primitives
whose tangential restrictions to B are zero. They are therefore
the same class in the actual relative cone(1.5). More explicitly,
on a common smaller cusp disk both choices solve the same
partial equations. The differences are antiholomorphic on the
punctured disk and continuous at zero, so they extend
antiholomorphically across zero. The mixed coefficient has value
zero, and a base normal one-form pulls back to zero on B_c.
Thus the difference of cutoff primitives is smooth near B
and is an ordinary smooth relative Deligne boundary. This does
not use a quasi-isomorphism for an unverified Sobolev-current
quotient. For chart changes, apply the same argument to the
intrinsic mixed and base (1,1) component equations in(2.4).
For the scalar, p_*(rho U^loc wedge omega_E)=
rho Omega_A u1. Its cusp value is zero. Formula(4.2) applies
also to this W^(1,p) primitive: its continuity and Holder
bound make the small-circle boundary tend to zero, and
Holder's inequality makes its derivative times 1/|q| integrable.
The conjugate primitive pushes to zero by type. The smoothing
at interior elliptic points has no boundary term. This proves
(5.5). Square.

More generally the pairing is compatible with relative-exact
changes in(1.5), not just our zero representatives. If a boundary
restriction of a primitive is Deligne-exact on B_c, its integral
against the closed omega_E is zero by compact Stokes on E.
That integral is exactly the boundary value b(c) in(4.2).
This is the relative/logarithmic Deligne product with total
degree5 and twist3 specified in §1. It proves that the particular
relative class C_j2 is nonzero because its pairing is M nonzero.

The only products involving singular objects above are the
explicit L1 functions/derivatives in §3 and the displayed
logarithmic test against a representative vanishing near B.
There is no appeal to pullback of arbitrary exact currents.
No abelian-scheme theorem is extended through a cusp fiber.

## 6. The actual rational scalar-Kummer source and its complete test

Ordinary motivic cohomology acts on compact-support motivic
cohomology. For the fixed class c_D this gives an actual map
\[
 {\cal K}: \mathcal O(Y)^*\otimes\mathbb Q
  \longrightarrow H^3_{M,c}(V^\circ,\mathbb Q(2)),\qquad
 v\longmapsto p_X^*\{v\}\cup c_D.                         \tag{6.1}
\]
The degree and twist are (1,1)+(2,1)=(3,2).
This is the compact-support cup, not an unproved push from
nonproper V^\circ. Explicitly, for f:V^\circ→Spec Q the unit
is a morphism 1→1(1)[1] on V^\circ. Apply f_! after tensoring
by (1)[2]. In this six-functor cohomological convention the
two actual morphisms are
\[
 c_D:\mathbf1_{\mathbb Q}\longrightarrow
                      f_!\mathbf1_{V^\circ}(1)[2],
 \qquad
 f_!\mathbf1_{V^\circ}(1)[2]\longrightarrow
                      f_!\mathbf1_{V^\circ}(2)[3].
\]
Their composition defines(6.1). Equivalently use
extension by zero followed by proper projection from V.
Thus the unit acts on the actual compact-support object;
no morphism extending that unit across B is assumed.
See [Déglise, §1.6](https://deglise.perso.math.cnrs.fr/docs/2014/beijing.pdf)
for the cohomology/compact-support product formalism.
The cone(1.3) retains the actual trivializations of c_D.

In the regulator, the curvature of c_D is Omega_D and its
boundary metric is zero. The unit regulator is log|v|.
Their product is log|v| Omega_D with its relative boundary
homotopy. Locally the Green identity(3.3) supplies the homotopy,
and log|v|G tends to zero in fiberwise L1 at each cusp by(3.4).
Thus its constants are exactly the zero constants in(5.1);
there is no additional cusp period. In the normalized frames
of §1 this proves
\[
 r_{\cal D}({\cal K}(v))={\cal C}_{\log|v|}.
 \tag{6.2}
\]
This is an actual rational motivic operation. It has not yet
produced the spectral coefficient j2.

**[NEW] Proposition6.1.** Every element of the image of(6.1)
has ZERO original scalar pairing(5.5).

*Proof.* A unit v on Y has divisor m(0-infinity), for an integer m,
since X is proper and these are its only omitted points.
As div u=(N-1)(0-infinity),
\[
 v^{N-1}/u^m=c\in\mathbb Q^*.
\]
Consequently
\[
 \log|v|=\frac{m}{N-1}l+\frac1{N-1}\log|c|.
\]
The constant part pairs to zero because integral F dmu=0.
The remaining part pairs to zero because F is Fricke even
and l is Fricke odd, at both cusps with absolute convergence.
Equations(6.2) and(5.5) now prove the assertion. Square.

This tests the WHOLE scalar-Kummer coefficient subspace for the
new corrected relative operation. It is not the earlier elliptic
norm push or the earlier product-polarization vanishing.
Since C_j2 has nonzero pairing, it does not belong to this
regulator image. It might belong to the regulator image of
some other relative higher cycle or a coefficient extension.
Neither that membership nor its negation is proved here.
In particular this does not exclude an integrated motive.

## 7. Completion, weighted adjoint and first missing arithmetic comparison

All formulas are linear in a. For the full completed second
coefficient they use
\[
 a=\widetilde j_2
   =j_2+\gamma_1 j_1+\gamma_2 j_0+\gamma_3 R_N,\qquad
 \Gamma(1+t)=1+\gamma_1t+\gamma_2t^2+\gamma_3t^3+\cdots .
 \tag{7.1}
\]
The gamma3 times pole term is present in the actual unpaired
current and its relative class. Only its SCALAR pairing vanishes,
along with the j0 and j1 pairings. Thus
\[
 {\cal P}({\cal C}_{\widetilde j_2})
     ={\cal P}({\cal C}_{j_2})
     ={\cal M}
     =-\frac{3N(N-1)}{2\pi^3}\ell_E L(E,2)
     =-\frac{\pi^2}{2\sqrt N}
                \langle I_L(F),\mathcal E_L''(1)\rangle .
 \tag{7.2}
\]
The last equality is the independently reviewed
[weighted adjoint](weighted-theta-adjoint-attack.md).
There is no division by L(E,2), no dropped finite coefficient
or cover degree, and no conversion of a de Rham period to a
rational Betti coordinate.

The rational geometry now supplies a concrete source complex,
the relative graph class, canonical metric homotopy and rational
scalar-Kummer subspace. The real coefficient j2 supplies a
nonzero class in its Deligne target and its exact original
scalar evaluation. The first missing comparison is a rational
relative motivic class or coefficient extension outside the
tested image(6.1), together with a regulator comparison
producing the required spectral class or the same original
functional through the specified relative boundary marking.

**[GAP RGC-389].** Construct that arithmetic source and a rational
map to D_pt tensor B2 tensor Q(1)^(-2), with its finite-place
and full-period comparison. The desired coefficient
6N(N-1)n_E must be a conclusion of this map.
The arithmetic extension and sufficient integral multiple
of the same beta2 are completed inputs; no primitivity follows.
Our real relative correction does not prove the gap merely
because its coefficient complex and Poincaré bundle are rational.

No old certificate was rerun; no shared synthesis file or
additional agent was used. The theorem-scope assertions above
are limited to the indicated primary versions. Every new
construction and comparison above passed the linked independent review.
