# Modular Jacobians, visibility, and the Sha that survives the projector

Date: 2026-09-12. This is a proof attempt toward the charter's universal
full-BSD objective. It neither proves nor disproves BSD. The `[NEW]`
deductions below are elementary consequences with proofs; they passed the
[coordinator review](review-modular-visibility.md) with the stated scope.

The proposed bound “every Sha prime divides the modular degree or congruence
number” is false for actual elliptic curves: §5 gives the published
$5389a1$ example. The exact calculation for the rank-two test curve gives
a different useful result:
$$
\operatorname{Vis}_{J_0(389)}\operatorname{Sha}(389a1)=0.
\tag{0.1}
$$
Thus all of its possible remaining Sha injects into the modular Jacobian;
the fixed visibility kernel contains none of it. A winding quotient
does not resolve this: its projection kills the elliptic factor already
as a morphism of abelian varieties. The argument below reaches an explicit
integer Hecke-operator annihilation problem, keeping the full local Selmer
conditions throughout.

## 1. Geometric maps and the modular-degree relation

Let $E/\mathbb Q$ be the optimal quotient attached to a rational newform
of exact level $N$. Set $J=J_0(N)$ and let $\pi:J\to E$ have connected
kernel. The dual map, using the principal polarizations of $J$ and $E$,
is an embedding $i:E\hookrightarrow J$. Write
$$
0\longrightarrow E\overset{i}{\longrightarrow}J
 \overset{q}{\longrightarrow}B\longrightarrow0,
\qquad d=\deg(X_0(N)\longrightarrow E).
\tag{1.1}
$$
The quotient $B=J/i(E)$ is not being identified with $\ker\pi$ integrally.

**[THEOREM]** The pullback–pushforward relation is
$$\pi i=[d]_E.\tag{1.2}$$
It follows either from pullback and norm for the degree-$d$ map of curves,
or from the modular polarization. See
[Cremona–Mazur, *Visualizing elements in the Shafarevich–Tate group*, §3,
“Optimal modular elliptic curves”](https://swc-math.github.io/notes/files/99MazurCremonaV.pdf),
published in *Experimental Mathematics* **9** (2000), 13–28,
[DOI 10.1080/10586458.2000.10504633](https://doi.org/10.1080/10586458.2000.10504633).
Their modular degree is the integer $d$ in (1.2); the degree of the
polarization $E\to E$ is $d^2$.

**[NEW] Lemma 1.1 (integral complementary map).** There is a homomorphism
$j:B\to J$ defined over $\mathbb Q$ such that
$$
jq=[d]_J-i\pi,\qquad qj=[d]_B,\qquad\pi j=0.
\tag{1.3}
$$

*Proof.* The morphism $[d]_J-i\pi$ vanishes on $i(E)$ by (1.2), so it
factors through the abelian-variety quotient $q$. Composing with $q$
gives $qj q=dq$, hence $qj=d$ because $q$ is surjective. Similarly
$\pi j q=d\pi-\pi i\pi=0$, so $\pi j=0$. $\square$

For a nonoptimal curve one can first use an isogeny to its optimal member,
but its degree must then be retained in every exceptional-prime set. None
of the statements below silently identifies different members of an
isogeny class integrally.

## 2. The global and local visibility sequences

For $F=\mathbb Q$ or $\mathbb Q_v$, let
$$
C(F)=B(F)/qJ(F),\qquad
\delta_F:C(F)\hookrightarrow H^1(F,E)
\tag{2.1}
$$
be the connecting map from (1.1). Here $H^1$ is Galois cohomology with
coefficients in the geometric points of the indicated abelian variety.

**[NEW] Proposition 2.1 (the exact visible subgroup).** The sequence
$$
0\to C(\mathbb Q)\overset{\delta}{\longrightarrow}H^1(\mathbb Q,E)
 \overset{i_*}{\longrightarrow}H^1(\mathbb Q,J)
 \overset{q_*}{\longrightarrow}H^1(\mathbb Q,B)
\tag{2.2}
$$
is exact at its first three nonzero terms, with the usual continuation
to $H^2(\mathbb Q,E)$. If
$$V_J(E)=\ker(\operatorname{Sha}(E)\to\operatorname{Sha}(J)),$$
then
$$
V_J(E)\simeq\ker\left(C(\mathbb Q)\longrightarrow
                                  \prod_v C(\mathbb Q_v)\right).
\tag{2.3}
$$
Moreover $C(F)$, and hence every visible class, is killed by $d$.
The group $C(\mathbb Q)$ is finite, without assuming Sha finiteness.

*Proof.* The long cohomology sequence proves (2.2), globally and locally.
A boundary class $\delta(b)$ is everywhere locally trivial precisely
when each $b$ lifts to a point of $J(\mathbb Q_v)$, proving (2.3).
Equation (1.3) gives $dB(F)\subset qJ(F)$, hence $dC(F)=0$.
Mordell–Weil makes $B(\mathbb Q)/dB(\mathbb Q)$ finite, and it surjects
onto $C(\mathbb Q)$. $\square$

In particular
$$V_J(E)\subseteq\operatorname{Sha}(E)[d],\tag{2.4}$$
which bounds the **order of each visible element**, not necessarily the
cardinality of the entire visible group by $d$. Visibility here always
means this kernel for the specified embedding. This agrees with
[Agashe–Stein, JNT **97** (2002), 171–185, Definitions 1.1–1.2 and (1.1)](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf),
[DOI 10.1006/jnth.2002.2810](https://doi.org/10.1006/jnth.2002.2810).

It is not generally correct to omit all local obstructions and write
$\operatorname{Sha}(E)\to\operatorname{Sha}(J)\to\operatorname{Sha}(B)$
as an exact sequence at the middle. An explicit correction is available.

**[NEW] Proposition 2.2 (the missing local term).** Put
$$
\mathcal C=\left(\prod_v C(\mathbb Q_v)\right)
                  /\operatorname{loc} C(\mathbb Q).
$$
There is a natural exact sequence
$$
0\to V_J(E)\to\operatorname{Sha}(E)
 \to\ker(\operatorname{Sha}(J)\to\operatorname{Sha}(B))
 \overset{o}{\longrightarrow}\mathcal C.
\tag{2.5}
$$
No surjectivity onto $\mathcal C$ is asserted. The same sequence on
$p$-primary parts is exact; one may replace $\mathcal C$ by
$\prod_v C(\mathbb Q_v)[p^\infty]/\operatorname{loc}C(\mathbb Q)[p^\infty]$.

*Proof.* If $\eta$ is in the middle kernel, (2.2) gives a lift
$\alpha\in H^1(\mathbb Q,E)$. For each $v$, its image in $H^1(\mathbb Q_v,J)$
is zero, so $\alpha_v$ lies in the injective image of $C(\mathbb Q_v)$.
Use these inverse images to define $o(\eta)$. A different global lift
differs by $\delta C(\mathbb Q)$, so the quotient removes the ambiguity.
The obstruction is zero precisely when subtracting a global boundary
makes the lift everywhere locally trivial. This proves exactness.
All the local and global $C$ groups are killed by the fixed integer $d$.
Their primary decompositions therefore commute with the product and
the quotient, proving the last assertion. $\square$

## 3. Finite Selmer groups and prime-to-degree splitting

Let $n=p^k$. For an abelian variety $A$ and a completion $F$, write
$$
\mathcal K_A(F,n)=\operatorname{im}\bigl(A(F)/nA(F)
                             \to H^1(F,A[n])\bigr).
$$
Then
$$
\operatorname{Sel}_n(A)=
\{x\in H^1(\mathbb Q,A[n]):x_v\in\mathcal K_A(\mathbb Q_v,n)
                                      \text{ for every }v\}.
\tag{3.1}
$$
All morphisms of abelian varieties send their Kummer conditions to the
corresponding Kummer conditions. This is the only local input needed
for the splitting below, so no ordinary, supersingular, or good-reduction
hypothesis on $p$ is needed.

Multiplication by $n$ on (1.1) gives the exact geometric torsion sequence
$$0\to E[n]\to J[n]\to B[n]\to0.$$
Let $\Delta_n:B(\mathbb Q)[n]\to H^1(\mathbb Q,E[n])$ be its connecting map.

**[NEW] Proposition 3.1 (finite-level kernel and local obstruction).**
Define
$$
U_n=B(\mathbb Q)[n]\cap\bigcap_v qJ(\mathbb Q_v).
$$
Then
$$
\ker(\operatorname{Sel}_n(E)\to\operatorname{Sel}_n(J))
 =\Delta_n(U_n)\simeq U_n/q(J(\mathbb Q)[n]).
\tag{3.2}
$$
More fully, there is an exact sequence
$$
0\to U_n/q(J(\mathbb Q)[n])\to\operatorname{Sel}_n(E)
 \to\ker(\operatorname{Sel}_n(J)\to\operatorname{Sel}_n(B))
 \to\mathcal C_n,
\tag{3.3}
$$
where
$$
\mathcal C_n=
\left(\prod_v C(\mathbb Q_v)[n]\right)
 /\operatorname{loc}\delta\bigl(B(\mathbb Q)[n]\bigr).
\tag{3.4}
$$
In (3.4), $\delta(b)_v$ is identified with an element of $C(\mathbb Q_v)[n]$
using its injective connecting map. The last map need not be surjective.

*Proof.* The kernel in global torsion cohomology is
$\Delta_n B(\mathbb Q)[n]$, with kernel $q(J(\mathbb Q)[n])$.
The image of $\Delta_n(b)$ in $H^1(\mathbb Q_v,E)$ is the ordinary
boundary $\delta_v(b)$. Thus $\Delta_n(b)$ satisfies the local Kummer
condition exactly when $b\in qJ(\mathbb Q_v)$, proving (3.2).

For (3.3), lift a class in the middle kernel to
$\alpha\in H^1(\mathbb Q,E[n])$. Locally $i_*\alpha_v$ is in the Kummer
image for $J$. The image of $\alpha_v$ in $H^1(\mathbb Q_v,E)[n]$
therefore lies in $C(\mathbb Q_v)[n]$. Changing the lift changes these
classes by the local boundaries of a single point of $B(\mathbb Q)[n]$.
The obstruction is zero precisely when a corrected global lift belongs
to $\operatorname{Sel}_n(E)$. This gives the stated exact sequence. $\square$

**[NEW] Theorem 3.2 (the full splitting away from $d$).** If $p\nmid d$,
then for every $k\geq1$
$$
\begin{split}
J[p^k]&\simeq E[p^k]\oplus B[p^k],\\
\operatorname{Sel}_{p^k}(J)&\simeq
                 \operatorname{Sel}_{p^k}(E)\oplus\operatorname{Sel}_{p^k}(B),\\
\operatorname{Sel}_{p^\infty}(J)&\simeq
                 \operatorname{Sel}_{p^\infty}(E)\oplus\operatorname{Sel}_{p^\infty}(B),\\
\operatorname{Sha}(J)[p^\infty]&\simeq
                 \operatorname{Sha}(E)[p^\infty]\oplus\operatorname{Sha}(B)[p^\infty].
\end{split}\tag{3.5}
$$
In the last two lines $d^{-1}$ means its action as a unit of $\mathbb Z_p$.
No finiteness assertion about any Sha group is used.

*Proof.* Let $\Phi:E\times B\to J$ be $(e,b)\mapsto i(e)+j(b)$ and
$\Psi:J\to E\times B$ be $(\pi,q)$. Equations (1.2)–(1.3) give
$\Psi\Phi=[d]$ and $\Phi\Psi=[d]$. On all modules killed by $p^k$ these
are inverse up to multiplication by the unit $d$. In particular they
give inverse maps on the geometric torsion modules, their global and
local cohomology, and the point quotients $A(F)/p^kA(F)$. The Kummer
diagrams commute, so the isomorphism preserves the full local conditions
in (3.1). This proves the finite Selmer assertion; compatible passage
to the direct limit proves the infinite one.

Alternatively apply $\Phi,\Psi$ to the global and local Weil–Châtelet
groups and invert $d$ on their $p$-primary parts. Taking localization
kernels gives the Sha assertion directly. $\square$

The consequence of excluding modular-degree primes is thus a surviving
**direct summand**, not its vanishing. At primes dividing $d$, (3.2)–(3.4)
record the additional torsion and local terms; one cannot replace them
by the same split formula.

## 4. What the congruence module actually gives

Let $K=\ker\pi$, and let $\mathbb T$ be the integral Hecke algebra acting
on $J$. Over $\mathbb Q$, the newform constituent gives a projector
$$e_E=\frac1d i\pi\in\operatorname{End}(J)\otimes\mathbb Q.$$
Let $\mathbb T_E$ and $\mathbb T_K$ be the images of $\mathbb T$ on
$E$ and $K$. The map
$$
0\to\mathbb T\to\mathbb T_E\oplus\mathbb T_K\to C_{\rm cong}\to0
\tag{4.1}
$$
has a finite cokernel. This is a fixed integral module, independent of $p$.

**[THEOREM]** For an optimal elliptic curve let $r_E$ be its congruence
number. Then $d\mid r_E$, and $v_p(r_E)=v_p(d)$ whenever $p^2\nmid N$.
In particular $r_E=d$ for squarefree $N$. The denominator of $e_E$ in
$\operatorname{End}(J)$ is $d$, and its denominator in the Hecke algebra
is $r_E$. These are Theorem 2.2 and Lemmas 4.2–4.4 in the
[18-page author version of Agashe–Ribet–Stein](https://www.wstein.org/papers/ars-congruence/current.pdf),
*The modular degree, congruence primes, and multiplicity one*,
published 2012, [DOI 10.1007/978-1-4614-1260-1_2](https://doi.org/10.1007/978-1-4614-1260-1_2).
The newform and optimality hypotheses are retained here.

**[NEW: implication and its limit]** If $p\nmid r_E$, then $e_E$ belongs
to $\mathbb T\otimes\mathbb Z_p$. Any $p$-primary Hecke module therefore
splits into its $e_E$ and $1-e_E$ parts. Applied to the actual Selmer and
Sha groups, its $e_E$ part is the elliptic summand in (3.5). Thus the
finite cokernel (4.1) removes mixing between the constituents. It gives
no map from that entire elliptic Sha summand into $C_{\rm cong}$.
The explicit connecting maps in §2 land only in the visible kernel.

This is also why semisimplicity of the Hecke action is insufficient:
it identifies which constituent contains a class, but does not decide
whether the constituent's Selmer quotient is nonzero. One would need
an additional arithmetic map to, or annihilation by, the fixed module
(4.1); no such map follows by taking its localization or its rational
projector.

## 5. An actual counterexample to the proposed universal degree bound

**[THEOREM: published example]** Consider the optimal curve $5389a1$
$$y^2+xy+y=x^3-35590x-2587197,\qquad5389=17\cdot317.$$
Its modular degree is prime to $3$, but
$$\operatorname{Sha}(5389a1)[3]\supseteq(\mathbb Z/3\mathbb Z)^2.$$
The two source ingredients must be distinguished carefully:

- [Cremona–Mazur, §4, “The kernel of multiplication by the modular degree”,
  p. 15 of the linked preprint](https://swc-math.github.io/notes/files/99MazurCremonaV.pdf)
  records that the modular degree of $5389A1$ is not divisible by $3$.
  Its simultaneous assertion that the full Sha order is $9$ was based on
  BSD; that is not used as proof of existence here.
- [Agashe–Stein, JNT 2002, §4.2 and Proposition 4.2](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf)
  subsequently prove the existence of these classes without conjectures.
  They become visible at level $7\cdot5389$ in an elliptic image $E'$
  related to $E$ by a $2$-power isogeny. Such an isogeny preserves
  $3$-primary Sha, by the same inverse-up-to-degree argument as §3.

The modular degree is an independent modular invariant, so the first
datum does not depend on the old conjectural Sha order. The second
paper explicitly separates its unconditional construction from that
prediction. Squarefree conductor and §4 also give $3\nmid r_E$.
Consequently both proposed assertions, with modular degree and with
congruence number, fail on this elliptic curve over $\mathbb Q$.
This is a counterexample to those proposed assertions, **not to BSD**.

For clarity about the theorem being used, a safe specialization of
Agashe–Stein's Theorem 3.1 over $\mathbb Q$ assumes abelian subvarieties
$A,F\subset J'$ with finite intersection, odd $n$ with $F[n]\subset A$,
good reduction of $J'$ at primes dividing $n$, and $n$ prime to
$\#(J'/F)(\mathbb Q)_{\rm tors}$, $\#F(\mathbb Q)_{\rm tors}$, and all
Tamagawa factors of $A,F$. It constructs a map
$F(\mathbb Q)/nF(\mathbb Q)\to V_{J'}(A)$ with kernel of size at most
$n^{\operatorname{rank}A(\mathbb Q)}$. The ramification inequality of
the source is automatic for odd $n$ over $\mathbb Q$. We have stated
good reduction for the ambient variety, a stronger hypothesis than
necessary, so the local argument at primes dividing $n$ applies directly.
The source checks the specific hypotheses for $5389a1$ at the higher level.
The theorem constructs a lower bound for Sha; it is not an upper bound
or a surjectivity theorem onto the whole group.

## 6. The exact test at level 389

**[THEOREM, exact modular-symbol and integral-homology computation]**
Sage 10.7 gives
$$J_0(389)\sim_{\mathbb Q}A_1\times A_2\times A_3\times A_6\times A_{20},$$
where the subscripts denote dimensions and $A_1=389a1$. The modular
kernel of the elliptic subvariety has abelian-group invariants $[40,40]$,
so its modular degree is $40$. An independent congruence-lattice
calculation gives $r_E=40$.

Reproduction (all operations here are exact):

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python - <<'PY'
from sage.all import *
D = J0(389).decomposition()
print([(A.dimension(), str(A.hecke_polynomial(2))) for A in D])
Esub = [A for A in D if A.dimension() == 1][0]
print(Esub.modular_kernel())
print(Esub.modular_degree())
print([(A.dimension(), A.lseries().lratio()) for A in D])
M = ModularSymbols(389, 2, sign=1)
W = [V for V in M.cuspidal_subspace().decomposition() if V.dimension() == 1][0]
print(W.congruence_number(W.complement().cuspidal_subspace()))
PY
```

The rational modular-symbol central-value ratios in the order above are
$$0,\quad0,\quad0,\quad0,\quad51200/97.$$
Only their zero/nonzero status is used here; the last ratio uses Sage's
homology-lattice normalization, not an asserted Néron-period BSD quotient.
The source implementation computes the winding element's image under the
rational period map and exact indices of integral lattices. The same
decomposition and vanishing pattern were already published in
Agashe–Stein §4.1.

The elliptic-curve method `E.modular_degree()` is intentionally absent:
its default `sympow` implementation uses a numerical stopping heuristic.
The modular-abelian-variety method above computes the finite polarization
kernel from exact integral homology; its order $1600$ gives $d=40$.

**[NEW: consequence for all primes at once]** By (2.4), the visible Sha
of $389a1$ is killed by $40=2^3\cdot5$. The existing
[exceptional-prime proof](exceptional-prime-finiteness.md) gives
$\operatorname{Sha}(E)[2^\infty]=0$, and the
[exact Kurihara witness](continuation-2026-09-12.md) gives
$\operatorname{Sha}(E)[5^\infty]=0$. Hence (0.1) follows, and the map
$$\operatorname{Sha}(389a1)\hookrightarrow\operatorname{Sha}(J_0(389))$$
is injective on the **entire** group, including any possible divisible
parts. A proof that the whole Sha is visible in this fixed Jacobian
would therefore amount to proving it zero.

This example also tests the direction of visibility concretely:
Agashe–Stein Proposition 4.1 uses the two rational-point directions of
$A_1$ to construct visible $(\mathbb Z/5\mathbb Z)^2$ in the Sha of
the dual of the dimension-20 factor. It produces classes in the other
factor; it supplies no upper bound for $\operatorname{Sha}(A_1)$.

## 7. Why the winding quotient cannot detect the surviving image

Let $J_w$ be the quotient formed from the modular newform factors with
nonzero central value, retaining their relevant oldform multiplicities.
At the prime level used below this is the usual winding quotient.
Its rational points and Sha are finite by the rank-zero modular-abelian-variety theorem of
Kolyvagin–Logachev. The exact construction and this use of that theorem
are recorded in [Agashe, *On invisible elements of the Tate–Shafarevich
group*, §2](https://www.math.fsu.edu/~agashe/math/craseng.pdf),
*C. R. Acad. Sci. Paris* **328** (1999), 369–374,
[DOI 10.1016/S0764-4442(99)80173-6](https://doi.org/10.1016/S0764-4442(99)80173-6).
Its subsequent examples of invisible classes at levels 1091 and 1429
assume BSD and are not being used as unconditional examples.

**[NEW] Lemma 7.1 (rank-zero targets kill the original curve).** If
$E(\mathbb Q)$ has positive rank and $A(\mathbb Q)$ is finite, then
$\operatorname{Hom}_{\mathbb Q}(E,A)=0$.

*Proof.* A nonzero homomorphism from an elliptic curve has finite kernel.
Its image of the infinite group $E(\mathbb Q)$ would then be infinite,
contradicting finiteness of $A(\mathbb Q)$. $\square$

It follows that the composition
$$E\overset{i}{\longrightarrow}J\longrightarrow J_w$$
is zero. The induced map on Sha is therefore zero regardless of the
size of $\operatorname{Sha}(E)$. Passing to the finite group
$\operatorname{Sha}(J_w)$ loses the original curve's image completely.
Equivalently, the rational winding projector has $E$-eigenvalue zero.
No homomorphism factoring through a rank-zero abelian variety can act
by a nonzero scalar on this $E$.

For $N=389$, the exact data in §6 identify $J_w$ up to isogeny with
$A_{20}$. The remaining abelian part has dimension twelve, comprising
$A_1,A_2,A_3,A_6$. Thus the hoped-for assumption that all complementary
factors have nonzero central value is already false in this test case.
Even if those complementary Sha groups were independently known finite,
(3.5) would still retain the unknown elliptic summand.

At the level of integral Hecke operators the same point can be seen
without any limiting argument. Let $g_{20}(X)$ be the $T_2$ characteristic
polynomial of $A_{20}$. The exact computation gives
$$g_{20}(-2)=-14500,$$
where $T_2$ acts on $E$ by $-2$. The operator $g_{20}(T_2)$ annihilates
the rank-zero factor, but acts as a nonzero integer on $E$. Knowing it
annihilates $\operatorname{Sha}(A_{20})$ says nothing about its action
on the complementary elliptic Sha. Conversely a projector onto $A_{20}$
acts by zero on $E$ and cannot bound it.

## 8. A precise, prime-independent Hecke criterion that would suffice

The modular degree does give a valid bound once the residual cohomology
image is bounded. The following isolates that additional input.

**[NEW] Proposition 8.1 (bounded-image criterion).** Suppose an integer
$c>0$ kills the image of $i_*:\operatorname{Sha}(E)\to\operatorname{Sha}(J)$.
Then $dc$ kills $\operatorname{Sha}(E)$, so it is finite and its possible
prime support is contained in the prime divisors of $dc$.

*Proof.* Apply $\pi_*$ to $c i_*x=0$ and use $\pi_*i_*=[d]$.
The group $\operatorname{Sha}(E)[dc]$ is finite as a quotient of the
finite $dc$-Selmer group. $\square$

**[NEW] Proposition 8.2 (a Hecke annihilator).** Let
$t\in\mathbb T$ satisfy $t\operatorname{Sha}(J)=0$, and let
$a_E(t)\in\mathbb Z$ be its eigenvalue on $E$. If $a_E(t)\ne0$, then
$d\,a_E(t)$ kills $\operatorname{Sha}(E)$. Thus an explicit such operator
would give an explicit finite-prime bound.

*Proof.* Hecke equivariance gives
$i_*(a_E(t)x)=t i_*x=0$. Apply $\pi_*$ and argue as above. $\square$

The fixed finite cokernel in (4.1) really constructs integral multiples
of the projector, but it does not show they annihilate Sha. In fact the
existence assertion in Proposition 8.2 is equivalent to Sha finiteness,
so treating it as automatic would be circular:

**[NEW] Proposition 8.3 (exact strength of that missing input).**
$\operatorname{Sha}(E)$ is finite if and only if
$$a_E\bigl(\operatorname{Ann}_{\mathbb T}\operatorname{Sha}(J)\bigr)\ne0.$$

*Proof.* One implication is Proposition 8.2. Conversely, if $c$ kills
$\operatorname{Sha}(E)$ and $D>0$ satisfies $D e_E\in\mathbb T$, take
$$t=cdD e_E=cD i\pi\in\mathbb T.$$
Since $\pi_*$ sends $\operatorname{Sha}(J)$ into $\operatorname{Sha}(E)$,
this $t$ kills $\operatorname{Sha}(J)$. Its $E$-eigenvalue is $cdD\ne0$.
$\square$

For $389a1$ the explicit integral projector numerator is
$$\Theta=40e_E=i\pi\in\mathbb T,$$
using $r_E=d=40$. The residual statement can be written without any
varying prime:

**[GAP H389]** Prove that the endomorphism $\Theta$ sends every everywhere
locally trivial $J_0(389)$-torsor class to zero in $H^1(\mathbb Q,J_0(389))$.

If this is proved, then (0.1) and $\Theta i=i[40]$ give
$40\operatorname{Sha}(E)=0$, and the known $2$- and $5$-parts force
$\operatorname{Sha}(E)=0$. Conversely that vanishing makes
$\Theta\operatorname{Sha}(J)=i\pi\operatorname{Sha}(J)=0$. Thus H389
is a sharply specified integral cohomology problem, not a consequence of
the already computed projector.

One can also construct a numerator using $T_2$ alone. If $h$ is the product
of the $T_2$ polynomials of dimensions $2,3,6,20$, then
$$h(T_2)=-58000e_E.$$
The evaluations of these four polynomials at $-2$ are respectively
$2,-2,-1,-14500$. This unnecessarily introduces the prime $29$;
the full Hecke algebra reduces the denominator to $40$. Removing the
extra denominator does not prove either numerator annihilates Sha.

## 9. Higher level and fixed ambient varieties

The true theorem that every torsor class is visible in some abelian
variety does not supply one ambient variety for every class. In
[Agashe–Stein Proposition 1.3](https://wstein.org/papers/visibility_of_sha/jnt_version.pdf),
one chooses a finite field extension splitting the particular class and
uses $\operatorname{Res}_{L/\mathbb Q}E_L$. The extension depends on the
class. A bound on these extensions is one of the unresolved equivalent
finiteness targets in the [geometric attack](genus-one-finiteness-attack.md).

**[NEW] Lemma 9.1 (fixed visibility is already finiteness).** The full
$\operatorname{Sha}(E)$ is visible in some single fixed embedding
$E\hookrightarrow A$ if and only if it is finite.

*Proof.* A fixed visible group is finite by Proposition 2.1's
Mordell–Weil argument (for a general embedding use Poincaré reducibility
to obtain a retraction up to a nonzero integer). Conversely, if Sha is
finite, choose a finite splitting field for each of its finitely many
classes and take their compositum $L$. The Weil-restriction embedding
in the cited proof kills every class at once. $\square$

Likewise, moving to a higher modular level can make previously invisible
classes visible, as §5 demonstrates, but any retraction up to degree $d'$
of that new embedding must have $p\mid d'$ when a nonzero order-$p$ class
is killed. This follows at once by applying the retraction to the killed
class. Thus arbitrary auxiliary levels cannot be assumed to preserve a
fixed finite set of possible visibility primes.

The attempt has therefore produced exact all-local-condition maps, an
actual counterexample to the naive degree/congruence bound, and a complete
description of why the fixed level and winding quotient miss the
remaining $389a1$ group. A proof of H389, or an explicit nonzero Hecke
annihilator eigenvalue in the general setting, is still needed. Even a
solution for this curve would leave the universal BSD rank and
leading-term comparisons outside this task.
