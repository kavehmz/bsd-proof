# Independent review of arithmetic duality for the Heegner defect

Date: 2026-09-12. Reviewer /root/uniform_witness, GPT-6 Astra/xhigh.
Reviewed [proof](heegner-defect-duality.md) and
[checkpoint](heegner-duality-checkpoint.md).

**PASS after the stated S/U clarification.** The final proof
defines S to be exactly the finite complement of the stated U,
together with the real place; the compact-support cone therefore
uses the correct local terms. All eight sections pass review,
and no mathematical correction remains.
No Sha-finiteness or height-nondegeneracy premise is needed.

Reviewed proof SHA256:
82988ad697e83ad52675cf5e806beda50f59848af7060974051facf3dd0391e7.
Reviewed checkpoint SHA256:
41402c0df9b08d9f36fa0d272b20ac23df31fd726f2272ba98458cdb161e410c.
Subsequent review links and checkpoint status updates are editorial.

## 1. Lower-index vanishing and strict Selmer descent

The previous reviewed odd-rank result gives $\nu_K\ge2$ under
the current ordinary irreducible hypotheses. Thus each one-prime
Heegner class is zero in its full coefficient quotient, and its
reduction to the common coefficient $p^k$ is zero.

Apply the finite-singular relation at ell to the one-prime
class indexed by q, and at q to the one-prime class indexed
by ell. The two-prime class has transverse local condition.
For these good inert primes, arithmetic K-Frobenius acts
trivially on $E[p^k]$ and the transverse local subgroup maps
isomorphically to the singular quotient. Vanishing of the
singular image therefore gives vanishing of the entire local
class. No desired rank-five conclusion is used at this step.
The previously repaired scalar normalization preserves these
zeros at the full coefficient.

The finite local condition outside m needs to be read with
its propagated definition, especially at bad primes.
[BCGS, arXiv:2312.09301v2, §1.1.1](https://arxiv.org/html/2312.09301v2#S1.SS1.SSS1)
defines the $p^k$ condition as the preimage of the
p-infinity point condition. This is the full Kummer image
$E(K_w)/p^k$ and is not merely the unramified subgroup of
$H^1(K_w,E[p^k])$ at every bad place.

One can verify that distinction directly using
$0\to E[p^k]\to E[p^\infty]\xrightarrow{p^k}E[p^\infty]\to0$.
The kernel of the map from finite cohomology to p-infinity
cohomology is $E(K_w)[p^\infty]/p^k$. It accounts for
the local torsion discarded by tensoring the point group
with $\mathbb Q_p/\mathbb Z_p$. The local Kummer diagrams
then identify the full preimage with $E(K_w)/p^k$.
At w away from p, the p-infinity point condition is zero,
whereas its finite preimage can contain precisely these
local torsion/component classes. At w above p, the
ordinary point condition gives the same finite Kummer
preimage, including the finite local torsion. Thus the
proof does not accidentally omit p-primary Tamagawa
contributions in passing to the finite Selmer group.

Odd analytic rank gives $w(E)=-1$, so the repaired raw
two-prime conjugation sign is $+1$. Restriction
$H^1(\mathbb Q,V)\to H^1(K,V)^+$ is an isomorphism:
all positive-degree cohomology of the order-two quotient
with p-primary coefficients vanishes. Its inverse is
$\frac12\operatorname{cor}$. Local corestriction on
Kummer classes is induced by the norm on point groups;
at split places it is the sum of the two local maps.
Multiplication by the inverse of 2 modulo $p^k$ is an
ordinary scalar on the finite Kummer subgroup. At ell
and q, restriction is injective since
$\operatorname{cor}\operatorname{res}=2$.
This proves membership in the asserted strict Selmer
group over Q and both zero localizations.

The real local cohomology is zero at odd p. This
applies to the Selmer local condition as well as to
the modified real terms in arithmetic duality.
The proof does not identify this Selmer class with a
Sha class; rational-point directions remain present.

## 2. The actual defect injection is integral and unramified

Inversion on G preserves its maximal order in
$\mathbb Q_p[G]$. Thus M, $M^{\max}$, C and the Tor
injection have the full semidirect-product action
$\Gamma=\operatorname{Gal}(F/\mathbb Q)$.
The Galois equivariance and injectivity of the Tor
and Kummer maps transfer the conjugation invariance
of the raw class to the actual element theta.

On $U_F$, the elliptic curve is an abelian scheme
and multiplication by $p^k$ is finite étale. Every
point of E(F) extends to a section over $U_F$ by
properness over its good places, so the point
Kummer torsors are actual classes in $H^1(U_F,V)$.
This justifies the unramified arithmetic-scheme
target, not only a generic-field target.

The cover $U_F\to U$ is finite étale and
$H^0(U_F,V)=E(F)[p^k]=0$ by the preceding reviewed
torsion calculation. The first five terms of
Cartan-Leray consequently identify
$$
 H^1(U,V)\simeq H^1(U_F,V)^\Gamma .
$$
There is no required higher-degree $K(\pi,1)$
assertion in this argument. It produces the
claimed canonical injection of $C[p^k]^\Gamma$.

For the explicit cocycle, the invariant point
residue guarantees a point $R_g\in E(F)$ with
$p^kR_g=(g-1)P_d$. Absence of p-primary torsion
gives uniqueness and $R_{gh}=R_g+gR_h$.
Hence $(g-1)Q_d-R_g$ is a cocycle with values
in V, restricting to the prescribed point
Kummer cocycle. Changing representatives
changes only its cohomology class. This is
an actual arithmetic injection from the
specified lattice quotient, not an assumed
realization of arbitrary abstract characters.

## 3. Primary duality and the Weil-pairing order

The primary statements were read directly in
[Demarche-Harari, arXiv:1804.03941v3, Theorem 1.1,
§2 and §5](https://arxiv.org/html/1804.03941),
and
[Milne, *Arithmetic Duality Theorems*, II.2.13,
II.3.3 and II.3.9–3.10](https://www.jmilne.org/math/Books/ADTnot.pdf).
The unversioned arXiv HTML identifies itself as v3
of 26 August 2019. The theorem applies to number
rings and says that the groups here are finite.
Its invertible-order case already applies to V
on U; no positive-characteristic fppf issue is
being imported into this setting.

Demarche-Harari use the compact-first pairing
$H_c^2(U,V)\times H^1(U,V^D)$.
The chosen identification sends the **ordinary**
factor z to the character $w\mapsto e_{p^k}(w,z)$.
Evaluation then gives exactly
$e_{p^k}(\text{compact factor},\text{ordinary factor})$
as in (3.1). This explains why the displayed
compact-first product has the declared Weil
order. If one instead identifies the compact
factor with its dual and writes an ordinary-first
evaluation, the alternating Weil pairing supplies
the opposite convention; it must not be silently
substituted for the proof's chosen one.

The image of the compact trace is in
$p^{-k}\mathbb Z/\mathbb Z$ because the product
is killed by $p^k$. Complete Tate complexes at
real places are acyclic for odd-order modules:
averaging by 2 contracts their cohomology.
F is totally imaginary. There is therefore no
unrecorded real p-primary contribution or
additional one-half in the global trace.

Perfect finite duality and the injection alpha
give the asserted surjection onto the character
group of the invariant defect. Every character
of a subgroup extends into $\mathbb Q/\mathbb Z$;
the exponent of the ambient group then forces
its values into $p^{-k}\mathbb Z/\mathbb Z$.
Extending the character sending an element of
order $p^s$ to $1/p^s$ proves exact-order
detection. No nondegeneracy of a height or
Cassels-Tate pairing is needed.

## 4. Cone product, boundaries and strict local annihilators

With the declared cone convention
$$
 D(a,b)=(da,\operatorname{res}a-db),
$$
a compact degree-two cocycle obeys da=0 and
$db=\operatorname{res}a$. If dz=0, the product
$(a\smile z,b\smile\operatorname{res}z)$ has
zero differential. For example its local
differential is
$\operatorname{res}a\smile\operatorname{res}z
-db\smile\operatorname{res}z=0$.
The sign from differentiating a local
degree-one b is correctly negative in the
Leibniz rule.

The formula also respects boundaries. If
$(a,b)=D(u,v)$ and dz=0, its product with z is
$D(u\smile z,v\smile\operatorname{res}z)$.
If z changes by dt, with t of degree zero,
the change is $D(a\smile t,b\smile\operatorname{res}t)$.
These calculations verify the product without
omitting the compact class's global component.

The chosen connecting representative
$(0,\beta)$ and compact trace normalized by
the sum of local Brauer invariants give
exactly (5.3), with beta first in the cup
product. The sign is consistent with the
compact-first Weil order in §3 of this review.
The ordinary global two-cochain of a general
compact test need not vanish; boundary tests
alone need not exhaust the detecting group.

Local abelian duality and its compatible
isogeny sequences in Milne I.3.2–I.3.5 make
the finite Kummer subgroup its own exact
annihilator for the principal-polarized
finite Weil/Tate pairing. This holds at
the p-adic and bad-reduction places too,
with their full point Kummer groups.
At ell and q the strict condition is zero,
whose annihilator is all local cohomology.

Dualizing the localization map from
$H^1(U,V)$ into the sum of local quotients
therefore gives precisely the subgroup
$L_m$ in (6.1). The cone boundary pairing
identifies its image with the annihilator
of the strict Selmer group. Finite perfect
duality proves (6.2). In particular every
test at either old auxiliary prime
annihilates the actual class, whereas
the remaining quotient still detects
the whole strict Selmer group, including
its point directions.

## 5. Transfer and the erased pullback tests

The finite étale sheaf trace is the sum
over the full geometric fiber. It is
adjoint to restriction under arithmetic
duality and is compatible with cup
product. Milne II.3.9–3.10 explicitly
checks the norm against local Brauer
invariants and the compact trace.
Thus both identities (7.1) have the
stated factor $h=[F:\mathbb Q]$.

The pairing upstairs is Gamma-invariant.
The finite Pontryagin dual of
$H_c^2(U_F,V)_\Gamma$ is
$H^1(U_F,V)^\Gamma$. Cartan-Leray has
already identified the latter with
$H^1(U,V)$. The adjoint map is
corestriction, so dualizing gives the
claimed isomorphism on coinvariants.
It neither divides by h nor replaces
coinvariants with invariants.

Pulling back both inputs instead gives
h times the downstairs pairing. Here
$h=2h_K(\ell+1)(q+1)$ is divisible by
$p^k$, so that value is zero in the
specified target. Corestriction can
still be surjective: the compact
class lifting a detecting downstairs
test need not itself be pulled back.
These facts are compatible, and the
proof keeps them separate.

The argument concerns full arithmetic
cohomology. It does not establish
Selmer control across the p-divisible
ring-class extension, where local
point conditions can change. That
scope restriction in the proof is
necessary and correctly retained.

## 6. Remaining scope and continuity

The perfect pairing makes HD-TP5
equivalent to the desired vanishing,
but supplies no higher-complex-derivative
formula for its values. Restricting
the strict Selmer dual further to the
actual subgroup $D_m^{\mathrm{str}}$
is legitimate by finite character
extension. A pairing on Sha alone,
the old-prime boundary tests, or the
automatically zero pullback pairings
would not replace these detecting tests.

The checkpoint's initial K-only
construction and its “both fields are
totally imaginary” wording are historical
planning: the final construction
descends to Q and explicitly uses the
real Tate convention. After final PASS,
the coordinator should update that
status and the candidate/verify wording.
Only this review file was written;
no old certificate or numerical
script was rerun and no agent spawned.
