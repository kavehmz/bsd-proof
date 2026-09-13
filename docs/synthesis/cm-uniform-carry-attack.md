# Actual finite CM moments and the point-height index

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Status: bounded construction completed with a
[full independent PASS review](review-cm-uniform-carry.md).
Reviewed mathematical version:
6faa3fc9826eb23610c719fb83818d8c5464d4c1d21eb17bed754e2f3f366faa.
Completion links are editorial; the reviewed mathematics is unchanged.
This continues the completed [coefficient certificate](cm-derivative-nonvanishing-attack.md),
its [full review](review-cm-derivative-nonvanishing.md), and its
[integral-bound audit](review-cm-derivative-integral-bound.md).
The objective remains full BSD over Q. No certificate is rerun here.

The new result is an exact integral index formula retaining the actual
point-Bockstein determinant, together with a finite arithmetic construction
of that determinant. It sharpens the previous coefficient-only bound when
the quadratic coefficient has valuation greater than one. It proves
neither uniform nonvanishing nor a common rational BSD frame.

## 1. Actual input, including every normalization

Fix
\[
 E:y^2=x^3+39x,\quad \omega=dx/(2y),\quad
 P=(3,12),\quad Q=(27,144),\quad P+Q=(1/4,25/8).
\]
The displayed P,Q are a FULL basis modulo the rational two-torsion.
The conductor is48672, the finite Tamagawa product is8, and the
algebraic and analytic ranks are exactly two. These are the previously
reviewed arithmetic and [analytic inputs](../../compute/data/cm39_analytic_rank_certificate.json).
Throughout this note
\[
 p\ge5,\qquad p\equiv1\pmod4,\qquad p\nmid 2\cdot3\cdot13.       \tag{1}
\]
All such primes are ordinary and nonanomalous for this E. Write
\[
 N_p=\#E(\mathbf F_p),\quad
 \alpha^2-a_p\alpha+p=0,\quad \alpha\in\mathbf Z_p^\times,\quad
 \beta=p/\alpha,\quad g_p=\log_p(1+p),\quad
 e_p=(1-\alpha^{-1})^2.
\]
Here p does not divide N_p, so e_p is a unit. Set T=gamma−1 with
chi_cyc(gamma)=1+p and use log_p(p)=0.

The Néron modular symbol and its actual bounded measure are
\[
 m(r)=\Omega_E^{-1}\Re\left(2\pi i\int_{i\infty}^r f(z)\,dz\right),
\quad
 \mu_p(a+p^n\mathbf Z_p)
 =\alpha^{-n}m(a/p^n)-\alpha^{-(n+1)}m(a/p^{n-1}).              \tag{2}
\]
The minimal parametrization has Manin constant1. Every cusp a/p^n
with p not dividing a is equivalent to0, whose image is O because
L(E,1)=0. Thus m(a/p^n) is in (1/2)Z at ALL levels. In particular
(2) is integral, without assuming integrality from finite samples.
The primary Manin/period input and complete proof are in
[the predecessor, §§2–3](cm-derivative-nonvanishing-attack.md).
The pushforward measure under
t(x)=log_p<x>/g_p gives precisely the fixed MTT series
\[
 L_p(E,T)=\int_{\mathbf Z_p^\times}(1+T)^{t(x)}\,d\mu_p(x),
 \qquad c_{2,p}=[T^2]L_p(E,T).                               \tag{3}
\]
There is no division by p−1 in this pushforward.

This is the realization of the SAME normalized two-variable theta-unit
class in the [actual Iwasawa presentation](cm-iwasawa-presentation-attack.md).
For reference, K=Q(i), f_0=39(1+i)^3, Omega_infinity=(1+i)Omega_E/2,
and c_cmp,p=(156i Omega_p)^(-1). The tame norm is UNNORMALIZED:
its degree is1152(p−1)^2, a p-unit. Before twisting, the tame character
is rho^(-1), where rho=(Psi^c)^(-1); after twisting it is trivial.
The coefficient is 2pr_rho(gamma_E^+). The actual smoothing factor is
\[
 q_a(X,Y)=12\bigl(a^2-u_a(1+X)^{\lambda_a}(1+Y)^{\lambda_a}\bigr),
 \quad u_a=\Psi^c((a)),\quad \lambda_a=\log_p(a)/g_p,            \tag{4}
\]
with a=5 except a=7 at p=5. It is a unit in the specified branch.
The theta twelfth power, N(a)−sigma_a sign and period scalar remain
unchanged. X,Y map to T by a QUOTIENT; this is not restriction to
the diagonal subgroup, and gives no factor1/2. Finite coefficient
p^m jets use ray exponents at least m+1.

Let R_p=Z_p[[X,Y]]. The reviewed genuine Selmer presentation is
\[
 C_{f,p}=[R_p^d\xrightarrow{\mathcal A(X,Y)}R_p^d]
 \quad\hbox{in degrees1,2},\qquad d=b+1.
\]
Its fixed cofactor convention and normalized unit determinant give
\[
 F=(-1)^b u\det\mathcal A,\quad u\in R_p^\times,\qquad
 F\in(X,Y)^2,\qquad
 c_{2,p}=\iota_p(F_{20}+F_{11}+F_{02}),\quad
 \iota_p\in\mathbf Z_p^\times.                              \tag{5}
\]
The last statement uses the actual Rubin derivative; it does not
assert a bounded Coleman power series on an arbitrary local generator.
In particular
\[
 c_{2,p}=(-1)^b\iota_pu(0)[T^2]\det\mathcal A(T,T).             \tag{6}
\]
No unit in (4)–(6) is reset to1. Derived base change, the presentation's
Tor groups and its possible nonunimodular global kernel vector remain
as in that proof. Freeness does not imply augmentation divisibility.

The Frobenius convention remains: absolute F acts on omega by beta
and on x omega by alpha; phi=F/p acts by alpha^(-1), beta^(-1)
respectively. The ordinary complementary vector nu lies on x omega,
with [omega,nu]=1. Thus
\[
 k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1}),\quad
 \delta_0=k_\alpha^{-1}\nu,\quad k_\alpha e_p=N_p/p.
\]
The inconsistent reciprocal-root label printed in SW§4.1 is not used.

## 2. The finite moment is an actual integral augmentation class

For n≥2 put G_n=(1+pZ_p)/(1+p^nZ_p), let gamma be its indicated
generator, set R_n=Z_p[G_n], and J_n=(gamma−1). Define
\[
 \Theta_{n,p}=
 \sum_{a=1}^{p-1}\sum_{j=0}^{p^{n-1}-1}
 \mu_p\bigl(\omega_p(a)(1+p)^j+p^n\mathbf Z_p\bigr)\gamma^j.
                                                               \tag{7}
\]
Here omega_p(a) means the Teichmüller residue at the precision used.
This is an ACTUAL integral finite distribution, compatible under
G_{n+1}→G_n by the exact Hecke norm relation in (2).
It is the image of (3), not a conjectural integral series.

**[NEW deduction] Proposition 2.1.** There are canonical isomorphisms
\[
 J_n/J_n^2\simeq\mathbf Z/p^{n-1},\qquad
 J_n^2/J_n^3\simeq\mathbf Z/p^{n-1},                           \tag{8}
\]
using gamma−1 and (gamma−1)^2. Moreover Theta_(n,p) belongs to
J_n^2, and its coordinate in the second quotient is c_(2,p)
modulo p^(n−1).

*Proof.* Put q=p^(n−1). The integral group ring is
Z_p[T]/((1+T)^q−1). Modulo T^3 its relation is
qT+binom(q,2)T^2; multiplication by T also gives qT^2=0.
Because p is odd, binom(q,2)=q(q−1)/2, so subtracting its
appropriate multiple of the latter relation leaves qT=0.
This proves (8), including absence of any smaller annihilator.
The genuine series (3) has zero constant and linear coefficients,
as proved in the derived-unit construction. Its image (7) therefore
lies in J_n^2 and has the asserted quadratic coordinate. ∎

A representative finite coefficient is
\[
 M_{n,p}:=\sum_{a,j}\binom j2
 \mu_p\bigl(\omega_p(a)(1+p)^j+p^n\mathbf Z_p\bigr)
 =\alpha^{-n}(A_{n,p}-\alpha^{-1}B_{n,p}),                    \tag{9}
\]
where A and B are the sums using the two modular symbols in (2).
On each residue class t(x)−j belongs to p^(n−1)Z_p, and
\[
 \binom{t(x)}2-\binom j2
   =(t(x)-j)(t(x)+j-1)/2.
\]
Consequently
\[
                         c_{2,p}-M_{n,p}\in p^{n-1}\mathbf Z_p. \tag{10}
\]
This independently describes the error and the finite augmentation
coordinate. It is not an exact lift from R_n to a rational group ring.

At levels2 and3 the ACTUAL carry formula is
\[
 c_{2,p}\equiv\alpha^{-2}A_{2,p}+\frac{p}{2\alpha^3}C_p
                    \pmod{p^2},                            \tag{11}
\]
\[
 \begin{split}
 A_{2,p}&=\sum_{a=1}^{p-1}\sum_{r=0}^{p-1}
       \binom r2\,m(\omega_p(a)(1+p)^r/p^2),\\
 C_p&=\sum_{a=1}^{p-1}\sum_{r,t=0}^{p-1}
       t(2r-1)m(\omega_p(a)(1+p)^{r+pt}/p^3).
 \end{split}
\]
Indeed j=r+pt gives the difference of weights
pt(2r−1)/2+p²t²/2. Summing children gives the level2
term; summing t kills the lower-symbol correction modulo p.
Finally B_(2,p)=binom(p,3)sum_a m(a/p)=0, since the latter
sum is (a_p−2)m(0). This derives (11), retaining its carry.
The already certified p=5 values give5+15=20 modulo25;
nothing has been recomputed.

The path from infinity to each cusp in these sums also has a genuine
Betti interpretation: its image under the fixed parametrization is
a closed integral loop on E. Adding its conjugate produces real
period 2Omega_E m(r), an integral multiple of the primitive real
period. Thus the finite symbols come from actual modular paths.
This does not turn their integral augmentation coordinate into a
rational point on E or identify a marked-point height.

## 3. Integral self-duality and the actual point Bockstein

At the augmentation, use the exact integral Shapiro identification
with the ordinary Selmer complex C_0=C_f(T_pE) over Q. Its local
condition at p is the saturated rank-one ordinary coefficient T^+;
at the bad places it can be represented by the zero local complex.

**[NEW deduction] Lemma 3.1.** The canonical principal polarization
and compatible local cup products give an integral quasi-isomorphism
\[
 C_0\simeq R\operatorname{Hom}_{\mathbf Z_p}
                      (C_0,\mathbf Z_p)[-3].
\]
The resulting edge map induces an isomorphism
\[
 {\cal D}:H^2(C_0)_{\rm tf}
           \ \xrightarrow{\ \sim\ }\
               \operatorname{Hom}_{\mathbf Z_p}(H^1(C_0),\mathbf Z_p).
                                                               \tag{12}
\]
No Sha-finiteness assumption occurs.

*Proof.* The Weil pairing is perfect on T_pE. Its ordinary line is
primitive and isotropic, and T/T^+ is the integral Tate dual of T^+.
Thus the ordinary local conditions are orthogonal as COMPLEXES.
At each bad place, the nontrivial CM inertia character survives
modulo p; the actual local complexes are acyclic, as checked in
the [local-condition proof](cm-ray-local-conditions-attack.md)
and predecessor integral audit. Consequently their duality error
complexes are also acyclic. There are no odd-p real Tate terms.

Apply [Nekovář, Theorem6.3.4 and Proposition6.7.6](https://www.numdam.org/item/AST_2006__310__R1_0.pdf)
with R=Z_p, dualizing complex Z_p, and the polarization.
The hypotheses here are finite free coefficients, finite cohomology,
and the just verified integral local orthogonality; there is no
general integral-unramified-duality assumption at a bad Tamagawa
prime. This gives the stated quasi-isomorphism.

The actual perfect C_0 has cohomology only in degrees1,2. Over the
DVR Z_p its universal-coefficient edge sequence is
\[
 0\longrightarrow\operatorname{Ext}^1_{\mathbf Z_p}
                  (H^2(C_0),\mathbf Z_p)
 \longrightarrow H^2(C_0)
 \longrightarrow\operatorname{Hom}_{\mathbf Z_p}
                  (H^1(C_0),\mathbf Z_p)\longrightarrow0.    \tag{13}
\]
This is the specialization of Nekovář6.3.5; it also follows directly
by dualizing any two-term free model. The Ext term is finite, and
the target is free, so the kernel is exactly all torsion in H².
Quotienting it out proves (12). It has not been discarded or
assumed zero. ∎

Define the INTEGRAL height Bockstein beta to be minus the connecting
map for the actual inverse cyclotomic coefficient deformation.
On a global one-cocycle f the natural connecting cochain is
−c_gamma(g)g f(h)T, where c_gamma=log_p chi_cyc/g_p.
Pair beta through (12), and take the T-coordinate. This defines
\[
 B_p(x,y)={\cal D}(\beta(y)/T)(x)\in\mathbf Z_p
       \quad (x,y\in H^1(C_0)).                             \tag{14}
\]
It is symmetric; the minus connecting sign and the alternating
polarization are the conventions of
[BKS§5.1.1](https://arxiv.org/pdf/1910.07404), or directly
Nekovář§11.2. Write bold B_p for its2×2 matrix on P,Q.

The point lattice is defined even before Sha finiteness. Indeed
\[
 0\longrightarrow E(\mathbf Q)^{\wedge}_p
 \longrightarrow H^1(C_0)
 \longrightarrow T_p\operatorname{Sha}(E/\mathbf Q)
 \longrightarrow0.
\]
The right term is torsion-free: an element of the inverse limit
killed by p has every coordinate zero by compatibility with the
next coordinate. Hence the point lattice is saturated. It is not
thereby all of H¹. At finite level there is still
\[
 0\longrightarrow H^1(C_0)/p^m
 \longrightarrow H^1(C_0\otimes^{\mathbf L}\mathbf Z/p^m)
 \longrightarrow H^2(C_0)[p^m]\longrightarrow0.              \tag{15}
\]
Thus computing the point matrix does not silently discard the
extra finite Selmer classes supplied by Tor.

## 4. The sharp index equality

**[NEW deduction] Theorem 4.1.** Suppose c_(2,p)≠0. Then the full
primary Sha is finite, bold B_p is nonsingular, and
\[
 \boxed{\ (c_{2,p})=
  \operatorname{Fitt}_{\mathbf Z_p}^0(\operatorname{Sha}[p^\infty])
            \,(\det\boldsymbol B_p)\ }.                     \tag{16}
\]
In particular
\[
 v_p\#\operatorname{Sha}[p^\infty]
       =v_p(c_{2,p})-v_p(\det\boldsymbol B_p)\ge0.             \tag{17}
\]
This is an equality of ACTUAL integral indices, not an assertion
that two exact scalars differ by1.

*Proof.* The existing height identity with the actual unit derivative is
\[
 h_\Gamma(x,w_0\otimes T)
       =k_\alpha\log_\omega(x)c_{2,p}T^2.
\]
Take the non-torsion rational point P, whose local logarithm is
nonzero. Thus w_0 is nonzero. The actual presentation's cofactor
criterion then gives full Selmer corank two. Consequently
Sha[p^\infty] is finite, and H¹(C_0) is precisely the full point
completion. These are the reviewed corank and coefficient-sequence
arguments, not hypotheses. The same coefficient sequence, with
H⁰((V/T)^−)=0 at this nonanomalous p, gives
\[
                  H^2(C_0)_{\rm tors}\simeq\operatorname{Sha}[p^\infty].
                                                               \tag{18}
\]
It is the full primary group, not just a divisible quotient.

Choose integral U,V in GL_d(Z_p) putting the constant differential
into Smith form
\[
 U\mathcal A(0)V=\operatorname{diag}(p^{a_1},\ldots,
                               p^{a_{d-2}},0,0).
\]
Set s=sum a_i. Equation (18) gives #Sha[p^\infty]=p^s.
Let D be the lower-right2×2 block of the coefficient of T in
U A(T,T)V. Then
\[
 [T^2]\det\mathcal A(T,T)
  =(\det U\det V)^{-1}p^s\det D.                            \tag{19}
\]
Every contributing term of order two must use all d−2 nonzero
constant Smith entries and exactly the indicated two linear
entries. Terms using an off-block linear entry require at least
three T-factors. No nonunit Smith factor is inverted.

The last two columns of V give a basis k of ker A(0); the last
two columns of U^(-1) give a basis q of the free cokernel quotient.
Let C in GL_2(Z_p) express (P,Q)=kC, and let
J_(ij)=Dcal(q_j)(k_i). Equation (12) implies J is in GL_2(Z_p).
The natural Bockstein is D in these frames. Therefore the
MINUS-Bockstein height matrix on P,Q is
\[
                 \boldsymbol B_p=-C^tJD C,\qquad
 \det\boldsymbol B_p=(\det C)^2\det J\det D.                 \tag{20}
\]
Combining (6),(19),(20) gives the exact scalar equation
\[
 c_{2,p}=\varepsilon_p\,p^s\det\boldsymbol B_p,\qquad
 \varepsilon_p=
 \frac{(-1)^b\iota_pu(0)}
      {\det U\det V\,(\det C)^2\det J}
                     \in\mathbf Z_p^\times.                \tag{21}
\]
This displays all frame-change factors. Their individual values
depend on the allowed Smith frames, but their product in (21)
does not. None was chosen to force a numerical ratio. Since c2
is nonzero, det B is nonzero. Equations (16),(17) follow. ∎

The proof needs the previously established all-height-one CM main
conjecture equality for the NORMALIZED elliptic-unit determinant,
including the height-one prime p. Rational Kato divisibility alone
would not replace that equality in (5). The exact primary
Kato15.2(b,c),15.6/Rubin comparison was verified in
[the presentation review](review-cm-iwasawa-presentation.md).
This scope is retained rather than generalized to an arbitrary curve.

**Corollary 4.2.** If a finite moment certificate proves
v_p(c_(2,p))=e and
\[
       \det\boldsymbol B_p\equiv0\pmod{p^{e-1}}\quad(e\ge2),  \tag{22}
\]
then Sha[p^\infty]=0. For e≤1 no additional test is required.

Indeed (17) makes its order exponent at most one under (22).
The finite odd-primary Cassels–Tate pairing is nondegenerate
and alternating, so that exponent is even, hence zero. This is
[Milne I§6, Theorem6.26](https://www.jmilne.org/math/Books/ADTnot.pdf)
with the rational principal polarization; finiteness of OTHER
primary components is not assumed. In general, once e is known,
computing the determinant modulo p^(e+1) determines a unique d≤e,
and the exact order is p^(e−d).

## 5. A finite arithmetic construction of the point matrix

This section makes (22) an actual finite test. It does not assume
a p-adic regulator or import an uncertified floating-point height.

Let
\[
 \Sigma(t)=\sigma_{\rm CM}(\log_E(t))\in t\mathbf Q[[t]],
 \qquad t=-x/y.
\]
The [reviewed CM sigma lemma](cm-regulator-tensor-attack.md#3-a-fixed-sigma-function-really-does-give-all-ordinary-heights-here)
proves that this SAME rational formal series is the canonical
ordinary sigma function at every p in (1), and
\[
                         \Sigma(t)\in t\mathbf Z_p[[t]]^\times.
                                                               \tag{23}
\]
The integrality is in t, not in the elliptic logarithm z.
It follows from the canonical F-unit-root complement x omega
and E_2=0. The primary sigma integrality statement is
[Mazur–Stein–Tate, Theorem1.3 and (1.8)](https://wstein.org/papers/pheight/pheight.pdf);
the linked author version is paginated585–622.

Set n_p=8N_p, a p-unit. It carries P,Q,P+Q into the formal
group at p and the identity component at every bad prime.
For R equal to any of these three points, write
\[
 n_pR=(a_R/d_R^2,b_R/d_R^3),\quad d_R>0,\quad
 \gcd(a_R,d_R)=\gcd(b_R,d_R)=1,\quad t_R=-a_Rd_R/b_R.
\]
The actual integers here are obtained by rational group law.
At p, a_R and b_R are units and v_p(t_R)=v_p(d_R)≥1.

For m≥1 let Sigma_[m+1] be the rational truncation through
degree m+1 and define the rational unit
\[
                   U_{R,m}=d_R/\Sigma_{[m+1]}(t_R).          \tag{24}
\]
For a rational p-unit u define lambda_(p,m)(u) in Z/p^m
by the finite equation
\[
 (1+p)^{(p-1)\lambda_{p,m}(u)}
                  \equiv u^{p-1}\pmod{p^{m+1}}.             \tag{25}
\]
There is a unique solution: 1+p generates
(1+pZ_p)/(1+p^(m+1)Z_p), and p−1 is invertible modulo p^m.
This equation removes Teichmüller exactly, including every carry.
It gives log_p(u)/g_p modulo p^m. It is a local UNIT coordinate,
not the logarithm of a cyclotomic Galois character evaluated at a
point. Under local reciprocity the inverse may occur; (25) fixes
the coordinate, and the height sign below is calibrated explicitly.

**[NEW deduction] Proposition 5.1.** The three finite values
\[
 q_{R,m}=2n_p^{-2}\lambda_{p,m}(U_{R,m})\quad\bmod p^m       \tag{26}
\]
give the ACTUAL point-Bockstein matrix modulo p^m:
\[
 \boldsymbol B_p\equiv
 \begin{pmatrix}
 q_{P,m}&(q_{P+Q,m}-q_{P,m}-q_{Q,m})/2\\
 (q_{P+Q,m}-q_{P,m}-q_{Q,m})/2&q_{Q,m}
 \end{pmatrix}\pmod{p^m}.                                  \tag{27}
\]
No Sha-finiteness assumption or nondegeneracy is needed.

*Proof of normalization.* MST§1, equations(1.1)–(1.3), uses the
Galois linear functional log_p(chi_cyc)/p and defines its quadratic
function by h_MST(R)=−(R,R)_MST/2. Its exact formula is
h_MST(n_pR)=p^(-1)log_p(Sigma(t_R)/d_R).
Thus the BILINEAR diagonal for log_p(chi_cyc)/g_p is
\[
             \frac{2}{n_p^2g_p}
                         \log_p(d_R/\Sigma(t_R)).           \tag{28}
\]
This checks the minus sign, factor2, the division by n_p² and the
different factor p in MST's convention.

The Selmer height comparison in
[Nekovář11.3.9](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
together with [Besser, Theorem1.1](https://arxiv.org/html/math/0209006v1),
identifies this ordinary point height with the minus-Bockstein
pairing (14), for the SAME global log and ordinary complement.
These comparisons are the ones used and checked in the
[derived-unit proof and review](review-cm-derived-unit.md).
Here their hypotheses hold: local H⁰(V)=0 and H⁰(V^−)=0,
the ordinary lines are dual, and the non-p rational local
complexes vanish. No identification of all Selmer classes with
points is used. BKS(5.3.2) sends gamma−1 to log_p chi_cyc(gamma);
it contains no factor1/p. These observations give (28) with exactly
the existing BKS sign. The finite-place denominator d_R includes
the global non-p height terms. It is not merely a local theta value.

*Proof of error and finite construction.* By (23),
\[
 v_p(\Sigma(t_R)-\Sigma_{[m+1]}(t_R))
                         \ge(m+2)v_p(t_R).
\]
Both sigma values have valuation v_p(t_R). Their ratio is
1 modulo p^((m+1)v_p(t_R)), hence modulo p^(m+1).
Its logarithm has that same lower valuation bound. Since v_p(g_p)=1,
replacing the infinite sigma by (24) changes (28) by an element
of p^mZ_p. All other factors in (26) are units.
Equations(25),(28) therefore prove the three diagonal congruences.
Symmetric polarization gives (27), with2 invertible.
The arguments also prove independence, at this precision, of the
permitted multiplier or of a longer sigma truncation. ∎

The recipe involves only finitely many exact rational operations,
a finite root/power computation and an explicit proved tail bound.
To determine the exact primary order after certifying e, take
m=e+1 in (24)–(27). For the vanishing test (22), m=e−1 suffices.
No finite subgroup is identified with the full point lattice before
the nonzero coefficient has supplied primary finiteness.

## 6. The first point test is an actual Fermat-quotient determinant

A useful simplification follows from CM symmetry, without computing
any new prime.

**[NEW deduction] Lemma 6.1.**
\[
 \Sigma(t)=t+\frac{65}{4}t^5+O(t^9).
\]
For1≤m≤3, Sigma_(m+1)(t)=t, so (24) is exactly
\[
                              U_{R,m}=-b_R/a_R.             \tag{29}
\]
In particular define the genuine rational Fermat quotient
\[
 {\mathfrak q}_p(u)=\frac{u^{p-1}-1}{p}\pmod p
                  \quad(u\in\mathbf Q^\times\cap\mathbf Z_p^\times).
\]
Then
\[
 \det\boldsymbol B_p\equiv n_p^{-4}
  \left(4x_Px_Q-(x_{P+Q}-x_P-x_Q)^2\right)\pmod p,           \tag{30}
\]
where x_R=mathfrak q_p(−b_R/a_R).

*Proof.* The equation for x in the parameter t is
x²−x/t²+39=0, so x=t^(-2)−39t²+O(t^6).
It gives omega=(1+78t^4+O(t^8))dt. Writing
Sigma=t(1+s t^4+O(t^8)), the sigma equation
−(d/omega)^2 log Sigma=x gives156−12s=−39, hence s=65/4.
The relation Sigma(it)=iSigma(t) excludes intervening degrees.
Alternatively this is the rational CM sigma construction (23).
For m≤3 the truncation is therefore t, and d_R/t_R=−b_R/a_R.
Equation(25) modulo p² gives lambda_(p,1)(u)=−mathfrak q_p(u).
Substitute this into (26),(27); its common minus sign disappears
from the2×2 determinant. This proves (30). ∎

Thus, if the symbol computation certifies v_p(c2)=2, a single
explicit finite Fermat-quotient determinant (30) vanishing modulo p
is enough to prove Sha[p^\infty]=0. This is a sharper actual test
than failure or success of (11), not a universal assertion that
the determinant vanishes. For higher required precision the same
construction retains the higher Teichmüller coordinates and sigma
coefficients; a first Fermat quotient alone is insufficient.

There is also a consequence at the ALREADY certified prime5:
(17), Sha[5^\infty]=0 and v_5(c2)=1 imply
v_5(det bold B_5)=1. In the Néron bilinear convention
H_p=g_p bold B_p, so
\[
                         v_5(\operatorname{Reg}_5)=3.       \tag{31}
\]
This follows from the exact index and normalization theorems, with
no new numerical regulator or rerun of the certificate.

## 7. What the actual arithmetic comparison does and does not prove uniformly

Equations(7)–(11) locate the finite carry in an actual group-ring
augmentation quotient. Equations(24)–(30) construct the point
determinant from actual rational points and the fixed rational
CM sigma series. The integral unit determinant and Selmer duality
give their sharp index relation (16). In particular this is more
than the construction of two unrelated formal power series.

It does not remove the primary nonvanishing premise. The finite
moment algorithm proves c2≠0 exactly when some n satisfies
M_(n,p) not congruent to0 modulo p^(n−1).
No proof of termination at every p in (1) has been obtained.
A zero result modulo p² may be a regulator factor, a Sha factor,
or just require more precision; it is not c2=0.

I tested the immediate uniform continuation of these identities.
Hecke distribution at0 removes B_(2,p), but the exact child
calculation leaves C_p in (11). Passing to the actual point
construction replaces the previously dropped Smith determinant
by the explicit unit coordinates (25), or (30) at first precision.
The theta-unit norm relations do not provide an evaluated identity
between C_p and these point coordinates in the current proof.
The matrix in (30) is not assigned a desired value or corrected
afterward. Nor is nondegeneracy of the rank-two point matrix inferred
from nonvanishing of a CM pairing on some rational directions.

There is a concrete obstruction to trying to use ONE fixed rational
formal-group evaluation for all primes. For each fixed positive n,
the nonzero rational point nP has a fixed finite denominator d(nP).
At a good prime p it belongs to the formal group exactly when
p divides d(nP). Hence any FINITE fixed list of multipliers works
at only finitely many good primes. Our valid multipliers n_p vary
with p. The fixed rational series Sigma alone therefore does not
make (24) one rational finite evaluation at almost every p.
This observation does not rule out a different global arithmetic
construction or a Coleman continuation; it identifies the failure
of this particular attempted finite descent.

Under c2≠0, (17) also shows why v_p(c2)≤1 is sufficient but not
necessary for primary vanishing: the entire larger valuation can
be accounted for by the ACTUAL determinant. The exact finite
height-corrected continuation target is
\[
 \begin{gathered}
 \text{for every p in (1), find n with }M_{n,p}\ne0\bmod p^{n-1};\\
 e=v_p(M_{n,p})<n-1,\qquad
 \det\boldsymbol B_p=0\bmod p^{e-1}\ \text{ if }e\ge2,
 \end{gathered}                                              \tag{32}
\]
where the second line is the finite arithmetic operation (24)–(27),
not an assumed height bound. Establishing (32) would prove vanishing
at every prime in (1). Neither (32) nor an almost-all-prime form
with a proved finite exceptional set has been established.

## 8. The exact rational frame still required

At every prime with c2≠0 the preceding theorem makes the normalized
frame coordinate well-defined and gives
\[
 q_p:=\frac{c_{2,p}}{2e_p\det\boldsymbol B_p}
     =\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}
     =\frac{\varepsilon_p}{2e_p}\#\operatorname{Sha}[p^\infty],
 \qquad q_p\in\mathbf Z_p,\quad
 v_p(q_p)=v_p\#\operatorname{Sha}[p^\infty].                  \tag{33}
\]
Here M_p in the middle expression is the normalized second
LOGARITHMIC theta moment from the derived-unit note; it is not
the finite modular-symbol approximation M_(n,p).
The identity c_cmp,p M_p=2g_p²c2 and H_p=g_p bold B_p retain
all Euler, generator and CM-to-Néron factors. In particular the
2 in (33) is the fixed Tamagawa/torsion quotient8/4, not a
new freedom to rescale the frame.

Formula(33) is a sharp local index result. It does not make
epsilon_p/(2e_p) equal to1 or identify the units for distinct p.
It also does not identify q_p with a rational number merely
because both input constructions began with rational data.

**[GAP CM-Uniform-Frame].** Construct from these actual unit
determinants and fixed point motives, BEFORE separate completions,
one rational framed element Z=q Xi_(P,Q) such that
\[
 q\mapsto q_p
 \quad\hbox{under the canonical }\mathbf Q\hookrightarrow\mathbf Q_p
 \text{ whenever (33) is defined},
 \qquad
 R_\infty(Z)=\frac{L''(E,1)/2}{2\Omega_E}.                    \tag{34}
\]
The real equality would force q=n_E and prove its rationality
as a conclusion. At other split primes the undivided comparison
must also be supplied; finite/excluded primes and nonsplit primes
still require their own complete arithmetic control. The existing
local secondary baseline remains C_v, not the normalized GLOBAL
block H/2.

The first new index step has been proved, but the attempted finite
rational descent fails as specified in §7. No map producing (34)
has been constructed. The universal BSD objective is unchanged.

## 9. Source audit and review boundary

The primary sources newly checked here are Nekovář6.3.4–6.3.5,
6.7.6–6.7.9 and11.3.1–11.3.12 for integral duality and ordinary
height comparison; MST§1 for its EXACT normalization and sigma
integrality; BKS§5.1.1 and(5.3.2) for the minus-Bockstein and
generator coordinate; and BesserTheorem1.1 for the ordinary point
comparison. These are used only with their verified local
hypotheses. No Sha-finiteness premise is imported from a source's
separate BSD regulator theorem.

The Nekovář PDF was read from the existing cache
/tmp/cm-presentation-nekovar.pdf, SHA256
61c84e5ad3252a2e520747215ac57a282addc2b58c824a3637bcd77bbe02153f.
New relevant extracts are /tmp/cm-uniform-nekovar-height.txt and the
previous /tmp/cm-nonvanishing-nekovar-selmer.txt.
The Kato/Rubin determinant equality, tame convention, local unit
iota and fixed CM sigma identification are the explicitly linked
reviewed predecessor inputs, not newly recomputed claims.

The [full independent review](review-cm-uniform-carry.md) passed
all nine sections, including the finite Ext term, exact Smith-frame
unit(21), MST's log/p versus BKS's log/g_p, rational sigma tail,
finite Fermat-quotient sign, and the conditional scope of(31)–(34).
No numerical script was run and no additional agent was created.
