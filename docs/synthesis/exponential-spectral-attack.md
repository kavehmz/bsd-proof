# An exponential de Rham realization of the spectral Fourier kernel

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
The `[NEW]` constructions passed
[independent review](review-exponential-spectral.md). The goal remains
full BSD over Q; no classical BSD determinant comparison is proved.

## 1. Positive construction and boundaries of the result

For an algebraic parameter $Z\ne0$ this note constructs a rational
rank-three irregular connection, a relative de Rham group of rational
rank six, rational Betti frames and explicit integration cycles. For
$Z>0$ its positive cycle produces, modulo $t^3$,
$$I(t,Z)=\int_0^\infty e^{-v}v^t(1+v/Z)^t\,dv.$$
The normalized kernel $I(t,Z)/\Gamma(1+t)$ is obtained by finite
sums and tensor products of period objects, because $\Gamma(1)=1$.
No arbitrary nonrational scalar period is inverted.

An additional completed Eisenstein normalization removes both the
completed-zeta derivative constants and this gamma normalization from
every individual nonzero Fourier kernel. Its paired second jet has
exact mass
$$-\frac{3N(N-1)}{2\pi^3}\,\ell_E L(f,2),\qquad N=389. \tag{1.1}$$
The algebraic parameter $Z$, the later substitution $Z=4\pi ny$, the
infinite Fourier sum and a classical rational BSD determinant are
different steps. Only the first and the exact analytic normalization
are constructed here.

## 2. A rational irregular connection with a relative logarithmic end

Put $F=\mathbb Q(Z)$, $A=F[t]/t^3$ and
$$q_*(v,Z)=\frac{v(v+Z)}Z.$$
On $v\ne0,-Z$, $Z\ne0$, use the rank-three bundle represented as
the rank-one $A$-module with connection
$$\nabla=d-dv+t\,d\log q_* . \tag{2.1}$$
This is a matrix connection over a reduced rational base: the notation
$t^3=0$ packages a nilpotent rank-three coefficient action. Its one-form
is closed and its coefficient matrices commute, so the total connection
in $(v,Z)$ is integrable. It is logarithmic at $v=0,-Z$ and irregular
at infinity: in $w=1/v$ the exponential part has pole order two.

In the displayed de Rham frame the dual horizontal multiplier is
$$h(v,Z)=e^{-v}\exp(t\log q_*(v,Z)). \tag{2.2}$$
On the positive ray use the real logarithm. Since $q_*/v\to1$ at
zero, the positive tangent $\partial/\partial v$ fixes its logarithmic
normalization with no extra $\log Z$ constant at that endpoint.

The unipotent factor is the rank-three toric logarithm variation,
with the sign of the connection fixed by (2.1), and graded pieces
$\mathbb Q,\mathbb Q(1),\mathbb Q(2)$. It is obtained from the
second logarithm construction, with inversion of the torus coordinate
if using the opposite horizontal-section sign. The actual logarithm
motives and their realizations are in
[Huber–Kings, arXiv:1505.04574v1, Definition 4.3.1, Proposition 4.6.1
and Lemma 6.4.1](https://arxiv.org/pdf/1505.04574v1).
The exponential factor is what makes this new connection irregular.

**The endpoint at zero is relative, not rapid.** Set
$$R=A[v,(v+Z)^{-1}],\qquad
\mathcal C_Z=[\,vR\xrightarrow{\nabla_v}R\,dv\,]. \tag{2.3}$$
The source forces the primitive to vanish at zero. In the local
relative frame $e'=ve$, its residue at zero is $1+t$, and the
target is that frame times $dv/v$. The dual coefficient in this
frame is $v h(v,Z)$, which has moderate logarithmic behavior and
vanishes to order one times log powers; it is not rapidly decreasing
to every order. At infinity, along a closed subsector of $\Re v>0$,
the factor $e^{-v}$ gives rapid decay against every rational pole.

For $f\in vR$, integration of $h\nabla_v f=d(hf)$ over the positive
ray has zero endpoint terms: $hf=O(v\log^2v)$ at zero and decreases
exponentially at infinity. The forms in $Rdv$ are integrable there.
On a small circle about zero their integrals tend to zero as
$O(\epsilon\log^2\epsilon)$, including all nilpotent coefficients.
These estimates are the relative regularization used here.

Bloch–Esnault's [arXiv:math/0005137v1, Theorem 0.1 and Example 0.2(ii)](https://arxiv.org/pdf/math/0005137)
give the irregular integration pairing and the gamma contour. Their
ordinary rapid-decay homology allows no nonzero rapid section at a
regular singular point. Thus their absolute theorem alone would not
justify our open $0\to\infty$ chain. The relative complex, boundary
condition and pairing are instead constructed explicitly below.

**[NEW] Proposition 2.1 (finite de Rham frame).** The degree-zero
cohomology of (2.3) is zero and
$$H^1(\mathcal C_Z)=A[\omega_0]\oplus A[\omega_1],
\qquad \omega_0=dv,\quad\omega_1=\frac{dv}{v+Z}. \tag{2.4}$$

*Proof.* The rational primitives vanishing at zero are spanned over
$A$ by $v^m$ for $m\ge1$ and $v/(v+Z)^k$ for $k\ge1$.
For the latter primitive, the highest pole of its covariant derivative
at $-Z$ has coefficient $Z(k-t)$ and order $k+1$. This coefficient
is a unit in $A$. It reduces every pole of order at least two.
For $v^m$, the highest polynomial term in its derivative is $-v^m$;
the other terms have smaller polynomial degree and at most a simple
pole. This reduces every positive polynomial degree, leaving (2.4).

For uniqueness, a primitive with a nonzero highest pole would produce
that nonzero pole of order one higher, so cannot have image in the
span (2.4). A pole-free primitive is a polynomial vanishing at zero;
its nonzero highest degree similarly persists in the image. Thus no
nonzero primitive maps into that span. This also proves the kernel
is zero and gives a free $A$-basis, not only a dimension count after
specialization. $\square$

## 3. Rational Betti frames, explicit cycles and comparison

The de Rham nilpotent $t$ must not be identified unchanged with a
rational Betti monodromy coordinate. Let $\varepsilon_j$ denote
coefficient extraction at $t^j$. In the dual horizontal coefficient
space set
$$\lambda_j=(2\pi i)^{-j}\varepsilon_j,\qquad j=0,1,2. \tag{3.1}$$
The rational Betti space is their $\mathbb Q$-span. A positive loop
around either zero or $-Z$ changes $\log q_*$ by $2\pi i$, hence
acts by
$$M\lambda_j=\sum_{r=0}^j\frac{\lambda_{j-r}}{r!}. \tag{3.2}$$
This is a rational matrix. The lattice on
$\lambda_0,\lambda_1,2\lambda_2$ is stable integrally. Equivalently
the primal Betti frame has comparison vectors $(2\pi i)^j t^j$
and inverse monodromy. These are the actual Tate-period factors of
the three graded pieces; a free $A$-module de Rham description is
not by itself an identification of the two rational structures.

Take the real oriented blowup at $0,-Z,\infty$. At zero use the
entire logarithmic boundary circle relatively, with its nearby local
system, choosing its positive tangent to frame transport. At infinity
use the connected rapid-decay arc $\Re v>0$ relatively. At $-Z$
keep ordinary closed-path monodromy; do not allow a non-rapid open
endpoint there. This specifies the relative topological problem.

For this explicit cycle chart assume $Z>0$; the rational connection
itself is defined on $Z\ne0$, and other complex parameters use local
cycle charts and analytic continuation. Choose an interior basepoint
$b=1$, let $p_0$ be the positive path
from the zero tangent to $b$, $p_\infty$ the positive path from $b$
to infinity, and $\ell$ a positive loop about $-Z$, based at $b$,
with a connecting path avoiding zero. If $V_B$ is the space (3.1),
the relative graph chain complex is
$$V_B^3\longrightarrow V_B,\qquad
(a,b,c)\longmapsto a-b+(M-1)c. \tag{3.3}$$
The zero-boundary circle is removed relatively, and the infinity arc
is one contractible rapid end; this leaves exactly these two paths
and one nonrelative loop. Its kernel has the rational basis of cycles
$$\Gamma_j=(p_0+p_\infty)\lambda_j,\qquad
\Lambda_j=\ell\lambda_j-p_0((M-1)\lambda_j),
\qquad j=0,1,2. \tag{3.4}$$
The correction in $\Lambda_j$ is essential when $j>0$.

For a form $f(v,t)dv$, integrate the scalar
$e^{-v}\lambda_j(\exp(t\log q_*)f(v,t))dv$ along a loaded path.
Interior boundaries cancel according to (3.3). Exact forms have
zero periods by Stokes and the estimates in §2. Homotopies are
compatible with the pairing because the loaded one-form is closed
on the punctured curve, and the relative boundary integrals vanish.
Thus (3.4) gives actual rational Betti cycles for (2.3).

**[NEW] Proposition 3.1 (the explicit comparison is perfect).**
Integration between (2.4) and (3.4), after extension to $\mathbb C$,
is a nonsingular pairing of dimension six. The positive periods are
$$\langle\Gamma_j,\omega_0\rangle
  =\frac{I_j(Z)}{(2\pi i)^j},\qquad
I(t,Z)=I_0(Z)+tI_1(Z)+t^2I_2(Z). \tag{3.5}$$

*Proof.* The graph differential is surjective, and its kernel has
the six displayed basis vectors. The de Rham dimension is six by
Proposition 2.1. Filter by the nilpotent degree. If a form contains
$t^k$, its pairing with a cycle loaded by $\lambda_j$ is zero for
$j<k$. For $j=k$, its logarithmic factor is constant; the correction
in $\Lambda_j$ has smaller $j$ and also pairs to zero. The diagonal
two-by-two period block, using $\omega_0,\omega_1$ and
$\Gamma_j,\Lambda_j$, is
$$\frac1{(2\pi i)^j}
 \begin{pmatrix}1&e^Z E_1(Z)\\0&2\pi i e^Z\end{pmatrix}.$$
The loop entries follow from the ordinary residue at $v=-Z$.
Every diagonal block is nonsingular. The full block-triangular
comparison is therefore nonsingular, with determinant
$(2\pi i)^{-3}e^{3Z}$ for these rational Betti bases, up to the
fixed ordering sign. Finally the positive integrals are (3.5) by
coefficient extraction. $\square$

Tensoring the $j$th period in (3.5) with the ordinary Tate period
$(2\pi i)^j$ produces the unscaled $I_j$. This is an actual framed
period operation, not an assertion that the comparison factors are
rational numbers. The construction is valid as a rational family in
$Z$; for numerical exponential periods one may specialize to a
positive algebraic $Z$.

## 4. Its rational Gauss–Manin system is the Bessel system

The full connection (2.1) has $dZ$ coefficient
$t((v+Z)^{-1}-Z^{-1})$, which preserves the relative lattice at
zero. It therefore induces a rational connection on (2.4).

**[NEW] Proposition 4.1.** Let
$$J_t(Z)=\int_0^\infty\frac{e^{-v}q_*(v,Z)^t}{v+Z}\,dv.$$
The positive period vector satisfies, modulo $t^3$,
$$\frac{d}{dZ}\begin{pmatrix}I\\J_t\end{pmatrix}
 =\begin{pmatrix}-t/Z&t\\-1/Z&1+t/Z\end{pmatrix}
          \begin{pmatrix}I\\J_t\end{pmatrix}. \tag{4.1}$$
Consequently $I''-I'-t(t+1)I/Z^2=0$, without dividing by $t$.

*Proof.* Differentiating the first form through the full connection
gives $-t\omega_0/Z+t\omega_1$. For the second, reduce its double
pole using the exact relation from the primitive $v/(v+Z)$:
$$0=-[\omega_0]+(Z+2t)[\omega_1]
               +Z(1-t)\left[\frac{dv}{(v+Z)^2}\right].$$
This gives the second row of (4.1). Differentiating its first row
and substituting its second row gives the stated scalar equation;
the calculation multiplies by $t$ but never cancels it. Boundary
differentiation creates no term, since the tangent normalization
$q_*/v\to1$ is independent of $Z$ and the infinity end is rapid.
$\square$

This is a rational irregular Gauss–Manin object, not a return to the
excluded regular-singular modular-cusp expression class. Its other
period solution contains $e^Z$, and infinity in the $Z$-line is
irregular.

## 5. Gamma normalization by finite period operations

Use the analogous relative complex with $q_*=v$:
$$[\,vA_0[v]\xrightarrow{d-dv+t\,dv/v}A_0[v]dv\,],
\qquad A_0=\mathbb Q[t]/t^3.$$
The polynomial reduction in Proposition 2.1 shows that its degree-one
cohomology is free of rank one over $A_0$, on $dv$. Its three positive
cycles have the same Tate frames (3.1), with no $-Z$ loop. Their
periods give
$$G(t)=\int_0^\infty e^{-v}v^t dv
       =\Gamma(1+t)=1+g_1t+g_2t^2\pmod{t^3}. \tag{5.1}$$
In particular the constant period is exactly the rational number one.

Therefore
$$G(t)^{-1}=1-g_1t+(g_1^2-g_2)t^2,$$
and the normalized kernel has coefficients
$$\frac{I(t,Z)}{G(t)}=I_0+
 (I_1-g_1I_0)t+
 \bigl(I_2-g_1I_1+(g_1^2-g_2)I_0\bigr)t^2. \tag{5.2}$$
Every term is a rational linear combination of products of the actual
periods already constructed, after their explicit Tate adjustments.
Direct sums realize additions and subtractions; tensor products realize
products. Concretely their cycles are product cycles, their exponential
potential is a sum of the original potentials, and absolute convergence
permits Fubini. Thus (5.2) uses finite tensor/period operations. It
does not invert a conjecturally nonrational scalar period, or claim
to construct the full untruncated inverse gamma function in one finite
object.

The preceding [Bessel calculation](spectral-regular-singular-attack.md),
§3, identifies (5.2) with
$$\frac{K_{1/2+t}(Z/2)}{K_{1/2}(Z/2)}
 =1+t\,e^ZE_1(Z)+t^2\int_Z^\infty\frac{e^uE_1(u)}u\,du
 \pmod{t^3}. \tag{5.3}$$
This gives a positive rational irregular realization of the very kernel
whose inverse-height expansion was proved factorially divergent.

## 6. Completed Eisenstein jets and their unchanged paired mass

Return to $N=389$ and retain the previous $F=y^2f\bar g$, both cusp
scalings, all Laurent coefficients and the exact original identity
$$\int_Y FA_2d\mu=-\frac{9N}{\pi^4(N+1)}\ell_E L(f,2),
\qquad \int F=\int FA_0=\int FA_1=0. \tag{6.1}$$

**[NEW] Lemma 6.1 (a holomorphic completion retains every pole term).**
If $C(1+t)=c_0+c_1t+c_2t^2+c_3t^3+\cdots$, then the coefficient
of $t^2$ in $C(1+t)E_\infty(z,1+t)$ is
$$c_0A_2+c_1A_1+c_2A_0+c_3R,$$
where $R=3/[\pi(N+1)]$. Its pairing with $F$ is exactly $c_0$
times the pairing in (6.1).

*Proof.* Multiply the Laurent series, including $R/t$. The $c_3R$
term is necessary in the unpaired family. All but the first term
pair to zero by (6.1). $\square$

Put
$$C_0(s)=\xi(2s)(N^{2s}-1),\qquad
C_1(s)=\Gamma(s)\xi(2s)(N^{2s}-1),\qquad
\xi(u)=\pi^{-u/2}\Gamma(u/2)\zeta(u). \tag{6.2}$$
They are holomorphic and nonzero at one and have the same value
$\pi(N^2-1)/6$. The first removes the completed-zeta and level
derivative constants from a nonzero Fourier mode. Multiplying by the
additional $\Gamma(s)$ removes the normalization in (5.3) as well.
Indeed, at the infinity cusp the positive $n$th mode of
$\mathcal E=C_1(s)E_\infty(z,s)$ is exactly
$$q^n n^t\left(N1_{N\mid n}\sigma_{-1-2t}(n/N)
                  -\sigma_{-1-2t}(n)\right)I(t,4\pi ny),
\qquad t=s-1. \tag{6.3}$$
At cusp zero it is
$$q^n n^t\left(N^{1+t}\sigma_{-1-2t}(n)
                -N^{-t}1_{N\mid n}\sigma_{-1-2t}(n/N)\right)
                 I(t,4\pi ny). \tag{6.4}$$
These follow directly by multiplying the exact oldform Fourier factors.
For $n=1$ they are $-q I(t,4\pi y)$ and
$Nq e^{t\log N}I(t,4\pi y)$ respectively. The remaining finite
divisor sums have coefficients $d^{-1}e^{-2t\log d}$; their truncated
logarithms of positive rational numbers are ordinary Kummer periods.
No zeta derivative or gamma inverse remains in an individual mode of
(6.3)–(6.4).

The zero modes have not disappeared. In the same normalized coordinates
they are exactly
$$\begin{aligned}
\mathcal E_\infty^{(0)}(z,s)&=
 \Gamma(s)\xi(2s)(N^{2s}-1)y^s
       +\Gamma(s)\xi(2s-1)(N-1)y^{1-s},\\
\mathcal E_0^{(0)}(z,s)&=
 \Gamma(s)\xi(2s-1)(N^s-N^{1-s})y^{1-s}.
\end{aligned} \tag{6.5}$$
Their common residue is $(N-1)/2$. Their derivative constants and
the cubic completion term in Lemma 6.1 still belong to the unpaired
family; the rank-three Fourier construction alone does not give
their arithmetic realization.

For either completion in (6.2), Lemma 6.1 gives the exact paired
mass (1.1), since
$$\frac{\pi(N^2-1)}6\cdot
       \frac{-9N}{\pi^4(N+1)}
       =-\frac{3N(N-1)}{2\pi^3}.$$
For 389 the rational numerator is $226398$. The original Tamagawa,
period and nonzero eta-correction conventions remain inside the same
$\ell_E$ of (6.1). This calculation neither drops $L(f,2)$ nor
treats it as an integral unit.

## 7. Exact remaining arithmetic steps

The new kernel object is a rational algebraic family on the $Z$-line.
The substitution actually used in the modular Fourier series is
$$Z=4\pi ny=-2n\log|q|.$$
It is not an algebraic map from the modular curve to that parameter
line. A coefficient family may also be formed with independent algebraic
variables $q,Z$, but imposing this real logarithmic relation is an
additional comparison, not an algebraic pullback already supplied by
(2.1).

Even after that substitution, constructing each finite Fourier mode
does not construct the infinite modular Fourier sum as one finite
exponential motive or as an object with a common rational Betti frame.
Equations (6.3)–(6.5) are exact analytic identities and distinguish
the unresolved zero-mode constants. The vanishing pairings justify
their effect on the integrated second jet, not deletion of those
terms from a proposed arithmetic object.

Finally an exponential de Rham/Betti comparison object is not already
the classical rational period–height determinant line of BSD. An
arithmetic map connecting the completed integrated source to the actual
noncuspidal determinant, with its fixed finite corrections, degree and
real-period factors and the $L(f,2)$ regulator factor, remains required.
The construction here supplies a concrete irregular source for the
individual kernels and a normalization that preserves the exact mass.
It proves neither leading-term rationality, integrality, full Sha
finiteness nor full BSD.
