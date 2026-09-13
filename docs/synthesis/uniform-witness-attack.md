# Uniform Kurihara witnesses: the exact index and the remaining obstruction

Date: 2026-09-12. This is an attack on the uniform-prime target in
[the continuation note](continuation-2026-09-12.md), not a proof of full BSD.
The deductions marked `[NEW]` passed the [independent review](review-uniform-witness.md); no historical novelty is claimed.

The concrete progress is twofold. First, for $389a1$ there are **no residual-image
exceptions among good primes $p\geq5$**; a short proof is given below. Thus the
Castella–Sano theorem supplies a unit Kurihara witness, of unspecified index,
at every such prime. Second, its smallest possible index is exactly
$\dim_{\mathbb F_p}\operatorname{Sel}_p$, and hence, for this rank-two curve,
exactly $2+\dim_{\mathbb F_p}\operatorname{Sha}[p]$. A Chebotarev argument constructs all the
local tests one could want, but shows precisely where the extra $\operatorname{Sha}[p]$
classes survive the tests on two known points.

## 1. Conventions and verified inputs

Fix an elliptic curve $E/\mathbb Q$ of conductor $N$ and a prime $p\geq5$.
Put
$$
\mathcal P_p=\{\ell\nmid Np:\ell\equiv1\pmod p,
                 a_\ell\equiv\ell+1\pmod p\},
\qquad
I_\ell=(\ell-1,a_\ell-\ell-1)\mathbb Z_p.
$$
Let $\mathcal N_p$ be its squarefree products, including $1$, and let
$I_n=\sum_{\ell\mid n}I_\ell$, with $I_1=0$. Write
$\delta_n\in\mathbb Z_p/I_n$ for the Kurihara number in the cited papers,
$\bar\delta_n$ for its image in $\mathbb F_p$, and $\nu(n)$ for the number of
prime factors. A choice of primitive roots is understood; changing it
multiplies $\delta_n$ by a unit. The harmless sign and real-period conventions
in the two sources also preserve every valuation used here for odd $p$.

Set
$$
s=\min\{\nu(n):\delta_n\ne0\},\qquad
u_p=\min\{\nu(n):\bar\delta_n\ne0\},
$$
and set either minimum to infinity when its defining set is empty. Put
$M_i=\min_{\nu(n)=i}v_p(\delta_n)$ and $M_\infty=\min_i M_i$, using
$v_p(0)=\infty$, including for zero in a finite quotient. Thus $s$ is a
nonzero-index invariant and $u_p$ is a unit-index invariant.

**[THEOREM: Kim, 2025 final version]** Assume that $\bar\rho_{E,p}$ is
surjective, the Manin constant is prime to $p$, and $s<\infty$. For
$X_p=\operatorname{Sel}_{p^\infty}(E/\mathbb Q)^\vee$,
$$
\operatorname{rank}_{\mathbb Z_p}X_p=s,\qquad
\operatorname{Fitt}_{i,\mathbb Z_p}(X_p)
   =p^{M_i-M_\infty}\mathbb Z_p
\quad(i\geq s,\ i\equiv s\pmod2).
\tag{1}
$$
Its finite invariant factors occur in equal pairs, and $\delta_n=0$ in the
opposite parity. These inputs are
[Kim, arXiv:2203.12159v6, Theorem 1.8 and Proposition 3.14](https://arxiv.org/html/2203.12159v6).
No ordinarity or condition $E(\mathbb Q_p)[p]=0$ is required for (1).
The extra local-torsion condition in that paper's Theorem 1.10 must not be
silently added to, or removed from, that separate theorem.

**[THEOREM: Castella–Sano, 2026 preprint]** For a non-CM elliptic curve,
$p>3$, surjective $\bar\rho_{E,p}$ and a modular parametrization whose Manin
constant is prime to $p$, one has
$$M_\infty=v_p\left(\prod_{\ell\mid N}c_\ell\right)$$
if $p$ is good ordinary, or if $p$ is good supersingular and $N$ is squarefree.
This is [Castella–Sano, arXiv:2601.14504v1, Theorem B](https://arxiv.org/html/2601.14504v1).
Consequently, in these cases with $p\nmid\prod c_\ell$, $u_p$ is finite.
The theorem controls this minimum's existence, not its value.

## 2. An explicit residual-image argument for 389a1

**[NEW: deduction from standard semistable and Tate-curve facts]** For
$$E:\quad y^2+y=x^3+x^2-2x,$$
$\bar\rho_{E,p}$ is surjective for every $p\geq5$, $p\ne389$.

*Proof.* The usual integral Weierstrass invariants are
$$
b_2=4,\quad b_4=-4,\quad b_6=1,\quad b_8=-3,
\qquad c_4=112,\qquad\Delta=389.
$$
The model is minimal: its discriminant valuation is below $12$ at every
prime. It has good reduction away from $389$ and multiplicative type $I_1$
at $389$, since $389\nmid c_4$. In particular it is semistable and its
only Tamagawa number is $c_{389}=1$.

We use the following **[THEOREM: Serre]**: if a semistable elliptic curve over
$\mathbb Q$ has reducible mod-$p$ representation, its semisimplification is
$\mathbb F_p\oplus\mathbb F_p(1)$. The reference is Serre,
*Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*,
Invent. Math. **15** (1972), 259–331, p. 307. The exact statement, without an
optimality requirement, is also explicitly recorded in
[Agashe–Winters, arXiv:2510.04323v1, §2](https://arxiv.org/html/2510.04323v1#S2).
It follows that reducibility would force
$p\mid\#E(\mathbb F_\ell)$ at every good $\ell\ne p$.

Direct counting gives
$$\#E(\mathbb F_2)=5,\qquad\#E(\mathbb F_3)=6.$$
Indeed the numbers of affine solutions above the two $x$-values modulo $2$
are $2,2$; above the three $x$-values modulo $3$ they are $2,2,1$. Add the
point at infinity in each case. Since $p\geq5$, both primes are usable, and
$p$ cannot divide both $5$ and $6$. Thus the representation is irreducible.

The **[THEOREM: Tate uniformization]** at the multiplicative prime $389$
gives a nontrivial unipotent element of its mod-$p$ inertia image whenever
$p\ne389$. Here is the relevant local calculation. After at most an
unramified quadratic extension the curve is a Tate curve with parameter
$q_T$ of valuation one. Its $p$-division points are generated by $\mu_p$
and $q_T^{1/p}$. Inertia fixes $\mu_p$ because $p\ne389$, whereas adjoining
$q_T^{1/p}$ has ramification degree $p$: the valuation of $q_T$ is one.
The resulting inertia action on these generators therefore contains
$\left(\begin{smallmatrix}1&a\\0&1\end{smallmatrix}\right)$ with $a\ne0$.
An unramified quadratic twist does not change this inertia assertion.

For completeness, an elementary group argument now suffices. If an
irreducible subgroup $G\subset\mathrm{GL}_2(\mathbb F_p)$ contains a
nontrivial transvection $t$ with fixed line $L$, some $g\in G$ has $gL\ne L$.
In a basis along $L$ and $gL$, the elements $t$ and $gtg^{-1}$ are respectively
nontrivial upper and lower unipotent matrices. Their powers give all upper
and all lower unipotents, because the field is the prime field. These two
root groups generate $\mathrm{SL}_2(\mathbb F_p)$ by elementary row
operations. Finally the determinant of $\bar\rho_{E,p}$ is the surjective
cyclotomic character, so $G=\mathrm{GL}_2(\mathbb F_p)$. $\square$

**[NEW: application]** The hypothesis-exception set for the two source
theorems, on this curve's good primes, can therefore be taken to be the
explicit set
$$S_0=\{2,3,389\}.$$
The semistable Manin-constant criterion used in the continuation note
(also Kim §1.4.1) supplies the period-integrality hypothesis. The curve is
non-CM, as already verified in the exact computation; alternatively
$v_{389}(j_E)=-1$ excludes a CM $j$-invariant. Since $N=389$ is squarefree
and $c_{389}=1$, Castella–Sano covers both reduction types at every
$p\notin S_0$ and gives
$$M_\infty=0,\qquad u_p<\infty.\tag{2}$$
This proves that no further residual-image exceptions need be inserted
in a proposed uniform theorem. It does not prove that no additional primes
have nonzero $\operatorname{Sha}[p]$.

## 3. The first unit index is exactly the mod-p Selmer dimension

**[NEW: elementary Fitting lemma]** If $R=\mathbb Z_p$ and $X$ is a finitely
generated $R$-module, then
$$
\min\{i:\operatorname{Fitt}_{i,R}(X)=R\}
   =\dim_{\mathbb F_p}(X/pX).
\tag{3}
$$

*Proof.* Write
$X\simeq R^s\oplus\bigoplus_{j=1}^t R/p^{a_j}R$ with every $a_j>0$.
A square presentation matrix is
$\operatorname{diag}(0,\ldots,0,p^{a_1},\ldots,p^{a_t})$ of size $s+t$.
Every minor of positive size is either zero or divisible by $p$, and the
ideal of minors of size zero is $R$. Thus the first unit Fitting ideal
is at $i=s+t$, which is also $\dim X/pX$. $\square$

**[NEW: exact unit-index formula]** Under the hypotheses of (1), suppose
additionally that $M_\infty=0$. Then
$$
\boxed{\ u_p=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
       =\operatorname{rank}E(\mathbb Q)+\dim_{\mathbb F_p}\operatorname{Sha}(E/\mathbb Q)[p].\ }
\tag{4}
$$
In particular the formula includes possible divisible parts of $\operatorname{Sha}$;
finiteness of $\operatorname{Sha}[p^\infty]$ is not an assumption.

*Proof.* Put $d=\dim_{\mathbb F_p}X_p/pX_p$. The paired invariant factors
in (1) imply $d\equiv s\pmod2$. For every index $i<s$, all $\delta_n$ with
$\nu(n)=i$ vanish by the definition of $s$. The opposite-parity indices
also vanish. For the remaining indices (1) and $M_\infty=0$ show that a
unit value at index $i$ exists exactly when
$\operatorname{Fitt}_i(X_p)=\mathbb Z_p$. Equation (3) gives the first such
index $d$, and this index has the required parity. The valuation minimum
$M_d=0$ is attained because the valuations lie in
$\mathbb Z_{\geq0}\cup\{\infty\}$. Hence $u_p=d$.

Pontryagin duality gives
$d=\dim_{\mathbb F_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)[p]$.
Surjectivity implies $E(\mathbb Q)[p^\infty]=0$. To verify the passage to
the finite-level Selmer group, put
$D=E(\mathbb Q)\otimes\mathbb Q_p/\mathbb Z_p$. The infinite Kummer
sequence, followed by multiplication by $p$, gives
$$
0\longrightarrow D[p]\longrightarrow\operatorname{Sel}_{p^\infty}[p]
  \longrightarrow\operatorname{Sha}[p]\longrightarrow0,
$$
because $D/pD=0$. The finite Kummer sequence is
$$
0\longrightarrow E(\mathbb Q)/pE(\mathbb Q)
 \longrightarrow\operatorname{Sel}_p
 \longrightarrow\operatorname{Sha}[p]\longrightarrow0.
$$
The natural map between these sequences is an isomorphism on the left
($P\mapsto P\otimes1/p$ and no rational $p$-torsion) and on the right.
It is therefore an isomorphism in the middle. Taking dimensions proves
both equalities in (4). $\square$

**[NEW: the nonprimitive variant]** If instead $M_\infty=a>0$, there is
no unit witness. Nevertheless the first index in the allowed parity at
which $M_i=a$ is still $\dim_{\mathbb F_p}\operatorname{Sel}_p$. This is
the same proof applied to (1). A stabilization index should not be called
a first nonzero index.

**[NEW: equivalence for the concrete curve]** The rank-two certification
and (2) imply, for every $p\notin S_0$,
$$
\begin{split}
\exists\ell\ne q\in\mathcal P_p:\bar\delta_{\ell q}\ne0
&\iff u_p=2\iff\dim_{\mathbb F_p}\operatorname{Sel}_p=2\\
&\iff\operatorname{Sha}[p]=0\iff\operatorname{Sha}[p^\infty]=0.
\end{split}\tag{5}
$$
The last equivalence is elementary: a nonzero $p$-primary torsion group
contains an element of order $p$, obtained by multiplying any nonzero
element by a suitable power of $p$. This also covers a divisible group.
Thus the target U$\delta$ is an exact reformulation of almost-all-prime
vanishing of $\operatorname{Sha}[p^\infty]$ in this setting, not merely a sufficient
criterion. The coefficient-comparison problem for the BSD leading term
remains a separate problem.

## 4. What Chebotarev can force, with a proof

For this section call a good prime $\ell\ne p$ *unipotent* when
$\bar\rho_{E,p}(\operatorname{Frob}_\ell)$ is a nonidentity unipotent.
Such a prime lies in $\mathcal P_p$, and
$$
H^1_f(\mathbb Q_\ell,E[p])
 \simeq E(\mathbb F_\ell)/pE(\mathbb F_\ell)
 \simeq E[p]/(\operatorname{Frob}_\ell-1)E[p]
$$
has dimension one. The first equality follows from good reduction and
$p$-divisibility of the formal group at $\ell\ne p$; the last is the
unramified cohomology description. It is essential to use nonidentity
unipotents here: the congruences defining $\mathcal P_p$ also allow the
identity Frobenius, whose local space has dimension two.

**[NEW: local functional realization]** Suppose $p\geq5$ and
$\bar\rho_{E,p}$ is surjective. Let $H$ be any finite-dimensional subspace
of $H^1(\mathbb Q,E[p])$. For every nonzero linear functional
$\lambda:H\to\mathbb F_p$, infinitely many unipotent primes have a
localization map on $H$ equal to $\lambda$ after a choice of basis of
their one-dimensional unramified cohomology group. One may exclude any
fixed finite set of primes.

*Proof.* Set $V=E[p]$, $K=\mathbb Q(E[p])$, and
$G=\operatorname{Gal}(K/\mathbb Q)=\mathrm{GL}_2(\mathbb F_p)$.
First $H^1(G,V)=0$. Indeed choose a central scalar $z=aI$ with $a\ne1$.
For any cocycle $c$ on $G$, comparing $c(zg)$ with $c(gz)$ gives
$$(a-1)c(g)=(g-1)c(z),$$
so $c$ is the coboundary of $(a-1)^{-1}c(z)$.
Inflation–restriction therefore injects $H^1(\mathbb Q,V)$ into
$\operatorname{Hom}(G_K,V)$, since $G_K$ acts trivially on $V$.

Choose a basis $c_1,\ldots,c_d$ of $H$, represented by cocycles, and let
$$W=\operatorname{im}\bigl(G_K\longrightarrow V^d,
                       \ h\mapsto(c_1(h),\ldots,c_d(h))\bigr).$$
This is a $G$-stable $\mathbb F_p$-subspace. It is all of $V^d$.
Otherwise, since $V^d$ is a direct sum of copies of the simple module $V$,
its proper submodule $W$ is killed by some nonzero $G$-linear map
$V^d\to V$. The endomorphism ring $\operatorname{End}_G(V)$ is
$\mathbb F_p$ (commute with all elementary matrices), so this map is
$(v_i)\mapsto\sum_i b_i v_i$ for nonzero coefficients $(b_i)$. Then
$\sum_i b_i c_i$ restricts to zero on $G_K$, contradicting the restriction
injection and independence of the $c_i$.

The cocycles and the residual representation together define a continuous
homomorphism into the finite semidirect product $V^d\rtimes G$. Its image
contains $V^d$ and surjects onto $G$, hence is the whole semidirect product.
Choose a nonidentity unipotent $\tau\in G$, a vector $e$ mapping to a basis
of $V/(\tau-1)V$, and the element with $G$-coordinate $\tau$ and cocycle
coordinates $\lambda(c_i)e$. Chebotarev applied to its conjugacy class
in the associated finite Galois extension gives infinitely many primes
with this Frobenius data. Localization of an unramified cocycle is its
Frobenius value modulo $(\tau-1)V$. Conjugation only changes the common
trivialization of this quotient, so the resulting functional has the
claimed form. Excluding all ramified primes and any other finite set
does not change the conclusion. $\square$

The proof uses the classical **[THEOREM: Chebotarev]** only to realize
a specified conjugacy class in a finite Galois group. Its cohomological
mechanism is the same one underlying the prime-selection statements in
[Kim §2.4, Proposition 2.2](https://arxiv.org/html/2203.12159v6#S2.SS4).
No quantitative density estimate, height comparison, or local condition
at $p$ has been assumed.

**[NEW: optimal number of local tests]** If $H=\operatorname{Sel}_p$ has
dimension $d$, the smallest number of unipotent primes for which the
combined localization map on $H$ is injective is $d$.

*Proof.* A sum of $m$ one-dimensional targets cannot inject a space of
dimension greater than $m$. Conversely, realize a basis of $H^*$ by the
preceding lemma, choosing distinct primes. Their localizations give an
isomorphism $H\to\mathbb F_p^d$. $\square$

Under (2), this smallest number of local tests and the first unit index
are consequently the same integer. This identifies their common
obstruction; it does not identify the unit support with an arbitrary
chosen collection of local tests.

## 5. The determinant of two points and the exact surviving kernel

Assume $\operatorname{rank}E(\mathbb Q)=2$, rational $p$-torsion is zero,
and choose a basis $P_1,P_2$ of the free Mordell–Weil group. More generally,
two independent points suffice at primes not dividing their index
$h=[E(\mathbb Q)/E(\mathbb Q)_{\rm tors}:\mathbb ZP_1+\mathbb ZP_2]$.
Let $K_p\subset H=\operatorname{Sel}_p$ be the two-dimensional Kummer space.

**[NEW: two-point determinant and kernel]** There are distinct unipotent
primes $\ell,q$ for which
$$
\det\begin{pmatrix}
\operatorname{loc}_\ell(P_1)&\operatorname{loc}_\ell(P_2)\\
\operatorname{loc}_q(P_1)&\operatorname{loc}_q(P_2)
\end{pmatrix}\ne0.
\tag{6}
$$
For every such pair, writing
$L_{\ell,q}=\operatorname{loc}_\ell\oplus\operatorname{loc}_q$ on $H$, the
quotient map $H\to\operatorname{Sha}[p]$ restricts to an isomorphism
$$
\boxed{\ \ker L_{\ell,q}\ \simeq\ \operatorname{Sha}[p].\ }
\tag{7}
$$

*Proof.* Extend the dual basis of $K_p^*$ to two functionals on $H$ and
realize them by the preceding lemma. This proves (6). For any pair
satisfying (6), $L_{\ell,q}|_{K_p}$ is an isomorphism onto its target.
Every $c\in H$ consequently has a unique $k\in K_p$ with
$L_{\ell,q}(c-k)=0$. The map from the kernel to $H/K_p$ is therefore
bijective, and the finite Kummer sequence identifies $H/K_p$ with
$\operatorname{Sha}[p]$. $\square$

Equation (7) gives the precise missing injectivity criterion. It also
explains why tests confined to rational points cannot certify it: every
extra Selmer class can be adjusted by a unique rational-point Kummer
class to vanish at both selected primes. Making the determinant in (6)
a unit does not remove any of these adjusted classes.

The following is an exact arithmetic version of the unresolved target.

**[GAP Uloc]** For $E=389a1$, construct an explicit nonzero integer $C$ such
that for every prime $p\nmid6\cdot389\cdot C$ there exist distinct
unipotent primes $\ell,q$ for which
$$
\ker\!\left(\operatorname{Sel}_p(E/\mathbb Q)
   \longrightarrow E(\mathbb F_\ell)/p\oplus E(\mathbb F_q)/p\right)=0.
\tag{8}
$$
Equations (4) and (7) prove that Uloc is equivalent to U$\delta$, after
allowing the same finite exceptional set. Chebotarev proves that an
arbitrary *finite* Selmer space can be separated by enough primes, and
proves (6) with two primes. The unproved part is that two tests suffice
on the whole space, uniformly in $p$.

## 6. Attempting deletion from an arbitrary unit witness

One might try the following implication: an arbitrary unit witness and
two independent points imply that pairs of auxiliary primes can be
removed or replaced until a two-prime unit witness is reached. The
strongest source-independent version would already imply
$$M_\infty=0,\quad\operatorname{rank}E(\mathbb Q)=2
                    \ \Longrightarrow\ u_p=2.$$

**[NEW: countermodel to that implication]** Fix any $p$ and consider
$$X=\mathbb Z_p^2\oplus(\mathbb Z/p\mathbb Z)^2.$$
Set $M_0=\infty$, $M_2=2$, $M_{2j}=0$ for $j\geq2$, and every odd
$M_i=\infty$. These are exactly the same-parity Fitting valuations of
$X$, with $s=2$ and $M_\infty=0$. The dual contains a rational-point
divisible summand $(\mathbb Q_p/\mathbb Z_p)^2$; its complementary finite
group has order $p^2$. All of primitivity, two known rank directions,
paired finite invariants, parity, and the structure identities hold,
but $u_p=4$. Thus those inputs cannot force a unit index of two.
At the level of witness minima, the values can be realized formally by
a nonzero $p^2$-divisible value at index two in a quotient of length
greater than two, and unit values at every even index at least four.

The separate formal possibility
$X=\mathbb Z_p^4$ with a designated rank-two rational-point summand has
$M_2=\infty$ and $M_4=0$: it encodes an additional divisible $\operatorname{Sha}$
corank of two. It too obeys these constraints. These are countermodels
to proposed deductions from the listed inputs, not elliptic-curve
counterexamples and not disproofs of BSD.

For local detector sets, ordinary row reduction can remove redundant
tests until there are $d=\dim\operatorname{Sel}_p$ tests, but cannot pass
below $d$. At $d>2$, (7) identifies the remaining obstruction. The Euler
system's finite–singular relations compare Selmer groups with altered
local conditions; deleting primes changes those groups. They do not
identify the original Selmer space with the span of the rational points.
Any proof of further descent must supply an arithmetic argument that the
kernel (7) is zero. No claim is made that a minimal unit witness must be
a divisor of an initially chosen unit witness.

## 7. A finite integral matrix would close the uniform gap

The finite-dimensional modular-symbol space is an appealing way to try
to force uniformity. Two elementary tests distinguish a valid integral
argument from an invalid one.

**[NEW: finite generation alone is insufficient]** Let a fixed integral
lattice be $M=\mathbb Z$ with the primitive functional $\phi=\mathrm{id}$.
For each prime $p$, let the hypothetical index-two admissible elements
generate $p^2M$, and let index-four elements generate $M$. Each lattice
is finitely generated, all rational spans are the same, and the union
over all primes of the index-two elements generates $M$ because
$\gcd(5^2,7^2)=1$. Yet each prime's own index-two values vanish modulo
that prime, while index-four values are units. Thus neither finite
generation nor a gcd taken across different primes proves U$\delta$.
The arithmetic admissibility restriction must remain attached to $p$.

Even a common finite presentation over all $p$-adic coefficient rings
does not suffice. Put
$$A=\prod_{p\geq5}\mathbb Z_p,\qquad a=(p)_p\in A,
\qquad X=A^2\oplus(A/aA)^2.$$
This is a finitely presented $A$-module, presented by
$\operatorname{diag}(0,0,a,a)$. Every specialization has $\mathbb Q_p$-rank
two but has mod-$p$ dimension four. The element $a$ is not a nonzero
rational integer diagonally embedded in $A$; every one of its components
is a nonunit. A common presentation over this product ring supplies no
finite set of exceptional rational primes.

Here is a sufficient determinant condition which really would work.

**[NEW: common integral presentation criterion]** Suppose a fixed
integer matrix
$$B:\mathbb Z^b\longrightarrow\mathbb Z^a$$
has rank $a-2$ over $\mathbb Q$. Suppose, for every $p$ outside an explicit
finite set, there is a surjection
$$\operatorname{coker}(B\otimes\mathbb F_p)
                    \twoheadrightarrow\operatorname{Sel}_p(E/\mathbb Q).
\tag{9}$$
If $E$ has rank two and its rational torsion has no $p$-part, then
$\operatorname{Sel}_p$ has dimension two for every such $p$ not dividing
any chosen nonzero $(a-2)$-minor $D$ of $B$. If $a=2$, take $D=1$.

*Proof.* At $p\nmid D$, the matrix has rank at least $a-2$, so the source
of (9) has dimension at most two. The Kummer space has dimension two
and lies inside the target. Thus both bounds are equalities. Equation
(4), wherever its hypotheses hold, supplies a two-prime unit witness.
The explicit exceptional set grows only by the prime divisors of $D$.
$\square$

**[GAP Uint]** For $389a1$, construct such a fixed matrix $B$, with a
verified nonzero minor $D$, and prove the maps (9) for all
$p\nmid6\cdot389$ outside a stated finite set. A finite integral model
of the full Selmer conditions, rather than just the rational-point
subspace, is required. No such model is constructed here. The local
condition at $p$ and the mod-$p$ Galois module both vary with $p$;
finite generation of the modular-symbol module does not establish (9).

The sharpened target is therefore an actual missing injection (8), or
a sufficient fixed integral presentation (9). All good $p\geq5$ already
have primitive Kurihara families. The work still needed is to bound
their first unit index by two, which the proved formula (4) measures
exactly as the absence of the remaining $\operatorname{Sha}[p]$ classes.
