# Second character variation on the full modular curve

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
The `[NEW]` deductions below passed
[independent review](review-spectral-second-variation.md). The parent
objective remains full BSD over Q; no leading-term comparison is proved.

## 1. Objects and exact result

Use the effective modular orbifold $Y=\Gamma_0(389)\backslash\mathfrak H$
and its two normalized width-one cusps. All orbifold conventions are
those of [the reviewed Mellin construction](mellin-variation-attack.md).
In particular a torsion-free $\Gamma_1(389)$ cover has degree 194;
integrals downstairs equal $1/194$ times pulled-back integrals upstairs.
Put
$$V=\operatorname{vol}(Y)=\frac{\pi(389+1)}3=130\pi,
\qquad R=V^{-1},\qquad \Delta=-y^2(\partial_x^2+\partial_y^2).$$
Let $\pi:X_0(389)\to E$ be the degree-$d=40$ modular map, and
write the rectangular elliptic periods as $\omega_1>0$, $\omega_2=i b$
with $b>0$. The original character direction is
$$w=\Re(\pi^*\omega)/\omega_1,\qquad
k(\gamma)=\int_\gamma w\in\mathbb Z.$$
Its integral rank-three realization is multiplication by
$(1+T)^{k(\gamma)}$ on $\mathbb Z[T]/T^3$.

This note proves the actual second-character scattering formula
$$\boxed{\ddot\Phi_{ab}(s)=\frac{8\pi^2}{2s-1}
 \left(4\int_Y D_wE_a(s)\,\mathcal R(s)D_wE_b(s)d\mu
             -\int_Y |w|^2E_a(s)E_b(s)d\mu\right),} \tag{1.1}$$
in the cusp normalization below, where
$D_wu=\langle du,w\rangle_{\rm hyp}$ and
$\mathcal R(s)=(\Delta-s(1-s))^{-1}$. The integrals are bilinear,
not sesquilinear, so their meromorphic spectral dependence is explicit.
Its double pole has coefficient $-8\pi^2\|w\|^2/V^2$.

For the two integral Betti directions of the elliptic factor, the
resulting Hodge energy matrix is exactly
$$G=\begin{pmatrix}40b/\omega_1&0\\0&40\omega_1/b\end{pmatrix},
\qquad\det G=1600. \tag{1.2}$$
This is not the point-height matrix in its specified full Mordell–Weil
basis. A further positive construction expresses that actual height
matrix using the same reduced Green resolvent, with explicit point
charges and rational logarithmic correction factors (§6). Equality of
the two types of sources is then tested, rather than assumed from the
shared inverse operator.

## 2. Character gauge and every cusp phase

On $\mathfrak H$ choose a real primitive $F$ of $w$. Write
$F_a=\lim_{y\to\infty}F(\sigma_a i y)$ for each chosen cusp lift.
The harmonic cusp form decays exponentially, so these limits exist.
Let $\chi_\epsilon(\gamma)=e^{2\pi i\epsilon k(\gamma)}$. The
character Eisenstein series, with incoming coefficient one at cusp $b$,
is
$$E_{\epsilon,b}(z,s)=\sum_{\gamma\in\Gamma_b\backslash\Gamma}
 \chi_\epsilon(\gamma)^{-1}\Im(\sigma_b^{-1}\gamma z)^s.$$
Parabolic triviality makes the sum well defined. It transforms by
$\chi_\epsilon$ under $\Gamma$, and agrees with the integral
$T$-family under $T=e^{2\pi i\epsilon}-1$.

Define the invariant gauge-normalized family
$$D_{\epsilon,b}(z,s)=e^{2\pi i\epsilon(F_b-F(z))}E_{\epsilon,b}(z,s).
\tag{2.1}$$
If $\Phi^\chi_{ab}(s,\epsilon)$ is the original outgoing coefficient,
the gauged coefficient is
$$\Phi^D_{ab}(s,\epsilon)
 =e^{2\pi i\epsilon(F_b-F_a)}\Phi^\chi_{ab}(s,\epsilon). \tag{2.2}$$
The incoming coefficient remains $\delta_{ab}$. Thus, with
$h_{ab}=F_b-F_a$, the exact boundary corrections are
$$\begin{aligned}
\dot\Phi^D_{ab}&=\dot\Phi^\chi_{ab}+2\pi i h_{ab}\Phi_{ab},\\
\ddot\Phi^D_{ab}&=\ddot\Phi^\chi_{ab}
           +4\pi i h_{ab}\dot\Phi^\chi_{ab}-4\pi^2h_{ab}^2\Phi_{ab}.
\end{aligned} \tag{2.3}$$
For the standard lifts at 389, take the primitive based at $i\infty$.
The exact cusp period of $\pi^*\omega$ from infinity to zero vanishes
because $L(f,1)=0$. Hence $F_\infty=F_0=0$, and (2.2) has no phase
correction. This is a proved property of these lifts, not a general
license to omit (2.3).

**[NEW] Lemma 2.1 (positive-Laplacian derivatives).** The conjugated
operator is
$$\Delta_\epsilon=e^{-2\pi i\epsilon F}\Delta e^{2\pi i\epsilon F}
 =\Delta+\epsilon L_1+\tfrac{\epsilon^2}{2}L_2,$$
where
$$L_1=-4\pi iD_w,\qquad L_2=8\pi^2|w|^2. \tag{2.4}$$
There are no higher operator derivatives.

*Proof.* Apply the Euclidean product rule to $e^{2\pi i\epsilon F}u$,
multiply by $-y^2$, and use $dF=w$ and $\Delta F=0$. The cross
term is $-4\pi i\epsilon y^2\nabla F\cdot\nabla u$ and the square
term is $4\pi^2\epsilon^2 y^2|\nabla F|^2u$. This gives (2.4).
The constant factor $e^{2\pi i\epsilon F_b}$ has no spatial derivative.
$\square$

The meromorphic continuation and resolvent identities for these
derivatives are available for cofinite groups with cusps in
Petridis–Risager, [arXiv:1703.09526v3, Corollary 4.5, Lemma 5.1 and
Theorems 5.2–5.4](https://arxiv.org/html/1703.09526). They use the
opposite Laplacian sign; (2.4) fixes ours directly. Their cusp-phase
conversion is retained here in (2.2), rather than identifying all
normalizations of a differentiated scattering matrix.

## 3. Second variation and its boundary integral

Dots denote actual $\epsilon$ derivatives, not Taylor coefficients.
Differentiation of $(\Delta_\epsilon-s(1-s))D_{\epsilon,b}=0$ gives
$$\begin{aligned}
(\Delta-s(1-s))\dot D_b&=-L_1E_b,\\
(\Delta-s(1-s))\ddot D_b&=-2L_1\dot D_b-L_2E_b.
\end{aligned} \tag{3.1}$$
For real $s>1$, the sources have exponential cusp decay. The derivatives
have no incoming term and their outgoing $y^{1-s}$ terms are $L^2$.
Since $s(1-s)<0$, the inverse is unique and
$$\dot D_b=-\mathcal R(s)L_1E_b,\qquad
\ddot D_b=2\mathcal R(s)L_1\mathcal R(s)L_1E_b
                                      -\mathcal R(s)L_2E_b. \tag{3.2}$$
Both identities extend meromorphically through the continued resolvent.

**[NEW] Proposition 3.1 (scattering Hessian).** With the notation in
§2, equation (1.1) holds for $\ddot\Phi^D$. At 389 with the standard
cusp lifts it is also $\ddot\Phi^\chi$.

*Proof.* Truncate both cusps at height $Y$ and apply Green's identity
to $E_a$ and $H=\ddot D_b$. With the positive Laplacian it gives
$$\int(E_a\Delta H-H\Delta E_a)d\mu
 =\sum_c\int_0^1(H\partial_yE_a-E_a\partial_yH)_{c,Y}dx.$$
The constant terms are $E_a=\delta_{ca}y^s+\Phi_{ca}y^{1-s}$ and
$H=\ddot\Phi^D_{cb}y^{1-s}$, up to exponentially small terms.
The outgoing-outgoing terms cancel. The surviving boundary limit is
$(2s-1)\ddot\Phi^D_{ab}$. Substituting (3.1) proves
$$\ddot\Phi^D_{ab}=-\frac1{2s-1}
             \int E_a(2L_1\dot D_b+L_2E_b)d\mu. \tag{3.3}$$
There is no hidden discarded incoming derivative; (2.1) made it zero.

Insert the first identity in (3.2). The real harmonic vector field
dual to $w$ has zero divergence, and cusp terms in integration by
parts vanish by exponential decay. Thus $D_w$ is antisymmetric for
the bilinear integral. Using $L_1=-4\pi iD_w$ twice gives
$$\int E_a L_1\mathcal R(s)L_1E_b
 =16\pi^2\int D_wE_a\,\mathcal R(s)D_wE_b.$$
Together with $L_2=8\pi^2|w|^2$ this proves (1.1). The same argument
for the first derivative gives
$\dot\Phi^D_{ab}=-(2s-1)^{-1}\int E_aL_1E_b$.
The previously reviewed first-response vanishing therefore proves
$\dot\Phi^D=0$ for this curve and direction. $\square$

For reference, a second derivative in $T$ is different. At $T=0$,
$$[T^2]D(T)=-\frac{\ddot D(0)}{8\pi^2}
                         -\frac{\dot D(0)}{4\pi i}. \tag{3.4}$$
This follows from $d/d\epsilon=2\pi i(1+T)d/dT$. The same conversion
holds for scattering coefficients. Since $\dot\Phi^D=0$ here, its
integral-$T$ quadratic coefficient is $-\ddot\Phi^D/(8\pi^2)$.
This keeps the rank-three integral local system separate from an
unhalved complex character derivative.

## 4. Every singular coefficient and the finite Green term

Set $t=s-1$. Use the already normalized Laurent coefficients
$$E_a(z,1+t)=R/t+A_a(z)+tB_a(z)+O(t^2),\qquad R=1/V.$$
They are the $A_0,A_1$ of the Mellin note, at each cusp. In particular
$A_\infty+A_0$ and $A_\infty-A_0$ have the exact eta formulas there,
including the $\log389$, gamma and zeta constants. No constant in
them is free to be adjusted in the following formulas.

Let $P_0u=V^{-1}\int u\,d\mu$ and let
$\mathcal G=\Delta^{-1}$ on mean-zero $L^2$ functions. The isolated
constant eigenfunction gives
$$\mathcal R(1+t)=\frac{P_0}{t(1+t)}+\mathcal G+O(t)
\quad\text{on the orthogonal complement, with its analytic extension}.
\tag{4.1}$$
More precisely the second summand is $(\Delta+t+t^2)^{-1}(1-P_0)$,
whose value at $t=0$ is $\mathcal G$.
Each $D_wE_a$ has mean zero, by the same divergence calculation, and
is regular at $t=0$ because $D_w$ kills the constant pole. Therefore
the resolvent term in (1.1) is regular at one.

Define the convergent real/bilinear quantities
$$\begin{aligned}
W&=\int |w|^2d\mu,\\
C_{ab}&=\int |w|^2(A_a+A_b)d\mu,\\
Q_{ab}&=\int |w|^2(A_aA_b+R(B_a+B_b))d\mu,\\
J_{ab}&=\int D_wA_a\,\mathcal G D_wA_b\,d\mu.
\end{aligned}$$

**[NEW] Proposition 4.1 (Laurent expansion with finite part).**
$$\ddot\Phi^D_{ab}(1+t)
 =\frac{-8\pi^2R^2W}{t^2}
 +\frac{-8\pi^2(RC_{ab}-2R^2W)}t
 +8\pi^2(4J_{ab}-Q_{ab}+2RC_{ab}-4R^2W)+O(t).
\tag{4.2}$$

*Proof.* The direct integral in (1.1) expands as
$R^2W/t^2+RC_{ab}/t+Q_{ab}+O(t)$. The other integral has value
$J_{ab}$ at zero by (4.1) and its mean-zero source. Finally
$(2s-1)^{-1}=1-2t+4t^2+O(t^3)$. Multiplication gives every coefficient
in (4.2). $\square$

For the ungauged matrix at arbitrary cusp phases one must further
apply (2.3); the factors of the old scattering matrix and its first
derivative then alter the simple pole and finite part. At 389 these
corrections are exactly zero. The double-pole normalization agrees
with the second-moment singularity in Petridis–Risager, Theorem 6.3;
their generating Dirichlet series has an additional gamma quotient,
which is not silently identified with the scattering entry here.

## 5. The rank-two elliptic factor measures a Hodge pairing

Adjoin the second integral direction
$$w_1=\Re\pi^*\omega/\omega_1,\qquad
w_2=\Im\pi^*\omega/b.$$
Each has integer periods. A two-parameter character gives mixed
derivatives by polarization of the preceding formulas; its quadratic
pole matrix, after division by $-8\pi^2/V^2$, is
$$G_{ij}=\int_Y\langle w_i,w_j\rangle d\mu. \tag{5.1}$$

**[NEW] Proposition 5.1 (exact integral-Betti Hodge determinant).**
Formula (1.2) holds.

*Proof.* Dirichlet energy of one-forms on a Riemann surface is
conformally invariant. On $E(\mathbb C)=\mathbb C/(\omega_1\mathbb Z+i b\mathbb Z)$,
with coordinate $z=u+iv$, the two normalized forms are
$du/\omega_1$ and $dv/b$. Their energy pairings on the rectangle
are $b/\omega_1$, $\omega_1/b$ and zero. Pullback by a holomorphic
map of degree $d$ multiplies the integral of the corresponding
two-form by $d$, including ramification. Here $d=40$, proving (1.2).
The integral is over the effective orbifold, equivalently the
degree-194 normalized cover; no further stack factor occurs.
$\square$

The columns in (5.1) are the dual Betti directions, not the two
Mordell–Weil points $P=(-1,1)$ and $Q=(0,-1)$. Assigning those
columns to $P,Q$ and asserting $G=H$ is false: $G_{12}=0$, whereas
the existing rational certificate for $H_{12}$ has strictly positive
endpoints in `compute/data/bsd_archimedean_interval.json` (approximately
0.27). The same certificate gives $0<\det H<27/100$, whereas
$\det G=1600$. A new frame/comparison cannot be supplied by silently
making this direct identification. This does not rule out a further
extension with a different specified regulator.

## 6. A positive bridge: the actual heights use the same Green resolvent

It is possible to put the noncuspidal point-height matrix into the
same reduced Green operator, but its sources are different. The
original $D_i=P_i-O$ pull back to divisors meeting the cusps, so
using them directly as $L^2$ point charges would incorrectly ignore
boundary conditions. We now move them explicitly off those cusps.

Retain the divisors $Z_j=B_j+\operatorname{div}h_j$ and rational
functions of the reviewed relative-cycle note, where
$B_1=S-R$, $B_2=T-R$, $R=(4,8)$,
$S=(-51/25,-68/125)$, $T=(1/16,-9/64)$. Put
$$V_*=P-Q=(1,0),\quad W_*=V_*+P=(-3/4,-15/8),\quad V_*+Q=P,$$
$$D'_1=W_*-V_*,\quad D'_2=P-V_*,$$
$$u_1=\frac{x+3/4}{y+x/2-1/2},\qquad
u_2=\frac{x+1}{y-x+1}. \tag{6.1}$$
The chord-divisor formula gives $\operatorname{div}u_i=D'_i-D_i$.
All supports of $D'_i$ and $Z_j$ are disjoint and avoid $O$.
To verify the only new avoidance assertions, exact substitution gives
$$\begin{array}{c|cc}
 &V_*&W_*\\\hline
h_1&413/81&3779/9747\\
h_2&50/9&3599/1083
\end{array}$$
and these points are distinct from $R,S,T$ and from the poles $x=4$.
The old $Z_j$ already avoid $P,Q,O$.

The rational multiplicative evaluations $u_i(Z_j)$ are also explicit:
$$U_{ij}:=u_i(Z_j)=
\begin{pmatrix}
11337/596372&-3599/9025\\
-405/1652&6/25
\end{pmatrix}_{ij}. \tag{6.2}$$
Here evaluation means the product over a rational divisor, including
field norms for its nonrational points. For verification without
factoring $h_j$, use Weil reciprocity in the form
$$u_i(Z_j)=\frac{u_i(S_j)}{u_i(R)}
             \frac{h_j(D'_i)}{h_j(D_i)},\qquad S_1=S, S_2=T.$$
The additional substitutions are
$$\begin{array}{c|ccc}
&R&S&T\\\hline
u_1&1/2&5/8&-4/3\\
u_2&1&-5/12&4/3
\end{array},$$
together with $h_1(P)=5$, $h_1(Q)=5/3$, $h_2(P)=h_2(Q)=4$,
and $h_j(O)=1$. They prove (6.2) by rational arithmetic. No canonical
height or L-value was used to choose the moving functions.

For an integral divisor $D$ of degree zero supported inside $Y$, write
$\delta_D$ for its distributional density against $d\mu$, normalized
by $\int\varphi\delta_Dd\mu=\sum_xn_x\varphi(x)$. At an elliptic
orbifold point use this same evaluation normalization; on a cover it
agrees with pullback divisors and the degree-normalized integral.
The coefficients are coarse-divisor multiplicities: in a uniformizer
with stabilizer order $e$, the pulled-back logarithmic singularity has
coefficient $e$ times that multiplicity, cancelling the $1/e$ orbifold
integration factor.
The logarithmic Green solution of mean zero is $2\pi\mathcal G\delta_D$.
Here $\mathcal G$ is extended distributionally; the solution is locally
logarithmic and $L^2$, bounded at cusps when the charges avoid them.

**[NEW] Proposition 6.1 (exact point-height resolvent formula).**
For $\mathcal D_i=\pi^*D'_i$ and $\mathcal Z_j=\pi^*Z_j$,
$$\boxed{H_{ij}=-\frac{2\pi}{40}
 \langle\delta_{\mathcal Z_j},\mathcal G\delta_{\mathcal D_i}\rangle
                                -\log|U_{ij}|.} \tag{6.3}$$
The angle brackets here mean evaluation at the disjoint divisor,
not an $L^2$ pairing of two unsmoothed delta distributions.

*Proof.* With $dd^c=(i/2\pi)\partial\bar\partial$, one has
$dd^cg=-(\Delta g/4\pi)d\mu$. A single-log Néron Green function
for a degree-zero divisor has $dd^cg=-\delta_D/2$, so it equals
$2\pi\mathcal G\delta_D$ up to a constant. This also follows from
its local singularity $-\log|z|$. Its pullback from $E$ has these
same singularities, is bounded at the cusps, and differs from the
mean-zero $L^2$ solution only by a constant. Pairing with the
degree-zero $\pi^*Z_j$ removes that constant. The projection formula
then gives
$$g_{D'_i}(Z_j)=\frac{2\pi}{40}
       \langle\delta_{\mathcal Z_j},\mathcal G\delta_{\mathcal D_i}\rangle.$$
The principal-divisor identity and (6.1) give
$g_{D_i}=g_{D'_i}+\log|u_i|$ up to a constant. The reviewed
finite corrections for the original $D_i,Z_j$ are zero at every
prime, so Faltings–Hriljac in the already fixed BSD normalization gives
$H_{ij}=-g_{D_i}(Z_j)$. Substitution proves (6.3), with its sign,
factor $2\pi$, degree 40 and rational logarithms. $\square$

The new logarithms are essential: moving $D_i$ alters its finite
intersection symbols by the corresponding rational principal data.
Equation (6.3) retains them exactly instead of asserting that the moved
pair still has zero finite symbols. The original Hodge unit's vertical
term at 389 and the period index two remain those of the earlier notes;
neither is removed by this analytic Green rewriting.

## 7. The first comparison that still fails

The resolvent term of the scattering finite part (4.2) pairs the smooth
mean-zero sources $D_wA_a$ and $D_wA_b$. Its other sources are smooth
densities $|w|^2$ times Eisenstein coefficients. In contrast, (6.3)
uses explicitly marked nonzero point-charge distributions and the
four rational logarithms (6.2). These sources cannot be identified
as distributions: all spectral sources are smooth in the interior,
while the point sources have nonzero atoms there. Applying an inverse
operator to each does not remove that distinction.

A concrete extension can include both by adjoining the logarithmic
potentials $\mathcal G\delta_{\mathcal D_i}$ to the smooth spectral
solutions. Its point block is then exactly the already defined
noncuspidal 1-motive regulator, by (6.3). What is not constructed is
a rational mixed class or pairing identifying the scattering finite
part, or a specified further spectral derivative of it, with that
point block's determinant. The fact that both are expressed using
$\mathcal G$ supplies no such identity.

**[GAP SV-389]** Construct an arithmetic extension/comparison linking
the actual second-character source (1.1), with finite part (4.2), to
the marked point-source determinant (6.3), and to the Mellin class
whose regulator is $\ell L(f,2)$. Retain the complete cusp phases,
the pole subtraction, the rational logarithms, the degree-40 and
degree-194 normalizations and the full real period $2\omega_1$.
No algebraicity of the spectral derivative, primitive integral class,
or cancellation of $L(f,2)$ is assumed. The second-character pole
already computed is a Hodge energy, and is not itself that missing
BSD determinant.
