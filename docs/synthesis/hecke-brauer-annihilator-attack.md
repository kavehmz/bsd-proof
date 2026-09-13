# The arithmetic Brauer component and the attempted Hecke annihilator

Date: 2026-09-12. This continues the coordinator-reviewed
[modular visibility argument](modular-visibility-attack.md).
Its prior exact sequences, splitting theorem, and source audit passed review;
see [the review](review-modular-visibility.md). The new deductions here have
full proofs and passed [independent coordinator review](review-hecke-brauer.md).

The task is to construct an annihilator, not to assume finite Sha or finite
Brauer groups. The attempts below do not construct the required annihilator.
They do identify the exact arithmetic cohomology omitted by a geometric
argument, transfer it without a finiteness assumption to a fixed regular
arithmetic surface, and give a specific Hecke calculation on $X_0(389)$:
$$t_0=T_2-T_3+1$$
kills the constant and geometric degree pieces but acts as the identity on
the $389a1$ Brauer/Sha component. An attempted use of Frobenius to overcome
this is checked at the cocycle level in §6. A real-place argument in §8
also shows that the complete Brauer group of a regular arithmetic model of
$389a1$ equals its Sha group, with no omitted $2$-primary correction.

## 1. Retaining the rational cusp and the constant Brauer group

Let $X/\mathbb Q$ be a smooth proper geometrically connected curve,
$c\in X(\mathbb Q)$ a rational point, and $J=\operatorname{Pic}^0_{X/\mathbb Q}$.
For the modular application $X=X_0(N)$ and $c=\infty$. All Brauer groups
are cohomological Brauer groups; for the regular curves and surfaces used
below they agree with the Azumaya Brauer groups.

For $F=\mathbb Q$ or a completion of a number field, let $s:X_F\to\operatorname{Spec}F$
be the structure map and define
$$
\operatorname{Br}_c(X_F)=\ker(c^*:\operatorname{Br}(X_F)\to\operatorname{Br}(F)),
\qquad N_c=1-s^*c^*.
\tag{1.1}
$$

**[NEW: deduction from Hochschild–Serre]** There is a canonical split
sequence and a resulting identification
$$
\begin{split}
0\to\operatorname{Br}(F)\overset{s^*}{\longrightarrow}\operatorname{Br}(X_F)
 &\longrightarrow H^1(F,J)\to0,\\
\operatorname{Br}_c(X_F)&\simeq H^1(F,J).
\end{split}\tag{1.2}
$$
These identifications commute with localization.

*Proof.* The section gives $c^*s^*=1$, so constants inject. The class of
$c$ splits the geometric Picard sequence as
$$\operatorname{Pic}(X_{\overline F})=J(\overline F)\oplus\mathbb Z[c].$$
Consequently $H^1(F,\operatorname{Pic}(X_{\overline F}))=H^1(F,J)$,
since a continuous map from a profinite group to $\mathbb Z$ is zero.
Tsen's theorem gives $\operatorname{Br}(X_{\overline F})=0$. The
Hochschild–Serre low-degree sequence, together with
$H^3(F,\overline F^\times)=0$ for these global and local fields, gives
(1.2). Restricting to the kernel of $c^*$ selects the unique normalized
representative of every quotient class. All maps are functorial under
field extension. $\square$

**[THEOREM, verified source input]** The exact sequences just used are
written explicitly in González-Avilés, *Brauer groups and Tate–Shafarevich
groups*, *J. Math. Sci. Univ. Tokyo* **10** (2003), 391–419,
[equations (5)–(6), pp. 401–402](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms100207.pdf),
[arXiv:math/0104214](https://arxiv.org/abs/math/0104214).
The rational-point specialization and local evaluation compatibility are
also given in [McCallum, *Brauer Points on Fermat Curves*, §2, p. 4](https://math.arizona.edu/~wmc/Research/BrauerFermat.pdf).
No finiteness or nondivisibility hypothesis on Sha enters these exact sequences.

Define the *strictly locally trivial* group
$$
\mathcal B(X)=\ker\left(\operatorname{Br}(X)\longrightarrow
                                    \prod_v\operatorname{Br}(X_{\mathbb Q_v})\right).
\tag{1.3}
$$
This is distinct in its definition from being merely locally constant.

**[NEW] Proposition 1.1.** The map (1.2) induces
$$\mathcal B(X)\simeq\operatorname{Sha}(J/\mathbb Q).\tag{1.4}$$
In particular $\mathcal B(X)\subset\operatorname{Br}_c(X)$.

*Proof.* A strictly locally trivial class evaluates at $c$ to a class in
$\operatorname{Br}(\mathbb Q)$ trivial at every completion. It is zero
by Brauer–Hasse–Noether, so the class is normalized. Conversely a normalized
representative whose image in $H^1(\mathbb Q,J)$ is locally zero becomes
a constant Brauer class at each place. Its evaluation at $c$ is zero,
so that local constant is zero. This proves both directions. $\square$

The rational cusp is what makes the normalization global. If an arbitrary
representative is locally constant, the constants are its local evaluations
at $c$ and are removed by the single global class $s^*c^*\beta$.
One must not discard the base-field term before checking this compatibility.

## 2. Exactly what finite geometric cohomology omits

Fix $n\geq1$. Since the generic base has characteristic zero, $\mu_n$
is an étale coefficient sheaf. Put
$$
\mathcal A_n(F)=\ker\left(H^2(X_F,\mu_n)\to H^2(X_{\overline F},\mu_n)\right)
                 \cap\ker\left(c^*:H^2(X_F,\mu_n)\to H^2(F,\mu_n)\right).
\tag{2.1}
$$

**[NEW] Proposition 2.1 (the missing middle term).** There are natural
identifications and an exact sequence
$$
\begin{gathered}
H^1(X_{\overline F},\mu_n)=J[n],\qquad
H^2(X_{\overline F},\mu_n)=\mathbb Z/n,\\
\mathcal A_n(F)\simeq H^1(F,J[n]),\\
0\to J(F)/nJ(F)\to\mathcal A_n(F)
                  \to\operatorname{Br}_c(X_F)[n]\to0.
\end{gathered}\tag{2.2}
$$
For these formulas there is no need to exclude even $n$ at real places.

*Proof.* Geometric Kummer theory gives the first equality. Multiplication
by $n$ is surjective on $J(\overline F)$, so geometric Kummer theory and
Tsen give the second equality, with trivial Galois action and generator
$c_1(\mathcal O(c))$.

Use the Hochschild–Serre spectral sequence for $\mu_n$. The degree-two
restriction map onto $H^2(X_{\overline F},\mu_n)$ is surjective because
of this degree-one cycle class. Its kernel has a filtration
$$
0\to H^2(F,\mu_n)\to
  \ker(H^2(X_F,\mu_n)\to H^2(X_{\overline F},\mu_n))
  \to H^1(F,J[n])\to0.
\tag{2.3}
$$
Here the potentially relevant differential
$d_2^{1,1}:H^1(F,J[n])\to H^3(F,\mu_n)$ is zero: the section makes
$H^3(F,\mu_n)\to H^3(X_F,\mu_n)$ injective, whereas the image of this
differential is killed by that edge map. The same argument handles the
earlier base-field differential. There are no other incoming or outgoing
differentials affecting the $(1,1)$ term. Thus no assertion that
$H^3(F,\mu_n)=0$ at even $n$ is being made. The section splits the left
term of (2.3); its kernel is precisely $\mathcal A_n(F)$.

Finally Kummer theory gives
$0\to\operatorname{Pic}(X_F)/n\to H^2(X_F,\mu_n)\to\operatorname{Br}(X_F)[n]\to0$.
The rational point makes $\operatorname{Pic}(X_F)=J(F)\oplus\mathbb Z[c]$:
the Picard descent obstruction is zero because constants inject in Brauer.
Remove the degree summand using $c_1(\mathcal O(c))$ and the constant
Brauer summand using $c^*$. The result is the last sequence in (2.2),
which is exactly the usual Galois Kummer sequence under (1.2). $\square$

Let $\mathcal A_n^{\rm Sel}(\mathbb Q)$ consist of the classes whose
localizations in $\mathcal A_n(\mathbb Q_v)$ come from
$J(\mathbb Q_v)/nJ(\mathbb Q_v)$ in (2.2).

**[NEW] Corollary 2.2 (all local conditions retained).**
$$
\begin{split}
\mathcal A_n^{\rm Sel}(\mathbb Q)&=\operatorname{Sel}_n(J/\mathbb Q),\\
0\to J(\mathbb Q)/nJ(\mathbb Q)&\to\mathcal A_n^{\rm Sel}(\mathbb Q)
                    \to\mathcal B(X)[n]\to0.
\end{split}\tag{2.4}
$$

*Proof.* Under (2.2), the defining local condition is exactly the local
Kummer condition for the finite Selmer group. Quotienting its global
Kummer subspace gives $\operatorname{Sha}(J)[n]$, hence (1.4) proves
the second line. $\square$

Thus the geometric group $H^2(X_{\overline{\mathbb Q}},\mu_n)$ records
only the degree class. The entire space in (2.4) lies in its restriction
kernel. A finite integral Betti presentation of geometric $H^2$, even
with its complete Hecke action, gives no injection of this arithmetic
kernel into the geometric group. Formula (2.4) computes the omitted
cokernel explicitly: it is $\operatorname{Sha}(J)[n]$.

## 3. Transfers and the normalization correction

Let $f:X\to E$ be a finite modular parametrization of degree $d$ with
$f(c)=O$. Pullback and norm on Picard varieties are the maps
$i:E\to J$ and $\pi:J\to E$ of the visibility note. On Brauer groups,
$f_*$ denotes corestriction. It can be defined on function fields; residue
compatibility at the closed points of these characteristic-zero curves
shows that it preserves unramified classes and hence lands in
$\operatorname{Br}(E)$. The restriction–corestriction identity gives
$f_*f^*=[d]$.

For the normalized groups define
$$f_*^0=N_O f_*,\qquad \Theta_c=f^*f_*^0.$$
Pullback $f^*$ itself preserves normalization because $f(c)=O$.

**[NEW] Proposition 3.1.** Under (1.2), these are the maps induced on
$H^1$ by $\pi,i$, respectively, and
$$f_*^0f^*=[d],\qquad \Theta_c=f^*f_*^0\ \longleftrightarrow\ i\pi.
\tag{3.1}
$$
They preserve strictly locally trivial groups. On those groups the
normalization correction to $f_*$ is already zero.

*Proof.* Pullback and norm commute with the divisor sequences defining
Picard groups, and with the Galois cohomology sequences defining (1.2).
Their actions on the degree-zero geometric Picard group are exactly
$f^*=i$ and $f_*=\pi$. Modding out constants therefore gives the asserted
maps, and normalization chooses their unique representatives. Since
$N_O$ is the identity on $\operatorname{Br}_O(E)$, the norm identity
proves the first equation in (3.1).

Both field restriction and corestriction commute with localization
(including the sums over points in a fiber). They send a class zero
over every completion to another such class. Its evaluation at $O$ is
then zero by Brauer–Hasse–Noether, proving the last assertion. $\square$

For a general Hecke correspondence $X\leftarrow C\to X$, use its
pull–norm action on Brauer and then apply $N_c$. The correspondence
sends constants to constants. Consequently
$N_c T N_c S=N_c TS$, so the normalized actions still satisfy the
Hecke algebra relations. The induced Picard action fixes the convention;
one must not interchange Picard and Albanese actions at bad-level operators.
For $T_\ell$ with $\ell\nmid N$, the two maps have degree $\ell+1$.
The conventions are explicitly specified in
[Ribet–Wake, PNAS **119** (2022), e2210032119, §2.2](https://pmc.ncbi.nlm.nih.gov/articles/PMC9565053/),
[DOI 10.1073/pnas.2210032119](https://doi.org/10.1073/pnas.2210032119).

The norm relation supplies a nonzero scalar, not zero. For example, on
$\gamma=f^*\beta$ with $\beta\in\mathcal B(E)$,
$$\Theta_c\gamma=d\gamma.\tag{3.2}$$
Away from $d$, pullback is therefore injective and split by $d^{-1}f_*^0$.
This recovers the surviving Sha summand in the visibility proof directly
on the Brauer group.

## 4. Cusps and zero-cycle evaluations do not detect these classes

**[NEW] Proposition 4.1.** If $\beta\in\mathcal B(X)$ and $z$ is any closed
point of $X$ with residue number field $L$, then $\beta(z)=0$ in
$\operatorname{Br}(L)$. In particular every evaluation on a rational
zero-cycle is zero.

*Proof.* At every completion $L_w$ above $\mathbb Q_v$, the evaluation
is the pullback of the zero class $\beta_v\in\operatorname{Br}(X_{\mathbb Q_v})$.
Thus $\beta(z)$ is locally zero everywhere over $L$. Brauer–Hasse–Noether
over $L$ gives $\beta(z)=0$. Zero-cycle evaluation is the sum of these
evaluations followed by corestriction. $\square$

This includes all rational cusps and all finite fibers of a modular
parametrization. A proof that evaluations on a selected finite set of
cusps vanish gives no additional constraint on $\mathcal B(X)$: even
all closed points give the same zero tests.

Manin–Drinfeld torsion of cuspidal divisor differences is a statement
inside the degree-zero Picard group. It does not turn (2.4)'s locally
defined line-bundle classes into one global line bundle. Correspondences
supported on products of zero-dimensional cycles with $X$ act through
degree or evaluation and vanish on the normalized middle group. A
relation expressing an operator solely by such correspondences would
also make its induced endomorphism of $J$ zero; it cannot represent
$\Theta=i\pi$, which acts on $E$ by the nonzero scalar $d$.

## 5. An explicit failed Eisenstein annihilator on the actual curve

For $E=389a1$ we have $d=40$ and $a_2=a_3=-2$, established by the exact
computations in the prior notes. Consider
$$t_0=T_2-T_3+1.$$

**[NEW] Proposition 5.1.** On the constant and geometric degree pieces
of the cohomology of $X_0(389)$, the operator $t_0$ is zero. On the
$E$-constituent of $H^1(\mathbb Q,J[n])$ and of $\mathcal B(X_0(389))$,
it is the identity wherever that constituent is defined by pullback
from $E$.

*Proof.* On constants $T_\ell$ acts by the norm degree $\ell+1$.
On geometric $H^2(\mu_n)$ it also acts by $\ell+1$: pullback multiplies
the degree by this factor and the norm preserves the degree of divisors.
Thus $t_0$ acts on both by $3-4+1=0$. On $E$ its eigenvalue is
$a_2-a_3+1=1$. Functoriality on Galois cohomology and the
Hochschild–Serre identification transfers this identity to the stated
arithmetic groups. $\square$

The classical rational-torsion proof uses an additional injectivity
that is absent here. In Ribet–Wake §2.5, Lemma 2.4, a prime-to-residue-
characteristic rational torsion subgroup injects into the reduction of
the Jacobian, and Eichler–Shimura gives the Eisenstein action there.
A strictly locally trivial Brauer class instead maps to zero already
in the Brauer group of the local generic curve. There is no analogous
injection from it into the reduction.

In particular, annihilating the known constant/cuspidal or geometric
pieces cannot be promoted to annihilating the middle group (2.4).
For $389a1$, doing that with $t_0$ would be exactly the unproved assertion
that the remaining elliptic group is zero.

## 6. Testing the Frobenius homotopy directly

There is a tempting stronger argument: for $\ell\nmid Np$, Eichler–Shimura gives
$T_\ell=\rho(g)+\ell\rho(g)^{-1}$ for an unramified Frobenius $g$ on
$T_pJ$, and inner conjugation acts trivially on
Galois cohomology. One might therefore try to conclude that
$T_\ell$ acts as $\ell+1$ on $H^1$, yielding the annihilator above.
The two actions in this proposed deduction are different.

**[NEW] Lemma 6.1 (the exact cocycle discrepancy).** Let $G$ act on a
module $M$, let $z:G\to M$ be a one-cocycle, and fix $g\in G$. The
cochain map from inner conjugation is
$$
(g\star z)(\sigma)=g\,z(g^{-1}\sigma g)
                  =z(\sigma)+(\sigma-1)z(g).
\tag{6.1}
$$
It induces the identity on $H^1(G,M)$. In contrast the operation
$z(\sigma)\mapsto g z(\sigma)$ is generally not a cochain map; its
cocycle defect at $(\sigma,\tau)$ is
$$ (g\sigma-\sigma g)z(\tau).\tag{6.2}$$

*Proof.* Expand $z(g^{-1}\sigma g)$ twice using
$z(ab)=z(a)+az(b)$ and $z(g^{-1})=-g^{-1}z(g)$; this gives (6.1).
Its correction is a coboundary. Expanding the cocycle condition after
coefficient multiplication by $g$ gives (6.2). $\square$

Eichler–Shimura relates the **coefficient** operators. Their sum is
Galois-equivariant, but its two summands need not separately define
endomorphisms of global cohomology. Equation (6.1) changes cocycle
arguments as well, so it does not replace either summand by the identity.
On a local unramified cyclic quotient the situation is different, but
restriction there loses exactly the classes under investigation.

This checks a specific possible construction rather than assuming it
cannot exist. To repair it one would have to construct a global
cochain homotopy, compatible with every local Kummer condition, for
the actual Hecke operator. No such homotopy is supplied by (6.1).

## 7. Transfer to a fixed regular arithmetic surface

Choose a regular connected two-dimensional scheme $\mathcal X$ proper
over $\operatorname{Spec}\mathbb Z$, with generic fiber $X$. Such a
regular proper model exists by resolution of arithmetic surfaces.
The rational cusp extends to a section by properness. Define
$$
\operatorname{Br}(\mathcal X)'=
\ker\left(\operatorname{Br}(\mathcal X)\to\operatorname{Br}(X_{\mathbb R})\right).
\tag{7.1}
$$

**[THEOREM: Milne's model comparison, verified in González-Avilés]**
For a regular connected surface proper over a nonempty open
$U\subset\operatorname{Spec}\mathbb Z$, with smooth geometrically
connected generic curve, the sequence
$$
0\to\operatorname{Br}(\mathcal X_U)\to\operatorname{Br}(X)
 \longrightarrow\bigoplus_{v\in U}\operatorname{Br}(X_{\mathbb Q_v})
\tag{7.2}
$$
is exact. This is
[González-Avilés, Lemma 2.2(b), p. 402](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms100207.pdf),
which cites Milne, *Comparison of the Brauer group with the Tate–Shafarevich
group*, J. Fac. Sci. Univ. Tokyo Sect. IA **28** (1981/1982), 735–743,
Lemma 2.6. Crucially, (7.2) has no finite-Sha or no-infinitely-divisible-Sha
hypothesis. The main order-comparison theorem in the 2003 paper does
have an additional hypothesis of that kind and is not used here.

**[NEW] Corollary 7.1 (the fixed-surface identification).**
$$
\operatorname{Br}(\mathcal X)'\simeq\mathcal B(X)
                               \simeq\operatorname{Sha}(J/\mathbb Q).
\tag{7.3}
$$
This is an identification of the whole groups, not just their finite
quotients or their prime-to-a-finite-set parts.

*Proof.* With $U=\operatorname{Spec}\mathbb Z$, the image in (7.2)
is exactly the kernel of all finite local restrictions. Imposing the
remaining real-place restriction gives (1.3). Apply Proposition 1.1.
$\square$

Thus all the target classes do extend to **one fixed** regular arithmetic
surface. Properness and unramified extension have not annihilated them.
Generic Hecke actions preserve $\mathcal B(X)$; (7.2)'s injectivity
therefore extends their action uniquely to $\operatorname{Br}(\mathcal X)'$.
This does not by itself construct an action on a chosen integral
finite-coefficient cochain complex of the model: extending correspondence
cycles and trace maps there is additional data.

For a good prime $\ell$, the smooth proper fiber has Brauer group zero
(Tsen, finite-field Hochschild–Serre, and Lang's theorem for its Jacobian).
Restriction to such fibers accordingly kills all classes from (7.3),
not just the classes already known to be zero. A specialization identity
for Hecke correspondences on the special fiber therefore proves no
injectivity back on (7.3). The distinction is visible on actual modular
curves: the known $3$-classes of $5389a1$ inject into
$\operatorname{Sha}(J_0(5389))$ because its modular degree is prime to $3$,
and hence give nonzero elements of (7.3) despite all these good-fiber
Brauer groups being zero. The source verification is in the visibility note.

On the fixed arithmetic model one must use fppf Kummer theory when
$n$ is not invertible. It gives the precise sequence
$$
0\to\operatorname{Pic}(\mathcal X)/n\to
 H^2_{\rm fppf}(\mathcal X,\mu_n)\to\operatorname{Br}(\mathcal X)[n]\to0.
\tag{7.4}
$$
Taking the preimage of the real-trivial Brauer subgroup retains
$\operatorname{Br}(\mathcal X)'[n]$ as the cokernel. Consequently even
a separately proved finite presentation of $\operatorname{Pic}(\mathcal X)$
controls the left term, not this quotient. The arithmetic-surface Picard
and zeta calculations in the coordinator's separate task are not assumed
to prove a further cohomological comparison here.

## 8. Removing the real-place term for 389a1

The coordinator asked whether the complete Brauer group of a proper
regular arithmetic model $\mathcal E/\mathbb Z$ of $E=389a1$ equals
its subgroup trivial over $\mathbb R$. The answer is yes, for a reason
that keeps all $2$-primary information.

**[NEW] Proposition 8.1.** Let $E/\mathbb Q$ have two real components
and a point $Q\in E(\mathbb Q)$ on its nonidentity component. For any
regular proper arithmetic model $\mathcal E/\mathbb Z$ of $E$,
$$\operatorname{Br}(\mathcal E)=\operatorname{Br}(\mathcal E)'
                              \simeq\operatorname{Sha}(E/\mathbb Q).
\tag{8.1}
$$
If $E(\mathbb R)$ is connected, the same assertion follows from the
zero section alone.

*Proof.* Both $O$ and $Q$ extend to sections. Their evaluations of
$\beta\in\operatorname{Br}(\mathcal E)$ lie in
$\operatorname{Br}(\mathbb Z)=0$. Normalize $\beta_{\mathbb R}$ at
$O$ and let $\alpha\in H^1(\mathbb R,E)$ be its image under (1.2).
Local Tate duality is a perfect pairing
$$E(\mathbb R)/N E(\mathbb C)\ \times H^1(\mathbb R,E)\to\mathbb Q/\mathbb Z.$$
Here $N(P)=P+\overline P$. Its image is exactly $E(\mathbb R)^0$:
$E(\mathbb C)$ is connected, so the image is connected, and it contains
$2E(\mathbb R)^0=E(\mathbb R)^0$. Thus the quotient is the two-element
component group, generated by $Q$.

The local Brauer evaluation identity is
$$\operatorname{inv}_{\mathbb R}(\beta(Q)-\beta(O))=\langle Q,\alpha\rangle.$$
Its left side is zero, so perfection forces $\alpha=0$. The remaining
Brauer class is constant and evaluates to zero at $O$, hence is zero.
This proves equality with the real-trivial subgroup; (7.3) proves (8.1).
For connected $E(\mathbb R)$ the norm quotient and $H^1(\mathbb R,E)$
are both zero, so the same argument uses only $O$. $\square$

**[THEOREM, verified local inputs]** The norm-quotient version of local
duality, including real places, is recorded in González-Avilés §1,
pp. 398–399. The evaluation identity is explicitly given in McCallum §2,
p. 4, citing Manin's 1970 ICM article. Neither input assumes finite Sha.

For $389a1$, the point $Q=(0,-1)$ lies in the bounded real component:
the roots of $x^3+x^2-2x+1/4$ are in $(-3,-1)$, $(0,1/4)$, $(1/2,1)$,
as certified in [the archimedean note](bsd-archimedean-bound.md).
The identity component contains infinity and is unbounded. Thus (8.1)
applies. The explicit equation and regularity verification of the
coordinator's arithmetic model are separate from this general argument.

## 9. The remaining cycle-lifting construction

For $X=X_0(389)$, the prior work proves that pullback identifies
$\operatorname{Sha}(E)$ with its full image in $\operatorname{Sha}(J)$;
the possible kernel is killed by $40$, and both the $2$- and $5$-primary
parts of $\operatorname{Sha}(E)$ are zero. Norm is surjective onto
$\operatorname{Sha}(E)$: on every remaining primary part use
$f_*f^*=[40]$ and invert $40$.

**[NEW: exact arithmetic image]** Under (7.3) and (8.1), this gives
$$
\operatorname{im}\bigl(\Theta_c:\operatorname{Br}(\mathcal X)'
                              \to\operatorname{Br}(\mathcal X)'\bigr)
 =f^*\operatorname{Br}(\mathcal E)
 \simeq\operatorname{Br}(\mathcal E).
\tag{9.1}
$$
The maps are defined on generic fibers and then extended uniquely by
(7.2); no finite-flat extension of $f$ between the chosen models is
silently assumed. This realizes the residual target as a specific
Brauer group on a fixed arithmetic surface, with its real term removed.

A direct construction at finite coefficients would have to do the following.

**[GAP HB-cycle, concrete sufficient construction for 389a1]** For every
$n\geq1$ and every
$z\in\mathcal A_n^{\rm Sel}(\mathbb Q)$ on $X_0(389)$, construct a
degree-zero rational line bundle $L_z\in\operatorname{Pic}^0(X_0(389))$
such that
$$\Theta_c z=c_1(L_z)\quad\text{in }\mathcal A_n(\mathbb Q).
\tag{9.2}
$$
The action here is the normalized pull–norm action on generic
finite-coefficient cohomology. Equation (2.4) proves that (9.2) would
kill every torsion class in (9.1), and hence prove
$\operatorname{Sha}(389a1)=0$. No analogous inference follows just
from the existence of local line bundles $L_{z,v}$: those are already
the Selmer conditions in (2.4).

The attempted constructions were: evaluation on cusps or norm fibers;
eliminating the degree and constant terms by an Eisenstein operator;
using the inner-conjugation homotopy with Eichler–Shimura; and extending
unramified classes to a proper regular model then specializing. Propositions
4.1, 5.1, Lemma 6.1, and the exact model comparison show precisely what
each actually supplies. None supplies the global line bundle in (9.2)
or a fixed integer multiple of it uniformly in $n$.

Allowing a fixed nonzero scalar multiple in (9.2) would suffice for
full Sha finiteness and an explicit prime bound, followed by separate
checks at those primes. Constructing that scalar or those line bundles
remains the unresolved arithmetic step. The universal full-BSD objective
also still requires the rank and leading-term comparisons beyond this
Brauer/Sha attack.
