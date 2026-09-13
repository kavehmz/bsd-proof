# CM theta functions and the rank-two regulator tensor

Date: 2026-09-12. This is a proof attempt toward the common-tensor target
in [coherent-moment-attack.md](coherent-moment-attack.md). It constructs
an exact common-theta description of the regulator and the cyclotomic
second moment, and a higher-precision moment identity that permits a
nonunit regulator. It does not identify those two operations on theta,
prove full Sha finiteness, or prove BSD. See the
[independent review](review-cm-regulator-tensor.md), now **PASS** for
the stated deductions and the direct source audit, and the independently reproduced
[analytic certificate](../../compute/data/cm39_analytic_rank_certificate.json).
No historical novelty is claimed.

## 1. The actual curve and source hypotheses

Take
$$
E:\ y^2=x^3+39x,\quad K=\mathbb Q(i),\quad
P=(3,12),\quad Q=(27,144),\quad\omega=dx/(2y).
\tag{1}
$$
This is the fifth curve of Banwait,
[arXiv:2609.08431v1](https://arxiv.org/html/2609.08431v1), a September
2026 preprint. Its Theorem B, §§2.1–2.6, 3.1–3.3, 6.1–6.3, 7.1–7.2,
and 13 were read. The theorem assumes algebraic rank two, $L(E,1)=0$,
root number $+1$, and a good split $p\ge5$ outside its specified
excluded set; it does not assume the complex analytic rank is exactly
two or full Sha finiteness.

**[THEOREM, exact arithmetic verification]** For (1),
$$
N=48672=2^5\cdot3^2\cdot13^2,
\quad E(\mathbb Q)_{\rm tors}\simeq\mathbb Z/2,
\quad \prod_v c_v=8,
\quad w(E)=+1,
\quad\operatorname{rank}E(\mathbb Q)=2.
$$
The points $P,Q$ form a full basis modulo torsion. Besides the source's
Table 1, a read-only exact check with Sage 10.7/PARI and eclib gave
`ellrank=[2,2,0,[[3,12],[27,144]]]` and full saturation
`(True,1,'[ ]')`. The exact command is recorded in §8.
Also $P+Q=(1/4,25/8)$ by the rational group law.

The already reviewed Mellin-certification algorithm, run on the explicit
coefficients of (1), also proves analytic rank two: its second completed
derivative has the positive enclosure
$608.09681704\pm2.27\cdot10^{-9}$, with 96-bit balls, integration
cutoff 40 and Fourier cutoff 1405. The leading coefficient lies in
the exact interval recorded in §8. This supplies the nonzero second
complex coefficient for this actual test curve; it is not inferred
from the preprint's approximate analytic-Sha entry.

The source's excluded set for this curve is contained in
$\{2,3,13\}$. More generally its five clauses are bad primes and the
torsion/Tamagawa factors, anomalous primes, reducible residual images,
period-comparison primes, and ray-class-order primes. Throughout the
identities using its Katz comparison, retain its conditions
$$
p\ge5,\qquad p\equiv1\pmod4,\qquad p\notin S_E.
\tag{2}
$$
For this curve $a_5=-2$, so the possible anomalous prime $5$ for a
$j=1728$ curve is not anomalous here. The regulator is nonetheless
allowed to be a nonunit: the source records this at $p=5$ and $15289$.
No finite-prime scan is used as a uniform theorem.

**Periods fixed exactly.** The model in (1) is minimal and has negative
discriminant, hence one real component. Let $\Omega_E$ be its full
real Néron period. Fix
$$
\Omega_\infty=\frac{1+i}{2}\Omega_E,\qquad
\mathfrak f=(1+i)^3(39),\qquad f_0=39(1+i)^3.
$$
Then $\Gamma=\Omega_\infty\mathbb Z[i]$ is the lattice for $\omega$,
$\mathrm N\mathfrak f=12168$, and the period ratio is
$\varpi_E=\Omega_E/\Omega_\infty=1-i$.
Thus $f_0\varpi_E=156i$. These are the period and conductor conventions
of Banwait §2.3 and Table 1. An embedding $K\hookrightarrow\mathbb Q_p$
corresponding to $\mathfrak p\mid p$ is fixed each time; $i$ in a
$p$-adic formula denotes its image under this embedding.

## 2. CM does not make the Mordell–Weil rank one

**[NEW, elementary CM descent] Lemma 1.** For any rational elliptic
curve $y^2=x^3-Dx$ and $K=\mathbb Q(i)$,
$$
E(K)\otimes\mathbb Q
=\bigl(E(\mathbb Q)\otimes\mathbb Q\bigr)
 \oplus[i]\bigl(E(\mathbb Q)\otimes\mathbb Q\bigr).
\tag{3}
$$
Consequently the curve (1) has rational rank four over $K$ and
$\mathbb Z[i]$-rank two. The analogous equality on free Mordell–Weil
modules holds after tensoring with $\mathbb Z_p$ for odd $p$.

*Proof.* The automorphism is $[i](x,y)=(-x,iy)$ and complex
conjugation $c$ satisfies $c[i]=-[i]c$. The projectors $(1\pm c)/2$
split $E(K)\otimes\mathbb Q$. The plus space is the rational
Mordell–Weil space, and $[i]$ identifies it with the minus space.
For any vector $v^-$ in the minus space, $-[i]v^-$ is in the plus
space and $v^-=[i](-[i]v^-)$. This proves (3). The same averaging
argument works over $\mathbb Z_p$ for odd $p$, after discarding
torsion; any discrepancy from taking invariants before removing
torsion is killed by two. $\square$

At a split prime, $T_pE$ has rank one over
$\mathbb Z[i]\otimes\mathbb Z_p$, and each idempotent component has
$\mathbb Z_p$-rank one. This is the rank of a **Galois representation**,
not the rank of its global Selmer space. In particular the relevant
regulator on $P,Q$ remains a two-by-two determinant. A pairing of the
form $c\log_\omega(P_i)\log_\omega(P_j)$ alone would have determinant
zero; CM multiplication does not identify the genuine height with
such a rank-one pairing.

## 3. A fixed sigma function really does give all ordinary heights here

The sources for this step are
[Stein–Wuthrich, published §4.1 and (4.1)](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf),
and [Bannai–Kobayashi, arXiv:math/0610163v4, Example 1.9 and §2](https://arxiv.org/html/math/0610163v4).
They fix the sigma and reduced-theta conventions; no Sha hypothesis
occurs in these constructions.

**[NEW, CM normalization lemma] Lemma 2.** For (1), at every good
split prime $p\ge5$, the Katz weight-two value is exactly
$E_2(E,\omega)=0$. The canonical ordinary $p$-adic sigma function is
therefore the same rational formal sigma function $\sigma_{\rm CM}$,
composed with the formal logarithm. The complex reduced theta for
$\Gamma$ is the same sigma function in its Néron logarithmic
coordinate.

*Proof.* On de Rham cohomology the CM automorphism acts by
$$
[i]^*\omega=i\omega,\qquad [i]^*(x\omega)=-i(x\omega).
$$
At a split prime the automorphism is defined over $\mathbb Q_p$ and
commutes with crystalline Frobenius. The canonical ordinary
unit-root line is stable under this automorphism and complements
the Hodge line $\mathbb Q_p\omega$. Since $i\ne-i$, it must be
$\mathbb Q_p(x\omega)$. In the notation of SW §4.1 its eigenvector
$a\omega+b\eta$ therefore has $a=0$, $b\ne0$; the formula
$E_2=-12a/b$ gives zero. SW's canonical sigma is
$\exp(E_2 z^2/24)\sigma(z)$, so its extra quadratic exponential is one.

For the Frobenius labels, use the F-unit-root prescription in
[Mazur–Stein–Tate, §3.2](https://wstein.org/papers/pheight/pheight.pdf).
Here F acts on $x\omega$ by the unit root $\alpha$, while
$\varphi=F/p$ acts on it by $\beta^{-1}$, where $\beta=p/\alpha$.
The printed reciprocal-root label in SW §4.1 is not an input to this
proof. The full dictionary and its independent check are recorded in
[the derived-unit note, §7](cm-derived-unit-attack.md#7-exact-height-formula-and-the-two-point-projection).

For the complex lattice, $i\Gamma=\Gamma$. Reindexing the absolutely
convergent Eisenstein–Kronecker sum defining the regularized
$e_2^*(\Gamma)$ multiplies it by $-1$; analytic continuation gives
$e_2^*(\Gamma)=0$. BK's reduced theta is
$\theta(z)=\exp(-e_2^*z^2/2)\sigma(z)$, again equal to sigma.
The pullback of $\omega$ is $dz$, fixing the coordinate in both cases.
$\square$

For clarity, this fixed formal function can be constructed over
$\mathbb Q$ without using a transcendental lattice. Let $x(z)$ be
the Laurent expansion determined by
$$
(x'(z))^2=4x(z)^3+156x(z),\qquad x(z)=z^{-2}+O(z^2).
$$
It has rational coefficients, and the CM symmetry forces its regular
terms to have exponents $4n-2$. Writing
$x(z)=z^{-2}+\sum_{n\ge1}b_nz^{4n-2}$, define
$$
\sigma_{\rm CM}(z)=z\exp\!\left(
 -\sum_{n\ge1}\frac{b_nz^{4n}}{(4n)(4n-1)}\right).
\tag{4}
$$
Then $d^2\log\sigma_{\rm CM}/dz^2=-x(z)$,
$\sigma_{\rm CM}(iz)=i\sigma_{\rm CM}(z)$, and its leading term is
$z$. These properties fix its normalization. Its initial terms are
$z+(13/20)z^5+\cdots$. The canonical integral expansion is in the
formal-group parameter $t=-x/y$, after composing with $z=\log_E(t)$;
one must not confuse integrality in $t$ with integrality of the
coefficients in the logarithmic coordinate $z$.

The Mazur–Tate integrality theorem gives
$\sigma_{\rm CM}(\log_E(t))\in t\mathbb Z_p[[t]]^\times$ at the
good split primes in question. This is not a claim of integrality
at inert primes or of coefficients with denominators supported at
one finite set of rational primes.

## 4. A genuine common-theta regulator identity

Let $g_p=\log_p(1+p)$ and use the Iwasawa branch $\log_p p=0$.
For a nonzero rational point $R$ write $e(R)>0$ for the square root
of the denominator of its minimal $x$-coordinate.
Choose a positive integer $m$ carrying $P,Q$ into the formal group
at $p$ and into the identity component at every bad prime. Under
(2), one may take
$$m=8\,\#E(\mathbb F_p),\qquad p\nmid m.$$
The same properties hold for $m(P+Q)$.

Let $K^{\rm col}_0(0,R,1)$ denote the Coleman Eisenstein–Kronecker
function of Bannai–Furusho–Kobayashi, with the same lattice,
differential, and log branch. Its second limit formula is
$$
K^{\rm col}_0(0,R,1)
=-\log_p\theta(R)-\frac1{12}\log_p\Delta_\Gamma.
\tag{5}
$$
Here $\Delta_\Gamma$ is the lattice discriminant in that theorem's
normalization; it is retained, not suppressed as a constant.
Source: [BFK, arXiv:0807.4007v2, Theorem 1.2 and Definition 5.1](https://arxiv.org/html/0807.4007v2).
The theorem holds at good $p\ge5$ for a curve over its CM field and
does not assume Sha finiteness. On the zero residue disc, the
Coleman theta logarithm is the formal theta logarithm itself.

For the three points $R=mP,mQ,m(P+Q)$ define
$$
F_p(R)=\log_p e(R)+K^{\rm col}_0(0,R,1)
                         +\frac1{12}\log_p\Delta_\Gamma.
\tag{6}
$$
Lemmas 2 and (5) identify this **actual value** with
$\log_p(e(R)/\sigma_p(R))$. Put
$$
A_p=m^{-2}F_p(mP),\quad B_p=m^{-2}F_p(mQ),\quad
C_p=m^{-2}F_p(m(P+Q)).
$$

**[NEW, exact regulator tensor identity] Proposition 3.** In the
SW/Banwait height convention,
$$
\boxed{\operatorname{Reg}_p(E/\mathbb Q)
=4A_pB_p-(C_p-A_p-B_p)^2.}
\tag{7}
$$
All three normalized values, and hence the expression, are independent
of the allowed multiplier $m$. No nondegeneracy or Sha-finiteness
hypothesis is needed for (7).

*Proof.* SW (4.1) gives
$\widehat h_p(R)=2F_p(R)$ at the multiplied points. Quadraticity
therefore identifies $2A_p,2B_p,2C_p$ with
$\widehat h_p(P),\widehat h_p(Q),\widehat h_p(P+Q)$ respectively.
Polarization gives
$\langle P,Q\rangle_p=C_p-A_p-B_p$. Taking the determinant on the
full basis $P,Q$ gives (7). The same equalities prove independence
of $m$. $\square$

This can also be expressed directly through the Poincaré section
$$
\Theta(z,w)=\frac{\sigma_{\rm CM}(z+w)}
 {\sigma_{\rm CM}(z)\sigma_{\rm CM}(w)}.
$$
On the formal discs,
$$
m^2\langle P,Q\rangle_p
=\log_p\frac{e(m(P+Q))}{e(mP)e(mQ)}
 -\log_p\Theta(mP,mQ).
\tag{8}
$$
This is an exact logarithm of the same reduced Poincaré theta section
whose torsion translates produce the Katz measure in BK §3.
It is stronger than merely assigning abstract variables the names
of height entries.

The coefficient polynomial
$$D(X,Y,Z)=4XY-(Z-X-Y)^2\in\operatorname{Sym}^2\mathbb Z^3$$
is primitive: its $Z^2$ coefficient is $-1$. Nevertheless (7) does
not assert that the analytic second moment is an element of this
three-generator integral lattice. That missing arithmetic map is
precisely what would be needed before invoking the primitive-tensor
criterion of the coherent-moment note.

## 5. The second moment and the normalized quotient

Fix the Katz measure, central twist $\mu_\psi$, and $p$-adic CM
period $\Omega_p\in\widehat{\mathbb Z_p^{\rm ur}}^\times$ in
Banwait's BK normalization. Let
$$
M_p=\int\ell^2\,d\mu_\psi,\qquad
\ell=\log_p\chi_{\rm cyc},\qquad e_p=(1-\alpha_p^{-1})^2.
$$
The mass and first cyclotomic logarithmic moment vanish by $L(E,1)=0$
and sign $+1$. Expanding the binomial coefficient gives the exact
identity of Banwait Proposition 6.1,
$$c_2(L^{\rm Katz})=M_p/(2g_p^2).$$
His Lemma 3.5, with all character and period choices fixed as above,
gives $L_p=c_{\rm cmp,p}u_p(T)L^{\rm Katz}$, where
$$
u_p(0)=1,\qquad c_{\rm cmp,p}=(156i\Omega_p)^{-1}.
\tag{9}
$$
Here (9) also follows directly from
[BK, Corollary 3.12](https://arxiv.org/html/math/0610163v4#S3.SS3):
in its notation $\Omega=\Omega_\infty/f_0$ and
$u=\Omega_E/\Omega=156i$, so its comparison gives
$L^{\rm MS}= (156i\Omega_p)^{-1}L^{\rm Katz}$ with compatible
systems of roots of unity. All its hypotheses hold: the fixed
differential is Néron, the reduction is good ordinary, and $156i$
is a $p$-unit under (2). With those compatible systems one may take
$u_p(T)=1$. Replacing a compatible system by its $a$th powers,
$a\in\mathbb Z_p^\times$, changes the Gauss sum by a character
value and hence changes the cyclotomic measure by a group element.
Its power series has constant term one. Equality on all finite
characters determines the bounded cyclotomic measure: finite Fourier
inversion determines its mass on every finite quotient. This explains
the exact constant in (9), rather than leaving an unspecified unit.

Since both lower coefficients vanish, only this specified constant
term affects the second coefficient. The multiplier $e_p$ is a
unit under (2), but its value must still be retained in an exact
identity.

For (1), $t_E^2/\prod c_v=1/2$. Thus
$\widetilde c_2=c_2/(2e_p)$ and
$\operatorname{Reg}_\gamma=\operatorname{Reg}_p/g_p^2$.
Whenever the regulator is nonzero, (7)–(9) prove
$$
\boxed{
\frac{\widetilde c_2(p)}{\operatorname{Reg}_\gamma}
=\frac{c_{\rm cmp,p}M_p}
 {4e_pD(A_p,B_p,C_p)}.}
\tag{10}
$$
In particular the two powers of the cyclotomic logarithm cancel
exactly. This quotient permits nonunit regulators. It is not made
equal to a Sha order by definition. Rubin plus Schneider identifies
its **valuation** with the primary Sha order under the finiteness
and nondegeneracy conditions recorded in Banwait Proposition 4.1;
that is not an exact cross-prime or complex comparison. The displayed
primary-form equality in the preprint must likewise be read with
its stated unit qualification, not as an exact replacement of the
full Sha order by its primary part.

## 6. A precision lift that does not lose a nonunit regulator

The weight-$2p-1$ criterion in Banwait concerns the reduction of
$M_p/p^2$ modulo $p$. It is insufficient to recover the quotient
(10) modulo $p$ when $v_p(\operatorname{Reg}_p)>2$.
Here is a proved next step, rather than an appeal to global mu=0.

**[NEW, higher-precision moment identity] Proposition 4.** For local
units $x,y\in\mathbb Z_p^\times$, $p\ge5$, put
$d=p-1$, $X=x^d$, $Y=y^{-d}$. Then uniformly in $x,y$,
$$
(\log_px+\log_py)^2
\equiv\frac{(X-Y)^2(3-X-Y)}{(p-1)^2}\pmod{p^4}.
\tag{11}
$$
Consequently, writing $N(k,l)=\int x^ky^{-l}\,d\mu_\psi$, with the
global character coordinates $x=\widehat\psi$ and
$y=\widehat{\bar\psi}$, whose product is $\chi_{\rm cyc}$,
$$
\begin{aligned}
M_p\equiv\frac1{(p-1)^2}\big(&3N(2d,0)-6N(d,d)+3N(0,2d)\\
&-N(3d,0)+N(2d,d)+N(d,2d)-N(0,3d)\big)
\pmod{p^4W}.
\end{aligned}
\tag{12}
$$

*Proof.* Put $a=X-1$, $b=Y-1$, both in $p\mathbb Z_p$.
The logarithm series gives
$$
(p-1)(\log_px+\log_py)
=a-b-\tfrac12(a^2-b^2)+O(p^3).
$$
The error is uniform: every omitted term has valuation at least
three, including indices divisible by $p$, since $j-v_p(j)\ge3$
for $j\ge3$ and $p\ge5$. Squaring gives
$(a-b)^2-(a-b)(a^2-b^2)$ modulo $p^4$; the squared quadratic
term and the product with the error are in $p^4$.
This is $(X-Y)^2(3-X-Y)$. Division by the unit $(p-1)^2$ proves
(11). The measure is $W$-valued, so integration preserves this
uniform congruence. Expanding the polynomial gives (12). $\square$

The exact polynomial moments in (12) retain all the factors in
Banwait Lemma 6.5(2). The independent derivation below verifies the
restricted formula directly from BK and fixes its coordinate meaning:
$$
N(k,l)=\Omega_p^{k+l+1}\mathcal E(k,l)(-1)^{k+l}
 k!(\mathrm N\mathfrak f)^l\,\mathcal P_{l,k+1},
\tag{13}
$$
where the class sums $\mathcal P$ are the source's $P_{a,b}$ and
$$
\mathcal E(k,l)=
\left(1-\frac{\pi^{k+l+1}}{p^{l+1}}\right)
\left(1-\frac{\pi^{k+l+1}}{p^{k+1}}\right),
\qquad \pi=\psi_E(\mathfrak p).
$$
The three degree-two terms have weight $2p-1$ and period power
$\Omega_p^{2p-1}$; the four new terms have weight $3p-2$ and power
$\Omega_p^{3p-2}$. These different period powers, the factorials,
and the individual Euler factors cannot be stripped off as units
inside the sum. Equation (12) is a precise higher-precision moment
formula; it does not automatically become a single algebraic number
of a fixed weight independent of $p$.

If $v_p(\operatorname{Reg}_p)=3$, an error in $p^4W$ becomes an
error in $pW$ after division by that regulator, so (12) is the
precision needed to study (10) modulo $p$. An error only in $p^3W$
would give no such information. More generally valuation $s$ in
the regulator requires numerator precision at least $p^{s+1}$.
This explicitly accommodates the regulator nonunits rather than
declaring them exceptions to the proposed common-tensor mechanism.

### 6.1. Independent audit of the restricted moments

The separate [source reconstruction and nonzero low-moment checks](cm-moment-source-check.md)
passed coordinator review and independently verify the normalization below.

This calculation uses [BK, §§3.1–3.3](https://arxiv.org/html/math/0610163v4#S3)
in version math/0610163v4, specifically the integral measure construction,
the two unit projectors, the distribution formula, and the definitions
of the partial Katz measures. It does not use the compressed formula
in Proposition 3.13. Write $F=\mathrm N\mathfrak f$ and
$\Omega=\Omega_\infty/f_0$, so $\Gamma=\mathfrak f\Omega$.

**Pole removal.** Here the second theta parameter is zero. Therefore
BK Proposition 3.3, which excludes a zero parameter, is not an
unrestricted moment formula available to us. The integral construction
subtracts the pole in the formal parameter; subtracting it in the
elliptic logarithm need not give the same power series. We instead
apply both unit projectors to the integral measure. The difference
between those two pole subtractions depends only on the second
variable. The first projector $1-A_1$, where $A_1$ averages first-leg
$p$-torsion translations, kills it identically. A correction depending
only on the first variable is similarly killed by $1-A_2$.
Thus the restricted transform is computed using the four full Laurent
theta functions, with every polar correction cancelled. This is also
the explicit cancellation in BK Lemma 3.4. No assertion that the
unrestricted logarithm-subtracted transform is integral is needed.

**The exact character transfer.** Fix a fractional ideal
$\mathfrak a$ prime to $\mathfrak fp$, put $q=\psi(\mathfrak a)$,
and choose $\alpha_0\in\mathfrak a^{-1}$ with
$\alpha_0\equiv1\pmod{\mathfrak f}$. Because this CM curve and
its differential descend to $K$, the isogeny differential factor
in BK §3.3 is $\Lambda(\mathfrak a)=q$, the conjugate lattice is
$\Gamma$, and
$$q\bar q=\mathrm N\mathfrak a,\qquad
\Omega_p^{\sigma_{\mathfrak a}}=\frac{q}{\mathrm N\mathfrak a}\Omega_p.
$$
Set $z_{\mathfrak a}=q\alpha_0\Omega$. The definition of BK's
$\widetilde\mu$ on $\mathfrak a^{-1}\Gamma$, followed by restriction
to both units, is therefore $q$ times the pushforward of the
fixed-lattice measure $\mu_{z_{\mathfrak a},0}^{\times}(u,v;\Gamma)$
by
$$ (u,v)\longmapsto(X,Y)=(qu,Fv/\bar q). \tag{13a} $$
Indeed the two logarithmic arguments in that definition are
$\Omega_p^{\sigma_{\mathfrak a}}\mathrm N\mathfrak a\log(1+S)$
and $\Omega_p^{\sigma_{\mathfrak a}}F\log(1+T)$, with prefactor $q$.
They equal $q\Omega_p\log(1+S)$ and
$F\Omega_p\log(1+T)/\bar q$. Any formal polar discrepancy is
annihilated as just proved. All the pushforward multipliers are
$p$-units.

For a continuous function $H$ of the global coordinates $x,y$, the
central twist on the partial ideal class $\mathfrak a^{-1}$ has
local integrand
$$q^{-1}X\,H(q^{-1}X,\bar q^{-1}Y^{-1}).$$
BK Definition 3.8 multiplies it by $\Omega_pX^{-1}$ and Definition
3.9 sums the partial classes. Substitution of (13a) gives exactly
$$\Omega_p\,H(u,(Fv)^{-1})$$
against $\mu_{z_{\mathfrak a},0}^{\times}$: the prefactor $q$,
the ideal-character factor $q^{-1}$, and $X/X$ all cancel. In
particular, for $H(x,y)=x^ky^{-l}$ the remaining factor is
$\Omega_p u^k(Fv)^l$. Equivalently, evaluating
$\varphi=\psi^{k+1}\bar\psi^{-l}$ gives the scalar cancellation
$$\varphi(\mathfrak a)^{-1}q^{k+1}\bar q^{-l}=1. \tag{13b}$$
This verifies the finite character as well as the infinite-type shift;
it does not merely suppress the finite character under the word
“twist.” It also proves equality of the pushforward measures, not
only their critical moments.

Inversion permutes the ray classes in this sum. If $\mathfrak a=(g)$,
put $z_g=\varepsilon(g)g\Omega$; then
$z_{\mathfrak a}\equiv z_g\pmod\Gamma$.
Changing $g$ to $ug$, $u\in\mathbb Z[i]^\times$, leaves this parameter
unchanged because $\varepsilon(u)=u^{-1}$. Thus the sum is over
$D_E=(\mathcal O_K/\mathfrak f)^\times/\mathcal O_K^\times$,
once per ray class. There is no extra factor four. This uses the
ray-class definition of the Katz sum directly, not an unnormalized
sum over all residue units. In particular, the second display of BK
Definition 3.6, if read literally as a sum over every residue unit,
repeats each term four times for this curve. That display is not an
input to this proof. Likewise we do not use the displayed period
power in BK Theorem 3.7: the derivatives above determine it directly.

**The two Euler factors.** Put $\pi=\psi(\mathfrak p)$,
so $\pi\bar\pi=p$. Choose $\epsilon$ by the Chinese remainder theorem
with $\epsilon\equiv1\pmod{\mathfrak f\mathfrak p}$ and
$\epsilon\equiv0\pmod{\bar{\mathfrak p}}$. Put
$\beta=\epsilon/\bar\pi\in\mathcal O_K$. In the four terms of
BK Proposition 3.5, homogeneity
$$\Theta_{a z_0,0}(az,aw;a\Gamma)=a^{-1}\Theta_{z_0,0}(z,w;\Gamma)$$
returns the three averaged terms to $\Gamma$. On the coefficient
$z^kw^l$ their factors and class parameters are
$$
\begin{array}{c|c}
\text{factor}&\text{parameter in }\mathbb C/\Gamma\\ \hline
\pi^k/\bar\pi^{l+1}&\pi z_g\\
\pi^l/\bar\pi^{k+1}&\beta z_g\\
\pi^{k+l}/\bar\pi^{k+l+2}&\pi\beta z_g.
\end{array}
\tag{13c}
$$
The $+1$ shifts come from the homogeneity factor $\bar\pi^{-1}$.
Since $\beta\equiv\bar\pi^{-1}\pmod{\mathfrak f}$, these are the
ray-class permutations $\mathfrak p$, $\bar{\mathfrak p}^{-1}$,
and their product. Here $\varepsilon(\pi)=\varepsilon(\bar\pi)=1$,
because $\psi((\pi))=\pi$ and $\psi((\bar\pi))=\bar\pi$;
hence also $\varepsilon(\beta)=1$. Retaining $\beta$ is necessary:
the literal complex number $z_g/\bar\pi$ need not be
$\mathfrak f$-torsion and cannot replace that inverse ray-class action.
The double factor in (13c) is the product of the first two.
Summing classes therefore gives
$$
\left(1-\frac{\pi^k}{\bar\pi^{l+1}}\right)
\left(1-\frac{\pi^l}{\bar\pi^{k+1}}\right)=\mathcal E(k,l).
$$
Finally the regular Laurent coefficient is
$(-1)^{k+l}F^l r_{l,k+1}([g])/l!$; the two logarithmic derivatives
contribute $\Omega_p^{k+l}k!l!$. Multiplication by the additional
$\Omega_p$ in (13b) proves (13), with every sign, factorial and
period power retained. The derivation applies to every $k,l\ge0$;
it uses the theta generating series, not a critical-range inequality.
It repairs the pole-removal ambiguity without altering (11)–(12),
whose proof was already independent of the theta formula.

## 7. Attempted arithmetic identification and its first remaining identity

The construction now has two actual operations on one CM theta
object: torsion translations and logarithmic cyclotomic moments
produce $M_p$, while non-torsion evaluations with denominator
corrections produce the determinant $D(A_p,B_p,C_p)$. The following
attempt tests whether CM multiplication or theta addition supplies
their comparison.

The sigma addition law, with these normalizations, is
$$
\frac{\sigma(z+w)\sigma(z-w)}{\sigma(z)^2\sigma(w)^2}
=\wp(w)-\wp(z).
\tag{14}
$$
It is the identity used in BFK Proposition 2.8; it also follows by
comparing divisors, poles and the leading Laurent coefficient.
For rational points the right side is algebraic, and differentiating
it gives the familiar rational addition formulas for zeta and
Weierstrass functions. Equation (14) establishes relations among
the three theta values in (7) and an additional value at $P-Q$.
It does not change their non-torsion arguments into the
$\mathfrak f$-division arguments in the Katz class sum.

More explicitly, if $z_P$ is a logarithm of a rational non-torsion
point, the addition law yields
$$
\zeta(z+z_P)-\zeta(z)-\zeta(z_P)
=\frac12\frac{\wp'(z)-\wp'(z_P)}{\wp(z)-\wp(z_P)}.
\tag{15}
$$
The right side is a rational function on the curve with algebraic
coefficients. The extra evaluation $\zeta(z_P)$ on the left is
not supplied by that rational function. The CM relation merely
relates it to the evaluation at $[i]P$; it does not identify it
with a torsion class sum or with the corresponding evaluation at
the independent point $Q$.

BK's algebraicity of translated reduced theta applies to torsion
translations (Theorem 2.9 and Corollary 2.10); that hypothesis fails
for $P,Q$. The precise polylogarithm source is
[Bannai–Kobayashi–Tsuji, arXiv:0711.1701v2](https://arxiv.org/html/0711.1701v2).
Its Theorem 4.15 constructs the full $p$-adic polylogarithm sheaf,
and its Theorem A.19 describes the real Hodge realization at any
nonzero complex point. Thus non-torsion realizations are not being
declared nonexistent. However the explicit syntomic specialization
in Theorem 4.23 assumes a nonzero torsion point of order prime to
$\mathfrak p$, and uses the splitting principle of Lemma 4.20.
These statements do not identify the determinant of two independent
rational-point heights with the torsion moment. Exact knowledge of the generating
theta function still determines its analytic evaluations; the
failure here is the missing arithmetic identity between the two
specified operations, not nonuniqueness of the analytic function.

To state that identity without suppressing normalizations, let
$$
n_E=\frac{(L''(E,1)/2)\,t_E^2}
 {\Omega_E\operatorname{Reg}_\infty\prod_vc_v}
=\frac{L''(E,1)/2}{2\Omega_E\operatorname{Reg}_\infty},
$$
where the real regulator is on the same full basis and in the BSD
height convention. No abstract embedding of this real number into
$\mathbb C_p$ is used in the arithmetic target below.

**[GAP CM-Theta, exact remaining comparison].** For the fixed curve
(1), first prove the rationality statement
$$n_E\in\mathbb Q.$$
Then, using the canonical inclusion $\mathbb Q\hookrightarrow\mathbb Q_p$,
prove for every split prime satisfying (2) the identity
$$
\boxed{c_{\rm cmp,p}M_p
=4e_p\,n_E\,D(A_p,B_p,C_p).}
\tag{16}
$$
In particular construct a common rational tensor, and its integral
lattice and evaluation maps, that
identifies the torsion second moment on the left with this actual
non-torsion height tensor on the right, independently of declaring
its scalar to be $n_E$. Where the regulator is nonzero, (16) is
equivalent to (10) having that canonically realized rational value
$n_E$. An identity using an arbitrarily chosen embedding of a real
number into $\mathbb C_p$ would not prove this rationality premise
and is not the target asserted here. If the
regulator is zero, (16) remains a defined tensor-valued comparison
but cannot be divided to establish a quotient or Sha finiteness.

**[CONDITIONAL, consequence of the proposed identity]** If (16) is
proved at a prime satisfying (2) and the regulator there is nonzero,
then primary Sha finiteness follows, rather than being a hidden
premise. Indeed the certified complex leading coefficient is nonzero,
so $n_E\ne0$ and (16) makes $M_p\ne0$. Thus $c_2(p)\ne0$ and
$\operatorname{ord}_T L_p=2$. Rubin's CM main conjecture identifies
this with the characteristic-series order, and the rank-two equality
case of Schneider's theorem gives finite $\Sha[p^\infty]$.
Nondegeneracy at every prime and coverage of inert or bad primes
would still be separate obligations. Equality of the evaluated
quotients alone also does not replace the requested global integral
tensor and its real realization.

The proposed derivation through CM multiplication succeeded in
fixing the sigma normalization and in proving (7)–(8). The proposed
derivation through addition/distribution laws reached (14)–(15),
which preserve the distinction between torsion moment data and
independent rational-point evaluations. The precision improvement
(11)–(13) repairs a real loss of information in the unit criterion,
but remains prime-dependent and does not supply (16).

Thus no common integral **analytic** tensor proportional to the
regulator tensor has been constructed. Calling the fixed generating
theta function integral or primitive, or invoking its mu-invariant,
does not establish (16). Nor is Sha finiteness assumed in
Lemmas 1–2, Proposition 3 or Proposition 4. The remaining comparison,
real-period realization, rank nondegeneracy and coverage of other
primes must all remain explicit in any later BSD deduction.

## 8. Reproducible arithmetic checks and continuation

The exact basis check used the existing runtime, without creating
a new prime table:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python - <<'PY'
from sage.all import EllipticCurve
from sage.libs.eclib.all import mwrank_MordellWeil
E = EllipticCurve([0,0,0,39,0])
mw = mwrank_MordellWeil(E.mwrank_curve(), verbose=False)
mw.process([[3,12,1],[27,144,1]], saturation_bound=0)
print(E.pari_curve().ellrank())
print(mw.saturate(max_prime=-1, min_prime=2), mw.rank())
print(E.conductor(), E.torsion_order(), E.tamagawa_product(), E.root_number())
PY
```

It returned the values in §1. An optional finite-precision
$E_2$ check returned $O(5^8)$; it is not the proof of exact vanishing
in Lemma 2. The corresponding sigma print was not used. This note
does not promote the source's approximate “analytic Sha” number to
an exact value.

The independent analytic-order certificate uses the existing proved
Mellin algorithm with the equation supplied explicitly, because this
label is absent from the installed small Cremona database:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python - <<'PY'
import compute.scripts.certify_mellin as m
from sage.all import EllipticCurve
E = EllipticCurve([0,0,0,39,0])
m.EllipticCurve = lambda unused_label: E
result = m.certify('CM-39', 96, 40)
print(result['completed_derivative_rational_endpoints'])
print(result['L_leading_rational_endpoints'])
PY
```

The constructor replacement is local to this process; no source file
is modified. The resulting enclosure is
$$
\frac{2679924907651496904488990337}{309485009821345068724781056}
\le\frac{L''(E,1)}2\le
\frac{2679924907662402912040072833}{309485009821345068724781056},
$$
approximately $8.6593044012\pm3.56\cdot10^{-11}$. Exact descent
rank two excludes analytic ranks zero and one by Gross–Zagier–Kolyvagin;
the nonzero second derivative supplies the upper bound two. The
[Mellin proof](analytic-rank-certificates.md) supplies the normalization
and both infinite tails uniformly for this call as well.

The coordinator independently reconstructed all coefficients through
1405 by finite-field point counts and Hecke recurrences, including
the additive factors at 2, 3 and 13. The standalone reproducer
[certify_cm39.py](../../compute/scripts/certify_cm39.py) then ran at
112 bits, cutoff 48 and Fourier cutoff 1686. Its
[full certificate](../../compute/data/cm39_analytic_rank_certificate.json)
gives $L''(E,1)/2=8.6593044012179\pm4.60\cdot10^{-14}$ as an
enclosure, strictly inside the preceding exact interval. The
[review](review-cm-regulator-tensor.md) records this separate PASS
and the proof scope. Neither enclosure proves leading-term rationality.

The next arithmetic action is to construct a relation in the
Poincaré-biextension or elliptic-polylogarithm realization that turns
the torsion moment functional into the full determinant in (7),
including the fixed CM and Néron periods of (9)–(10). Repeating a
unit scan or only proving nonvanishing of the whole measure would
not address that relation.
