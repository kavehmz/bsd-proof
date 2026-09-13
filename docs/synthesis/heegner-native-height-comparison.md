# The native Heegner scalar as an actual isogeny Cassels–Tate value

Date: 2026-09-12. Owner /root/uniform_witness, GPT-6 Astra/xhigh.
**Completed bounded construction, independently reviewed PASS** in
[review-heegner-native-height.md](review-heegner-native-height.md).
All seven sections, including the separate norm-Prym point subcase,
passed against mathematical revision
75370e6e4a132e2b0311991e421770fbe97db56c2c030aed9c48ad213ab5c693.
Subsequent status and review-link changes are editorial.
Restart: [checkpoint](heegner-native-height-checkpoint.md).
The objective remains full BSD for elliptic curves over Q.

We construct abelian varieties and isogenies whose local Kummer
conditions are exactly the previously constructed native conditions.
The particular remaining scalar becomes a classical Cassels–Tate
pairing of two specified torsors on one of these abelian varieties.
We then test a geometric transport of the integral Kato class into
that variety: the needed finite-coefficient inclusion does not
extend to any nonzero elliptic homomorphism. The extra complex zero
has not been shown to annihilate the constructed torsor pairing.

## 1. Exact inputs, without rebuilding the finite evaluator

Use the [native proof](heegner-native-pairing-attack.md) and its
[independent review](review-heegner-native-pairing.md).
Write n=p^k, R=Z/n, M=E[n], M_D=M tensor epsilon_K.
The hypotheses include good ordinary nonanomalous p>=5,
the stated surjective image and p-unit Manin range for the actual
d0, all primes of Np split in the imaginary quadratic K,
L(E^D,1) nonzero, and the additional p not dividing h_K.
The O5 complex input is ord_(s=1)L(E,s)>=5.
For i in {ell,q}, let F=F_i/K be the actual cyclic p-part of
the ring-class extension, of degree p^e, e=v_p(i+1)>=k.
F/Q is dihedral of degree2p^e.
The actual inverse-Artin coordinate a_i has tame value -1.

The first-order quotient is the specified sequence
$$
 {\cal E}_i:\quad
 0\longrightarrow M_D\xrightarrow{\iota}N_i
       \xrightarrow{\pi}M\longrightarrow0 ,
 \qquad
 g(z,t)=(gz,\epsilon_K(g)gt+a_i(g)gz).
 \tag{1}
$$
This is a quotient of the actual induced regular module;
no new extension class is substituted.
Keep the fixed cofactor classes A,B and actual input
$$
 z=d_0{\cal P}_{A,B}(w_k).
 \tag{2}
$$
The existing theorem gives a global first lift (z,t_i) and
native local lifts (z_v,tau_i,v). All finite places of
S={v:v divides NpD ell q}, and the real Tate convention, are kept.

For a single normalized test b_i and scalar R_i use the clean
additional hypotheses
$$
 p\nmid\operatorname{Tam}(E),\qquad
 \operatorname{Sel}_n(E^D/\mathbb Q)=0.
 \tag{3}
$$
Then d0 is a proved p-unit, but it is not deleted from(2).
The already constructed test has local condition J_i,v=F_v
away from i and J_i,i=H_tr^1(Q_i,M_D), with
$$
 \operatorname{loc}_i(b_i)=\beta_i=-a_i\otimes t_i^+,\qquad
 {\cal R}_i(z)=B_i(\eta_i,\beta_i),\qquad
 B_v(x,y)=n\,\operatorname{inv}_v e_n(x\cup y).
 \tag{4}
$$
Here eta_i is the finite difference after the existing unique
global correction C. Compact coefficients occur FIRST in e_n.
No reconstruction of C, its bordered determinant, or the
p-generator is needed below.

The geometric construction in §§2–4 also works without(3):
use the actual J_i,v and every test in their exact dual Selmer
group, instead of pretending that group is one free R-line.
The preceding d0 theorem is used only in its stated image,
period and Tamagawa scope. If v_p(d0)>=k, the actual input(2)
is zero; no unscaled class is recovered.

## 2. Realization by two actual isogenies

Put
$$
 {\cal A}=\operatorname{Res}_{F/\mathbb Q}(E_F).
 \tag{5}
$$
It is an abelian variety of dimension2p^e. Over Qbar it is
the product of copies of E indexed by embeddings of F.
Its n-torsion is the induced regular coefficient module.
Let
$$
 \rho:{\cal A}[n]\twoheadrightarrow N_i,\qquad
 {\cal K}=\ker\rho
 \tag{6}
$$
be the fixed actual coefficient quotient of(1).
Both are finite etale group schemes over Q. Define
$$
 {\cal B}={\cal A}/{\cal K},\quad q_1:{\cal A}\to{\cal B},
 \quad \psi:{\cal B}\to{\cal A},\quad
 \psi q_1=[n]_{\cal A}.
 \tag{7}
$$
The quotient exists and [n] descends because it kills K.
Its kernel is canonically A[n]/K=N_i, via q1.
In particular deg(psi)=n^4.

For the existence/descent input one may use
[Milne, Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf),
Chapter I Remark8.12 and Chapter IV Lemma2.1
(172-page primary author text, PDF pp.44 and140).
The Weil restriction here can also be constructed directly by
Galois descent of the product just described; the product
polarization descends and gives projectivity.

Now quotient B by its subgroup iota(M_D) inside ker(psi):
$$
 {\cal C}={\cal B}/\iota(M_D),\qquad
 \psi_1:{\cal B}\to{\cal C},\qquad
 \psi_2:{\cal C}\to{\cal A},\qquad \psi=\psi_2\psi_1 .
 \tag{8}
$$
Then
$$
 \ker\psi_1=M_D,\qquad \ker\psi_2=M,\qquad
 \deg\psi_1=\deg\psi_2=n^2.
 \tag{9}
$$
The identification of ker(psi2) with M uses EXACTLY pi in(1).
Thus the kernel sequence of this factorization is(1), with
its fixed coordinates, not merely an isomorphic unmarked sequence.

For any place v and isogeny f:X→Y set
$$
 W_{f,v}=\operatorname{im}\bigl(Y(\mathbb Q_v)
          \xrightarrow{\delta_f}H^1(\mathbb Q_v,X[f])\bigr)
        =\ker\bigl(H^1(\mathbb Q_v,X[f])
                             \to H^1(\mathbb Q_v,X)\bigr).
 \tag{10}
$$

**[NEW] Proposition2.1.** The native Shapiro point condition on
N_i is W_psi,v. Its exact preimage J_i,v is W_(psi1),v,
and its image in M is W_(psi2),v.

*Proof.* Naturality of the diagram with top multiplication[n]
on A and bottom psi gives
delta_psi(P)=rho_*(delta_n(P)) for every P in A(Q_v).
Under Shapiro, A(Q_v) is the product of the actual local
point groups E(F_w), not the diagonal of that product.
Consequently its image is precisely the native condition.

The two compositions M_D→N_i→B and M_D→B are identical.
Taking kernels of the maps on H1 into H1(Q_v,B) gives
iota^(-1)W_psi,v=W_(psi1),v. This argument retains the
H0 connecting terms; it does not mistake an H1 injection
for an injective coefficient map.

Finally psi1 sends delta_psi(P) to delta_(psi2)(P).
Both connecting maps use ALL P in A(Q_v), so
pi(W_psi,v)=W_(psi2),v. Square.

At the ramified prime i, the already checked native image
is zero. Thus W_psi,i=0 and W_(psi2),i=0, while
W_(psi1),i is the nonzero transverse line. There is no
contradiction: the latter maps to zero in H1(N_i) through
the actual H0 boundary in(1).
In the clean case the remaining J_i,v are exactly the
previous finite conditions. In the nonclean case(10)
retains their actual component and local image defects.
No universal-norm surjectivity is being imposed.

## 3. The test and input give torsors on C and its dual

The local Kummer condition of the dual isogeny is the exact
annihilator of(10). This is
[Morgan–Smith2103.08530v2, Proposition6.1](https://arxiv.org/html/2103.08530v2),
with no Sha finiteness hypothesis.
The dual finite-group identification is also Milne,
Chapter I Theorem9.1: ker(f^dual) is the Cartier dual of ker(f).

Define the marked dual identification
$$
 \lambda_D:M_D\longrightarrow M_D^\vee,\qquad
 \lambda_D(b)(m)=e_n(m,b).
 \tag{11}
$$
This order is deliberate. Let b_i^vee=lambda_D(b_i).
Proposition2.1 and local duality prove
$$
 z\in\operatorname{Sel}^{\psi_2}({\cal C}),\qquad
 b_i^\vee\in\operatorname{Sel}^{\psi_1^\vee}({\cal C}^\vee).
 \tag{12}
$$
The first assertion uses the established native LOCAL lifts
of the particular z; global native compatibility is not
assumed. The second uses J_i,v perpendicular, including the
transverse condition at i.

Push these finite cocycles through their actual kernel
inclusions. This constructs
$$
 \begin{split}
 \xi_i(z)&\in\operatorname{Sha}({\cal C}/\mathbb Q)[\psi_2],
       &&\xi_i(z)= [\,M\hookrightarrow{\cal C}\,]_*(z),\\
 \upsilon_i&\in\operatorname{Sha}({\cal C}^\vee/\mathbb Q)
                                  [\psi_1^\vee],
       &&\upsilon_i=[\,M_D^\vee\hookrightarrow{\cal C}^\vee\,]_*
                                                     (b_i^\vee).
 \end{split}
 \tag{13}
$$
They are locally trivial because of(12). Both are killed by n.
Either may be zero or nonprimitive; no nonzero Sha class
is asserted. This is an actual torsor construction by Galois
descent, on the isogeny quotient C, not on the rank-zero E^D.

The point kernels in this construction are exactly
$$
 \begin{split}
 0&\to{\cal A}(\mathbb Q)/\psi_2{\cal C}(\mathbb Q)
       \to\operatorname{Sel}^{\psi_2}{\cal C}
       \to\operatorname{Sha}({\cal C})[\psi_2]\to0,\\
 0&\to{\cal B}^\vee(\mathbb Q)/
                         \psi_1^\vee{\cal C}^\vee(\mathbb Q)
       \to\operatorname{Sel}^{\psi_1^\vee}{\cal C}^\vee
       \to\operatorname{Sha}({\cal C}^\vee)[\psi_1^\vee]\to0 .
 \end{split}
 \tag{14}
$$
These follow from the isogeny Kummer exact sequences and
localization. They supply concrete sufficient targets:
an actual point preimage for z or b_i^vee makes the
corresponding torsor zero. Rank zero of E^D does not
compute either point quotient in(14).

## 4. Exact classical Cassels–Tate comparison, including its sign

Use the convention of
[Morgan–Smith2103.08530v2, Definition3.2 and §6.1](https://arxiv.org/html/2103.08530v2).
The primary version is dated26June2022.
Its decorated exact sequence requires the preimage and image
equalities of local conditions, precisely those proved in
Proposition2.1. Its isogeny comparison in §6.1 identifies
the pairing with the classical Cassels–Tate pairing on
Sha(C) times Sha(C^dual). Neither group is assumed finite.

**[NEW] Theorem4.1.** Under(3), the actual native scalar is
$$
 \boxed{\quad
  \frac{{\cal R}_i(z)}{n}
       =-\operatorname{CT}_{\cal C}
                       \bigl(\xi_i(z),\upsilon_i\bigr)
             \quad\text{in }(1/n)\mathbb Z/\mathbb Z .
       \quad}
 \tag{15}
$$

*Proof.* Choose the established GLOBAL cocycle
f=(z,t_i^natural) in N_i, and local native cocycles
f_v=(z_v,tau_i,v). In Morgan–Smith Definition3.2 one may
take the degree-two primitive epsilon=0 because df=0.
The local difference f|v-f_v is
iota(t_i^natural|v-tau_i,v)=-iota(eta_v).
Their coefficient evaluation with b_i^vee is, by(11),
exactly e_n(-eta_v,b_i,v), with the first coefficient
in the project's compact-first position.
Away from i the finite/finite invariants vanish.
At i the invariant is -R_i(z)/n. This proves the
finite-module equality with its sign. The isogeny
factorization(8) and the primary §6.1 identify it
with the classical torsor pairing(13). Square.

The geometry in §§2–3 and the first equality with the full
sum of local compact terms remain valid without(3).
Only the reduction to one R-generator and one old
coordinate uses the clean hypotheses.

The exact point transport from the native proof is unchanged:
the twist CLASS map is A=u_iota^(-1)iota_* and its point-dual
map is A^(-dagger)=u_iota iota_*.
Evaluation(11) preserves that contragredient dictionary.
In particular (e_p,z_D0)=d0 and the p-local term is not
renormalized or discarded in passing to(15).
Linearity retains d0 in xi_i(d0 P_(A,B)(w_k)).
Outside the clean case, the unscaled P_(A,B)(w_k) need
not even satisfy the native image condition on M.

Base-changing BOTH torsors/tests from Q to K multiplies(15)
by2. This follows directly by restricting the cochains:
at each nonsplit place the Brauer invariant is multiplied
by the local degree, and at split places the two equal
terms are summed. At infinity odd-primary Tate groups vanish.
Thus the Q value is half the K value, consistently with
kappa_Q=cor_(K/Q)(kappa_K)/2. Tame inertia itself acquires
no extra factor2. The existing raw/standard scalar u_2=-1
for the two-prime top class is unrelated to the minus in(15),
which comes from global-minus-local in the CTP definition.

## 5. Testing an elliptic height transport on these actual varieties

A tempting use of(15) is to claim that w0 comes from the
integral Tate-module Selmer group, so its image is automatically
divisible in Sha(C) and hence pairs to zero. Such a statement
needs a compatible map at all p-power coefficients. We test
the most direct geometric candidate: extend the coefficient
inclusion M=ker(psi2)→C to an elliptic homomorphism E→C.

Let t:A→E be the norm (sum on geometric factors), j:E→A
the diagonal, and P0=ker(t). The geometric sum map has
connected kernel, so P0 is an abelian variety. In the
fixed sum/difference basis e_+=e_1+e_2, the plus coordinate
is half the sum of the two induced coordinates. Hence
$$
 \pi\rho=\tfrac12\,t|_{{\cal A}[n]}.
 \tag{16}
$$
The factor1/2 acts only on the finite odd-primary coefficients.
It is not asserted to be a morphism of abelian varieties.
Using the alternative normalized basis changes this identity
by its explicit p-unit and leaves the following kernel equalities
unchanged.
Therefore the composite q2=psi1 q1 is the actual quotient
$$
 {\cal C}={\cal A}/P_0[n],\qquad
 \psi_2q_2=[n]_{\cal A},\qquad
 q_2\psi_2=[n]_{\cal C}.
 \tag{17}
$$
All these are integral geometric maps.

**[NEW] Proposition5.1.** No Q-homomorphism h:E→C has a
nonzero restriction E[n]→ker(psi2). In particular the marked
inclusion of M in(13) cannot be the restriction of such an h.
The same assertion holds for homomorphisms with denominators
prime to p.

*Proof.* The surjective-image range is non-CM, so
End_F(E)=Z. Weil-restriction adjunction gives
Hom_Q(E,A)=Z j. Since tj=[2p^e] and n divides p^e,
j(E[n]) is contained in P0[n].
Thus q2 j kills E[n] and factors uniquely through [n]:E→E:
$$
 q_2j=j_0[n]\quad\text{for some }j_0:E\to{\cal C}.
 \tag{18}
$$
Composing with psi2 gives psi2 j0=j, since multiplication
by n is surjective and Hom groups are torsion-free.

For any h:E→C write psi2 h=m j, m an integer.
Then(17) gives
n h=q2 psi2 h=m q2 j=m n j0, so h=m j0.
If h(E[n]) is contained in ker(psi2), then m j is zero
on E[n]. The diagonal j is injective, so n divides m.
It follows that h itself is zero on E[n].
Clearing a denominator prime to p proves the last assertion.
Square.

This is a calculation on the constructed abelian varieties,
not an abstract countermodel. Inverting a p-isogeny rationally
does not extend its marked finite kernel inclusion.
An integral Selmer class for E consequently cannot be
transported into the divisible subgroup of Sha(C) merely
by invoking an elliptic map which does not exist.
The proposition does not rule out a more elaborate
correspondence, a complex of motives, or a new arithmetic
construction. It specifies the failure of this attempted one.

### 5.2. An explicit norm-Prym torsor when the input comes from a point

This subsection is a SUBCASE, not a claim that the actual z in(2)
comes from a rational point. Suppose z=Kum_n(P), P in E(Q),
and suppose z satisfies the native image conditions as before.
Let
$$
 \partial_t:E(\mathbb Q)\longrightarrow H^1(\mathbb Q,P_0)
 \tag{18a}
$$
be the torsor boundary of the ACTUAL norm sequence
0→P0→A→E→0. The restriction of q2 to P0 factors as
q2|P0=j_P[n], where j_P:P0→C is a closed immersion.
This gives the pushout sequence
0→P0→C→E→0 obtained by multiplying the P0 term by n.

**[NEW] Proposition5.2.** With the half-norm convention(16),
$$
 \xi_i(\operatorname{Kum}_n P)
        =-j_{P,*}\partial_t(2P)\quad\text{in }H^1(\mathbb Q,C).
 \tag{18b}
$$
The torsor on the right is locally trivial AFTER this push,
but the norm torsor partial_t(2P) itself is not asserted to
belong to Sha(P0). The exact local point conditions are
$$
 2P\in t{\cal A}(\mathbb Q_v)+nE(\mathbb Q_v)
                 \quad\text{at every }v.
 \tag{18c}
$$
Moreover xi_i(Kum_n P)=0 if and only if the corresponding
GLOBAL congruence
2P in tA(Q)+nE(Q) holds.

*Proof.* The map from ker(psi2) to E[n] induced by the norm
on C is twice its marked identification with M, by(16).
Thus the psi2 Kummer class of a point Q_A in A(Q_v) is
half the ordinary n-Kummer class of t(Q_A).
This proves(18c); the same argument and the first exact
sequence(14) give the assertion about a zero global torsor.

For the sign and torsor identity, choose Q in E(Qbar) with
nQ=P, and choose a in A(Qbar) with t(a)=Q.
Then na lies in the norm fiber above P and
g mapping to g(na)-na represents partial_t(P).
For every g choose r_g in P0(Qbar) with
n r_g=g(na)-na. The element
u_g=ga-a-r_g belongs to A[n] and has norm gQ-Q.
Its image under q2 is independent of the choice of r_g.
The marked inclusion of the cocycle gQ-Q from M into C is
2q2(u_g), because of(16). Hence that cocycle in C is
$$
 2d(q_2a)-2j_P\,d(na).
$$
In cohomology this is -j_P partial_t(2P), proving(18b).
The assumed native local conditions give its local
triviality; they need not make partial_t(2P) locally zero.
The construction uses only finite algebraic point choices.
Square.

Combining(15) and(18b) gives the concrete point-subcase value
$$
 \frac{{\cal R}_i(\operatorname{Kum}_n P)}{n}
    =\operatorname{CT}_{\cal C}
                 \bigl(j_{P,*}\partial_t(2P),\upsilon_i\bigr).
 \tag{18d}
$$
Thus an attempted rational-point comparison leaves an actual
norm-Prym torsor, with a global norm congruence as a sufficient
vanishing construction. The local congruences(18c) are not
silently upgraded to a global norm theorem for an abelian variety.
If a point P is used for the ACTUAL input, its full d0 and
cofactor multiplicities must first be included in that point
class. No rational-point premise for w0 or z has been supplied.

## 6. The finite tame direction is not a cyclotomic height coordinate

I checked
[Howard1202.6343v1, Theorem2.5](https://arxiv.org/html/1202.6343v1)
and the new primary
[Macias Castillo–Sano2603.23978v1, Hypothesis4.1 and Theorem4.2](https://arxiv.org/html/2603.23978v1),
dated25March2026. The latter proves a BD/Nekovar height comparison
for ordinary Selmer complexes over a Z_p-extension, with its
own explicit minus sign. These theorems do not identify an
untwisted complex central derivative with the finite pairing(15).
Howard's test belongs to the propagated height Selmer condition;
the actual b_i is transverse at the old prime.

There is an exact local obstruction to obtaining our a_i
by reduction of a torsion-free Z_p-extension character.
At the old place of K the residue cardinality is i².
For tame inertia sigma and arithmetic Frobenius Frob,
Frob sigma Frob^(-1)=sigma^(i²).
An additive abelian Z_p-valued character chi consequently
satisfies
$$
 (i^2-1)\chi(\sigma)=0,\qquad\text{hence }\chi(\sigma)=0 .
 \tag{19}
$$
But a_i(sigma)=-1 modulo n.
The finite ramified character exists because
v_p(i²-1)=v_p(i+1)=e>=k; it has no such Z_p lift.
Finite augmentation Bocksteins are still legitimate,
but their existence supplies no analytic cyclotomic derivative.
This is separate from the previously completed local point-norm
failure, which is not being rerun.

The actual isogeny quotient C also retains the other arithmetic
constituents of the ring-class field. Since it is isogenous to A,
its complete Hasse–Weil L-function is
$$
 L({\cal C}/\mathbb Q,s)=L(E/F,s)
   =L(E/\mathbb Q,s)L(E^D/\mathbb Q,s)
      \prod_{\{\chi,\chi^{-1}\},\ \chi\ne1}
                    L(E/K,\chi,s)^2 .
 \tag{20}
$$
This follows from the regular representation of the actual
dihedral Galois group: its two one-dimensional representations
occur once, and each two-dimensional induced representation
occurs twice. All nontrivial characters here have conductor i
over K; the extension is totally ramified at i and unramified
elsewhere. Equation(20) uses complete local factors, including
ramified ones, rather than omitting an Euler factor and later
canceling its possibly nonunit augmentation.

The extra untwisted central zero is a zero of the E factor
in(20). Our torsors(13) have not been projected out of the
other constituents by a geometric map. Proposition5.1
demonstrates why the marked finite inclusion cannot be
replaced by the obvious elliptic summand map.
No new Gross–Zagier height formula for these torsors follows
from(20), and no analytic rank statement for C proves that
its Cassels–Tate value is zero.

## 7. The precise remaining arithmetic comparison

The operation carried out is
$$
 (z,b_i)
 \longmapsto
 (\xi_i(z),\upsilon_i)
 \longmapsto
 \operatorname{CT}_{\cal C}(\xi_i(z),\upsilon_i)
       =-{\cal R}_i(z)/p^k.
 \tag{21}
$$
Every object and map is defined from the actual finite
ring-class quotient, native points and corrected Kato class.
There is no unnamed lift on which a height is evaluated.
The residual term is the pairing of the two specific
isogeny torsors(13), not an unspecified element of a
formal norm-relation module.

One sufficient new arithmetic construction would put
xi_i(d0 P_(A,B)(w_k)) in the divisible subgroup of Sha(C),
or construct an actual point preimage in the first sequence(14).
Another would do the corresponding operation for upsilon_i.
A weaker construction need only prove their specific
Cassels–Tate orthogonality from L'''(E,1)=0.
None has been established here. Finite Sha(E), finite Sha(C),
or a p-adic third-coefficient identity is not an input.

Even if these two particular pairings vanish for ell and q,
the reviewed mixed coset and its genuine Heegner top
ambiguity remain. The geometric realization of the FIRST
obstruction does not select that mixed/top class.
The full BSD objective, O5 and NP-TP5 remain open.

Primary versions and scopes are recorded at their uses.
No old mathematical script was rerun, no extra agent was
created, and no shared synthesis file was changed.
