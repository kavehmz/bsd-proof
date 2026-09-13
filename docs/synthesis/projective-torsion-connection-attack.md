# Torsion connections, Cartier duality, and integral character blocks

Date: 2026-09-12. Agent /root/uniform_witness, GPT-6 Astra/xhigh.
The objective remains full BSD over Q. All [NEW] deductions below
have passed [independent coordinator review](review-projective-torsion-connection.md).
The review records the mathematical revision; subsequent review-link
and checkpoint edits are editorial. No nonzero Sha class of389a1 is asserted.

The exact torsion-connection obstruction from the previous construction
is a finite-flat Hodge–Tate differential. It can be computed on ordinary
p-power torsion and, over an unramified base, on supersingular torsion.
The full torsion-character bundle necessarily contains an obstructed
horizontal line. Saturation shows that changing its integral algebra
model cannot hide that obstruction. A smaller ordinary character block
does admit a genuine integral finite-monodromy construction locally;
its global descent requires additional arithmetic information.

## 1. The obstruction and the Cartier-dual character

Let R be the ring of integers of a finite extension of Q_p, K its
fraction field, and $\mathscr E/R$ an elliptic scheme with good reduction.
Write $\widehat{\mathscr E}=\operatorname{Pic}^0(\mathscr E/R)$,
$\omega_{\mathscr E}=e^*\Omega^1_{\mathscr E/R}$, and
$G_n=\mathscr E[n]$, where n>0. Fix the normalized Poincaré line.

For $t\in\widehat{\mathscr E}[n](R)$ let $\mathscr L_t$ be its rigidified
degree-zero line. It has compatible canonical trivializations
$\mathscr L_t^{\otimes n}\simeq\mathcal O$ and $[n]^*\mathscr L_t\simeq\mathcal O$.
The previous [connection construction](projective-monodromy-attack.md#93-the-integral-torsion-lift-calculation)
proves that an integral relative connection $\nabla_0$ exists. Write
its n-th tensor power, in that trivialization, as $d+b$, with
$b\in\omega_{\mathscr E}(R)$, and define
$$o_n(t)=[b]\in\omega_{\mathscr E}(R)/n\omega_{\mathscr E}(R). \tag{1.1}$$
It is independent of $\nabla_0$, since adding a differential changes
b by n times that differential. Its vanishing is equivalent to the
integrality of the unique generic connection for which the n-th-power
trivialization is horizontal.

Put $q=[n]$. Define the character $\chi_t:G_n\to\mu_n$ by the canonical
frame tau of $q^*\mathscr L_t$:
$$\tau(x+g)=\chi_t(g)\tau(x). \tag{1.2}$$
This fixes the sign convention for the Cartier identification
$\widehat{\mathscr E}[n]\simeq G_n^D$. Replacing all characters by their
inverses changes the signs below and none of the vanishing criteria.

The invariant cotangent sequence of q gives
$$\omega_{G_n}\simeq\omega_{\mathscr E}/n\omega_{\mathscr E}. \tag{1.3}$$
The map
$$\operatorname{HT}_n(t):=\chi_t^*(dz/z)\in\omega_{G_n}(R) \tag{1.4}$$
is the finite-flat Hodge–Tate map, with domain the Cartier dual.
The definition by pullback of dz/z is in Fargues,
[*La filtration canonique des points de torsion des groupes p-divisibles*,
Ann.ENS44(2011),905–961, §2](https://www.numdam.org/item/10.24033/asens.2157.pdf),
DOI10.24033/asens.2157, printedp912.

**[NEW] Proposition1.1 (exact comparison).** With (1.2),
$$o_n(t)=\operatorname{HT}_n(t). \tag{1.5}$$

*Proof.* In the frame tau write $q^*\nabla_0=d+a$, where a is a global
invariant differential on the source elliptic scheme. The n-th tensor
power is $d+na$. On the other hand it is $q^*(d+b)=d+nb$, because
$q^*\omega=n\omega$. R has no n-torsion, so a=b under the invariant
differential identification between source and target.

On $G_n\times_R\mathscr E$, translation pulls an invariant differential
back to the sum of its two pullbacks. Comparing the connection forms
in (1.2) therefore gives
$$\operatorname{pr}_{G_n}^*(b|_{G_n})=d\log\chi_t.$$
Restrict at the identity of the elliptic factor and use (1.3).
This proves (1.5). The calculation takes place on the whole finite-flat
group scheme, including its infinitesimal fibers, rather than just on
its generic points. $\square$

In particular finite-flat torsor descent gives the exact obstruction
to descending the constant differential on the trivializing cover.
It cannot be replaced by pointwise Galois invariance over a ramified
splitting field.

For $n=mp^r$ with (m,p)=1, the prime-to-p part has zero invariant
differentials. If t has p-power order, the compatible tensor
trivializations give $o_n(t)=m\,o_{p^r}(t)$ under the identification
of the quotient ideals. Multiplication by m is a unit, so it does not
change any of the local vanishing criteria.

## 2. Exact ordinary computation without splitting the whole extension

Assume ordinary reduction and write
$$0\to G_r^0\to G_r=\mathscr E[p^r]\to G_r^{\rm et}\to0. \tag{2.1}$$
Here $G_r^0$ is of multiplicative type and order p^r, and the quotient
is finite étale of order p^r. The extension (2.1) need not split.
The ordinary connected–étale structure is recalled in Fargues §1.1;
his §2.5, Lemma4, also gives the level-one kernel statement.

After a finite unramified extension, fix a group-scheme isomorphism
$$\iota:\mu_{p^r}\overset\sim\longrightarrow G_r^0.$$
Restriction identifies $\omega_{G_r}$ with $\omega_{G_r^0}$ because
the quotient is étale. For a Néron generator omega, define the exact
unit
$$\iota^*\omega=u\,dz/z,\qquad
u\in(R/p^rR)^\times. \tag{2.2}$$
This unit is the differential of the chosen multiplicative
trivialization, not an unnamed normalization scalar.

Dualizing (2.1) gives
$$0\to(G_r^{\rm et})^D\to G_r^D\to(G_r^0)^D\simeq\mathbb Z/p^r\to0.$$
For $t\in G_r^D(R')$, over any finite extension where it is defined,
let $a(t)\in\mathbb Z/p^r$ be its image in this quotient.

**[NEW] Proposition2.1.** One has the exact formula
$$o_{p^r}(t)=a(t)u^{-1}\omega\pmod{p^r\omega}. \tag{2.3}$$
Consequently its kernel on torsion points is the connected subgroup
of the dual. A point mapping to an étale generator has a unit obstruction.

*Proof.* The character of t restricted to $G_r^0$ is $z\mapsto z^{a(t)}$.
Its differential is $a(t)dz/z$. Combine this with (1.5) and (2.2).
The injection $\mathbb Z/p^r\to R'/p^rR'$ shows that the value is zero
exactly when a(t)=0. The kernel group is $(G_r^{\rm et})^D=(G_r^D)^0$.
$\square$

The computation does not choose a lift of the étale quotient back
into $G_r^D$. Over a sufficiently large finite field containing the
torsion there are points over every quotient element, by properness
of the finite-flat group. Thus a(t)=1 actually occurs. The resulting
obstruction remains nonzero after further ramified base change.

Connected dual torsion has zero obstruction because its characters
factor through the étale group $G_r^{\rm et}$. This is a scheme-level
factorization, not a consequence of all its special-fiber points
coalescing. It will supply the positive construction in §6.

## 3. Supersingular computation over an unramified base

Now assume R is unramified over Z_p and the special fiber is supersingular.
Normalize v(p)=1. All assertions concern good reduction; no statement
about arbitrary ramified deformations is substituted here.

For an invariant differential torsion module $R'/(\gamma)$, the
valuation of a nonzero class means v(y) for a representative with
v(y)<v(gamma). It is well-defined: changing the lift adds something
of larger valuation. Changing an integral generator multiplies by
a unit and preserves that valuation. In particular values in
$\omega_{\mathscr E}/p^r$ have this meaning whenever their valuation
is less than r.

### 3.1. The order-p calculation

Use the canonical principal polarizations to identify the elliptic
curves with their duals. Let t be a nonzero p-torsion point and H
the finite-flat closure of the cyclic subgroup it generates after
a finite extension R' where its points are defined. Let
$$q_H:\mathscr E\to\mathscr B=\mathscr E/H$$
be the quotient isogeny and choose Néron generators omega, omega_B.
Write $q_H^*\omega_B=a_H\omega$.

**[NEW] Lemma3.1.** Every nonzero p-torsion formal parameter z(t) has
valuation $1/(p^2-1)$, and
$$v(a_H)=\deg(H)=\frac1{p+1}. \tag{3.1}$$

*Proof.* The supersingular special fiber has its entire p-torsion
supported at the origin. The multiplication morphism has degree p²,
so its local expansion modulo p starts with a unit times $z^{p^2}$.
The linear term in characteristic zero is pz. Since p is a uniformizer
in the unramified original R, all intermediate coefficients are
divisible by p. Weierstrass preparation, or its Newton polygon, makes
$[p](z)/z$ a unit times an Eisenstein polynomial of degree p²-1.
This proves the first valuation assertion for all its nonzero roots.

The quotient isogeny on formal groups is a unit times
$\prod_{h\in H}(z-z(h))$. Its distinguished degree is p, because its
special fiber is purely inseparable of degree p. The derivative at
zero therefore has valuation
$$\sum_{h\ne0}v(z(h))=(p-1)/(p^2-1)=1/(p+1).$$
The invariant cotangent sequence identifies
$\omega_H=R'/(a_H)\cdot\omega$, proving the degree assertion.
All changes between integral Néron parameters contribute units.
$\square$

We use the following established exact order-p input.

**[THEOREM, Oort–Tate calculation]** For an order-p finite-flat group
H over the ring of integers of an algebraically closed complete
extension, and a generator t of its generic cyclic group, one can
write
$$\omega_{H^D}\simeq\mathcal O_C/(\gamma),\qquad
\alpha_H(t)=y\bmod\gamma,$$
with
$$v(\gamma)=1-\deg(H),\qquad v(y)=\deg(H)/(p-1). \tag{3.2}$$
This is Fargues §6.5, Lemma9, printedp943 (PDF page40 with its cover).
It is the finite-group Hodge–Tate map of (1.4), with domain H.

The pullback used to pass from (3.2) to the elliptic p-torsion must
not be replaced by its saturated image. The dual of the inclusion
$H\to\mathscr E[p]$ is
$$\mathscr E[p]^D\longrightarrow H^D.$$
Under principal polarizations it is $q_H$ restricted to p-torsion,
with $H^D$ identified with $\ker(q_H^\vee)\subset\mathscr B$.
Indeed the usual compatibility of isogeny Weil pairings is
$e_p(h,x)=e_{q_H}(h,q_Hx)$, which fixes that identification.
This equality on generic fibers extends to the finite-flat models,
whose coordinate algebras are R'-torsion-free.

Accordingly the induced cotangent map is
$$\omega_{H^D}\longrightarrow\omega_{\mathscr E[p]^D},
\qquad \omega_B\longmapsto a_H\omega. \tag{3.3}$$
It is the derivative of q_H, not the derivative of its dual.
The opposite pairing convention changes its sign only. The annihilator
of $\omega_{H^D}$ has valuation p/(p+1), and multiplication by a_H
of valuation1/(p+1) maps it into $\omega_{\mathscr E[p]^D}=R'/p$.
Thus this is the actual nonsaturated cotangent map.

**[NEW] Proposition3.2.** For every nonzero p-torsion point t,
$$v(o_p(t))=\frac{p}{p^2-1}<1. \tag{3.4}$$

*Proof.* Functoriality of the finite Hodge–Tate map makes o_p(t)
the image of (3.2) under (3.3). Its valuation is therefore
$$\frac1{p+1}+\frac1{(p+1)(p-1)}=\frac p{p^2-1}.$$
The value in (3.2) has valuation less than its annihilator's
valuation p/(p+1), and the image has valuation less than1.
Both valuations are consequently valuations of nonzero torsion
differentials, not valuations of arbitrarily chosen zero-class
representatives. No rescaling of the image by $a_H^{-1}$ is allowed.
$\square$

### 3.2. All p-power levels

In this subsection write $o_r=o_{p^r}$.
The Cartier pairings give the two compatible identities
$$o_1(p^{r-1}t)=o_r(t)\pmod{p\omega}, \tag{3.5}$$
for $t\in\widehat{\mathscr E}[p^r]$, and
$$o_r(t)=p^{r-s}o_s(t)\pmod{p^r\omega} \tag{3.6}$$
when t lies in $\widehat{\mathscr E}[p^s]$. The first is restriction along $\mathscr E[p]\subset
\mathscr E[p^r]$, dual to multiplication by $p^{r-1}$.
The second also follows directly by taking the $p^{r-s}$-th power
of the rigid trivialization of $\mathscr L_t^{p^s}$.

**[NEW] Corollary3.3.** If t has exact order p^s, with 1<=s<=r,
then
$$v(o_r(t))=r-s+\frac p{p^2-1}<r. \tag{3.7}$$
In particular the finite Hodge–Tate map has no nonzero point in its
kernel over this unramified supersingular base.

*Proof.* If s=r, (3.5) reduces to the nonzero order-p value (3.4),
of valuation less than1. Every lift modulo p^r has that same
valuation. Apply (3.6) for smaller s. The strict inequality in
(3.7) prevents truncation from making the class zero. $\square$

There is an independent weaker check that requires no unramified
hypothesis. Fargues §5.4, Theorem3, printedp935, says that the
cokernel of the linearized Hodge–Tate map for a finite-flat group
over $\mathcal O_C$ is killed by every element of valuation at least
1/(p-1). Applied to the dual of elliptic p^r-torsion, its target is
$\mathcal O_C/p^r$ times an invariant differential. For p>=3 this
cannot have zero image, since an element of valuation1/(p-1)<1<=r
does not kill the target. Some finite torsion point therefore has
nonzero obstruction. Such a point and its differential value are
defined over a finite extension of the original local field.
This weaker theorem already detects the full packet at any good
reduction prime; the exact formula (3.7) is restricted to the
unramified supersingular case proved above.

## 4. A different integral algebra lattice cannot hide a horizontal line

The following argument keeps the integral model, not just its
generic representation.

**[NEW] Lemma4.1 (saturation with a connection).** Let X be a regular
integral surface smooth of relative dimension one over a complete DVR.
Let M be a vector bundle with a regular relative connection, and let
L_K be a horizontal line subbundle of M on the generic curve. Its
saturation N in M is an invertible sheaf preserved by the connection.

*Proof.* Define N as the intersection of M with L_K in its generic
restriction. It is coherent by noetherianity. The quotient M/N embeds
in the generic-curve quotient, so is torsion-free on X. At a
two-dimensional local ring the depth lemma gives depth(N)>=2;
at height one N is free. Thus N is rank-one reflexive, hence
invertible on the regular surface.

The connection followed by projection to
$(M/N)\otimes\Omega^1_{X/R}$ is O_X-linear on N: its extra Leibniz
term has image zero. It vanishes generically. The target is
torsion-free because the differential sheaf is invertible, so it
vanishes everywhere. Thus N is preserved. $\square$

For a good elliptic model the restriction
$\operatorname{Pic}(X)\to\operatorname{Pic}(X_K)$ is injective.
A generically trivial line has a vertical divisor; the only vertical
prime is the geometrically integral special fiber, itself principal.
Consequently N in Lemma4.1 is the usual rigidified extension of its
generic torsion line, up to an isomorphism. Multiplying an isomorphism
by a scalar in K does not change a relative connection.

**[NEW] Corollary4.2.** If a generic algebra connection contains a
horizontal torsion line with nonzero obstruction (1.1) after a finite
local extension, no Azumaya extension of that generic algebra carries
a regular connection extending it.

*Proof.* Base change the proposed Azumaya algebra and connection to
that extension. Its underlying vector bundle satisfies Lemma4.1.
The resulting invertible horizontal extension is the same torsion
line by Picard injectivity, contradicting (1.1). $\square$

This rules out hiding the obstruction in an unstable or nondiagonal
integral lattice. It asserts a necessary condition for the fixed
generic connection; it does not rule out other connections with
infinite monodromy.

## 5. Consequence for the actual full torsion-character packet

Keep the finite torsor
$$T=f_D^{-1}(O),\qquad f_D(c)=[\mathcal O_C(nc-D)]$$
and the rank-n² Poincaré bundle from
[the previous proof, §9](projective-monodromy-attack.md).
For a Brauer class of period n, the required divisor D exists by the
reviewed period-index argument. For the Brauer-zero control one can
instead take C=E and D=n[O] for any n.

Geometrically the weights are the torsor T under $\widehat E[n]$.
The endomorphism algebra contains the line for every difference
$t_i-t_j\in\widehat E[n]$, with its finite-order connection.
This follows either directly from the Poincaré family or from the
constant algebra on the multiplication-by-n cover. After a finite
splitting field, its individual matrix-unit lines are actual generic
horizontal line subbundles.

**[NEW] Theorem5.1.** If p>=3 is a good prime dividing n, the
constructed finite-monodromy projective connection on this full packet
has no regular extension on any Azumaya model over $\mathscr E_{\mathbb Z_p}$.

*Proof.* Write n=mp^r with (m,p)=1. In the ordinary case Proposition2.1
supplies a torsion-character difference with unit obstruction.
In the supersingular case for E/Q_p, Corollary3.3 supplies a nonzero
obstruction for every nonzero p-primary difference. Alternatively,
the general Hodge–Tate cokernel bound supplies at least one.
The prime-to-p factor m does not affect vanishing. Apply Corollary4.2.
$\square$

For389a1 every possible remaining period has its prime divisors among
good primes at least5. Thus the theorem tests every possible nontrivial
period for this finite-packet construction, not only ordinary ones.
It makes no assertion that such a period occurs. The same obstruction
already holds for the Brauer-zero control with n>1.

The earlier rank-n degree-zero local construction still supplies
regular integral connections. Theorem5.1 explains why one cannot
demand that they extend this particular finite-order generic connection.
Regular connection existence and integral finite-monodromy descent
are distinct properties.

## 6. An actual integral ordinary subpacket

There is a positive local construction after reducing the character
set. We give it for n=p^r; prime-to-p factors can be retained separately.

Assume ordinary reduction. Let
$$C_r=(G_r^D)^0\subset\widehat{\mathscr E}[p^r]$$
be the connected dual subgroup. Every pair of weights in a coset
of C_r has zero obstruction by Proposition2.1. Conversely a set of
weights with all differences in the kernel is contained in one such
coset.

Local Selmer triviality identifies the torsor T with a division fiber
after choosing a local point on the genus-one curve. Properness then
extends it to a finite-flat $G_r^D$-torsor $\mathscr T/R$.
The quotient $\mathscr T/C_r$ is finite étale and has a section after
a finite unramified extension R'/R. Fix one, and let $\mathscr D$
be its inverse image, a finite-flat C_r-torsor of rank p^r.

Let
$$q:\widehat{\mathscr E}\to\widehat{\mathscr E}/C_r,\qquad
v=q^\vee:\mathscr E'\to\mathscr E. \tag{6.1}$$
The kernel of v is $C_r^D$, which is étale. Thus v is an actual
finite étale isogeny of degree p^r over R'. Pullback by v on Pic0
is q, whose kernel is C_r.

Use the chosen local origin to form the normalized Poincaré family
on $\mathscr E\times\mathscr D$, and push it to $\mathscr E$.
Call the resulting rank-p^r bundle $W_{\mathscr D}$.
The map from $\mathscr D$ to $\widehat{\mathscr E}/C_r$ is
schematically constant, since $\mathscr D$ is a coset torsor.
Poincaré functoriality therefore gives
$$v^*W_{\mathscr D}\simeq
 \mathscr L'\otimes
 (\mathcal O_{\mathscr E'}\otimes_{R'}\mathcal O(\mathscr D)) \tag{6.2}$$
for the line $\mathscr L'$ defined by that constant image point.
All rigidifications are at zero, so no unrecorded base-line factor
is needed; such a factor would cancel in endomorphisms in any case.

Taking endomorphisms in (6.2) gives the constant matrix algebra.
Its deck matrices are constant in the elliptic coordinate. The
constant differential therefore descends along the finite étale v,
constructing a regular integral projective connection on
$\mathcal End(W_{\mathscr D})$. Its generic fiber is the corresponding
horizontal character subpacket of the full construction.

This is a scheme-level construction on the finite-flat torsor
$\mathscr D$, including collisions of its special-fiber points.
It is not a direct sum asserted from its geometric points, and is
not inferred from Galois invariance over a ramified splitting field.

## 7. Global scope and the next arithmetic target

This subpacket discussion retains $n=p^r$ from §6. It can be applied
to individual primary Brauer classes. It does not assert that
prime-to-p character differences vanish in a general composite packet.

For389a1 the reviewed residual image on E[p] is surjective at every
good p>=5. The local connected line C_r therefore does not define
a G_Q-stable subgroup at any such prime: its p-torsion would give
an invariant line in E[p].

This also obstructs descent of the entire local block as an algebra,
not merely descent of its chosen weight subset. Over an algebraic
closure, $\mathcal End(W_{\mathscr D})$ has degree-zero line support
exactly $C_r$, each line occurring with multiplicity p^r. The
decomposition into these pairwise nonisomorphic line bundles is
unique. Descent of the algebra would therefore force its support
$C_r$ to be G_Q-stable. Tensoring $W_{\mathscr D}$ by any common
line does not change this endomorphism algebra or its support.

More generally, let S be a nonempty G_Q-stable subset of the
geometric weight torsor T, and suppose all its differences lie in
the ordinary local kernel C_r. The subgroup generated by these
differences is G_Q-stable and cyclic. If nonzero, its p-torsion is
an invariant line, a contradiction. Hence S is a singleton.
For the supersingular unramified case, Corollary3.3 makes this
conclusion immediate even locally.

Thus the positive ordinary block does not descend as this global
packet or its horizontal summand. In the stable-subset argument,
a singleton that descends as a marked weight (or its marked line)
is a rational point of the fixed character torsor T, and trivializes
that finite torsor. Descent of only its scalar endomorphism algebra
does not supply such a marked weight: the endomorphism algebra
of every geometric line is $\mathcal O$, and the scalar algebra
is already present independently of $\beta$.
Marked singleton descent is stronger than the vanishing of its
image $\beta$: $\beta=0$ does not force the unshifted T to be
trivial. Equivalence with $\beta=0$ requires allowing a global
Kummer adjustment, namely replacing T by $f_D^{-1}(P)$ for some
$P\in E(\mathbb Q)$. A rational point c of C gives such a fiber
by taking P=f_D(c); conversely a rational point of any such fiber
is a rational point of C. This is the unresolved adjusted
character-torsor step of the previous construction.
This argument concerns subpackets of the actual finite-monodromy
construction, not arbitrary new Euler systems, derived operations
or different geometric objects.

**[GAP TC-389]** Construct a uniform splitting object for the original
Brauer classes by an arithmetic mechanism that survives these exact
torsion-differential and global-descent conditions, or construct the
rational point in the appropriately Kummer-adjusted character torsor.
The existing degree-n and degree-n² constructions do not provide
a period-independent bound.

No p-curvature conjecture was invoked. The negative result is an
explicit integral-connection obstruction, and the positive result
is a local finite étale isogeny construction. Neither proves a
nonzero Sha class or resolves full BSD.
