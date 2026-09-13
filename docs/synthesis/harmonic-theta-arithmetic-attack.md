# Harmonic theta insertion and its arithmetic comparison

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
The bounded construction and all `[NEW]` deductions passed
[independent review](review-harmonic-theta-arithmetic.md).
Restart: [checkpoint](harmonic-theta-arithmetic-checkpoint.md).
The objective remains full BSD over Q.

This note tests the full harmonic-polynomial theta insertion arising from
the reviewed integrated spectral class. The rational noncentral K2 line
is an input, not a construction to repeat. The required arithmetic map
to the actual period-height determinant remains the target.

## 1. Exact harmonic insertion, with the original normalization

All notation and the joint endpoint estimates are those of the reviewed
[integrated construction](integrated-spectral-comparison-attack.md).
In particular $N=389$, $v_\eta=N^{-6}\Delta(z)/\Delta(Nz)$,
$l=\log|v_\eta|$, $g=(2\pi i)^{-1}d\log v_\eta/dz$,
$F=y^2f\bar g$ and $d\mu=dx\,dy/y^2$. Write
$$\Lambda_z=\mathbb Zz+\mathbb Z,\quad
\Lambda'_z=\mathbb Zz+N^{-1}\mathbb Z,\quad Q_z(w)=|w|^2/y.$$
On the second lattice this is the TRANSPORTED SOURCE Hodge norm,
1/N times the target's intrinsic principal normalized norm. Set
$$\Theta=\sum_{w\in\Lambda_z}e^{-\pi uQ_z(w)},\quad
\Theta'=\sum_{w\in\Lambda'_z}e^{-\pi uQ_z(w)},\quad H_N=\Theta'-\Theta,$$
$$S_N(z,u)=\sum_{w\in\Lambda'_z}w^2e^{-\pi uQ_z(w)}
              -\sum_{w\in\Lambda_z}w^2e^{-\pi uQ_z(w)}. \tag{1.1}$$
These are complete lattice sums; the zero vectors contribute zero to S.
The polynomial $w^2$ is harmonic in the two real coordinates of w.
It transforms with factor $(cz+d)^{-2}$, so $f(z)S_N(z,u)$ is a scalar
on the modular curve. This is not the rank-three quadratic lattice of
the Kudla–Millson kernel introduced later.

Let $\alpha=\pi^*\omega=c_\pi2\pi ifdz$ and
$\eta=-i\,l\alpha/(4\pi^2c_\pi)$, so $d\eta=Fd\mu$, including
the proved absence of cusp atoms. The full target is
$$\mathcal M=-\frac{3N(N-1)}{2\pi^3}\ell L(E,2),\qquad
\ell=L''(E,1)/2=4\pi(J''(0)-\mathcal C_E).$$

**[NEW] Proposition 1.1.** With the complex orientation on Y followed
by increasing u, one has the absolutely convergent identities
$$\boxed{\mathcal M=
 \frac{i}{16\pi^2c_\pi}\int_0^\infty\!\int_Y
    (\log u)^2l\,d_zH_N\wedge\alpha\,du
 =\frac18\int_0^\infty\!\int_Y
    u(\log u)^2l f(z)S_N(z,u)d\mu\,du.} \tag{1.2}$$

*Proof.* Start with the actual relative three-form
$\frac14(\log u)^2[H_N-(N-1)\chi(u)/u]Fd\mu\wedge du$
from the integrated proof. For fixed truncated cusp/heat intervals,
Stokes in z gives
$$\int H_N\,d\eta=-\int d_zH_N\wedge\eta$$
up to its oriented cusp boundary integral. The cutoff term is
independent of z. Its integrated contribution is zero by $\int F=0$,
and its z-derivative is zero. Thus the small-heat pole has been
retained and removed in exactly the proved way, not discarded.

In a cusp coordinate, l=O(y), $\alpha$ decays exponentially, and
all theta derivatives have Gaussian bounds with polynomial factors.
At the two simultaneous heat/cusp ends these are, after Poisson
subtraction, bounded by polynomials times
$e^{-c_1y-c_2\sqrt u}$ and $e^{-c_1y-c_2/\sqrt u}$ respectively.
They are the derivative bounds proved in the integrated Lemma 3.1.
Consequently the cusp boundary integrals tend to zero, and all
integrals of the z-derivatives converge absolutely with $(\log u)^2$.
Equivalently, pull back to the fine cover and apply Stokes to the
smooth relative forms flat along the Borel–Serre/heat boundary.
No integration by parts in u is used, hence there is no unaccounted
heat endpoint term. The downstairs integral retains the covering
factor $1/194$ if expressed on that integral relative chain.

Substitution of $\eta$ proves the first equality of (1.2), including
its sign. For $w=mz+n$ or $mz+n/N$, direct differentiation gives
$$\bar\partial Q_z(w)=-\frac{iw^2}{2y^2}d\bar z,\qquad
\bar\partial H_N=\frac{i\pi u}{2y^2}S_Nd\bar z.$$
The (1,0) part of $d_zH_N$ wedges to zero with $\alpha$. Using
$d\bar z\wedge dz=2i\,dx\wedge dy$, one obtains
$$d_zH_N\wedge\alpha=-2i\pi^2c_\pi u f S_Nd\mu.$$
This proves the factor $1/8$ in the second equality. $\square$

## 2. The moment that an arithmetic source must supply

For the level-one completed series $E^*(z,s)=\xi(2s)E(z,s)$ put
$$J_N(z,s)=N^sE^*(Nz,s)-E^*(z,s)
          =\xi(2s)(N^{2s}-1)E_\infty(z,s).$$
Thus the fully completed family is $\Gamma(s)J_N(z,s)$. Write
$$J_N(z,1+t)=\frac{R_N}{t}+j_0(z)+tj_1(z)+t^2j_2(z)+\cdots,
\qquad R_N=(N-1)/2. \tag{2.1}$$
The reviewed lower cancellations imply
$\int F=\int Fj_0=\int Fj_1=0$ and
$\int Fj_2=\mathcal M$. Multiplication by $\Gamma(1+t)$ changes
the unpaired second coefficient by its exact lower coefficients,
including the cubic gamma coefficient times $R_N$; each pairs to
zero. They will also be retained in the arithmetic theta test below.

Define the entire-in-s harmonic Mellin family, for each fixed z,
$$\mathcal S_N(z,s)=\int_0^\infty u^s S_N(z,u)du.$$
The derivative of the small-u leading term is zero, so Gaussian
Poisson bounds at both ends justify this integral for all s. For
$\Re s>1$ direct Mellin integration also gives
$$\mathcal S_N(z,s)=\frac{\Gamma(s+1)y^{s+1}}{\pi^{s+1}}
 \left(\sum_{w\in\Lambda'_z\setminus0}\frac{w^2}{|w|^{2s+2}}
       -\sum_{w\in\Lambda_z\setminus0}\frac{w^2}{|w|^{2s+2}}\right).
\tag{2.2}$$
At other s the lattice expression means that continuation, not an
unjustified rearrangement of a conditionally convergent series.
Differentiating the exact scalar Mellin formula gives
$$\bar\partial J_N(z,s)=\frac{i\pi}{4y^2}\mathcal S_N(z,s)d\bar z.
\tag{2.3}$$
In particular the insertion in (1.2) is exactly
$\partial_s^2\mathcal S_N(z,s)|_{s=1}$, not another integer-weight
Eisenstein–Kronecker coefficient. In the convergent domain its derivative
contains the explicit logarithms
$\log(y/\pi)+\psi(s+1)-2\log|w|$ and their square, together with
$\psi'(s+1)$. This specifies the required radial moment.
For comparison, the undifferentiated moment is exactly
$$\mathcal S_N(z,1)=\frac{y^2}{3}
       \bigl(N^2\overline{E_2(Nz)}-\overline{E_2(z)}\bigr)
                   -\frac{(N-1)y}{\pi}. \tag{2.4}$$
Indeed the Kronecker finite part of $E^*(z,s)$ displayed in §3 has
$\bar\partial$-derivative $i\pi\bar E_2/12-i/(4y)$; substitute it
in (2.3). Thus the full base moment has an explicit Hodge-curvature
term in addition to the finite torsion component. It is retained below.

## 3. A finite cyclic-torsion construction, and its exact residual

Let C be the universal cyclic subgroup of order N on the source
elliptic curve, analytically represented by a/N for a modulo N.
It is defined over the modular curve even when its points are not
individually rational. Pass to a fine cover and its algebraic Hodge-frame
$\mathbb G_m$-torsor, so the universal invariant differential is actually
trivialized. On that frame use
the short Weierstrass coordinate x with $x(w)=\wp(w;\Lambda_z)$.
Since N is odd,
$$\Phi_C(w)=\prod_{a\in(C\setminus0)/\{\pm1\}}
                        (x(w)-x(a)) \tag{3.1}$$
is an actual rational function on the pulled-back elliptic family. Its
divisor is $[C]-N[0]$. Under a frame change $\omega\mapsto\lambda\omega$,
the function scales by $\lambda^{-(N-1)}$; its homogeneous Hodge
weight is N-1. These changes scale it by a base unit,
and its logarithmic differential along the elliptic fiber is
intrinsic. The Kummer class asserted here lives on that frame-torsor
family with this divisor removed, in motivic degree one and Tate twist
one. It is not silently descended as a scalar unit on the modular
curve. Downstairs it is a section with the stated Hodge weight; choosing
a meromorphic frame downstairs would introduce its base divisor and
would require retaining that additional boundary. This construction
does not assign a motive to the spectral parameter.

Expanding $\wp(w)=w^{-2}+O(w^2)$ shows
$$d\log\Phi_C=-(N-1)\frac{dw}{w}
 -\left(\sum_{a\in C\setminus0}\wp(a)\right)w\,dw+O(w^3)dw.
\tag{3.2}$$
The finite trace in this jet is a section of the square of the Hodge
line, independent of a choice of short equation after retaining its
differential frame.

Here is the exact full heat family corresponding to that DEGREE-ZERO
isogeny correction:
$$H_C=(\Theta'-1)-N(\Theta-1),\qquad
S_C=S_N-(N-1)\sum_{w\in\Lambda_z}w^2e^{-\pi uQ_z(w)},$$
$$J_C(z,s)=\frac12\int_0^\infty u^{s-1}H_C(z,u)du
          =N^sE^*(Nz,s)-NE^*(z,s). \tag{3.3}$$
The integral identity first holds in $\Re s>1$; in fact H_C has
constant small-u limit N-1 and large-u limit zero. Its pole at s=1
has canceled because the torsion divisor has degree zero.

**[NEW] Proposition 3.1.** The finite part and the base harmonic moment
of (3.3) are
$$J_C(z,1)=\frac N{12}\log|v_\eta(z)|+\frac N2\log N,$$
$$\int_0^\infty u S_C(z,u)du=-\frac{Ny^2}{3}\overline{g(z)},
\qquad
\sum_{a\in C\setminus0}\wp(a)=-\frac{N\pi^2}{3}g(z). \tag{3.4}$$
For the specified F, its paired family satisfies
$$\int_YFJ_C(z,s)d\mu=\frac12(N^s-N)M_T(s),\qquad
M_T(s)=-\frac{24}{\sqrt N}\Lambda(E,s)\Lambda(E,s+1). \tag{3.5}$$
It has order at least THREE at s=1. In particular its second paired
jet, also after multiplication by $\Gamma(s)$, is zero. The entire
target remains in the exact residual
$$J_N-J_C=(N-1)E^*(z,s),\qquad
\mathcal M=(N-1)[t^2]\int_YFE^*(z,1+t)d\mu. \tag{3.6}$$

*Proof.* The level-one Kronecker finite part in this normalization is
$$E^*(z,1+t)=\frac1{2t}+\kappa-\frac12\log y-2\log|\eta(z)|+O(t),
\quad\kappa=\frac{\gamma-\log(4\pi)}2.$$
Taking the difference in (3.3), including the derivative of $N^{1+t}$
times $1/(2t)$, gives $2N\log|\eta(z)/\eta(Nz)|$, exactly the first
formula (3.4). The $N\log N/2$ term retains the declared normalization
of $v_\eta$. The differentiated Mellin identity (2.3), now for $J_C$,
and $\bar\partial\log|v_\eta|=-\pi i\bar g\,d\bar z$ give the
second formula.

One can see the finite algebraic jet without a limiting summation
convention: the normally convergent differences defining $\wp(a)$
give the difference between the two weight-two lattice sums,
$$G_2^*(\Lambda'_z)-NG_2^*(\Lambda_z)
       =\sum_{a\in C\setminus0}\wp(a).$$
Here $G_2^*(\Lambda_z)=\pi^2E_2(z)/3-\pi/y$ is the heat-regularized
sum, and scaling $\Lambda'_z=N^{-1}\Lambda_{Nz}$ multiplies it by
$N^2$. The area terms cancel in this degree-zero difference, yielding
the last formula (3.4). Equivalently, it follows by Mellin integration
of the second formula. In the Tate frame $2\pi i\,dw$, the trace
coefficient is $Ng/12$, not the unscaled $-N\pi^2g/3$.

Finally Fricke invariance gives
$\int F(\Theta(Nz,u)-1)=T_F(u)$. Therefore
$\int FH_C=T_F(u/N)-NT_F(u)$, proving (3.5). The factor $N^s-N$
has a simple zero at one, while $M_T$ has order two. This proves the
vanishing and (3.6). All steps use the full heat families, not only
their base coefficient. $\square$

Thus the natural finite torsion/Kummer component has actually been
constructed and tested. Extending that component with its own full
heat family does not recover the second jet. The residual is the
explicit source-lattice term (3.6), with its nonzero mass, not a
discarded finite-fiber or cusp correction.

## 4. The actual elliptic-polylogarithm component

The primary inputs here are Sprang,
[*The algebraic de Rham realization of the elliptic polylogarithm via
the Poincaré bundle*, 1802.04996v2](https://arxiv.org/pdf/1802.04996v2),
Theorems 5.8 and 6.1, and
[*Eisenstein–Kronecker series via the Poincaré bundle*, 1801.05677v3](https://arxiv.org/pdf/1801.05677v3),
Theorem 4.2. They construct actual logarithm sheaves from finite
infinitesimal neighborhoods of the Poincaré bundle and specialize their
polylogarithm classes at nonzero torsion sections. In degree k the
torsion specialization lies in
$H^1_{\rm dR}(Y,\operatorname{Sym}^kH^1_{\rm dR})$ and is represented
by an Eisenstein form of weight k+2. The Hodge interpretation in the
second source is at specified integer indices, not a spectral derivative.

We apply the degree-zero, weight-two part on a full-level fine cover.
Take auxiliary D=5, coprime to 6N, and sum the N-torsion sections
$s_a=a/N$, $1\le a<N$. All are disjoint from the removed D-torsion.
The auxiliary dual torsion sum is over ALL nonzero D-torsion, so the
nonzero, coprime torsion premises in Theorem 4.2 hold before taking
that sum. The resulting finite sum is invariant under the cyclic
subgroup's changes of generator and under coefficient Galois action.
Transfer from a full-level cover followed by division by its degree
gives a rational class downstairs. This is rational descent; it does
not assert integral primitivity.

Here is a direct normalization check of the component this operation
gives. In the source's elliptic differential frame dw put
$$F^{(2)}_{(a,b)}(z)=-\sum'_{m,n}
             \frac{\zeta_N^{mb-na}}{(mz+n)^2},$$
with the usual Eisenstein continuation at weight two. Finite Fourier
orthogonality, or its absolutely convergent regularization first, gives
$$\sum_{a=1}^{N-1}F^{(2)}_{(0,a)}
 =G_2^*(z)-NG_2^*(Nz)=\frac{\pi^2}{3}g(z). \tag{4.1}$$
The degree-zero correction from the complete D-torsion distribution
is
$$D^2F^{(w)}_{(a,b)}-D^{2-w}F^{(w)}_{(Da,Db)}. \tag{4.2}$$
To check its exponent, separate the full lattice sum into vectors
divisible by D and those not both divisible by D. The divisible
vectors contribute $D^{-w}$ and change the character to (Da,Db);
the prefactor is $D^2$. Thus their coefficient is exactly $D^{2-w}$.
At w=2 the D-map permutes the nonzero cyclic N-torsion labels, so
the trace in (4.1) is multiplied by $D^2-1=24$. Its representative is
therefore
$$8\pi^2g(z)\,dw^2=-2g(z)(2\pi i\,dw)^2. \tag{4.3}$$
With the declared Tate Kodaira–Spencer convention
$\operatorname{KS}((2\pi i\,dw)^2)=dq/q$, the resulting de Rham
class is exactly $-2[d\log v_\eta]$. This computes a genuine
arithmetic component of the proposed construction, of cohomological
degree one and trivial symmetric-power coefficient. In motivic
normalization it retains the Kummer Tate twist $\mathbb Q(1)$;
its de Rham representative is $d\log$ of the unit. It agrees with the actual
weight-two Kummer component in §3, after the displayed finite factors.

**Source-display precision.** In 1802.04996v2, printed p.31 defines
the D-variant with $D^{1-w}$, whereas the final reindexing in its own
proof on p.35 gives $D^{2-w}$. Both pages were rendered and inspected.
Formula (4.2) uses the directly proved reindexing, not the inconsistent
shorthand display. The cyclic weight-two trace can also be computed
entirely from the actual Kummer unit $v_\eta$ and (3.4), so none of
the spectral conclusions depends on resolving a transcendental
normalization by fiat. This is a local source-display discrepancy,
not a counterexample to BSD or to the existence of the polylogarithm.

The de Rham theorem determines a differential class, not the real
constant in a logarithm of a unit. That constant has already been
fixed here by $v_\eta=N^{-6}\Delta/\Delta_N$ and the explicit
$N\log N/2$ term in (3.4). Any remaining constant under a different
polylogarithm rigidification pairs with $\int F=0$; it cannot produce
the nonzero second moment.

Passing from k=0 to k=1 or 2 in the source theorem gives coefficient
systems $\operatorname{Sym}^1H^1$ or $\operatorname{Sym}^2H^1$ and
weights three or four. It is not an operation differentiating s twice
while keeping (2.2) at the same weight-two component. The concrete
same-kernel continuation that does keep that component is (3.3), and
its entire second paired jet is zero by (3.5). Thus the tested finite
torsion construction leaves exactly the residual (3.6). This does not
exclude another extension involving the pro-system or a different
integrated arithmetic construction.

## 5. The arithmetic theta theorem applied to the FULL spectral source

There is a second construction to test that really accepts the entire
unpaired spectral family. Use precisely Du–Yang's squarefree-level
lattice, effective stack multiplicities and normalized Petersson metric
from [1702.07917v2](https://arxiv.org/pdf/1702.07917v2), Theorems
1.3–1.6 and Proposition 2.2. Their lattice is the trace-zero rank-three
quadratic space of signature (1,2); their kernel
$\Theta_L(\tau,z)$ is a (1,1)-form in z and has modular weight 3/2
in a DIFFERENT upper-half-plane variable $\tau$. Define
$$I_L(\tau,h)=\int_Y h(z)\Theta_L(\tau,z).$$
Their cusp bound is Gaussian in the height at every cusp, so it
applies to every fixed Laurent coefficient $j_i$, with its prescribed
polynomial/logarithmic cusp growth.

For prime N their normalized scalar input is exactly
$$N^{2s}\pi^{-s}\Gamma(s)\zeta^{(N)}(2s)E_\infty(z,s)
       =J_N(z,s).$$
Thus their Theorem 1.4, with no normalization adjustment, says
$$\boxed{I_L(\tau,J_N(\cdot,s))=\xi(s)\mathcal E_L(\tau,s).}
\tag{5.1}$$
The Fricke-transformed input has the same lift. This is an actual
theta comparison for the whole family; neither cusp is omitted.

Write $\mathcal E^{(r)}=\partial_s^r\mathcal E_L(\tau,s)|_{s=1}$ and
$$\xi(1+t)=t^{-1}+\kappa+a_1t+a_2t^2+O(t^3). \tag{5.2}$$
The constants $a_1,a_2$ are the derivatives of the fixed function
$\xi(1+t)-t^{-1}$ at zero, with coefficient factorials. They are
not arbitrary metric constants. Then exact coefficient extraction gives
$$I_L(\tau,j_0)=\mathcal E^{(1)}+\kappa\mathcal E^{(0)},$$
$$\boxed{I_L(\tau,j_2)=\frac{\mathcal E^{(3)}}6
  +\frac\kappa2\mathcal E^{(2)}+a_1\mathcal E^{(1)}+a_2\mathcal E^{(0)}.}
\tag{5.3}$$
The residue check is $R_NI_L(\tau,1)=\mathcal E^{(0)}$, which is
their Theorem 1.6. All interchange of Laurent coefficients and the
integral follows by subtracting the explicit pole and using their
Gaussian cusp estimate uniformly on a compact s-neighborhood.

For the fully completed source do NOT delete its gamma-pole cross term.
Define, exactly,
$$\Gamma(1+t)\xi(1+t)=t^{-1}+h_0+h_1t+h_2t^2+O(t^3),
\qquad h_0=\kappa-\gamma=-\frac{\gamma+\log(4\pi)}2.$$
If $\widetilde j_2=[t^2]\Gamma(1+t)J_N(z,1+t)$, then
$$\boxed{I_L(\tau,\widetilde j_2)=\frac{\mathcal E^{(3)}}6
  +\frac{h_0}2\mathcal E^{(2)}+h_1\mathcal E^{(1)}+h_2\mathcal E^{(0)}.}
\tag{5.4}$$
Equations (5.2)–(5.4) retain every scattering/completion constant by
specifying its exact generating function, including the cubic
coefficient of $\Gamma(1+t)$ times $R_N$. Although
$\int F\widetilde j_2=\int Fj_2=\mathcal M$, the two UNPAIRED
theta lifts are not identified by dropping those lower terms.

### The actual lower arithmetic component, with its vertical correction

The constant term itself has a genuine arithmetic class. Set
$$A=\Delta(Nz)^N/\Delta(z),\qquad k=12(N-1).$$
The exact finite divisor, already verified from Du–Yang Lemma 6.4, is
$$\operatorname{div}A=(N^2-1)\mathcal P_\infty-12N\mathcal X_N^0.
\tag{5.5}$$
Let $\|A\|_0=|A|y^{k/2}$, and let $\widehat\omega_0$ be the
weight-one Hodge line with that standard Petersson norm. The
Kronecker limit formula gives
$$j_0=(N-1)\kappa-\frac1{12}\log\|A\|_0.$$
Therefore the specific arithmetic divisor
$$\widehat D_0=
 \left(\frac{N^2-1}{24}\mathcal P_\infty
                   -\frac N2\mathcal X_N^0,\ j_0\right)
 =\frac{N-1}{2}\widehat\omega_0+a((N-1)\kappa) \tag{5.6}$$
is defined in the source's arithmetic Chow group with cusp singularities.
The constant is forced by the fixed Laurent subtraction. This is a
canonical metric calculation, not an arbitrary choice to fit $\mathcal M$.

Use $C=(\log4\pi+\gamma)/2$ and $c=4\pi e^{-C}$ for the
Du–Yang norm, so $\log c=-\kappa$ and
$\widehat\omega_0=\widehat\omega_{\rm DY}+a(\log c)$.
Their exact intersections are
$$\begin{aligned}
\langle\widehat\phi,\widehat\omega_{\rm DY}\rangle
 &=\frac1{N-1}\left(\mathcal E^{(1)}
              -\frac N{N-1}\log N\,\mathcal E^{(0)}\right),\\
\langle\widehat\phi,a(1)\rangle&=\frac{\mathcal E^{(0)}}{N-1},\qquad
\langle\widehat\phi,\mathcal X_N^0\rangle
                  =\frac{\log N}{N-1}\mathcal E^{(0)}.
\end{aligned} \tag{5.7}$$
Substitution proves the concrete arithmetic comparison
$$\boxed{I_L(\tau,j_0)=
 2\left\langle\widehat\phi(\tau),
              \widehat D_0+\frac N2\mathcal X_N^0\right\rangle.}
\tag{5.8}$$
The added vertical class in (5.8) is necessary: omitting it loses
$N\log N\,\mathcal E^{(0)}/(N-1)$. It changes the finite divisor
to $(N^2-1)\mathcal P_\infty/24$ while retaining its forced Green
function $j_0$. Thus this test has been pushed through an actual
arithmetic intersection, with all finite and archimedean constants.

### The higher response is a genuine additional term in this test

The specified arithmetic Hodge, vertical and constant classes in (5.7)
give only the span of $\mathcal E^{(0)},\mathcal E^{(1)}$. The
additional terms in (5.3) or (5.4) cannot be removed by a fixed linear
combination of those classes. This assertion can be proved without an
uncertain incoming-term multiplicity convention.

**[NEW] Proposition 5.1 (exact differential obstruction for this
arithmetic span).** Let $\Delta_{3/2}$ be the weight-3/2 Laplacian
$-v^2(\partial_u^2+\partial_v^2)+(3i/2)v(\partial_u+i\partial_v)$,
where here $\tau=u+iv$. For either response $\mathcal Q$ in (5.3)
or (5.4),
$$\boxed{\Delta_{3/2}^3\mathcal Q=-\frac1{64}\mathcal E^{(0)}\ne0.}
\tag{5.9}$$
On the span produced by (5.7), $\Delta_{3/2}^2=0$.

*Proof.* The incoming power in the source's Eisenstein definition is
$v^{(s-1)/2}$. Direct application of the displayed Laplacian and
commutation with the weight-3/2 slash action give
$$\Delta_{3/2}\mathcal E_L(\tau,s)
          =-\frac{s(s-1)}4\mathcal E_L(\tau,s).$$
The normalization is independent of $\tau$ and does not change this
identity. Differentiating it shows that three Laplacians kill
$\mathcal E^{(r)}$ for $r\le2$, whereas
$\Delta_{3/2}^3\mathcal E^{(3)}=6(-1/4)^3\mathcal E^{(0)}$.
This proves (5.9); two Laplacians kill the lower span. The Eisenstein
value $\mathcal E^{(0)}$ is nonzero, as follows from its defining
nonzero incoming term (or the source's degree formula).
No spectral derivative is claimed algebraic from this calculation.
$\square$

The arithmetic surface has dimension two, so an ordinary product of
three codimension-one arithmetic classes on that SAME surface lies
in the zero codimension-three group in the rational/real arithmetic
Chow ring used here. This does not assert absence of higher integral
stabilizer torsion on the modular stack. Merely appending a second Hodge
intersection to (5.8) does not construct (5.4). An intersection on a
higher-dimensional fiber product would require its own cycle, coefficient
projection and comparison theorem; it is not the theorem applied here.
This is a limitation of the tested classes and operation, not an
exclusion of all arithmetic theta constructions.

## 6. The precise rational comparison still required

Two actual arithmetic inputs have now been tested: the finite
cyclic-torsion/Poincaré component and the canonical arithmetic
Kronecker divisor. The first has the coherent continuation (3.3),
whose second paired jet is zero. The second has the genuine
intersection (5.8), but the full spectral response retains (5.4),
with the nonzero differential value (5.9).

The theta variable $\tau$ does not replace the elliptic newform f
in the original integral. Formula (5.4) computes the image of its
spectral factor under a second theta lift. The desired number is
still $\int_YFj_2\,d\mu$. No inverse/adjoint theta correspondence
identifying this f-weighted pairing with the determinant of the
specified noncuspidal point heights has been constructed here.
Even a realization of the right side of (5.4) by itself would have
to retain that additional comparison; it would not automatically
prove the scalar rationality.

The target remains the actual rational line
$$D_{\rm pt}\otimes B_2\otimes\mathbb Q(1)^{-2},$$
with frame evaluation $-\Omega_E\operatorname{Reg}_E L(E,2)/(4\pi^3)$
and exact spectral coefficient $6N(N-1)n_E$. The line
$B_2=\mathbb Q\beta_2$, with regulator $L(E,2)/\pi$, is an input
from the reviewed integrated construction. The coordinator's completed,
[independently reviewed arithmetic extension](k2-arithmetic-divisor-attack.md)
gives this actual class a unique rational lift to
$\operatorname{CH}^2(\mathcal E,2)$ on the regular arithmetic model,
with a sufficient integral multiple. No part of that construction is
rerun here. None of these lines is
declared integrally primitive without a proof of its lattice index.

**[GAP HT-389]** Construct an arithmetic extension or cycle realizing
the retained second radial moment, with the full theta/f pairing and
a proved rational map into this exact line. It must supply the
source-lattice term in (3.6), or the equivalent higher response
(5.4) together with its f-weighted comparison. The computations
above do not establish rationality or integrality of $n_E$, and
leave full BSD over Q open.

## 7. Verification and restart record

Primary versions inspected: Sprang 1802.04996v2 (19 Dec 2019),
Theorems 5.8/6.1, with pp.31 and35 rendered to check the conflicting
D-variant exponent; Sprang 1801.05677v3 Theorem 4.2; Du–Yang
1702.07917v2 (4 Feb 2018), Theorems 1.3–1.6, Proposition 2.2, definition (1.6)
and the proof of (2.12). The finite divisor and stack conventions
are also linked to their previous independent verification.

Temporary source copies are `/tmp/harmonic-sprang-polylog.pdf` and
`/tmp/harmonic-du-yang.pdf`; the authoritative versions are linked
above. No old certificate, numeric prime scan or height calculation
was rerun. All new deductions passed the linked independent review;
the arithmetic spectral-to-point-height map in HT-389 remains missing.
