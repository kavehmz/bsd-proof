# An actual compact unit-cup trace and its full real image

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Completed bounded construction; all new deductions passed
[independent review](review-relative-cup-trace.md).
Restart: [checkpoint](relative-cup-trace-checkpoint.md).
The completed radial and beta2 proofs remain unchanged.
The universal objective is full BSD over Q, still unresolved.

We construct a rational morphism on the entire relative motivic
cohomology group, calculate its composite with the entire boundary
injection, and compute its Deligne realization on the spectral class.
The resulting retraction is rational. The spectral input is still
only a real Deligne class, and the real coefficient still lacks
the point-height determinant.

## 1. Rational objects, right cup and the compact trace

Keep
\[
 N=389,\quad X=X_0(N),\quad Y=X\setminus\{0,\infty\},\quad E=389a1,
 \quad V=X\times E,\quad B=\{0,\infty\}\times E .
\]
Let j:V^\circ=Y×E→V be the open immersion,
p:V→E the proper projection, f=pj and q:E→Spec Q.
The exact unit is
\[
 u(z)=N^{-6}\Delta(z)/\Delta(Nz),\qquad
 \operatorname{div}(u)=(N-1)([0]-[\infty]).
 \tag{1.1}
\]
Its motivic class kappa_u lies in H_M¹(Y,Q(1)); pull it to
V^\circ without changing notation. Neither its constant N^(-6)
nor either boundary marking is changed.

Use the cohomological compact-support convention
\[
 H^r_{M,c}(V^\circ,\mathbb Q(t))
 =\operatorname{Hom}\bigl(\mathbf1_{\mathbb Q},
                         (qf)_!\mathbf1_{V^\circ}(t)[r]\bigr).
\]
It agrees with H_M^r(V,B;Q(t)) for this proper pair.
This is the convention of
[Déglise, Definition1.5 and §1.6](https://deglise.perso.math.cnrs.fr/docs/2014/beijing.pdf)
and the localization triangle of
[Voevodsky, Proposition4.1.5](https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s5.pdf).

The ordinary cohomology action on compact cohomology gives
\[
 H^3_{M,c}(V^\circ,\mathbb Q(2))
       \longrightarrow H^4_{M,c}(V^\circ,\mathbb Q(3)),
       \qquad c\longmapsto c\cup\kappa_u .                \tag{1.2}
\]
The order in(1.2) is RIGHT cup. Since the cohomological degrees
are3 and1, it is MINUS left cup by kappa_u.
At the six-functor level it is induced by the actual morphism
1→1(1)[1] on V^\circ and the monoidal module action, with
the Koszul interchange chosen to give exactly(1.2).
No extension of this unit morphism across B is assumed.

Smooth purity gives
\[
 f^!\mathbf1_E=\mathbf1_{V^\circ}(1)[2].
 \tag{1.3}
\]
The trace is the actual adjunction counit, with twists retained:
\[
 f_!\mathbf1_{V^\circ}(3)[4]
   =f_!f^!\mathbf1_E(2)[2]
          \xrightarrow{\epsilon_f}\mathbf1_E(2)[2].
 \tag{1.4}
\]
Applying q_* and Hom(1_Q,-) defines
H_M,c⁴(V^\circ,Q(3))→H_M²(E,Q(2)).
The schemes are regular, smooth over Q, and the relative
dimension is one. Canonical orientation, purity and the
rational-motive comparison are
[Déglise–Fasel–Jin–Khan, TheoremA(I),(II),(V)](https://www.numdam.org/item/JEP_2021__8__533_0.pdf).
Only the smooth case is needed.

Equivalently, AFTER forming the compact cup, use
j_!1→1_V and then the proper smooth projection trace for p.
Indeed f_!f^!=p_*j_!j^!p^!, and the counit is the composite
p_*j_!j^!p^!→p_*p^!→1_E. This also fixes its compatibility
with the given compactification. It is not an ordinary
pushforward of cohomology from the nonproper open.

Define the actual rational morphism
\[
 \boxed{\mathsf T_u(c)=\operatorname{Tr}_f(c\cup\kappa_u):
 H^3_M(V,B;\mathbb Q(2))\longrightarrow H^2_M(E,\mathbb Q(2)).}
 \tag{1.5}
\]
The total degree and twist are (3,2)+(1,1)-(2,1)=(2,2).
The trace orientation sends a rational closed point of a
smooth proper curve to degree1. In Betti/de Rham coordinates,
its relative-dimension-one integration factor is(2pi i)^(-1).
This is the current/trace normalization of
[Burgos–Goswami1712.10150v2, §4.1 and Proposition5.5](https://arxiv.org/html/1712.10150v2).
Thus the later sign is testable by a cochain integral.

## 2. Composite on the whole motivic K2 group

Recall the PROVED rational injection
\[
 j_B(\beta)=\partial^+(\beta,0),\qquad
 H^2_M(E,\mathbb Q(2))\hookrightarrow H^3_M(V,B;\mathbb Q(2)).
 \tag{2.1}
\]
Here the fiber differential is D(c,b)=(dc,i^*c-db),
the natural ordinary projection is plus, and
partial^+(b)=(0,+b)=-partial_can(b).
The [beta2 boundary proof](relative-beta2-boundary-attack.md)
proved that both cusp restrictions are equal already motivically,
using the actual rational-equivalence chain from u/(N-1).
Projection to E realizes the full diagonal image.
We use the entire injection(2.1), without a rank-one
hypothesis on its domain.

Let
\[
 e_0=\partial^+(1,0)\in H^1_{M,c}(Y,\mathbb Q(0)).
\]
The compact product and its boundary compatibility give
j_B(beta)=e_0 external-product beta. This may be checked
in the same fiber cone: multiplying (0,1,0) by the
degree-two class beta gives (0,beta,0).
Moving beta past kappa_u produces no sign because
their degrees are2 and1. The projection formula therefore gives
\[
 \mathsf T_u(j_B(\beta))=\lambda\,\beta,\qquad
 \lambda=\operatorname{Tr}_Y(e_0\cup\kappa_u)
                       \in H^0_M(\mathbb Q,\mathbb Q(0))=\mathbb Q.
 \tag{2.2}
\]
This has reduced the FULL motivic composite to a rational
endomorphism of the unit object, not to an evaluation of beta.

**[NEW] Lemma2.1.** With the order and orientation above,
lambda=N-1.

*Proof.* In the actual Betti fiber cone choose a smooth real
cutoff rho on X which is1 near0 and0 nearinfinity.
Subtracting D(rho,0) from (0,1,0) represents e0 by -d rho,
with zero boundary. The Kummer class is represented by
du/u, whose period around a positively oriented small
circle is2pi i ord_c(u). Equivalently use i darg u;
the difference d log|u| is exact and has no boundary contribution.

The normalized trace thus computes the image of lambda as
\[
 \frac1{2\pi i}\int_Y -d\rho\wedge\frac{du}{u}.
 \tag{2.3}
\]
For X with small cusp disks removed, Stokes gives
integral d(rho du/u)=-2pi i(N-1): the inner boundary
at0 is clockwise and the other one has rho=0.
The unit's holomorphic nonvanishing local factor has
zero circle integral. Therefore(2.3) equals N-1.

The number lambda in(2.2) was proved to lie in Q BEFORE
this calculation. The map Q→C on endomorphisms of the
unit is injective, so(2.3) determines that rational
endomorphism. No faithfulness of a realization on
general motivic K2 classes is assumed. The positive
Kummer residue and point-degree trace are also directly
compatible with the source's logarithmic current formula
d[dt/t]=delta_0-delta_infinity, in Burgos–Goswami(4.3).
Square.

**[NEW] Theorem2.2.** On the WHOLE group H_M²(E,Q(2)),
\[
 \boxed{\mathsf T_u\circ j_B=(N-1)\operatorname{id}.}       \tag{2.4}
\]
Consequently
\[
 \mathsf R_u=\frac1{N-1}\mathsf T_u,\qquad
 \Pi_B=j_B\mathsf R_u
 \tag{2.5}
\]
are an actual rational retraction and an idempotent on
H_M³(V,B,Q(2)), respectively.

*Proof.* Combine(2.2) and Lemma2.1. Then
R_u j_B=id and Pi_B²=j_B(R_u j_B)R_u=Pi_B.
Square.

Changing to the opposite cup order or to the canonical
rather than positive boundary changes(2.4)'s sign.
No such change is made here. Division by N-1 is division
in Q; N-1=388 is not an integral unit at2 or97.
This proves no primitive integral splitting.

## 3. The native real Deligne cup, including its derivative term

Use the previously reviewed unit-normalized coordinates.
A real relative degree-three/twist-two class represented
by a smooth real (1,1) form S, closed under dd^c and
zero near both cusp fibers, has native form
\[
 c=2\pi i S .
\]
All classes used below have such representatives by the
[radial correction](radial-graph-correction-attack.md)
or the explicit beta2 cutoff. Set l=log|u| with its
FULL normalization from(1.1).

In the total Deligne complex the concise-complex map gives
\[
 G(c)=(\partial c-\bar\partial c,\ 2\partial c,\ c),\qquad
 G(l)=(\partial l-\bar\partial l,\ 2\partial l,\ l).
\]
For the chosen RIGHT product, whose first degree is3,
the third component is
\[
 2c\wedge\partial l-l\partial c+l\bar\partial c.
\]
The degree-four/twist-three concise complex projects this
to the real form part R(2), by half the sum with its
complex conjugate. Since bar c=-c, the result is
\[
 c\wedge(\partial l-\bar\partial l)
                         -l(\partial c-\bar\partial c).
 \tag{3.1}
\]
This uses the exact cochain products and projections of
[Burgos–Goswami, §§4.3–4.5](https://arxiv.org/html/1712.10150v2);
there is no replacement of the product by naive multiplication.

The native curve trace has factor(2pi i)^(-1).
It cancels the factor in c, yielding the following
native degree-two/twist-two ONE-FORM on E:
\[
 \boxed{\Theta_u(S)=\int_Y
 \left[S\wedge(\partial l-\bar\partial l)
                         -l(\partial S-\bar\partial S)\right].}
 \tag{3.2}
\]
Here integration means the actual fiber integral along Y.
The integrand has compact support in that variable.
The resulting form is imaginary-real, as required by
D²(E,2)=i A¹_real(E). The second term in(3.2) is retained.

**[NEW] Proposition3.1.** Formula(3.2) represents the real
Deligne realization of T_u on each class with the specified
relative representative. It is a closed one-form and
depends only on that relative Deligne class.

*Proof.* Equation(3.1) is the actual Deligne product.
After extension by zero it is a smooth form on X×E.
The proper projection formula for the Beilinson regulator,
Burgos–Goswami Proposition5.5, gives precisely the trace
factor and(3.2). The relative product is natural on the
fiber cone; its maps commute with regulator and the
extension by zero. Hence relative-exact changes give
Deligne-exact output.

One may also check closedness directly. Put
a_l=partial l-barpartial l. Since l is harmonic on Y,
d a_l=-2partial barpartial l=0 there.
The derivative of partial S-barpartial S is
-2partial barpartial S=0.
In the derivative of the integrand of(3.2), the
remaining terms from dS wedge a_l and
-dl wedge(partial S-barpartial S) cancel, using the
degree-three/degree-one interchange and the absence
of types(3,1),(1,3) on the surface.
Thus the output is closed. Square.

For additional clarity, with A(S)=integral_Y lS,
integration by parts gives the exact alternative form
\[
 \Theta_u(S)=2\int_Y S\wedge(\partial l-\bar\partial l)
                  -(\partial_E-\bar\partial_E)A(S).
 \tag{3.3}
\]
This does not discard the derivative term in general.
For the translation-invariant representatives constructed
from aOmega_D in the radial proof, A(S) is a constant
function of E, so that derivative is zero.
The formula with the full l remains our definition.

There are no unverified cusp limits here: S is smooth
and zero near both cusp fibers. Those representatives
were constructed from the actual spectral coefficient
with zero tangential constants, all cutoff estimates
already proved in the radial note. No product of j2
with a cusp Dirac or of arbitrary singular currents
is introduced.

## 4. Exact relation to the original logarithmic functional

The inherited functional is
\[
 {\cal P}(S)=\frac{i}{4\pi^2c_\pi}
               \int_{Y\times E}S\wedge\omega_E
                                  \wedge\bar\partial l.
 \tag{4.1}
\]
The differential omega_E is the named rational de Rham
frame, with omega1=integral_a omega_E and
Omega_E=2omega1. No Betti period is set to one.

**[NEW] Proposition4.1.**
\[
 \boxed{\int_E\omega_E\wedge\Theta_u(S)
                              =8\pi^2i c_\pi\,{\cal P}(S).} \tag{4.2}
\]

*Proof.* Put I=integral_V S wedge omega_E wedge barpartial l.
In integral omega_E wedge(3.2), the term involving
S wedge partial l has type(3,1) and is zero.
The surviving part of the first term is -I.
Likewise the term involving l partial S is zero by type.
Finally compact Stokes applied to
barpartial(l omega_E wedge S) gives
\[
 \int_V l\,\omega_E\wedge\bar\partial S
                  =\int_V\bar\partial l\wedge\omega_E\wedge S=-I.
\]
There is no boundary term because S is zero near B.
Thus the left side of(4.2) is -2I.
Since P(S)=iI/(4pi²c_pi), this is exactly(4.2).
Square.

In particular if Theta_u(S)=i eta with eta real closed
and anti-invariant, its b-period satisfies
\[
 \boxed{\mathscr R_E^{\cal D}(\mathsf T_u^{\cal D}[S])
              =\frac{8\pi^2c_\pi}{\omega_1}{\cal P}(S).}  \tag{4.3}
\]
This follows from the fixed Riemann-bilinear identity
integral_E omega_E wedge eta=omega1 integral_b eta.
It agrees with the proved beta2 boundary scalar:
substituting P(j_B beta2) gives(N-1)L(E,2)/pi,
as required by the whole motivic composite(2.4).

For a direct form check on any boundary regulator i eta,
the positive-boundary cutoff is
S=(d rho wedge eta)^(1,1)/(2pi).
The two integrals
integral partial rho wedge barpartial l and
integral partial l wedge barpartial rho both equal
pi i(N-1). Substitution into(3.2), or(3.3) with
A(S)=0, gives i(N-1)eta.
This verifies the full native form composite as well
as the independent motivic calculation.

## 5. The arithmetic real eigenspace and full image of C_j2

On the projective complex curve E, the concise Deligne
complex in degrees1,2,3 and twist2 is
imaginary functions, imaginary one-forms, imaginary
(1,1) forms. The first two differentials are -d.
The latter assertion at degree2 holds because on a
curve there are no types(2,0),(0,2). Therefore
\[
 H^2_{\cal D}(E(\mathbb C),\mathbb R(2))
                       =i\,H^1(E(\mathbb C),\mathbb R).
 \tag{5.1}
\]
Let c_infinity denote geometric complex conjugation.
The arithmetic involution on i eta is
overline(c_infinity^*(i eta))=-i c_infinity^*eta.
Its fixed part is consequently
\[
 i\,H^1(E(\mathbb C),\mathbb R)^- ,
 \tag{5.2}
\]
which is ONE-DIMENSIONAL because the established
integral basis has c(a)=a and c(b)=-b.
The b-period integral is an isomorphism on this real
space. The class r_D(beta2), with period L(E,2)/pi,
is therefore a basis of this REAL realization.

The rational geometry, actual rational unit and trace
commute with this involution. The radial C_j2 has the
arithmetic real structure, so its image lies in(5.2).
There is no claim that the whole rational group
H_M²(E,Q2) has rank one.

**[NEW] Theorem5.1.** For the actual class C_j2 of the
reviewed radial construction,
\[
 \boxed{\mathsf T_u^{\cal D}({\cal C}_{j_2})
   =-12N(N-1)c_\pi\,\frac{\ell_E}{\omega_1}\,
                                  r_{\cal D}(\beta_2),}  \tag{5.3}
\]
and hence
\[
 \boxed{\mathsf R_u^{\cal D}({\cal C}_{j_2})
   =-12Nc_\pi\,\frac{\ell_E}{\omega_1}\,
                                  r_{\cal D}(\beta_2).}  \tag{5.4}
\]

*Proof.* The input scalar is the already proved
\[
 {\cal P}({\cal C}_{j_2})={\cal M}
                =-\frac{3N(N-1)}{2\pi^3}\ell_E L(E,2).
\]
Equation(4.3) gives its projected period as
-12N(N-1)c_pi ell_E L(E,2)/(pi omega1).
Divide by the NONZERO REAL period L(E,2)/pi of the
explicit basis in(5.2). This determines the full real
Deligne class and gives(5.3). Division by N-1 gives(5.4).
No rational motivic preimage of C_j2 was assumed. Square.

The full completed coefficient is still
tildej2=j2+gamma1 j1+gamma2 j0+gamma3 R_N.
We retain all these terms before applying the map.
Their known lower scalar pairings are zero.
Equation(4.3), together with the one-dimensional
real eigenspace, now proves the STRONGER projected
class equality
\[
 \mathsf T_u^{\cal D}({\cal C}_{\widetilde j_2})
                  =\mathsf T_u^{\cal D}({\cal C}_{j_2}).  \tag{5.5}
\]
The Gamma-pole cross term was not deleted from the
unpaired relative class.

## 6. The remaining arithmetic comparison

The map T_u is rational on the entire motivic group,
and R_u really retracts j_B. Its Deligne realization
on the ACTUAL spectral class is now computed fully,
not just by an unspecified scalar test. The operator
does not make that real spectral class motivic.

Even if a rational relative lift of C_j2 were supplied,
R_u would produce some rational K2(E) class.
It would not by itself prove that this class belongs
to Q beta2, since rank one of K2(E)_Q is not established.
The one-dimensional REAL target(5.2) is not that
rational rank assertion. This distinction prevents
an inference of rationality from the real multiple
in(5.4).

Moreover its coefficient is
\[
 -12Nc_\pi\ell_E/\omega_1
       =-24Nc_\pi\ell_E/\Omega_E,
\]
which is missing Reg_E. The full target remains
D_pt tensor Q beta2 tensor Q(1)^(-2), with original
frame value -Omega_E Reg_E L(E,2)/(4pi³) and desired
coefficient6N(N-1)n_E. Root's separate point-height
operation must be compared arithmetically with this
projection; a formal multiplication of real periods
does not supply that map.

**[GAP RCT-389].** Construct a rational framed source
for the projected spectral class and its comparison
with the actual point-height determinant, retaining
all finite corrections and integral denominators.
This is an attempted route, not a claimed necessary
condition for full BSD. Neither an integral primitive
splitting nor full Sha finiteness has been proved here.

All primary sources and normalizations used above
were read directly. No completed proof/shared synthesis
was changed, no old certificate rerun and no new
agent spawned. All new deductions passed the linked independent review.
