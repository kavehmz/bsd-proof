# Actual higher Heegner residue vectors and the surviving finite class

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded construction; all eight sections have independent
**PASS** [review](review-heegner-higher-residue.md). The coordinator also
checked the corrected proof and reconstructed the joint-image and cyclicity
arguments. The reviewed mathematical revision is
627ab2762db0c56c94ee8eac3cff963e2dfb21ed2b0e5c89419df89adfc900f6;
subsequent header and status changes are editorial.
Restart: [checkpoint](heegner-higher-residue-checkpoint.md).
The universal full BSD objective remains active. This note obtains
actual higher-class relations and a conditional finite Selmer control
statement. It does not prove rank-five vanishing.

## 1. Fixed coefficient, strict group, and signed convention

Keep the original O5 assumptions: E/Q is non-CM, p>=5 is good ordinary,
E[p] is irreducible, its analytic rank is odd and at least five,
and K has the stated odd fundamental discriminant D prime to Np,
all primes of Np split, and $L(E^D,1)\ne0$.
Fix two inert Heegner Kolyvagin primes $\ell,q$, put $m=\ell q$,
and set
$$
 k=M(m),\qquad R=\mathbb Z/p^k,\qquad V=E[p^k],\qquad
 U=\operatorname{Spec}\mathbb Z[1/(Np|D|m)] .
 \tag{1}
$$
S consists exactly of the complement of U and the real place.
All fresh primes v below are inert in K, avoid $6NpDm$,
and satisfy $a_v\equiv0$, $v\equiv-1\pmod{p^k}$.
There is **no full-image hypothesis**. Detection in this range
is the reviewed Theorem 6.3 of
[the signed Gysin construction](heegner-gysin-bridge.md),
whose [review](review-heegner-gysin.md) includes its image
and sign repairs.

Let
$$
 \kappa=\kappa_{m,\mathbb Q}^{\mathrm{raw}}
     \in\mathcal S:=\operatorname{Sel}_{p^k}(E/\mathbb Q)
                  _{\operatorname{loc}_\ell=
                    \operatorname{loc}_q=0}.
$$
Its K-restriction is the raw two-prime class. This strict
membership follows from the already proved one-prime vanishing.
No Sha quotient replaces $\mathcal S$.
Set
$$
 \mathcal D=H_c^2(U,V)/L_m,
$$
the reviewed perfect dual of $\mathcal S$.

We retain the signed convention without renaming it canonical:
the compact cone has differential
$D(a,b)=(da,\operatorname{res}a-db)$, the project's
$\partial^+\beta=(0,+\beta)$ is minus the canonical
triangle boundary, and its compact trace is positive on
that signed boundary. The map $G_v$ is minus the usual
positive-valuation Gysin map.
For $y:\mu_{p^k}\to V$ in
$W_v=H^0(\mathbb F_v,V(-1))$, define
$$
 e_{p^k}(y(\zeta),x)=\zeta^{\lambda_y(x)}.
$$
The reviewed formulas are
$$
 \mathscr P(z,G_v(y))
   =\frac{\lambda_y(z(F_v))}{p^k},\qquad
 \sum_{v\in T}G_v(\operatorname{res}^{\mathrm{tame}}_v b)
    =\partial^+_S(\operatorname{loc}_S b).
 \tag{2}
$$
The first uses rational arithmetic Frobenius and the
compact-first Weil order. The second uses the positive
Kummer-valuation residue and an actual class on $U\setminus T$.

Choose $\lambda_v:V_v^+\simeq R$ as in local reciprocity
and its unique Weil-dual $y_v\in W_v$. Write
$g_v=[G_v(y_v)]\in\mathcal D$ and
$$
 a_v(\kappa)=
 \lambda_v\bigl(\kappa_{m,K}^{\mathrm{raw}}(F_v^2)\bigr)
 =\psi_{v,k}(e_t\mathcal D_{v,m})\in R.
 \tag{3}
$$
To distinguish this test value from the Fourier coefficient,
we always retain its argument: $a_v(E)$ means the Fourier
coefficient when both occur in a formula.
The exact quadratic restriction factor is
$$
 \mathscr P(\kappa,g_v)=\frac{a_v(\kappa)}{2p^k}
            \quad\text{in }p^{-k}\mathbb Z/\mathbb Z.
 \tag{4}
$$
Thus $2g_v$, not $g_v$, pairs to the K-local toric value
divided by $p^k$. Division by 2 here is its inverse in R.

## 2. Actual even-index classes lie in the residue source

Let T be a finite set of fresh primes, and J an even-cardinality
subset of T. Put $n_J=m\prod_{v\in J}v$, so $M(n_J)=k$.
Choose the CM points, generators and class-group transversals
compatibly in $H_{m\prod T}$ and restrict them to its
subconductors. This makes all derived points below specified.

The raw class of index $n_J$ has conjugation sign
$(-1)^{2+|J|}=+1$. It therefore has the unique Q-descent
$$
 b_J=\tfrac12\operatorname{cor}_{K/\mathbb Q}
             \kappa_{n_J,K}^{\mathrm{raw}}
        \in H^1(U\setminus T,V).
 \tag{5}
$$
Let
$$
 A_S=
 \bigoplus_{u\in S_f\setminus\{\ell,q\}}E(\mathbb Q_u)/p^k
       \ \oplus H^1(\mathbb Q_\ell,V)
       \ \oplus H^1(\mathbb Q_q,V)
$$
with Kummer embeddings, and
$B_T=\{b:\operatorname{loc}_S b\in A_S\}$, exactly as
in the Gysin presentation.

**[NEW] Proposition 2.1.** Every b_J in (5) belongs to B_T.
Its tame residue at $v\in T\setminus J$ is zero.

*Proof.* Away from its conductor $n_J$ the classical
Heegner class has the finite point Kummer condition.
At the old conductor primes ell,q, A_S allows all
local cohomology. At every other prime of S it allows
the finite point group. Local corestriction carries
Kummer classes to point norms, including the two
terms at a split place; multiplication by the p-unit
$1/2$ preserves this condition. The odd-p real
condition is zero. This proves membership in B_T.
At $v\in T\setminus J$ the class is unramified,
so its positive tame residue is zero.
$\square$

In particular a four-prime class need not have zero
localization at ell or q. Its old-prime local
components are retained in the right side of (2);
they vanish in $\mathcal D$ only because the
defined subgroup $L_m$ quotients them out.

## 3. Exact residue vectors from the actual cofactors

Fix a lift of $\sigma_v$ from the local ring-class
generator to tame inertia and put
$$
 \zeta_v=\delta(v)(\sigma_v)\in\mu_{p^k}.
$$
It is primitive: the local ring-class extension
has tame ramification degree v+1, divisible by
$p^k$, and a generator has primitive image in
its p-primary quotient. The Kummer character of
a uniformizer has that primitive inertia value.
The unramified extension $K_{(v)}/\mathbb Q_v$
does not change this inertia or valuation.

Let $e_v^+=\lambda_v^{-1}(1)$ and
$e_v^-=y_v(\zeta_v)$, so
$e_{p^k}(e_v^-,e_v^+)=\zeta_v$.
Both are bases of their R-lines. Write
$\lambda_v^-:V_v^-\to R$ for coordinate in $e_v^-$.
For a local class b, the positive residue y satisfies
$$
 y(\zeta_v)=b(\sigma_v).
 \tag{6}
$$
There is no factor two in (6): inertia is unchanged
under the unramified quadratic restriction.

For $v\in J$, put $n=n_J/v$, an odd-index conductor.
Use its actual derived point $P_n=A_ny_n$ and the
compatible point $Y_{n,v}=\widetilde A_ny_{nv}$.
The coefficient remains k because n still contains m.
Define the integer point combination
$$
 B_{n,v}
   =\frac{v+1}{p^k}Y_{n,v}
      -\frac{a_v(E)}{p^k}P_n
                   \in E(H_{nv}).
 \tag{7}
$$
This is the same specified trace-zero cofactor as
in the preceding construction, now at the actual
higher conductor. Its norm to $H_n$ is zero.

Let
$$
 x_{n,v}=
 \kappa_{n,K}^{\mathrm{raw}}(F_v^2)\in V_v^-,
 \qquad
 h_{J,v}=\lambda_v^-(x_{n,v}).
 \tag{8}
$$
Finite evaluation is defined because v is fresh
for n. The minus eigenspace follows from the
raw odd-index conjugation sign.

**[NEW] Proposition 3.1 (full-p-power residue vector).**
The actual reduction of (7) is
$\overline B_{n,v}=x_{n,v}$, and
$$
 \operatorname{res}^{\mathrm{tame}}_v b_J
      =-h_{J,v}\,y_v\quad(v\in J).
 \tag{9}
$$
Consequently the exact compact relation is
$$
 -\sum_{v\in J}h_{J,v}G_v(y_v)
     =\partial^+_S(\operatorname{loc}_S b_J),
 \qquad
 \sum_{v\in J}h_{J,v}g_v=0\ \text{in }\mathcal D .
 \tag{10}
$$

*Proof.* The compatible trace gives
$N_vY_{n,v}=a_v(E)P_n$. Hence
$(\sigma_v-1)D_vY_{n,v}=p^kB_{n,v}$,
so B is the specified division correction
in the raw index-nv cocycle. Its specialization,
using the CM v-isogeny congruence and
$(a_v(E)-F_v)(F_v^2-1)=(v+1)F_v-a_v(E)$,
is
$$
 \overline B_{n,v}=-F_vx_{n,v}.
$$
Here $F_vx_{n,v}=-x_{n,v}$, so this is $x_{n,v}$.
Inertia acts trivially on the residue field of
a division point of E (good reduction at v);
the raw cocycle evaluated on $\sigma_v$
therefore specializes to
$-\overline B_{n,v}=-x_{n,v}$.
Equivalently this is Howard's finite-singular
relation with the odd-index sign -1.
The unique Q-descent has the same inertia
evaluation after restriction to K, giving (9)
via (6). Apply the signed relation (2) to
the actual b_J, then pass to its quotient
using Proposition 2.1.
$\square$

The normalization in this proof is precisely the
one reconstructed from
[Howard, arXiv:1202.6340v1, §1.7,
Proposition 1.7.4](https://arxiv.org/html/1202.6340#S1.SS7)
in the earlier reviewed note. It does not apply
a non-equivariant coefficient Frobenius globally.
The finite conjugation action is $F_v$, whereas
the transverse action is $v^{-1}F_v=-F_v$.

For the standard Kolyvagin system write
$u_r=(-1)^{r(r-1)/2}$ in the current $w(E)=-1$
case. If $r=2+|J|$ is even, then
$u_r=-u_{r-1}$. Its residue coordinates,
after stripping the declared tensor generators,
are $-u_rh_{J,v}=u_{r-1}h_{J,v}$.
For four primes $u_4=1$, while
$u_2=u_3=-1$; for six primes $u_6=-1$.
The odd-index tensor factors have nontrivial
conjugation action and are stripped only for
these coordinate formulas, not declared
trivial Q-coefficients.

Pair (10) with the base raw class kappa.
Its strict Selmer conditions annihilate
the right side. With (4), this is
$$
 -\sum_{v\in J}\frac{h_{J,v}a_v(\kappa)}{2p^k}=0,
 \quad\text{equivalently}\quad
 \sum_{v\in J}h_{J,v}a_v(\kappa)=0\quad\text{in }R.
 \tag{11}
$$
This displays separately the raw sign,
the signed Gysin convention and the
Q/K factor two.

## 4. Joint fresh-prime selection under irreducibility

The following elementary extension of the reviewed
detection argument allows an actual test of (10).
Its source cohomology input is
[Lawson-Wuthrich, arXiv:1505.02940v2,
Lemmas 3–4](https://arxiv.org/pdf/1505.02940v2),
read directly: over Q, residual irreducibility
and p>=5 give
$H^1(G_k,E[p^k])=0$ for every k.
Their proof uses a nontrivial residual
homothety and does not presume a central
scalar lift at every higher level.

Let $L_0=\mathbb Q(E[p^k])$.
Because K ramifies at a prime of D
where $L_0$ is unramified,
$K\cap L_0=\mathbb Q$.
Thus the coefficient image of $G_K$
is the same $G_k$ as over Q.

**[NEW] Lemma 4.1 (matrix algebra without full image).**
The R-algebra generated by this coefficient image
is all of $\operatorname{End}_R(V)$.

*Proof.* The image contains the matrix of a
complex conjugation, diagonalizable as
$\operatorname{diag}(1,-1)$ over R.
Its two idempotents $(1\pm\tau)/2$
are the diagonal matrix units.
Residual irreducibility gives an image
matrix with unit upper-right entry and
one with unit lower-left entry; otherwise
one of these two residual lines would be
invariant. Multiplication by the diagonal
units extracts those off-diagonal units,
and dividing their unit coefficients
gives the remaining matrix units.
$\square$

**[NEW] Proposition 4.2 (joint plus/minus detection).**
Suppose actual classes $c_1,\ldots,c_d\in H^1(K,V)$
have conjugation eigenvalues $\epsilon_j\in\{+1,-1\}$,
orders $p^{s_j}$, and span the internal direct sum
$\bigoplus_j Rc_j$. Then infinitely many fresh
Kolyvagin primes permit simultaneous K-local
Frobenius values, after conjugacy transport, prescribed
arbitrarily in
$\prod_j p^{k-s_j}V_\tau^{\epsilon_j}$.
In particular simultaneous zero and exact-order
conditions in these eigenspaces can be imposed.

*Proof.* Restriction from K to $KL_0$ is injective
on $H^1(K,V)$ by the quoted cohomology vanishing.
Let W be the joint image of the restricted
homomorphisms in $V^d$. It is R-linear and stable
under the diagonal $G_k$ action. Lemma 4.1 makes
it $V\otimes_R A$ for a submodule $A\subset R^d$:
the two diagonal units isolate the two rows and
the off-diagonal units identify their row modules.

The annihilator of A for the ordinary dot
product consists precisely of relations
$\sum_jr_jc_j=0$, by restriction injectivity.
The internal direct-sum hypothesis makes this
annihilator $\bigoplus_jp^{s_j}R$.
The finite perfect dot-product pairing into
$p^{-k}\mathbb Z/\mathbb Z$ gives the
double-annihilator identity, so
$A=\bigoplus_jp^{k-s_j}R$.
Thus
$$
 W=\prod_jp^{k-s_j}V.
 \tag{12}
$$

Each $c_j$ descends to a rational cocycle
with coefficient module V if $\epsilon_j=+1$
and $V\otimes\epsilon_K$ if $\epsilon_j=-1$.
Choose such cocycles. On $G_{KL_0}$ their
coefficients are all V and their joint
image is (12). Choose an actual complex
conjugation $\tau$ and $h\in G_{KL_0}$
with the desired translations $w_j$.
The cocycle value at tau is killed by
$1+\epsilon_j\tau$, because $\tau^2=1$.
Consequently
$$
 c_j((h\tau)^2)
       =(1+\epsilon_j\tau)w_j
       =2\operatorname{pr}_{\epsilon_j}w_j .
 \tag{13}
$$
The chosen rational cocycles and both coefficient
representations cut out a finite Galois extension
over Q. Chebotarev there supplies the indicated
Frobenius class and any further finite exclusions.
Its E-coefficient matrix is tau, so it has trace
zero and determinant -1 modulo $p^k$, and acts
nontrivially on K. Its squared translations
are (13); 2 is a unit. Conjugacy transports each
by an invertible coefficient action, preserving
the asserted zero and order conditions.
$\square$

No full residual or integral image is required.
This proof does not claim that all representations
in characteristic p are semisimple.

## 5. Four-prime classes eliminate zero tests but leave a detecting test

In this note the phrase “primitive case” means that the base
class has exact order $p^k$, equivalently admits a unit fresh-prime
evaluation by the proved detection theorem.

Take two fresh primes $v_i,v_j$. Abbreviate
$$
 h_{ij}=\lambda_{v_i}^-\!
    \left(\kappa_{m v_j,K}^{\mathrm{raw}}(F_{v_i}^2)\right),
 \qquad a_i=a_{v_i}(\kappa).
$$
Their actual four-prime class gives
$$
 h_{ij}g_{v_i}+h_{ji}g_{v_j}=0,\qquad
 h_{ij}a_i+h_{ji}a_j=0\quad\text{in }R.
 \tag{14}
$$
Both h-values are coordinates of the specified
higher cofactor reductions in (7).

**[NEW] Proposition 5.1 (a concrete elimination).**
Suppose $\kappa$ has exact order $p^k$.
Choose $v_i$ detecting that order, so $a_i$
is a unit. Then infinitely many choices of
$v_j$ satisfy
$$
 a_j=0,\quad h_{ji}\in R^\times,\quad h_{ij}=0,
 \qquad g_{v_j}=0\text{ in }\mathcal D,
 \quad\operatorname{ord}(g_{v_i})=p^k.
 \tag{15}
$$

*Proof.* Finite-singular compatibility at $v_i$
makes the actual three-prime class
$d_i=\kappa_{m v_i,K}^{\mathrm{raw}}$
have order $p^k$: its transverse evaluation
is the unit finite value of the base class.
Its conjugation sign is -1. The base
class and $d_i$ span an internal direct
sum because their signs differ.
Proposition 4.2 supplies $v_j$ with
base finite value zero and the finite
value of $d_i$ a unit. These are
$a_j=0$ and $h_{ji}\in R^\times$.
The second equation (14), with $a_i$
a unit, forces $h_{ij}=0$.
The first gives $g_{v_j}=0$.
Finally (4) pairs $g_{v_i}$ with kappa
to a value of order $p^k$, proving
its asserted order.
$\square$

Before passage to the strict quotient,
the same actual four-prime class gives
$$
 G_{v_j}(y_{v_j})
   =-h_{ji}^{-1}\partial^+_S
                    (\operatorname{loc}_S b_{\{i,j\}}).
 \tag{16}
$$
Thus the eliminated test is an explicit
old-S boundary in compact cohomology;
it is not asserted zero before that quotient.
The surviving $g_{v_i}$ evaluates to the
nonzero reduction of $B_{m,v_i}$.
This explains exactly which test the
four-prime operation removes.

Here is the nonprimitive version, with
no division by a nonunit.

**[NEW] Proposition 5.2.** If kappa has
order $p^s$, choose $v_i$ with $a_i$
of that exact order. Let $p^{s'}$ be
the order of $d_i$, so $s'\ge s$.
There are infinitely many fresh $v_j$
with
$$
 a_j=0,\qquad
 \operatorname{ord}(h_{ji})=p^{s'},\qquad
 h_{ij}\in p^sR .
 \tag{17}
$$
Their relation remains the full (14).

*Proof.* The local compatibility gives
the lower bound on $s'$. The opposite
signs again give the direct-sum
hypothesis in Proposition 4.2, proving
the first two choices. Since
$a_i=p^{k-s}$ times a unit, its
annihilator in R is exactly $p^sR$.
Equation (14) proves the last assertion.
$\square$

The remaining coefficient in (17) is
the actual reduction of
$B_{m v_j,v_i}$, constrained to that
annihilator ideal. It is not known to
be zero when $s<k$. Likewise
$h_{ji}$ need not be a unit.
The primitive manipulation cannot be
reused by silently dividing the
whole Heegner system by a p-power.

## 6. A finite Selmer control statement reconstructed from those classes

**[NEW] Theorem 6.1.** Under the hypotheses above,
if the raw two-prime class kappa has
order $p^k$, then
$$
 \mathcal S=R\kappa .
 \tag{18}
$$
This is a conditional finite Euler-system
upper-bound deduction, not a proof
that such a class exists at rank five.

*Proof.* Choose $v_i$ as in Proposition 5.1.
For any $z\in\mathcal S$, subtract the
unique scalar multiple of kappa whose
finite evaluation at $v_i$ agrees with z;
the scalar exists because $a_i$ is a
unit and the Q/K factor is the unit 2.
Call the difference $z'$. It is still
strict Selmer and has zero finite
evaluation at $v_i$.

Suppose $z'\ne0$, of order $p^t$.
Over K the three actual classes
$\kappa_K,z'_K,d_i$ span an internal
direct sum. Indeed $d_i$ has minus
sign and the first two have plus sign.
A relation between the first two,
evaluated at $v_i$, has zero coefficient
on kappa because its value is a unit;
the remaining relations are just the
annihilator of $z'$.

Proposition 4.2 therefore gives a fresh
$v_j$ where kappa has finite value
zero, $z'$ has finite value of exact
order $p^t$, and $d_i$ has unit
finite value. Apply the actual
four-prime relation as in Proposition
5.1. It forces $g_{v_j}=0$ in
$\mathcal D$. Perfect duality then
makes its pairing with every strict
Selmer class zero, in particular with
$z'$. But (2) and the unit factor two
give a nonzero pairing of order $p^t$
with $z'$, a contradiction. Thus
$z'=0$, proving (18).
$\square$

This proof uses actual four-prime
classes, their old-S local conditions,
and simultaneous arithmetic Frobenius
choices. It is not a matrix
countermodel. It shows that, under
the primitive assumption, the higher
relations identify the surviving
strict Selmer direction with the
base class itself. They do not
make that direction zero.

**[NEW] Proposition 6.2 (a surviving direction exists independently).**
The actual group $\mathcal S$ always
contains a free R-submodule of rank
at least one under the present O5
hypotheses.

*Proof.* The reviewed odd-rank theorem
gives $s_p(E)\ge3$. The finite Selmer
group identifies with
$\operatorname{Sel}_{p^\infty}(E/\mathbb Q)[p^k]$
because $E(\mathbb Q)[p^\infty]=0$;
the propagated finite local conditions
are the full point Kummer conditions.
Its divisible corank supplies an
actual free $R^3$ submodule.
At each old good prime ell,q,
$H_f^1(\mathbb Q_\ell,V)=
V/(F_\ell-1)V\simeq R$,
since the Frobenius eigenvalues are
1 and -1 modulo $p^k$.
Restrict the two localization maps
to that free $R^3$. Smith reduction
over R of its map to $R^2$ leaves
at least one zero source column,
whose free R summand is in the
kernel. That kernel lies in the
strict Selmer group.
$\square$

Consequently the full strict dual
is never zero in this setting.
Even the residues of **all** classes
in B_T cannot span all of
$\bigoplus W_v$ when T generates
that dual. Thus trying to prove
that the higher Heegner residue
vectors span every test would
prove a false statement about
the actual strict group.
This does not disprove O5:
the particular kappa can be
zero inside a nonzero group.

As a consistency consequence
in the primitive case,
$\operatorname{Sel}_{p^k}(E/\mathbb Q)
\simeq R^3$. Its order is at
most $p^{3k}$ by (18) and the
two old rank-one targets, and
at least $p^{3k}$ by the
divisible-corank lower bound;
the resulting surjection onto
$R^2$ splits as R-modules.
This is compatible with the
already known possibility
$s_p(E)=3$. It does not prove
Mordell-Weil rank three or
finiteness of a divisible
Sha contribution.

## 7. What the higher residue test leaves

For a generating T, form the
actual relation matrix with
column indexed by each even
J and entries $h_{J,v}$ on J,
zero elsewhere. Equations
(9)–(11) compute these entries
on specified points and show
that the vector of base
toric evaluations annihilates
every such column at the full
coefficient. No assumption
that these Heegner columns
generate all residues of B_T
has been made.

The concrete elimination in
§5 and the proof in §6 give
more than a new expression
of the old trace relation:
they show how actual
four-prime residues remove
zero-evaluation tests, and
conditionally identify the
remaining strict direction.
In the nonprimitive case
the explicit remaining
terms are (17). In the
primitive case the surviving
value is
$$
 a_i=-\lambda_{v_i}
       \operatorname{pr}_+
           \overline{B_{m,v_i}},
 \tag{19}
$$
a unit under that case's
assumption. No higher
residue relation annihilates
it in the foregoing argument.

All these deductions already
use only the odd-rank-three
inputs and their one-prime
vanishing. The additional
untwisted $L'''(E/K,1)=0$
has not supplied a new
relation or coefficient
identity. No height-sector
or old/new denominator
calculation was repeated
as a new result here.

**[GAP HR-TP5].** Supply a
rank-sensitive arithmetic
comparison that forces
the actual values (19),
including the nonprimitive
case, to vanish from the
additional untwisted
central derivatives.
It must distinguish the
specified Heegner class
from other classes in
the necessarily nonzero
strict Selmer group.
It cannot be replaced
by the fact that every
strict class annihilates
the existing residue
relations, or by a
claim that their entire
dual quotient is zero.

The primitive conditional
cyclicity and the exact
nonprimitive coefficients
are the finite arithmetic
control obtained by this
operation. The desired
cofactor reduction
vanishing and universal
BSD remain open.

## 8. Source and verification scope

The exact classical
Heegner points, their
full-coefficient cocycle
and finite-singular
relation were checked
in Howard §1.7 and
BCGS2312.09301v2 §1.1.2.
The repaired scalar
normalization is the
on-page proof already
reviewed in this project.
The Gysin presentation
and its signed trace
are used only after
their independent
review, including
the original
irreducible-image range.
Lawson-Wuthrich
1505.02940v2 Lemmas
3–4 were read directly
on PDF pp.3–4.

Only the two assigned
files were written.
No new agents, source
model changes, shared
synthesis edits or
old numerical reruns
were performed.
Every [NEW] deduction
in this note has now
received independent
PASS review, linked
in the header.
