# Signed closed-point classes and a residue presentation of the Heegner tests

Date: 2026-09-12. Owner: coordinator. Status: completed; every [NEW] deduction below passed
[independent adversarial review](review-heegner-gysin.md), including
the signed-convention repair and the irreducible-image extension. The objective remains full BSD over Q, which is unresolved.

## 1. Fixed arithmetic object and normalization

Keep the actual objects and all hypotheses of
[Heegner defect duality](heegner-defect-duality.md) and
[fresh-prime geometric reciprocity](heegner-local-reciprocity-attack.md).
In particular n=p^k, R=Z/n, V=E[n],
U=Spec Z[1/(Np|D|m)], m=ell q, and S is EXACTLY the finite complement
of U together with its real place. Let kappa_Q be the raw two-prime
Q-class already proved to lie in strict finite Selmer, with zero old-prime
localizations. Its K-restriction is kappa_K. Its lattice obstruction is
zero if and only if kappa_Q is zero.

The compact pairing is the one fixed in the duality note:

$$\mathscr P(z,\eta)=\operatorname{tr}_c(\eta\smile z),
\qquad H^1(U,V)\times H^2_c(U,V)\longrightarrow n^{-1}\mathbb Z/\mathbb Z,
\tag{1.1}$$

using e_n(compact coefficient,ordinary coefficient). Its trace on a
compact boundary is the SUM of the usual local Brauer invariants.
All Frobenius elements in this note are arithmetic Frobenius.
The compact cone has differential D(a,b)=(da,res(a)-db).
At odd p the real Tate complex vanishes.

**Convention audit.** In this displayed fiber complex, with its natural
PLUS projection to the ordinary cochains, the canonical triangle's
connecting map sends a local cocycle beta to (0,-beta). The predecessor
instead FIXED the signed map partial^+(beta)=(0,+beta) and its trace by
tr_c(partial^+ beta)=sum inv(beta). We retain precisely that signed map
and trace; every partial in this note means partial^+. Relative to a
trace normalized positively on the canonical connecting map, this trace
has the opposite sign. Perfectness and projection formulas are unchanged.
The closed-point class G_v defined below is also signed: it is MINUS
the usual positive-valuation Gysin class. These choices are stated before
the pairing calculation and are not identified with the canonical
triangle's boundary or the positive divisor class.

Let v be a fresh prime outside S, with good reduction. Put
W_v=H^0(F_v,V(-1)). Regard an element y of W_v as the actual unramified
Galois-equivariant homomorphism mu_n -> V on the henselian local trait.
The Weil pairing defines a Galois-equivariant functional
lambda_y:V -> R by

$$e_n(y(\zeta),x)=\zeta^{\lambda_y(x)}\quad(\zeta\in\mu_n).
\tag{1.2}$$

No choice of a primitive root is needed for this definition. It factors
through the Frobenius coinvariants of V. For z in H^1(U,V), write
z_v(F_v) for a cocycle's unramified Frobenius value modulo (F_v-1)V;
lambda_y(z_v(F_v)) is independent of its representative.

## 2. Local purity and the explicitly signed closed-point class

Let i_v:Spec F_v -> U. The usual Kummer valuation residue sends
delta(v) to 1. With the natural PLUS projection in our local fiber
complex, its canonical support boundary is represented by (0,-delta(v)).
Write g_v^std for the corresponding positive-valuation Gysin map.
Our closed-point map is explicitly its negative:

$$G_v=-g_v^{\rm std}:W_v\longrightarrow H^2_{\{v\}}(U,V)
                    \longrightarrow H^2_c(U,V).\tag{2.1}$$

The last map exists because the support is a proper closed subscheme
inside U; it retains the trivialization on the complement and hence at S.
It is not merely the map to ordinary H^2(U,V).

**[THEOREM, primary local and functorial inputs]** The needed support
calculation follows from Milne, *Arithmetic Duality Theorems*, second
edition (2006), II.1.5–II.1.7, and Kummer theory. Compact extension by
zero and its local exact sequences are in II.2.3–II.2.4. For cochain
excision and compatibility with cup products use Demarche–Harari,
arXiv:1804.03941v3, Proposition 2.12, Lemmas 4.1 and 4.7. Sources read:
[Milne](https://www.jmilne.org/math/Books/ADTnot.pdf),
[Demarche–Harari](https://arxiv.org/html/1804.03941).
Only the invertible finite coefficient case is used here.

For clarity, the specific purity calculation can be reconstructed locally.
Over the strict henselization at v, every unit has an n-th root. Thus
Kummer classes of the fraction field, modulo those from the trait, are
measured by valuation modulo n. The trait has no higher étale cohomology
for these locally constant finite coefficients. Its support cohomology
vanishes below degree two and in degree two is canonically V(-1).
Descent of this calculation gives H^2_{v}(U,V)=H^0(F_v,V(-1)).
The SIGNED image G_v(y) is represented in the local support cone by

$$(0,\beta_y),\qquad \beta_y=y_*\delta(v)\in H^1(\mathbb Q_v,V).
\tag{2.2}$$

Replacing v by another uniformizer changes beta_y by an unramified
class and leaves its support class unchanged. This gives (2.1) from
actual finite sheaves and Kummer cocycles. No higher K(pi,1) comparison
and no purity theorem on the elliptic arithmetic surface is assumed.

## 3. The closed-support sign is opposite the pushed local boundary

Write U'=U\{v}, j:U' -> U. Its usual compact cone has the added Q_v
term. Let partial'_v be the local connecting map from H^1(Q_v,V)
to H^2_c(U',V).

**[NEW] Proposition 3.1.** With the orientation in §2,

$$G_v(y)=-j_!\partial'_v\beta_y.\tag{3.1}$$

*Proof.* The sign can be checked before taking cohomology. Let A, O, K
and L be compatible actual étale cochain models for U', the henselian
trait at v, its fraction field, and the local terms at S, respectively.
Étale excision identifies the ordinary complex on U with the homotopy
fiber of A direct-sum O -> K, using restriction from A MINUS restriction
from O. Consequently an actual model for the compact complex of U has
coordinates in degree r

$$(a,o,h,s)\in A^r\oplus O^r\oplus K^{r-1}\oplus L^{r-1},$$

and differential

$$D(a,o,h,s)=(da,do,\operatorname{res}_v a-\operatorname{res}_v o-dh,
                        \operatorname{res}_S a-ds).\tag{3.2}$$

The ordinary comparison sends a cochain on U to its two restrictions
and homotopy zero; these signs are thus fixed by the original cone.
The local support cone O -> K has coordinates (o,b) and differential
(do,res(o)-db). Its map into (3.2) is

$$(o,b)\longmapsto(0,o,-b,0).\tag{3.3}$$

This is a chain map by direct substitution. On the other hand the
compact complex on U' has coordinates (a,s,l), with l the added
K-component. Its extension-by-zero map into (3.2) is

$$(a,s,l)\longmapsto(a,0,l,s).\tag{3.4}$$

It is the inclusion into the fiber of the map to O, and is the usual
j_! map. The boundary class partial'_v beta is (0,0,beta), so (3.4)
sends it to (0,0,beta,0), while (3.3) sends our signed local support
class (0,beta) to (0,0,-beta,0). This proves (3.1). ∎

This distinguishes the signed closed-point class on the original U
from the added signed boundary class on U'. In the usual positive-valuation
Gysin convention, g_v^std=-G_v and hence g_v^std=j_!partial'_v beta_y.
Both formulations are explicit; neither identifies the signed local
support representative with the canonical connecting map.

## 4. Exact Frobenius pairing, including the other sign

**[NEW] Lemma 4.1.** If chi is an unramified R-valued character of G_Qv
and pi_v is a uniformizer, then in the compact-first coefficient order

$$\operatorname{inv}_v(\delta(\pi_v)\smile\chi)
       =-\frac{\chi(F_v)}n\pmod{\mathbb Z}.\tag{4.1}$$

*Proof.* Choose r with r^n=pi_v and a continuous integer lift c(g) of
chi(g). Write d c(g,h)=c(g)+c(h)-c(gh), which is divisible by n.
The multiplicative one-cochain q(g)=r^{c(g)} satisfies

$$d q(g,h)=\delta(\pi_v)(g)^{c(h)}
                     \pi_v^{d c(g,h)/n}.\tag{4.2}$$

Therefore the class of delta(pi_v) cup chi in H^2(Q_v,G_m) is minus
the class represented by pi_v^{dc/n}. The latter is the unramified
cyclic class with invariant chi(F_v)/n: valuation sends its cocycle to
the integer Bockstein of chi/n, and the invariant is evaluation at
arithmetic Frobenius. This is the invariant convention in Milne ADT
I.1.5–I.1.6; (4.2) supplies the cup-order sign directly. ∎

**[NEW] Theorem 4.2.** For every z in H^1(U,V),

$$\boxed{\ \mathscr P(z,G_v(y))
           =\frac{\lambda_y(z_v(F_v))}{n}\pmod{\mathbb Z}.\ }\tag{4.3}$$

*Proof.* The projection formula for j_!, compact trace and cup product
reduces pairing with j_!partial'_v beta_y to the local invariant of
beta_y cup loc_v z. By (1.2), this class is delta(v) cup chi, where
chi=lambda_y composed with loc_v z. It is unramified since z extends
over U, and lambda_y is Galois equivariant. Lemma 4.1 gives its
negative Frobenius value. Proposition 3.1 supplies the second minus
sign. This proves (4.3) in precisely the old compact trace normalization. ∎

In particular this is a direct geometric representative of the
Frobenius functional on actual global cohomology. No perfect-duality
argument was used to select an unspecified representative with the
right value after the fact.

## 5. The finite toric value is paired with twice this class

Now take v among the fresh Kolyvagin primes from the reciprocity note:
v is inert in K, $a_v\equiv0$ and $v\equiv-1\pmod{p^k}$, and v does not divide 6NpDm.
Then F_v^2=1 on V and V=V_v^+ direct-sum V_v^- with both summands
free of rank one over R. Fix the same R-ISOMORPHISM lambda_v:V_v^+ -> R
as in that note. Weil duality gives a UNIQUE y_v in W_v such that
lambda_(y_v) is lambda_v on V_v^+ and zero on V_v^-.
Indeed V(-1) invariants are precisely the minus eigenspace with its
Tate coefficient, and the cross Weil pairing is perfect.

**[NEW] Corollary 5.1.** For the raw two-prime class and its actual
supersingular divisor and isogeny-cover function,

$$\boxed{\ \mathscr P(\kappa_{\mathbb Q},2G_v(y_v))
       =\frac{\psi_{v,k}(D_{v,m})}{p^k}
       =\frac{\psi_{v,k}(e_tD_{v,m})}{p^k}\pmod{\mathbb Z}.\ }\tag{5.1}$$

*Proof.* At the unramified quadratic local extension K_lambda/Q_v,
restriction changes the Frobenius value of a cocycle c to
c(F_v^2)=(1+F_v)c(F_v). Since lambda_(y_v) is Frobenius invariant,
its value is 2 lambda_(y_v)(c(F_v)). This is the ev_v value in the
reviewed finite-field reciprocity identity. Theorem 4.2 proves (5.1),
and the established e_t identity preserves the toric value. ∎

The division by p^k in (5.1) means the canonical embedding R into
p^(-k)Z/Z. Multiplication by 2 is a unit on all groups here. It is
separate from u_2=-1, which relates the standard two-prime system to
the RAW class used throughout this paper. For the standard class the
corresponding scalar and tensor generators must still be applied.

## 6. These actual closed-point classes generate the compact dual

We first reproduce generation under the extra full-image hypothesis
of the earlier detection proof, then REMOVE that extra hypothesis in
Theorem 6.3 below. Irreducibility is not asserted to imply full image.

### 6.1. Generation using the previously reviewed full-image argument

Temporarily assume rho_(E,p^k)(G_Q)=GL_2(R).

**[NEW] Theorem 6.1.** The classes G_v(y_v), as v ranges through the
fresh primes just specified (with any choice of each lambda_v), generate
H^2_c(U,V). A finite subset suffices. Their images therefore generate
both the strict finite Selmer dual and the dual of the actual invariant
Heegner defect subgroup.

*Proof.* Let z be a nonzero element of H^1(U,V) of exact order p^s.
The proof of Proposition 2.1 in the reciprocity note applies to this
class, not just to the particular Heegner class: central-scalar
cohomology vanishing injects it into the homomorphisms over Q(E[n]);
its translation image is p^(k-s)V. K remains disjoint from its finite
cocycle field by the same ramification and p-group argument. Choosing
h times complex conjugation yields a fresh prime with the K-local
Frobenius value of exact order p^s in the plus eigenspace. An isomorphism
lambda_v preserves that order. By (4.3), equivalently (5.1)'s factor-two
calculation for z, pairing z with G_v(y_v) is nonzero and has order p^s.

The subgroup generated by these closed-point classes thus has zero
annihilator under the already proved finite perfect duality. Its
quotient in H^2_c(U,V) has zero Pontryagin dual and so is zero. This
group is finite; successively adding a class outside the current span
therefore gives a finite generating subset. Passage to either existing
dual quotient preserves generation. ∎

The finite set depends on the curve, coefficient and ramification set.
There is no uniform cardinality, fixed integer test matrix, primary
finiteness or bound for Sha in this assertion.


### 6.2. Removing full image: the original irreducible O5 range suffices

**[THEOREM, primary homothety/cohomology input]** Let E/Q be an elliptic
curve, p>3, and suppose E[p] is irreducible. Then

$$H^1(G_k,E[p^k])=0\quad\text{for every }k\ge1,
\qquad G_k=\operatorname{Gal}(\mathbb Q(E[p^k])/\mathbb Q).
\tag{6.1}$$

This follows from Lawson–Wuthrich, *Vanishing of some Galois cohomology
groups for elliptic curves*, Lemmas 3 and 4. Lemma 4 supplies a nontrivial
residual homothety because the determinant is surjective over Q and an
irreducible group is not contained in a Borel; Lemma 3 gives vanishing
at every p-power. Root read the exact proofs in
[arXiv:1505.02940v2](https://arxiv.org/pdf/1505.02940), pp. 3–4
(the fetched PDF has a June 27, 2018 internal date), also available in
[the conference author copy](https://warwick.ac.uk/fac/sci/maths/people/staff/david_loeffler/jhc70/lawsonwuthrich.pdf).
No reducible exceptional case of their classification is imported.

**[NEW] Lemma 6.2.** Let a subgroup H of GL_2(Z/p^k) have irreducible
residual action. Every nonzero H-stable R-submodule W of V=R^2 has
W=p^tV for some 0<=t<k.

*Proof.* Choose t such that W is contained in p^tV but not p^(t+1)V.
Its image in p^tV/p^(t+1)V is a nonzero invariant subspace for the
residual action and therefore the whole two-dimensional space. Thus
W+p^(t+1)V=p^tV. The finite module p^tV/W satisfies pM=M; Nakayama's
lemma, or iteration p^kM=0, gives M=0. Therefore W=p^tV. ∎

**[NEW] Theorem 6.3 (full-coefficient detection without full image).**
In the original O5 setup, residual irreducibility alone suffices for:

1. exact-order detection of every class z in H^1(U,V) at infinitely
   many fresh primes v inert in K with $a_v\equiv0$ and $v\equiv-1\pmod{p^k}$;
2. generation of H^2_c(U,V) by the classes G_v(y_v), with a finite
   subset sufficient;
3. equivalence of the actual toric vanishing in (5.1) with theta_m=0.

In particular the stronger GL_2(Z/p^k) hypothesis is no longer needed
for these conclusions. This is an extension of the earlier project's
detection theorem, not a claim that the cohomology input is new.

*Proof.* Put L=Q(E[p^k]). Equation (6.1) makes restriction injective
from H^1(Q,V) to H^1(L,V). For a cocycle c representing a nonzero
class z of exact order p^s, the latter restriction is a homomorphism,
whose image W is stable under G_k. Lemma 6.2 gives W=p^tV. Its
exponent equals the order of the homomorphism and hence, by injectivity,
the order of z. Thus t=k-s, exactly as in the full-image argument.

Let L_c/Q be the finite Galois extension cut out by (c,rho). Then
Gal(L_c/L)=W is a p-group. The quadratic Heegner field K ramifies at
a prime of D, whereas L is unramified there because (D,Np)=1.
So K is not contained in L, nor in L_c: otherwise LK/L would have
degree two inside a p-extension. Since K is quadratic, K and L_c
are linearly disjoint over Q.

A complex conjugation tau has free rank-one plus and minus eigenspaces
on V. Its cocycle value is in the minus eigenspace, since tau^2=1.
Choose w in p^(k-s)V_tau^+ of exact order p^s. Disjointness lets us
choose h in G_(LK) with c(h)=w. The element gamma=h tau has
rho(gamma)=rho(tau), acts nontrivially on K, and satisfies

$$c(\gamma^2)=(1+\tau)(w+c(\tau))=2w.\tag{6.2}$$

Chebotarev in L_cK/Q supplies infinitely many fresh primes with that
Frobenius conjugacy class. They have trace zero, determinant minus
one modulo p^k, and inert K-Frobenius. The K-local value has exact
order p^s. Conjugating gamma changes the translation of gamma^2
by an invertible linear action, so this order statement is independent
of the Frobenius representative. The plus local eigenspace likewise
transforms naturally. This proves assertion 1.

Theorem 4.2 and the factor-two restriction calculation show that the
actual signed Gysin classes separate every nonzero z. Finite perfect duality
and finite generation then give assertion 2 exactly as in Theorem 6.1.
For the particular raw Heegner class, the reviewed finite-field cover
identity and (5.1) give assertion 3. Their construction needs the local
Frobenius conditions, which have now been supplied without full image. ∎

This extension is over Q with p>=5 and the ORIGINAL residual
irreducibility and Heegner-field assumptions. It does not extend to
reducible representations or arbitrary base fields by assertion.
It removes a restriction on detection; it does not prove O5 vanishing.

## 7. Actual global residue relations among the generators

Let T be any finite set of these fresh primes. Put U_T=U minus T.
For every v in T use the POSITIVE local residue

$$\operatorname{res}^{\rm tame}_v:
 H^1(U_T,V)\longrightarrow H^0(\mathbb F_v,V(-1))=W_v.\tag{7.1}$$

It is restriction followed by the support/Kummer residue, so
res_v^tame(y delta(v))=y. Let partial_S denote the compact boundary
on the original U. The following identity holds for actual global
classes, with no rank hypothesis:

**[NEW] Proposition 7.1.** For b in H^1(U_T,V),

$$\sum_{v\in T}G_v(\operatorname{res}^{\rm tame}_v b)
        =\partial_S(\operatorname{loc}_S b)
                  \quad\text{in }H^2_c(U,V).\tag{7.2}$$

More precisely, a tuple (y_v) has sum G_v(y_v)=partial_S(alpha) for a
specified alpha in the direct sum of S-local H^1 groups IF AND ONLY IF
there is a b in H^1(U_T,V) with those tame residues and
loc_S b=alpha.

*Proof.* Use the model (3.2), now with O and K the direct sums over T.
A tuple of residue classes is represented by the closed local cocycles
beta_v=y_v delta(v). Its Gysin sum is (0,0,-beta,0), and
partial_S(alpha) is (0,0,0,alpha). If their difference is a boundary
D(a,o,h,s), the equations say da=do=0,

    res_T(a)-res_T(o)-dh = -beta,
    res_S(a)-ds = -alpha.

The class b=-[a] has residue tuple y and S-localization alpha.
Conversely, given such b, choose a closed representative. At each
v in T, loc_v b-beta_v has zero tame residue. Local support exactness
identifies this kernel with the image of H^1(O_v,V). Choose closed
cochains representing these unramified classes, and cochain homotopies
for the difference. The analogous choice at S expresses loc_S b-alpha
as a coboundary. Substitution in (3.2), with a=-b and the matching
negated choices, makes (0,0,-beta,-alpha) a boundary. This proves the
if and only if, and taking the actual residue/localization of b gives
(7.2). ∎

In particular the kernel of the Gysin sum consists of actual residues
of global classes whose S-localizations are all zero. The local
trivializations needed by the compact cone have not been omitted.

Now let L_m be EXACTLY the boundary subgroup in the Heegner-duality
proof. Thus L_m=partial_S(A_S), where

$$A_S=\bigoplus_{u\in S_f\setminus\{\ell,q\}}
          E(\mathbb Q_u)/p^k
       \ \oplus H^1(\mathbb Q_\ell,V)
       \ \oplus H^1(\mathbb Q_q,V),\tag{7.3}$$

with the point groups embedded by Kummer. Define the actual global group

$$B_T=\{b\in H^1(U_T,V):\operatorname{loc}_S b\in A_S\}.\tag{7.4}$$

**[NEW] Corollary 7.2.** If T is a finite generating set from Theorem 6.3,
there is an exact presentation

$$B_T\xrightarrow{\operatorname{res}^{\rm tame}_T}
       \bigoplus_{v\in T}W_v
       \xrightarrow{\sum G_v}H^2_c(U,V)/L_m\longrightarrow0.\tag{7.5}$$

*Proof.* The second map is onto by Theorem 6.3. A tuple maps to zero
in the quotient exactly when its Gysin sum equals partial_S(alpha)
for some alpha in A_S. Proposition 7.1 characterizes exactly those
tuples as residues of the global classes (7.4). ∎

Thus the compact dual has an actual presentation by fresh closed-point
classes and global residue relations. The first group is arithmetic
cohomology with the stated local conditions; it is not a prescribed
free module. Its image is not known from rank-five analytic vanishing.
The presentation does not by itself lower the size of the dual.

## 8. What remains to prove

The preceding constructions identify the previous finite toric values
with actual generating geometric classes in the strict Selmer dual,
including the explicit SIGNED boundary/Gysin convention, factor two,
and their global residue relations.
They do not prove that the Heegner class evaluates to zero on those
generators. The extra full-image condition has been removed by Theorem 6.3; all
original irreducible O5 hypotheses remain.

**[GAP Gysin-TP5, equivalent to LR-TP5 in its stated range].** Under the
full original O5 hypotheses, show that the functional

$$\bigoplus_{v\in T}W_v\longrightarrow p^{-k}\mathbb Z/\mathbb Z,
\qquad (y_v)\longmapsto\sum_v\mathscr P(\kappa_{\mathbb Q},G_v(y_v))
\tag{8.1}$$

is identically zero, for a finite generating T from Theorem 6.3.
It already annihilates the actual residue subgroup in (7.5), because
kappa_Q is strict Selmer. That known annihilation is merely the descent
of (8.1) to the dual quotient; it is not zero on the entire source.
The additional untwisted analytic derivatives must be compared with
these values, not only with their existing reciprocity relations.

A concrete next test is to insert actual higher even-index Kolyvagin
classes into B_T and compute their residues with the already audited
finite-singular scalars. Whether those relations carry additional
rank-sensitive information remains to be determined. The universal
BSD rank statement, full Sha finiteness and exact leading formula are
not proved or disproved by this construction.
