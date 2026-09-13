# Arithmetic duality for the actual two-prime Heegner defect

Date: 2026-09-12. Owner: coordinator. New deductions passed
[independent review](review-heegner-defect-duality.md). The objective remains full BSD over Q. This note constructs finite
arithmetic tests for the reviewed TP5 obstruction; it does not prove that
the tests vanish from analytic rank five.

## 1. Actual fields, lattices and the finite obstruction

Keep every hypothesis and convention of the
[reviewed two-prime Heegner construction](two-prime-heegner-height-attack.md).
In particular E/Q is non-CM, p≥5 is good ordinary with irreducible E[p],
its analytic rank is odd and at least five, and K satisfies the stated
Heegner and rank-zero auxiliary-twist hypotheses. Set m=ell q and retain
the full common coefficient p^k. Write F=H_m,

$$G=\operatorname{Gal}(F/K),\qquad
\Gamma=\operatorname{Gal}(F/\mathbb Q)=G\rtimes\langle\tau\rangle,$$

where τ is a complex conjugation and acts on G by inversion.
Let V=E[p^k], A=Z/p^k, and A^*=p^(-k)Z/Z inside Q/Z.
The already constructed actual lattices are

$$M=E(F)\otimes\mathbb Z_p,\quad
M^{\max}=\mathscr O_m M\subset M\otimes\mathbb Q_p,\quad
C=M^{\max}/M,$$

where O_m is the maximal order of Q_p[G]. Inversion preserves O_m,
so these lattices and C have their natural full Γ-actions. The Tor map is

$$j_k:C[p^k]\hookrightarrow M/p^kM,
\qquad [Q]\longmapsto p^kQ\bmod p^kM.\tag{1.1}$$

The particular element θ=θ_m is the residue of P_m/p^k, with
P_m=S_GD_ell D_q y_m. The preceding proof establishes that it exists
in M^max, lies in C[p^k]^G, and maps under j_k and Kummer to the
restriction of the raw two-prime Heegner class. It also proves E(F)[p]=0.
All assertions below retain that full p^k coefficient.

## 2. Descent to Q and the strict finite Selmer group

Let κ_K be the raw two-prime class over K. We continue to use the raw
class; the normalized two-prime system differs by the proved scalar −1
and the fixed tensor generators, so has the same vanishing and order.

**[NEW] Proposition 2.1.** The element θ is Γ-invariant and determines
a unique class

$$\kappa_{\mathbb Q}\in\operatorname{Sel}_{p^k}(E/\mathbb Q),
\qquad\operatorname{res}_{K/\mathbb Q}\kappa_{\mathbb Q}=\kappa_K.$$

It satisfies

$$\kappa_{\mathbb Q}=\tfrac12\operatorname{cor}_{K/\mathbb Q}\kappa_K,
\qquad \operatorname{loc}_\ell\kappa_{\mathbb Q}
=\operatorname{loc}_q\kappa_{\mathbb Q}=0.\tag{2.1}$$

*Proof.* The repaired conjugation calculation gives
τκ_K=epsilon_2 κ_K with epsilon_2=−w(E)=1, since the analytic rank is
odd. The equivariant injectivity of j_k and of Kummer consequently gives
τθ=θ. The Γ-invariance of its point residue also follows directly from
the same conjugation calculation on P_m modulo p^k.

The [reviewed odd-rank theorem](odd-rank-selmer-bridge.md) gives
nu_K=s_p(E)−1≥2. Hence every one-prime class vanishes in its full
coefficient quotient. At ell and q, the finite-singular relations for
the two-prime class therefore have zero right-hand side. Its local
class is transverse there, and the transverse-to-singular map is an
isomorphism. Its whole localization is consequently zero at both primes.
Outside m, the propagated classical point conditions are the finite
Kummer conditions. Thus κ_K belongs to the ordinary finite Selmer group,
with zero localization at the two auxiliary primes. This step uses the
proved lower-index vanishing, not the desired rank-five conclusion.

Because 2 is invertible on V, restriction identifies H¹(Q,V) with the
τ-invariants in H¹(K,V). Equivalently use inflation-restriction and
average over this quadratic group. The inverse is (1/2)corestriction.
Local corestriction of a point Kummer class is the Kummer class of the
local norm of that point. The same formula includes both completions
at a split place. It follows that (1/2)corestriction of κ_K satisfies
the finite Kummer condition at every rational place. The real condition
is zero at odd p. Finally local restriction at the inert ell and q is
injective, because restriction followed by corestriction is multiplication
by 2. Their K-localizations were zero, proving (2.1). ∎

In particular the obstruction is not automatically a Sha class: the
finite Selmer group here retains both point Kummer classes and Sha.
Neither their quotient nor any primary finiteness is assumed.

## 3. The finite arithmetic cohomology pairing

Let S consist exactly of the rational primes dividing NpDm and the real place,
and put

$$U=\operatorname{Spec}\mathbb Z[1/(Np|D|m)],\qquad
U_F=\operatorname{Spec}\mathcal O_F[1/(Np|D|m)].$$

The map U_F→U is finite étale, with group Γ, because F/Q is ramified
only at primes already inverted. The good elliptic scheme over U has
finite étale p^k-torsion V. This use of arithmetic duality is on the
one-dimensional number rings, not on the elliptic arithmetic surface.

**[THEOREM, finite duality input]** Artin–Verdier duality gives perfect
pairings of finite groups

$$H^1(U_L,V)\times H^2_c(U_L,V^D)\longrightarrow A^*,
\qquad L=\mathbb Q,F,$$

where V^D=Hom(V,G_m). See
[Demarche–Harari, arXiv:1804.03941v3, Theorem 1.1 and §2](https://arxiv.org/html/1804.03941)
for the finite-flat theorem, compact-support cone and number-field
finiteness; here the order is already invertible. See also
[Milne, *Arithmetic Duality Theorems*, II.3.3](https://www.jmilne.org/math/Books/ADTnot.pdf).
Real places use complete Tate complexes. These vanish for our odd
coefficients; F has no real places. Thus there is no omitted real
p-primary term.

Use the Weil pairing to identify V with V^D by sending v to
(w↦e_(p^k)(w,v)). In the following compact-first formula this
identification is applied to the ordinary class z, so the compact
coefficient is V and the ordinary coefficient is V^D. Define

$$\mathscr P_L(z,\eta)
=\operatorname{tr}_{L,c}\bigl(\eta\smile z\bigr),
\quad z\in H^1(U_L,V),\ \eta\in H^2_c(U_L,V),\tag{3.1}$$

with coefficient pairing e_(p^k)(compact factor, ordinary factor).
The trace is normalized by the usual local Brauer invariants on the
compact-support boundary. This fixes the overall sign as well as the
inclusion A^*⊂Q/Z. It is not a p-adic height.

We write H¹(U_L,V) rather than assume a higher-degree K(pi,1)
comparison. In degree one its classes are precisely the finite étale
torsors, so the usual unramified Galois H¹ description and the Kummer
classes used here agree. All higher cochain models below compute the
actual étale/compact-support groups.

## 4. A canonical arithmetic dual for the invariant defect

Put D_m=C[p^k]^Γ. The finite cover has H⁰(U_F,V)=E(F)[p^k]=0.
The Cartan–Leray inflation-restriction sequence therefore gives

$$\operatorname{res}:H^1(U,V)
 \overset\sim\longrightarrow H^1(U_F,V)^\Gamma.\tag{4.1}$$

Kummer and j_k are Γ-equivariant injections. Consequently they define
a canonical injection

$$\alpha:D_m\hookrightarrow H^1(U,V),\qquad
\operatorname{res}\alpha(d)=\delta_F(j_k(d)),\quad
\alpha(\theta)=\kappa_{\mathbb Q}.\tag{4.2}$$

To represent this map by actual point data, choose a point P_d in E(F)
representing j_k(d), using E(F)/p^k≅M/p^kM. Choose Q_d in E(Qbar)
with p^kQ_d=P_d. For g in G_Q there is a unique R_g in E(F) with
p^kR_g=(g−1)P_d. Then

$$c_d(g)=(g-1)Q_d-R_g\tag{4.3}$$

is the descended cocycle. The same no-p-torsion and invariance arguments
as in the Heegner construction prove existence, uniqueness and its
cocycle identity. Changing the point representative or its division
point changes only the cohomology representative. This describes α
without replacing the actual Mordell–Weil lattice by a model module.

**[NEW] Proposition 4.1.** The map

$$\mathcal E_m:H^2_c(U,V)\twoheadrightarrow\operatorname{Hom}(D_m,A^*),
\qquad \mathcal E_m(\eta)(d)=\mathscr P_{\mathbb Q}(\alpha(d),\eta)
\tag{4.4}$$

is a canonical surjection. It induces a perfect pairing of D_m with
H²_c(U,V)/ker(E_m). If θ has exact order p^s, there is an η for which
E_m(η)(θ) has that same exact order p^s.

*Proof.* Perfect duality identifies H²_c(U,V) with the Pontryagin dual
of H¹(U,V). Restriction of characters along the injection α is surjective:
a character of a subgroup extends to a finite abelian group with values
in Q/Z, which is divisible. Because the whole group is killed by p^k,
the extended character has image in A^*. This proves (4.4) and the
perfect quotient pairing. Extend the character sending a generator θ
of its cyclic subgroup to 1/p^s to obtain the last assertion. ∎

Thus these are actual compact-support arithmetic cohomology tests,
not unspecified characters whose arithmetic realization is assumed.
The construction proves their existence and exact pairing. It does not
compute their values from complex central derivatives.

## 5. Cochains and the local terms retained by the tests

Choose compatible cochain models C_L for RΓ(U_L,V) and C_v for the
local complexes, with cup products and restriction maps. With real
Tate terms zero in our range, use the convention

$$C^i_{L,c}=C^i_L\oplus\bigoplus_{v\in S_{L,f}}C^{i-1}_v,
\qquad D(a,b)=(da,\operatorname{res}a-db).\tag{5.1}$$

**Signed-boundary clarification (subsequent Gysin review).** With the
natural PLUS projection from this fiber complex to C_L, the canonical
triangle connecting map sends beta to (0,-beta). In this note the symbol
partial was fixed as the SIGNED map beta -> (0,+beta), and the trace was
fixed positively on that signed boundary. Thus partial is minus the
canonical connecting map in this particular cochain convention. The trace
is correspondingly opposite to one fixed positively on the canonical
connecting map. All displayed pairings and formulas here retain their
original declared signs; perfectness, annihilators and transfer are
unchanged. The [closed-point comparison](heegner-gysin-bridge.md) explicitly
uses a signed Gysin class as well and does not identify it with the
standard positive divisor class.

This is the shifted compact-support cone. A class η in H²_c is
represented by (a,(b_v)) with da=0 and db_v=res_v a. If z is represented
by a closed ordinary one-cochain, the compact-first product is represented
by

$$(a\smile z,(b_v\smile\operatorname{res}_v z)_v).\tag{5.2}$$

The differential vanishes by the displayed equations and Leibniz rule.
Changing either cocycle representative changes (5.2) by a cone boundary.
Taking the compact trace gives exactly (3.1), with the Weil pairing on
coefficients. This direct cone calculation retains the global two-cochain;
it is not silently dropped in favor of only local classes.

For β=(β_v) in the direct sum of local H¹ groups, the signed boundary class
∂β is represented by (0,(β_v)). Our trace convention gives

$$\mathscr P_L(z,\partial\beta)
=\sum_{v\in S_{L,f}}\operatorname{inv}_v
       (\beta_v\smile\operatorname{loc}_v z).\tag{5.3}$$

This fixes the local evaluation rule for tests that do come from the
boundary. General detecting classes need not have zero global component.
The cone and its product can also be obtained from the resolutions in
Demarche–Harari §2; formula (5.2) is checked here without importing a
function-field-only comparison from their appendix.

## 6. The dual of the Selmer group with two strict local conditions

Let F_v be the finite Kummer subgroup E(Q_v)/p^k inside H¹(Q_v,V).
It is its own exact annihilator for the local Weil/Tate pairing. This is
the finite Kummer consequence of local abelian duality and its compatible
isogeny sequence; see Milne, I.3.2–I.3.5. Equivalently, the adjoint of the
map to H¹(Q_v,E)[p^k] is the local point Kummer injection, so their
kernel and annihilator coincide.

Define S_m^str to be the ordinary finite Selmer group over Q with zero
localization at ell and q. It is a subgroup of H¹(U,V). Let

$$\mathcal F^{\rm str}=\bigoplus_{v\in S_f}\mathcal F_v^{\rm str},
\quad \mathcal F_v^{\rm str}=\begin{cases}0,&v=\ell,q,\\
F_v,&v\ne\ell,q,\end{cases}$$

and

$$L_m=\partial\left(
 \bigoplus_{v\in S_f\setminus\{\ell,q\}}F_v
 \ \oplus H^1(\mathbb Q_\ell,V)\oplus H^1(\mathbb Q_q,V)\right).
\tag{6.1}$$

**[NEW] Proposition 6.1.** There is a canonical perfect pairing

$$S_m^{\rm str}\times\bigl(H^2_c(U,V)/L_m\bigr)\longrightarrow A^*.
\tag{6.2}$$

In particular κ_Q is annihilated by every compact boundary test in L_m,
but is still detected by the quotient (6.2) if nonzero.

*Proof.* The group S_m^str is the kernel of H¹(U,V)→(direct sum local
H¹)/F^str. Dualizing this sequence identifies its annihilator in the
Pontryagin dual of H¹(U,V) with the image of (F^str)^perp. By local
self-duality of the finite Kummer groups, this local perpendicular is
exactly the group inside parentheses in (6.1). Formula (5.3) identifies
its map to H²_c(U,V) with ∂. Global perfect duality then proves (6.2).
Proposition 2.1 supplies κ_Q in this strict group. ∎

This is a degree-two compact-support dual of the entire finite Selmer
group, including its point directions. It is not the Cassels–Tate pairing
on Sha, which would forget those directions. At the two original auxiliary
primes every local boundary test is zero on κ_Q, because its localization
there is zero. A fresh-prime test is a different construction.

## 7. Transfer preserves the tests through coinvariants, not averaging

Let h=[F:Q]=2h_K(ell+1)(q+1). In particular p^k divides h.
The finite étale cover supplies pullback, corestriction and their
projection formula for (3.1):

$$\mathscr P_F(\operatorname{res}z,\eta_F)
=\mathscr P_{\mathbb Q}(z,\operatorname{cor}\eta_F),\qquad
\operatorname{cor}\operatorname{res}\eta=h\eta.\tag{7.1}$$

These identities follow from the sheaf trace (sum over the finite fiber)
and its compatibility with cup product and the compact trace. No division
by h occurs in their construction.

**[NEW] Proposition 7.1.** Corestriction induces an isomorphism

$$H^2_c(U_F,V)_\Gamma\overset\sim\longrightarrow H^2_c(U,V).
\tag{7.2}$$

But for any two classes z in H¹(U,V) and η in H²_c(U,V),

$$\mathscr P_F(\operatorname{res}z,\operatorname{res}\eta)
=h\mathscr P_{\mathbb Q}(z,\eta)=0.\tag{7.3}$$

*Proof.* Under the finite perfect dualities, the dual of the coinvariant
group on the left of (7.2) is H¹(U_F,V)^Γ. Equation (4.1) identifies
that group with H¹(U,V), and (7.1) identifies the dual map with
corestriction. Taking finite Pontryagin duals proves (7.2). The second
identity in (7.1) gives (7.3); its value is killed by p^k and p^k divides h. ∎

Corestriction is therefore surjective, although it annihilates the
pullback of a base class here. If a detecting η downstairs is chosen,
there is an upstairs compact class η_F whose corestriction is η.
It need not be the pullback of a downstairs class. Restricting attention
to those pullbacks would erase every test in (7.3).

Equation (7.2) concerns full cohomology and its compact-support dual.
It is not a Selmer control isomorphism across this p-divisible-degree
extension: local Kummer conditions may acquire extra classes after base
change. No such Selmer-invariants identification is assumed.

## 8. The remaining arithmetic vanishing

Let D_m^str be the subgroup of D_m whose image under α lies in S_m^str.
It contains θ. Restricting the perfect pairing (6.2) gives a canonical
surjection onto Hom(D_m^str,A^*), so the strict Selmer quotient still
supplies all detecting characters of this actual defect.

**[GAP HD-TP5].** Under the analytic-rank-five hypotheses, prove

$$\mathscr P_{\mathbb Q}(\kappa_{\mathbb Q},\eta)=0
\quad\text{for every }\eta\in H^2_c(U,V)/L_m.\tag{8.1}$$

Equivalently it is enough to do so for any constructed collection whose
images generate the dual of D_m^str. Such a proof must give an actual
geometric or arithmetic comparison with the higher untwisted vanishing.
It may not replace (8.1) by the automatically zero base-changed pairings
(7.3), by a pairing on Sha alone, or by tests at the two original primes.

By the proved perfect pairing, (8.1) is equivalent to θ=0 and hence to
the two-prime O5 vanishing. The construction here has supplied exact
finite arithmetic tests, their cochains, and their transfer behavior.
It has not proved their vanishing, a new Selmer corank bound, full Sha
finiteness, or the universal BSD leading formula.
