# An actual transverse generator and a one-coordinate native pairing

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Status: completed bounded construction, independently reviewed **PASS**
in [review-heegner-native-pairing.md](review-heegner-native-pairing.md).
All seven sections passed against mathematical revision
e67fb3c138b5425cf3b95fa41feb0349f62a8c59ffc23e9fd9eff126da19bcfd,
including the exact dual twist transport. Later status edits are editorial.
Restart: [checkpoint](heegner-native-pairing-checkpoint.md).
The universal full BSD objective remains active.

This note constructs the transverse twist test with a fixed arithmetic
normalization. It reduces the actual compact pairing to one finite
Frobenius coordinate, gives its finite matrix evaluation, and computes
the effect of the proposed twist-zeta correction exactly. That
correction has zero effect after the required p-local normalization.
The remaining coordinate is not proved zero from analytic rank five.

## 1. Scope and the actual pairing to be evaluated

Keep all objects of the
[reviewed tame-nullhomotopy proof](heegner-tame-nullhomotopy-attack.md):
E,p,K,D,m=ell q, k=M(m), R=Z/p^k, M=E[p^k],
M_D=M tensor epsilon_K, U=Spec Z[1/(Np|D|ell q)], and
the ACTUAL corrected input
$$
 z=d_0\mathcal P_{A,B}(w_k).
 \tag{1}
$$
The classes A,B are fixed, not adjusted to prescribe a value.
No finite Sha hypothesis is made for E. The independent tame
coordinates still require p not dividing h_K. The use of the
actual d_0 annihilator remains in the preceding surjective,
Manin-unit, ordinary nonanomalous range.

First work in the explicit additional clean case
$$
 p\nmid\operatorname{Tam}(E),\qquad
 \operatorname{Sel}_{p^k}(E^D/\mathbb Q)=0 .
 \tag{2}
$$
Since the twist has rank zero, its p-primary Sha group is finite;
vanishing of this finite Selmer group for k>=1 makes that whole
primary group zero. The preceding exact valuation therefore gives
d_0 in Z_p^times. This is a consequence of (2), not an assumption
that every auxiliary twist enjoys it. Section7 retains the other
cases with the actual J_i,v groups.

Write
$$
 H_v=H^1(\mathbb Q_v,M_D),\quad
 F_v=H_f^1(\mathbb Q_v,M_D),\quad Q_v=H_v/F_v,\qquad
 H_S=\bigoplus_{v\in S}H_v,\ F_S=\bigoplus F_v,\ Q_S=\bigoplus Q_v.
 \tag{3}
$$
S is the actual finite complement and the real place. The real
Tate group is zero. The local pairing is
$$
 B_v(h,h')=p^k\operatorname{inv}_v(e_{p^k}(h\cup h'))\in R.
 \tag{4}
$$
Its first coefficient is the COMPACT coefficient when used in
the project pairing. It is symmetric on H^1 because the Weil
pairing and the degree-one cup interchange both change sign.
F_v is its exact annihilator.

For i=ell,q the preceding construction provides a global
primitive t_i and native local primitives tau_i,v satisfying
$$
 dt_i=-a_i\cup z,\qquad d\tau_{i,v}=-a_i\cup z_v.
 \tag{5}
$$
The actual compact class is
c_i=(-a_i cup z,(tau_i,v)) modulo partial^+ J_i.
In (2), J_i,v=F_v away from i and J_i,i is the old
transverse line. Global existence in (5) is completed work.

## 2. A unique arithmetic localization inverse

**[NEW] Proposition 2.1.** Under (2), the map
$$
 q\operatorname{loc}:H^1(U,M_D)\longrightarrow Q_S
 \tag{6}
$$
is an isomorphism. Denote its UNIQUE inverse by C.

*Proof.* Finite Poitou–Tate says that the image K_S of global
localization in H_S is its exact annihilator under sum B_v.
The same is true for F_S. The intersection K_S cap F_S is
the localization of the classical twist Selmer group and is
zero. Both finite self-annihilating groups have square-root
order in H_S, so K_S+F_S=H_S. The global localization
kernel is S-strict and hence belongs to the zero classical
Selmer group. This proves (6). Square.

This is an inverse between actual arithmetic groups, not the
choice of a functional on an abstract Selmer module.
For any v let
$$
 C_v(q)=C(0,\ldots,q,\ldots,0),\qquad
 \sigma_v(q)=\operatorname{loc}_v C_v(q).
 \tag{7}
$$
Then sigma_v is a section of H_v to Q_v. Its image T_v
is isotropic: the other localizations of both global
classes C_v(q),C_v(q') are finite, so global reciprocity
makes their v-pairing zero. It follows that
H_v=F_v direct-sum T_v. These local complements are
specified by the arithmetic inverse C.

At either old prime i, the previously proved rank-one
isotropy calculation makes T_i the ACTUAL transverse
line, not just an unspecified complement.

Choose its primitive class beta_i as follows. Choose
t_i^+ in the plus Frobenius line of M and y_i^- in
the minus line, with
e_(p^k)(y_i^-,t_i^+)=zeta_i, where zeta_i is the fixed
positive uniformizer-Kummer value of the tame generator.
Normalize the local Frobenius lift so a_i(F_i)=0.
Then
$$
 \beta_i=-a_i\otimes t_i^+\in H_{{\rm tr},i}^1(\mathbb Q_i,M_D).
 \tag{8}
$$
It has inertia value t_i^+. If f_i in F_i has finite
Frobenius value r y_i^-, local Tate duality gives
B_i(f_i,beta_i)=r. This may equivalently be taken as
the sign normalization of beta_i. Restricting to the
unramified quadratic field changes the finite value
to2r and the local invariant by2; inertia is unchanged.
It is the usual positive unramified-character/uniformizer
pairing, with the coefficients in the order of (4).

Define
$$
 b_i=C_i(q_i(\beta_i)).
 \tag{9}
$$
It has localization beta_i at i and is finite everywhere
else. In particular it is the specified generator of the
transverse twist test group R. Multiplying it by an
unknown unit is not part of its definition.

The construction is usable on finite presentations:
represent H^1(U,M_D) by cocycles on finite arithmetic
quotients, compute their actual local Kummer quotients,
and solve (6) with the stated right side. Existence and
uniqueness of the class follow from (6); no search over
arbitrary Pontryagin characters is needed.

## 3. The p-generator comes from the actual twist zeta class

Let T_D=T_p(E^D), alpha the ordinary unit root, beta=p/alpha,
and retain the fixed BKS differential normalization
$$
 \delta_0=k_\alpha^{-1}\nu,\qquad
 k_\alpha=(1-\alpha^{-1})^{-1}(1-\beta^{-1}),\qquad
 [\omega_D,\nu]=1.
 \tag{10}
$$
For precision, the next local calculation is first on T_D.
Let iota_*:T_D to T_pE tensor epsilon_K be the fixed
Weil-compatible geometric twist identification, and let
u_iota be its differential scalar from the predecessor.
The inherited CLASS transport is A=u_iota^{-1}iota_*.
Its first-slot dual transport is
A^{-dagger}=u_iota iota_*; explicitly
(A^{-dagger}x,A y)=(x,y).
At p the scalar u_iota is a p-unit, since the twist is
unramified and both minimal differentials are primitive.
This scalar is retained, not set to one.

**[NEW] Lemma 3.1.** At a good nonanomalous ordinary prime,
the local class e_p^D=exp(delta_0) is a primitive element
of the integral point-Kummer lattice. The functional
$$
 O_p^D(\xi)=(e_p^D,\xi)_p
 \tag{11}
$$
is therefore an integral isomorphism from the singular
local quotient to Z_p. No CM splitting is required.

*Proof.* Nonanomalousness gives #E^D(F_p) prime to p.
The local point completion is the formal group, whose
Neron logarithm identifies it with pZ_p. The fixed
exponential identity gives log_omega(e_p^D)=k_alpha^{-1},
of valuation1. Thus it is primitive.
The ordinary quotient and its dual have no residual
invariants. The coefficient sequence consequently makes
the point lattice saturated in the free rank-two H^1
lattice. Integral local Tate duality identifies its
dual with the singular quotient, proving (11).
This uses a pairing with the point lattice and the
quotient, not an integral splitting of the ordinary
representation. Square.

In every M_D formula below set e_p=A^{-dagger}e_p^D
and O_p=(e_p,-)=O_p^D A^{-1}. Likewise z_D,0 below
denotes the inherited class A(z_D,0^D), as in the
preceding Heegner–Kato proof. Thus all class and
first-slot point transports are contragredient.

The ordinary Coleman construction, with precisely this
delta_0, gives
$$
 O_p(\operatorname{loc}_p z_{D,0})=d_0.
 \tag{12}
$$
This is the augmentation of the fixed actual Kato
reciprocity law, not a normalization assigned afterward.
The BKS definitions(6.3.1)–(6.3.2) and the finite
Coleman pairing give (12).
The Euler-factor check is explicit: the normalized Kato
dual exponential BEFORE transport has coefficient
(1-alpha^{-1})(1-beta^{-1})L(E^D,1)/Omega_(E^D)^+.
Pairing with delta_0 multiplies it by k_alpha^{-1},
giving (1-alpha^{-1})^2 L(E^D,1)/Omega_(E^D)^+=d_0.
The dual transports preserve this exact pairing.
All periods here are the same fixed plus-cycle periods.
At every non-p place the integral z_D,0 has the point
Kummer condition. Hence, with Q_p identified by O_p,
$$
 b_p:=d_0^{-1}z_{D,0,k}=C_p(1).
 \tag{13}
$$
Only the proved p-unit d_0 is inverted here. Formula(13)
is unavailable as an integral operation if (2) is removed.
The class b_p is p-relaxed, not a finite local class.

Write loc_p(b_i)=h_i e_p in the finite group at p.
Define P_i modulo p^k to represent
(A^{-dagger})^{-1}loc_p(b_i) in the T_D point lattice.
This is an actual local point class because the
geometric identification and its retained p-unit
scalar preserve that lattice. Then
$$
 h_i=k_\alpha\log_{\omega_D}(P_i)\pmod{p^k}.
 \tag{14}
$$
The ratio is formed in the integral formal lattice:
log(P_i) is determined modulo p^{k+1}, and
log(e_p) has valuation1. This is not cancellation of
a nonunit in an unqualified R-valued expression.

Global reciprocity for b_i and b_p gives the exact
cross-local identity
$$
 f_i(\operatorname{loc}_i b_p)=-h_i,\qquad
 f_i(\operatorname{loc}_i z_{D,0,k})=-d_0h_i .
 \tag{15}
$$
Here f_i denotes the finite-coordinate map fixed by
B_i(-,beta_i). Only i and p contribute: at all other
places both classes are finite.
Equation(15) relates an actual finite Kato localization
to a local formal logarithm of the transverse test.
It does not make P_i a global rational point on E^D.

## 4. The compact pairing is one explicit finite coordinate

Define closed local differences
$$
 \delta_v=\tau_{i,v}-\operatorname{loc}_v t_i,\qquad
 h=C(q(\delta)),\qquad t_i^\natural=t_i+h .
 \tag{16}
$$
Choose any cocycle representative of h. Then
$$
 \eta_v:=\tau_{i,v}-\operatorname{loc}_v t_i^\natural
                         \in F_v
 \tag{17}
$$
as cohomology classes at every place.

**[NEW] Theorem 4.1 (exact native evaluator).** Put
$$
 \mathcal R_i(z)=B_i(\eta_i,\beta_i)\in R.
 \tag{18}
$$
Then the previous compact-first pairing is exactly
$$
 \mathscr P(b_i,c_i)=\mathcal R_i(z)/p^k.
 \tag{19}
$$
Native first-lift compatibility is equivalent to
R_i(z)=0. The scalar is independent of the global
primitive and of the chosen native local lifts.

*Proof.* In the preceding formula choose the global
three-cup primitive u=t_i^natural cup b_i. Subtracting
its compact boundary leaves the local classes
eta_v cup b_i,v. Away from i both classes are finite,
so every such local invariant is zero. At i the
value is exactly (18), proving (19). Since eta_i
is finite and its permitted native correction is
transverse, compatibility at i requires eta_i=0;
all other native conditions are already satisfied.
Perfectness of the old finite/transverse pairing
proves the equivalence.

If t_i is replaced by t_i+g for a global cocycle,
then C(q(delta)) changes by -g, since C is the
inverse of (6). Thus the normalized class does
not change. A native local change away from i is
finite and changes no quotient coordinate. A native
change at i is a multiple of beta_i, so it changes
h by the same multiple of b_i; the latter has
zero finite coordinate at i. Hence (18) is unchanged.
Coboundaries give the same conclusion. Square.

This eliminates the unspecified global degree-two
primitive from the old triple-cup expression. It
still leaves an arithmetic coefficient to calculate.
It does not state that this coefficient is zero.

Here is a finite matrix evaluation of it. Suppose
first that Q_S is free, choose any actual basis
xi_1,...,xi_d of H^1(U,M_D), and use the corresponding
local quotient coordinates. Form
$$
 L=(q_v\operatorname{loc}_v\xi_a)_{v,a},\quad
 q_\delta=(q_v\delta_v)_v,\quad
 r_i=(f_i\operatorname{loc}_i\xi_a)_a,\quad
 d_i=f_i(\delta_i).
 \tag{20}
$$
The finite-coordinate maps use the local complements
sigma_v of (7), so f_i is defined on all H_i.
The actual localization isomorphism proves det L
is a unit. Therefore
$$
 \boxed{\mathcal R_i(z)
   =d_i-r_iL^{-1}q_\delta
   =\frac{\det\begin{pmatrix}L&q_\delta\\r_i&d_i\end{pmatrix}}
                {\det L}.}
 \tag{21}
$$
All entries are finite Galois/Kummer evaluations of
specified classes or nullcochains. Changing the basis
changes numerator and denominator compatibly.
The only inverse is of the proved unit det L.
If Q_S has shorter cyclic factors, use its actual
Smith presentation and solve (6) as congruences;
do not replace it by a free module or divide a
nonunit diagonal entry.

For the particularly transparent subrange where the
non-p bad local groups vanish, the coordinates are
p,ell,q and L is a3-by3 matrix. The classes
b_p,b_ell,b_q are a distinguished basis and make
L the identity. More generally (20) retains all
actual places in S.

## 5. The attempted zeta correction has exactly zero net effect

Define, for u not v,
$$
 G_{uv}(q)=\operatorname{loc}_u C_v(q)\in F_u.
 \tag{22}
$$
Global reciprocity makes these maps skew-adjoint:
$$
 B_u(G_{uv}(q_v),\sigma_u(q_u))
   +B_v(\sigma_v(q_v),G_{vu}(q_u))=0.
 \tag{23}
$$
For old rank-one coordinates this is G_uv=-G_vu.
The diagonal is zero by the choice of sigma_v.
These are relations between actual localizations of
the constructed global test classes.

With the distinguished basis, (21) becomes
$$
 \mathcal R_i(z)=f_i(\delta_i)
     -\sum_{v\ne i}f_i\bigl(G_{iv}(q_v\delta_v)\bigr).
 \tag{24}
$$
The p contribution is explicitly
$$
 +h_i\,q_p(\delta_p),
 \tag{25}
$$
by (15). It is not legitimate to remove it by
calling the twist zeta class finite at p.

**[NEW] Proposition 5.1.** Replacing a global primitive
t_i by t_i+lambda z_D,0,k changes (24) by exactly zero.

*Proof.* In the i finite coordinate the change is
-lambda f_i(loc_i z_D,0,k)=lambda d_0h_i.
The p singular difference changes by -lambda d_0,
so (25) changes by -lambda d_0h_i. These cancel.
There are no other singular coordinates of the
integral Kato class. This is also the explicit
zeta-instance of the inverse identity in (16).
Square.

Thus the actual rank-zero zeta class supplies a
normalized generator and computes a reciprocity
term, but it cannot be used to set the native
value to zero by an arbitrary scalar correction.
The apparent adjustable old-prime term is
compensated at p.

I also tested whether a known derived-height
universal-norm theorem would kill (18).
[Bertolini–Darmon, Derived p-adic heights, AJM117(1995)](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/pub13.pdf),
Section1.1 assumption(4), requires surjectivity of
the local point norms. This fails on our actual
ramified old-prime extension. There the formal
kernel is uniquely p-divisible, residue action
is trivial, and the residue norm is multiplication
by p^{e_i}. Consequently its norm cokernel is
$$
 E(\mathbb F_{i^2})/p^{e_i}E(\mathbb F_{i^2}),
       \quad\text{whose quotient modulo }p^k
                      \text{ is }R^2 .
 \tag{26}
$$
The latter follows from Frob_i^2=1 on E[p^k].
Moreover b_i itself has the transverse condition
at i, rather than the source's classical finite
condition. Therefore that height theorem does
not evaluate this native pairing. Its symmetric
local Tate and Cassels exact-sequence statements
in Section1.2 do apply and agree with (6),(23).

## 6. What can be selected if the native values vanish

If R_ell(z)=R_q(z)=0, the normalized global primitives
in (16), with fixed cochain representatives, satisfy
the native local conditions. They provide an actual
finite construction of compatible first lifts.
The class of each such lift still admits addition
of lambda_i b_i, the actual transverse twist
Selmer group. Choosing representatives or a
finite linear-system solution is an algorithmic
selection, not a motivic normalization theorem.

Their mixed obstruction remains the actual class
$$
 \Omega=-a_\ell\cup t_q-a_q\cup t_\ell-a_{\ell,q}\cup z
                                  \in Z^2(U,M).
 \tag{27}
$$
Permitted first-lift changes give
$$
 [\Omega]\longmapsto[\Omega]
       -\lambda_q a_\ell\cup b_q-\lambda_\ell a_q\cup b_\ell .
 \tag{28}
$$
At ell the first adjustment has coefficient given
by the actual finite localization G_ell,q, through
the fixed tame cup isomorphism; at q the second
has coefficient G_q,ell=-G_ell,q. The other old
localization of each term is zero. At p the
second-cohomology target is zero by nonanomalousness,
and at other places the clean finite/unramified
conditions give zero. Thus (23) identifies the
exact local adjustment coefficients.

If that cross coefficient is a unit, the two
old mixed local values can be removed uniquely
at those coordinates. If it is a nonunit, the
remaining local values must lie in its actual
ideal before such a correction exists; no
nonunit is cancelled. After removing local values
the residual class lies in the actual global
kernel Sha_S^2(M), dual to the S-strict E
cohomology. Nothing about the finite rank-zero
twist annihilates this E-group or the particular
residual element.

Even if the mixed class vanishes and a top
primitive is selected, adding the ACTUAL
Heegner Shapiro class Y_ell Y_q kappa_raw
preserves all lower coefficients and the
native point-image conditions. Its effect
on the top coefficient is exactly kappa_raw,
or -kappa_standard. Quadratic descent uses
cor/2 and the same compact-FIRST pairing;
no new quadratic factor enters inertia.

## 7. Nonclean presentation and the remaining arithmetic coefficient

If the classical twist Selmer group is nonzero,
(6) is not inverted. Its kernel is that Selmer
group, and its image/cokernel are computed by
the actual finite Poitou–Tate sequence.
If Tamagawa factors intervene, retain the
actual preimage groups J_i,v from the preceding
native point construction, not the clean
finite/transverse substitution.

A presentation valid in these cases consists
of the finite global cocycle equations, their
actual local maps, and generators/relations
for every J_i,v. The test module is the kernel
of localization modulo J_i,v perpendicular.
Pairing (18) of the preceding proof with those
actual generators gives its full finite
evaluation vector. Nonfree Smith factors
and d_0's valuation stay in the equations.
The earlier global annihilator is not a unit
inverse for these presentations.

The completed calculation here is the exact
native evaluator(21)/(24), the arithmetic
generator(9)/(13), and the exact zero effect
of the proposed twist-zeta correction.
The entry R_i(d_0 P_AB(w_k)) has NOT been
shown to vanish universally. Neither the
skew reciprocity relation(23) nor the norm
calculation(26) computes it from the extra
complex equality L'''(E,1)=0.

**[OPEN, NP-TP5].** Construct the arithmetic
comparison evaluating that particular
bordered coefficient from the extra complex
vanishing, then select a compatible mixed
lift with its actual Heegner top coefficient.
A p-adic third coefficient or an assumed
finite Sha group for E is not substituted.
This note does not claim a full proof of
O5 or BSD.

Primary verification: Milne ADT second edition
I.2–I.4 and finite Cassels/Poitou–Tate exactness;
BKS1910.07404v2 equations6.3.1–6.3.2 and its
finite Coleman definition; BCGS2312.09301v2
Theorem3.2.2 for the fixed Kato normalization;
the published Bertolini–Darmon source above,
Sections1.1–1.2, for the tested norm hypothesis.
The finite Galois/etale comparison and all
prior raw/standard signs are the independently
reviewed inputs in the preceding note.
No old numerical certificate was rerun, no
new agent was spawned and no shared synthesis
was edited.
