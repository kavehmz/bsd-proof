# An arithmetic Hodge class for the eta correction, and its elliptic projection

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Model: GPT-6 Astra, xhigh reasoning. The
[independent review](review-arithmetic-green.md) passed; its absolute-
convergence and limited-scope clarifications were applied. The objective
remains full BSD over Q; no proof of BSD or of the
rationality/integrality of its higher leading quotient is obtained here.

## 1. What is constructed

For N=389 and the normalized newform f of 389a1, the preceding work proves

$$
\ell_E=\frac{L''(E,1)}2=4\pi(J''(0)-\mathcal C_E),\qquad
110<\mathcal C_E<111.
$$

The definitions and certificate are in
[higher-period-integrality-attack.md, §5](higher-period-integrality-attack.md)
and [eta-correction-certificate.md](eta-correction-certificate.md).
Writing z=x+iy, the relevant invariant function is

$$
U(z)=\log|\eta(z)\eta(Nz)|+\frac12\log y+\frac14\log N.
\tag{1.1}
$$

This note constructs an **actual arithmetic divisor** whose Green function
is exactly -48U. Its vertical components, often invisible in a complex
formula, are retained. The natural theta lift of this class is evaluated
using a precise arithmetic Siegel–Weil theorem. Its Mordell–Weil component
and its projection to 389a1 are then proved zero. This rules out the
specific proposal that the eta Hodge class and its modular-unit quotient
already supply the two nonzero rational-point directions in the regulator.

It does not rule out an additional secondary class retaining the geodesic,
the f-differential, and new rational-point data. The arithmetic square of a
Green divisor is a star product of currents, not the pointwise square U^2.
That distinction is tested explicitly below.

Throughout the computations involving modular stacks and arithmetic theta
series we use the conventions of Du–Yang, including their multiplicity
2/|Aut(x)|. Thus degrees at the generic order-two stabilizer agree with
ordinary coarse-curve degrees. An application using the usual stack
degree 1/|Aut(x)| must retain the resulting factor of two. No such factor
is discarded in a proposed all-prime BSD comparison.

## 2. Primary arithmetic framework

**[THEOREM, sources and scope]** For squarefree N, Du–Yang use the regular,
proper, flat Deligne–Mumford model \(\mathcal X_0(N)/\mathbb Z\) of cyclic
isogenies of generalized elliptic curves. Their §4 defines arithmetic
divisors with logarithmic and log-log cusp singularities and their
intersection pairing; §6.3 constructs the metrized Hodge bundle.
Source: [arXiv:1702.07917v2](https://arxiv.org/html/1702.07917v2),
§§4, 6.2–6.3. In particular, the bad fiber at prime N has components
\(\mathcal X_N^0,\mathcal X_N^\infty\), each of multiplicity one, containing
the corresponding cusps.

The general ring construction and proper arithmetic degree for
log-singular automorphic bundles are provided by Burgos Gil–Kramer–Kühn,
[arXiv:math/0502085v1](https://arxiv.org/html/math/0502085),
Theorems 2.15, 2.17 and 5.3. For the modular stack calculations here, the
specific Du–Yang formulas are used rather than silently applying a
scheme theorem to a stack. All ring-level projection statements below
are rational unless explicitly stated otherwise.

Let \(\omega\) denote the modular Hodge line. Its standard Petersson
metric in weight k is

$$\|F(z)\|_{k,0}=|F(z)|y^{k/2}.$$

Our convention for curvature is

$$dd^c=\frac{i}{2\pi}\partial\bar\partial,
\qquad dd^c\log|v|^2=\delta_{\operatorname{div}v}.$$

An arithmetic divisor \((D,g)\) satisfies
\(dd^c[g]+\delta_{D(\mathbb C)}=\omega_D\); for a metrized line and a
rational section s its Green function is \(-\log\|s\|^2\).

## 3. Exact product and quotient, including the bad fiber

Here N is any prime. Distinguish the ordinary discriminant modular form
\(\Delta(z)=\eta(z)^{24}\) from the generalized discriminant in Du–Yang.
Use the abbreviations

$$
\Delta_1=\Delta(z),\qquad \Delta_N=\Delta(Nz),\qquad
A=\frac{\Delta_N^N}{\Delta_1},\qquad k=12(N-1),
$$
$$
B=A|_k W_N=N^{-6(N+1)}\frac{\Delta_1^N}{\Delta_N}.
\tag{3.1}
$$

The k-slash action includes \(\det(W_N)^{k/2}\). The function called
\(\Delta_N\) in Du–Yang is A in the notation of this note.

**[THEOREM, exact arithmetic input]** Du–Yang Lemma 6.4 gives, in this
prime-level notation,

$$
\operatorname{div}A=(N^2-1)\mathcal P_\infty-12N\mathcal X_N^0,
\tag{3.2}
$$
$$
\operatorname{div}B=(N^2-1)\mathcal P_0
-6(N+1)\mathcal X_N^\infty-6(N-1)\mathcal X_N^0.
\tag{3.3}
$$

The hypotheses are prime, hence squarefree, level and the specified
canonical model. Formula (3.1) follows also from their Proposition 3.4.

**[NEW] Proposition 3.1 (the Green class of U).** The rational section

$$s=N^6\Delta_1\Delta_N\quad\text{of }\omega^{24}$$

has divisor

$$
D_U=(N+1)(\mathcal P_\infty+\mathcal P_0)
        +6(\mathcal X_N^\infty-\mathcal X_N^0).
\tag{3.4}
$$

Its standard Petersson Green function is exactly

$$g_U=-\log\|s\|_{24,0}^{2}=-48U.$$

Consequently

$$
\widehat D_U=(D_U,-48U)
=\widehat c_1(\overline\omega_0^{24})
\quad\text{in }\widehat{\operatorname{CH}}^1(\mathcal X_0(N),\text{cusps})_{\mathbb Q}.
\tag{3.5}
$$

*Proof.* The discriminant transformation
\(\Delta(-1/z)=z^{12}\Delta(z)\) gives (3.1) with the stated power of N.
Thus

$$AB=N^{-6(N+1)}(\Delta_1\Delta_N)^{N-1}.$$

Taking divisors and using
\(\operatorname{div}N=\mathcal X_N^0+\mathcal X_N^\infty\), equations
(3.2)–(3.3) yield

$$
\operatorname{div}(\Delta_1\Delta_N)
=(N+1)(\mathcal P_\infty+\mathcal P_0)-12\mathcal X_N^0.
$$

Multiplying by N^6 gives (3.4). Since

$$
\log\|s\|_{24,0}
=6\log N+\log|\Delta_1\Delta_N|+12\log y=24U,
$$

the Green function is -48U. This is the first arithmetic Chern class
of the actual metrized Hodge power, represented by its rational section,
which proves (3.5). Its membership with the asserted cusp growth follows
also directly from the expansion in §4. \(\square\)

**[NEW] Proposition 3.2 (the quotient is principal, with a vertical term).**
The normalized weight-zero modular unit

$$v=N^{-6}\frac{\Delta_1}{\Delta_N}$$

has divisor

$$
D_v=(N-1)(\mathcal P_0-\mathcal P_\infty)
       +6(\mathcal X_N^0-\mathcal X_N^\infty).
\tag{3.6}
$$

In particular \(\widehat{\operatorname{div}}v=(D_v,-\log|v|^2)\) is
zero in the arithmetic Chow group, and its generic divisor is
\((N-1)(0-\infty)\).

*Proof.* Combine (3.2) with the divisor of \(\Delta_1\Delta_N\) just
computed. Solving the two linear relations gives

$$
\operatorname{div}\Delta_1=\mathcal P_\infty+N\mathcal P_0,
\qquad
\operatorname{div}\Delta_N=N\mathcal P_\infty+\mathcal P_0
                                  -12\mathcal X_N^0.
$$

Subtract and include \(N^{-6}\). This is (3.6). Vanishing of the full
arithmetic principal divisor is a defining rational-equivalence relation.
It includes both the displayed vertical term and the logarithm of N in
the archimedean function. \(\square\)

For 389 these formulas become

$$
D_U=390(\mathcal P_\infty+\mathcal P_0)
                 +6(\mathcal X_{389}^\infty-\mathcal X_{389}^0),
$$
$$
D_v=388(\mathcal P_0-\mathcal P_\infty)
                 +6(\mathcal X_{389}^0-\mathcal X_{389}^\infty).
$$

The product of eta functions is a section with curvature; their ratio,
after taking the 24th power and this normalization, is a rational
modular unit. Treating both as weight-zero units loses this distinction
and the explicit bad-fiber terms.

## 4. Curvature, singularities, and the proposed square

**[NEW] Proposition 4.1 (curvature and boundary growth).** On the open
modular curve,

$$
dd^cU=-\frac1{8\pi}\frac{dx\,dy}{y^2},\qquad
\omega_{D_U}=\frac6\pi\frac{dx\,dy}{y^2}.
\tag{4.1}
$$

At the cusp infinity, with q=exp(2 pi i z),

$$
U=\frac{N+1}{24}\log|q|+\frac12\log(-\log|q|)
   +\frac14\log N-\frac12\log(2\pi)+O(|q|).
\tag{4.2}
$$

The corresponding assertion at zero follows by Fricke invariance. As a
current on the compact curve,

$$
dd^c[-48U]+\delta_{(N+1)(0+\infty)}
=\frac6\pi\frac{dx\,dy}{y^2}.
\tag{4.3}
$$

*Proof.* The logarithm of the absolute value of a nonvanishing
holomorphic eta product is harmonic on the upper half-plane. Direct
differentiation gives
\(dd^c\log y=-(4\pi)^{-1}dx\,dy/y^2\), proving (4.1).
The q-product has \(\Delta_1\Delta_N=q^{N+1}(1+O(q))\); substituting
\(y=-\log|q|/(2\pi)\) gives (4.2). The linear logarithmic term gives
the divisor current by Poincaré–Lelong; the remaining log-log term has
the locally integrable hyperbolic curvature in (4.3). The same
calculation at the other cusp completes the current identity. \(\square\)

With the declared coarse-compatible counting, the hyperbolic area is
\((\pi/3)(N+1)\), so the integral of the curvature in (4.1) is
\(2(N+1)\), equal to the horizontal divisor degree. This also checks
the factors 24, 48 and pi independently.

**[THEOREM, arithmetic product type]** Gillet–Soulé,
[Arithmetic intersection theory, Publ. Math. IHÉS 72 (1990), 93–174](https://www.numdam.org/item/10.1007/BF02699132.pdf),
§§2.1 and 4.3, define the arithmetic product using a star product of
Green currents. Du–Yang Proposition 4.1 supplies its cusp-regularized
version in the present model. For disjoint divisors away from the
boundary, its schematic form is

$$g_1*g_2=g_1\delta_{D_2}+\omega_{D_1}g_2,$$

up to the usual exact-current equivalence. At a shared cusp the
regularized formula includes explicit boundary terms, not a product
of the two Green functions.

The degree check is therefore:

| Candidate | Arithmetic/Deligne location | Analytic degree |
|---|---|---|
| \(\widehat D_U\) | arithmetic codimension 1 | Green function, type (0,0); curvature (1,1) |
| \(\widehat D_U^2\) | arithmetic codimension 2, followed by degree to \(\widehat{\operatorname{CH}}^1(\mathbb Z)\) | Green current of type (1,1), integrated over the whole complex curve |
| \(\int_\gamma U^2\alpha\) | proposed path-period functional | a one-form integrated over a real relative one-chain |
| ordinary \(K_2\) regulator on a curve | \(H^2_{\mathcal D}(X,\mathbb R(2))\) | a closed real one-form, with residue conditions |

Here \(\alpha=2\pi i f(z)dz\) and \(\gamma\) is the path from zero to
infinity. A Deligne pairing of two metrized lines gives a metrized line
over the base; its degree gives the same arithmetic intersection (see
Gillet–Soulé §4.3.8). It does not change the analytic degree of the
star-product formula into that of the last path integral.

**[NEW] Lemma 4.2 (a literal Green square is not the requested class).**
The function U^2 is not a Green function for a divisor with a
log-singular line metric of the type used above. Moreover the complex
one-form U^2 alpha is not closed. For a normalized weight-two f its
real part is not closed either.

*Proof.* Equation (4.2) gives a nonzero leading \((\log|q|)^2\) term
in U^2. A divisor Green function for such a line has a linear
\(\log|q|\) term plus log-log metric growth. No change of divisor
subtracts that square term.

On an open set where U and alpha are nonzero,
\(d(U^2\alpha)=2U\bar\partial U\wedge\alpha\).
If this vanished identically, U would be holomorphic there, hence
locally constant because real, contradicting (4.1).

For the real assertion, put \(a=\pi(N+1)/12>0\). Near infinity,
\(U=-ay+\tfrac12\log y+O(1)\),
\(\partial_yU=-a+O(1/y)\), and \(\partial_xU=O(e^{-2\pi y})\).
At x=1/4 the normalization f=q+O(q^2) gives
\(\operatorname{Re}\alpha=-2\pi e^{-2\pi y}dx+O(e^{-4\pi y})(dx,dy)\).
Thus \(2U\,dU\wedge\operatorname{Re}\alpha\) has a nonzero leading
term of size \(4\pi a^2y e^{-2\pi y}dx\wedge dy\). It cannot vanish
for all sufficiently large y. \(\square\)

Allowing arbitrary singular currents can enlarge the group of possible
representatives; it does not by itself add an algebraic cycle or an
integral regulator comparison. Ordinary K_2 symbols give closed
regulator one-forms. The literal form in Lemma 4.2 is not such a
representative. Likewise, if u(z)=log(eta(z)eta(Nz)) is its holomorphic
branch on the upper half-plane, then \(u^2\alpha\) is closed and
\((u^2-U^2)\alpha\) has the negative of the same nonzero exterior
derivative. The corrected numerical difference still needs secondary
data if represented in this way.

## 5. An actual arithmetic theta comparison for this Hodge class

This section pushes the constructed class through a nontrivial existing
arithmetic comparison rather than assuming one for the target derivative.

Use precisely the theta kernel \(\Theta_L(\tau,z)\), normalized
Eisenstein series \(\mathcal E_L(\tau,s)\), and arithmetic theta
function \(\widehat\phi(\tau)\) of Du–Yang. Let

$$
C_{\rm DY}=\frac{\log(4\pi)+\gamma_{\rm Euler}}2,\qquad
c=4\pi e^{-C_{\rm DY}},\qquad
\kappa_N=\frac{N\log N}{2(N-1)}-\frac12\log c.
\tag{5.1}
$$

Their norm in weight k is \(\|F\|_{k,\rm DY}=|F|(cy)^{k/2}\),
and their absolutely convergent theta lift is

$$I(\tau,F)=\int_{X_0(N)}F(z)\Theta_L(\tau,z).$$

**[THEOREM, exact inputs]** Du–Yang Theorem 1.6 gives

$$
I(\tau,1)=\frac2{N-1}\mathcal E_L(\tau,1),\qquad
I(\tau,\log\|A\|_{k,\rm DY})
=I(\tau,\log\|B\|_{k,\rm DY})=-12\mathcal E_L'(\tau,1).
\tag{5.2}
$$

Their Theorem 1.3 gives

$$
\langle\widehat\phi,\widehat\omega_{\rm DY}\rangle
=\frac1{N-1}\left(\mathcal E_L'
-\frac{N}{N-1}\log N\,\mathcal E_L\right),\qquad
\langle\widehat\phi,a(1)\rangle=\frac1{N-1}\mathcal E_L,
\tag{5.3}
$$

where the values and derivatives in (5.3) are at s=1. These theorems
apply to squarefree N with their specified lattice and normalization;
no elliptic-curve rank hypothesis enters them.

**[NEW] Proposition 5.1 (the theta lift and arithmetic intersection of U).**
For prime N,

$$
I(\tau,U)=-\frac1{N-1}\mathcal E_L'(\tau,1)
             +\frac{2\kappa_N}{N-1}\mathcal E_L(\tau,1),
\tag{5.4}
$$
$$
\boxed{\langle\widehat\phi(\tau),\widehat D_U\rangle
=-24I(\tau,U).} \tag{5.5}
$$

*Proof.* Equation (3.1) and the metric definition give

$$
\log\|A\|_{k,\rm DY}+\log\|B\|_{k,\rm DY}
=24(N-1)U-12N\log N+12(N-1)\log c.
$$

Thus U is the sum of those two logarithms divided by 24(N-1), plus
kappa_N. Apply the linear theta lift and (5.2) to get (5.4).

Changing the weight-one metric from \(y^{1/2}\) to \((cy)^{1/2}\)
subtracts log c from its Green function. Hence
\(\widehat\omega_0=\widehat\omega_{\rm DY}+a(\log c)\).
By (3.5) and (5.3),

$$
\langle\widehat\phi,\widehat D_U\rangle
=\frac{24}{N-1}\mathcal E_L'
+\frac{24}{N-1}
  \left(\log c-\frac{N\log N}{N-1}\right)\mathcal E_L.
$$

This equals -24 times (5.4), by (5.1). All vertical and metric
normalizations have remained in the calculation. \(\square\)

Thus a genuine arithmetic Green-function identity for U exists and has
been made explicit. It is linear in U, uses a (1,1) theta kernel on the
whole modular curve, and yields the first s-derivative of an Eisenstein
series. It is not an identity for \(\int_\gamma U^2\alpha\) or for the
second derivative of the fixed elliptic L-function.

The genus-two version is also not a second-derivative substitution:
Sankaran–Shi–Yang, [arXiv:2206.05823v1](https://arxiv.org/pdf/2206.05823),
Theorem 2.14, for N>3 odd squarefree, relates arithmetic codimension-two
degrees to \(\partial_s\mathcal E(\tau,s)|_{s=0}\), a **first**
derivative of a genus-two Siegel Eisenstein series. Its degree/cycle
construction is compatible with the second row of the table in §4.
No specialization from that theorem to the desired fixed weight-two
second derivative is asserted here.

## 6. The first elliptic comparison gives zero

Let \(\pi:X_0(389)\to E\) be a rational modular parametrization,
normalized by \(\pi(\infty)=O\), and let \(\pi_*:J_0(389)\to E\)
be its induced homomorphism. The previously certified torsion group of
389a1 is trivial.

For an arithmetic divisor \((D,g)\), define its rational Mordell–Weil
projection relative to the rational cusp infinity by

$$
\operatorname{AJ}_{\infty}(D,g)
=[D_{\mathbb Q}-\deg(D_{\mathbb Q})\infty]
\in J_0(N)(\mathbb Q)\otimes\mathbb Q.
\tag{6.1}
$$

This is well-defined: a principal arithmetic divisor restricts to a
principal generic divisor, a vertical divisor has zero generic fiber,
and metric changes do not change the generic line bundle. Its elliptic
f-component is \(\pi_*\operatorname{AJ}_{\infty}\). This definition
does not assert that the complete arithmetic Chow group, including its
infinite-dimensional metric functions, has been projected to zero.

**[NEW] Proposition 6.1 (vanishing of the point-valued candidate).**
For the product and quotient classes constructed above,

$$
\operatorname{AJ}_{\infty}(\widehat D_U)=0,
\qquad \pi_*\operatorname{AJ}_{\infty}(\widehat D_U)=0.
\tag{6.2}
$$

At N=389 the equality \(\pi(0)=O\) holds integrally in E(Q).
Every degree-zero divisor supported on the two rational cusps therefore
maps to zero in E(Q).

*Proof.* The horizontal part of D_U has degree 2(N+1), so (6.1) gives
the class of \((N+1)(0-\infty)\). By (3.6), \((N-1)(0-\infty)\)
is principal on the generic fiber. It follows that the class is torsion,
hence zero after tensoring with Q. Its image in E(Q) is torsion as well.
For E=389a1 that torsion group is zero, so \(\pi(0)-\pi(\infty)=0\).
Every degree-zero cusp divisor is an integral multiple of their
difference. \(\square\)

This agrees with the arithmetic decomposition in Du–Yang §8,
Propositions 8.2–8.3: the Mordell–Weil component is determined by the
degree-zero generic Picard class, while degree, vertical and metric
components are separate. Replacing a log-singular metric by a smooth
one changes an a(function) term and does not manufacture a nonzero
Mordell–Weil component.

**[NEW] Corollary 6.2 (the proposed height determinant vanishes).**
Take any two point classes obtained by rational linear combinations of
the degree-zero generic divisors of the eta product, eta quotient and
cusps, and then project them to 389a1. Their Néron–Tate height Gram
determinant is zero.

*Proof.* Both point classes are zero by Proposition 6.1. \(\square\)

The actual full basis P=(-1,1), Q=(0,-1) has a strictly positive
regulator. Thus this explicitly constructed point-valued candidate
cannot be the required regulator tensor. The conclusion concerns that
candidate: a new correspondence involving other cycles or secondary
data could produce other rational points.

An integral arithmetic divisor or an integral line module also does
not imply that its arithmetic degree is an integer. For example the
free line Z on Spec Z with norm \(\|1\|=e^{-a}\) has arithmetic degree
a for any real a. The relevant integer statement in BSD must concern
the ratio to the specifically normalized period–height lattice, not
integrality of the underlying divisor coefficients alone.

## 7. Testing the corrected difference itself

There is one additional structural fact that helps delimit what the
Hodge class can contribute. Set \(t=\log(\sqrt N y)\),
\(\rho(t)=y f(iy)\), and let u(y)=log(eta(iy)eta(iNy)). For sign +1,
rho is even and \(U(t)=u(y)+t/2\) is even.

**[NEW] Proposition 7.1 (independence from an added invariant potential).**
Let H(t) be any even real function for which the constituent square
moments and the cross-term integrals used below converge absolutely.
Replace U by U+H and u by u+H in the second eta moment and
its correction. Then

$$
\int\rho\big((u+H)^2-(U+H)^2\big)
=\int\rho(u^2-U^2)=\frac14\int\rho(t)t^2dt.
\tag{7.1}
$$

*Proof.* The difference introduced by H is
\(2\rho H(u-U)=-\rho Ht\), an odd integrable function. Its integral
is zero. Substituting u=U-t/2 in the remaining expression leaves
\(\rho(-Ut+t^2/4)\); the first term is odd. \(\square\)

For compactly supported smooth even H, convergence is immediate. Thus
the corrected difference is insensitive to adding such a
Fricke-invariant potential; U by itself is auxiliary to that identity.
This does not prove that the corrected period lacks an arithmetic
interpretation. For the proposed literal representation, retaining the
holomorphic/frame or path data is a construction requirement; invariance
alone is not a general obstruction to other arithmetic constructions.

The exact completed construction sequence in this attempt is therefore

$$
U\ \longmapsto\ \widehat D_U
\ \longmapsto\ \langle\widehat\phi,\widehat D_U\rangle=-24I(U),
$$

with an explicit Eisenstein expression, while

$$
\widehat D_U\ \longmapsto\ J_0(389)(\mathbb Q)\otimes\mathbb Q
\ \longmapsto\ E(\mathbb Q)\otimes\mathbb Q
$$

is zero. The attempted arithmetic construction has reached its first
nontrivial comparison and the required elliptic projection; neither
produces the missing rank-two height determinant.

## 8. Precise remaining construction problem

**[GAP AG-389]** Let E, f, P and Q be as above, with the full real Néron
period and the BSD height convention of the certified regulator. Construct
an algebraic secondary cycle/extension with its specified integral
structure, retaining the relative cusp path and the f-component, and a
proved regulator map whose value is

$$
4\pi(J''(0)-\mathcal C_E)
$$

and whose image lies in

$$
\mathbb Z\,\Omega_E\big(h(P,P)h(Q,Q)-h(P,Q)^2\big).
$$

Its point-valued or determinant-valued arithmetic realization must use
nonzero Mordell–Weil directions; the cusp-supported Hodge and modular-unit
classes in §§3–6 cannot supply them. Its Green/Deligne representative
must include the terms needed for the correct degree and boundary
conditions; the nonclosed one-form in §4 is not enough. The full finite
fiber and metric normalizations must be included, as they were for
\(\widehat D_U\).

This is an unmet construction problem, not the definition of a new
zeta element by its desired real period. The actual class and actual
theta comparison constructed here can be used as inputs or tests, but
no morphism from them to the required integral determinant line has
been produced.

## 9. Verification and restart record

New formulas checked in the independent review are (3.4)–(3.6), the curvature
and boundary factors in §4, the norm conversion and arithmetic identity
(5.4)–(5.5), the Mordell–Weil projection in §6, and Proposition 7.1.
All source theorems were read in the versions and sections linked above.
The displayed vertical-divisor calculation is algebraic and was not
replaced by numerical evidence. No existing certificate was rerun.

Only this note and [arithmetic-green-checkpoint.md](arithmetic-green-checkpoint.md)
were edited in this task. The strongest next task is a secondary
construction incorporating noncuspidal point data and a relative
regulator pairing; merely taking the arithmetic square of the Hodge
class or invoking a genus-two first-derivative theorem repeats the
specific mismatch already checked here.
