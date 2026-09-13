# Derived comparison: an explicit attack and its surviving reductions

Date: 2026-09-12. Scope: the higher complex leading coefficient, determinant
descent, and finite-character interpolation. This file follows the
[charter](../00-charter.md), and supplements
[approach G, §§2.3–2.4](../approaches/G-motivic-bloch-kato.md) and the
[mixed-character computation](continuation-2026-09-12.md).
Every `[NEW]` below is an elementary deduction, not a claim of historical
novelty. Coordinator review on 2026-09-12 passed Lemmas 2.1–2.2 and
Propositions 4.2 and 6.1, including the cofactor signs, functional equation,
and all-prime divisibility argument. Other `[NEW]` statements remain pending
independent review.

The attack yields three useful conclusions with proofs. First, a cofactor
version of determinant descent needs less height nondegeneracy than a scalar
regulator quotient. Second, even all nontrivial twist valuations, the central
rank, and an exact inversion functional equation do not determine the central
coefficient valuation of a bounded power series. Third, all-prime one-sided
complex divisibility, rationality, and a coarse archimedean bound can imply
full BSD without identifying any local unit. The required comparison of the
complex coefficient with the arithmetic determinant is not proved here.

## 1. Conventions and verification of the sources

Let $E/\mathbb Q$ be an elliptic curve and suppose, whenever a leading-term
statement below is made, that
$r=\operatorname{rank}E(\mathbb Q)=\operatorname{ord}_{s=1}L(E,s)$ has already
been proved. Set
$$
\ell_E=\frac{L^{(r)}(E,1)}{r!},\qquad
c_E=\frac{\ell_E}{\Omega_E R_\infty},\qquad
t=\#E(\mathbb Q)_{\rm tors},\qquad C=\prod_{q\mid N}c_q.
$$
Here $\Omega_E=\int_{E(\mathbb R)}|\omega|$ for a minimal Néron differential,
and $R_\infty$ is the Néron–Tate regulator of a saturated basis of the free
Mordell–Weil group. Thus the all-prime target is $c_E=\#\operatorname{Sha}\,C/t^2$.
No valuation of $c_E$ is used until its rationality is an explicit hypothesis.

**[THEOREM, source audit].** Burns–Kurihara–Sano (BKS),
[arXiv:1910.07404v2](https://arxiv.org/abs/1910.07404v2), was published in
*J. Math. Soc. Japan* **76**(3) (2024), 855–919,
[DOI 10.2969/jmsj/90699069](https://doi.org/10.2969/jmsj/90699069).
The [published PDF](https://kurihara.math.keio.ac.jp/bks4.pdf), including
Hypothesis 2.2 and Theorems 7.3, 7.6, 7.8, was checked directly.
Hypothesis 2.2 requires $H^1(\mathbb Z_S,T)$ free over $\mathbb Z_p$, $r>0$,
and $\operatorname{Sha}[p^\infty]$ finite. Theorem 7.3 descends the integral main conjecture
to an arithmetic derived formula up to a unit. Theorem 7.6 additionally needs
the generalized Perrin–Riou comparison and a nonzero Bockstein regulator to
obtain $\mathrm{BSD}_p$. The infinite-level conjecture is numbered **4.8 in
the publication**, versus **4.9 in arXiv v2**. Theorem 5.6 and Lemma 5.9
relate the Bockstein vector to the height pairing.

**[THEOREM, source audit].** The companion paper,
[arXiv:2103.11535v1](https://arxiv.org/abs/2103.11535v1), is
*International Mathematics Research Notices* **2025**(4), rnaf012,
[DOI 10.1093/imrn/rnaf012](https://doi.org/10.1093/imrn/rnaf012);
publication metadata were checked against the
[author's institutional record](https://kclpure.kcl.ac.uk/portal/en/publications/on-derivatives-of-katos-euler-system-and-the-mazur-tate-conjectur/).
Its [Theorem 1.1](https://arxiv.org/html/2103.11535v1#S1)
has **BSD over $\mathbb Q$ as hypothesis (d)**, in addition to its field,
residual-image, and generalized Perrin–Riou hypotheses. It cannot be applied
as an independent proof of BSD. Definition 4.3 constructs a determinantal
zeta element; Proposition 4.4 identifies its specialization with the
arithmetic BSD element **conditionally on Conjecture 3.4**. Construction of
the element alone is not this identification.

The proofs below use explicit linear algebra and power series, rather than
adding any unverified arithmetic theorem to these inputs.

## 2. What a first Bockstein actually computes

**[NEW] Lemma 2.1 (determinant coefficient with its torsion factor).**
Let $\mathcal O$ be a discrete valuation ring with fraction field $K$ and
valuation $v$, and let $D(T)\in M_n(\mathcal O[[T]])$. Suppose
$\operatorname{rank}_K D(0)=n-r$. Choose integral Smith bases in which
$$
D(0)=\operatorname{diag}(d_1,\ldots,d_{n-r},0,\ldots,0),\quad d_i\ne0.
$$
Let $H\in M_r(\mathcal O)$ be the bottom-right block of the coefficient of
$T$ in these bases. It is the matrix of the connecting map
$$
\beta:\ker D(0)\longrightarrow\operatorname{coker}D(0)_{\rm tf}
$$
obtained by lifting modulo $T^2$, dividing the differential by $T$, and
projecting to the torsion-free cokernel. Then, in these bases,
$$
\det D(T)=T^r\left(\prod_{i=1}^{n-r}d_i\right)\det H+O(T^{r+1}). \tag{2.1}
$$
If $\det H\ne0$, the order is exactly $r$, and in the original integral
bases
$$
v([T^r]\det D)=
\operatorname{length}_{\mathcal O}(\operatorname{coker}D(0)_{\rm tors})
+v(\det H). \tag{2.2}
$$

*Proof.* Write $D=\left(\begin{smallmatrix}A&B\\C&F\end{smallmatrix}\right)$
with $A(0)=\operatorname{diag}(d_i)$ and $B(0)=C(0)=F(0)=0$.
Over $K[[T]]$, $A$ is invertible, so block elimination gives
$$
\det D=\det A\det(F-CA^{-1}B).
$$
Here $CA^{-1}B\in T^2M_r(K[[T]])$ and $F=TH+O(T^2)$. This proves (2.1).
The Smith torsion has length $\sum_i v(d_i)$; the determinants of the
integral basis changes are units. Taking valuations proves (2.2). The
description of $\beta$ follows directly by applying $D(T)$ to a vector in
the final $r$ basis directions. $\square$

The factors $d_i$ are essential. Replacing the integral complex by its
rational cohomology before taking this coefficient loses the torsion factor.
If $\det H=0$, (2.1) gives a zero coefficient, not permission to divide by
the regulator. Higher terms of the Schur complement are then needed.

**[NEW] Lemma 2.2 (the rank-one cofactor form).** Let instead
$D(T)\in M_{m,m+1}(\mathcal O[[T]])$, and suppose
$\operatorname{rank}_KD(0)=m-r+1=:k$. In integral Smith bases take
$D(0)$ to have its nonzero diagonal $d_1,\ldots,d_k$ in its first $k$
rows and columns. Let $B\in M_{r-1,r}(\mathcal O)$ be the bottom-right
block of $[T]D(T)$. For an $m$ by $m+1$ matrix $M$ put
$$
\operatorname{cof}(M)_j=(-1)^{j+1}\det M_{\widehat j},
$$
where column $j$ is omitted. Then
$$
\operatorname{cof}(D(T))=
(-1)^kT^{r-1}\left(\prod_{i=1}^kd_i\right)
(0,\ldots,0,\operatorname{cof}(B))+O(T^r). \tag{2.3}
$$
In particular the first derived cofactor is nonzero exactly when
$\operatorname{rank}_K B=r-1$.

*Proof.* Each of the bottom $r-1$ rows is divisible by $T$.
For a minor omitting a bottom-block column, the coefficient of $T^{r-1}$
is $\prod_i d_i$ times the corresponding maximal minor of $B$: after
factoring these $T$'s and reducing modulo $T$, the top block is diagonal
and its top-right block is zero. Its cofactor sign changes by $(-1)^k$.
If a top-block column is omitted, the same reduction leaves its top row
identically zero, so that minor is divisible by $T^r$. This proves (2.3),
including the cases $k=0$ or $r=1$, with empty determinant equal to one.
A matrix with $r-1$ rows has a nonzero maximal minor precisely when it has
row rank $r-1$. $\square$

**[CONDITIONAL, arithmetic interpretation].** When an arithmetic complex
has the two-term integral presentation used in BKS descent, (2.3) explains
why a rank-one zeta class can have a first nonzero derivative of degree
$r-1$ and why its coefficient includes a torsion factor. This calculation
does not identify its image under an archimedean period map. Applying it
to an elliptic curve requires the integral presentation and local
normalizations; the linear-algebra lemma supplies neither automatically.

## 3. A vector comparison can survive a degenerate height

**[NEW] Lemma 3.1 (cofactor test).** Let $H$ be a symmetric $r$ by $r$
matrix over a characteristic-zero field $K$ and let $l\in K^r$ be a
nonzero column representing a linear functional on $K^r$. Define
$$
R(H,l)=\operatorname{adj}(H)l.
$$
Then
$$
H R(H,l)=\det(H)l. \tag{3.1}
$$
Moreover:

1. If $H$ is invertible, $R(H,l)\ne0$.
2. If $\operatorname{rank}H=r-1$, then $R(H,l)\ne0$ exactly when $l$
   does not vanish on $\ker H$.
3. If $\operatorname{rank}H\le r-2$, then $R(H,l)=0$.

*Proof.* The adjugate identity proves (3.1) and the first assertion.
In the second case the adjugate is a nonzero matrix of rank one. Its
columns and rows lie in the same one-dimensional kernel, because $H$ is
symmetric. Thus, for a nonzero kernel column $v$, it has the form
$a vv^{\mathsf t}$ with $a\ne0$. Its product with $l$ is nonzero exactly
when $v^{\mathsf t}l=l(v)\ne0$. In the last case every $(r-1)$-minor
vanishes. This also covers $r=1$ using the empty minor convention.
$\square$

There is an explicit exterior-power interpretation, so (3.1) is not the
only information being used. Regard row $i$ of $H$ as a covector $h_i$.
The $i$th coordinate of $R(H,l)$ is the coefficient of the standard
volume form in
$$
h_1\wedge\cdots\wedge h_{i-1}\wedge l\wedge
h_{i+1}\wedge\cdots\wedge h_r. \tag{3.2}
$$
Indeed its coefficient is $\sum_j\operatorname{cof}_{ij}(H)l_j$, and the
cofactor matrix is symmetric. If $\ker l$ is used as the $(r-1)$-dimensional
target dual, these are exactly the signed maximal minors of the restricted
height map, with the volume normalization specified by $l$.

**[THEOREM/NEW, interpretation].** In the good ordinary setting of BKS §5.2, under Hypothesis 2.2,
formula (3.2) is the linear algebra in Lemma 5.9, with
$l=\log_\omega$ and the height matrix $H_p$, after choosing the
augmentation coordinate and the determinant bases used there.
It gives the Bockstein vector in the corresponding coordinates. Thus the
condition that this vector be nonzero can be strictly weaker than
$\det H_p\ne0$. For example
$$
H=\operatorname{diag}(1,\ldots,1,0),\qquad l=e_r
\quad\Longrightarrow\quad R(H,l)=e_r\ne0,
\quad\det H=0.
$$
This example is linear algebra, not a claim that a specific elliptic curve
has this height matrix. It shows why the vector condition in BKS Theorem
7.6 should be retained rather than strengthened without need.

**[NEW] Lemma 3.2 (lattice cancellation without a pairing).** If $V$ is a
$\mathbb Q_p$-vector space, $R\in V\setminus\{0\}$, and $a,b\in\mathbb Q_p^\times$,
then
$$
\mathbb Z_p(aR)\subseteq\mathbb Z_p(bR)
\iff v_p(a)\ge v_p(b).
$$
Equality is equivalent to equality of valuations.

*Proof.* The map $\mathbb Q_p\to V$, $x\mapsto xR$, is injective. Pull
back the inclusion and compare fractional ideals of $\mathbb Z_p$.
$\square$

For example, if descent proves $\kappa=uA_pR$ with $u\in\mathbb Z_p^\times$
and $R\ne0$, then a comparison merely of lattices
$\mathbb Z_p(c_ER)=\mathbb Z_p\kappa$ already gives the desired valuation;
identifying $u$ is unnecessary. Even the inclusion
$c_ER\in\mathbb Z_p\kappa$ gives the one-sided inequality used in §6.
All explicit period and Euler factors must be included in both $c_E$ and
$A_p$ before making this cancellation. The deduction fails for $R=0$.

## 4. Finite-character interpolation: exact values versus valuations

**[NEW] Lemma 4.1 (the topology and bounded uniqueness).** For odd $p$,
let $t_n=\zeta_{p^n}-1$, with $\zeta_{p^n}$ primitive. Then
$$
v_p(t_n)=\frac1{p^{n-1}(p-1)}=:\delta_n.
$$
In particular $|t_n|_p\to1$; these parameters do not tend to zero.
For a nonzero bounded series
$F(T)=\sum_{j\ge0}a_jT^j\in\mathbb Q_p\otimes_{\mathbb Z_p}\mathbb Z_p[[T]]$,
set
$$
\mu=\min_j v_p(a_j),\qquad
\lambda=\min\{j:v_p(a_j)=\mu\}.
$$
For every sufficiently large $n$,
$$
v_p(F(t_n))=\mu+\lambda\delta_n. \tag{4.1}
$$
Consequently two bounded series agreeing at primitive torsion points of
unbounded order agree identically.

*Proof.* Every primitive $p^n$th root has the same $p$-adic distance from
one by Galois invariance. The product of $1-\zeta_{p^n}^a$ over primitive
exponents is $\Phi_{p^n}(1)=p$, proving the valuation formula. Since the
coefficient valuations are integers bounded below, $\mu$ and $\lambda$
exist. For $j>\lambda$, the valuation of $a_jt_n^j$ is strictly larger than
$\mu+\lambda\delta_n$. For each of the finitely many $j<\lambda$ choose
$n$ so large that
$$
v_p(a_j)-\mu>(\lambda-j)\delta_n.
$$
The $\lambda$th term is then the unique term of least valuation in the
convergent series, proving (4.1). Apply this to the difference of two
series for uniqueness. $\square$

Thus correct, exact interpolation of a bounded $p$-adic $L$-function does
fix the series and all its $p$-adic derivatives. Boundary topology alone
does not create an ambiguity. The boundedness hypothesis matters:
$\log(1+T)$ is a nonzero analytic function on $|T|_p<1$ vanishing at every
$t_n$, and its coefficients $(-1)^{j+1}/j$ have unbounded denominators.
The vanishing follows from
$p^n\log\zeta_{p^n}=\log(\zeta_{p^n}^{p^n})=0$.

**[NEW] Proposition 4.2 (all twist valuations still lose the central
coefficient, even with rank and symmetry fixed).** Let $p\ge5$, $r\ge0$,
and set
$$
\iota(T)=-\frac{T}{1+T},\qquad u(T)=\frac{T}{2+T},\qquad
F_a(T)=u(T)^r\bigl(p^a+u(T)^2\bigr),\quad a\ge1.
$$
These belong to $\mathbb Z_p[[T]]$, satisfy the exact functional equation
$$
F_a(\iota(T))=(-1)^rF_a(T),
$$
have the same central order $r$, and have the same $(\mu,\lambda)=(0,r+2)$.
At **every** nontrivial $p$-power torsion parameter $t_n$ they satisfy
$$
v_p(F_a(t_n))=(r+2)\delta_n,
$$
independently of $a$. Nevertheless
$$
[T^r]F_a(T)=\frac{p^a}{2^r},\qquad
v_p([T^r]F_a)=a.
$$
Also $G(T)=u(T)^{r+2}$ has the same symmetry and all the same torsion-value
valuations, but has central order $r+2$.

*Proof.* Since $2$ is a unit, $u$ is an integral formal parameter and
$u(\iota(T))=-u(T)$. The stated central coefficient follows from
$u(T)=T/2+O(T^2)$. Reduction modulo $p$ gives $u^{r+2}$, proving the
$(\mu,\lambda)$ assertion. At $t_n$, $2+t_n$ is a unit, so
$v_p(u(t_n))=\delta_n$. Since $2\delta_n\le2/(p-1)<1\le a$, the two
terms in $p^a+u(t_n)^2$ have different valuations and the second is smaller.
The claims follow by the ultrametric inequality. $\square$

These are counterexamples to a proposed implication for bounded power
series. They are not presented as $L$-functions of elliptic curves. They
show precisely that a proof using only twist valuations, boundedness,
rank and inversion symmetry is missing additional arithmetic information.
They do not invalidate exact interpolation, an exact characteristic ideal,
or any arithmetic theorem using more than these data.

## 5. Trying to turn the mixed character difference into a complex derivative

The earlier lemma gives, for integral modular-symbol coefficients $b_x$
and order-$p$ characters $\chi_i(x)=\zeta_p^{k_i(x)}$,
$$
D=\sum_x b_x\prod_{i=1}^m(\zeta_p^{k_i(x)}-1),\qquad
\frac{D}{(\zeta_p-1)^m}\bmod(\zeta_p-1)
=\sum_x\bar b_x\prod_i\bar k_i(x). \tag{5.1}
$$
This is an exact integral augmentation statement. Proper-subset
interpolation terms remain imprimitive at the original modulus and require
the Euler corrections proved in the earlier file.

**[NEW] Lemma 5.1 (the proposed archimedean limiting step is not uniform).**
Under the complex embedding $\zeta_p=e^{2\pi i/p}$, the approximation
$$
\frac{\zeta_p^k-1}{\zeta_p-1}\sim k
$$
as $p\to\infty$ is not uniform for $0\le k<p$. In particular, for
$k=(p-1)/2$ the quotient divided by $k$ tends to $2i/\pi$, not one.

*Proof.* In this case $\zeta_p^k=-e^{-\pi i/p}$, so the numerator tends
to $-2$. The denominator $k(\zeta_p-1)$ tends to $\pi i$. Their ratio
tends to $2i/\pi$. $\square$

Discrete logarithms in (5.1) range across all of $\mathbb F_p$, while their
moduli and the summation sets also change. Consequently a termwise use of
this approximation cannot turn (5.1) into an archimedean derivative. A
dominated convergence estimate and an identification of the resulting
weight would both need proof.

**[NEW] Lemma 5.2 (fixed finite characters have no complex tangent).**
If $G$ is finite and $z\mapsto\chi_z$ is a family of characters
$G\to\mathbb C^\times$ such that each $\chi_z(g)$ is holomorphic on a
connected complex domain, then the family is constant.

*Proof.* For each $g$ of order $d$, $\chi_z(g)^d=1$. A continuous map
from a connected set into the finite set of $d$th roots is constant.
$\square$

For comparison, the complex central derivative is a Mellin derivative.
**[NEW, elementary analytic calculation].** If $f_E$ is the normalized
weight-two cusp form and
$$
M(s)=\int_0^\infty f_E(iy)y^{s-1}\,dy,
$$
then $L(E,s)=(2\pi)^sM(s)/\Gamma(s)$. Exponential cusp decay at infinity
and, by the modular transformation at zero, a bound of the form
$O(y^{-2}e^{-c/y})$ there justify every differentiation locally uniformly
in $s$. If the order at one is $r$, multiplication by the nonvanishing
factor $(2\pi)^s/\Gamma(s)$ gives
$$
\ell_E=\frac{2\pi}{r!}
\int_0^\infty f_E(iy)(\log y)^r\,dy. \tag{5.2}
$$
Indeed $M$ has the same order, so all lower Leibniz terms vanish.
The Mellin identity itself follows by integrating the Fourier expansion
termwise in its half-plane of absolute convergence, then continuing
analytically using the convergent cusp integral.

The first missing step in the proposed passage is now explicit: there is
no proved identity replacing the discrete weights in (5.1), after their
changing local and Gauss-sum normalizations, by the Mellin weight
$(\log y)^r$ in (5.2), followed by division by $R_\infty$. The two lemmas
disprove the immediate continuity argument; they do not prove that a more
substantial arithmetic identity is impossible.

Likewise an abstract embedding of $\mathbb R$ into $\mathbb C_p$, used to
state comparison conjectures, supplies no continuity argument. **[NEW]**
there is no continuous unital field embedding of $\mathbb R$ into
$\mathbb C_p$: its additive image would be connected and therefore a
singleton in a totally disconnected field. Such abstract embeddings fix
rational numbers; proving $c_E\in\mathbb Q$ would remove their ambiguity
for $c_E$, but would still not identify its arithmetic lattice.

## 6. The units can be bypassed: a one-sided and archimedean reduction

**[NEW] Proposition 6.1 (one-sided global criterion).** Suppose the rank
equality for $E$ has been proved. Suppose further that:

1. $c_E\in\mathbb Q_{>0}$;
2. $\operatorname{Sha}(E/\mathbb Q)[p^\infty]$ is finite for **every** prime $p$;
3. for every prime $p$ one has
   $$
   v_p\left(c_E\frac{t^2}{C}\right)
   \ge \log_p\#\operatorname{Sha}(E/\mathbb Q)[p^\infty]. \tag{6.1}
   $$

Then $n_E:=c_Et^2/C$ is a positive integer, the full group $\operatorname{Sha}$ is
finite, and $\#\operatorname{Sha}$ divides $n_E$. If, in addition, a positive real
number $h$ is proved to satisfy $h\le\#\operatorname{Sha}$ and
$$
n_E<2h, \tag{6.2}
$$
then full BSD holds: $n_E=\#\operatorname{Sha}$. In particular $0<n_E<2$, together
with the three hypotheses, proves both BSD and $\operatorname{Sha}=0$.

*Proof.* The right side of (6.1) is a nonnegative integer. Hence the
positive rational $n_E$ has nonnegative valuation at every prime and is
an integer. Its prime support is finite. Outside this support (6.1)
implies $\operatorname{Sha}[p^\infty]=0$. Inside it the groups are finite by hypothesis.
Since $\operatorname{Sha}$ is torsion, its primary decomposition is therefore a finite
direct sum of finite groups. Taking the product of (6.1) over this finite
support gives $\#\operatorname{Sha}\mid n_E$. Consequently
$n_E/\#\operatorname{Sha}$ is a positive integer; (6.2) makes it less than two. It is
one. For the last assertion use the unconditional lower bound $h=1$ on
the order of a finite group. $\square$

This proof does not assume a finite exceptional set for $\operatorname{Sha}$ in advance:
the rational comparison number supplies it. It does require (6.1) at
every prime, including $2$, bad primes, and supersingular primes. A
good-ordinary theorem alone does not supply that premise. It also does
not deduce local finiteness from the orders of finite Selmer quotients.

**[NEW] Corollary 6.2 (valuation equality and positivity suffice).** With
rank equality, local finiteness at all primes, and $c_E\in\mathbb Q_{>0}$,
replace (6.1) by equality at every prime. Then full BSD follows without
(6.2).

*Proof.* Proposition 6.1 supplies global finiteness. The positive rational
$n_E/\#\operatorname{Sha}$ has valuation zero at all primes, so its numerator and
denominator in lowest terms are both one. $\square$

One-sided divisibility is enough for the first proposition, which is
strictly less than a comparison with each specific $p$-adic unit. Mere
positivity cannot replace (6.2) in the one-sided version: the positive
integer $n_E/\#\operatorname{Sha}$ could be two or larger. Neither proposition proves
rationality of $c_E$ or the complex comparison inequality.

**[GAP V, the weakened comparison target].** Let $E/\mathbb Q$ have proved
equal algebraic and analytic rank $r\ge2$, and assume
$\operatorname{Sha}[p^\infty]$ finite for every $p$ and $c_E\in\mathbb Q_{>0}$, with
$c_E,\Omega_E,R_\infty,t,C$ as in §1. Prove (6.1) for every prime $p$.
This is a precise one-sided leading-term problem. Coupled with (6.2), it
would finish BSD for the curve; it does not ask for exact local units or
reverse divisibility.

**[GAP D, a concrete route toward Gap V at one prime].** Fix an $E$ as in
Gap V and an odd prime $p$. Put $T=T_pE$, and choose $S$ containing
$\infty,p$ and all bad primes. Assume $H^1(\mathbb Z_S,T)$ is
$\mathbb Z_p$-free. In the BKS determinant line, include all local and
period factors to use the fundamental-line coordinate of §1, in which
the arithmetic lattice has coordinate
$$
\#\operatorname{Sha}[p^\infty]\,C/t^2\quad\text{up to }\mathbb Z_p^\times.
$$
Assume that the specialized Kato determinant element is nonzero and
belongs to this integral lattice, and denote its coordinate by
$d_p\in\mathbb Q_p^\times$. Assume its Bockstein map is nonzero on the
fundamental line. These are explicit premises; they are not claimed for
every prime by the construction alone.
Prove the weaker comparison
$$
c_E\in d_p\mathbb Z_p. \tag{6.3}
$$
Here integrality of the determinant element is an explicit premise, so
$v_p(d_p)\ge v_p(\#\operatorname{Sha}[p^\infty]C/t^2)$; with the integral main conjecture
this is equality. Equation (6.3), or equivalently the corresponding
inclusion of Bockstein-vector lattices by Lemma 3.2, would imply (6.1)
at $p$. This statement deliberately specifies the required comparison
and normalization instead of treating the characteristic ideal as a
canonical scalar.

The serious attempt at (6.3) in this file was to descend known twisted
interpolation and retain only valuations. Lemma 2.1 and Lemma 2.2 prove
the arithmetic part of that descent. Lemma 4.1 validates uniqueness when
the complete interpolation values are retained. Proposition 4.2 shows
exactly why replacing them by valuations cannot identify the central
coefficient, even after rank and symmetry are supplied. Lemmas 5.1–5.2
rule out the proposed automatic passage to (5.2). None of these steps
proves (6.3).

## 7. Normalization and logical checks for applying the criterion

The following are requirements of the displayed formulas, not further
conjectures being silently added.

- A regulator from a finite-index point lattice is the saturated
  regulator multiplied by the square of that index. Its use changes
  $n_E$, and can invalidate the interval criterion unless corrected.
- BKS use $\Omega^+$ in their conventions. Its ratio to the full real
  period in §1 must be retained at $2$; an odd-prime comparison cannot
  dispose of that factor in the all-prime criterion.
- For $L_S(E,s)=L(E,s)\prod_{q\in S_f}P_q(q^{-s})$ with nonzero removed
  local factors at one, its leading coefficient equals
  $\ell_E\prod_{q\in S_f}P_q(q^{-1})$. These factors must occur on both
  sides before applying a valuation. Split-multiplicative $p$-adic
  exceptional-zero factors require their own normalization.
- $L^{(r)}$ in §1 is an actual derivative and is divided by $r!$.
  Some source notation calls the Taylor coefficient $L^{(r)}$ itself.
- The proofs here make no unconditional claim that the complex leading
  coefficient is positive for every elliptic curve. Positivity in §6
  is an input, which can be certified for a specified curve by a
  rigorous archimedean calculation.
- A nonzero Bockstein vector is weaker than a nonzero scalar regulator,
  but its nonvanishing for a given elliptic curve still needs proof.
  The vector comparison is useful when available; it is not generated
  by the elementary cofactor lemma.

The independent analytic-rank work can provide rigorous intervals for
$\ell_E$. To apply (6.2), it must be supplemented with a certified interval
for the correctly normalized $\Omega_E R_\infty$ and the exact lattice
index. Even a narrow interval around one does not prove $n_E$ is rational
or integral. The remaining rationality and comparison statements above
are therefore explicit, substantive obligations.
