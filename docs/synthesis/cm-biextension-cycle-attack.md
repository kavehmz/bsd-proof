# A relative CM cycle and its secondary determinant

Date: 2026-09-12. Author: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
This continues the reviewed [CM theta construction](cm-regulator-tensor-attack.md)
and [moment normalization](cm-moment-source-check.md). The new claims
below passed [independent review](review-cm-biextension-cycle.md), with
the stated secondary-regulator scope. The objective remains full BSD over
Q; no finiteness of Sha or rationality of the complex BSD quotient is
assumed.

The construction below produces an explicit rational 1-motive, including
fixed rational Kummer corrections, whose secondary determinant is the
full regulator. It also determines exactly what the naive exterior
zero-cycle detects. A comparison with the torsion second moment remains
unproved; it is not supplied by calling both quantities periods.

## 1. Fixed data and the first exterior cycle

Use the minimal equation and full basis already certified:
$$E:y^2=x^3+39x,\qquad P_1=P=(3,12),\quad P_2=Q=(27,144),
\qquad\omega=dx/(2y).$$
Write $d_R=(R)-(O)$, and put
$$z_{P,Q}=d_P\times d_Q\in\mathrm{CH}^2(E^2)_{\mathbb Q}.
\tag{1}$$
Let $\tau$ exchange the two factors of $E^2$.

**[NEW, cycle and degree calculation] Proposition 1.**
$$z_{P,Q}+\tau_*z_{P,Q}=0. \tag{2}$$
Both $z_{P,Q}$ and its geometric antisymmetrization have zero ordinary
Deligne cycle class in $H^4_{\mathcal D}(E^2_{\mathbb C},\mathbb Q(2))$.
The relevant geometric minus projector on $h^1(E)\otimes h^1(E)$
realizes $\operatorname{Sym}^2H^1(E)$ in cohomological degree two;
it does not realize the one-dimensional Tate determinant.

*Proof.* The quotient $q:E^2\to\operatorname{Sym}^2E$ is finite flat
of degree two. The sum map
$a:\operatorname{Sym}^2E\to E\simeq\operatorname{Pic}^2(E)$ is a
projective-line bundle: a degree-two line bundle has two independent
sections by Riemann–Roch, and the Poincaré bundle exists because $O$
is rational. The projective-bundle formula makes
$a_*:\mathrm{CH}_0(\operatorname{Sym}^2E)\to\mathrm{CH}_0(E)$
an isomorphism. But
$$a_*q_*z_{P,Q}=(P+Q)-(P)-(Q)+(O)=0$$
in $\operatorname{Pic}^0(E)$ by the elliptic group law. Thus $q_*z=0$.
Flat pullback gives $q^*q_*z=z+\tau_*z$, proving (2). This is the
symmetric-product argument underlying
[Beauville–Voisin, Lemma 1.5](https://www.cmls.polytechnique.fr/~voisin/Articlesweb/Chowams.pdf),
here written for two different divisors over Q. No assertion that $z$
itself is nonzero, or zero, in the rational Chow group is needed.

The degree of $z$ is zero. Its Albanese image is also zero: its four
points are $(P,Q)-(P,O)-(O,Q)+(O,O)$, whose sum in $E^2$ is $(O,O)$.
For a smooth projective surface, the Abel–Jacobi invariant of a
degree-zero zero-cycle is its Albanese invariant. The ordinary Deligne
cycle class consists of that invariant and the degree, so both vanish.
Equivalently, Poincaré duality identifies the relevant intermediate
Jacobian from $H^3$ with the Albanese, and integration of the coordinate
one-forms cancels in these four terms.

Finally $d_P,d_Q$ belong to the $h^1$ parts of the two curve motives.
For $\alpha,\beta\in H^1(E)$,
$$\tau^*(\mathrm{pr}_1^*\alpha\wedge\mathrm{pr}_2^*\beta)
=-\mathrm{pr}_1^*\beta\wedge\mathrm{pr}_2^*\alpha.$$
Thus geometric exchange is minus ordinary tensor exchange on this
Künneth component. Its minus eigenspace is $\operatorname{Sym}^2H^1$,
while its plus eigenspace is $\bigwedge^2H^1\simeq\mathbb Q(-1)$.
In particular the motivic cohomology degree of (1) is
$H^4_{\mathcal M}(E^2,\mathbb Q(2))$, not a degree-one extension
whose regulator could simply be the height determinant. $\square$

The complex regulator of the full independent basis is positive.
Consequently (1) with its ordinary Deligne regulator cannot be the
desired regulator class. This is a conclusion about this specified
cycle and regulator, not a vanishing theorem for secondary invariants.

## 2. A specific relative 1-motive

Take the rational two-torsion point $T=(0,0)$ and set
$$B_1=P+T=(13,-52),\qquad
B_2=Q+T=(13/9,-208/27).\tag{3}$$
These coordinates follow from $R+T=(39/x(R),-39y(R)/x(R)^2)$.
Let
$$A=\{O,P,Q\},\qquad B=\{T,B_1,B_2\},\qquad U=E\setminus B.$$
The two supports are disjoint. Put $d_i=(P_i)-(O)$ and
$e_j=(B_j)-(T)$, so $[e_j]=[d_j]$ in $\operatorname{Pic}^0(E)$.

**[THEOREM, construction used]** The generalized Jacobian $J_B$ for
the reduced modulus $B$ is an extension
$$0\longrightarrow T_B\longrightarrow J_B\longrightarrow E
\longrightarrow0,\qquad T_B\simeq\mathbb G_m^2.$$
Divisors away from $B$ have canonical classes in $J_B$. Thus there is
an algebraic 1-motive
$$\mathcal M=[L_A\xrightarrow{u}J_B],\qquad
L_A=\mathbb Z d_1\oplus\mathbb Z d_2,\qquad u(d_i)=[d_i]_B.
\tag{4}$$
Its homological realization is $H_1(U,A)$.
The 1-motive, its biextensions and the curve realization are the
constructions of [Deligne, Hodge III, §§10.1–10.3](https://www.numdam.org/article/PMIHES_1974__44__5_0.pdf),
Publ. Math. IHÉS 44 (1974), DOI 10.1007/BF02685881. In particular
this construction does not posit an unproved general category of
mixed motives or a Sha-finiteness condition.

**[NEW, explicit relative realization] Proposition 2.** If
$H=H_1(U(\mathbb C),A;\mathbb Q)$, then
$$\operatorname{Gr}^W_0H=L_{A,\mathbb Q},\qquad
\operatorname{Gr}^W_{-1}H=H_1(E,\mathbb Q),\qquad
W_{-2}H=L_{B,\mathbb Q}^{\vee}(1),\tag{5}$$
where $L_B=\mathbb Ze_1\oplus\mathbb Ze_2$. Each rank is two.
The following rational differentials give the two residue directions:
$$
\begin{aligned}
\kappa_1&=\left(\frac{y-52}{x-13}-\frac yx\right)\omega,\\
\kappa_2&=\left(\frac{y-208/27}{x-13/9}-\frac yx\right)\omega.
\end{aligned}\tag{6}
$$
Their residue divisors are $e_1,e_2$, respectively.

*Proof.* The localization sequence for $E\setminus B$ inserts the
two independent small loops about $B_1,B_2$ into $H_1(U)$; the loop
about $T$ is their negative sum. These are the weight-minus-two
Tate directions. Quotienting gives $H_1(E)$. The relative sequence
$0\to H_1(U)\to H_1(U,A)\to\widetilde H_0(A)\to0$ supplies the
two weight-zero directions, proving (5). Analytically, the generalized
Jacobian is obtained by integrating differentials with these allowed
simple poles; adjoining the paths of the divisors $d_i$ gives exactly
the realization of (4).

For $R=(a,b)$ with $b\ne0$, the differential
$((y+b)/(x-a))\omega$ has residue $+1$ at $R$, residue $-1$ at
$O$, and no other pole. At $-R$ its numerator cancels the denominator.
For $T$, $y\omega/x=dx/(2x)$ has the same residues at $T,O$,
because $x$ has a double zero at $T$. Subtracting this latter form
proves (6), including cancellation of the pole at $O$. $\square$

Choose paths $\gamma_i$ from $O$ to $P_i$ in $U(\mathbb C)$. The
matrix $I^0_{ij}=\int_{\gamma_i}\kappa_j$ is therefore a genuine
relative period block. At infinity one normalizes the third-kind
forms to have purely imaginary periods. At a good split $p\ge5$
one uses the Coleman–Gross normalization with complement
$W_p=\mathbb Q_p(x\omega)$, proved to be the canonical unit-root
line in the predecessor note. Each normalized form has the shape
$$\kappa_{j,v}=\kappa_j+a_{j,v}\omega.\tag{7}$$
The coefficients in (7) are determined by the indicated realization's
splitting, not assumed rational or zero because the CM $E_2$ vanishes.
Write $I_{ij,\infty}=\operatorname{Re}\int_{\gamma_i}\kappa_{j,\infty}$
and $I_{ij,p}=\int_{d_i}^{\rm Col}\kappa_{j,p}$.

The real normalization and its relation to biextension periods are
fixed in [Bloch–de Jong–Sertöz, §§2 and 4](https://arxiv.org/html/2206.01220v2),
J. London Math. Soc. 108 (2023), 340–361, DOI 10.1112/jlms.12747.
For the ordinary p-adic normalization use
[Balakrishnan–Besser, §§2–4](https://arxiv.org/html/1201.6016v2).
Their Corollaries 4.2–4.3 give exactly $-2\log\sigma_p$ locally
and $+2\log_p d$ for the denominator correction. Thus the resulting
quadratic height is precisely the SW convention of the predecessor
note. The real convention is $\lim_n4^{-n}h_x(2^nR)$, twice the
height associated to the degree-one theta divisor. No factor two is
discarded in either realization.

## 3. Computing every finite-place correction

Let $C_{\ell,ij}$ be the intersection of extensions of $d_i,e_j$ to
the minimal proper regular model at $\ell$, with one extension made
orthogonal to all fiber components. The correction is independent
of the ambiguity of adding the whole fiber, since the other divisor
has degree zero.

**[NEW, exact arithmetic computation] Proposition 3.** The only
nonzero matrices are
$$
C_2=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\quad
C_3=-\frac12\begin{pmatrix}1&3\\3&5\end{pmatrix},\quad
C_7=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{8}
$$
In particular $C_{13}=0$. For both $v=\infty$ and the good split
primes $p$ under consideration, the full global height matrix is
$$
H_v=I_v+\frac12
\begin{pmatrix}
\log_v(3/2)&\log_v(27/98)\\
\log_v(27/98)&\log_v(243/2)
\end{pmatrix}.
\tag{9}
$$
Here $\log_\infty$ is the real logarithm and $\log_p p=0$.

*Proof.* The exact discriminant is $-64\cdot39^3$, and the certified
conductor is $2^5\cdot3^2\cdot13^2$. At every bad prime Ogg's
formula gives two geometric fiber components. The reduction is
additive (the $j$-invariant is integral), so each fiber has Kodaira
type III. Its nonidentity component has self-intersection $-2$.
If $r_i,s_j$ are the intersections of $d_i,e_j$ with that component,
the vertical correction is $r_i s_j/2$: adding $(r_i/2)$ times that
component makes $d_i$ orthogonal to it and to the identity component.

At 2 the singular point of the reduced minimal cubic is $(1,0)$.
Both $P_i$ and both $B_j$ reduce there, while $O,T$ are in the
identity component. Thus $r_i=s_j=1$. At 3 the singular point is
$(0,0)$; $P,Q,T$ are nonidentity, while $B_1$ is nonsingular and
$B_2$ is in the formal group. Thus $r_i=1,s_j=-1$. At 13 both
$P_i$ are identity, and $B_1,B_2,T$ are nonidentity, giving
$r_i=s_j=0$. These component assertions can equally be read from
the displayed coordinates and the definition of $E_0$ by smooth
reduction on the minimal cubic.

For completeness the horizontal intersections also admit a complete
calculation. Sections lie in the smooth Néron locus of the regular
model. Translation there shows that the intersection of two distinct
sections $R,S$ is
$$j_\ell(R-S),\qquad
j_\ell(V)=\max\{0,-v_\ell(x(V))/2\}.$$
If their reductions differ the intersection is zero; if they agree,
the formal parameter $t=-x/y$ of their difference has this valuation
and computes the intersection length. In our configuration,
$$P_i-B_i=T,\quad P_i-T=B_i,\quad
x(P-B_2)=x(Q-B_1)=156/49.$$
For example $P-Q=(49/4,385/8)$ and adding $T$ gives that last
$x$-coordinate. Thus the horizontal contribution is
$$j_\ell(P_i-B_j)-j_\ell(B_i)-j_\ell(B_j).$$
The only negative valuations involved are $v_3(x(B_2))=-2$ and
$v_7(156/49)=-2$. The horizontal matrices are consequently
$\left(\begin{smallmatrix}0&-1\\-1&-2\end{smallmatrix}\right)$ at 3,
$\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ at 7,
and zero elsewhere. Adding the vertical contributions proves (8).

The local/global Néron formula is
$H_\infty=I_\infty-\sum_\ell C_\ell\log\ell$, with these signs;
see equations (4.3)–(4.4) in Bloch–de Jong–Sertöz. For p-adic
heights take the global idèle character whose component at $p$ is
$\log_p$ and whose value on a uniformizer $\ell$ away from $p$
is $-\log_p\ell$. The sum vanishes on Q-times by the product formula.
Balakrishnan–Besser (2.1) therefore gives
$H_p=I_p-\sum_{\ell\ne p}C_\ell\log_p\ell$.
The omitted $p$ term would be zero anyway. Inserting (8) gives (9).
Since $[e_j]=[d_j]$, these are the full height pairings on the
certified basis; their matrices are symmetric. $\square$

This is a fixed calculation of the arithmetic data of the proposed
cycle. It neither scans p-adic leading coefficients nor uses a
conjectural analytic Sha value.

## 4. Incorporating the corrections into an algebraic object

Choose coordinates on $T_B$ dual to the residue divisors $e_1,e_2$,
so that the period of its point $(r_1,r_2)$ against residue direction
$j$ is $\log_v r_j$. This fixes the orientation of the inclusion
$\iota:T_B\hookrightarrow J_B$. Put
$$r_1=(3/2,27/98),\qquad r_2=(27/98,243/2)\in T_B(\mathbb Q).$$
Define a new, entirely algebraic 1-motive
$$\mathcal M^\sharp=
[\mathbb Z^2\xrightarrow{u^\sharp}J_B],\qquad
u^\sharp(b_i)=2u(d_i)+\iota(r_i),\tag{10}$$
using additive notation for $J_B$ and multiplicative notation for
the torus point. Give its weight-zero part the rational frame
$a_i=b_i/2$. Its projection to $E$ sends $a_i$ to $P_i$.
The only denominator of this frame is two.

**[NEW, corrected relative realization] Proposition 4.** The secondary
height block of $\mathcal M^\sharp$ on the frame $a_1,a_2$, with
the real or ordinary p-adic normalization specified in §2, is $H_v$
in (9). In particular its secondary exterior determinant is
$$\det H_\infty=\operatorname{Reg}_\infty,
\qquad \det H_p=4A_pB_p-(C_p-A_p-B_p)^2.\tag{11}$$

*Proof.* The normalized local pairing against each $e_j$ descends to
a logarithm on $J_B$. Indeed a defining generalized-Jacobian relation
is a principal divisor $(f)$ with $f$ taking the same nonzero value
at all points of $B$; its local pairing is $\log_v f(e_j)=0$.
The resulting logarithm restricts to the ordinary logarithm of
character $e_j$ on $T_B$. At infinity the real part has zero periods
by the chosen normalization; at $p$ the specified Coleman splitting
gives the logarithm. Thus it is additive on $J_B$ with precisely the
torus normalization used in (10).

The point $2u(d_i)$ has twice the original relative period
row. Adding the rational torus point contributes $\log_v(r_{ij})$
in residue direction $j$, without changing the abelian image or its
holomorphic-period normalization. Dividing the lattice frame by two
therefore gives $I_{ij,v}+\tfrac12\log_v(r_{ij})$. Equation (9)
identifies this with the genuine global height row, proving the
first assertion. The second follows by taking the determinant and
using the already proved polarization formula for $A_p,B_p,C_p$.
Neither assertion requires a nonzero p-adic determinant. $\square$

The correction is thus realized by fixed rational Kummer points,
rather than an unspecified real or p-adic scalar. This does not say
that an arbitrary local period of a 1-motive is a canonical height:
the local splittings and the explicit frame in (10) are essential.
At the primes $p\ge5$ these frames remain integral over $\mathbb Z_p$.
This assertion is about the fixed denominators of the construction,
not about the regulator being a unit.

Here is a precise degree-two secondary class and its factor. Before
the Kummer correction, form the product relative pair
$$(U^2,\ A\times U\ \cup\ U\times A).$$
For any two normalized differential forms $\eta_1,\eta_2$ and
relative paths $\gamma_1,\gamma_2$, its relative two-cycle
$$\Gamma_{12}=\gamma_1\times\gamma_2-\gamma_2\times\gamma_1$$
satisfies the exact identity
$$\int_{\Gamma_{12}}\mathrm{pr}_1^*\eta_1\wedge\mathrm{pr}_2^*\eta_2
=\det\left(\int_{\gamma_i}\eta_j\right).\tag{12}$$
This is Fubini with the product orientations. Geometric factor exchange
acts as minus tensor exchange on products of degree-one chains, so
$\Gamma_{12}$ is in the geometric plus part. Its abstract tensor
realization is the ordinary exterior square of the six-dimensional
relative $H_1$, not the pure component of (1).

For (10), take the same exterior construction in the tensor category
generated by this algebraic 1-motive and the displayed rational Kummer
motives. The resulting framed object $\Xi_{P,Q}$ has top frame
$a_1\wedge a_2$ and bottom frame dual to $e_1\wedge e_2$, with
extreme graded pieces Q(0) and Q(2). Its graded ranks, in weights
$0,-1,-2,-3,-4$, are respectively
$$1,\ 4,\ 5,\ 4,\ 1.\tag{13}$$
These are obtained by taking the exterior square of the three graded
pieces of ranks 2,2,2 in (5). Thus this is a specific framed tensor
of an algebraic 1-motive, with a relative degree-two realization.
It is not claimed to be a new element of
$\mathrm{CH}^2(E^2)$ or of $\operatorname{Ext}^2(\mathbb Q,\mathbb Q(2))$.

**[NEW, secondary exterior formula] Lemma 5.** Let $N_v$ be the
central height-obstruction block of the normalized realization (10),
viewed on its weight-graded vector space: it sends $a_i$ to
$\sum_jH_{ij,v}f_j$ in the bottom Tate space and is zero on the
other graded pieces. The $f_j$ are the bottom frame dual to $e_j$.
Let $N_v^{\wedge}$ be its derivation action on the exterior square.
Then
$$\frac12(N_v^{\wedge})^2(a_1\wedge a_2)
=\det(H_v)f_1\wedge f_2.\tag{14}$$

*Proof.* $N_v^2=0$, so applying the derivation twice gives exactly
$2N_va_1\wedge N_va_2$. Expansion in $f_1,f_2$ gives twice the
determinant. $\square$

This computes the requested secondary regulator of $\Xi_{P,Q}$.
The height obstruction uses the Hodge/real or filtered Frobenius
splitting; $N_v$ is not asserted to be a rational motivic endomorphism.
In particular (14) must not be used to manufacture a rational
projector from its real or p-adic matrix. At infinity the obstruction
is a normalized, single-valued biextension period, rather than the
raw holomorphic period block; this distinction is explicit in
Bloch–de Jong–Sertöz Theorem 2.9.

## 5. Testing the actual torsion specialization

The next proposed operation was to restrict the universal Poincaré
connection to the conductor-torsion arguments of the Katz construction
and transport their frames to (10). This has a precise obstruction
already at the first logarithm layer.

**[NEW, arithmetic obstruction to the first specialization map]
Proposition 6.** Let $F$ be any number field containing all support
points of a torsion endpoint construction. Let
$\mathcal T=[L\to G]$ be a 1-motive such that its lattice map has
torsion image in the abelian quotient of $G$. Every morphism of
rational 1-motives
$$\mathcal T\longrightarrow\mathcal M^\sharp_F\otimes\mathbb Q$$
induces zero on the weight-zero lattice. In particular no such map
can carry two torsion endpoint frames to $a_1,a_2$.

*Proof.* A morphism is a compatible pair of maps on lattices and
semiabelian varieties; the statement with rational coefficients is
obtained by clearing denominators. On abelian quotients, compatibility
sends the image of every source lattice element to a torsion point.
The torus part maps to zero in $E$. But the target lattice map to
$E(F)\otimes\mathbb Q$ is
$$\mathbb Q^2\longrightarrow E(F)\otimes\mathbb Q,
\qquad(a,b)\longmapsto aP+bQ.$$
It is injective: an integer relation that is torsion over $F$ is
the same relation among the original rational points, contradicting
their certified independence. Therefore the lattice component of
the morphism is zero. $\square$

This is applicable to each finite level consisting only of torsion
point Kummer 1-motives and their torus extensions. CM multiplication,
finite torsion distribution, and morphisms between those objects do
not change its conclusion. It is not a claim that the entire elliptic
polylogarithm is such a 1-motive: its higher extension classes are
explicitly outside this proposition. An inverse limit or a derived
operation creating a new extension would require an additional argument.

To push beyond this obstruction, use the actual connection forms (6).
Their residue map and all rational differential coefficients are
explicit, while (7) inserts the realization's splitting. If
$u_i=\int_{\gamma_i}\omega$ and $a=(a_{1,v},a_{2,v})^t$, then before
the real single-valued operation the normalized matrix is
$$I_v=I^0_v+ua^t,\qquad
\det(I^0_v+ua^t)=\det I^0_v+a^t\operatorname{adj}(I^0_v)u.\tag{15}$$
The last equality follows by direct expansion of a two-by-two
determinant; its quadratic term vanishes since $ua^t$ has rank one.
After inserting the Kummer correction one replaces $I^0_v$ in
(15) by $I^0_v+\tfrac12\log_v r$. Thus even the scalar to be
compared is sensitive to the non-torsion extension's splitting.
Knowing the universal rational connection is not the same as knowing
that its framed scalar lies in the specified rational line.

The relevant primary source is
[Bannai–Kobayashi–Tsuji, 0711.1701v2](https://arxiv.org/html/0711.1701v2):
Proposition 1.6 gives rational connection functions, and Theorem 4.15
constructs the full filtered Frobenius polylogarithm. Theorem A.19
permits a Hodge realization at our non-torsion points. Its explicit
syntomic value in Theorem 4.23, however, uses a nonzero prime-to-p
torsion point and the splitting of Lemma 4.20. Applied directly at
$P,Q$ it does not supply the missing trivialization; Proposition 6
explains the elementary obstruction at its first logarithm layer.
No new higher-extension comparison producing that trivialization
has been constructed here.

The torus correction in (10) suggests a second concrete attempt:
apply algebraic characters of $J_B$ to its two lattice points and
compare their logarithms with elliptic units. This attempt can also
be decided on the actual arithmetic object.

**[NEW, no algebraic logarithm shortcut] Proposition 7.**
$$\operatorname{Hom}_{F\text{-groups}}(J_{B,F},\mathbb G_m)=0$$
for every number field $F$. Thus the normalized logarithms in the
proof of Proposition 4 cannot be obtained from nonzero algebraic
characters of $J_B$.

*Proof.* Any character of $J_B$ restricts to a character
$(n_1,n_2)$ of $T_B$. A character trivial on the torus factors
through $E$ and is zero, since an abelian variety has no nonconstant
regular invertible function. The obstruction to extending a torus
character is the pushout class of the extension $J_B$: under the
Poincaré identification
$\operatorname{Ext}^1(E,\mathbb G_m)=\operatorname{Pic}^0(E)$,
it is $n_1[e_1]+n_2[e_2]$, up to the common sign of the torus
orientation. These classes are $n_1P+n_2Q$. Independence of the
certified basis forces $n_1=n_2=0$ whenever this class vanishes.
The same reasoning after clearing denominators proves the rational
version. This description of the generalized-Jacobian extension
is precisely its Poincaré construction: pushing out by the residue
character of a divisor on $B$ gives that divisor's degree-zero
line bundle. $\square$

Consequently the fixed rational points $r_i$ in the kernel torus
really can correct the local height block, but those torus coordinates
do not extend to rational functions that are group characters on
all of $J_B$. The tested character map therefore does not replace the
secondary realization in (14) by logarithms of global algebraic characters.
This excludes a specified map; it does not exclude higher
polylogarithmic regulators or settle the missing equality below.

## 6. The first remaining equality, with its rational target

Let
$$\mathscr L_{P,Q}=\det_{\mathbb Q}(L_A\otimes\mathbb Q)
\otimes\det_{\mathbb Q}(L_B\otimes\mathbb Q)$$
be the rational line of the two exterior frames. Denote its generator
$(d_1\wedge d_2)\otimes(e_1\wedge e_2)$, as realized by the
framed object above, also by $\Xi_{P,Q}$. Let its secondary
realizations be
$$R_\infty(\Xi_{P,Q})=\operatorname{Reg}_\infty,
\qquad R_p(\Xi_{P,Q})=\operatorname{Reg}_p.$$
This is a line of frames with specified secondary realization maps;
it is not a claim that the fifteen-dimensional object in (13) has
collapsed to a Tate motive. Its frame is integral away from two.

Keep all the verified constants of the predecessor note:
$$c_{\rm cmp,p}=(156i\Omega_p)^{-1},\quad
e_p=(1-\alpha_p^{-1})^2,\quad
M_p=\int(\log_p\chi_{\rm cyc})^2\,d\mu_\psi.$$

**[GAP CM-Biex, precise remaining construction].** Construct from the
fixed CM torsion theta/polylogarithm object a rational framed element
$Z_\theta\in\mathscr L_{P,Q}$, independently of assigning it a real
coefficient, such that
$$
R_\infty(Z_\theta)=\frac{L''(E,1)/2}{2\Omega_E},\qquad
R_p(Z_\theta)=\frac{c_{\rm cmp,p}M_p}{4e_p}
\quad\text{for every good split }p\ge5\text{ in the stated scope}.
\tag{16}
$$
If $Z_\theta=q\Xi_{P,Q}$, its rational coefficient $q$ would have to
equal
$$q=\frac{L''(E,1)/2}{2\Omega_E\operatorname{Reg}_\infty}=n_E.$$
Thus the first equality in (16) proves rationality rather than
presupposing it. The second is then the canonical Q-to-Q_p comparison
CM-Theta. A zero p-adic regulator is permitted in the statement;
no division by it is used to formulate the gap.

The attempted construction reached an actual arithmetic object (10),
the fully computed Kummer correction (8)–(9), and its secondary
exterior realization (14). The direct finite-level torsion transfer
fails by Proposition 6, and the direct algebraic-character extraction
of elliptic-unit logarithms fails by Proposition 7. Passing to the full polylogarithm gives
well-defined additional extensions but no verified map into this
specific framed line with the realizations (16). The moment formula
alone assigns numbers to torsion translations, not such a rational
framed element. Equality of ideals or values up to units would not
establish (16).

The construction therefore proves neither (16), nondegeneracy of
every p-adic regulator, finiteness of Sha, nor BSD. It identifies an
actual secondary arithmetic realization on the full basis and the
first exact comparison still required. All new identities above are
independent of those unproved assertions.
