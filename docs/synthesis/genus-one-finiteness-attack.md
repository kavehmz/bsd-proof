# Genus-one torsors: attacking finiteness through divisor degrees

Date: 2026-09-12. This attack concerns the finiteness of
$\operatorname{Sha}(E/\mathbb Q)$ without using an $L$-function or a
comparison of regulators. The fixed test curve is
$$
E=389a1:\qquad y^2+y=x^3+x^2-2x.
$$
Its discriminant is $389$, so its minimal model defines an abelian scheme
$\mathcal E$ over $U=\operatorname{Spec}\mathbb Z[1/389]$.
The notation and epistemic standards are those of the
[charter](../00-charter.md). All `[NEW]` deductions below have proofs;
the tag makes no assertion of historical novelty. Coordinator review on
2026-09-12 passed Propositions 2.3, 3.1, 6.1 and Lemmas 5.1–5.2,
including the minimum-degree, exponent, specialization, and quotient
arguments. Other `[NEW]` statements remain pending independent review.

The attack proves the exact degree criterion, identifies two different
descent obstructions which must not be conflated, and tests three ways of
producing a bound. No uniform arithmetic degree bound is proved. The
geometric construction in §6 is over a complex function field and is not
a counterexample to BSD over a number field.

## 1. Primary inputs and their precise scope

**[THEOREM].** For a proper geometrically integral variety $X/k$ there is
an exact sequence
$$
0\longrightarrow\operatorname{Pic}(X)
\longrightarrow\operatorname{Pic}(X_{\bar k})^{G_k}
\xrightarrow{\mathrm{ob}_X}\operatorname{Br}(k)
\longrightarrow\operatorname{Br}_1(X).
\tag{1.1}
$$
For a number field $k$, the map
$\operatorname{Br}(k)\to\bigoplus_v\operatorname{Br}(k_v)$ is injective.
These are respectively the Hochschild–Serre Picard–Brauer sequence and
the injective part of Brauer–Hasse–Noether. Verified statements:
Poonen, *Rational Points on Varieties*, Corollary 6.7.8 and Theorem
1.5.36(i), in the
[author's text](https://math.mit.edu/~poonen/papers/Qpoints.pdf).
Riemann–Roch is Theorem 2.5.3 there.

**[THEOREM].** If $X/k$ is an everywhere locally soluble genus-one curve
over a number field, its period equals its index. A stronger general
abelian-variety splitting-degree statement is Clark, Theorem 3,
[arXiv:math/0406135](https://arxiv.org/abs/math/0406135).
The classical genus-one statement is attributed there to Cassels and
O'Neil. Section 2 gives its proof in the exact form needed here.

**[THEOREM].** Let $\mathcal A/U$ be an abelian scheme over an open
subscheme of the ring of integers of a number field $k$, with generic
fiber $A$. Milne, *Arithmetic Duality Theorems*, second edition (2006),
II, Lemma 5.5 and equation (5.5.1), gives
$$
0\longrightarrow H^1(U,\mathcal A)
\longrightarrow H^1(k,A)
\longrightarrow\bigoplus_{v\in U}H^1(k_v,A),
\tag{1.2}
$$
and identifies the further kernel of localization at the omitted places
with $\operatorname{Sha}(k,A)$. Proposition II.5.1 asserts torsion and
cofinite-type conclusions, not finiteness of the entire $H^1$ group;
its $m$-primary assertions assume $m$ invertible on $U$. See the
[author's complete book](https://www.jmilne.org/math/Books/ADTnot.pdf),
printed pp. 197–202. For smooth $\mathcal A$, étale and fppf torsors agree.

**[THEOREM].** Krämer–Maculan,
[arXiv:2310.08485v5](https://arxiv.org/abs/2310.08485v5), dated
11 March 2026, Proposition 3.5, proves finiteness of torsors over
$\mathcal O_{k,S}$ under abelian schemes of fixed dimension **equipped
with a polarization of fixed degree $d$**. Its proof uses Lemma 3.4
and finiteness for the finite group scheme $\ker\lambda$. Lemma 3.6
states that such torsor models are smooth projective and that an ample
generic-fiber line bundle extends relatively amply; it does not bound its
degree. These statements were checked in
[§3 of the current full text](https://arxiv.org/html/2310.08485v5#S3).

**[THEOREM].** For each fixed $m\ge1$, the $m$-Selmer group and hence
$\operatorname{Sha}(k,A)[m]$ are finite. The more general finite
$m$-torsion assertion for classes locally trivial outside a fixed finite
set is Harari–Szamuely, Lemma 2.2,
[arXiv:2110.13127](https://arxiv.org/abs/2110.13127),
[verified author PDF](https://www.imo.universite-paris-saclay.fr/~harari/articles/submathz.pdf).
It is a statement for each fixed $m$, not an exponent bound.

## 2. Two obstructions, and the exact minimal degree

Write $\xi=[X]\in H^1(k,E)$ for an $E$-torsor $X$ and let
$P=\operatorname{ord}(\xi)$, its period. The index $I(X)$ is the gcd of
degrees of its closed points. All torsors considered here are smooth,
projective, geometrically integral curves of genus one.
The period is finite: any closed point gives a finite splitting field,
and restriction followed by corestriction kills $\xi$ by that field's
degree.

**[NEW] Lemma 2.1 (the obstruction before the Brauer obstruction).**
For every integer $d$, the degree-$d$ Picard scheme
$\operatorname{Pic}^d_{X/k}$ is an $E$-torsor of class $d\xi$, using the
usual Abel–Jacobi identification. Consequently
$$
\operatorname{Pic}^d_{X/k}(k)\ne\varnothing
\quad\Longleftrightarrow\quad d\xi=0.
\tag{2.1}
$$
Equivalently, the connecting homomorphism associated to
$$
0\longrightarrow E(\bar k)
\longrightarrow\operatorname{Pic}(X_{\bar k})
\xrightarrow{\deg}\mathbb Z\longrightarrow0
\tag{2.2}
$$
sends $1$ to $\xi$.

*Proof.* Choose $x\in X(\bar k)$ and identify $X_{\bar k}$ with
$E_{\bar k}$ by origin $x$. Put $a_\sigma=\sigma x-x$; these form a
cocycle representing $\xi$. Identify a divisor class of degree $d$ with
the degree-zero class obtained by subtracting $dx$. In this coordinate,
Galois acts as $z\mapsto\sigma z+d a_\sigma$. That is the torsor cocycle
$d\xi$. This proves both descriptions. An $E$-torsor is trivial exactly
when it has a $k$-point. $\square$

Thus the fact that the geometric Néron–Severi group is
$\mathbb Z$ with trivial Galois action does **not** supply a rational
degree-one divisor class. The degree-one component first has to acquire
a rational point. Only after that does (1.1) ask whether the resulting
rational divisor class is an actual line bundle on $X$.

**[NEW] Lemma 2.2 (local solubility removes the second obstruction).**
Suppose $k$ is a number field and $X(k_v)\ne\varnothing$ for every place
$v$. Then $\mathrm{ob}_X$ in (1.1) is zero. In particular
$$
\operatorname{Pic}(X)
\simeq\operatorname{Pic}(X_{\bar k})^{G_k}.
\tag{2.3}
$$

*Proof.* Let $b=\mathrm{ob}_X(L)$ for a Galois-invariant geometric line
bundle class. By exactness, its image in $\operatorname{Br}(X)$ is zero.
For each $v$, a point $x_v\in X(k_v)$ provides a left inverse to
$\operatorname{Br}(k_v)\to\operatorname{Br}(X_{k_v})$ by evaluation.
The local image $b_v$ is therefore zero. Brauer–Hasse–Noether implies
$b=0$. Exactness of (1.1) proves (2.3). $\square$

**[NEW] Proposition 2.3 (minimum, not merely a gcd).** Under the
hypotheses of Lemma 2.2, the following positive integers are all equal:
$$
P=I(X)
=\min\{\deg D:D\text{ is a nonzero effective }k\text{-divisor on }X\}
=\min\{[L:k]:X(L)\ne\varnothing\}.
\tag{2.4}
$$
The smallest degree of an ample line bundle is also $P$. The smallest
degree of a very ample line bundle is the smallest multiple of $P$ which
is at least three.

*Proof.* By Lemma 2.1 there is a rational degree-$P$ divisor class, and
Lemma 2.2 makes it an actual line bundle $L$ over $k$. Its degree is
positive, while the canonical divisor has degree zero. Riemann–Roch and
the absence of sections in negative degree give
$h^0(X,L)=P$. A nonzero $k$-section gives an effective divisor $D$ of
degree $P$.

Every closed point $z$ gives a rational divisor class of degree
$[k(z):k]$, so Lemma 2.1 implies $P\mid[k(z):k]$. Therefore an effective
divisor of total degree $P$ must consist of a single closed point of
degree $P$, with multiplicity one. This proves (2.4). A line bundle on a
proper curve is ample exactly when its degree is positive.

For degree $d\ge3$, over $\bar k$ every length-two subscheme $Z$ satisfies
$H^1(X,L(-Z))=0$, by duality and $\deg L(-Z)>0$. Thus $L$ separates
points and tangent vectors and is very ample. Degrees one and two have
respectively one and two sections and cannot embed a genus-one curve.
Lemmas 2.1–2.2 give a degree-$d$ line bundle exactly for $P\mid d$.
$\square$

**[NEW] Consequence (testing the plane-cubic shortcut).** For an
everywhere locally soluble $X$, a plane cubic model exists exactly when
$3\xi=0$. A degree-one class would make $X(k)$ nonempty. Riemann–Roch
proves effectivity of a positive-degree line bundle already available;
it does not create its degree. For a period-two torsor the minimal
embedding degree is four, not three.

## 3. The uniform degree criterion really is full finiteness

**[NEW] Proposition 3.1.** For a fixed elliptic curve $E/k$ over a number
field, the following assertions are equivalent:

1. $\operatorname{Sha}(k,E)$ is finite.
2. It has bounded exponent.
3. There is an integer $B$ such that every everywhere locally soluble
   $E$-torsor has a nonzero effective $k$-divisor of degree at most $B$.
4. There is an integer $B$ such that every such torsor has a point over
   some extension $L/k$ of degree at most $B$.
5. There is one finite extension $L/k$ over which all such torsors have
   points.

*Proof.* A finite group has bounded exponent. If its exponent divides
$M$, it is contained in the finite group $\operatorname{Sha}(k,E)[M]$,
so bounded exponent implies finiteness. Proposition 2.3 identifies each
torsor's period with the two minima in assertions 3 and 4. A uniform
bound $B$ on these periods makes the exponent divide
$\operatorname{lcm}(1,2,\ldots,B)$; conversely an exponent $M$ makes the
periods at most $M$. If the group is finite, choose a splitting field for
each of its finitely many torsors and take their compositum, proving 5.
If 5 holds, restriction followed by corestriction on $H^1(k,E)$ is
multiplication by $[L:k]$, so that integer kills the group. $\square$

This equivalence means that the desired geometric degree bound is a
substantive finiteness theorem, not a weaker consequence of projectivity.
It also gives a route for checking a proposed bound: if it supplied
$B$, a single finite descent at $\operatorname{lcm}(1,\ldots,B)$ would
contain the entire group.

**[GAP Degree-389].** Produce an integer $B\ge1$ and prove: every smooth
projective geometrically integral genus-one curve $X/\mathbb Q$ with an
$E$-torsor structure, for
$E:y^2+y=x^3+x^2-2x$, and with
$X(\mathbb R)\ne\varnothing$ and $X(\mathbb Q_p)\ne\varnothing$ for
every prime $p$, has a closed point of degree at most $B$ over
$\mathbb Q$. An ineffective existence proof of a uniform $B$ already
proves finiteness; an explicit bound would give a finite descent target.

The next sections are actual attempts to supply this $B$, including the
precise parts each attempt establishes.

## 4. Attempt through integral models and polarized finiteness

**[NEW, deduction from (1.2)].** Every class in
$\operatorname{Sha}(E/\mathbb Q)$ extends uniquely to a class in
$H^1(U,\mathcal E)$, and is represented by a smooth projective
$\mathcal E$-torsor $\mathcal X/U$. Its localizations at $389$ and the
real place are zero. Conversely a class of $H^1(U,\mathcal E)$ with
these two zero localizations lies in $\operatorname{Sha}(E/\mathbb Q)$.

*Proof.* Exactness of (1.2) gives existence and uniqueness of the integral
cohomology class. The smooth projective representability is
Krämer–Maculan Lemma 3.6. At primes in $U$, torsors over the completed
local ring are trivial: their special fibers have points by Lang's
theorem over the finite residue field, and smoothness lifts those
points. Imposing the remaining two local conditions gives exactly the
definition of $\operatorname{Sha}$. $\square$

Thus good reduction outside $\{389\}$ is already present for **all**
classes being investigated. Passing to these models has not discarded an
infinite tail of possible periods.

**[NEW] Lemma 4.1 (why a degree bound would make the integral argument
work).** Fix $d\ge1$ and enlarge $U$ to
$U_d=\operatorname{Spec}\mathbb Z[1/(389d)]$. The set of generic-fiber
$E$-torsors which extend to $\mathcal E$-torsors over $U$ and admit a
degree-$d$ line bundle is finite.

*Proof.* Such a line bundle extends relatively amply by Lemma 3.6 of the
verified source. The degree-$d$ relative Picard torsor has a section, so
$d[\mathcal X]=0$ after passage to $U_d$, by the relative version of the
cocycle calculation in Lemma 2.1. In the étale Kummer sequence
$$
0\longrightarrow\mathcal E[d]\longrightarrow\mathcal E
\xrightarrow{[d]}\mathcal E\longrightarrow0
$$
over $U_d$, its class therefore lifts to $H^1(U_d,\mathcal E[d])$.
This is a finite set: $\mathcal E[d]$ is a fixed finite étale group
scheme, and Hermite–Minkowski gives finiteness of its torsors over a
fixed number ring. Restriction to the generic fiber proves the claim.
Equivalently one may apply Krämer–Maculan Proposition 3.5. $\square$

The finite étale kernel in this proof has order $d^2$, and $U_d$ depends
on the primes dividing $d$. Neither of those quantities has been bounded
as $X$ varies. Taking the union of these finite sets over all $d$ is not
a finiteness argument.

**[NEW] Lemma 4.2 (the canonical bundle supplies degree zero).** For any
$\mathcal E$-torsor $\pi:\mathcal X\to U$ there is a canonical
isomorphism
$$
\Omega^1_{\mathcal X/U}
\simeq\pi^*\bigl(e^*\Omega^1_{\mathcal E/U}\bigr).
\tag{4.1}
$$
Every tensor power of this line bundle, including its duals and twists
pulled back from $U$, has degree zero on each fiber.

*Proof.* Trivialize the torsor étale-locally on $U$. The standard
identification of relative differentials on an elliptic scheme with
the pullback of its invariant differentials is invariant under
translation. It therefore descends across the translation transition
maps. Pullbacks from the base restrict to trivial line bundles on
fibers, proving the degree statement. $\square$

This calculation tests the genus-at-least-two strategy concretely.
For genus one the canonical bundle cannot produce a fixed ample degree.
The Hodge line in (4.1) is the same for every torsor of the fixed
Jacobian. Also, the principal polarization on $E$ is not a degree-one
line bundle on $X$: its degree-one geometric Néron–Severi class still
faces the first obstruction $\delta(1)=\xi$ in Lemma 2.1.

The affine-group finiteness theorem cannot close the argument either.
Javanpeykar–Loughran, Lemma 2.1,
[arXiv:1501.04526](https://arxiv.org/abs/1501.04526), states finiteness
of $H^1$ for a **smooth affine** group scheme of finite type over the
number ring. An elliptic scheme is proper and not affine. Their
[accepted manuscript](https://pure.manchester.ac.uk/ws/portalfiles/portal/51573794/Flags.pdf)
also explicitly distinguishes torsors of abelian varieties in §1.2.
The finite presentation of $\mathcal E$ does not satisfy the omitted
affineness hypothesis.

## 5. A second arithmetic attack: a common splitting source

The previous attempt reached an unknown degree. This attempt tries to
bound that degree by constructing one global source for all torsors.

**[NEW] Lemma 5.1 (a fixed source gives an explicit exponent).** Let
$Y/k$ be a nonempty smooth projective geometrically integral curve over
a number field. Let $\mathcal T$ be any set of $E$-torsor classes such
that, for each $X\in\mathcal T$, there is a $k$-morphism $Y\to X$.
Then every element of $\mathcal T$ is killed by $I(Y)$, the gcd of the
degrees of closed points of $Y$.

*Proof.* For every closed point $y\in Y$, its image supplies a
$k(y)$-point on $X$. Restriction and corestriction imply
$[k(y):k][X]=0$. A finite integer linear combination of these degrees
equals their gcd, so $I(Y)[X]=0$. $\square$

A rational map from this smooth projective $Y$ to a proper curve $X$
extends everywhere, so the same conclusion holds for rational maps.
If $\mathcal T=\operatorname{Sha}(k,E)$, Lemma 5.1 and finite
$I(Y)$-torsion prove finiteness.

**[GAP Source-389].** Construct one smooth projective geometrically
integral curve $Y/\mathbb Q$ such that every everywhere locally soluble
$389a1$-torsor admits a $\mathbb Q$-morphism from $Y$. More weakly,
construct one finite extension $L/\mathbb Q$ over which all such
torsors have points. Either conclusion supplies a uniform exponent by
the proved restriction–corestriction argument.

The tempting choice $Y=E$ fails to give a construction: a morphism
$E\to X$ sends $0\in E(\mathbb Q)$ to a rational point of $X$.
Consequently such a map exists only for a trivial torsor. Identifying
the Jacobian of $X$ with $E$ does not construct an inverse Albanese map
from $E$ to $X$.

There is, however, a completely explicit **period-dependent** global
source. If $[X]$ has order $m$, a trivialization of its $m$-fold torsor
sum gives a morphism
$$
f_m:X\longrightarrow E,\qquad f_m(x+P)=f_m(x)+mP.
\tag{5.1}
$$
**[NEW]** Its degree is $m^2$, since over $\bar k$ it is a translate of
$[m]$. Pulling back $\mathcal O_E(0)$ supplies a degree-$m^2$ effective
divisor. Under local solubility, Proposition 2.3 improves this to degree
$m$. This constructs a divisor for each torsor but leaves the common
bound dependent on its unknown period. It records exactly where the
straightforward norm/pullback construction stops.

A recently proved function-field finiteness theorem might seem to
provide the fixed source. Harari–Szamuely Theorem 1.1 proves finiteness
for a constant commutative group over $k(Y)$ when $k$ is a number field,
with local conditions at the **closed points of $Y$**. The following
calculation checks that it does not import arithmetic local solubility.

**[NEW] Lemma 5.2 (the two local conditions differ).** Let $Y/k$ be as
above, $F=k(Y)$, and let $F_y$ be its completion at a closed point $y$.
If a constant class $\xi\in H^1(k,E)$ becomes trivial in
$H^1(F_y,E)$, then its restriction to $H^1(k(y),E)$ is zero.
It is consequently killed by $[k(y):k]$. If $y\in Y(k)$, then
$H^1(k,E)\to H^1(F_y,E)$ is injective.

*Proof.* The constant torsor $X\times_k\operatorname{Spec}
\widehat{\mathcal O}_{Y,y}$ is proper. An $F_y$-point extends by the
valuative criterion to a point over the completed local ring and
specializes to a $k(y)$-point. The first assertion follows; apply
restriction–corestriction for the second. For a rational $y$, the
specialized point is already a $k$-point. $\square$

Thus the constant classes to which the function-field local conditions
apply are already killed by the degree of any single closed point of
$Y$. When $Y$ has a rational point, a nonzero number-field Sha class
does not satisfy these new local conditions at all. The theorem's
finiteness does not produce $Y$ or a common splitting field for the
unknown number-field classes.

## 6. An actual geometric stress test for the proposed bound

**[NEW] Proposition 6.1.** Fix nonisogenous complex elliptic curves
$A$ and $B$, and put $F=\mathbb C(B)$. For every $n\ge2$ there exists
an $A_F$-torsor $X_n/F$ of period exactly $n$ which extends to a smooth
projective torsor under $A\times B$ over the **fixed proper base $B$**.
It has points over the completion at every closed point of $B$.
In particular every positive-degree divisor on $X_n$ has degree at
least $n$, despite its fixed Jacobian and everywhere good reduction.

*Proof.* Choose a homomorphism
$f:B[n]\to A[n]$ of exact additive order $n$. Such maps exist since
both groups are isomorphic to $(\mathbb Z/n\mathbb Z)^2$. Over the
finite étale cover $[n]:B\to B$, start with the trivial torsor
$A\times B$. For $T\in B[n]$ impose the descent action
$$
T:(a,b)\longmapsto(a+f(T),b+T).
\tag{6.1}
$$
It is free. Its quotient
$\mathcal X_n=(A\times B)/\{(f(T),T):T\in B[n]\}$ is a projective
abelian surface, and the map induced by $(a,b)\mapsto[n]b$ to $B$
makes it a torsor under the constant elliptic scheme $A\times B$.
Equivalently these properties follow by finite étale descent from the
trivial torsor. In particular it is smooth with genus-one fibers.

The $d$-fold torsor class is obtained by replacing $f$ with $df$. If it
were trivial over $B$, a section pulled to the covering $B$ would be a
morphism $h:B\to A$ with
$$
h(b+T)=h(b)+df(T).
$$
Any morphism between complex elliptic curves is a translate of a
homomorphism. To check this directly, lift the map to their universal
covers $\mathbb C$. Its derivative descends to a holomorphic function
on the compact source torus and is constant. The lift is therefore
$z\mapsto az+c$, with $a$ carrying the source lattice into the target
lattice. If $a\ne0$ it induces an isogeny. Thus nonisogeny implies that
$h$ is constant. The equation is therefore
possible exactly when $df=0$, or $n\mid d$. The integral torsor thus
has order $n$. The restriction $H^1(B,A)\to H^1(F,A_F)$ is injective:
a generic section of a proper torsor extends over every local ring of
the smooth base curve. Hence its generic class also has order $n$.

Each special fiber over a closed point of $B$ is a nonempty smooth
curve over $\mathbb C$ and has a $\mathbb C$-point. Smoothness and
Hensel's lemma lift this to the completed local ring and its fraction
field. Finally the cocycle argument of Lemma 2.1, which works over any
characteristic-zero field, shows that $n$ divides the degree of every
divisor on the generic fiber. $\square$

This construction tests only a geometric inference. The base is a
complex curve, not a number ring, and $F$ is not a number field. It
shows that smooth integral models, a fixed Hodge line, a fixed Jacobian,
and completed-local points do not by themselves force a degree bound
in a theorem insensitive to the arithmetic nature of the base.

The key arithmetic difference can also be seen in Kummer cohomology:
over the complex base the group of constant points $A(\mathbb C)$ is
divisible, while morphisms $B\to A$ add no nonconstant maps. Over a
number field the analogous point groups are finitely generated. The
finite-generation theorem supplies finite quotients for each integer,
but no argument here upgrades it to a bound on the integers $n$ needed
to trivialize all torsors.

## 7. The precise remaining arithmetic statement

The geometric attempt has removed the Brauer obstruction **after** a
rational Picard class exists, and has constructed the least-degree
divisor for each known period. It has also proved that ample generic
line bundles extend on the fixed integral model and that each fixed
degree gives only finitely many classes. These are substantive
ingredients of a prospective proof.

The unsolved step is uniformly controlling the first obstruction
$$
\delta_X(1)=[X]\in H^1(\mathbb Q,E)
$$
in the degree sequence (2.2), for all locally soluble torsors of the
fixed curve. Neither (1.1), relative Riemann–Roch, fixed-degree
polarized finiteness, nor the constant-group function-field theorem
supplies that control. Gaps Degree-389 and Source-389 state two
concrete forms in which such control would complete finiteness.

For comparison with the previous arithmetic calculation,
[the explicit Kurihara witness](continuation-2026-09-12.md)
establishes $\operatorname{Sha}(389a1)[5^\infty]=0$. Proposition 2.3
therefore implies that every locally soluble torsor in this test case
has minimal divisor degree prime to $5$. That excludes one prime
factor of the unknown degrees; it is not an upper bound on them.

No result in this file establishes full Sha finiteness, the BSD leading
term, or a BSD counterexample. Its proofs isolate the required uniform
arithmetic bound without assuming it as a hidden polarization or
cohomological-finiteness hypothesis.
