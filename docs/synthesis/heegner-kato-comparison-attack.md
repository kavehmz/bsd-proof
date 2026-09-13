# Actual cyclotomic and tame jets in the Heegner–Kato comparison

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-kato-comparison.md](review-heegner-kato-comparison.md).
All eight sections and the old-prime cup map were checked against
mathematical revision
84297adc102effbcc5a1d92bafef70330b832bd970c58b31913555e72aa0a64e.
Subsequent header/checkpoint changes are editorial.
Restart: [checkpoint](heegner-kato-comparison-checkpoint.md).
The objective remains full BSD for every elliptic curve over Q.

This note constructs an integral second cyclotomic Kato derivative,
its exact weighted Beilinson–Flach specialization, and finite local
cofactor maps to the strict group containing the actual two-prime
Heegner class. It then constructs the actual two-variable tame
coefficient representation and computes its lifting obstruction.
None of these constructions proves rank-five vanishing.

## 1. Objects and fixed normalizations

Use the O5 hypotheses and the fixed modular parametrization of the
[reviewed higher-residue note](heegner-higher-residue-attack.md):
E/Q is non-CM, p>=5 is good ordinary, E[p] is irreducible,
its complex analytic rank is odd and at least five, and K has odd
discriminant D prime to Np, with all primes of Np split and
L(E^D,1) nonzero. Put m=ell q, k=M(m), R=Z/p^k, T=T_pE,
and V=T tensor Q_p. The old primes ell,q are inert Heegner
Kolyvagin primes at the full exponent k.

Write
$$
 \kappa=\kappa_{m,\mathbb Q}^{\rm raw}
  =\tfrac12\operatorname{cor}_{K/\mathbb Q}
       \kappa_{m,K}^{\rm raw}\in
 \mathcal S=\operatorname{Sel}_{p^k}(E/\mathbb Q)
                 _{\operatorname{loc}_\ell=\operatorname{loc}_q=0}.
 \tag{1}
$$
The raw class has plus conjugation sign. The standard class is
u_2 kappa=-kappa; u_r=(-1)^{r(r-1)/2}. No coefficient Frobenius
is applied as if it were a global equivariant operator.
For a fresh detecting prime v and its fixed plus functional lambda_v,
set
$$
 b_v(z)=\lambda_v(z(F_v)),\qquad
 a_v(z_K)=2b_v(z).
 \tag{2}
$$
In the signed compact convention already reviewed,
pairing z with G_v(y_v) is b_v(z)/p^k. The factor two in (2)
belongs to Frobenius restriction, not to tame inertia residues.

For the most explicit integral Kato normalization below we work
first in the additional **nonanomalous range**
a_p(E) not congruent to 1 modulo p, and use the modular lattice
T_f of BCGS Section 3.1.2. Irreducibility excludes rational
p-isogenies, so a minimal isogeny from its elliptic curve E_bullet
to E has degree prime to p. Fix that isogeny and the resulting
Tate-module identification. Its differential and period scalars
are fixed, not discarded. Equivalently one may take E=E_bullet.
Indeed, a nonzero p-primary kernel of a minimal isogeny would
either contain a G_Q-stable line in E[p], contradicting
irreducibility, or contain all E[p], in which case factoring
through multiplication by p contradicts minimality.
The finite Heegner and tame constructions themselves need no
nonanomalous condition.

Fix Gamma=Gal(Q_infinity/Q), gamma with cyclotomic character
chi_cyc(gamma)=1+p, and X=gamma-1. Iwasawa cohomology means the
inverse limit with corestriction. In its cochain realization
the coefficient action is rho_T(g)Psi(g)^{-1}; this declares the
inverse-character convention. Mellin evaluation sends X to
(1+p)^t-1. If using a positive-character cochain convention,
apply the involution X mapsto (1+X)^{-1}-1 throughout.

Let z_infinity be the actual integral Kato class and F_E(X) its
ordinary Coleman image. The integral construction and exact
reciprocity normalization are
[BCGS2312.09301v2, Theorem 3.2.2](https://arxiv.org/html/2312.09301v2#S3.SS2.SSS2).
Fix its remaining period/unit choices once. With Neron periods
and the corresponding Coleman map,
$$
 F_E(\chi)=
 \frac{p^r}{\tau(\bar\chi)\alpha^r}
       \frac{L(E,\bar\chi,1)}{\Omega_E^+}\quad(r>0),\qquad
 F_E(0)=(1-\alpha^{-1})^2\frac{L(E,1)}{\Omega_E^+},
 \tag{3}
$$
where r is the primitive cyclotomic conductor exponent and
alpha is the unit root of Z^2-a_pZ+p.
Use the analogous fixed normalization z_D,F_D for E^D.
For comparison with the induced representation, transport z_D
by the twist isomorphism normalized on the differential, as in
BDV Section 4.3: if iota sends omega_D to u_iota omega_E,
the transported class is u_iota^{-1} iota_*(z_D).
We retain this isomorphism in every occurrence of z_D below.
The Coleman map on that factor is transported with it.

Thus d_0=F_D(0) is nonzero, but **need not be a p-adic unit**.
Changing to an integral smoothed Kato class multiplies both z
and its Coleman image by the same specified smoothing series.
All following identities then acquire those same factors;
one cannot divide them modulo p^k. Likewise no division by
the modular degree d_pi is made: the same pi defines y_m,
its cofactor B_2, and the elliptic realization used here.

## 2. A genuine integral second Kato derivative without finite Sha

**[NEW] Proposition 2.1.** In the stated range,
$$
 z_\infty=X^2w_\infty,\qquad
 w_0\in\operatorname{Sel}(\mathbb Q,T),\qquad
 F_E(X)=X^3C_E(X).
 \tag{4}
$$
Division by X^2 is unique. In particular w_0 has a well-defined
image w_k in the full finite point-Kummer Selmer group.
These statements allow w_0=0 and C_E(0)=0.

*Proof.* Put H^i=H^i_Iw(Q_infinity,T), using the full
Galois complex with S_0 containing Np and infinity.
Kato's groups in Sections8.2/12.2 are initially defined
using j_*T on the cyclotomic integer scheme with p removed.
We first compare these two complexes at (X).

For a bad finite v not p, H^0(Q_v,V)=0 because the
local p-primary torsion on E(Q_v) is finite. Local
self-duality gives H^2(Q_v,V)=0, and local Euler
characteristic gives H^1(Q_v,V)=0. The unramified
complex R Gamma(F_v,V^{I_v}) is acyclic as well:
F_v-1 is an isomorphism on this finite-dimensional
space because its invariant subspace is H^0(Q_v,V)=0.
The localization triangle comparing j_* with Rj_*
has the higher-inertia term
R Gamma(F_v,H^1(I_v,V))[-1]; the preceding statements
and the inertia spectral sequence show that this
term is acyclic. At Iwasawa level the corresponding
bounded local complexes have finitely generated
cohomology, and their derived specialization at (X)
has this acyclic rational fiber. Derived Nakayama
over the DVR Lambda_(X) makes their localization
acyclic. Equivalently their local Euler polynomials
have nonzero value at the augmentation.

Thus Kato's complex and the full Galois complex are
isomorphic after localization at (X). Kato12.4 gives
rank one and torsion-freeness of H^1 there, and torsion
of H^2. Kato12.5(3) bounds length H^2 by length H^1/Z(f).
Its exceptional local term is absent at good p. The conjugation
identity12.5(1), after the Tate twist, makes the minus Betti
coefficient vanish on the trivial finite cyclotomic branch.
The chosen nonzero plus coefficient therefore generates
Z(f) over Lambda_(X). This applies the length bound to the
actual z_infinity, not to an arbitrary characteristic generator.
Only this rational height-one bound is used; the integral
big-image condition12.5(4) is not being imported.
Any difference between the chosen primitive and S-truncated
Kato normalization has nonzero Euler value at X=0 and hence
is a unit at Lambda_(X); it does not change this length.

For odd p the relevant global p-cohomological dimension is two.
Finite p-power cohomology and the Mittag–Leffler property give
derived Iwasawa base change in these degrees, in particular
$$
 H^2/XH^2=H^2(G_{\mathbb Q,S_0},T),\qquad
 H^1/XH^1\hookrightarrow H^1(G_{\mathbb Q,S_0},T).
 \tag{5}
$$
The inverse-limit finite Selmer group injects into the latter
group and has Z_p-rank s_p(E)>=3 by the reviewed odd-rank
theorem. This rank includes any divisible Sha contribution.
The global Euler characteristic of V is -1, and H^0(V)=0;
hence H^2(G_Q,S_0,V) has dimension at least two.
The first formula in (5) makes length H^2_(X) at least two.
Thus z_infinity is X^2-divisible at (X).

The target of the injection in (5) is Z_p-torsion free:
its torsion is supplied by E(Q)[p-infinity], which is zero.
If an integral class becomes X-divisible at (X), an element
s outside (X) kills its image in that target. There it acts
by the nonzero scalar s(0), so the image is zero. This proves
integral X-divisibility. Apply the same argument to the
integral quotient once more. The coefficient exact sequence
and H^0(G_Q,T)=0 give H^1[X]=0, proving uniqueness.

Kato18.4 gives ord_X F_E>=s_p(E), hence at least three.
This is a Selmer-corank inequality, not a comparison with
complex analytic order. The ordinary Coleman map at X=0
is a nonzero scalar times the Bloch–Kato dual exponential.
Since Col(w_infinity)=F_E/X^2 is divisible by X, w_0 is
finite at p. At every finite v not p, H^1(Q_v,V)=0 and
H^1(Q_v,T) is precisely the p-adic completion of E(Q_v):
the local Weil–Chatelet p-primary group is finite, so its
Tate module is zero. Thus w_0 has point-Kummer local conditions.
The odd-p real condition is zero. Reduction of an integral
point-Kummer class lies in the full finite Kummer condition,
which proves the assertion about w_k. No Sha finiteness or
rational-point basis has been used. Square.

This argument extends the already reviewed first-derivative
construction to the actual non-CM class and corank lower bound.
It supplies order two, not the additional order needed at
complex analytic rank five.

## 3. The actual Beilinson–Flach second and third coefficients

Use the **published 50-page version** of
[Bertolini–Darmon–Venerucci, Advances398(2022),108172](https://www.math.mcgill.ca/darmon/pub/Articles/Research/77.BDV/bdv-advances.pdf).
Its Theorem4.2 is a global Iwasawa-cohomology comparison,
not just an identity of logarithms. The auxiliary CM family
specializes to Eis_1(epsilon_K); fix its induced-representation
isomorphism gamma. In its basis put e_+=v_g^++v_g^- and
e_-=v_g^+-v_g^-.

Let B_c denote the source's p-stabilized specialization of its
actual smoothed Beilinson–Flach class. Precisely, if sp denotes
the weight-(2,1) and modular-form specialization, then
$$
 \operatorname{sp}({}_c{\rm BF})
   =E_\alpha B_c,\qquad
 E_\alpha=\alpha(p-1)(1-\alpha^{-2})(1-p^{-1}\alpha^{-2}).
 \tag{6}
$$
The source's exact scalar is A_c=A M_c, where A is its
Rankin factorization unit, fixed by its interpolation periods,
and, on the branch s=t,
$$
 M_c(t)=\pm(c^2-c^{2t+1}\epsilon_K(c)),\qquad
 \Omega_{g,\gamma}=2\langle v_g^+,\omega_g\rangle_g.
 \tag{7}
$$
Here c>=2 is coprime to 6NDp; the source fixes the displayed sign.
More explicitly, on the locus where the denominator is nonzero,
A(t) is the quotient of its fixed Rankin p-adic function
L_p(f_alpha,g,1+t) by F_E(t)F_D(t); source equation(30)
proves that this quotient extends as the specified analytic
unit at t=0. This is a scalar defined by interpolation,
not by dividing zero specializations or adjusting cohomology
classes after the fact.
Define the normalized class by the **exact scalar identity**
$$
 \mathcal B
  :=\frac{\Omega_{g,\gamma}}{A_cE_\alpha}
               \operatorname{sp}({}_c{\rm BF})
   =F_D(X)z_\infty\otimes e_+
       +F_E(X)z_{D,\infty}\otimes e_- .
 \tag{8}
$$
Compatible fixed changes of the elliptic period bases in Section1
are included in A_c. Equations(6)–(8), not an unspecified unit
equality, define the normalization being used.
The equality is in characteristic-zero analytic Iwasawa
cohomology; E_alpha and A_c are nonzero near X=0.

The right side of (8) is integral in its fixed elliptic
coefficient lattice. This specifies an integral lattice for
the normalized image. It **does not** prove that the map from
the original geometric BF lattice is integral or saturated.
The factors E_alpha, A_c and Omega have not been called
p-adic units. Even choosing c so M_c(0) is a unit would
not settle the other factors.

**[NEW] Proposition 3.1.** Write F_D=d_0+d_1X+..., and
c_3=C_E(0). The following are actual coefficient identities:
$$
 \left.(\mathcal B_+/X^2)\right|_0=d_0w_0,\qquad
 \left.(\mathcal B_-/X^3)\right|_0=c_3z_{D,0}.
 \tag{9}
$$
Moreover the full next plus jet is
$$
 \mathcal B_+/X^2 \pmod {X^2}
       =(d_0+d_1X)(w_\infty\pmod {X^2}).
 \tag{10}
$$
The second formula in (9) is zero over Q_p if and only if c_3=0.

*Proof.* Substitute (4) into (8); multiplication in the
actual coefficient module proves (9) and (10).
The rank-zero twist's dual exponential is nonzero by
reciprocity and L(E^D,1) nonzero, so z_D,0 is nonzero.
There is no additional root-number cancellation of that term.
Square.

In particular z_D,0 is p-relaxed and is not finite at p.
The second formula of (9) is a component of the balanced
BF jet, not a classical Selmer class when c_3 is nonzero.
No Selmer height is assigned to that component.

The last object in (10) is a cohomology class with coefficients
T tensor Lambda/(X^2); it is not canonically a pair of classes
in H^1(Q,T). For clarity, write a representing cocycle as
w_0(g)+Xw_1(g), with ell_gamma(g) defined by
Psi(g)=gamma^{ell_gamma(g)}. In the declared inverse-character
convention its equation is
$$
 d w_1(g,h)=\ell_\gamma(g)\,g w_0(h).
 \tag{11}
$$
Thus w_1 need not itself be a cocycle. This retains the
cyclotomic Bockstein term instead of assigning a height
to an unspecified third-coefficient lift.

If L_p(E,1+t)=F_E((1+p)^t-1), then
$$
 c_3=\frac{L_p^{(3)}(E,1)}
                  {6\log_p(1+p)^3}.
 \tag{12}
$$
The logarithmic denominator cannot be dropped in a statement
modulo p^k. The known complex equality L^{(3)}(E,1)=0 does
not set (12) to zero: interpolation(3) involves primitive
cyclotomic twists of a fixed complex central value. BDV's
Heegner comparison Theorem4.3 evaluates the bottom logarithm;
it supplies no third complex-to-cyclotomic coefficient identity.

## 4. An explicit full-coefficient map into the old strict group

Let H=Sel_{p^k}(E/Q), and choose the fixed identifications
of the two old finite Kummer groups with R. Write
$$
 L:H\longrightarrow R^2,\qquad
 L(z)=(l_\ell(z),l_q(z)),\qquad
 [z,z']_m=\det(L(z),L(z')).
 $$
For any ACTUAL classes a,b in H define
$$
 \mathcal P_{a,b}(z)
    =[a,b]_m z-[z,b]_m a-[a,z]_m b.
 \tag{13}
$$

**[NEW] Proposition 4.1.** Formula(13) defines an R-linear
map H to S, without dividing any determinant. For every
fresh v it gives the exact test
$$
 a_v(\operatorname{res}_K\mathcal P_{a,b}(w_k))
  =[a,b]_m a_v(w_{k,K})
      -[w_k,b]_m a_v(a_K)-[a,w_k]_m a_v(b_K).
 \tag{14}
$$
Its signed Gysin pairing over Q is the right side divided
by 2p^k.

*Proof.* Apply L to (13); the alternating identity in R^2
makes it zero over any commutative ring. Formula(14) follows
by linearity and (2). This does not use primitivity. Square.

Suppose now that the specified kappa has order p^k.
The reviewed higher-residue theorem gives S=R kappa and
H=R^3, with L surjective. Choose a,b satisfying
L(a)=(1,0), L(b)=(0,1), and a detecting v with
a_v(kappa_K) a unit. Then
$$
 \mathcal P_{a,b}(w_k)=A_{a,b}\kappa,\qquad
 A_{a,b}=
 \frac{a_v(w_{k,K})-l_\ell(w_k)a_v(a_K)
                         -l_q(w_k)a_v(b_K)}
      {a_v(\kappa_K)} \quad\text{in }R .
 \tag{15}
$$
This is an actual finite coefficient comparison with the
constructed Kato derivative. Inserting the normalized
BF second coefficient multiplies its right side by d_0.
The Heegner denominator in (15) equals the fixed actual
cofactor test -lambda_v pr_+ Bbar_(m,v), by the previous
level-Nv construction. If the standard Heegner class is used
instead, its coefficient is -A_(a,b).

**[NEW] Proposition 4.2.** The scalar is not naturally a
unit, and the choices in (15) retain an exact ambiguity:
$$
 A_{a+t\kappa,b+s\kappa}
       =A_{a,b}-t\,l_\ell(w_k)-s\,l_q(w_k).
 \tag{16}
$$
Only its class modulo (l_ell(w_k),l_q(w_k)) is independent
of these sections.

*Proof.* Substitute the new sections into (13), noting that
their old local coordinates are unchanged. Square.

Thus choosing a convenient old-prime splitting cannot prove
a unit comparison. In the nonprimitive case (13)–(14) still
hold at the full coefficient, but P_(a,b)(w_k) need not be
in R kappa; its actual image in S/R kappa is an additional
residual class. No division of the Heegner system is used.

## 5. The genuine tame infinitesimal representation

There is no Kato class with the same Kolyvagin label m:
the cyclotomic ideals are (ell-1,a_ell-ell-1), while ell+1
is zero modulo p^k here. Hence ell-1 is a unit. More
geometrically, the degree of Q(mu_ell)/Q is prime to p,
whereas the local ring-class degree ell+1 has p-power part.

To attempt a repair, keep the ACTUAL ring-class extension.
For the explicit two-coordinate calculation only, impose
the additional hypothesis p not dividing h_K. This is not
asserted for the auxiliary twist supplied by nonvanishing.
The ring-class exact sequence and O_K^*=plus/minus1 give
$$
 G=\operatorname{Gal}(H_m/K)_{(p)}
     \simeq C_{p^{e_\ell}}\times C_{p^{e_q}},
       \qquad e_i=v_p(i+1)\ge k.
 \tag{17}
$$
Without this extra hypothesis use the actual entire group
and its augmentation ideal; its local tangent directions
need not be independently primitive.

Set A=R[G] and
$$
 B=R[Y_\ell,Y_q]/(Y_\ell^2,Y_q^2),\qquad
 A\longrightarrow B,\quad \sigma_i\longmapsto1+Y_i.
 \tag{18}
$$
This is well-defined because p^k divides p^{e_i}.
Let theta:G_K to B^* be the inverse of the quotient Artin
character, so
$$
 \theta(g)=1+a_\ell(g)Y_\ell+a_q(g)Y_q
                    +a_\ell(g)a_q(g)Y_\ell Y_q .
 \tag{19}
$$
The a_i are the negatives of the chosen additive Artin
coordinates modulo p^k. Conjugation inverts them.
For the actual induced theta representation
Ind_K^Q theta, its two summands over K have characters
theta and theta^{-1}. In the sum/difference basis its matrix
on G_K is
$$
 I+J(a_\ell Y_\ell+a_qY_q)
              +I\,a_\ell a_qY_\ell Y_q,\qquad
 J=\begin{pmatrix}0&1\\1&0\end{pmatrix};
 \quad c=\operatorname{diag}(1,-1).
 \tag{20}
$$
These are matrices of an actual arithmetic representation,
not a postulated Euler-system model.

The augmentation is 1 direct-sum epsilon_K. Every nontrivial
p-power character rho of G instead has irreducible
Ind_K^Q rho in characteristic zero, since rho is not its
inverse. Frobenius reciprocity gives
$$
 \operatorname{Hom}_{G_Q}
    (\operatorname{Ind}_K^Q\rho,1\oplus\epsilon_K)=0.
 \tag{21}
$$
Thus the Eisenstein projection in (8) is exactly the trivial
character specialization; it supplies no characteristic-zero
projection from the primitive ell q sectors. Congruence at
p is precisely what the nonsemisimple ring(18) retains.

## 6. A full-p^k Heegner coefficient and the precise lifting term

**[NEW] Proposition 6.1.** Under (17), the actual Shapiro
class of y_m, after coefficient specialization(18), equals
$$
 \mathscr H_{m,B}
      =Y_\ell Y_q\,\kappa_{m,K}^{\rm raw}
       \quad\text{in }H^1(K,T/p^k\otimes_R B(\theta)).
 \tag{22}
$$
Multiplication into the top ideal defines an injective map
on H^1. The rational plus class obtained from (22) is
Y_ell Y_q kappa, with the half-corestriction of (1).

*Proof.* By Shapiro, Kummer(y_m) defines a class with
coefficients in the induced regular ring-class module;
after trace of the prime-to-p part it is the theta module
above. Its restriction to H_m is
$$
 \sum_{g\in\operatorname{Gal}(H_m/K)}
           g\,\operatorname{Kum}(y_m)\otimes \bar g^{-1}.
 \tag{23}
$$
Choose the representatives of Gal(H_1/K) with zero
p-Artin coordinates; (17) permits this. Expanding (23)
in B, its constant coefficient is Kummer(Tr y_m).
Its single-Y_ell coefficient is
-Kummer(S D_ell Norm_q y_m), and similarly for q.
The actual norm relation Norm_q y_m=a_q(E)y_ell
makes this coefficient zero modulo p^k; the constant
coefficient has both Fourier factors and is zero as well.
The mixed coefficient is exactly
Kummer(S D_ell D_q y_m)=Kummer(P_m).
It is the restriction of the raw class by its definition.
This choice of representatives leaves the fixed raw class
unchanged: modulo p^k, (sigma_i-1)D_ell D_q y_m is zero
by the derivative identity and the factor a_i(E) in the
actual norm relation. Changing a representative by an
element of Gal(H_m/H_1) therefore leaves P_m unchanged
modulo p^k.

The known no-p-torsion assertion E(H_m)[p]=0 makes
restriction to H_m injective for these coefficient modules:
their H_m-invariants are zero. One can check the assertion
directly here: the invariant subspace in E[p] is G_Q-stable,
so irreducibility would make it all of E[p] if nonzero.
But H_m/Q is unramified at p, whereas good ordinary E[p]
has the nontrivial mod-p cyclotomic character on inertia.
This proves (22).
Also B/(Y_ell Y_q) has a filtration by copies of T/p^k,
whose G_K-invariants vanish. The coefficient exact sequence
therefore proves injectivity of the map from the top ideal
on H^1. Descent of its plus eigenspace uses the p-unit2,
as in (1). No Fourier idempotent denominator was used.
Square.

We next attempt to lift the ACTUAL BF second cyclotomic
coefficient d_0w_k from (9) through the tame representation.
Set z=d_0w_k. Its augmentation lies in the plus summand
T/p^k of (20). A lift with first derivatives in the other
summand has cochains
$$
 (z,0)+Y_\ell(0,t_\ell)+Y_q(0,t_q)
                   +Y_\ell Y_q(v,0).
 \tag{24}
$$
The a_i extend uniquely to epsilon_K-valued one-cocycles
on G_Q, zero on the chosen conjugation. The product
a_ell,q(g)=a_ell(g)a_q(g) is a scalar one-cochain.

**[NEW] Proposition 6.2.** The exact equations for (24)
to be a global cocycle are
$$
 \begin{split}
 d t_\ell&=-a_\ell\cup z,&
 d t_q&=-a_q\cup z,\\
 d v&=-a_\ell\cup t_q-a_q\cup t_\ell
                         -a_{\ell,q}\cup z .
 \end{split}
 \tag{25}
$$
The first two right sides have coefficients T/p^k
tensor epsilon_K; the last has coefficients T/p^k.
In particular the first obstruction is the actual pair
([a_ell cup z],[a_q cup z]) in the twist's H^2.
After choosing its nullhomotopies, the last displayed
two-cocycle is the next obstruction.

*Proof.* Substitute (24) into the inhomogeneous cocycle
equation and use the matrices(20), including the ordinary
rho_T action. This gives (25) coefficient by coefficient.
The twisted additivity of a_i gives
d a_ell,q=-(a_ell cup a_q+a_q cup a_ell).
Together with the first equations this verifies directly
that the final right side is closed. Changing t_i by
a twist-valued cocycle changes that right side by its
displayed cup with the other a_j. Square.

**[NEW] Proposition 6.3 (the old-prime obstruction is explicit).**
For i=ell or q, the local map
$$
 H_f^1(\mathbb Q_i,T/p^k)
      \longrightarrow H^2(\mathbb Q_i,T/p^k\otimes\epsilon_K),
       \qquad x\longmapsto a_i\cup x
 \tag{25a}
$$
is an isomorphism between free rank-one R-modules.
The other a_j has zero local cohomology class at i.
Consequently, the first obstruction in (25), localized at
the two old primes, is exactly d_0 times the two finite
localizations of w_k, under (25a). If d_0 is a unit, a
global lift requires w_k to be strict at both old primes.

*Proof.* At i the coefficient E[p^k] is unramified with
Frobenius eigenvalues +1,-1 and free rank-one eigenspaces.
The character epsilon_K has Frobenius -1, while i=-1
in R. The class a_i is tamely ramified and primitive:
on the chosen local ring-class generator its value is -1.
The local unramified H^1 of R epsilon_K is zero, since
F-1=-2 is a unit. Local duality identifies the target of
(25a) with the dual of
H^0(Q_i,E[p^k] tensor epsilon_K), the latter generated
by the minus Frobenius line of E[p^k].

The Weil pairing pairs this minus line perfectly with
the plus line representing H_f^1(Q_i,E[p^k]).
Pairing (25a) with a generator therefore becomes the
local Tate pairing between a primitive tame class in
H^1(R epsilon_K) and the unramified line in
H^1(R epsilon_K(1)). That pairing is perfect, proving
the asserted isomorphism. The character a_j for j not i
is unramified at i and hence is zero there in H^1.
All assertions are at the full R coefficient. Square.

One may choose the old identifications l_i in Section4
using (25a) and a fixed generator of its H^2 target;
this fixes their sign without suppressing a tame-unit
factor. Under unramified quadratic restriction,
res(a_i cup x)=res(a_i) cup res(x), and local invariant
is multiplied by 2. The finite value res(x)(F_i^2)
is likewise 2x(F_i). Thus this calculation has exactly
the Q/K factor of (2), and introduces no factor two
into a tame inertia coordinate.

The cofactor correction (13) therefore cancels these
two explicit local obstructions. It does not assert
that the remaining global twist-H^2 obstruction is
zero, or that all local conditions at the other primes
have been trivialized.

Formula(25) is the first exact missing map in the attempted
finite tame extension of (8). Analytic rank zero of E^D
does not make this full finite-coefficient H^2, or the
corresponding local-condition obstruction, zero.
Finite Sha of the rank-zero twist is known, but is not
the assertion that its p-primary contribution vanishes.
The first t_i would also need the native local conditions
under Shapiro; global cochain solutions alone do not
prove that requirement.

Even if such a lift existed, v in (25) is generally NOT
a cocycle. It cannot simply be declared equal to kappa
or assigned a Selmer height. The actual Heegner class
(22) has zero lower coefficients, whereas (24) starts
from d_0w_k and retains exactly the right sides of(25).
A relative comparison must supply compatible lower
nullhomotopies and show that the remaining mixed class
is the specified (22). Neither Theorem4.2 nor the
bottom-logarithm comparison constructs that map.

## 7. Extra untwisted vanishing has not killed the remaining coefficients

The computations above produce two distinct concrete residuals:
the cyclotomic coefficient c_3z_D,0 in (9), and the tame
mixed right side of (25). The old-prime cofactor map
produces the actual finite coefficient (15), with
ambiguity(16), and an extra quotient class in the
nonprimitive case. None is set to zero by L^{(3)}(E,1)=0
in the primary comparisons inspected here.

For completeness, at a primitive ring-class character rho
of conductor c dividing m, the Rankin L-function is
L(E/K,rho,s). If v divides m/c, its omitted inert local
factor is
$$
 Q_v(s)=1-(a_v(E)^2-2v)v^{-2s}+v^{2-4s};
 \quad Q_v(1)=\frac{(v+1)^2-a_v(E)^2}{v^2}.
 \tag{26}
$$
If v divides c its ramified local factor is already one.
This follows from the eigenvalues alpha_v^2,beta_v^2
of Frob_v^2 and the fact that an unramified ring-class
character is trivial on the principal ideal (v).
Thus the trivial-character augmentation has
product_(v|m) Q_v(s) L(E,s)L(E^D,s). It vanishes to
order at least five, but it is the augmentation of the
finite theta coefficient system. Equations(19)–(25)
retain the other coefficients rather than replacing
them with that augmentation. Formula(26) is retained
normalization from the preceding conductor calculation,
not claimed as new progress.

The [generalized Perrin–Riou source, BKS1910.07404v2](https://arxiv.org/html/1910.07404v2)
does not close this step. Hypothesis2.2 assumes positive
Mordell–Weil rank and finite Sha[p-infinity]. Its
Theorem1.3 additionally assumes finite primary Sha over
the real abelian field F. Its conjectural infinite-level
comparison is in degree r_alg-1. Moreover L_S^* in
Definition2.4 is the ACTUAL leading term, not automatically
L_S^{(3)}/3! when r_alg=3. Substituting the latter would
silently import the very rank comparison at issue.
Our proof(4) uses Kato's actual cohomology and full
Selmer rank directly, so it does not import these
finite-Sha hypotheses.

The coordinator requested a scope check of
[Longo–Vigni, Research Math.Sci.13,64(2026)](https://link.springer.com/article/10.1007/s40687-026-00646-7).
Theorem B concerns analytic rank one for even-weight
motives, assuming the specified regulator bijectivity
and Abel–Jacobi injectivity; Theorem A is a conditional
reformulation. Its Kolyvagin nonvanishing theorem does
not assert our rank-five class vanishing. In particular
Theorem9.2 gives odd Selmer rank at least three and even
Selmer rank at least two, with its stated height/regulator
hypotheses. These statements
therefore provide no new map in (25).

**[OPEN, HK-TP5].** Construct an integral comparison, at
the actual finite ring-class coefficient ring, between
the mixed class(22) and a normalized cyclotomic or
Rankin class, including its lower nullhomotopies and
local conditions. Prove a rank-sensitive identity for
the resulting coefficient using the additional complex
vanishing. In the primitive test(15), this must determine
the coefficient and its normalization; choosing sections
to alter it is not a proof. In all cases the comparison
must retain the full p^k and cannot rely on dividing d_0,
a smoothing factor, a modular degree or a nonunit Heegner
coefficient.

## 8. Primary-source and reproduction record

- Kato, Asterisque295(2004), Sections12.4–12.6 and18.4,
  read in the complete cached primary PDF and extracted
  text; the exact Selmer-corank inequality18.4 on printed
  p.281 was also visually checked in
  /tmp/heegner-kato-kato281.png. The publisher URL is
  https://www.numdam.org/article/AST_2004__295__117_0.pdf .
  The web reader rejected its size; the complete local
  PDF hash is
  3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d.
- BCGS2312.09301v2, Sections3.1–3.2, read directly in the
  primary HTML. Its integral normalization and prime-to-p
  isogeny conventions are distinguished from BDV's
  characteristic-zero scalar comparison.
- BDV published PDF, Theorems4.2–4.3 and equations23–30,
  downloaded and inspected at printed pp.32–38.
  Temporary files are /tmp/heegner-kato-bdv22.pdf and .txt;
  PDF SHA256
  4536fcf4292acb75b437a5826285ef6daf5083cbd0f1adfc19d96f2728928a8e.
  Extraction uses the bundled native Poppler pdftotext
  with its -layout option. No numerical certificate was run.
- BKS1910.07404v2, Hypothesis2.2, Definitions2.4/4.6,
  Theorem1.3 and Conjecture4.9 were read directly.
- The 2026 Longo–Vigni published primary HTML was inspected
  in Sections1.1–1.3 and9.1; its title is not used as a theorem
  of higher-rank BSD.

Only the two assigned proof/checkpoint files were written.
No agents were spawned and no shared synthesis was edited.
