# An actual rational motive for the ordered Poisson path source

Date:2026-09-13. Owner /root/higher_period_integrality,
GPT-6 Astra/xhigh. Complete bounded construction, independently reviewed
**[PASS for all seven sections](review-poisson-path-motive.md)**.
[Checkpoint](poisson-path-motive-checkpoint.md).
Full BSD over Q remains open.

The [completed Hodge framing](poisson-hodge-framing-attack.md) and
[its review](review-poisson-hodge-framing.md) are unchanged inputs.
We construct an actual rational motivic source and frame maps for
that ordered MHS. No motivic t-structure or faithfulness of a
realization is assumed.

## 1. Category, reduced homology and the ordered coefficient map

Keep X=X0(389), Y=X minus its two cusps, E=389a1, the actual modular
map pi, the rational Néron differential omega_E, and the exact unit

    u=389^(-6)Delta(z)/Delta(389z),
    alpha=pi^*omega_E=c_pi·2pi i f dz, theta=dlog u.

The reduced finite scheme B2=(u^(-1)(2))_red is the fixed one.
It is finite étale over Q and is not presumed an unramified fiber
of the rational map u.

Use the stable enhancement of rational Beilinson motives. For the
explicit diagrams below one may work first with strict complexes
of rational presheaves with transfers and then take their images
in DM_Q(T)=DM_B(T). Our bases T are smooth over Q. The comparison,
model and six-functor inputs are CD Theorem14.2.9, Corollary14.2.11,
Theorems15.2.1 and16.1.4/16.2.18 in the
[8September2019 author version,442pages](https://deglise.perso.math.cnrs.fr/docs/2019/DM.pdf).
Actual finite diagrams supply their nullhomotopies; we do not form
an unspecified cone solely in the unenhanced homotopy category.

For a smooth scheme Z write M(Z) for its homological motive. Define

    I_Y=Fib(M(Y)→1), H_mot=I_Y[-1],
    H_E,mot=h1(E)_hom[-1], K_mot=H_E,mot(1).                (1.1)

The augmentation is induced by the structure morphism. I_Y is
defined without choosing a point of Y. The elliptic h1 is the
actual Chow summand defined using O, with its positive geometric
homology frame; the canonical elliptic decomposition is the same
one used in the preceding point-product proof.

There are actual motivic morphisms

    p_H:H_mot→H_E,mot,  u_H:H_mot→1(1).                    (1.2)

The first is I_Y→M(Y)→M(E) followed by the h1 projector and shift.
For the second, the actual morphism u:Y→Gm respects augmentations,
so induces I_Y→I_Gm. The coordinate Kummer map on Gm identifies
I_Gm with1(1)[1], with the positive winding generator. Then shift
by[-1]. This identification is the weight-one calculation in
[MVW Theorem4.1 and its proof](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).
In Betti/de Rham comparison its coordinate period is2pi i. The
map is not divided by a period or by the modular degree.

Define the ORDERED map

    lambda_mot=p_H tensor u_H:
       H_mot tensor H_mot→H_E,mot tensor1(1)=K_mot.         (1.3)

This is the full tensor product; it is not symmetrized or
antisymmetrized. On realizations it is exactly
(a,b)↦pi_*a tensor u_*b. The previously used normalized cusp vector
gamma0/388 is therefore the same rational MHS vector, with the
same denominator. No primitive integral splitting is asserted.

## 2. The uniform labelled path complex

Initially let b,z be points over a number field F. The construction
also makes sense uniformly over

    T=B2×_Q Y,

where b and z are the two labelled sections of the constant curve
Y_T. All objects and maps in this section are actual algebraic
diagrams over that smooth Q-scheme. Set A=M_T(Y_T).
The face maps from Y_T to Y_T² are

    L(y)=(b,y), D(y)=(y,y), R(y)=(y,z).

Keep three LABELLED pair-point copies of T, named LD, LR, DR.
Their images are respectively(b,b),(b,z),(z,z), even when b=z.
Form the strict outer complex

    D2=1_T^3 --d2--> D1=A^3 --d1--> D0=M_T(Y_T²),          (2.1)

in cohomological outer degrees-2,-1,0. Here d1 is the sum of
the three face maps, and d2 has the matrix

                LD     LR     DR
       L        b_*    z_*     0
       D       -b_*     0     z_*
       R         0    -b_*   -z_* .                        (2.2)

Every column has equal images under its two face inclusions,
so d1d2=0 as an equality of actual correspondences. The matrix
therefore defines a strict complex before motivic localization.
Let R2_aug be its total object and set

    P2_mot=R2_aug[-2].                                     (2.3)

There is NO triple-intersection term in this definition. It is
a specified labelled diagram, not the full Čech complex of the
geometric union at a coincident pair of endpoints.

For comparison define the uniformly labelled first complex

    R1_aug=[1_b⊕1_z --(b_*,z_*)--> A],
    P1_mot=R1_aug[-1],                                     (2.4)

with the two terms of R1 in degrees-1,0. The endpoint copies
remain labelled separately when b=z.

**[NEW] Proposition2.1.** For b distinct from z, R2_aug identifies
with the ordinary relative motive

    M(Y²,(b×Y) union Delta_Y union(Y×z)),

and R1_aug with M(Y,{b,z}). At b=z there is an actual split
triangle

    1[2] --k--> R2_aug→
       M(Y²,(b×Y) union Delta_Y union(Y×b))→1[3],           (2.5)

where k has point coordinates(-1,+1,-1) in(LD,LR,DR).
After shifting[-2], its first line is the actual constant-path
unit in P2_mot.

*Proof.* For distinct endpoints, the three face curves have
exactly the three indicated pair intersections and no triple.
Proper descent for the normalization/closed cover identifies
the motive of the union with its two-term face/intersection
diagram. Taking its cofiber into M(Y²) gives(2.1): the cofiber
changes the Čech incidence j-i to i-j. This is motivic proper
descent, supplied by CD14.3.4; over the field F the constructible
motives and their duals give equivalently the cohomological
closed-cover descent. No assertion of a motivic kernel from a
Betti isomorphism is involved.

At b=z the full closed-cover complex has one additional triple
point in outer degree-3. Its differential into the three pair
points is precisely k=(-1,+1,-1). Thus the full relative motive
is the cofiber of the stated map1[2]→R2_aug. At equal endpoints
d2k=0. Projection to the LR point component is a map
R2_aug→1[2] whose composite with k is1. This proves the
split triangle and identifies its constant line algebraically.
The analogous first complex has constant vector(1,-1).

The relative-union comparisons in this proof are used on the
field fibers (or on the distinct-endpoint locus). Over all T
the definition is the smooth labelled diagram(2.1); we do not
assume improper base change for a singular total union at the
coincidence locus. The defining smooth motives and their maps
commute with base change directly. Square.

## 3. Actual truncation, augmentation and the chronological signs

There is a strict map

    R2_aug→R1_aug[1]                                      (3.1)

which selects the R-face component and sends LR and DR to the
labelled b and z endpoints respectively; it kills D0 and LD.
The differential of R1[1] is the negative of its original
differential. Equation(2.2) therefore checks(3.1) column by column:
LR maps to-b_* and DR to-z_* on both sides. Shift[-2] to obtain

    tr2:P2_mot→P1_mot.                                    (3.2)

Define aug1:P1_mot→1 by its b-point projection. Then

    aug2=aug1 tr2:P2_mot→1                               (3.3)

is exactly the LR corner projection of(2.1), after the shift.

**[NEW] Lemma3.1.** On Betti realization these maps are the
positive chronological truncation and path augmentation.
They keep the constant line when the endpoints coincide.

*Proof.* Let gamma be a path from b to z. Sample the triangle
(gamma(s),gamma(t)),0<=s<=t<=1, oriented by ds wedge dt.
Its ordinary boundary in Y² is

    D(gamma)−R(gamma)−L(gamma).

In the total relative chain model the lifted cycle is therefore

    (T_gamma; a_L=gamma,a_D=-gamma,a_R=gamma;
                  c_LD=-1,c_LR=+1,c_DR=-1).               (3.4)

Indeed its Y² boundary cancels against the three face chains.
The boundaries of those chains cancel against(2.2) applied to
the displayed point vector. Applying(3.1) gives
(gamma; +b,-z), the positive relative path in the first complex.
Applying(3.3) gives1. This fixes both maps without selecting an
unknown period or an unspecified homotopy.

For a constant path at b=z, T_gamma and all face chains are zero,
and the vector in(3.4) is k. It is the unit from(2.5), maps to
(1,-1) under tr2, and has augmentation1. Thus the constant
path has not been lost by replacing a labelled complex with the
literal coincident-endpoint relative pair. Square.

These are actual motivic maps of the displayed diagrams. Their
comparison with chronological truncation is also consistent with
[Looijenga2403.03748v2, Theorem1.1 and Corollary3.1](https://arxiv.org/pdf/2403.03748v2),
the13-page23June2024 revision. His opposite coordinate indexing
does not replace the ds wedge dt convention used in(3.4).

## 4. The shifted product and the motivic pushout

We specify the tensor-shift convention to remove a possible sign
ambiguity. For cochain complexes, let

    sigma:A[p] tensor B[q]→(A tensorB)[p+q],
    sigma(a tensorb)=(-1)^(q·deg_A(a))(a tensorb),           (4.1)

where deg_A is the UNSHIFTED cochain degree. The differential on
A[p] is(-1)^p d_A. Direct substitution checks that(4.1) is a
chain isomorphism. Fix this convention in the enhancement and
its realization.

Let i:I_Y→M(Y) be the reduced inclusion. The chronological
product map is the ACTUAL morphism

    j_chron =
      -sigma followed by
      (I_Y tensorI_Y)[-2]→M(Y²)[-2]→P2_mot.                (4.2)

The second arrow is the ordinary ordered Cartesian product of
motives. The last arrow is the D0 inclusion in the total complex.
There is no exterior projector in(4.2).

**[NEW] Lemma4.1.** The Betti realization of j_chron is the
ordered injection H1(Y) tensorH1(Y)→P2(b,z) given by Chen
multiplication of augmentation differences. Both tr2 and aug2
kill it with their specified ZERO nullhomotopy.

*Proof.* A Betti one-cycle of I_Y has unshifted cochain degree-1.
For p=q=-1, (4.1) sends the tensor of the shifted degree-zero
cycles to the NEGATIVE of their product cycle shifted[-2].
The explicit minus in(4.2) removes exactly that sign. Its image
is the positive product of one-cycles in the two chronological
coordinates.

Evaluation of an earliest-first length-two word on a product
(h-1)(k-1) is a_eta(h)a_xi(k). Pairing the positive product
cycle with p1^eta wedge p2^xi has the same value. These pairings
identify the full degree-two augmentation tensor for the free
fundamental group of Y, and give the claimed kernel map.
This agrees with Looijenga Example4.5. A different coherent
tensor-shift convention may absorb the written minus into sigma;
the actual calibration here is fixed by(4.1) and the positive
chronological product.

Finally tr2 and aug2 vanish on the D0 inclusion in(2.1).
Their composites with(4.2) are thus zero at the defining complex
level, which supplies the stated nullhomotopies before localization.
This is stronger than saying their realizations happen to vanish.
Square.

Define the rational motive

    V_mot =
      Cofib[(j_chron,-lambda_mot):
               H_mot tensor²→P2_mot⊕K_mot].                (4.3)

The actual bottom frame map is inclusion of K_mot into this
cofiber. The map(tr2,0) factors through it by Lemma4.1, giving
V_mot→P1_mot. The map(aug2,0) similarly gives the actual
augmentation

    K_mot→V_mot→1.                                        (4.4)

The cofiber universal property uses the SPECIFIED zero
nullhomotopies from Lemma4.1, not an arbitrary choice to obtain
the desired top value. Compatibility aug2=aug1 tr2 is retained.

We do NOT assert that the motivic fiber of P2_mot→P1_mot is
H_mot tensor², nor that K_mot→V_mot→P1_mot is an exact
sequence for an unconstructed motivic t-structure. The actual
frame maps exist without either assertion.

## 5. Realizations give exactly the reviewed ordered MHS

**[NEW] Proposition5.1.** Betti and Hodge realizations of V_mot
are concentrated in ordinary degree zero and identify, respecting
the maps(4.4), with the rational MHS V_(b,z) in the completed
Poisson Hodge-framing proof. Its compatible algebraic de Rham
realization has the same ordered word and Tate frames.

*Proof.* Y is a noncompact finite-type Riemann surface, with
ordinary homology only in degrees0 and1. Its augmentation removes
H0, so I_Y[-1] realizes H1(Y) in degree zero. The elliptic
Chow projector similarly makes H_E,mot realize H1(E) in degree
zero; its twist gives precisely K=H1(E)(1).

Choose a finite graph spine of Y through the two endpoints.
Its deformation retraction, applied simultaneously to both
coordinates, preserves the labelled faces. The relative path
pair therefore has a relative CW model of dimension two.
Looijenga Theorem1.1 gives vanishing below degree two, so the
relative homology is concentrated in degree two. For b!=z
Proposition2.1 gives P2_mot in degree zero with the full path
module. For b=z the split constant line in(2.5) adds exactly
the missing Q, also in degree zero. This is a direct relative
topology argument, not an inference of a motivic isomorphism.

The fundamental group of Y is free, so
I²/I³=H1(Y) tensorH1(Y). Lemma4.1 identifies the realized
map j_chron with its canonical injective path-kernel map.
The realized map(j_chron,-lambda) is consequently injective.
The cofiber(4.3) has no cohomology in degree-1 and its only
cohomology is the ordinary pushout

    (P2(b,z)⊕K)/{(w,-lambda(w))}.

This is exactly the already defined rational MHS V_(b,z).
The bottom map is injective on realizations: if(0,k) is in
the graph of(j,-lambda), injectivity of j forces k=0.
The augmentation is the path augmentation with coefficient1.
Thus the bottom and top frames match, rather than matching
only the dimensions of graded pieces.

All maps in the construction are geometric correspondences,
cofibers and fixed rational projectors. Hodge realization
preserves them after base change to C by
[Tubach2407.02256v3, Theorem1.4](https://arxiv.org/html/2407.02256v3#S1.SS2).
The algebraic/Betti bar comparison and its logarithmic Hodge
filtration are
[Hain math/0109204v2, Theorems13.6–13.7](https://arxiv.org/html/math/0109204v2).
With the orientation in Lemmas3.1/4.1, the central covector
I_(alpha,theta) restricts to2pi i ell_omega, exactly as in the
reviewed Hodge proof. No additional2,388, modular-degree or
Tate-period factor is introduced. Square.

The same labelled diagram is defined over all T=B2×Y, including
the coincidence locus. Its terms are the motives of constant
smooth families and labelled sections, and commute with base
change. Their Betti realizations are complexes of local systems;
their finite total cofiber is likewise locally constant as a
derived complex. One may identify the resulting degree-zero
local system explicitly on a contractible endpoint disk by
choosing continuous short paths and using(3.4) for their
concatenations with based loops. The prism homotopies of those
paths give the usual path transport; at b=z the constant cycle
is exactly k. Thus the construction does not glue unrelated
fibers by an arbitrary isomorphism. It realizes the augmented
path variation across that locus.

## 6. Finite-base descent and a single averaged source

Let q:T=B2×Y→Y be the finite étale projection, of degree
d=degree(B2/Q). Every basepoint conjugate is retained. The
relative motive V_mot above is defined over this Q-scheme T.
All its bottom coefficients are the pullback of
K_Y=H_E,mot(1) on Y. Put A=q_*1_T and V_sum=q_*V_mot.
The finite projection formula identifies the bottom source
with K_Y tensorA, and the top map has target A.

There are actual motivic maps unit:1_Y→A and trace:A→1_Y,
whose composite is multiplication by d. First pull the top
back along the unit:

    V_top=Fib[V_sum⊕1_Y→A],

where the map is the top augmentation minus the unit.
The fixed zero bottom-to-top nullhomotopy gives a map
K_Y tensorA→V_top. Then form the bottom pushout

    V_av=Cofib[K_Y tensorA→V_top⊕K_Y],                     (6.1)

with first component this inclusion and second component
-id_K tensor(trace/d). The unit and trace are the actual
finite étale adjunction maps; there is no Tate twist for
this relative-dimension-zero trace.

**[NEW] Proposition6.1.** V_av is a rational motive over Y
with actual top1_Y and bottom K_Y frame maps. Its realization
is concentrated in degree zero. On its complex fiber at z,
the canonical real Deligne quantity of the preceding Hodge
proof is the average

    h_av(z)=d^(-1) sum_(b in B2(C)) h_(omega,b)(z).          (6.2)

*Proof.* Finite pushforward is the direct sum of the geometric
fibers on realizations. Their top maps are surjective and
bottom maps injective. The first fiber in(6.1) is therefore
the ordinary pullback of the top diagonal, in degree zero;
the second cofiber is the ordinary pushout of its bottom
by trace/d, again in degree zero.

Deligne bigradings and the real splitting operator are
functorial for MHS morphisms. The top lift in this pullback
maps to the tuple of top lifts in all summands, and the
bottom pushout sends their central weight-minus-three
components to their sum divided by d. Applying the fixed
elliptic functional proves(6.2). This is a consequence of
the actual finite pullback/pushout construction, not a
rationality inference from averaging transcendental numbers.
Square.

At an algebraic endpoint z over a number field F, pullback
gives the corresponding motive over F with rational
coefficients. Further restriction of scalars to Q retains
all endpoint conjugates as well; no rational projection to
one arbitrarily chosen embedding is asserted. Over the
Q-defined parameter Y, (6.1) is already an actual relative
rational source. The denominator d is retained and is not
declared a unit at every prime.

## 7. The exact source now obtained and the remaining comparison

The framed identification in Proposition5.1 transports the
ALREADY PROVED Deligne calculation without changing any
normalization:

    h_(omega,b)(z)=Re ell_omega(pi_-3 delta e_D)
                 =-U_b(z)/(4pi).

Equation(6.2) and the earlier basepoint independence therefore give

    q_F(z)=-(h_av(z)-h_av(infinity))/c_pi.                  (7.1)

The infinity value is the proved finite LIMIT after the full
principal-part and compact-genus correction. This construction
does not identify it with an algebraic tangential fiber.
The root's canonical Hodge operation, logarithmic F1 repair,
weight-zero constant and scalar-conjugation convention remain
the ones proved in the completed Hodge note.

We have supplied an ACTUAL motive, its actual ordered maps,
specified augmentation nullhomotopy, coincident-endpoint
constant line, and finite-base descent. The framed MHS is
recovered by exact realization and explicit relative topology.
No motivic kernel isomorphism was inferred from that topology,
and no motivic t-structure or general realization-faithfulness
assertion entered the construction.

**[GAP PPM-389].** The Deligne splitting/projection and the
elliptic period in(7.1) are canonical REAL operations on this
rational source. They have not become rational motivic
morphisms. Constructing the arithmetic map to the fixed
point/K2/Tate determinant, with coefficient6·389·388 n_E
and its integral lattice as conclusions, remains open.
This source construction also does not remove the actual
marked-coefficient or added Poincare-boundary obstruction.

No old computation, certificate, shared synthesis edit,
predecessor proof edit or new agent was used. All seven sections
passed independent review in their stated source-motive scope.
