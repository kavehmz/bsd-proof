# Derived elliptic units and the rational CM determinant line

Date: 2026-09-12. Author: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Status: bounded construction completed; independent mathematical review
[PASS](review-cm-derived-unit.md), including the Frobenius and exact-scalar
audit below. The target is
[CM-Biex](cm-biextension-cycle-attack.md#6-the-first-remaining-equality-with-its-rational-target).
No Sha-finiteness, Selmer-corank-two, regulator-nondegeneracy or complex
rationality hypothesis is implicit below.

## 1. Actual finite-level units

Fix $E:y^2=x^3+39x$, $K=\mathbb Q(i)$, and a good split prime
$p\ge5$ in the scope of the preceding CM note. Write
$p=\mathfrak p\bar{\mathfrak p}$ and
$\pi=\psi_E(\mathfrak p)$, so $\pi\bar\pi=p$.
Keep the exact Néron data
$$\Gamma_E=\Omega_\infty\mathbb Z[i],\quad
\mathfrak f=(f_0),\quad f_0=39(1+i)^3,\quad
\Delta_E=-64\cdot39^3.$$

For an integer $a>1$ prime to $6p\,\mathrm N\mathfrak f$, use the rational elliptic
function
$$\Theta_a(R)=a^{-12}\Delta_E^{a^2-1}
\prod_{0\ne U\in E[a]}(x(R)-x(U))^{-6}.\tag{1}$$
The product over all nonzero a-torsion points is invariant under
Galois and has rational coefficients. Here a is odd, so pairing U
and −U shows that (1) is the twelfth power of the normalized theta
function conventionally denoted $\Theta_0(z;\Gamma_E,(a))$.
It has divisor $12(a^2[O]-\sum_{U\in E[a]}[U])$.
Taking the twelfth power fixes the root-of-unity ambiguity; its
factor 12 will be retained in cohomology.

**[THEOREM, precise elliptic-unit input]** Put
$$F_{k,n}=K(\mathfrak f\mathfrak p^n\bar{\mathfrak p}^k),\qquad
L_{k,n}=K(E[\mathfrak p^n\bar{\mathfrak p}^k]),$$
and let $R_{k,n}$ be the point represented in $\mathbb C/\Gamma_E$
by $\Omega_\infty/(f_0\pi^n\bar\pi^k)$. Then
$$e_{k,n}(a)=N_{F_{k,n}/L_{k,n}}\Theta_a(R_{k,n})
\in\mathcal O_{L_{k,n}}^\times\qquad(k,n\ge1)\tag{2}$$
is norm compatible in both indices. The conductor contains several
prime factors, which is what makes these values global units.

These exact definitions, including the twelfth power, are in
[U. Schmitt, A comparison of elliptic units in certain prime power conductor cases, §§2.1–2.3 and Definition 3.12](https://www.mathi.uni-heidelberg.de/fg-sga/Preprints/Comparison%20of%20elliptic%20units_vFINAL.pdf),
Acta Arith. 171.1 (2015), 39–66, DOI 10.4064/aa171-1-4.
Only these general-conductor constructions are used; the paper's
prime-power-conductor comparison theorem in §3.4 is not used.
His printed pp.47–49 record the norm law in the ray fields. If an
ideal $\mathfrak q=(q)$ is removed from a modulus $\mathfrak m$
with the unit-injectivity condition retained, that law is
$$
N_{K(\mathfrak m)/K(\mathfrak m/\mathfrak q)}\Theta_a(R)
=\begin{cases}
\Theta_a(qR),&\mathfrak q\mid\mathfrak m/\mathfrak q,\\
\Theta_a(qR)^{1-\sigma_{\mathfrak q}^{-1}},
 &\mathfrak q\nmid\mathfrak m/\mathfrak q.
\end{cases}\tag{3}
$$
Here $\sigma_{\mathfrak q}$ is arithmetic Frobenius on the lower
ray field, and the ideals are prime to the smoothing ideal when
needed. The modulus $\mathfrak f$ injects $\mathbb Z[i]^\times$
into its residue units, so no missing global-unit multiplicity
occurs in (2)–(3). The norm down to $L_{k,n}$ gives precisely the
system of Definition 3.12, not a merely formally postulated Euler
system.

## 2. Twisting before cyclotomic specialization

Let $T_{\mathfrak p}E=\mathbb Z_p(\Psi)$ be the idempotent
component of the Tate module. Then
$$\Psi\Psi^c=\chi_{\rm cyc},\qquad
\rho=\Psi\chi_{\rm cyc}^{-1}=(\Psi^c)^{-1},\qquad
\mathbb Z_p(1)\otimes\mathbb Z_p(\rho)=T_{\mathfrak p}E.\tag{4}$$
Fix compatible bases of the indicated rank-one modules. The eventual
comparison with the Néron differential must retain these bases and
their associated CM period.

**[NEW, finite-level twisting construction] Proposition 1.** Let
$K_n=K\mathbb Q_n$ be the nth cyclotomic layer and put
$L_r=L_{r,r}$. For integers $m\ge1$ and sufficiently large
$r\ge\max(m,n+1)$, define
$$z_{n,m}^{a}=\operatorname{Cor}_{L_r/K_n}
\bigl(\delta_m(e_{r,r}(a))\otimes t_{\rho,m}\bigr)
\in H^1(K_n,T_{\mathfrak p}E/p^m).\tag{5}$$
These classes are independent of sufficiently large r, compatible
under coefficient reduction in m and corestriction in n, and hence
define $z_\infty^a\in H^1_{\rm Iw}(K_\infty,T_{\mathfrak p}E)$.

*Proof.* The finite field $L_r$ trivializes the two Tate components
modulo $p^m$, and contains $\mu_{p^m}$ by the Weil pairing. Thus it
also trivializes $\rho$ modulo $p^m$. It contains $K_n$ for the
specified sufficiently large r. The tensor in (5) is consequently
a well-defined cohomology class with the required coefficients.
Increasing r replaces its Kummer class by that of a norm-compatible
unit, so Kummer compatibility with corestriction and the projection
formula prove independence. Reduction in m respects the compatible
bases and Kummer maps. Transitivity of corestriction proves
compatibility in n. Taking the two inverse limits proves the claim.
$\square$

This is the exact twist of
[Rubin, Euler Systems, VI.3.5 and VI.5.3](https://swc-math.github.io/aws/1999/99RubinES.pdf).
The character $\rho$ generally does not factor through the
cyclotomic quotient. Twisting only after first discarding the other
CM direction is therefore not this construction.

For clarity the group-ring action changes as follows. If $\sigma$
acts on an untwisted class u, then
$$\operatorname{Tw}_\rho(\sigma u)
=\rho(\sigma)^{-1}\sigma\operatorname{Tw}_\rho(u).\tag{6}$$
This follows by applying $\sigma$ to both factors in $u\otimes t_\rho$.
In particular (3)'s new-prime factor becomes
$1-\rho(\sigma_{\mathfrak q})\sigma_{\mathfrak q}^{-1}$.
This fixes the inverse and character convention, rather than calling
the factor an unspecified Euler factor.

The integral induced representation
$\operatorname{Ind}_{G_K}^{G_\mathbb Q}T_{\mathfrak p}E$ is
$T_pE$: its two summands are the integral CM idempotent components,
interchanged by complex conjugation. Shapiro therefore views (5)
as a class over $\mathbb Q_n$ for $T_pE$. No multiplicative factor
two is inserted in this identification.

## 3. Exact smoothing and the Néron-normalized unit class

Schmitt Definition 3.12 and Proposition 3.13 normalize the semilocal
Coleman map by
$$\mathcal L(e(a))=12(\sigma_a-N(a))\lambda.\tag{7}$$
The integral measure $\lambda$ is independent of a. The sign in
$\sigma_a-N(a)$ is part of this convention. After (6) and cyclotomic
restriction the smoothing factor is
$$q_{a,p}(T)=12\bigl(\Psi^c((a))\overline\sigma_a-a^2\bigr),
\quad T=\gamma-1,\quad\chi_{\rm cyc}(\gamma)=1+p.\tag{8}$$

**[NEW, integral removal of smoothing] Lemma 2.** Use a=5 if p≠5,
and a=7 if p=5. Then $q_{a,p}$ is a unit of $\mathbb Z_p[[T]]$.
Thus
$$z_\infty^{\rm Sch}=q_{a,p}^{-1}z_\infty^a\tag{9}$$
is a defined integral cyclotomic class. It is independent of the
permitted auxiliary choice, with the convention of (7).

*Proof.* Since E is defined over Q, the CM value on the rational
ideal (a) is real and has norm $a^2$, hence is ±a. Consequently
$q_{a,p}(0)=12(\pm a-a^2)$. For a=5 its possible prime divisors
are 2,3,5; for a=7 its two values are −12·42 and −12·56, neither
divisible by 5. This proves the unit claim. For independence, the
injective semilocal Coleman map in Schmitt §3.3 and (7) imply
$(\sigma_b-Nb)e(a)=(\sigma_a-Na)e(b)$ in the completed unit
module. Twisting and corestricting preserve this identity. Multiplying
by the inverse unit smoothing factors proves equality in (9).
$\square$

The exact reciprocity dictionary is supplied by the primary CM
construction in [Kato, Astérisque 295 (2004), §§15.4–15.16](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
DOI 10.24033/ast.639. That full PDF was read locally after the web
reader rejected its size. Kato normalizes by $N(a)-\sigma_a$, the
opposite sign to (7). His canonical function ${}_a\theta_E$ has
divisor $a^2[O]-E[a]$ and is characterized by its norm compatibility
(Proposition 1.3 and §15.4). Its twelfth power is (1): the product
formula has the same divisor and the same leading coefficient
$a^{-12}\Delta_E^{a^2-1}$ at O, as follows from Proposition 1.3(3);
their quotient is therefore the constant one. Thus his
normalized unit is the negative of (9), not (9) itself, after fixing
the same coefficient vector.

We specify that vector rather than leaving a period scalar implicit.
Let b be the Betti cycle with period $\Omega_\infty$. In the basis
$b,ib$ the real cycle is $b-ib$, with period $\Omega_E$, and
$$\gamma_E^+=\tfrac12\bigl(b^\vee-(ib)^\vee\bigr)
\in H^1_B(E,\mathbb Q)^+,
\qquad\operatorname{per}(\omega)^+=\Omega_E\gamma_E^+.\tag{9a}$$
Use the CM cohomological component with Galois character
$\rho=(\Psi^c)^{-1}$, and let $\operatorname{pr}_\rho$ be its
idempotent projector after extending coefficients to K. Set
$\gamma_{\rm CM}=2\operatorname{pr}_\rho(\gamma_E^+)$.
Its induced plus projection is exactly $\gamma_E^+$, since complex
conjugation interchanges the two CM components. All these Betti
coefficients belong to $\mathbb Z[i,1/2]$; their p-adic realization
is the coefficient used in (5). This is a rational Betti choice
fixed before completing at p, not a real L-value ratio.

Apply Kato with the CM embedding/type selected by $\rho$. If his
fixed type instead labels the conjugate component, conjugate the
CM construction first. This is concrete for our diagonal tower:
$$\overline{\Omega_\infty}=-i\Omega_\infty,\qquad
\bar f_0=i f_0,\qquad\overline{R_{r,r}}=-R_{r,r}.$$
The function $\Theta_a$ in (1) is rational and even, so its value
at $R_{r,r}$ is invariant under complex conjugation. The norm in
(2) commutes with conjugation, since both fields are stable under
it, and hence $e_{r,r}(a)$ is likewise invariant. Exchanging the
two CM components therefore retains the same induced plus Betti
coefficient $\gamma_E^+$; after the Tate twist (1), the even
cyclotomic branch below is unchanged. No theorem for the wrong
CM type or the opposite local condition is being substituted.

**[THEOREM, exact CM reciprocity in this normalization]** Let
$z_\infty$ be the image of Kato's normalized finite-level elliptic
units under twisting by $\gamma_{\rm CM}$ and Shapiro. Equivalently
it is (5) divided by $12(a^2-\Psi^c((a))\overline\sigma_a)$,
with that coefficient vector. Then the Néron-normalized ordinary
Coleman map satisfies
$$\operatorname{Col}_{\alpha,\omega}(z_\infty)=L_p(E,T).\tag{9b}$$

Here is the exact source chain. Kato §15.6 defines the untwisted
element by dividing the canonical units by $N(a)-\sigma_a$.
Proposition 15.9 computes its twisted dual exponentials with the
CM Betti period. Lemma 15.11 fixes the rational Betti comparison
by the differential-period map; (15.12.2) and (15.16.1) identify
the image with the corresponding Kato zeta element, exactly.
The Tate twist (1) and the trivial finite cyclotomic branch are
taken as in Theorem 16.6, which then gives its Coleman image.
For weight two these
comparisons concern the actual elliptic-curve motive; no assertion
about identifying higher-weight motives is being imported from
the warning after Lemma 15.11. Equation (9a) fixes its real period
to be $\Omega_E$. The local line in (4) and its conjugate are
selected by their Galois characters, so the opposite-prime finite
and singular local conditions are not confused.

In the notation of BKS §6.1 this is $L_{S,p}$ with real period
$\Omega_E$. All bad Euler factors of this CM curve are one, and
at the trivial character the p-factor satisfies
$$\frac{1-\alpha^{-1}}{1-\beta^{-1}}
(1-\alpha/p)(1-\beta/p)=(1-\alpha^{-1})^2,
\qquad\beta=p/\alpha.$$
At ramified cyclotomic characters the p-factor is absent. Thus this
is exactly the MTT series used in the predecessor note. Its already
audited Katz comparison gives
$$[T^2]L_p(E,T)=c_2=
\frac{c_{\rm cmp,p}M_p}{2g_p^2},\qquad
c_{\rm cmp,p}=(156i\Omega_p)^{-1}.\tag{9c}$$
The first two coefficients vanish. No equality up to an unspecified
unit is substituted in (9b) or (9c).

## 4. The full Selmer Bockstein needs no Sha hypothesis

Let $V=V_pE$, $S=\{2,3,13,p,\infty\}$, and use the ordinary
Selmer complex with the canonical local line $F^+V$ at p and
unramified local complexes away from p. For finite coefficient
algebra $A_2=\mathbb Q_p[T]/T^2$, give $V\otimes A_2$ the inverse
cyclotomic action
$$g(v\otimes1)=g(v)\otimes(1-c_\gamma(g)T),\qquad
c_\gamma(g)=\frac{\log_p\chi_{\rm cyc}(g)}{g_p},\quad
g_p=\log_p(1+p).\tag{10}$$
The compatible local cones form the usual Selmer complex. Denote
its specialization at T=0 by C₀. Good ordinarity makes
$H^1(C_0)=\operatorname{Sel}(\mathbb Q,V)$, including possible
Tate-module Sha classes. The exact sequence of coefficient complexes
gives a connecting map $\partial:H^1(C_0)\to H^2(C_0)\otimes(T)/(T^2)$.

**[NEW, explicit cochain calculation] Lemma 3.** On a constant lift
of a global one-cocycle f, the connecting map is represented by
$$\partial(f)(g,h)=-c_\gamma(g)\,g f(h)\,T.\tag{11}$$
The local components are the corresponding connecting maps of the
Selmer cone. This defines a map on the entire Selmer group without
a restriction on its dimension.

*Proof.* The deformed differential of the lifted one-cochain is
$g f(h)(1-c_\gamma(g)T)-f(gh)+f(g)$. The constant term is zero
by the cocycle identity, and its T term is exactly (11). Changing
a lift or a representative changes it by a boundary; the same
calculation in each local complex is compatible with the restriction
maps defining the cone. $\square$

Use $\beta=-\partial$, the explicit minus-Bockstein convention in
[BKS, §5.1.1, equation (5.1.1)](https://arxiv.org/pdf/1910.07404),
and global duality to obtain $h_\Gamma$ valued in $(T)/(T^2)$.
The construction in that subsection is on full Selmer groups.
The restriction to divisor classes agrees with Coleman–Gross for
the same logarithm and complement by
[Besser, math/0209006v1, Theorem 1.1](https://arxiv.org/html/math/0209006v1).
The canonical ordinary complement and the SW height normalization
were fixed in the reviewed CM note. Consequently, on the known
Mordell–Weil subspace,
$$h_\Gamma(P_i,P_j)=g_p^{-1}h_p(P_i,P_j)T.\tag{12}$$
This retains the sign and the generator logarithm, with no assumption
that the Mordell–Weil subspace exhausts Selmer.

**[NEW, exact restricted determinant] Proposition 4.** If Hₚ is the
two-by-two height matrix on P,Q, then the exterior Bockstein pairing
on their determinant frames is
$$\det(h_\Gamma(P_i,P_j))
=\frac{\operatorname{Reg}_p}{g_p^2}T^2
\quad\text{in }(T^2)/(T^3).\tag{13}$$
It is the realization of the full arithmetic determinant constructed
in the preceding note, since Hₚ includes its fixed rational Kummer
corrections. It need not be the determinant of the entire Selmer
complex.

*Proof.* Take the determinant of (12). The known arithmetic subspace
has basis P,Q, while the full group fits into
$$0\to E(\mathbb Q)\otimes\mathbb Q_p\to\operatorname{Sel}(\mathbb Q,V)
\to T_p\Sha(E/\mathbb Q)\otimes\mathbb Q_p\to0.$$
Hence no identification of these two spaces is justified by rank
two alone. $\square$

## 5. Rationalizing at finite levels erases this derivative

The units (2) exist at finite algebraic levels before any p-completion.
It is therefore natural to attempt their Bockstein descent there,
over Q, and only afterward compare realizations. The augmentation
calculation gives an exact test of that proposed order of operations.

**[NEW, finite-level rational descent test] Proposition 5.** Let
$G_n=\langle\gamma_n\rangle$ have order $p^n$, and let $I_n$ be the
augmentation ideal of $\mathbb Z[G_n]$. Then
$$I_n/I_n^2\simeq\mathbb Z/p^n,\qquad\gamma_n-1\longmapsto1.\tag{14}$$
The quotient transition maps give inverse limit $\mathbb Z_p$.
In contrast, if $I_{n,\mathbb Q}$ is the augmentation ideal of
$\mathbb Q[G_n]$, then
$$I_{n,\mathbb Q}^2=I_{n,\mathbb Q},\qquad
I_{n,\mathbb Q}^r/I_{n,\mathbb Q}^{r+1}=0\quad(r\ge1).\tag{15}$$

*Proof.* Writing $t=\gamma_n-1$, the ring is
$\mathbb Z[t]/((1+t)^{p^n}-1)$. Modulo $t^2$ its sole nonconstant
relation is $p^nt=0$, giving (14) with its compatible generator.
Over Q, let $e_0=p^{-n}\sum_{g\in G_n}g$. This is an idempotent
with augmentation one, and $I_{n,\mathbb Q}=(1-e_0)\mathbb Q[G_n]$.
It is idempotent, proving (15). $\square$

Thus rationalizing each finite-level unit relation and then taking
its positive augmentation quotient produces zero, not the desired
rational determinant element. The nonzero direction in (10)–(13)
comes from the inverse limit of integral p-power torsion quotients.
This is not a proof that a higher motivic rational descent is impossible;
it rules out this specific finite-level rational augmentation construction.
It also does not treat all p-adic completions as one rational line.

## 6. A global first derivative without finite Sha

Write $\mathcal H^i=H^i_{\rm Iw}(\mathbb Q_\infty,T_pE)$ with S
as above and $\Lambda=\mathbb Z_p[[T]]$. The height-one localization
$\Lambda_{(T)}$ is a discrete valuation ring with residue field Qₚ.

**[THEOREM, Iwasawa inputs used]** Kato Theorems 12.4 and 12.5(3),
proved in the CM case in §§15.13–15.17 using Rubin's theorem, give:
$\mathcal H^1$ has rank one, $\mathcal H^2$ is torsion, and at
the augmentation prime the length of $\mathcal H^2_{(T)}$ is at
most the length of $\mathcal H^1_{(T)}/\Lambda_{(T)}z_\infty$.
These are rational height-one assertions. The possible extra local
term in Theorem 12.5(3) is zero because p is good. None requires
finite Sha. The exact CM zeta-element identification above ensures
that this is the actual unit class, not an arbitrarily chosen
generator of the same characteristic ideal.

More precisely, Kato initially gives the bound for the submodule
$Z(f)$ generated by all Betti coefficients. The conjugation relation
in Theorem 12.5(1) is $z_{c\gamma}=-\sigma_{-1}z_\gamma$ before
the Tate twist. Twisting by (1) changes its right side to
$\sigma_{-1}z_\gamma$. On the trivial finite cyclotomic branch,
the minus Betti part is therefore zero, and the one-dimensional
plus part generates $Z(f)$. Its nonzero vector $\gamma_E^+$ thus
generates precisely $\Lambda_{(T)}z_\infty$. This is what applies
the length inequality to the individual class used here. In the
CM proof, $K=\mathbb Q(i)$ is not contained in
$\mathbb Q(\mu_{p^\infty})$ for p≥5, since K ramifies at 2;
the augmentation height-one prime does not contain p, so condition
15.2(a) is sufficient for Kato's §15.17 comparison.

**[NEW, rank-two divisibility without identifying Selmer] Proposition 6.**
The class $z_\infty$ is divisible by T in rational Iwasawa cohomology.
Every integral elliptic-unit class in the same scalar line and
normalization is divisible by T in $\mathcal H^1$ itself. In
particular its first derivative is canonically defined.

*Proof.* The global p-cohomological dimension is two, since p is
odd and S contains p and infinity. In the inverse-limit construction
one may use finite p-power coefficients, whose cohomology groups
are finite; their inverse systems satisfy Mittag–Leffler. Thus the
derived Iwasawa cohomology has no third group. Derived base change
along T consequently gives
$$\mathcal H^2/T\mathcal H^2\simeq H^2(G_{\mathbb Q,S},T_pE).\tag{16}$$
The global Euler characteristic for this two-dimensional odd
representation is −1. Since $H^0(G_{\mathbb Q,S},V)=0$, it says
$$\dim H^1(G_{\mathbb Q,S},V)-\dim H^2(G_{\mathbb Q,S},V)=1.$$
The two independent Kummer classes P,Q inject into H¹, so H² has
dimension at least one. By (16) the T-primary length of
$\mathcal H^2_{(T)}$ is at least one. The Iwasawa divisibility input
therefore makes the unit class divisible by T after localization.

For the integral assertion, coefficient base change also gives an
injection
$$\mathcal H^1/T\mathcal H^1\hookrightarrow
H^1(G_{\mathbb Q,S},T_pE).\tag{17}$$
The target is Zₚ-torsion free: its possible p-power torsion comes
from $E(\mathbb Q)[p^\infty]$, which is zero since the torsion order
is two. In the CM-component description, $E(K)[p^\infty]=0$ as
well: the plus/minus projectors and multiplication by i identify
its two eigenspaces with $E(\mathbb Q)[p^\infty]$ for odd p.

If an integral class becomes T-divisible after localization at (T),
some $s\notin(T)$ kills its image in (17). On that quotient s acts
as the nonzero scalar $s(0)\in\mathbb Z_p$. Torsion-freeness forces
the image to vanish. This proves actual integral T-divisibility,
rather than assuming it from a T-order computation. Finally
$\mathcal H^1[T]=0$ by the same coefficient sequence and H⁰=0,
so division is unique. $\square$

Set
$$z_\infty=T w_\infty,\qquad
\kappa_p=w_0\otimes T.\tag{18}$$
This notation permits $\kappa_p=0$ if the actual vanishing order
is larger. It asserts a first derived class, not that one is the
first nonzero derivative.

**[NEW, full Selmer membership] Lemma 7.** $w_0$ belongs to
$\operatorname{Sel}(\mathbb Q,V)$ without any corank-two assumption.

*Proof.* Equation (9b) gives
$\operatorname{Col}(w_\infty)=L_p(E,T)/T\in T\mathbb Q_p[[T]]$.
At augmentation the ordinary Coleman map is a nonzero scalar times
the dual exponential, so $\exp^*(\operatorname{loc}_p w_0)=0$.
That kernel is $H_f^1(\mathbb Q_p,V)$. At every finite place
$\ell\ne p$, $H^1(\mathbb Q_\ell,V)=0$: the local Euler
characteristic is zero, and both H⁰ and H² vanish by local duality
and finiteness of local p-power torsion on E. Thus all other finite
conditions hold; the odd-p real condition contributes nothing.
This proves the Selmer assertion. The nonzero scalar at p is
computed explicitly below. $\square$

## 7. Exact height formula and the two-point projection

**Frobenius convention audit.** Distinguish the absolute cohomological
Frobenius $F$ on $H^1_{\rm cris}(E/\mathbb Z_p)\otimes\mathbb Q_p$
from the Frobenius $\varphi$ on $D_{\rm cris}(V_pE)$. We use the
principal-polarization identification
$$V_pE\simeq H^1_{\rm et}(E_{\overline{\mathbb Q}},\mathbb Q_p)(1).$$
After the fixed Tate identification the underlying de Rham space is
$H^1_{\rm dR}(E/\mathbb Q_p)$, its $F^0$ line is $\mathbb Q_p\omega$,
and $\varphi=p^{-1}F$. Set $\eta=x\omega$, and let $\alpha$ be
the unit root of $X^2-a_pX+p$ and $\beta=p/\alpha$. On this curve
the exact dictionary is
$$
\begin{array}{c|c|c}
\text{line}&F\text{-eigenvalue on }H^1_{\rm cris}
 &\varphi\text{-eigenvalue on }D_{\rm cris}(V_pE)\\ \hline
\mathbb Q_p\omega&\beta&\beta/p=\alpha^{-1}\\
\mathbb Q_p\eta&\alpha&\alpha/p=\beta^{-1}.
\end{array}\tag{19a}
$$

*Proof of the dictionary.* At split p, $[i]^*$ has the distinct
eigenvalues i and −i on $\omega,\eta$ and commutes with F. Thus F
preserves each displayed line. The integral Hodge-filtration property
$F(\omega)\in pH^1_{\rm cris}$ is stated explicitly in
[Mazur–Stein–Tate, §3.2 and Algorithm 3.2](https://wstein.org/papers/pheight/pheight.pdf),
Documenta Math., Extra Volume Coates (2006), published pp.577–614,
DOI 10.4171/DMS/4/17; the linked author version is paginated 585–622.
Since the
ordinary characteristic polynomial has precisely one root divisible
by p, this gives $F\omega=\beta\omega$; the other line has
eigenvalue $\alpha$. The Tate twist divides F by p, proving (19a).
Equivalently, weak admissibility excludes a slope-zero F-stable
Hodge line of Hodge weight one. $\square$

Thus the phrase “unit-root complement” in the preceding CM sigma
proof refers to the F-unit-root line $\mathbb Q_p\eta$. It has
$\varphi$-eigenvalue $\beta^{-1}$, of valuation −1. The printed
$\alpha^{-1}$ label in
[Stein–Wuthrich, §4.1](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf)
is inconsistent with that paper's explicit $\varphi=F/p$
normalization in §3.5 and the MST unit-root recipe. It is not used
here. The prior conclusion $E_2=0$ remains valid from MST: the
F-unit-root line is exactly $\eta$, so the coefficient of $\omega$
in $F^n\eta$ is zero. No reciprocal-eigenvalue assertion from the
printed SW §4.1 is needed for the canonical sigma or height.

Put $k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1})$.
All factors are nonzero at good p. For the Néron differential choose
the crystalline vector $\nu$ with $\varphi\nu=\beta^{-1}\nu$
and $[\omega,\nu]=1$, exactly as in BKS Lemma 6.9. By (19a),
$\nu$ is a nonzero multiple of $\eta$ and is transverse to the
Hodge line. The alternating pairing here is the one induced by
polarization on $D_{\rm dR}(V)\times D_{\rm cris}(V)$, with its
Tate-valued target trivialized as in BKS; it satisfies
$[\varphi u,\varphi v]=p^{-1}[u,v]$. The two eigenvalues in (19a)
multiply to $p^{-1}$, consistently with this pairing.
In the Coleman normalization of BKS §6.3,
$$\delta_0=\frac1p\left(-\varphi^{-1}+(p-1)(1-\varphi)^{-1}\right)\nu
=\frac{1-\alpha^{-1}}{1-\beta^{-1}}\nu.\tag{19}$$
Indeed $\operatorname{Tr}(\zeta_p)=-1$, and substituting
$\varphi\nu=\beta^{-1}\nu$ gives
$p^{-1}(-\beta+(p-1)\beta/(\beta-1))=k_\alpha^{-1}$.
This fixes the Euler scalar directly; it is not an unspecified unit.

**[NEW, derived unit height identity on the full Selmer space] Proposition 8.**
For every $x\in E(\mathbb Q)\otimes\mathbb Q_p$,
$$h_\Gamma(x,\kappa_p)=k_\alpha\log_\omega(x)c_2T^2.\tag{20}$$
Neither finite Sha nor equality of Mordell–Weil and Selmer spaces
is needed.

*Proof.* For the lift $w_\infty$, Lemma 7 permits Rubin's local
derivative $D(w)$ in
$H^1(\mathbb Q_p,F^-V)\otimes(T)/(T^2)$: reduce its singular
localization modulo T² and divide by T. Uniqueness follows from
$H^0(\mathbb Q_p,F^-V)=0$. In the diagram of the global and local
Selmer cones the compatibility of connecting maps gives
$\beta(w_0)=\delta(D(w))$. Pairing against x and using local/global
duality gives
$$h_\Gamma(x,w_0)=(x,D(w))_p.$$
This is the proof of BKS Theorem 6.11; here its unnecessary
identification of the *whole* Selmer dual with the Mordell–Weil
dual is omitted. The pairing and this diagram already exist on
the full Selmer complex. Howard's
[Theorem 4.5](https://arxiv.org/html/1202.6343v1) gives the same
derived-height identity with this full-Selmer scope.

The Coleman definition and norm compatibility of its exponential
test vectors give, modulo T²,
$$\operatorname{Col}(w_\infty)
=(\exp(\delta_0),D(w))_p=c_2T.$$
This is the direct computation in BKS Lemma 6.14. By (19) and
exponential/logarithm duality,
$x=k_\alpha\log_\omega(x)\exp(\delta_0)$ in the one-dimensional
local finite cohomology. Substitute this in the previous pairing
and multiply by T, proving (20). The only global requirement used
was Lemma 7, already established without Sha finiteness. $\square$

Write $W_p=E(\mathbb Q)\otimes\mathbb Q_p$, with basis P,Q,
and $H=H_p$, $l=(\log_\omega P,\log_\omega Q)^t$. The vector
$$R_{p,\omega}=g_p^{-1}\bigl((H_{22}l_1-H_{12}l_2)P
+(H_{11}l_2-H_{12}l_1)Q\bigr)\otimes T\tag{21}$$
satisfies
$$h_\Gamma(x,R_{p,\omega})=\log_\omega(x)
\frac{\operatorname{Reg}_p}{g_p^2}T^2.$$
This follows from $H\operatorname{adj}(H)=\det(H)\mathrm{id}$
and symmetry of H, even when its determinant is zero.
It defines the restricted Bockstein map on the actual determinant
frame by $\mathcal B_p(\Xi_{P,Q})=R_{p,\omega}$.

**[NEW, exact p-local determinant realization without corank two]
Proposition 9.** Suppose only additionally that
$\operatorname{Reg}_p\ne0$. There is a canonical height-orthogonal
projection
$\operatorname{pr}_{W_p}:\operatorname{Sel}(\mathbb Q,V)\to W_p$.
The derived element
$$Z_p=\mathcal B_p^{-1}\left(
\frac{p}{2\#E(\mathbb F_p)}\operatorname{pr}_{W_p}(\kappa_p)
\right)\in\mathscr L_{P,Q}\otimes\mathbb Q_p\tag{22}$$
is defined, and has exactly the p-adic realization required by CM-Biex:
$$Z_p=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p}\Xi_{P,Q},
\qquad R_p(Z_p)=\frac{c_{\rm cmp,p}M_p}{4e_p}.\tag{23}$$

*Proof.* Nondegeneracy of H defines the projection by requiring that
the difference pair to zero against P,Q. This does not require
nondegeneracy on the remaining Selmer space or its absence. Equation
(20) determines the projection explicitly:
$$\operatorname{pr}_{W_p}(\kappa_p)
=\frac{g_p^2 k_\alpha c_2}{\operatorname{Reg}_p}R_{p,\omega}.$$
The logarithm of a non-torsion rational point is nonzero locally:
the kernel of the elliptic logarithm on $E(\mathbb Q_p)$ is its
torsion subgroup. Thus l is nonzero and (21) is nonzero when H is
invertible. The inverse in (22) is the inverse on its one-dimensional
image, so is defined by this displayed equality.

Finally
$$k_\alpha e_p=(1-\alpha^{-1})(1-\beta^{-1})
=\frac{\#E(\mathbb F_p)}p.$$
Combine this with (9c) to obtain
$$\frac{p}{2\#E(\mathbb F_p)}
\frac{g_p^2 k_\alpha c_2}{\operatorname{Reg}_p}
=\frac{c_{\rm cmp,p}M_p}{4e_p\operatorname{Reg}_p},$$
which proves (23). All generator logarithms, the twelfth power,
the smoothing sign, the local Euler factor and the CM-to-Néron
period have been retained. $\square$

Projection in (22) may discard additional Selmer classes. It does
not prove that their quotient is zero or that Sha is finite. Nor
is nondegeneracy at every prime asserted. If H is degenerate,
(18), (20) and (21) still make sense, while the inverse construction
(22) is not justified.

## 8. Descent to the single rational framed element

The units in (2) and the Betti vector (9a) were defined before
separate p-adic completions. The derived operation in (18) is not
defined at that rational finite level: Proposition 5 shows precisely
that all its positive rational augmentation quotients vanish.
This supplies an explicit failure of the proposed order of descent,
rather than merely observing that the current construction is p-adic.

Keeping the integral levels and taking their inverse limit repairs
the local construction, but yields the separate Zₚ directions in
(14). No argument identifies their resulting scalars (23) with
one rational coefficient, and (22)'s height projection likewise
uses a separate p-adic realization. Finite-level exact norm
compatibility proves neither of those additional comparisons.

**[GAP CM-Derived, remaining rational descent].** Construct a single
$Z_\theta\in\mathscr L_{P,Q}$ over Q, by an arithmetic operation on
the elliptic-unit system retaining its derived extension data, such
that its localization equals (22) at every prime where that map is
defined, with compatible undivided identity at the other good split
primes, and such that
$$R_\infty(Z_\theta)=\frac{L''(E,1)/2}{2\Omega_E}.$$
Writing $Z_\theta=q\Xi_{P,Q}$ would prove $q=n_E\in\mathbb Q$;
that rationality is not a premise. The exact finite-level rational
augmentation route was attempted and fails by (15). No different
higher descent map producing this element has been constructed.

The completed p-local result is the genuine derived unit and its
exact height/determinant realization (18)–(23), with the explicit
nondegeneracy condition only where an inverse is taken. It gives no
new Sha-finiteness statement, no proof of the complex leading-term
formula, and no resolution of universal BSD.

Primary-source audit record: Kato's full PDF has SHA-256
`3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d`.
It was read at §§1.3,12.4–12.5,15.4–15.17 and16.6; the exact
normalization arguments above do not rely on a secondary summary.
The source explicitly distinguishes height-one rational divisibility
from stronger integral results. No old numerical certificate or
unit scan was rerun.
