# The Poisson source as an exact canonical Deligne invariant

Date: 2026-09-13. Author: root/coordinator. **All seven sections passed
[independent review](review-poisson-hodge-framing.md).**
[Restart checkpoint](poisson-hodge-framing-checkpoint.md).
Full BSD over Q remains active and unresolved. All claims marked NEW below
are deductions about this specific construction, not claims of novelty.

## 1. Fixed inputs and the statement

Use every normalization in the reviewed
[finite iterated-source formula](poisson-iterated-source-attack.md):
X=X0(389), Y=X\{0,infinity}, alpha=pi*omega_E=c_pi(2pi i)f dz,
theta=dlog u, u=389^-6 Delta(z)/Delta(389z), l=log|u|.
Let b belong to the reduced finite algebraic scheme u^-1(2), and write

    A=int_b^z alpha,  Atilde=int_b^z rho,  B=int_b^z theta,
    l'=Re B=l-log2,  v=bar A-Atilde.

The second-kind rho has all compact periods equal to those of bar alpha,
only possible pole infinity, and zero residues. Thus v is single-valued
and v(b)=0. All iterated words are EARLIEST-FIRST:
I_(eta,xi)=int (int_b^x eta)xi. Prefixing a loop h adds
I_(eta,xi)(h)+(int_h eta)(int_b^z xi). No word reversal is implicit.

The old construction defines the cusp principal parts
s_c=pp_c[(bar A_c-Atilde)theta], a meromorphic differential xi_b with
these principal parts, and the unique compact holomorphic correction eta_b
whose real periods make

    U_b=Re(2l A-I_(alpha,theta)-I_(rho,theta)-int_b^z(xi_b+eta_b))

single-valued. It proves q_F=(U_b-U_b(infinity))/(4pi c_pi), with a finite
cusp limit after cancellation. We retain that theorem as an input.

**[NEW] Main assertion.** There is an actual rational mixed Hodge structure
V_(b,z), obtained by the ordered pushout of the length-two path module in
§3, with top Q(0), bottom K=H1(E,Q)(1), and fixed geometric frames. Let eD
be the top Deligne lift, delta its real splitting operator, and pi_-3 the
Deligne weight projection to K. Define

    ell_omega(h tensor 1(1)_B)=int_h omega_E,
    h_(omega,b)(z)=Re ell_omega(pi_-3 delta eD).

Then, with no adjustable scalar,

    h_(omega,b)(z)=-U_b(z)/(4pi),
    q_F(z)=-(h_(omega,b)(z)-h_(omega,b)(infinity))/c_pi.       (1.1)

Here h(infinity) means the proved finite limit. We do not assert in this
note that it is an algebraic tangential fiber. The construction concerns
an actual rational realization and a canonical REAL Hodge operation;
it does not identify a rational motivic morphism or the BSD coefficient.

## 2. The complex loop character and the compact Hodge correction

**[NEW] Lemma 2.1.** The function on based loops

    G_b(h)=I_(rho,theta)(h)+overline{I_(alpha,theta)(h)}       (2.1)

is a complex additive character. Its cusp periods are
G_b(gamma_c)=-2pi i Res_c s_c. Consequently sum_c Res_c s_c=0,
without using the existence of q_F.

*Proof.* Write a_h=int_h alpha and b_h=int_h theta. The two concatenation
cross terms in (2.1) are bar a_h b_k and bar a_h bar b_k. Their sum iszero
because b_k is in 2pi i Z. This proves additivity, so G_b factors through
H1(Y,Z). For a small positive cusp loop transported to b, integration of
the single-valued local primitive gives

    I_(alpha,theta)(gamma_c)=2pi i m_c A_c,
    I_(rho,theta)(gamma_c)=2pi i Res_c(Atilde theta).

For completeness, if tau ends at x near c, Chen concatenation on
tau gamma tau^-1 adds Atilde(x) int_gamma theta to the local based
integral. This cancels the subtraction of Atilde(x) in that local
primitive. The formula remains valid when Atilde has a pole. Conjugation
of the first identity changes the sign of 2pi i, proving the residue
formula. The sum of the two oriented cusp loops iszero in H1(Y), giving
the stated compatibility. The differential Mittag-Leffler criterion
therefore supplies xi_b by the same finite Riemann-Roch system. QED.

Set Lambda_b=G_b+[xi_b]. Its cusp periods vanish by Lemma 2.1, so it is
a class in H1(X,C). Write its pure Hodge decomposition as
Lambda_b=Lambda10+Lambda01, and also use these symbols for the unique
holomorphic/antiholomorphic differential representatives.

**[NEW] Lemma 2.2.** The old correction is exactly

    eta_b=2log2 alpha-Lambda10-overline{Lambda01}.            (2.2)

Indeed Re Lambda is the real part of the sum of xi periods and BOTH old
iterated periods. The real periods required of eta_b are
2log2 Re a-Re Lambda. The right side of (2.2) has these periods and is
holomorphic. Uniqueness is the real compact-period isomorphism proved in
the previous note. This retains all compact genus directions.

## 3. The rational ordered pushout and its exact frames

Put H=H1(Y,Q), H_E=H1(E,Q). The actual algebraic maps pi and u give MHS maps
pi_*:H->H_E and u_*:H->Q(1). In the residue exact sequence
0->Q(1)->H->H1(X,Q)->0, the positive cusp class gamma_0 maps under u_*
to 388 times 1(1)_B. Thus

    t=gamma_0/388,  H_X=ker u_*,  H=H_X direct-sum Q(1)t,    (3.1)

and H_X maps isomorphically to H1(X,Q) as a MHS. This is a rational
splitting with denominator388. No primitive integral splitting is claimed.
The compact map pi_* kills t.

Let P_j(b,z) be the rational path module modulo augmentation length j+1,
with its natural augmentation to Q. For b!=z its homological geometric
realization at j=2 is

    H2(Y²,({b}xY) union Delta_Y union (Yx{z});Q).

The triangle (gamma(s),gamma(t)), 0<=s<=t<=1, oriented ds wedge dt,
specifies our chronological tensor convention. For b=z retain the
constant Q-line in addition to I/I³. The geometric path theorem and
compatibility of truncation and multiplication are supplied by
[Looijenga2403.03748v2, Theorem1.1, Corollary3.1, Example4.5 and final
paragraph](https://arxiv.org/pdf/2403.03748v2). Since the fundamental group
of this affine curve is free, multiplication identifies I²/I³ with
H tensor H. Equivalently there is no compact H² cup relation on Y.
Consequently the geometric truncation sequence is

    0 -> H tensor H -> P2(b,z) -> P1(b,z) -> 0              (3.2)

in rational MHS, independently of any path used to describe it.
Algebraic de Rham comparison and its logarithmic Hodge filtration are
as in [Hain math/0109204v2, Theorems13.6–13.7](https://arxiv.org/pdf/math/0109204).
The cited PDF has the v2 arXiv stamp26October2001.

Use the ORDERED, surjective rational MHS map

    lambda:H tensor H -> K=H_E(1),
    lambda(a tensor b)=pi_*a tensor u_*b.                  (3.3)

Push out (3.2):

    V_(b,z)=(P2(b,z) direct-sum K)/{(w,-lambda(w))},
    0 -> K -> V_(b,z) -> P1(b,z) -> 0.                    (3.4)

This is an actual object in the abelian category of rational MHS with
the compatible geometric Betti/de Rham construction. This note makes no
automatic passage from that quotient to a selected motivic cohomology class.
The weight pieces are Q(0), H_X, Q(1), K in weights0,-1,-2,-3.
K has types(-2,-1),(-1,-2). The top and bottom frames in §1 are fixed by
augmentation, pi and the DECLARED Betti Tate generator. In particular the
central alpha-theta covector restricts to 2pi i ell_omega, not ell_omega.

## 4. Two canonical central Hodge covectors

All covectors below are in V_(b,z)^dual_C. Set

    f_alpha=I_(alpha,theta),
    f_rho1=I_(rho,theta)+int xi_b,
    f_rhoD=I_(rho,theta)+int xi_b-int Lambda10.              (4.1)

They factor through (3.4), because their restrictions on H tensor H are
the corresponding compact alpha or bar alpha period, followed by the
theta period. This is precisely (3.3); length-one corrections vanish there.

**[NEW] Lemma 4.1.** The covectors f_alpha and f_rhoD are the canonical
Deligne lifts in I^(2,1) and I^(1,2) of their central covectors.

*Proof.* The logarithmic bar representative of f_alpha has two holomorphic
one-forms, so it is in F². The lower P1^dual has no F²; the only F² line
in V^dual is I^(2,1). This identifies the first lift uniquely.

The second-kind representative must be corrected before asserting its
filtration. Since rho=bar alpha-dv and v(b)=0, integration by parts gives

    f_rho1=I_(bar alpha,theta)+int(xi_b-v theta).            (4.2)

The differential xi_b-v theta has type(1,0) and
d(xi_b-v theta)=-bar alpha wedge theta. These are the closed-bar equations
in our earliest-first convention. At cusp c it equals a holomorphic
regular remainder minus bar a_c(q_c)theta: xi_b cancels the full principal
part of (bar A_c-Atilde)theta. It is therefore a smooth logarithmic form
(a smooth coefficient times dq_c/q_c is allowed). Formula (4.2) lies in
the F¹ logarithmic bar subcomplex. Hain's filtration theorem now proves
f_rho1 in F¹. The ordinary holomorphic correction preserves F¹.

By the exact restriction of prefix-loop functions, f_rho1+bar f_alpha
annihilates K and, on H within the augmentation-zero part, represents

    Lambda_b+2l' bar alpha.                               (4.3)

For example the two extra prefix terms are bar a_h B and bar a_h bar B.
There is no Tate component in (4.3), since all cusp periods vanish.
Subtracting int Lambda10 leaves only a compact (0,1) class. Therefore
f_rhoD+bar f_alpha lies in bar F¹ W1 plus W0 in V^dual. This statement
allows the possible weight-zero path constant; it does not set it tozero.

The exact Deligne formula at(p,q)=(1,2) is

    I^(1,2)=F¹ intersect W3 intersect
      (bar F² intersect W3 + bar F¹ intersect W1 + bar F0 intersect W0).

Thus f_rhoD lies in I^(1,2). Its central image fixes it uniquely, since
P1^dual has no weight3 piece. These Deligne formulas and the convention
that exp(-i delta) splits over R are those of
[Burgos Gil–Goswami–Pearlstein2410.17167v3, §2.1,
equations2.2,2.6–2.7](https://arxiv.org/pdf/2410.17167v3).
QED.

Changing xi_b by a compact holomorphic differential changes Lambda10 by
the same differential; these cancel in f_rhoD. Changing the second-kind
representative of the SAME cohomology class similarly leaves the canonical
lift unchanged by uniqueness. No rationality of the displayed period
coefficients is asserted.

On K the Tate comparison yields the useful EXACT identity

    f_rhoD|K=-bar f_alpha|K.                              (4.4)

Indeed the two restrictions on h tensor1(1)_B are 2pi i int_h omega and
2pi i overline{int_h omega}; scalar Betti conjugation negates 2pi i.
This is not geometric real Frobenius and those two conjugations are not
interchanged.

## 5. The real split compact lift

By the listed Hodge types, delta can only map top weight0 to weight-2
or-3, and weight-1 to weight-3. It kills weight-2 and-3. Hence delta²=0.
The I^(-1,-1) lift tD of the normalized Tate class inside W_-2 V is real:
the adjacent K has no component strictly lower in both indices.

Let s_H^D denote the Deligne lift of H_X into W_-1 V, and put
hat s_H=exp(-i delta_-)s_H^D, the canonical real split lift. Here delta_-
is the restriction to W_-1; it maps only H_X to K. For the chosen path
gamma let r_H be the unique element of H_X,R whose periods against ALL
compact holomorphic forms equal their path integrals. Existence and
uniqueness follow from the real compact-period isomorphism. In particular
alpha(r_H)=A and theta(r_H)=0.

Choose any real lift R_r of r_H in the augmentation-zero path module,
viewed in V. Concretely use a real combination of prefix-loop differences;
the cusp loop gamma_0/388 removes any Tate component. The difference
R_r-hat s_H(r_H) belongs to K_R.

**[NEW] Lemma 5.1.**

    2 f_alpha(hat s_H(r_H))
      =2l' A+int_b^z overline{Lambda01}.                   (5.1)

*Proof.* The two covectors in Lemma4.1 vanish on all Deligne H_X lifts.
Write y_r=delta_- hat s_H(r_H), which is real in K. Since delta²=0,
their values on hat s_H are -i f_alpha(y_r) and -i f_rhoD(y_r).
Equation(4.4) gives
f_rhoD(hat s_H(r_H))=overline{f_alpha(hat s_H(r_H))}.
Also f_alpha+bar f_rhoD vanishes on K_R. Its evaluation can therefore
be calculated on R_r instead, and (4.3) gives

    2 f_alpha(hat s_H(r_H))
      =f_alpha(R_r)+bar f_rhoD(R_r)
      =2l' A+overline{Lambda01(r_H)}.

The last term equals the path integral of the holomorphic differential
bar Lambda01 by the defining ALL-form period property of r_H. QED.

## 6. Top lift, conjugation, and the scalar

Let eB be the real Betti path vector [gamma]. Set

    e'=eB-hat s_H(r_H)-(B/(2pi i))tD.                      (6.1)

It has augmentation1 and annihilates all first-order F¹ covectors:
the compact periods are removed by r_H and the logarithmic period by tD.
Since f_alpha and f_rhoD form a basis of K_C^dual, there is a unique vK
such that their values on vK agree with their values on e'. Put

    eD=e'-vK.                                            (6.2)

This vector annihilates all of F¹(V^dual), so lies in F0 V. Moreover
bar eD-eD is in W_-2 because the compact lift in (6.1) is real.
The Deligne formula for I00 now identifies it as the top lift: in this
weight range its lower correction term is all W_-2. More explicitly
bar F^-1 W_-2 contains the Tate piece and bar F^-2 W_-3 contains K.
The two central Deligne covectors vanish on tD by their types.

The real splitting convention and delta²=0 give
bar eD=eD-2i delta eD. Applying conjugation directly to (6.1)-(6.2),
and using Re B=l', yields

    delta eD=(l'/(2pi))tD+(bar vK-vK)/(2i),
    y:=pi_-3 delta eD=(bar vK-vK)/(2i).                   (6.3)

The projection here is the declared Deligne projection; tD is the real
weight-2 lift. The central term y is real. If vK=x+i w with x,w in K_R,
then y=-w, and (4.4) and the comparison 2pi i ell_omega give

    Re ell_omega(y)
      =(1/(4pi))Re(f_alpha(vK)+f_rhoD(vK)).                (6.4)

For instance the sum on x is purely imaginary and the real part on i w
is -4pi Re ell_omega(w), which verifies both the sign and the factor.

Subtracting (5.1) in the evaluation of (6.1), we obtain

    Re(f_alpha(vK)+f_rhoD(vK))
      =Re(I_(alpha,theta)+I_(rho,theta)+int xi_b
           -int Lambda10-2l' A-int bar Lambda01)
      =-U_b(z),                                         (6.5)

where the last equality is precisely (2.2). Equations(6.4)-(6.5) prove
the first assertion in (1.1); the completed finite Poisson theorem proves
the second. This is a direct framed calculation, with no period or
regulator rescaling chosen to fit the answer.

## 7. Exact scope and remaining arithmetic step

For algebraic b,z the source is a rational geometric Betti/de Rham
realization and its actual ordered MHS pushout. The operation delta,
the Deligne projections and ell_omega with its Tate comparison are now
specified canonically. The argument also proves the principal-part
compatibility without assuming the Poisson solution. Basepoint averaging
over the reduced finite scheme u=2 retains all conjugates, with rational
averaging denominator; the cusp-normalized expression is independent of b
by the completed uniqueness theorem.

This identifies the exact canonical Hodge operation behind the formerly
explicit real normalization. It does not make that operation rational.
It does not identify the Petersson/theta functional with an arithmetic
intersection, lift the marked coefficient obstruction motivically, prove
the integral point/K2/Tate comparison, or settle any universal BSD case
beyond the previously reviewed results. These are still separate targets.
The full compact-genus correction, ordered tensor map, denominator388,
constant-line exception, positive cusp orientation and 2pi i Tate factor
have all been retained. No old numerical certificate was rerun.

The independent audit checked (3.2), (4.2) and its logarithmic filtration,
the allowed path constant in I^(1,2), the I00 criterion, and signs/factors
in (5.1), (6.3)-(6.5). No mathematical correction was required. Its exact
reviewed mathematical revision is recorded in the review; these completion
and review-link edits are editorial.
