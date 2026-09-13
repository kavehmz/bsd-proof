# Actual two-prime Heegner heights and the integral rank-five target

Date: 2026-09-12. Author: /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded construction; all [NEW] deductions passed
[independent coordinator review](review-two-prime-heegner-height.md).
Restart: [checkpoint](two-prime-heegner-height-checkpoint.md).
The parent objective remains full BSD for every elliptic curve over Q.
No rank-five theorem, Sha finiteness theorem, or BSD counterexample is claimed.

## 1. The exact arithmetic object

Assume the ordinary hypotheses of [O5](odd-rank-selmer-bridge.md#5-the-next-exact-statement-at-analytic-rank-at-least-five).
Thus E/Q is non-CM, p>=5 is good ordinary, E[p] is irreducible over G_Q,
and the analytic rank of E is odd and at least five. Fix an imaginary
quadratic K of odd fundamental discriminant D different from -3, with
(D,Np)=1, every prime of Np split in K, and L(E^D,1) nonzero.
No finiteness of Sha is assumed. Let f be the normalized newform of E.

Choose distinct inert primes ell,q not dividing NpD, with
$$
 k_\ell=\min(v_p(\ell+1),v_p(a_\ell))\ge1,\quad
 k_q=\min(v_p(q+1),v_p(a_q))\ge1,\quad
 k=\min(k_\ell,k_q),\quad m=\ell q.
 \tag{1}
$$
We write ell as $\ell$ in formulas. The coefficient ideal in O5 is
$(p^k)=J_\ell+J_q$, not an ideal from the cyclotomic Kurihara construction.
Set $H_c=K[c]$, the ring class field of $\mathcal O_c=\mathbb Z+c\mathcal O_K$,
and
$$
 G=\operatorname{Gal}(H_m/K),\qquad
 G_0=\operatorname{Gal}(H_m/H_1)=G_\ell\times G_q.
$$
Here $G_\ell$ has order $\ell+1$, $G_q$ has order $q+1$, and
$h_m=|G|=h_K(\ell+1)(q+1)$, with $h_K=[H_1:K]$.
These assertions follow from the ring-class exact sequence: the quotient
of local units at an inert prime is
$\mathbb F_{\ell^2}^{\times}/\mathbb F_\ell^\times$; the global unit
correction is one because D is neither -3 nor -4. The two local factors
are independent by the Chinese remainder theorem. We do not assume that
the extension $G$ of $\operatorname{Gal}(H_1/K)$ by $G_0$ splits, or that
$p\nmid h_K$.

Fix an ideal $\mathfrak N\subset\mathcal O_K$ with
$\mathcal O_K/\mathfrak N=\mathbb Z/N\mathbb Z$ and a modular parametrization
$\pi:X_0(N)\to E$, normalized by $\pi(\infty)=O$. Its degree is denoted
$d_\pi$ and is retained throughout. For $c\mid m$ let $x_c$ be the CM
point of the cyclic isogeny
$$
 \mathbb C/\mathcal O_c\longrightarrow
 \mathbb C/(\mathfrak N\cap\mathcal O_c)^{-1},
 \qquad y_c=\pi(x_c)\in E(H_c).
 \tag{2}
$$
Use the compatible CM points and Artin maps in this formula at all four
conductors. In particular, translating one conductor independently is
not an allowed change of normalization.

**[THEOREM, source inputs]** The Heegner construction, its trace and
reduction relations, and its cohomological descent are as in
[Howard, arXiv:1202.6340v1, §1.7](https://arxiv.org/html/1202.6340#S1.SS7)
and [BCGS, arXiv:2312.09301v2, §1.1.2](https://arxiv.org/html/2312.09301v2#S1.SS1.SSS2).
For a fresh inert prime $r$, these relations are
$$
 \operatorname{Tr}_{H_{cr}/H_c}y_{cr}=a_r y_c,\qquad
 y_{cr}\equiv\operatorname{Frob}_r y_c
       \pmod{\mathfrak r}.
 \tag{3}
$$
The reduction equality uses a prime above r and the corresponding
arithmetic Frobenius acting on the reduction of the lower point.
Only primes away from cNpD occur here.

**[NEW] Lemma 1.1 (torsion needed for exact descent).**
$E(H_m)[p]=0$ under the stated irreducibility hypotheses.
The same conclusion holds for every ring class field $H_n$
with $p\nmid nD$.

*Proof.* The ring class field $H_m$ is Galois over Q and is unramified
at p, since $p\nmid mD$. Thus $E(H_m)[p]$ is a $G_{\mathbb Q}$-stable
subspace of E[p]. If nonzero, irreducibility makes it all of E[p].
The Weil pairing would then put $\mu_p$ in the unramified-at-p field
$H_m$, whereas $\mathbb Q(\mu_p)/\mathbb Q$ is ramified at p. This is
impossible for p>=3. The argument only used $p\nmid mD$, so applies
with any such n in place of m, including every $H_c$, $c\mid m$.
In particular there is no p-primary torsion in these Mordell-Weil groups.
$\square$

This proof does not require surjectivity over K. Howard's older global
theorems impose surjectivity; the present exact descent instead follows
from Lemma 1.1 and inflation-restriction. BCGS explicitly supplies the
Heegner system under its weaker torsion hypothesis. We do not transfer
Howard's older Selmer bound to a larger hypothesis range without BCGS.

## 2. An actual point, an exact cocycle, and its local normalization

Fix generators $\sigma_\ell,\sigma_q$ of the two inertia factors. Put
$$
 D_\ell=\sum_{i=1}^{\ell}i\sigma_\ell^i,\quad
 D_q=\sum_{j=1}^{q}j\sigma_q^j,\quad
 N_\ell=\sum_{i=0}^{\ell}\sigma_\ell^i.
$$
Let S be an actual set of representatives for $G/G_0$ and write
$S_G=\sum_{s\in S}s$. Define
$$
 A_m=S_GD_\ell D_q\in\mathbb Z[G],\qquad
 P_m=A_my_m\in E(H_m).
 \tag{4}
$$
This P_m is the specified lift whose height is computed below. There is
no division by the class number. Other transversals may change P_m while
giving the same class modulo $p^k$.

**[NEW, reconstruction of the descent] Proposition 2.1.**
The image of P_m in $E(H_m)/p^kE(H_m)$ is G-invariant. Its Kummer image
is the restriction of a unique class
$$
 \kappa_m^{\mathrm{raw}}\in H^1(K,E[p^k]).
 \tag{5}
$$
Furthermore
$$
 \kappa_m^{\mathrm{raw}}=0
 \quad\Longleftrightarrow\quad P_m\in p^kE(H_m).
 \tag{6}
$$

*Proof.* Telescoping gives $(\sigma_\ell-1)D_\ell=(\ell+1)-N_\ell$.
Apply (3) to obtain the exact point equality
$$
 (\sigma_\ell-1)P_m
 =S_GD_q\big((\ell+1)y_m-a_\ell y_q\big)
 \in p^kE(H_m),
 \tag{7}
$$
and interchange ell,q for the other equality. Already $D_\ell D_qy_m$
is $G_0$-invariant modulo $p^k$. Multiplication by any g in G permutes
S up to factors in $G_0$, proving the asserted full invariance. The same
argument proves independence of S modulo $p^k$.

The kernel and cokernel of restriction in (5) are the outer terms of
inflation-restriction with coefficient $E(H_m)[p^k]=0$, so restriction
is an isomorphism onto the invariants. Kummer is injective on
$E(H_m)/p^kE(H_m)$, proving both uniqueness and (6). $\square$

Here is a cocycle rather than a height assigned to a cohomology class.
Choose $Q\in E(\overline K)$ with $p^kQ=P_m$. For each $g\in G_K$
there is a unique $R_g\in E(H_m)$ with
$p^kR_g=(g-1)P_m$. Then
$$
 c_m(g)=(g-1)Q-R_g\in E[p^k].
 \tag{8}
$$
Uniqueness gives $R_{gh}=R_g+gR_h$, so (8) is a cocycle.
For $g\in G_{H_m}$, $R_g=0$ and its restriction is precisely the
Kummer cocycle of P_m. For a lift of $\sigma_\ell$,
$$
 R_{\sigma_\ell}=S_GD_q
 \left(\frac{\ell+1}{p^k}y_m-\frac{a_\ell}{p^k}y_q\right).
 \tag{9}
$$
These are integers in (9), with no omitted local divisibility factor.
Changing Q changes (8) by a coboundary.

**[THEOREM, local conditions and normalization]** The class (5) satisfies
the ordinary propagated Selmer conditions away from m and the transverse
conditions at ell and q, as in Howard Lemma 1.7.3 and BCGS §1.1.2.
At $\lambda\mid\ell$, the transverse condition is the kernel of
restriction to the relevant totally ramified local ring-class extension.
The local finite Frobenius is trivial on E[$p^k$], since
$a_\ell=0$ and $\ell=-1$ modulo $p^k$ imply
$\operatorname{Frob}_\ell^2=1$ on E[$p^k$]. The unramified local
evaluation after $D_\ell$ is multiplied by $\ell(\ell+1)/2$, hence is
zero modulo $p^k$. This verifies the transverse step directly.

The raw classes need the finite-singular correction to form the
normalized Kolyvagin system. To keep it visible, denote Howard's
automorphism $\chi_\ell$ by $\Xi_\ell$. Proposition 1.7.4 constructs it
from reduction, projection onto the p-Sylow group, the operation
$$
 p^{-k_\ell}\big(a_\ell-(\ell+1)\operatorname{Frob}_\ell\big),
 \tag{10}
$$
and lifting finite-field torsion. This is an operation on the specified
finite group, not an assertion that a formally divided matrix is
invertible on any lattice. The Frobenius eigencyclic lengths are
$v_p(\ell+1-a_\ell)$ and $v_p(\ell+1+a_\ell)$, and the resulting map
is an isomorphism. For a fresh ell its comparison is
$\Xi_\ell(\kappa_c^{\mathrm{raw}}(\operatorname{Frob}_\lambda))
=\kappa_{c\ell}^{\mathrm{raw}}(\sigma_\ell)$, with reduction to the
common coefficient quotient.

The local coefficient map in (10) must not simply be applied to
global cocycle values: it need not be $G_K$-equivariant. We therefore
replace the compressed induced-automorphism wording of Howard
Theorem 1.7.5 by the following explicit scalar normalization. This
also resolves the source-scope question under O5's weaker
irreducibility hypothesis.

**[NEW] Proposition 2.2 (signed normalization at the full coefficient).**
Let $w(E)$ be the functional-equation sign over Q and
$\epsilon_0=-w(E)$. For a squarefree Heegner conductor n with
r prime factors, put
$$
 \epsilon_r=\epsilon_0(-1)^r,\qquad
 u_r=\epsilon_0^r(-1)^{r(r-1)/2}.
$$
The classes
$$
 \kappa_n^{\mathrm{std}}=
 u_r\,\kappa_n^{\mathrm{raw}}\otimes_{v\mid n}\sigma_v
 \tag{11a}
$$
satisfy the finite-singular compatibility of a Kolyvagin system,
at every full common coefficient quotient. In particular
$$
 \kappa_{\ell q}^{\mathrm{std}}
 =-\kappa_{\ell q}^{\mathrm{raw}}\otimes\sigma_\ell\otimes\sigma_q,
 \qquad
 \kappa_{\ell q}^{\mathrm{std}}=0
 \Longleftrightarrow\kappa_{\ell q}^{\mathrm{raw}}=0.
 \tag{11}
$$

*Proof, first step: the global conjugation eigenvalue.*
Let $\tau$ be complex conjugation. For each c, the CM/Fricke
relation has the form
$$
 \tau y_c=\epsilon_0\sigma_cy_c+t_c,\qquad
 \sigma_c\in\operatorname{Gal}(H_c/K),\quad
 t_c\in E(H_c)_{\mathrm{tors}}.
$$
Here is the geometric reason for this relation. Write
$\mathfrak a=\mathfrak N\cap\mathcal O_c$.
Complex conjugation takes the target lattice
$\mathfrak a^{-1}$ in (2) to $\overline{\mathfrak a}^{-1}$.
The CM point associated with the ideal $\mathfrak a$ has
isogeny $\mathbb C/\mathfrak a\to\mathbb C/\mathcal O_c$.
Its Fricke dual is
$\mathbb C/\mathcal O_c\to\mathbb C/(N^{-1}\mathfrak a)$,
and $N^{-1}\mathfrak a=\overline{\mathfrak a}^{-1}$.
CM reciprocity identifies the first CM point with a Galois
translate of $x_c$ (the inverse depends on the declared Artin
convention and is immaterial here). On the f-quotient the
Fricke involution has eigenvalue $-w(E)=\epsilon_0$.
The normalization at infinity adds only the image of the
cuspidal divisor $(0)-(\infty)$, which is torsion by
Manin-Drinfeld. This proves the displayed relation.

The same CM relation is stated in
[Bertolini-Darmon, *Kolyvagin's descent and Mordell-Weil groups over
ring class fields*, Lemma 2.3, author PDF p. 4](https://www.math.mcgill.ca/darmon/pub/Articles/Research/04.Kolyvagin-descent/paper.pdf).
The publication is J. reine angew. Math. 412 (1990), 63–74,
[DOI 10.1515/crll.1990.412.63](https://www.degruyterbrill.com/document/doi/10.1515/crll.1990.412.63/html);
the author PDF has its own pagination and a 2007 file date.
That paper works under stronger residual assumptions; the
argument above uses those assumptions only through absence of
p-torsion, already proved here in Lemma 1.1. Its torsion error
is therefore zero modulo every $p^k$ under consideration.

On the ring class group $\tau g\tau^{-1}=g^{-1}$, and exactly
$$
 \tau D_v\tau^{-1}=(v+1)(N_v-1)-D_v
                    \equiv-D_v\pmod{p^k}
 \quad(k\le k_v).
$$
For general n, the calculation (7) at each prime factor shows
that $D_ny_n$ is invariant modulo $p^k$ under its inertia
product, and Lemma 1.1 gives the same exact restriction
isomorphism as in Proposition 2.1. For
$P_n=S_GD_ny_n$, the inverted and then $\sigma_n$-translated
transversal is another complete transversal. Since $D_ny_n$ is
invariant modulo $p^k$ under the inertia product, the proof of
Proposition 2.1 gives
$$
 \tau[P_n]=\epsilon_r[P_n]
       \quad\text{in }E(H_n)/p^kE(H_n).
$$
Kummer and the injective restriction map commute with the
**genuine** conjugation action on cohomology, so
$C\kappa_n^{\mathrm{raw}}=\epsilon_r\kappa_n^{\mathrm{raw}}$.
For n=1 the identical argument applies to the bottom trace in
$E(K)\otimes\mathbb Z_p$. This is the sign convention also
recorded in
[Jetchev-Lauter-Stein, arXiv:0707.0032, §3.2](https://arxiv.org/html/0707.0032#S3.SS2),
which cites Gross Proposition 5.4(ii). No stronger global theorem
from that paper is used.

*Second step: the local coefficient map and the transverse sign.*
At a fresh inert prime v, write $F=\operatorname{Frob}_v$ on
the good reduction. Fix a common coefficient $p^k$ with
$k\le\min(M(n),k_v)$. Choose a representative
$U\in E(\mathbb F_{v^2})$ of the point class in
$E(\mathbb F_{v^2})/p^k$ corresponding to the local Kummer class.
Choose $V\in E(\overline{\mathbb F}_v)$ with $p^kV=U$.
The finite Kummer evaluation is
$x=(F^2-1)V\in E[p^k]$. Cayley-Hamilton gives the exact identity
$$
 a_v-(v+1)F=(F-a_v)(F^2-1).
$$
The divided finite-group operation (10), computed using V, is
therefore $(F-a_v)x=Fx$ on E[$p^k$]. It is independent of V,
because $a_v-(v+1)F$ kills E[$p^k$]. Hence the local map
$\Xi_v$ is F under the finite Kummer evaluation. This proof
also shows compatibility with reduction from $p^{k_v}$ to $p^k$.

For a lift h of arithmetic Frobenius in $G_{\mathbb Q_v}$,
the cohomological action is
$$
 (C_hc)(g)=h\,c(h^{-1}gh).
$$
It represents C globally: h and $\tau$ differ by an element
of $G_K$, whose simultaneous conjugation action is a
coboundary on cocycles. At finite evaluation $g=h^2$ this
action is $x\mapsto Fx$. At tame transverse evaluation
$g=\sigma_v$, the relation
$h^{-1}\sigma_vh=\sigma_v^{v^{-1}}$ gives instead
$x\mapsto v^{-1}Fx=-Fx$ modulo $p^k$.
Evaluation is unaffected by coboundaries because both
$h^2$ and inertia act trivially on E[$p^k$].
Thus the transverse sign has not been suppressed.

In particular finite evaluation of the eigenclass
$\kappa_n^{\mathrm{raw}}$ obeys
$F\kappa_n^{\mathrm{raw}}(\operatorname{Frob}_\lambda)
=\epsilon_r\kappa_n^{\mathrm{raw}}(\operatorname{Frob}_\lambda)$.
Howard's local relation preceding this proposition becomes
$$
 \kappa_{nv}^{\mathrm{raw}}(\sigma_v)
  =\epsilon_r
       \kappa_n^{\mathrm{raw}}(\operatorname{Frob}_\lambda).
 \tag{11b}
$$
The flip $\epsilon_{r+1}=-\epsilon_r$ is consistent with
the just-computed transverse sign.

*Third step: normalize every edge by a scalar.*
The units $u_r$ satisfy $u_{r+1}\epsilon_r=u_r$. Multiply
(11b) by $u_{r+1}$ and insert the declared tensor generators.
The two resulting evaluations agree, which is exactly the
finite-singular compatibility of Howard Definition 1.2.3.
All other Selmer conditions are preserved by the scalar unit.
The recursion is independent of which fresh prime is added;
thus it works simultaneously on every edge and at every
common p-power. Finally $u_2=-1$, proving (11). $\square$

BCGS §1.1.2 explicitly defines the raw class by inverse restriction
before its unrecorded slight modification. We use (11a) as an
explicit choice of that normalization. The raw family and this
normalized family have exactly the same zero entries and
divisibility indices; no identification with an unspecified
author's scalar convention is needed for the O5 statement.
In the rest of this note $\kappa_n^{\mathrm{Heeg}}$ may mean
this normalized choice when a Kolyvagin system is required.
Equations (6) and (11) establish the vanishing comparison
used in (22). Neither a non-equivariant coefficient matrix
nor an assumed global extension of a local $\Xi_v$ is used.
The classical system is retained; its Iwasawa p-stabilization,
which has additional p-Euler factors, is not substituted.

## 3. Character expansion with matching conductors

Write $\widehat G$ for all complex characters. Adopt the projector
convention
$$
 e_\chi=\frac1{h_m}\sum_{g\in G}\chi(g)^{-1}g,\qquad
 Y_\chi(m)=\sum_{g\in G}\chi(g)^{-1}g y_m.
 \tag{12}
$$
For each chi, let $c_\chi\mid m$ be its exact ring-class conductor, and
let $\chi_c$ denote the corresponding primitive character at that
conductor. Define $Y_{\chi_c}(c_\chi)$ by the analogous unnormalized
sum at $H_{c_\chi}$. Use the Artin convention in which this is the
Heegner character sum in the Gross-Zagier formula below. With the other
reciprocity convention replace chi there by $\chi^{-1}$; nothing is
changed by dropping this replacement without declaring the convention.

Put
$$
 s_\chi=\sum_{s\in S}\chi(s),\qquad
 d_\ell(\chi)=
 \begin{cases}
   \ell(\ell+1)/2,&\chi(\sigma_\ell)=1,\\
   (\ell+1)/(\chi(\sigma_\ell)-1),&\chi(\sigma_\ell)\ne1,
 \end{cases}
 \tag{13}
$$
and define $d_q$ similarly. Evaluation of the telescoping identity
proves the second branch of (13); direct summation proves the first.
In particular, neither expression is replaced by a logarithmic
approximation at roots of unity.

**[NEW] Proposition 3.1 (actual toric decomposition).**
$$
 e_\chi P_m=\frac{s_\chi d_\ell(\chi)d_q(\chi)}{h_m}
      b_\chi Y_{\chi_c}(c_\chi),\qquad
 b_\chi=\prod_{r\mid m/c_\chi}a_r.
 \tag{14}
$$

*Proof.* Every g acts on the chi-eigenspace by chi(g), proving the
operator factor in (14). If chi factors through $H_c$, regroup its
unnormalized sum by $\operatorname{Gal}(H_m/H_c)$, then apply (3) once
for every removed prime. This proves
$Y_\chi(m)=b_\chi Y_{\chi_c}(c_\chi)$. There is no class-degree factor
in this equality because the character sums are unnormalized.
Dividing by $h_m$ only at (12) proves (14). $\square$

The factors $a_r$ in (14) are essential. A character imprimitive at
the larger conductor cannot be fed directly into a primitive
Gross-Zagier formula at that larger conductor with these factors omitted.

Use $\widehat h_K$ throughout with exactly the Néron-Tate normalization
over K in Cai-Shu-Tian Theorem 1.1, and its positive Hermitian extension
to $E(\overline K)\otimes\mathbb C$. In particular the convention is
kept fixed when the field of definition of a point changes. No
conversion to an absolute height, a Silverman half-height, or a BSD
regulator is made in this note. The associated pairing is G-invariant.
The character eigenspaces are orthogonal: pairing vectors with
eigencharacters chi,psi is multiplied by chi(g) conjugate(psi(g)),
which differs from one for some g unless chi=psi.

**[THEOREM, exact analytic input]**
[Cai-Shu-Tian, arXiv:1408.1733v2, Theorem 1.1](https://arxiv.org/html/1408.1733#S1.Thmthm1)
gives, in the current notation and conductor,
$$
 \widehat h_K(Y_{\chi_c}(c_\chi))
 =\frac{d_\pi c_\chi\sqrt{|D|}}
           {8\pi^2(f,f)_{\Gamma_0(N)}}\,
       L'(E/K,\chi_c,1),
 \qquad
 (f,f)_{\Gamma_0(N)}
   =\int_{\Gamma_0(N)\backslash\mathbb H}|f(z)|^2\,dx\,dy .
 \tag{15}
$$
Here the source's general factors $2^{-\mu(N,D)}$ and $u^{-2}$ in
the formula for L' equal one: $(N,D)=1$ and
$u=[\mathcal O_{c_\chi}^{\times}:\mathbb Z^\times]=1$.
Its hypotheses $(c_\chi,N)=1$, no inert prime dividing N, splitting
when a prime square divides N, and the additional condition at
$(N,D)$ all hold. Each primitive twist in (15) has sign -1.
L is the finite Rankin L-function, without the archimedean Euler
factor, with the source's finite local factors; the $8\pi^2$ is
therefore retained. The normalization $\pi(\infty)=O$ is required.
No assertion that the Manin constant is one is used, and $d_\pi$
absorbs the chosen parametrization exactly as the cited formula states.
The subsequent BSD conjecture displayed in that source is not an input.

**[NEW] Corollary 3.2 (height of the specified derivative point).**
Combining orthogonality with (14)-(15) gives the exact finite identity
$$
 \boxed{\displaystyle
 \widehat h_K(P_m)=
 \frac{d_\pi\sqrt{|D|}}
      {8\pi^2(f,f)_{\Gamma_0(N)}h_m^2}
 \sum_{\chi\in\widehat G}
 c_\chi\,
 |s_\chi d_\ell(\chi)d_q(\chi)|^2
 \left(\prod_{r\mid m/c_\chi}a_r^2\right)
 L'(E/K,\chi_c,1).}
 \tag{16}
$$
All summands are heights of the specified primitive toric points
times nonnegative scalars. This is a height identity for P_m in (4),
not a definition of a height on (5).

## 4. What fifth-order vanishing actually annihilates

The rank-zero auxiliary twist gives
$L(E/K,s)=L(E,s)L(E^D,s)$, so the derivatives of orders below five
vanish at 1. Let $P_K=\operatorname{Tr}_{H_1/K}y_1$.
Formula (15) for the trivial character says
$\widehat h_K(P_K)=0$. Thus P_K is torsion, hence zero in
$E(K)\otimes\mathbb Z_p$ by Lemma 1.1.

**[NEW] Proposition 4.1.** The rational trivial-character component of
P_m is
$$
 e_1P_m=\frac{a_\ell a_q\,\ell q}{4}P_K,
 \tag{17}
$$
so vanishes in the rational Mordell-Weil space under O5.
All other conductor-one components of P_m vanish regardless of rank.

*Proof.* Tracing (3) gives
$e_1y_m=a_\ell a_qP_K/h_m$. On the trivial component
$s_1=h_K$, $d_\ell(1)=\ell(\ell+1)/2$ and
$d_q(1)=q(q+1)/2$; substitute $h_m=h_K(\ell+1)(q+1)$.
For any nontrivial chi factoring through G/G_0,
$s_\chi$ is the sum of that character over the entire class group,
and is zero. $\square$

The surviving terms of (16) have exact conductor ell, q, or ell*q.
They involve first central derivatives of *different* Rankin L-functions.
Equation (16) contains neither the third nor the fourth derivative
of the untwisted function. It supplies no identity setting these
remaining terms to zero from untwisted fifth-order vanishing.
This observation is a statement about the actual formula, not a
claim that such arithmetic implications can never exist. We do not
assert nonvanishing of any of these twists for every chosen pair.

Even a full proof of (6) would not require $\widehat h_K(P_m)=0$:
P_m may be $p^k$ times a non-torsion point. Conversely, the quadratic
identity
$$
 \widehat h_K(P_m+p^kR)-\widehat h_K(P_m)
 =2p^k\langle P_m,R\rangle_K+p^{2k}\widehat h_K(R)
 \tag{18}
$$
shows why a height cannot be attached to an unspecified representative
of its residue class. Positivity detects torsion of the chosen point;
it does not by itself detect its divisibility by $p^k$.

## 5. A positive divisibility result in the actual character saturation

Let
$$
 M_m=E(H_m)\otimes\mathbb Z_p,\qquad
 B_m=\mathbb Q_p[G],\qquad
 \mathscr O_m=\text{the maximal }\mathbb Z_p\text{-order in }B_m.
$$
Since G is abelian, $B_m$ is a product of finite p-adic fields and
$\mathscr O_m$ is the product of their integer rings. Define the
actual enlarged Mordell-Weil lattice and its finite quotient
$$
 M_m^{\max}=\mathscr O_mM_m\subset M_m\otimes\mathbb Q_p,\qquad
 C_m=M_m^{\max}/M_m.
 \tag{19}
$$
All these groups are defined from the actual E and ring class field;
no model module replaces them. Lemma 1.1 and Mordell-Weil imply
that M_m is a free finite-rank $\mathbb Z_p$-module. The enlarged
lattice has the same rational span, so $C_m$ is finite.

Write $e_\ell=v_p(\ell+1)$ and $e_q=v_p(q+1)$, which can exceed
$k_\ell,k_q$ if the corresponding a-coefficient has smaller valuation.

**[NEW] Proposition 5.1 (two derivatives gain divisibility after saturation).**
$$
 A_m\in p^{\,e_\ell+e_q-1}\mathscr O_m
       \subset p^{\,2k-1}\mathscr O_m .
 \tag{20}
$$

*Proof.* Embed every simple factor of $B_m$ into $\overline{\mathbb Q}_p$.
Its embeddings are the p-adic characters of G. Formula (13) holds
for these characters as well. On the trivial ell-character,
$v_p(d_\ell)=e_\ell$, because p is odd and $\ell$ is a p-adic unit.
On a nontrivial character, write $\zeta=\chi(\sigma_\ell)$; then
$$
 v_p(d_\ell)=e_\ell-v_p(\zeta-1).
$$
If zeta has nontrivial prime-to-p part, $v_p(\zeta-1)=0$.
If it has exact p-power order $p^a$, then
$v_p(\zeta-1)=1/(p^{a-1}(p-1))\le1/(p-1)$.
The same estimates hold at q. Since $s_\chi$ is an algebraic
integer,
$$
 v_p(A_m(\chi))\ge e_\ell+e_q-\frac{2}{p-1}
                         \ge e_\ell+e_q-1.
$$
Membership in $p^b\mathscr O_m$ is tested in each field factor,
so this proves (20). No character projector is claimed integral
in $\mathbb Z_p[G]$. $\square$

Put
$$
 t_m=e_\ell+e_q-1-k\ge0,\qquad
 Q_m^{\max}=\frac{A_m}{p^k}y_m\in p^{t_m}M_m^{\max},
 \qquad
 \theta_m=[Q_m^{\max}]\in C_m.
 \tag{21}
$$
The symbol $Q_m^{\max}$ is a vector in a specified p-adic
Mordell-Weil lattice. It is not the algebraic division point Q
chosen for (8).

**[NEW] Proposition 5.2 (exact residual class).**
$$
 \theta_m\in C_m[p^k]^G\cap p^{t_m}C_m,\qquad
 \boxed{\quad\kappa_m^{\mathrm{Heeg}}=0
                \ \Longleftrightarrow\ \theta_m=0.\quad}
 \tag{22}
$$

*Proof.* Tensor $0\to M_m\to M_m^{\max}\to C_m\to0$
with $\mathbb Z_p/p^k$. The resulting exact sequence is
$$
 0\longrightarrow C_m[p^k]
 \xrightarrow{\ j_k\ } M_m/p^kM_m
 \longrightarrow M_m^{\max}/p^kM_m^{\max}
 \longrightarrow C_m/p^kC_m\longrightarrow0,
 \tag{23}
$$
where $j_k([Q])=p^kQ\bmod p^kM_m$ for a lift Q in
$M_m^{\max}$. Now $p^kQ_m^{\max}=P_m$, so
$j_k(\theta_m)$ is precisely the class of P_m. Its G-invariance
and injectivity of $j_k$ give $\theta_m\in C_m[p^k]^G$.
Its stated depth in C_m follows from (21).

For a finitely generated abelian group without p-primary torsion,
the natural map
$E(H_m)/p^kE(H_m)\to M_m/p^kM_m$ is an isomorphism.
Consequently $\theta_m=0$ is equivalent to (6), and (11)
preserves this vanishing. $\square$

Equations (21)-(23) preserve the **full** p-power in O5.
They do not merely test the residual mod-p class. In particular:
$$
 p^{t_m}C_m=0\quad\Longrightarrow\quad
 \kappa_m^{\mathrm{Heeg}}=0.
 \tag{24}
$$
Conversely a nonzero class would require the exponent of $C_m$
to be at least $p^{t_m+1}=p^{e_\ell+e_q-k}$.
These are statements about the actual Mordell-Weil lattice in (19).

**[NEW] Lemma 5.3 (the elementary conductor bound is too weak).**
Let $b_m=v_p(h_m)=v_p(h_K)+e_\ell+e_q$. Then
$$
 p^{b_m}C_m=0.
 \tag{25}
$$

*Proof.* If $x\in\mathscr O_m$, write $x=\sum_g x_g g$ in
$\mathbb Q_p[G]$. Fourier inversion says
$h_m x_g=\sum_\chi x(\chi)\chi(g)^{-1}$.
The right side is a p-adic algebraic integer; since the left side
lies in $\mathbb Q_p$, it is in $\mathbb Z_p$. Thus
$h_m\mathscr O_m\subset\mathbb Z_p[G]$, proving (25). $\square$

This argument misses the sufficient exponent in (24) by
$b_m-t_m=v_p(h_K)+k+1$. Making the auxiliary congruences deeper
does not remove this deficit. Neither finiteness of each M_m nor
decomposing its rational character spaces proves (24).

## 6. The precise remaining geometric comparison

**[GAP TP5, integral Heegner divisibility].**
For every E,p,K satisfying §1 with odd analytic rank of E at least
five, and every pair ell,q satisfying (1), prove
$$
 \frac{S_GD_\ell D_q}{p^k}y_{\ell q}
       \in E(H_{\ell q})\otimes\mathbb Z_p
       \quad\text{inside }M_{\ell q}^{\max}.
 \tag{26}
$$
Equivalently, prove that the explicitly defined class
$\theta_{\ell q}$ in (21) is zero. By (22) and the reviewed O5
equivalence, (26) for every pair gives $s_p(E)\ge5$.
It does not by itself prove rank equality, full Sha finiteness,
or the leading coefficient.

This attempt already constructs the candidate divided point in
$M_m^{\max}$ and proves its depth there. The first unresolved step
is its descent to the *actual* Mordell-Weil lattice $M_m$.
Its image under the injection (23), Kummer and inverse restriction
is exactly the raw O5 class. Thus the missing term in a proposed
characterwise argument is now an explicit finite arithmetic
cokernel element, not an unspecified error term.

A stronger sufficient geometric statement is the bound in (24)
for these Mordell-Weil character-saturation quotients under the
rank-five hypotheses. No proof of that bound has been obtained,
and it should not be presumed true merely because it is sufficient.
The more targeted (26) could hold even when that stronger bound
fails for other points.

The actual height calculation attempts to test (26) as follows.
The untwisted vanishing annihilates (17), and (16) computes the
remaining positive toric components. Over $\mathbb Q_p[G]$ the
candidate is already divisible, by (20). All rational character
and real-height tests therefore omit exactly the lattice quotient
in (23). An additional integral comparison must control that
quotient or this particular element. No identification of a
complex derivative with $\theta_m$, nor a canonical reduction
modulo $p^k$ of a complex height, has been constructed here.

One entirely explicit pairing formulation is also available:
since C_m is a finite p-group, its characters
$\lambda:C_m\to\mathbb Q_p/\mathbb Z_p$ separate points.
Consequently (26) is equivalent to
$$
 \lambda(\theta_m)=0
       \quad\text{for every such }\lambda.
 \tag{27}
$$
A geometric higher Gross-Zagier comparison would suffice if it
constructed these values from the vanishing untwisted third
central derivative with all integral normalization factors and
proved their vanishing. Such a comparison is an explicit open
construction target, not a theorem supplied by (15). Formula
(27) involves a finite arithmetic pairing and so does not assign
a height to an unspecified cohomology lift.

The result of this bounded attack is (4)-(16), together with the
positive maximal-order divisibility (20) and its exact residual
class (22). The fifth-order analytic hypothesis currently reaches
only (17) through the cited Gross-Zagier formula. The extra
arithmetic descent in (26) remains unresolved.

## 7. Source and verification scope

- Howard, *The Heegner point Kolyvagin system*, arXiv:1202.6340v1,
  §1.7, Lemmas 1.7.1-1.7.3, Proposition 1.7.4; Definition 1.2.3:
  actual CM points, norm/reduction identities, cocycles, transverse
  conditions and local finite-singular correction. Proposition 2.2
  above replaces Theorem 1.7.5's compressed global-automorphism
  language by an explicit signed scalar. The older global
  surjectivity hypothesis is not imported into O5.
- Burungale-Castella-Grossi-Skinner, *Non-vanishing of Kolyvagin
  systems and Iwasawa theory*, arXiv:2312.09301v2, §1.1.2:
  classical Heegner construction under the stated torsion condition,
  full coefficient quotients and modification. Its corank theorem
  is used only through the reviewed odd-rank note.
- Cai-Shu-Tian, *Explicit Gross-Zagier and Waldspurger Formulae*,
  arXiv:1408.1733v2, Theorem 1.1: exact primitive conductor formula,
  Petersson normalization, units, common-prime and parametrization
  factors. The unversioned HTML identifies itself as v2 of
  18 November 2014; the direct v2 HTML URL returned a server error.

The indicated primary passages were read directly. No numerical
certificate was rerun, no new package installed, and no finite-Sha
or BSD conjecture in those sources used. All algebraic derivations
tagged [NEW] above are written on the page and passed the linked
independent review, including the signed normalization repair.
The integral descent statement TP5 remains unresolved.
