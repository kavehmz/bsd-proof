# A higher arithmetic theta construction for the retained response

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
The bounded constructions and all new deductions passed
[independent review](review-higher-arithmetic-theta.md).
Restart: [checkpoint](higher-arithmetic-theta-checkpoint.md).
The objective remains full BSD over Q.

This note seeks an actual secondary or higher-dimensional arithmetic
cycle for the completed spectral response retained in the
[harmonic construction](harmonic-theta-arithmetic-attack.md).
The original f-weighted regulator comparison remains part of the target.

## 1. Fixed response and comparison line

Use exactly the Du–Yang v2 normalization of the reviewed harmonic note.
Write $\mathcal E^{(r)}(\tau)=\partial_s^r\mathcal E_L(\tau,s)|_{s=1}$,
$$\Gamma(1+t)\xi(1+t)=t^{-1}+h_0+h_1t+h_2t^2+O(t^3),\qquad
h_0=-\frac{\gamma+\log(4\pi)}2,$$
and retain the full response
$$\mathcal Q=\frac{\mathcal E^{(3)}}6+\frac{h_0}2\mathcal E^{(2)}
                   +h_1\mathcal E^{(1)}+h_2\mathcal E^{(0)}. \tag{1.1}$$
The generating function, rather than a free metric normalization, fixes
all h-coefficients and the pole contribution. In particular
$\Delta_{3/2}^3\mathcal Q=-\mathcal E^{(0)}/64$.
The desired number before the second theta lift is still
$$\mathcal M=-\frac{3N(N-1)}{2\pi^3}\ell L(E,2),\qquad N=389.$$
Its arithmetic target remains
$$D_{\rm pt}\otimes B_2\otimes\mathbb Q(1)^{-2},$$
with frame $-\Omega_E\operatorname{Reg}_E L(E,2)/(4\pi^3)$ and
coefficient $6N(N-1)n_E$. The rational arithmetic extension of the
actual $B_2$ class is a completed input. Neither it nor any class
below is called integrally primitive.

## 2. A genuine genus-two arithmetic cycle and a precise projection

Our first space is the regular arithmetic modular stack
$\mathcal X=\mathcal X_0(389)$. We use the arithmetic special cycles
of Sankaran–Shi–Yang, *A genus two arithmetic Siegel–Weil formula on
$X_0(N)$*, [arXiv:2206.05823v1](https://arxiv.org/pdf/2206.05823v1),
Definitions 2.11–2.13, Theorem 2.14 and Corollary 4.16. The same
formulas occur in the [author's 45-page revision](https://home.cc.umanitoba.ca/~sankaras/ArithSW-rev1.pdf),
where the rank-one analytic formula is (223), and its genus-one
normalization comparison is (226). We keep that revision's notation
below. Its arithmetic degree is the stack degree, with the factor
$1/2$ for the generic central stabilizer recorded in Remark 2.7.
It is not silently replaced by effective integration.

For a nonsingular positive T, the actual cycle parametrizes a cyclic
N-isogeny $\phi:E\to E'$ together with two Rosati-skew endomorphisms
$\alpha_1,\alpha_2$ whose moment matrix is NT and for which
$\alpha_i\phi^{-1}$ are actual homomorphisms. This last condition is
part of the moduli problem. The cycle has codimension two and is
supported at a supersingular finite fiber when its difference set has
one prime. Its regulator is arithmetic degree, not a height assigned
to an arbitrary cohomology representative. The source supplies the
corresponding Green currents for the other signatures.

The complete genus-two degree series is
$$\sum_T\widehat{\deg}\widehat Z(T,V)q^T
       =C_N\,\partial_u E_2(Z,u,\Phi_2^L)|_{u=0},\qquad
C_N=\frac{N+1}{24}. \tag{2.1}$$
Here Z is in the genus-two Siegel half-space, V=Im Z, and the
quadratic lattice is
$L=\{\left(\begin{smallmatrix}a&b/N\\c&-a\end{smallmatrix}\right):
a,b,c\in\mathbb Z\}$ with quadratic form $N\det$. This is a
theorem for an actual arithmetic cycle with a fixed archimedean
construction. No derivative order is changed in quoting it.

The concrete projection tested here is the rank-one Fourier face
$T=\operatorname{diag}(0,t)$ with $V=\operatorname{diag}(v_1,v_2)$.
It is obtained by selecting the zero coefficients in Re Z11 and
Re Z12; selecting a further t-coefficient is then unambiguous.
It is not the assertion that an arbitrary pullback of a genus-two
series equals a genus-one third derivative.

Put
$$\widehat\omega_{\rm mod}=-2\widehat\omega_N
                 -\widehat{\mathcal X}_N^0+a(\log N).$$
For t>0 the actual selected cycle is
$$\boxed{\widehat Z_{0,t}(v_1,v_2)
  =\widehat Z(t,v_2)\,\widehat\omega_{\rm mod}
                       -a(\log v_1\,\delta_{Z(t)(\mathbb C)}).}
\tag{2.2}$$
Thus it has a specified arithmetic intersection and boundary current,
rather than an unspecified second height. Its dependence on
$\log v_1$ is affine in the arithmetic Chow group.

The other terms of this projection are not discarded. For t<0 replace
$Z(t)$ in (2.2) by the modified cusp divisor
$Z^*(t,v_2)=Z(t)+g(t,v_2)\mathcal S$, where $\mathcal S$ is the sum
of BOTH cusps and
$$g(t,v_2)=\frac{\sqrt N}{2\pi\sqrt{v_2}}
          \beta_{3/2}(-4\pi t v_2)
\quad\hbox{if }-Nt\hbox{ is a square},$$
and zero otherwise; $\beta_{3/2}(r)=\int_1^\infty e^{-ru}u^{-3/2}du$.
At T=0 the source's exact class is
$$\widehat Z(0,V)=\widehat\omega_{\rm mod}^2
                   +a(\log\det V\,[\Omega]),\qquad
\Omega=\frac{d\mu}{2\pi}. \tag{2.3}$$
Its degree is $\widehat{\deg}(\widehat\omega_{\rm mod}^2)
+C_N\log(v_1v_2)$: the stack integral of $\Omega$ is $(N+1)/12$
and arithmetic degree of an archimedean two-current is half that
integral. Equations (2.2)–(2.3) retain the vertical modification and
the entire zero and negative-square boundary response.

## 3. What that higher cycle actually produces

Use the source's classical genus-one series
$E_1(\tau,u,\Phi_1^L)$ and its EXACT normalization comparison
$$\mathcal E_L(\tau,s)_{\mu_0}
 =A_N(s)E_1(\tau,s-1/2,\Phi_1^L),$$
$$A_N(s)=-\frac{s}{4\pi}\xi(2s)(1-N^{-2s})N^{1/2+3s/2}.
\tag{3.1}$$
This is the source's formula (226), fixing the scalar $\mu_0$
component of the vector-valued Du–Yang series. Its arithmetic degree
remains the one in (2.1); no additional factor of two is inserted
from an informal stack comparison. Let $\mathcal E_t^{(r)}$ denote
the t-th Fourier TERM, including its $q^t$, of that component's
r-th s-derivative at one.

**[NEW] Proposition 3.1 (complete rank-one response).** For t>0,
$$\boxed{\widehat{\deg}\widehat Z_{0,t}(v_1,v_2)q^t
 =-\frac{1}{N-1}\left(2\mathcal E_t^{(1)}
        +\left(\log v_1-\frac{2N\log N}{N-1}\right)
                                    \mathcal E_t^{(0)}\right).}
\tag{3.2}$$

*Proof.* Corollary 4.16 in the source gives, in its adelic Whittaker
notation,
$$v_1^{-3/4}E'_{2,T}(g_V,0)
 =2W'_t(g_{v_2},1/2)
             +(\log v_1+c_N)W_t(g_{v_2},1/2),$$
$$c_N=2+4\frac{\xi'(2)}{\xi(2)}
                        +\frac{N-1}{N+1}\log N. \tag{3.3}$$
The derivative on the first W is in its genus-one inducing parameter.
Classical conversion multiplies by $\det(V)^{-3/4}$, so (3.3)
becomes the same formula for classical Fourier terms. In (3.1) a
genus-one parameter derivative is an s-derivative with slope one.
Substitution into (3.3) therefore gives
$$C_N C'_{2,T}(V,0)q^t
 =\frac{C_N}{A_N(1)}\left(2\mathcal E_t^{(1)}
   +\left(\log v_1+c_N-2\frac{A_N'(1)}{A_N(1)}\right)
                                            \mathcal E_t^{(0)}\right).$$
Directly,
$$A_N(1)=-\frac{N^2-1}{24},\qquad
\frac{A_N'(1)}{A_N(1)}
 =1+2\frac{\xi'(2)}{\xi(2)}
       +\left(\frac{2}{N^2-1}+\frac32\right)\log N.$$
Thus $C_N/A_N(1)=-1/(N-1)$ and
$$c_N-2A_N'(1)/A_N(1)=-\frac{2N}{N-1}\log N.$$
Apply the exact arithmetic-degree theorem (2.1) to conclude (3.2).
All archimedean and bad-level factors were kept in (3.3) before
cancellation; in particular the last logarithm is not dropped.
$\square$

This yields an explicit residual for the proposed identification with
the retained response: subtracting (3.2) from its t-th term gives
$$\frac{\mathcal E_t^{(3)}}6+\frac{h_0}2\mathcal E_t^{(2)}
 +\left(h_1+\frac2{N-1}\right)\mathcal E_t^{(1)}
 +\left(h_2+\frac{\log v_1}{N-1}
                    -\frac{2N\log N}{(N-1)^2}\right)\mathcal E_t^{(0)}.
\tag{3.4}$$
It is a real mismatch for this operation, not only a difference of
names: the third weight-3/2 Laplacian of (3.4) is
$-\mathcal E_t^{(0)}/64$, while the selected genus-two response is
killed by its second Laplacian. At t=1 the value term is nonzero:
the lattice vector
$\left(\begin{smallmatrix}0&-1/N\\1&0\end{smallmatrix}\right)$
has norm one and supplies an actual complex special point, so the
genus-one degree coefficient is positive. Thus even this one
coefficient cannot agree with the proposed third response.
Derivatives in the auxiliary $\log v_1$ only differentiate the affine
formula; its second such derivative is zero, including the zero term
(2.3). None of this excludes a different projection or an additional
secondary cycle. It tests the actual face projection (2.2).

## 4. An explicit higher polylogarithm cycle on a four-dimensional space

Let S be a connected fine modular curve of full level 35N over a
number field containing its level coordinates, and let
$\pi:\mathscr E\to S$ be the universal elliptic curve. The base is
smooth, affine and one-dimensional. Put
$$U=\mathscr E\setminus\mathscr E[5],\quad
A=\mathscr E\times_S\mathscr E\times_S\mathscr E,\quad
W=A\setminus A[5]. \tag{4.1}$$
A has dimension four and abelian relative dimension three. Choose
nonzero 5-torsion sections $\sigma,\tau,\upsilon$. The theorem used
below is not asserted over the compactified cusp fibers.

Write $\omega=\pi_*\Omega^1_{\mathscr E/S}$. The discriminant
trivializes $\omega^{12}$ on S. For a nonzero 5-torsion section
$\sigma$, the rigidified line
$$\mathcal O_{\mathscr E}(\sigma-0)\otimes\pi^*\omega^{-1}$$
has order dividing five in the relative Picard scheme. Indeed its
restriction at zero is trivial, since
$0^*\mathcal O_{\mathscr E}(\sigma-0)\simeq\omega$, and its relative
Picard point is torsion. It follows that
$\mathcal O_{\mathscr E}(60(\sigma-0))$ is trivial. Choose a rational
function $f_\sigma$ with EXACT divisor $60(\sigma-0)$ on $\mathscr E$.
There is no missing base divisor: the discriminant is nonvanishing
on this open modular base.

Let T be the actual trace $\operatorname{tr}_{[6]}$ on units of U:
restrict to $[6]^{-1}U$ and take the field norm along [6]. In
additive notation for units tensored with $\mathbb Q$, define
$$u_\sigma=\frac1{60}[f_\sigma],\qquad
\xi_\sigma=\frac{36-T}{35}u_\sigma
 =\frac1{2100}\left[
       \frac{f_\sigma^{36}}{\operatorname{Norm}_{[6]}f_\sigma}\right]
       \in H^1_M(U,\mathbb Q(1)). \tag{4.2}$$
Use the same construction for $\tau,\upsilon$.

**[NEW] Lemma 4.1 (actual norm projector).** The class $\xi_\sigma$
is independent of $f_\sigma$, satisfies $T\xi_\sigma=\xi_\sigma$,
and has localization residue $[\sigma]-[0]$.

*Proof.* Since $6\sigma=\sigma$, norm pushforward preserves the
divisor of $f_\sigma$. Thus $(T-1)u_\sigma$ has zero divisor on the
entire proper elliptic family and is pulled back from
$\mathcal O(S)^*\otimes\mathbb Q$. On base units T is multiplication
by $\deg[6]=36$. Consequently
$$(T-36)(T-1)u_\sigma=0.$$
This proves invariance in (4.2). Its residue is multiplied by
$(36-1)/35=1$. Two choices of $f_\sigma$ differ by a base unit,
which the same projector kills. Conversely an invariant base unit
is zero rationally, since 35 is nonzero. $\square$

There are closed regular immersions of codimension two
$$\begin{aligned}
i_1:U&\longrightarrow W,&x&\longmapsto(x,\tau,\upsilon),\\
i_2:U&\longrightarrow W,&y&\longmapsto(0,y,\upsilon),\\
i_3:U&\longrightarrow W,&z&\longmapsto(0,0,z).
\end{aligned} \tag{4.3}$$
Each missing point of the complete elliptic curve lands in $A[5]$,
so its image is closed in W. Define the actual higher Chow class
$$\boxed{\Xi=(i_1)_*\xi_\sigma+(i_2)_*\xi_\tau+(i_3)_*\xi_\upsilon
   \in H^5_M(W,\mathbb Q(3))=\operatorname{CH}^3(W,1)_{\mathbb Q}.}
\tag{4.4}$$
Its cycle is the sum of the graphs of the three rational functions
in (4.2), pushed along (4.3), with coefficient $1/2100$.
Their Bloch boundaries inside W vanish. In A the residues telescope:
$$\begin{aligned}
&[(\sigma,\tau,\upsilon)]-[(0,\tau,\upsilon)]\\
&\quad+[(0,\tau,\upsilon)]-[(0,0,\upsilon)]\\
&\quad+[(0,0,\upsilon)]-[(0,0,0)]\\
&\hspace{30mm}=[(\sigma,\tau,\upsilon)]-[(0,0,0)]. \tag{4.5}
\end{aligned}$$
In particular $\Xi\ne0$. Multiplication by 2100 gives an integral
Bloch cycle on this open space over the chosen number field. No
integral extension at all arithmetic primes or primitivity follows.

The trace operation on W commutes with these pushed cycles.
After restriction to $[6]^{-1}W$, an $i_j$-curve is restricted
precisely to $[6]^{-1}U$, and $[6]i_j=i_j[6]$ because its fixed
sections are 5-torsion. Proper pushforward and open restriction
therefore prove commutation. Thus $\Xi$ has trace eigenvalue one.

Kings–Rössler,
[*Higher analytic torsion, polylogarithms and norm compatible elements
on abelian schemes*, 1412.2925v2](https://arxiv.org/pdf/1412.2925v2),
Corollary 2.2.2 and Lemma 4.2.8, give a residue isomorphism on this
trace-weight-zero part. It identifies the finite cycle (4.4) with
the actual degree-zero polylogarithm attached to
$a=(\sigma,\tau,\upsilon)$. The cycle was constructed before that
identification, without defining a class from its desired real value.

## 5. Its canonical higher analytic torsion regulator and projections

Let $\mathfrak g_A$ denote the source's $\mathfrak g_{A^\vee}$,
the canonical zero-section Green current class ON A in
Kings–Rössler Theorem 4.1.1. Current classes here are taken modulo
$\operatorname{im}\partial+\operatorname{im}\bar\partial$.
It is specified by the canonically
metrized Poincaré bundle and arithmetic Chern character. Its
complement restriction is the indicated component of Bismut–Köhler
higher analytic torsion. It is not an adjustable metric. The map is
$$\operatorname{cyc}_{\rm an}:
H^5_M(W,\mathbb Q(3))\longrightarrow
             H^5_{D,\rm an}(W_{\mathbb R},\mathbb R(3)). \tag{5.1}$$
Its current representative has type (2,2), and retains all three
Tate twists. Theorem 4.1.2 and Proposition 4.2.4 of the source,
with the residue sign in (4.5), give exactly
$$\boxed{-2\operatorname{cyc}_{\rm an}(\Xi)
                =(T_{-a}^*\mathfrak g_A-\mathfrak g_A)|_W.} \tag{5.2}$$
The source's product formula, Lemmas 4.2.7–4.2.8, also represents
this as the sum of Gysin pushes of the three elliptic unit regulators.
This is a genuine higher-dimensional secondary regulator, not a
third ordinary divisor product on $\mathcal X_0(N)$.

**[NEW] Proposition 5.1 (nonzero torsion projection).** For
$U^{(3)}=U\times_SU\times_SU\subset W$ one has
$$\Xi|_{U^{(3)}}=0.$$
Hence the pullback along any section whose three coordinates are
nonzero 7-torsion is zero in motivic cohomology before any regulator.

*Proof.* Each support in (4.3) fixes two coordinates in
$\mathscr E[5]$ and is disjoint from $U^{(3)}$. Its restricted
higher Chow cycle is therefore zero. Nonzero 7-torsion is disjoint
from 5-torsion, so the indicated sections factor through that open.
$\square$

The nonzero class remains on the three partial-torsion supports
before this projection, as recorded by (4.5). This calculation
does not make the whole class or all of its possible projections zero.

For an alternative scalar projection retain the elliptic fibers.
Let
$$P=\mathcal O_{\mathscr E}(0)\otimes\pi^*\omega,\qquad
L=\bigotimes_{j=1}^3\operatorname{pr}_j^*P.$$
P is the rigidified symmetric principal polarization line.
For a torsion section t, the theorem of the cube gives $t^*P$
torsion: if Dt=0 then
$(t^*P)^{D^2}\simeq0^*P\simeq\mathcal O_S$.
On U, the canonical section of $\mathcal O(0)$ is nowhere zero,
so $P|_U\simeq\pi^*\omega$.

**[NEW] Proposition 5.2 (polarization projection).**
$$\Xi\smile c_1(L)=0
                       \quad\text{in }H^7_M(W,\mathbb Q(4)). \tag{5.3}$$
For the canonical metrized polarization the corresponding compact
fiber integral of the regulator representative against
$c_1(\overline L)$ is identically zero on S.

*Proof.* On each $i_j(U)$ the restriction of L is $P|_U$ times
pullbacks of its restrictions at the fixed torsion or zero sections.
Those latter lines are torsion or trivial. Since $\omega^{12}$
is trivial, $c_1(i_j^*L)=0$ rationally. The projection formula
applied to (4.4) proves (5.3), before any attempted proper push
from the punctured W. No such push is silently assumed.

For the analytic projection, use the canonical GLOBAL current
difference on a compact fiber $A_s$; base change to that fiber is
allowed by the source theorem. The curvature
$\lambda=c_1(\overline L)|_{A_s}$ is translation invariant and closed.
Consequently, directly,
$$\int_{A_s}(T_{-a}^*\mathfrak g_A-\mathfrak g_A)\wedge\lambda
   =\int_{A_s}\mathfrak g_A\wedge(T_a^*\lambda-\lambda)=0.$$
This integral is independent of the global current representative
modulo $\operatorname{im}\partial+\operatorname{im}\bar\partial$
by Stokes on the compact fiber. It does not extend an unspecified
equality of current classes from W across its deleted locus.

The pushed-unit calculation gives a compatible representative.
In relative dimension one, (5.2) fixes the unit regulator as
$$r_\sigma=-\tfrac12(T_{-\sigma}^*\mathfrak g_{\mathscr E}
                                      -\mathfrak g_{\mathscr E}).$$
On an $i_j$-fiber the curvature of $\overline L$ is the invariant
principal volume form $\mu$ of mass one. Translation invariance
and change of variable on that compact elliptic fiber give
$$\int_{\mathscr E_s}r_\sigma\,\mu=0.$$
The logarithmic singularities are integrable; removed-circle
limits contribute zero. No new constant is chosen to force
the average. The other terms have the same calculation.
Integrating these representatives also gives zero. Horizontal
curvature components cannot contribute to the degree-zero
fiber integral. This analytic projection
remains distinct from an unconstructed proper motivic push.
$\square$

Thus two natural scalar projections of an actual nonzero higher
polylogarithm class have been computed, and both yield zero.
Neither is a realization of the nonzero $\mathcal M$ or (1.1).
A refinement keeping other supports, noncuspidal coefficients,
or another secondary trivialization needs an additional comparison.

## 6. Remaining comparison after these constructions

The genus-two arithmetic projection gives (3.2), with exact residual
(3.4). The larger space supplies a NONZERO rational higher Chow
cycle and its canonical analytic torsion regulator; its torsion
and polarization scalar projections give zero. These calculations
use actual spaces, cycles, projections and regulator maps.
They do not repeat the already excluded ordinary triple-divisor
operation or introduce arbitrary real metrics.

There is also a genuine boundary premise: at the compactified cusps
the universal elliptic curve is generalized, not an abelian scheme.
Kings–Rössler applies on S. An extension over those degenerations
requires its own logarithmic complex and boundary cycle. It does
not follow from applying the abelian-scheme theorem across a cusp.
The genus-two source has its own explicit terms (2.2)–(2.3);
they are not the missing extension of (4.4).

**[GAP HAT-389]** Construct another secondary arithmetic cycle or
coefficient projection whose regulator equals the retained response,
with a rational map to $D_{\rm pt}\otimes B_2\otimes\mathbb Q(1)^{-2}$.
The original f-weighted comparison remains necessary; the
coordinator's separate adjoint-theta work is not assumed here.
The exact $6N(N-1)n_E$ coefficient and h-constants remain those
of §1. Rationality, integrality and full BSD remain unproved.

All new deductions passed the linked independent review. The rational
spectral-to-height comparison in HAT-389 remains unconstructed.
No shared synthesis, new agent or old numerical certificate was used
as a substitute for that comparison.
