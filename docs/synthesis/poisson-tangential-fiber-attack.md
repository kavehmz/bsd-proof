# An actual tangential motive for the finite Poisson cusp value

Date:2026-09-13. Author: root/coordinator. **All eight sections passed
[independent review](review-poisson-tangential-fiber.md).**
[Restart](poisson-tangential-fiber-checkpoint.md).
Full BSD over Q remains active and unresolved. The
[canonical Hodge formula](poisson-hodge-framing-attack.md) and
[actual path motive](poisson-path-motive-attack.md), with their separate
reviews, are completed inputs. This note constructs their missing
tangential source and identifies its exact central real invariant.

## 1. Rational local parameter and fixed cusp data

Keep X=X0(389), Y=X minus its two rational cusps, E=389a1,
alpha=pi*omega_E, theta=dlog u, and

    u=389^-6 Delta(z)/Delta(389z).

The basepoint b belongs to the fixed reduced finite scheme u^-1(2).
Write c=infinity. Its modular formal coordinate q defines a rational
nonzero cotangent vector dq|c. Choose an ACTUAL element t in the rational
local ring O_(X,c) such that t/q->1. Such an element exists because
the maximal ideal modulo its square is the one-dimensional rational
cotangent space. After shrinking an algebraic neighborhood W_c of c,
t is regular, has no other zero, and t:W_c->A1_Q is etale at c.
We can shrink further to make it etale on W_c. The formal q parameter
is not silently assumed to be a rational function on X.

Put W_c^*=W_c minus c. The expansion in this actual parameter is

    u=a_c t^(m_c)(1+O(t)),  m_c=-388,  a_c=389^-6.         (1.1)

It follows directly from the leading terms of the two Delta series
and t/q->1. At c=0, the normalized Fricke formal parameter similarly
has m_c=+388 and a_c=389^6, since u composed with Fricke is u^-1.
All assertions below can be applied separately at either cusp.

Let V_mot,b be the completed ordered source over the endpoint curve
(over the number field of b), and V_mot,av its actual finite-base
average over Q. Their bottom is K_mot=H_E,mot(1), and their top maps
to1. The averaging source retains its extra compact and Tate middle
directions. No middle quotient is discarded at the cusp.

## 2. Actual motivic unipotent specialization and its normalization

Use the rational motivic Kummer object K_t over Gm, in the triangle
1(1)->K_t->1 whose connecting class is the coordinate t.
Let Log_n=Sym^n K_t, with the canonical transition maps of the
logarithmic pro-object. Define its dual ind-object by the ACTUAL duals
Log_n^dual and their dual transition maps. On Hodge realizations these
have weights0,2,...,2n. If expressed through the determinant identification,
Log_n^dual is Sym^n K_t(-n), not Sym^n K_t(n).

For j:W_c^*->W_c and i:c->W_c the ordinary unipotent functor is

    Upsilon_t(M)=colim_n i* j_*(M tensor t*Log_n^dual).      (2.1)

This is an actual functor in the stable rational motivic category, not
an operation defined by its Betti realization. The logarithmic construction,
its equivalence with motivic unipotent nearby cycles and its preservation
of constructibility are in
[Ayoub, The motivic nearby cycles and the conservation conjecture,
§4.6, Definitions4.29/4.32, Proposition4.42 and its proof](https://user.math.uzh.ch/ayoub/PDF-Files/Leiden.pdf).
The inspected author PDF has42pages; the constructibility conclusion is
explicit in the paragraph following Corollary4.46. This applies over Q
and the finite number fields here, in characteristiczero. The rational
Beilinson/transfer-motive comparison is the one already checked for our
smooth bases. Each finite logarithm is dualizable as an iterated Tate
extension. No motivic t-structure or Betti-faithfulness assertion is needed.

Set the specified cusp motives

    V_(b,c)^tan=Upsilon_t(V_mot,b|W_c^*),
    V_(av,c)^tan=Upsilon_t(V_mot,av|W_c^*).                 (2.2)

They are constructible rational motives over the corresponding field.
Because t is etale at c, specialization of a constant coefficient is
that same coefficient, with its natural unit frame. Exactness therefore
gives ACTUAL frame maps K_mot->V^tan->1 by applying the functor to the
old frame maps. Finite proper pushforward commutes with specialization;
the old Artin top pullback and bottom Tr/degree(B2) pushout remain the
same rational averaging construction. No new averaging denominator occurs.

For clarity about realizations, the logarithmic model is compatible
with Betti realization as in
[Ivorra–Morel, Lemma3.13 and Corollary3.14](https://morel.perso.math.cnrs.fr/PerverseMotives.pdf).
For Hodge realization use its colimit-preserving six-operation comparison
and the identical logarithmic model. In
[Tubach2407.02256v3, Theorem1.4 and Proposition3.31](https://arxiv.org/pdf/2407.02256v3),
Upsilon_t[-1] is Saito's PERVERSE nearby functor. Our source is the
ordinary degreezero local system on a curve, so Upsilon_t ITSELF gives
its limit MHS in degreezero. We do not insert another[-1] or Tate twist.
The positive-weight logarithms and this shift are also checked directly
in [Saito, Extension of mixed Hodge modules, §1.1 and Proposition1.3](https://www.numdam.org/item/CM_1990__74_2_209_0.pdf).

Tensoring with the dual logarithm retains the full nearby fiber, not
just invariants of M. Choose the compatible dual divided-power polynomial
coordinate T, of weight2, in which positive Kummer transport acts by
T->T-1 on the dual logarithm. The total logarithm is L-d/dT.
It is surjective on V[T]; its kernel is exp(T L)V.
Thus its degreezero cohomology is the full V and its degreeone cohomology
iszero. This illustrates the comparison, but constructibility in(2.2)
uses the actual motivic theorem, not stabilization guessed from this model.

## 3. Endpoint monodromy and the unchanged limit weights

Let T_c be positive endpoint PATH TRANSPORT on Betti homology and
L_c=log T_c. The notation L_c denotes a REAL Betti endomorphism.
The motivic monodromy is Tate-valued; its coefficient in the declared
Betti Tate generator corresponds to this logarithm. A factor2pi i in
de Rham comparison is not a rational change of Betti basis.

**[NEW] Lemma3.1.** On the ordered pushed path source,

    L_c²=0,  L_c W_r subset W_(r-2).                      (3.1)

It kills the bottom K and the middle Tate direction. On the compact
middle H_X it is the ordered product with the cusp cycle, followed by
pi_* tensor u_*.

*Proof.* Transport appends a positive local cusp loop to a path. On the
length-one quotient it adds the cusp class m_c times the normalized
Tate direction, with no compact homology contribution. On a prefix-loop
difference its new term is the chronological product of that compact
loop and the cusp loop. The completed ordered lambda sends it toK.
If the first loop is a cusp, pi_* kills it; hence the middle Tate line
has no such term. Degree-two products are fixed modulo lengththree.
This proves both assertions in(3.1), and T_c=1+L_c. Any central term
on a chosen top Betti lift also lands inK and is then killed. QED.

The source Hodge realization is an admissible variation: it is a smooth
mixed Hodge module obtained from the actual geometric construction.
This smooth/admissible criterion and the relative monodromy condition are
given by [Saito1605.00435v5, §3.1 and Theorem3.4](https://arxiv.org/pdf/1605.00435v5).
Its GrW pieces are constant. Therefore the induced L_c on each GrW iszero,
and W itself satisfies the defining relative-monodromy conditions by(3.1).
Uniqueness of that filtration shows that the LIMIT weight filtration is
the same W, with weights0,-1,-2,-3. In particular the limit top and
bottom maps have the same graded frames, and delta²=0 as before.

The limit MHS and its tangent dependence can be read in the explicit
canonical-extension formulation in
[Hain, The rank of the normal functions of the Ceresa and Gross–Schoen
cycles, §11, Propositions11.1–11.2](https://dukespace.lib.duke.edu/server/api/core/bitstreams/757f44c8-ab9d-4eda-b0e3-315bd58b160d/content),
the published40-page2025 version. The monodromy is a morphism of type
(-1,-1) on that limit. The tangent dq(v)=1 is the one selected in§1.

Our period-map sign is fixed independently. If z=log t/(2pi i), the
homological period map in flat Betti coordinates has leading orbit

    F(t)=exp(-z L_c)F_tan,                                (3.2)

up to the holomorphic vanishing correction. For the coordinate Kummer
extension this says eD=eB-(logt/(2pi i))tB. Its positive transport is
eB->eB+tB, proving the minus in(3.2). A convention using the inverse
transport logarithm writes the same formula with a plus instead.

## 4. The actual corrected period table at the tangent

Use every notation from the completed Hodge proof. In particular
A=int_b^z alpha, B=int_b^z theta, Atilde=int_b^z rho,
Lambda=G+[xi_b]=Lambda10+Lambda01, and the canonical dual covectors are

    f_alpha=I_(alpha,theta),
    f_rhoD=I_(rho,theta)+int xi_b-int Lambda10.              (4.1)

Let A_c be the finite compact alpha integral to c. For a compatible
branch put B_c^tan=lim(B-m_c logt). By(1.1),

    Re B_c^tan=log|a_c/2|=:l_c^tan.                       (4.2)

The imaginary branch is retained; it is not used to change a real scalar.
Every compact holomorphic integral has its analogous finite limit.

**[NEW] Lemma4.1.** The regularized canonical central covectors have
finite values

    f_alpha,c^tan=lim[f_alpha-m_c A_c logt],
    f_rho,c^tan=lim[f_rhoD-m_c bar A_c logt].               (4.3)

Together with the compact periods and B_c^tan, these are the actual
filtered Betti/de Rham period table of the tangential specialization.

*Proof.* Locally A=A_c+O(t), so
df_alpha=A theta=m_c A_c dt/t plus a regular differential.
The second-kind primitive Atilde may have poles, but the completed xi_b
has EXACT principal part pp[(bar A_c-Atilde)theta]. Consequently

    d f_rhoD=Atilde theta+xi_b-Lambda10
             =m_c bar A_c dt/t plus a regular differential.

This proves(4.3); the poles are canceled before taking a finite part.
It does not regularize the uncorrected second-kind word by itself.

To check the full table rather than just top values, for a fixed based
loop h the prefix-loop differences have rows

    f_alpha: I_(alpha,theta)(h)+a_h B,
    f_rhoD: I_(rho,theta)(h)+int_h xi_b-int_h Lambda10+bar a_h B.

Thus their only varying logarithmic terms are m_c a_h logt and
m_c bar a_h logt. On the cusp middle direction these terms arezero,
since its compact period iszero. On K the covectors are constant and
retain f_alpha=2pi i ell_omega and f_rhoD=-bar f_alpha.
This matches the action in Lemma3.1 on every weight piece. Untwisting
the dual rows by the inverse of(3.2) removes exactly these logarithms.
The resulting table is the canonical-extension limit, which is the
Hodge realization in§2. The actual constant path/top frame supplies
its retained weightzero term. QED.

The regularized f_alpha is the canonical I^(2,1) lift in the limit:
it is F² and there is no F² in the lower first-path quotient.
For f_rho,c^tan, the lower restriction of its sum with bar f_alpha is
Lambda01+2l_c^tan bar alpha, with no Tate component, plus the possible
top constant. It is still F¹ by the canonical extension of the filtered
source. The SAME Deligne formula used in the completed proof therefore
identifies it as the canonical I^(1,2) lift. The top constant is allowed
by that formula and is not discarded.

## 5. Exact equality of the tangential scalar and the finite limit

Let eD_c be the top Deligne lift in the limit MHS, and define, with
the SAME bottom elliptic/Tate functional,

    h_b,c^tan=Re ell_omega(pi_-3 delta eD_c).               (5.1)

**[NEW] Theorem5.1.**

    h_b,c^tan=lim_(z->c) h_b(z).                          (5.2)

In particular no additional rational, logarithmic or Tate scalar is
needed to identify the former finite part with this actual source.

*Proof.* The finite-dimensional Deligne calculation in the completed
Hodge note uses precisely the first-order rows, the two canonical central
rows and their lower restriction character. Lemma4.1 supplies the same
data at the tangent, with B replaced by B_c^tan and A by A_c. Repeating
that algebra, or substituting this table in its equations(5.1),(6.3)–(6.5),
gives

    h_b,c^tan=-1/(4pi) Re[2l_c^tan A_c
                         -f_alpha,c^tan-f_rho,c^tan
                         +int_b^c bar Lambda01].          (5.3)

All compact genus periods remain in the last term and in the canonical
real compact lift. There is no elliptic-only replacement of that lift.

The completed formula for a finite endpoint is the same expression with
l'=Re B,A,f_alpha,f_rhoD and int_b^z bar Lambda01. Write each term
using(4.2)–(4.3). Its possible unbounded real part is

    Re[2m_c log|t| A_c-m_c(A_c+bar A_c)logt]=0.

The remaining errors are O(|t| |log|t||) plus O(|t|) on a bounded branch.
Thus its limit is exactly the bracket in(5.3). The expression is already
single-valued by the previous theorem, so this gives the unrestricted
cusp limit. This proves(5.2), using the ACTUAL limiting Hodge table
rather than a general unproved continuity claim for arbitrary heights.
QED.

There is also a structural check of the cancellation. On the nilpotent
orbit exp(w L_c)F_tan, where w=-logt/(2pi i), functoriality gives
[delta_tan,L_c]=0 and

    delta_orbit=delta_tan+Im(w)L_c,
    eD_orbit=exp(w L_c)eD_c.

This follows by applying exp(-i(delta_tan+Im(w)L_c)) and the uniqueness
of the real splitting. The Deligne projections transform by the same
exp(wL_c). Since L_c eD_c lies in the Tate I^(-1,-1) part, its projection
to weight-3 iszero. Hence the central quantity(5.1) is exactly constant
on the orbit. The explicit table argument above controls the vanishing
correction and fixes the chronological sign, including the2pi i factor.

Changing the tangent by a nonzero complex scalar changes the limiting
period table by another such orbit translation. Therefore this CENTRAL
real scalar is independent of that change, even though the full framed
limit MHS can change. We assert no rational motivic isomorphism between
different tangent choices merely from equality of their central scalars.

## 6. Averaging, both cusps and the exact Poisson formula

Apply the construction directly to the actual averaged motive overY.
Proper finite-base compatibility, exactness and the old trace denominator
show that its central tangential scalar is

    h_av,c^tan=(1/degree(B2)) sum_b h_b,c^tan.              (6.1)

Every conjugate is retained, with the same fixed bottom map. By(5.2)
this equals the previous limit h_av(c). Hence the original canonical
Poisson function has the expression

    q_F(z)=-(h_av(z)-h_av,infinity^tan)/c_pi.               (6.2)

The subtracted constant is now the canonical real invariant of an
ACTUAL rational cusp motive. It is not an unassigned analytic finite
part. The already proved q_F(0)=q_F(infinity)=0 also gives
h_av,0^tan=h_av,infinity^tan. That equality is a real invariant equality,
not a claimed motivic identification of the two cusp objects.

The Kummer first-path component remembers the actual leading unit:
at infinity its regularized log is log(389^-6/2), and at0 it is
log(389^6/2), with their compatible complex branches. The real values
of the central scalar agree after the FULL correction despite these
different first-path data. Neither leading unit is set to1.

## 7. Completed substep and remaining arithmetic comparison

The new source is an actual constructible rational motive defined by
unipotent specialization of the already constructed path motive. Its
ordinary realization is the full tangential limit MHS in degreezero,
with unchanged top/bottom frames and the actual averaging denominator.
Its central Deligne scalar is exactly the finite cusp value in the
Poisson formula. The formal modular coordinate has only selected a
rational tangent; an algebraic uniformizer was used for the functor.

This does not make delta a rational motivic map, prove a rational
spectral class, remove the marked point–K2 obstruction, identify the
Petersson operation with an arithmetic pairing, or produce the universal
BSD leading coefficient. The existing Deligne-nilpotence comparison
constraint remains. The next arithmetic operation must still retain all
point/K2/Tate and integral frames.

The independent review audited the actual logarithmic specialization and
constructibility/realization hypotheses, dual-logarithm Tate sign, ordinary
versus perverse shift, positive transport sign, relative weight filtration,
complete regularized period table and exact scalar cancellation. No old
numerical certificate or period computation was rerun.

## 8. The actual fiber trace removes the cusp constant entirely

This additional construction uses the multiplicities of the SAME algebraic
fiber u=2. It does not assume that this fiber is unramified. Let
r:X->P1 be the finite map defined by u. Its degree is388, because
div(u)=388(c0-c_infinity). Write

    div(u-2)=sum_(b in B2) e_b[b]-388[c_infinity].           (8.1)

In this formula closed-point residue degrees are understood; after base
change to C, sum_b e_b=388. Each e_b is a positive integer constant on
Galois conjugates, so it defines an ACTUAL endomorphism E_B of the finite
Artin motive A=q_*1_(B2×Y), acting by e_b on its components.

**[NEW] Proposition8.1.** For every lambda inP1, with fiber multiplicities,

    sum_(x in r^-1(lambda)) e_x q_F(x)=0.                 (8.2)

*Proof.* The original curvature identity can be written as a current on X:

    dd^c q_F = i/(16pi² c_pi)
                    (alpha wedge bar theta+theta wedge bar alpha).

This is the completed normalization: the earlier Phi_b had curvature
4pi c_pi ReF dmu. The right side is locally integrable at both cusps.
The proved q_F=O(q log|q|) after its cusp constant has no hidden
delta mass there; its boundary flux tends tozero. Thus the displayed
current equation holds on the compact curve, not only on Y.

On the complement of branch values, write theta=r^*(dw/w). Pushing
the equation by the proper map r gives the differential trace of alpha
and its conjugate. The trace r_*alpha is a GLOBAL holomorphic one-form
onP1, hence iszero. To verify regularity at a branch point directly,
choose local coordinates w=z^e and write alpha=sum_(n>=0)a_n z^n dz.
Summing the e inverse branches leaves only n=e-1+je, j>=0, yielding
a holomorphic series in w. The same argument applies at infinity in
its reciprocal coordinate. Thus no meromorphic trace pole is omitted.

The pushed right-hand side iszero off a finite set. It is an absolutely
continuous measure: a finite fiber has area measurezero, and the original
coefficients are locally integrable. It therefore has no atom at that
finite set and iszero everywhere. Consequently r_*q_F is a harmonic
distribution onP1, hence a constant smooth function.

Off the branch values this function is the ordinary sum of q_F over
the inverse branches. Continuity extends it to the fiber sum with
ramification multiplicities. At infinity the sole point is c_infinity,
of multiplicity388, and q_F(c_infinity)=0. The constant is thereforezero,
which proves(8.2). QED.

In particular sum_b e_b q_F(b)=0. The exact finite-endpoint Hodge formula
and h_b(b)=0 give h_b,infinity=c_pi q_F(b), and hence

    sum_b e_b h_b,infinity=0.                             (8.3)

This is an exact trace identity, not a numerical approximation or an
assumption that the individual cusp constants vanish.

**[NEW] Corollary8.2.** In the completed finite-base source construction,
replace the bottom map id_K tensorTr/degree(B2) by either

    id_K tensorTr_e,  or  id_K tensor(Tr_e/388),
    Tr_e=Tr compose E_B.                                  (8.4)

Keep the SAME top pullback along the Artin unit. These give actual
rational motives V_Sigma and V_e overY with the fixed bottom K and top1.
Their canonical central invariants satisfy EXACTLY

    h_Sigma(z)=sum_b e_b h_b(z)=-388 c_pi q_F(z),
    h_e(z)=h_Sigma(z)/388=-c_pi q_F(z).                   (8.5)

Both tangential central invariants at both cusps arezero.

*Proof.* The finite Artin endomorphism and trace in(8.4) are actual
motivic maps. Their composite with the unit is388, by(8.1).
The same exact top pullback/bottom pushout construction and functorial
Deligne splitting as in the completed path motive therefore give the
stated weighted sums. Using h_b(z)=-c_pi q_F(z)+h_b,infinity and(8.3)
proves(8.5). The tangent assertion follows from Theorem5.1 and the
already proved two zero cusp values. QED.

The first map in(8.4) uses integer multiplicities and the unnormalized
finite trace; no division by388 is inserted there. The second is its
specified rational normalization, retaining the primes2 and97. Neither
asserts that every earlier rational projector or the full source lattice
is primitive at those primes. A zero central cusp scalar is not a zero
motivic cusp object.

The exact spectral operation can consequently be written using the
UNNORMALIZED weighted source as

    M = pi/(4 sqrt(389) c_pi) <I_L(h_Sigma),R_omega>_Pet.    (8.6)

Indeed substitute(8.5) in the previously proved
M=-pi·388/(4sqrt(389))<I_L(q_F),R_omega>_Pet.
This removes the analytic cusp-constant subtraction by an actual
algebraic fiber trace. It does not turn the remaining Petersson/Hodge
operation into a rational arithmetic morphism or supply the BSD determinant.
This eighth section passed the same separate adversarial review, including
the full current/ramification argument and both weighted trace maps.
