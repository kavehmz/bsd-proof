# Projective monodromy, integral connections, and the degree-zero repair

Date: 2026-09-12. Agent /root/uniform_witness, GPT-6 Astra/xhigh.
The objective remains full BSD over Q. All [NEW] deductions below passed
[independent coordinator review](review-projective-monodromy.md).
No nonzero Sha class for 389a1 is asserted.

The stable twisted (n,1) bundle admits an actual projective
trivialization by multiplication by n, of degree n². Its projective
connection cannot extend over a good prime dividing n: its projective
Atiyah class has nonzero trace in that characteristic. This also happens
for the ordinary stable bundle with Brauer class zero. A degree-zero
Poincaré pushforward admits a different integral local construction of
connections; its finite-monodromy and arithmetic descent requirements
must then be checked separately.

## 1. Reviewed inputs and the ordinary control

Let E=389a1 and let its regular proper model be
$$\mathcal E:\ Y^2Z+YZ^2=X^3+X^2Z-2XZ^2.$$
The reviewed [model](weil-etale-lattice-attack.md) and
[K-theory proof](k-theory-lattice-attack.md) give
$$\operatorname{Br}(\mathcal E)=\operatorname{Sha}(E),
\qquad \pi_1^{\rm et}(\mathcal E)=1.$$
The only bad fiber is split irreducible I1 at389. The known zero
primary parts at2,3,5,389 imply that the period of every class is prime
to389. These are existing inputs; no old script has been rerun.

For a class $\beta$ of period n, the reviewed
[twisted construction](twisted-sheaf-lifting-attack.md) gives a stable
weight-one bundle V of rank n and descended determinant $\mathcal O_E(O)$
on a geometrically trivial $\mu_n$ Kummer gerbe. Its ordinary algebra
$A_\beta=\mathcal End(V)$ has degree n and Brauer class $\beta$.
Its zero-section fiber is framed as a matrix algebra.

The ordinary stable bundle $V_n^0=V_n(\mathcal O_E(O))$ exists for
every n by the previous induction. Put $A_n^0=\mathcal End(V_n^0)$.
This is the control: its Brauer class is zero for every n, whereas
its intrinsic projective monodromy below has order n². Here n denotes
the control's rank, not the period of its zero Brauer class.

## 2. Multiplication by n trivializes the actual algebra

**[NEW] Lemma2.1.** For a stable rank-n degree-one bundle W over an
algebraically closed characteristic-zero elliptic curve,
$$\mathcal End(W)\simeq
\bigoplus_{M\in\operatorname{Pic}^0(E)[n]}M. \tag{2.1}$$

*Proof.* Each $W\otimes M$ is stable with the same determinant, hence
isomorphic to W. Choose the resulting map $j_M:M\to\mathcal End(W)$.
The trace of $j_Mj_N$ is zero if $MN\ne\mathcal O$: it would be a
section of the nontrivial degree-zero line $(MN)^{-1}$. If $N=M^{-1}$,
the product is an invertible scalar, with nonzero trace n times that
scalar. Thus the trace pairing on the direct sum is fiberwise
nondegenerate. Its map to $\mathcal End(W)$ is an isomorphism because
both bundles have rank n². $\square$

This proof also works in characteristic prime to n, but will not be
used when the characteristic divides n. It agrees with Brion,
[*Homogeneous projective bundles over abelian varieties*,
arXiv:1104.0818v4](https://arxiv.org/html/1104.0818v4),
Proposition3.1(ii), whose §3 likewise assumes characteristic prime to n.

**[NEW] Proposition2.2.** Over Q there is an algebra isomorphism
$$[n]^*A_\beta\simeq M_n(\mathcal O_E). \tag{2.2}$$

*Proof.* Every line in (2.1) becomes trivial under [n]. Hence
geometrically $[n]^*A_\beta$ is a trivial vector bundle. Put
$B=H^0(E,[n]^*A_\beta)$. Flat base change shows that evaluation
$$\mathcal O_E\otimes_{\mathbb Q}B\longrightarrow[n]^*A_\beta$$
is an isomorphism: after algebraic closure both sides are constant
of rank n². It is an algebra isomorphism. Evaluation at O identifies
B with the framed algebra $A_\beta|_O=M_n(\mathbb Q)$. $\square$

Thus [n] is an actual finite étale projective trivialization of degree
n². For the degree theorem see
[Stacks, Lemma39.9.8](https://stacks.math.columbia.edu/tag/0BFG).
Brauer splitting alone also follows from $[n]^*\beta=n\beta=0$
under normalized Hochschild–Serre, but would not establish (2.2).

Deck transformations of [n] now give
$$\rho_\beta:E[n]\longrightarrow\mathrm{PGL}_n \tag{2.3}$$
over Q. Their coefficients in the trivialization are constant in the
E-coordinate, since every morphism from a proper connected E to the
affine group PGL is constant. Geometrically the adjoint representation
contains all n² characters of E[n], by (2.1). Hence (2.3) is faithful.

## 3. Heisenberg matrices and the generic projective connection

The inverse image of (2.3) in $\mathrm{GL}_n$ is a theta extension
$$1\to\mathbb G_m\to\widetilde H_\beta\to E[n]\to1. \tag{3.1}$$
Its commutator pairing is nondegenerate. Indeed a finite central lift
acts semisimply in characteristic zero; its invariant endomorphisms
are scalars, so its representation is irreducible. A commuting lift
is then scalar, and faithfulness in PGL kills the pairing's radical.

After choosing a symplectic basis and a primitive n-th root $\zeta$,
the standard Heisenberg matrices on basis $e_j$, $j\in\mathbb Z/n$, are
$$Ue_j=\zeta^j e_j,\quad Te_j=e_{j+1},\quad UT=\zeta TU. \tag{3.2}$$
Their classes commute and have projective image $(\mathbb Z/n)^2$.
This is Brion §2.3's Heisenberg construction, used only in characteristic
zero. The same geometric representation occurs for the ordinary control
$A_n^0$; it does not detect the Brauer class.

The ordinary differential on the constant algebra in (2.2) descends
along finite étale [n], since its deck matrices are constant.
It gives an algebra connection on $A_\beta$, equivalently a projective
connection. It is integrable because $\Omega_E^2=0$. Its complex
projective monodromy is finite of order n². It is the unique projective
connection: (2.1) gives
$$H^0(E,(A_\beta/\mathcal O_E)\otimes\Omega_E^1)=0,$$
and this is the space of differences of two projective connections.

The smallest connected horizontal trivializing cover has degree n²,
by faithfulness on $\pi_1(E_{\mathbb C})/n\pi_1(E_{\mathbb C})$.
This is not the minimal Brauer splitting degree: the previous
degree-n torsor point supplies that, and the generic algebra index is n.

## 4. The actual arithmetic form torsor

Over an algebraic closure $A_\beta\simeq A_n^0$, and
$$\operatorname{Aut}_E(A_n^0)\simeq\operatorname{Pic}^0(E)[n]. \tag{4.1}$$
A projective automorphism lifts to an isomorphism
$V_n^0\simeq V_n^0\otimes M$, modulo scalar; determinant gives $M^n=1$,
and stability gives one projective automorphism per M. This identifies
the group law and Galois action. The group is finite étale in
characteristic zero; see also Brion Proposition3.1(iii).

Choose a geometric algebra isomorphism $\phi:A_n^0\to A_\beta$.
The cocycle $\phi^{-1}\sigma\phi$ gives a finite form torsor
$$\eta_\beta\in H^1(\mathbb Q,\operatorname{Pic}^0(E)[n]). \tag{4.2}$$
The line bundles of lifts of these projective differences are its
line-tensor cocycle. Their image in $H^1(\mathbb Q,\operatorname{Pic}^0(E))$
is the normalized Hochschild–Serre class of $\beta$, with sign fixed
by the lift convention. The principal polarization identifies this
with the ordinary E[n] Kummer sequence.

Consequently the local Selmer condition is precisely
$$\eta_{\beta,v}\in E(\mathbb Q_v)/nE(\mathbb Q_v)
\subset H^1(\mathbb Q_v,E[n]). \tag{4.3}$$
It is not the assertion $\eta_{\beta,v}=0$. A local neutralization
can produce a nontrivial division-point torsor of a local point.
Globally $\beta=0$ means that (4.2) is a global Kummer class, not
necessarily the zero finite torsor. Changing the ordinary control's
determinant changes (4.2) by a global Kummer class.

## 5. An integral projective model away from n and389

Put $S=\operatorname{Spec}\mathbb Z[1/389]$ and
$U=\operatorname{Spec}\mathbb Z[1/(389n)]$.
The restriction $\mathcal E_S$ is an abelian scheme.

The ordinary $V_n^0$ extends on $\mathcal E_S$ with stable geometric
fibers. Start with $\mathcal O(O)$ and take successive generator
extensions by $\mathcal O$. The characteristic-free degree-one induction
gives fiberwise stability, $h^0=1$, $h^1=0$, and a one-dimensional Ext1.
Relative Serre duality, using the invariant Néron differential, and
cohomology/base change make the relative Ext1 an invertible module on S.
This module is free since S is an affine principal ideal scheme.
The generator stays nonzero on every fiber. The local-to-global
spectral sequence has no extra obstruction because S is affine.

Over U the projective automorphism group of this model is $\mathcal E_U[n]$.
The universal normalized Poincaré line supplies its n-torsion twists;
the relative Hom is a line and evaluation is a fiberwise isomorphism.
Taking endomorphisms cancels this line. Thus (4.1) extends as an
isomorphism of finite étale groups.

At every prime of U, (4.3) is unramified: a local point extends by
properness, and its inverse image under étale [n] is integral finite
étale. Hence the finite form torsor extends over U. Twisting the
ordinary algebra by it constructs an algebra $\mathcal A_{\beta,U}$
on $\mathcal E_U$ with generic fiber $A_\beta$.

Furthermore
$$[n]^*\mathcal A_{\beta,U}\simeq M_n(\mathcal O_{\mathcal E_U}). \tag{5.1}$$
Each geometric fiber is constant by Lemma2.1. Constancy of h0 and
base change identify the algebra with the pullback of its zero-section
algebra. That algebra is generically split, hence split over regular U;
all finite projective modules over $\mathbb Z[1/(389n)]$ are free.
This proves (5.1). Finite étale descent therefore extends the projective
connection over this explicit integral model, without discarding
additional unspecified primes.

On the larger good model $\mathcal E_S$, multiplication by n remains
finite locally free of degree n². The fieldwise multiplication theorem,
properness, and the Cohen–Macaulay source/regular target give this
abelian-scheme assertion. Its differential is explicitly
$$[n]^*\omega=n\omega,\qquad
\Omega^1_{\mathcal E_S/\mathcal E_S,\,[n]}
 \simeq(\mathcal O_{\mathcal E_S}/n)\omega. \tag{5.2}$$
Thus it is not étale at a good prime dividing n. Pullback of the
Brauer class is nevertheless zero by generic vanishing and regular
Brauer injectivity. This is an actual finite-flat Brauer splitting
cover on the good model, with degree n².

## 6. A projective Atiyah obstruction without a stability assumption

**[NEW] Proposition6.1.** Let X be a smooth projective geometrically
connected curve over an algebraically closed field of characteristic
p>0. A rank-n degree-d vector bundle W with p|n and p∤d has no
algebraic projective connection.

*Proof.* In local frames, the Atiyah cocycle is $g_{ij}^{-1}dg_{ij}$
(up to the choice of frame convention). Its image in
$$H^1(X,(\mathcal End(W)/\mathcal O_X)\otimes\Omega_X^1)$$
is the obstruction to a projective connection: local connection matrices
glue modulo scalars exactly when this class vanishes.

Because n=0 in the field, trace kills scalar matrices and descends
to $\mathcal End(W)/\mathcal O_X$. The projective obstruction therefore
maps to $d\log\det(g_{ij})$, the Hodge Chern class of $\det W$.
Its Serre trace is d: a rational section of the determinant with
divisor $\sum m_xx$ computes this trace by residues of $m_xdt_x/t_x$.
Since d≠0 in the field, the obstruction is nonzero. $\square$

The trace–determinant identity is also proved in Kuhn,
[*The Atiyah class on algebraic stacks*](https://doi.org/10.1017/fms.2024.109),
Example4.10, without a characteristic restriction. The proof here
uses its transition-matrix identity and an explicit residue calculation.

**[NEW] Corollary6.2.** At a good prime p|n, no degree-n Azumaya
extension of the generic algebra $A_\beta$ to $\mathcal E_{\mathbb Z_p}$
has a regular projective connection.

*Proof.* Its Brauer class is zero by local Selmer triviality and
regular generic injectivity. It is therefore $\mathcal End(W)$
for a rank-n vector bundle W on that model. A degree-zero neutralization
of the original Kummer gerbe makes generic V an ordinary degree-one
bundle. Equal projectivizations differ by a line bundle, so
$\deg W_{\mathbb Q_p}\equiv1\pmod n$. Degree specializes in the
proper flat family. The special fiber contradicts Proposition6.1.
$\square$

This excludes unstable extensions too, and holds for the ordinary
control $A_n^0$ with Brauer class zero. It is an intrinsic rank-degree
obstruction, not a bound on possible Sha periods. Finite-flat descent
in (5.2) cannot be substituted for étale descent of the differential.
An integral crystalline object inducing such a regular projective
connection is likewise excluded; no assertion about isocrystals
after inverting p or logarithmic connections is made.

## 7. The separate ramification at389

Here (n,389)=1 by the reviewed primary result. The
[exceptional-prime proof](exceptional-prime-finiteness.md) supplies
Tate uniformization
$$E(\overline{\mathbb Q}_{389})
 =\overline{\mathbb Q}_{389}^{\,*}/q_T^{\mathbb Z},
\qquad v(q_T)=1.$$
See also Silverman,
[*The Arithmetic of Elliptic Curves*, AppendixC, Theorem14.1](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf).

An n-torsion basis is represented by $\zeta_n,q_T^{1/n}$.
The polynomial $T^n-q_T$ is Eisenstein. Its root has ramification
index n, tame since n is prime to389. Over the maximal unramified
extension, inertia acts on E[n] by the full transvection
$$\begin{pmatrix}1&1\\0&1\end{pmatrix}\pmod n. \tag{7.1}$$
Thus E[n] has no finite étale extension over $\mathbb Z_{389}$.
A finite-flat group of invertible order n² there would be étale,
so cannot extend it either.

On the smooth part of the I1 fiber, multiplication is $z\mapsto z^n$
on $\mathbb G_m$, of degree n, whereas generic degree is n². Hence [n]
is not a finite-flat self-map of the same proper I1 model.

One can still extend the generic cover by normalization: normalize
$\mathcal E$ in the function-field extension defined by [n].
Excellence makes this finite; its normal two-dimensional local rings
are Cohen–Macaulay, so it is flat over the regular target, of degree n².
Resolution gives a regular proper generically finite cover
$\mathcal Y_n\to\mathcal E$ with the same generic degree.
The pulled-back Brauer class is generically zero and therefore zero
on this regular resolution. No generic Brauer injectivity is assumed
for the unresolved singular normalization.

Neither this cover nor (5.2) is étale on the full model. Its trivial
étale fundamental group consequently does not trivialize these
constructed objects. The same ramification occurs for the ordinary
control and cannot distinguish its zero Brauer class from $\beta$.

## 8. The degree-zero Poincaré repair is locally integral

Let C be the locally soluble genus-one torsor corresponding to $\beta$
with the Picard-gerbe convention of the previous note. Let
$D=\operatorname{Spec}L\subset C$ be its constructed degree-n point.
The universal Poincaré pushforward gives a rank-n degree-zero twisted
bundle W and an ordinary Azumaya algebra $A_W=\mathcal End(W)$.

**[NEW] Proposition8.1 (finite-flat local connection).** At every good
prime p, including p|n, there is an integral local model of $A_W$
on $\mathcal E_{\mathbb Z_p}$ equipped with a regular algebra connection.
No division by n or order of a Galois group is used.

*Proof.* Put R=$\mathbb Z_p$, K=$\mathbb Q_p$. Choose a local point
$c_0\in C(K)$ and use it to identify $C_K$ with $E_K$. Let A be the
integral closure of R in the finite étale K-algebra $L\otimes_{\mathbb Q}K$.
It is a finite free R-algebra of rank n, possibly ramified and possibly
a product of discrete valuation rings. Properness of the abelian
scheme extends the difference point $D-c_0$ to $a\in\mathcal E(A)$.
Its normalized Poincaré line $\mathscr L_a$ on $\mathcal E_A$ has
relative degree zero.

Here trace-zero really does suffice because this is a *line bundle*,
before any pushforward. Relative duality gives
$$H^1(\mathcal E_A,\Omega^1_{\mathcal E_A/A})\simeq A,$$
and the trace of its relative Atiyah class is its relative degree,
zero. Equivalently the class is generically zero by the degree-zero
formula, and the displayed A-module is torsion-free over R.
Thus the entire line-bundle Atiyah class vanishes integrally.
Choose a relative connection
$$\nabla:\mathscr L_a\longrightarrow
 \mathscr L_a\otimes\Omega^1_{\mathcal E_A/A}.$$
Connections form a torsor under
$H^0(\mathcal E_A,\Omega^1_{\mathcal E_A/A})=A\omega$.

Let $q:\mathcal E_A\to\mathcal E_R$ be the finite-flat projection.
Smooth base change identifies $\Omega^1_{\mathcal E_A/A}$ with
$q^*\Omega^1_{\mathcal E_R/R}$. The projection formula therefore
pushes the connection to
$$q_*\mathscr L_a\longrightarrow
 (q_*\mathscr L_a)\otimes\Omega^1_{\mathcal E_R/R}. \tag{8.1}$$
For $f\in\mathcal O_{\mathcal E_R}$ it satisfies the Leibniz rule
because the original connection does. Its rank is n, and its curvature
is zero since the relative curve has no two-forms. Its endomorphism
connection is an algebra connection.

The chosen $c_0$ neutralizes the Picard gerbe. Under that neutralization,
the generic fiber of $q_*\mathscr L_a$ is exactly the original
Poincaré pushforward W. Hence its endomorphism algebra is the required
local model. $\square$

This uses relative connections in the E-direction. It does not treat
a ramified A/R as an étale extension, or identify
$\Omega_{\mathcal E_A/R}$ with $\Omega_{\mathcal E_A/A}$.
No averaging across conjugate points is involved.

Over Q an algebra connection on $A_W$ can also be constructed:
over a finite Galois field splitting D and the gerbe, W is a sum
of degree-zero lines, each of which has a connection. The resulting
endomorphism connection can be averaged over that finite Galois group.
The space of algebra connections is affine and the Leibniz identities
are affine-linear; curvature vanishes on a curve. This gives a
Q-connection, but its average can divide the group order. Proposition8.1
constructs integral local connections separately; it does not claim
that this particular averaged connection is integral.

There is a convenient moduli interpretation. The universal vectorial
extension
$$0\to\omega_E\to E^\natural\to E\to0 \tag{8.2}$$
parametrizes rigidified degree-zero lines with relative connection.
The fiber above a is a vector-group torsor over the affine base
Spec A, hence has an integral point. For the abelian-scheme interpretation
see Mazur–Messing, *Universal Extensions and One Dimensional Crystalline
Cohomology*, ChapterI §4; a complete curve-model formulation is
[Cais, arXiv:0909.1849v1, Theorem1.2](https://arxiv.org/html/0909.1849v1).
In the good-reduction setting used in Proposition8.1 the model is
smooth and regular with geometrically reduced fiber, so that theorem
identifies the connections with ordinary relative connections.

## 9. Finite monodromy: a new construction and its exact denominator

### 9.1. Arbitrary degree-zero pushforwards need not have finite monodromy

Geometrically the bundle from D is a sum of Poincaré lines indexed
by its n points. Its endomorphism lines correspond to the differences
$c_i-c_j$. If any such difference is non-torsion, no projective
connection on $A_W$ can have finite monodromy.

Indeed finite projective monodromy would give a finite étale cover
trivializing the projective bundle. Over an algebraic closure such
a connected cover of an elliptic curve is an isogeny after choosing
origins. Pullback of the endomorphism decomposition would be a sum
of trivial lines; hence every $L_{c_i-c_j}$ would be killed by that
isogeny. Its kernel on Pic0 is finite, forcing every difference to
be torsion. This proves the asserted necessary condition without
making any claim that a particular nonzero $\beta$ exists.

Thus the regular connections in §8 do not automatically have finite
monodromy. The trivial étale fundamental group of the arithmetic
model cannot be applied to an arbitrary regular algebraic connection.

### 9.2. A finite-monodromy degree-zero variant of rank n²

There is an actual way to force torsion differences. The rational
degree-n divisor D defines the n-covering
$$f_D:C\longrightarrow E,\qquad
 c\longmapsto[\mathcal O_C(nc-D)]. \tag{9.1}$$
After choosing an origin geometrically it is multiplication by n
followed by a translation. Thus it is finite étale of degree n².
The fiber
$$T=f_D^{-1}(O) \tag{9.2}$$
is a finite étale E[n]-torsor over Q. It need not be a single closed
point or have a rational point. Its geometric points have all their
differences in E[n].

Push the universal Poincaré line from this finite scheme as in the
previous construction. It gives a rank-n² degree-zero twisted bundle
$W_T$ for the same Brauer class $\beta$.
Geometrically it is, up to a common degree-zero line, the sum of all
n² torsion Poincaré lines. Consequently
$$[n]^*\mathcal End(W_T)\simeq
 M_{n^2}(\mathcal O_E), \tag{9.3}$$
by the same global-sections/evaluation proof as Proposition2.2.
This produces a finite-monodromy projective connection on a degree-zero
Azumaya representative. The generic cover still has degree n²;
the rank of the representative has increased to n².

Its geometric projective representation is a sum of characters and
has zero commutator. Arithmetic splitting does not follow. Here is
its exact descent term.

Let H=E[n] be the deck group of [n], so its character group is the
n-torsion Picard group. The inverse image of its projective
representation in $\mathrm{GL}_{n^2}$ is a commutative extension
$$1\to\mathbb G_m\to G_T\to H\to1. \tag{9.4}$$
It is commutative because it is geometrically diagonal. The sheaf
of characters of $G_T$ restricting to weight one on its central
$\mathbb G_m$ is an $H^D$-torsor, and it is precisely the torsor T
under the Poincaré/Weil-pairing identification (or its inverse if
the opposite Picard sign convention is used).

To verify this last assertion, choose $t_0\in T(\overline{\mathbb Q})$.
The geometric weights can then be labeled by
$t_0+H^D$. If $\sigma t_0=t_0+\tau_\sigma$, the Galois action on
these labels is
$$h\longmapsto\sigma h+\tau_\sigma.$$
These are exactly the differences of weight-one characters in (9.4).
Thus its character torsor has the cocycle of T. Equivalently its
character sheaf is an extension
$$0\to H^D\to X^*(G_T)\to\mathbb Z\to0,$$
whose fiber over1 is T. A weight-one rational character is a
splitting of (9.4), and exists exactly when $T(\mathbb Q)$ is nonempty.

Replacing the fiber (9.2) by $f_D^{-1}(P)$ for $P\in E(\mathbb Q)$
changes its class by the global Kummer class of P. Local solubility
provides such adjustments at every completion; it does not supply
a single global P with a rational point in the adjusted fiber.
This is the arithmetic form torsor of §4 after the intrinsic
Heisenberg commutator has been removed.

### 9.3. The integral torsion-lift calculation

The finite connection on the torsion Poincaré lines in (9.3) carries
a further integral condition. Let A be a finite product of complete
discrete valuation rings over $\mathbb Z_p$ with good reduction,
and let $t\in E[n](A)$.

Choose an integral lift $\widetilde t\in E^\natural(A)$ using (8.2).
Then $n\widetilde t=b\in\omega_E(A)$. Over the fraction algebra,
the unique n-torsion lift is
$$\widetilde t_{\rm tor}=\widetilde t-b/n. \tag{9.5}$$
It extends integrally if and only if
$$[b]=0\quad\text{in }\omega_E(A)/n\omega_E(A). \tag{9.6}$$
This residue class is independent of the initial lift: adding a
changes b by na. These statements follow directly by multiplication
by n in the vector extension, where the vector part has no n-torsion.

There is an equivalent connection calculation. Let $\mathscr L_t$
be the normalized torsion line with a chosen integral trivialization
$\mathscr L_t^{\otimes n}\simeq\mathcal O$, and choose any integral
connection $\nabla_0$. Its n-th tensor power is $d+b$ on the trivial
line, for an invariant differential b. The unique connection making
that trivialization horizontal is
$$\nabla_{\rm tor}=\nabla_0-b/n. \tag{9.7}$$
Its integrality is exactly (9.6). This is the finite-order connection
which is trivialized by the corresponding torsion cover.

Thus the degree-zero repair does remove the rank-degree Atiyah
obstruction and really constructs local integral connections.
It does not prove that the finite-order choices required for
finite monodromy lie in those integral lattices. No nonzero value
of (9.6) for an unspecified Sha class is asserted; the formula gives
the exact additional condition that must be checked or constructed.

For projective rather than line connections, common scalar changes
are allowed. Accordingly the required torsion-lift conditions concern
the differences of the point lifts, with their additive compatibility,
not a separately fixed absolute lift of every summand. Merely checking
the total trace of the pushforward does not verify these conditions.
Nor do pointwise integral checks over a ramified Galois splitting field
alone prove integral descent: the isomorphisms over the full tensor
product $A\otimes_R A$, including its infinitesimal structure, and
their cocycle condition must be retained. A regular connection is
also less data than a crystalline stratification or an everywhere
étale local system.

## 10. What is retained at389 and the exact remaining target

The local good-reduction construction of §8 is not silently extended
over the node at389. After a field extension of ramification e,
the regular Tate model has fiber I_e and component group
$\mathbb Z/e$. A Tate point represented by u has component
$$v_L(u)\pmod e,\qquad v_L(q_T)=e. \tag{10.1}$$
The line/connection comparison with the identity component requires
this component term to be removed. Multiplication by e removes it,
but e can depend on the chosen splitting field. It is not a fixed
bound supplied by the original I1 model.

Cais Theorem1.2 applies to the resolved regular semistable model:
its closed fiber is geometrically reduced. Its Picard group with
connection requires degree zero on every geometric component and
uses the relative dualizing sheaf. At a node this is not a claim
about an ordinary smooth-family differential; on the normalization
the dualizing differential has the familiar opposite logarithmic
residues at the two branches. We therefore retain both the component
condition (10.1) and this differential convention. The theorem assumes
no finite Sha group.

The attempt has now produced:

- a finite projective trivialization by [n] and a projective connection
  for the stable (n,1) representative, with explicit failure of regular
  integral extension at good primes dividing n;
- an actual integral local connection for the rank-n degree-zero
  Poincaré representative, even over ramified splitting algebras;
- a rank-n² degree-zero representative with finite projective monodromy,
  whose commutator is zero but whose rational weight-one character
  remains the specific Selmer torsor T;
- exact integral torsion-connection conditions (9.6), and the Tate
  component term at389.

**[GAP PM-389]** Construct, uniformly for every $\beta$, either a
global Kummer adjustment making the character torsor in (9.4) have
a rational point, or splitting objects whose degrees are bounded by
one integer independent of the period. A finite-monodromy approach
must additionally construct compatible integral torsion differences
satisfying (9.6) and the component requirements at389, then prove the
actual comparison to an everywhere étale splitting object before
using $\pi_1^{\rm et}(\mathcal E)=1$.

The local integral connections alone do not supply that comparison.
The explicit finite covers retain degree n² and the character torsor
retains the original global Kummer problem. No rank bound, uniform
degree bound, or full BSD proof/disproof is obtained.
