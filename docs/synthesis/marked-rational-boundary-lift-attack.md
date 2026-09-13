# The rational boundary input in the marked coefficient triangle

Date:2026-09-13. Owner /root/higher_period_integrality,
GPT-6 Astra/xhigh. Complete bounded construction, independently reviewed
**[PASS for all nine sections](review-marked-rational-boundary-lift.md)**.
[Checkpoint](marked-rational-boundary-lift-checkpoint.md).
Full BSD over Q remains open.

The actual coefficient motive and its real lifting theorem are inputs
from the [completed marked construction](marked-coefficient-extension-attack.md).
This note tests the KNOWN rational input j_B(beta2), not an invented
rational class for the spectral value.

## 1. Actual objects and the signed boundary composite

Let C=X0(389), S=C minus Sigma, and B0={c0,c_infinity} be the two
original rational cusps. The coefficient triangle already constructed
in DM_B(S) is

    F -> W -> 1 --epsilon_W--> F[1].

The actual motivic fibers at both cusps are identified with the SAME
constant fiber W0: pi(c0)=pi(c_infinity)=O and all a_ij(O)=1.
Let F0 be the corresponding fiber of the top map and
epsilon0:1->F0[1] its connecting morphism. These identifications use
the full corrected divisor marking, not merely equality of realizations.

Write R_E(2)=RΓ_M(E_t,Q(2)). The fixed beta2 is a rational morphism
1->R_E(2)[2]. Thus

    chi_beta = epsilon0 tensor beta2
       in Hom_DM_B(Q)(1,F0 tensor R_E(2)[3])                 (1.1)

is an ACTUAL point-coefficient/K2 product. Its class is not defined by
its real regulator. Retain the relative functor K_D(2) of the completed
proof, and the positive cusp boundary j^+_(B,D)(b)=(0,+b).

**[NEW] Proposition1.1.** For b2,S=j_B(beta2)|_(S×E_t), its motivic
coefficient obstruction is

    O_W^M(b2,S) = -j^+_(B,F)(chi_beta,0)
       in H_M^4(K_F(2)).                                   (1.2)

Equivalently, this obstruction is zero exactly when the pair
(chi_beta,0) belongs to the image of the actual restriction

    H_M^3(S×E_t,F(2)) -> H_M^3(B0×E_t,F0(2)).                (1.3)

*Proof.* Work with the stable coefficient enhancement fixed in the
predecessor. Applying the relative functor gives the two coefficient
and boundary exact triangles and their natural diagram. The sign can
be verified on its fiber complexes. For the relative convention
D(a,b)=(da,r(a)-db), the positive boundary of a degree-two cocycle
beta is(0,+beta). A graded lift to W has coefficient differential
epsilon_W beta. Its relative differential is consequently
(0,-epsilon0 beta) in the boundary component of K_F. Thus the
coefficient connecting map followed by the positive cusp boundary
has the MINUS sign in(1.2). This computation is a map-of-cones
calculation in the actual enhancement, so it determines the motivic
connecting morphism, not only its Betti realization. The long exact
sequence for K_F proves the equivalence with(1.3). Square.

The global morphism epsilon_W tensor beta2 restricts to
(chi_beta,chi_beta). Its positive relative boundary is zero. This
checks compatibility with using the other cusp, where the scalar
input is the negative of j_B(beta2). It does not make either
individual boundary component vanish.

If chi_beta itself were zero, a fiberwise K2 lift through W0 would
give a sufficient rational relative lift by positive boundary. This
is only sufficient: (1.3) could also hold through a nonzero global
class. Neither vanishing is inferred from the completed real lift.

## 2. The actual exterior filtration and its point component

Let G_mot be the fiber of V_marked→L in the preceding construction.
It is the CONSTANT homological coefficient of U0=E_s minus{O,P,Q},
where E_s denotes the point curve, distinct from the test factor E_t.
More explicitly, with P_U=RΓ_M(U0,Q) pulled to S,

    G_mot = (Cofib(1→P_U)[1])^dual.                         (2.1)

The octahedron for1→P_U→q_*1_B, followed by duality, identifies
(2.1) with the kernel in the actual marked pullback. Thus there is
a specified triangle

    G_mot→V_marked→L --eta-->G_mot[1],
    eta(e_j)=eta_j.                                        (2.2)

The two eta_j are represented by the ACTUAL translated degree-zero
divisors T_pi(z)Z_j on U0. At the cusps they are the fixed eta_j,0
of the corrected semiabelian points g_j=AJ_A(Z_j). This is a map in
the relative motive, not a chosen real period lift.

The rational exterior filtration for(2.2) gives the actual triangle

    wedge²G_mot→F→G_mot tensorL→(wedge²G_mot)[1].            (2.3)

We use the monoidal model enhancement, as required by
[Guletskii, math/0306297v1, §3.4 Proposition19](https://arxiv.org/pdf/math/0306297v1).
The inspected PDF has36pages, the arXiv banner19June2003 and a
recompiled front date21November2018; we use its displayed Proposition19,
not an unverified numbering in the published version.
For exterior degree two, the filtration can also be constructed
directly: take the pushout-product filtration on V tensor² with
successive terms G tensorG, (G tensorV) amalgam (V tensorG),
and V tensorV, then apply the rational antisymmetrizer.
Its middle quotient is G tensorL and its last quotient wedge²L.
This proves(2.3) and fixes its maps in the actual enhancement.

**[NEW] Proposition2.1.** The image of epsilon_W under
F[1]→(G_mot tensorL)[1] is

    eta_1 tensor e2 − eta_2 tensor e1.                       (2.4)

There is a natural constant abelian quotient G_mot→H, where H is
the homological H1 coefficient of E_s. Under it, (2.4) is the
CONSTANT class

    kappa(P) tensor e2 − kappa(Q) tensor e1
       in Hom(1,(H tensorL)[1]).                            (2.5)

*Proof.* Represent(2.2) by its coefficient cone with graded top lifts
e1,e2 and differential d(e_j)=eta_j. Modulo the term with two G
factors, the differential of the alternating generator is
eta1 wedge e2+e1 wedge eta2, which is(2.4). The same calculation on
the pushout-product diagram proves the map statement without
assuming a motivic t-structure. The source generator and the target
line both use e1 tensor e2−e2 tensor e1. Therefore the raw projector's
factor1/2 cancels on the matched frames; there is no extra factor2
in(2.4).

Inclusion U0→E_s followed by the h1 Chow projector based at O gives
the map to H. The degree-zero cycle T_xZ_j has the same proper
Picard class as Z_j, namely P_j, independently of x. The rational
function F_j(x,w) already constructed has divisor T_xZ_j−Z_j.
Thus its proper-cycle map is the constant point class. This proves
(2.5) motivically. It does not discard the relative toric class
of F_j, whose values at the removed A are precisely a_ij(x). Square.

Set D=H tensorL. Let

    chi_D=(kappa(P) tensor e2−kappa(Q) tensor e1) cup beta2
       in H_M³(E_t,D(2)).                                 (2.6)

The projection of the full obstruction(1.2) is exactly

    O_D = −j^+_(B,D)(chi_D,0)|_S.                           (2.7)

The class chi_D has an explicit higher-Chow presentation. If z_beta
is the fixed rational cycle representing beta2 from the completed
modular-unit construction, its components are

    ([P]−[O]) external-product z_beta,
    −([Q]−[O]) external-product z_beta
       in CH³(E_s×E_t,2)_Q.                               (2.8)

Here the first component is in the e2 column and the second in the
e1 column. To verify the degree, write h1(E_s) for the cohomological
Chow summand of RΓ(E_s,Q). Curve duality identifies
H=h1(E_s)(1)[1], with the positive divisor cycle convention.
Then H_M³(E_t,H(2)) is the h1(E_s) part of
H_M⁴(E_s×E_t,Q(3))=CH³(E_s×E_t,2)_Q.
No independent Tate factor has been dropped.

The correction from Z_j to this proper point divisor has a literal
rational chain. With m_(R,P_j) the same normalized Miller function,

    div(h_j/m_(R,P_j)) = Z_j−([P_j]−[O]).                   (2.9)

Indeed div m_(R,P_j)=[R]+[P_j]−[R+P_j]−[O].
External product of the function-graph chain in(2.9) with z_beta
has cubical boundary

    (Z_j−([P_j]−[O])) external-product z_beta.

This is a CH³(E_s×E_t,3) CHAIN whose boundary identifies the two
CH³(-,2) presentations. It is not a proof that either presentation
is zero. The chain is used on the PROPER E_s: its endpoint support
contains P_j and O, so it does not trivialize the relative coefficient
on E_s minus A. That remaining toric data is retained in(2.2).

## 3. Explicit rational K2 corrections for the moving toric component

Write S_E=E_s minus Sigma_E and Y'=S minus B0. The exact rational
functions a_ij on S_E and their pullbacks A_ij=a_ij∘pi on S are
the ones in the completed marked proof. They have A_ij(c0)=
A_ij(c_infinity)=1 and the full h_j corrections.
On Y' both u and A_ij are units. Form their actual symbols

    sigma_ij={u,A_ij} in H_M²(Y',Q(2)).                      (3.1)

Use the fixed Rost convention partial{t,a}=a. Thus, writing
f=t^m f0 and g=t^n g0, the tame residue is
(-1)^(mn)g0^m/f0^n. This is the same convention as the preceding
Kummer and boundary proofs.

**[NEW] Proposition3.1.** Each(3.1) extends uniquely to a rational
class in H_M²(S,Q(2)). Its added-boundary residue at s in Sigma is

    partial_s sigma_ij = u(s)^(-ord_s A_ij).                 (3.2)

For s above−R, with ramification index e_s, the four residues are
the Kummer vector

    −e_s [[4,3],[3,4]] kappa(u(s)).                          (3.3)

The proper finite transfer along pi:S→S_E satisfies

    pi_* sigma_ij=0 in H_M²(S_E,Q(2)).                       (3.4)

*Proof.* At either old cusp the residue is A_ij(c)^(ord_cu)=1.
Localization for these two codimension-one points has kernel term
H_M⁰(B0,Q(1))=0 and residue term H_M¹(B0,Q(1)).
Weight-one motivic cohomology gives the first vanishing and identifies
the second with the multiplicative groups. Therefore the zero residues
give existence and uniqueness of the extension. At an added point u
has valuation zero, yielding(3.2). The actual residue matrix from the
marked proof yields(3.3), including its minus sign.

At the generic point the norm/projection formula gives
pi_*{u,pi^*a_ij}={Norm_pi(u),a_ij}. The completed graph-unit proof
computed Norm_pi(u)=±1. Consequently this symbol is torsion of order
at most2 and is zero rationally. The restriction of H_M²(S_E,Q2)
to the generic field is injective: its localization kernel again
has terms H_M⁰(k(x),Q1)=0. Hence the global transfer is zero. Square.

These classes are actual rational K2 corrections retaining all new
boundary values. No nonzero claim about sigma_ij is inferred just
from its displayed possible residues, and the trace-zero statement
does not identify the whole class with zero.
The projection formula and divisor/norm compatibility are the same
primary higher-Chow functoriality from
[Levine, Theorem5.2 and Corollary5.3](https://www.numdam.org/article/AST_1994__226__235_0.pdf)
used in the completed boundary proof. Weight-one identification and
the motivic/higher-Chow dictionary are
[MVW, §§4 and19](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).

The variable toric extension ALONE has a rational boundary lift:
its matrix A_ij is identically1 at each old cusp, so its Kummer
one-motive fiber splits there with the canonical top lattice.
Take the exterior of that top section, in the matched alternating
frame, tensor beta2, and apply positive boundary. This constructs
the lift for that toric extension. It does not split the fixed
semiabelian point extensions eta_j,0 and is not a lift for the full W.
Equations(3.1)–(3.3) record the extra boundary terms which would be
lost by replacing this comparison with a zero framing at Sigma.

## 4. The first rational obstruction modulo the actual added boundary

For CONSTANT coefficient D, work first on the proper pair
(C×E_t,B0×E_t). The two cusp restrictions agree motivically by the
actual divisor-chain divu=388(c0−c_infinity), exactly as in the
completed beta2 proof, now with constant coefficient D. Projection
to E_t realizes every diagonal class. Thus

    j^+_(B,D):H_M³(E_t,D(2))→H_M⁴(C×E_t,B0×E_t;D(2))

is injective. This statement is about the proper pair.
Put O_D,proper=−j^+_(B,D)(chi_D,0).

**[NEW] Proposition4.1.** The projected obstruction(2.7) vanishes
if and only if O_D,proper belongs to the image of the actual Gysin map

    H_M²(Sigma×E_t,D(1))
       --i_Sigma,*--> H_M⁴(C×E_t,B0×E_t;D(2)).              (4.1)

*Proof.* Sigma and B0 are disjoint. Localization therefore supplies
the triangle of complexes with supports in Sigma×E_t, the proper
relative complex, and its restriction to S×E_t. Absolute purity
for this regular codimension-one embedding identifies the support
complex with RΓ(Sigma×E_t,D(1))[-2]. The resulting degree-four
exact sequence is precisely(4.1) and the claimed kernel statement.
Use CD Theorem14.4.1 and its coefficient projection formula, already
checked in the preceding motivic construction. Square.

This is a precise first-component test. Vanishing of the FULL
obstruction implies(4.1); the converse need not hold because the
remaining exterior/toric components of F are still present.

The warning about the open curve is essential. The principal
function u need not be1 on Sigma. By MVW Theorem7.16, the zero-cycle
relation for the open curve is measured by Pic(C,Sigma), and
rational-function boundaries must retain that boundary trivialization.
The proper relation alone therefore does not prove that the two
maps into M(S) agree. No injection of j_B after restriction to S,
and no false trivialization of O_E((-R)-O), is assumed.

## 5. Right cup and the finite boundary-unit condition

Extend the COMPLETED compact unit-cup trace to the constant
coefficient D. With Y=C minus B0, it acts in the present degree as

    T_u^D:H_M⁴(C×E_t,B0×E_t;D(2))→H_M³(E_t,D(2)),
    c ↦ Tr_Y(c RIGHT-CUP kappa_u).                          (5.1)

The cup raises degree and twist by(1,1); the smooth curve counit
lowers them by(2,1). This is the actual nonproper compact trace,
not pushforward of ordinary cohomology from S.

**[NEW] Lemma5.1.** For chi in H_M^r(E_t,D(2)), with the same
trace in the corresponding degree,

    T_u^D(j^+_(B,D)chi)=(-1)^r 388chi.                      (5.2)

In particular T_u^D(O_D,proper)=388chi_D.
For zeta_s in H_M²(E_(k(s)),D(1)),

    T_u^D(i_s,*zeta_s)
       =Tr_(k(s)/Q)(zeta_s RIGHT-CUP kappa(u(s))).           (5.3)

*Proof.* Write j_Bchi=e0 external-product chi, where e0 has
degree one on the base. Moving chi past the RIGHTMOST kappa_u
gives(-1)^r. The remaining base trace is the previously proved
Tr_Y(e0 cup kappa_u)=388, a rational endomorphism of the unit.
This proves(5.2) for the actual coefficient morphisms, without
assuming realization faithfulness on chi. Here r=3, so j_Bchi
has trace−388chi. The additional minus in O_D,proper cancels it.

For(5.3), apply the compact projection formula at the closed
point and compose the Gysin and trace counits. The restriction
of the unit is its actual value u(s). The degree-two Gysin shift
and the degree-minus-two curve trace cancel, as do their opposite
Tate twists. The remaining right-cup order is precisely the one
written. No odd interchange is needed in(5.3). Square.

It follows that any rational full lift forces, at least, an equality

    388chi_D =
       sum_(s in Sigma) Tr_(k(s)/Q)
                      (zeta_s RIGHT-CUP kappa(u(s)))        (5.4)

for some zeta=(zeta_s) with O_D,proper=i_Sigma,*zeta.
The classes zeta_s have a concrete cycle type:
H_M²(E_t,H(1)) is the h1(E_s) component of
CH²(E_s×E_t,1)_Q over k(s). Thus(5.4) compares the actual point×K2
cycles in(2.8) with traces of explicit added-fiber units times
higher-Chow degree-one cycles. This necessary condition is stronger
than a zero real regulator and weaker than the full lift statement.
No factor involving the unknown BSD quotient occurs.

## 6. A natural pulled-back boundary correction gives zero

The added divisor is the FULL inverse image of Sigma_E. Let x be
a closed point of Sigma_E and let e_s be the ramification index
at s above x. Given xi_x in H_M²(E_(k(x)),D(1)), consider the
actual flat-pullback pattern

    zeta_s=e_s Res_(k(s)/k(x))xi_x.                          (6.1)

These are legitimate rational boundary classes; no trivialization
has been assigned to any Poincare bundle.

**[NEW] Proposition6.1.** The contribution of every pattern(6.1)
to the right side of(5.4) is zero.

*Proof.* Since u is a unit at every point above x, evaluation of
the finite function-field norm gives

    product_(s|x) Norm_(k(s)/k(x))(u(s))^(e_s)
                         =Norm_pi(u)(x)=±1.

The ramification multiplicities in this formula are necessary.
The right-cup projection formula and transitivity of trace now
identify the contribution with

    Tr_(k(x)/Q)(xi_x cup kappa(±1))=0

in rational motivic cohomology. This proves the stated vanishing
for these actual pulled-back patterns. Square.

The result does not prove chi_D nonzero and does not rule out
other boundary classes. It shows concretely that this natural
downstairs correction cannot remove a nonzero chi_D through(5.4).
It is consistent with the actual trace-zero K2 corrections(3.4).

## 7. A primary symbol theorem does not erase the needed degree

I also checked the precise ordinary Somekawa comparison in
[Kahn–Yamazaki, Theorems1.5,11.14 and12.3](https://webusers.imj-prg.fr/~bruno.kahn/preprints/Somekawa-Voevodsky31.pdf),
the40-page author version. Their algebraic-cycle formula gives
CH_(-r)(X,r). On the surface E_s×E_t, r=1 therefore gives
CH³(E_s×E_t,1), while r=2 gives CH⁴(E_s×E_t,2).
Neither is the point product CH³(E_s×E_t,2) in(2.8).
Applying that theorem with a changed higher-Chow degree would be
invalid. It supplies no vanishing relation for the present products.
No general vanishing or nonvanishing of those motivic groups is claimed.

The actual chains(2.9) remove the principal-divisor correction
DIFFERENCES in the abelian projection, and the actual symbols(3.1)
handle the specified variable toric residues. Neither calculation
annihilates the remaining fixed products(P−O)×beta2 and(Q−O)×beta2.
No rational cochain giving their needed boundary relation has
been constructed in this note.

## 8. Exact outcome and remaining arithmetic task

The full motivic obstruction is the explicit class(1.2). Its
first exterior/abelian component is the actual point/K2 product
in(2.8), with positive divisor frames and the derived exterior
coefficient one. The fixed h_j relations, the variable rational
K2 correction symbols, their tame residues and their proper
trace zero are calculated. The full added-boundary localization
and the degree-dependent RIGHT-cup sign give the necessary
finite-unit-span condition(5.4). The particular pulled-back
correction(6.1) has exactly zero contribution.

**[GAP MRBL-389].** Produce the rational global coefficient class
in(1.3), or an explicit nullcochain for(1.2), for the KNOWN beta2
input. In the projected test, this requires controlling the
point×beta2 cycles and their actual added-boundary relation, then
the remaining toric/exterior component. Equality(5.4) alone is
not sufficient for the full lift. The original point/Artin
projector degree b, exterior projector2, all Tate factors, and
the nonzero Poincare boundary tuple remain unchanged.

Even a lift of this known rational boundary input would not make
the spectral class rational or determine its point-height
coefficient. The original target D_pt tensorB2 tensorQ(-2), with
coefficient6·389·388n_E and integral primitivity as conclusions,
remains separate. No old certificate, shared synthesis edit,
completed predecessor edit or new agent was used. All nine sections
have passed independent review in their stated scope.

## 9. The Tate component is actually zero; the remaining component

This is a further component test of the specific cycles(2.8), not a
claim that those cycles themselves vanish. Let h denote the
COHOMOLOGICAL h1 summand of RΓ(E,Q), so that its Betti cohomology
is H¹(E) in degree one. The canonical elliptic motivic decomposition
and symmetric-square identity give

    RΓ(E,Q)=1⊕h⊕1(-1)[-2],
    Sym²(h)=1(-1)[-2].                                    (9.1)

Here Sym² is the categorical projector using geometric interchange.
These are rational motivic identities. Primary references are
[Ancona–Enright-Ward–Huber1312.4171v2, Theorem3.1.4,
Theorem4.2.3 and Proposition4.3.5](https://arxiv.org/pdf/1312.4171v2),
whose inspected51-page version gives the canonical group-law
Kunneth decomposition and its elliptic degree-two summand.
Dualizing their homological convention gives(9.1).
No claim of faithful Betti realization is used to infer(9.1).

**[NEW] Proposition9.1.** Let z_P=([P]−[O])×beta2 and
z_Q=([Q]−[O])×beta2 in CH³(E×E,2)_Q. For the actual geometric
interchange t:E×E→E×E,

    (1+t^*)z_P/2=(1+t^*)z_Q/2=0.                          (9.2)

Equivalently these products lie entirely in the geometric MINUS
summand of h tensorh. The group of that summand has not been proved
zero here.

*Proof.* The point divisor is in the h summand: its degree iszero,
and H_M²(Q,Q1)=0 removes the other possible component. Beta2 also
lies entirely in h. Indeed its other two components in(9.1) lie
in H_M²(Q,Q2) and H_M⁰(Q,Q1), and both groups arezero rationally.
For the first vanishing, K2(Q) is torsion: the tame localization
sequence has kernel K2(Z)=Z/2 and quotient the DIRECT SUM of
finite groups F_p^*. This is
[Weibel, III5.2.2 and III6.5.1](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf).
The second vanishing is the weight-one motivic calculation already
used in§3.

Thus both products lie in the h tensorh component of
H_M⁴(E×E,Q3). The geometric PLUS projector on that component is
Sym²(h), which(9.1) identifies with1(-1)[-2]. Its group in the
present degree and twist is

    Hom(1,1(-1)[-2](3)[4])=H_M²(Q,Q2)=0.

This proves(9.2) motivically. The projector denominator2 remains
rational. Square.

Under Betti realization, geometric interchange on two degree-one
classes is MINUS ordinary interchange. Consequently the remaining
geometric MINUS motive has its degree-two realization equal to the
ordinary rank-three symmetric square of H¹(E). The Tate PLUS
component and this remaining component must not be interchanged.
The same distinction was essential for the marked exterior frames.

The calculation proves a rational zero for this SPECIFIED Tate
projection. It neither produces a nullcochain for the full cycles
z_P,z_Q nor controls their remaining non-Tate component, the toric
part of F or the boundary selection in(1.3). GAP MRBL-389 is
unchanged except that this Tate component has now been eliminated.
This additional component calculation passed independent review
along with the preceding eight sections.
