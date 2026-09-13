# Actual derived symbols for the point–K2 obstruction

Date:2026-09-13. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
All eight sections passed [independent review](review-point-k2-derived-symbol.md),
with the explicit cancellation-source precision recorded there.
[Checkpoint](point-k2-derived-symbol-checkpoint.md).
Full BSD over Q remains open.

This note gives an exact degree-one Suslin model and actual rational
Milnor K3 cochains for the remaining point–K2 classes. It computes the
first translation difference of a fixed diagonal cycle, and supplies
a nullcochain for its second translation differences. The first
differences themselves are not proved zero.

## 1. Fixed arithmetic input and the degree to be computed

Use the same curve and full basis as in the
[reviewed rational-boundary construction](marked-rational-boundary-lift-attack.md):
\[
 E:y^2+y=x^3+x^2-2x,\qquad P=(-1,1),\quad Q=(0,-1).
\]
Write X=E_s×E_t, distinguishing the point factor from the K2 test
factor. The fixed rational class
\[
 \beta=\beta_2\in H_M^2(E_t,\mathbb Q(2))
                  =CH^2(E_t,2)_{\mathbb Q}
\]
is the ACTUAL class constructed in
[the integrated proof, §7](integrated-spectral-comparison-attack.md),
with real regulator L(E,2)/π in its stated native frame. Its unique
rational arithmetic-model extension is a completed input. It is not
defined by taking an inverse real regulator here.

The abelian projection of the coefficient obstruction uses
\[
 z_R=([R]-[O])\times\beta\in CH^3(X,2)_{\mathbb Q},\qquad R=P,Q.
 \tag{1.1}
\]
The predecessor proved that the two h1 projectors select these classes
and that their geometric PLUS part vanishes rationally. We retain the
geometric MINUS part, with the rational projector
e_-=(1-\tau_{12})/2. No integral primitivity is claimed.

Let A=M_1(E) be the homological elliptic motive. Curve duality gives
h=A(-1)[-2] for its cohomological h1 object. Consequently the group
containing the remaining classes is
\[
\begin{split}
 \operatorname{Hom}(\mathbf1,e_-(h\otimes h)(3)[4])
  &=\operatorname{Hom}(\mathbf1,e_-(A\otimes A)(1))\\
  &=\operatorname{Hom}
       (\mathbf1,e_-(A\otimes A\otimes\mathbb G_{m,\mathbb Q})[-1]).
\end{split}                                                    \tag{1.2}
\]
Here Q(1)=G_m,Q[-1]. Both shifts used to replace h by A are even,
and no odd permutation of factors is made. Thus the geometric MINUS
projector in (1.2) is the original one; there is no new interchange
of PLUS and MINUS. Formula (1.2) is a degree-minus-one morphism
group, not an ordinary degree-zero Somekawa group.

## 2. A genuine degree-one Suslin model

**[NEW] Proposition2.1.** Let the tensor below mean Voevodsky's tensor
of rational Nisnevich sheaves with transfers, and put
\[
 {\cal T}=e_-\bigl(E_{\mathbb Q}\otimes_{\rm ShT}E_{\mathbb Q}
                         \otimes_{\rm ShT}\mathbb G_{m,\mathbb Q}\bigr).
\]
Then the group in (1.2) is canonically
\[
 H^{-1}(C_*{\cal T})(\mathbb Q)
   =H_1\bigl({\cal T}(\Delta^\bullet_{\mathbb Q}),\partial_{\rm Suslin}\bigr).
 \tag{2.1}
\]
The tensor of the homotopy-invariant sheaves is not being assumed flat
after motivic localization.

*Proof.* First justify the category in which the Hom is computed.
Over the perfect field Q, Voevodsky's cancellation theorem,
[math/0202012v1, Corollary4.10](https://arxiv.org/pdf/math/0202012v1),
makes simultaneous Tate twist fully faithful on effective motives.
Iterating it identifies every transition map in the stabilization
Hom colimit with an isomorphism. Therefore the effective geometric
category embeds fully faithfully in the stable category, also with
rational coefficients and idempotent summands. The unit, A and
G_m,Q=Q(1)[1] are effective geometric objects, as are their tensor
product, e_- summand and shifts. Thus the stable Hom in the last
line of (1.2) is its effective Hom, including the shift [-1].
We compute that effective Hom below.

For the abelian variety E, A is the image of the homotopy
invariant transfer sheaf E_Q in degree zero: AEWH, Def2.1.4 and
Prop2.1.3, in the version specified below. Sugiyama's published
AppendixA PropositionA.1 proves that the rational transfer-SHEAF
tensor is exact. CorollaryA.3 identifies its derived tensor on
degree-zero sheaves with that sheaf tensor. Thus no flatness
assumption has been inserted at this stage.

The A1 localization is then C_*. Kahn–Yamazaki Lemma3.3 explicitly
describes motivic tensor as C_*(C⊗^L D); it need only be right
t-exact. Applying it to the three factors gives C_*T, not T
concentrated in degree zero. Rational idempotents commute with this
construction. Their §3.4, equation(3.2), identifies morphisms from
the unit to C[i] with H^i(C)(k) over the base field. Equivalently,
Nisnevich evaluation at SpecQ is exact, since every Nisnevich cover
of a field has a section. The Suslin complex has its n-simplices
in cohomological degree -n, which proves (2.1). Square.

This is a concrete complex of sheaves with transfers; the tensor is
not the naive pointwise tensor of groups of points. The rational
Nisnevich/étale equivalence used in the cited rational source does
not assert exactness of the homotopy-invariant tensor category.

The actual beta itself belongs to
\[
 H_1 C_*\bigl(E_{\mathbb Q}\otimes_{\rm ShT}
                             \mathbb G_{m,\mathbb Q}\bigr)(\mathbb Q)
  =\operatorname{Hom}(\mathbf1,A(1)).
 \tag{2.2}
\]
Indeed its h1 component is
Hom(1,h(2)[2])=Hom(1,A(1)). Its already computed nonzero
regulator proves that (2.2) contains this nonzero class. Therefore
discarding the degree-one Suslin homology in favor of the ordinary
H0 tensor would already discard the known beta input. It cannot
prove the desired point product zero. This is a test on the
actual beta, not an abstract derived countermodel.

The point R defines a rational section of E_Q and hence a specified
map from the complex in (2.2) to that in (2.1), followed by e_-.
Its image is z_R. A concrete representative of beta may be sent
through this map; no filling in Suslin degree two has been supplied.
The next sections instead construct explicit rational cochains
for the same higher-Chow group through coniveau.

## 3. The exact Gersten complex in this degree

**[NEW] Proposition3.1.** For the smooth surface X over Q,
\[
 CH^3(X,2)_{\mathbb Q}\simeq
 H^1\left[
 K_3^M(\mathbb Q(X))_{\mathbb Q}
 \xrightarrow{d}
 \bigoplus_{D\in X^{(1)}}K_2^M(\mathbb Q(D))_{\mathbb Q}
 \xrightarrow{d}
 \bigoplus_{x\in X^{(2)}}\mathbb Q(x)^*\otimes\mathbb Q
 \right].
 \tag{3.1}
\]
The differentials are the tame residues, with normalization and
residue-field transfers for the second differential.

*Proof.* The motivic coniveau spectral sequence is
\[
 E_1^{p,q}=\bigoplus_{x\in X^{(p)}}
 H_M^{q-p}(\mathbb Q(x),\mathbb Q(3-p))
 \ \Longrightarrow\ H_M^{p+q}(X,\mathbb Q(3)).
 \tag{3.2}
\]
Déglise §2.1, equation(2.1.c), gives this spectral sequence;
Proposition2.7 identifies its d1 with the residue/transfer
differential. In total degree four the only possibly nonzero
term is (p,q)=(1,3). The (0,4) term vanishes because a field has
H_M^i(F,Q(n))=0 for i>n: in the higher-Chow complex there are no
codimension-n cycles on simplices of dimension 2n-i<n.
The (2,2) term is H_M^0(F,Q(1))=0, using Q(1)=G_m[-1].
The q=3 row consists precisely of K3, K2 and K1 by the field
Milnor-symbol theorem. No higher differential enters (1,3),
since its source would have negative codimension, or leaves it,
since its target would have codimension at least three. The
coniveau filtration has only this graded piece in total four.
Finally H_M^4(X,Q(3))=CH^3(X,2)_Q. This proves (3.1), not
merely an edge map or an associated-graded approximation. Square.

We fix the Kummer-FIRST orientation
\[
 \partial_v\{\varpi,a,b\}=\{\bar a,\bar b\}
 \quad\text{for valuation units }a,b.                       \tag{3.3}
\]
It is Rost's positive-uniformizer convention. If beta is unramified
at v, his product rule gives
\[
 \partial_v\{f,\beta\}=v(f)\,s_v(\beta).                    \tag{3.4}
\]
For a unit f the right side is zero. These formulas apply to
rational linear combinations and finite norms by the projection
formula and norm/residue compatibility.

The original class beta embeds in
K2^M(Q(E_t))_Q: localization for the smooth curve has kernel
formed from H_M^0(k(x),Q(1)), which is zero. Its tame residues
are all zero. At a rational point its specialization belongs to
K2(Q)_Q=0, by the already used rational K2 calculation. Only
the rational points O and -R will require that last vanishing.
No vanishing of arbitrary function-field K2 is used.

## 4. Two-variable Miller functions with all divisors retained

Write s=(x1,y1), t=(x2,y2), and let m_(a,b)(t) denote the
monic-y chord through a,b divided by the vertical line through a+b.
It has divisor [a]+[b]-[a+b]-[O]. Define
\[
 M_R(s,t)=m_{(s,-R)}(t),\qquad R=P,Q.
 \tag{4.1}
\]
These are actual functions in Q(X)^*. On the given Weierstrass model,
\[
\begin{array}{ll}
 \lambda_P=(y_1+2)/(x_1+1),&
 M_P=\dfrac{y_2+2-\lambda_P(x_2+1)}
                 {x_2+x_1-\lambda_P^2},\\[5pt]
 \lambda_Q=y_1/x_1,&
 M_Q=\dfrac{y_2-\lambda_Q x_2}
                 {x_2+1+x_1-\lambda_Q^2}.
\end{array}                                                \tag{4.2}
\]
Put V_R={s=R}, H_R={t=R}, Δ={t=s}, and
Γ_-R={t=s-R}, all with their reduced divisor multiplicities.

**[NEW] Proposition4.1.** The complete divisor is
\[
 \operatorname{div}(M_R)
   =V_R-V_O+\Delta-\Gamma_{-R}+H_{-R}-H_O .
 \tag{4.3}
\]

*Proof.* Over the generic first variable, the ordinary chord divisor
gives Δ-Γ_-R+H_-R-H_O. Any additional divisor must be vertical.
The denominators defining the slope can be singular only at s=R,
s=-R and s=O. At -R the slope has its tangent limit: both numerator
and denominator of its displayed quotient vanish simply. The
resulting Miller function is generically nonzero, so there is no
vertical divisor there.

At R the slope has a simple pole, since R is not a 2-torsion point:
2y_R+1 is 3 for P and -1 for Q. In a local parameter at R, the
numerator of M_R has a simple pole and its denominator a double
pole, with nonzero generic leading coefficients. The quotient
therefore has a simple zero. This supplies V_R.

At O use the parameter -x/y. The slope has a simple pole, while
x(s-R) tends to x(-R). The denominator tends to x2-x_R; the
leading numerator is -lambda_R(x2-x_R). Thus M_R has a simple
pole along V_O. The explicit formulas have no other possible
vertical components. This proves (4.3). Square.

Dropping V_R-V_O would remove exactly the wanted point product.
The constants in (4.2) use the given rational model; multiplying
M_R by a constant would not change the residue calculation below.

## 5. An actual K3 cochain for the first translation difference

Let
\[
 D_\beta=\Delta_*\beta,\qquad
 T_R=(\tau_R\times\mathrm{id})_* ,
 \quad \tau_R(s)=s+R.
\]
Both are defined on the proper surface; D_beta is a cycle in
the middle group of (3.1). Define the rational K3 cochain
\[
 \Theta_R=\{M_R,p_t^*\beta\}\in K_3^M(\mathbb Q(X))_{\mathbb Q}.
 \tag{5.1}
\]
This is an actual finite symbol expression. More explicitly, use
the fixed finite rational norm-symbol presentation of beta from
its construction. If its generic restriction is
Σ_j c_j N_{L_j/Q(E_t)}{f_j,g_j}, (5.1) is
Σ_j c_j N{M_R,f_j,g_j} on the corresponding pulled fields.
Thus (5.1) retains every original rational coefficient and norm
degree; it is not a class selected from a regulator value.

**[NEW] Proposition5.1.** In the Gersten cochain complex,
\[
 d\Theta_R=z_R+D_\beta-T_R D_\beta.                         \tag{5.2}
\]
Consequently
\[
 z_R=(T_R-1)D_\beta\quad\text{in }CH^3(X,2)_{\mathbb Q}.
 \tag{5.3}
\]

*Proof.* At V_R,V_O formula (3.4) gives beta,-beta. At Δ
it gives the positive diagonal beta. At Γ_-R it gives minus
beta pulled back by t=s-R. Parameterizing that graph instead
by t identifies this term with -T_R D_beta. This reparameterization
is essential: it does not assume that translation fixes beta.

Along H_-R and H_O, the specialization of beta is the pullback
of its specialization at the rational point -R or O. Each is
zero in K2(Q)_Q, so these two residues vanish. On any other
horizontal divisor M_R is a unit at its generic point and beta
is unramified; Rost's product rule gives zero. On any other
divisor the valuation on Q(E_t) is trivial and M_R is a unit,
so the residue is again zero. Norm/residue compatibility proves
the same calculation for the fixed finite norm presentation.
This is every codimension-one divisor and proves (5.2).
Passing to (3.1) gives (5.3). Square.

The diagonal cycle is fixed by the geometric interchange. The
already proved vanishing of the PLUS part of z_R therefore gives
the useful equality
\[
 z_R=e_-T_R D_\beta .
 \tag{5.4}
\]
It does not make the right side zero: translation of one factor
does not commute with the geometric interchange. In particular,
the proposed direct Miller filling of z_R has the explicit
residual D_beta-T_R D_beta, rather than zero boundary elsewhere.

## 6. A rational nullcochain for second translation differences

For rational R,S with R,S,R+S different from O and with the
ordinary chord defined, set m_RS=m_(R,S) on the first E.
The cases R=P,S=Q satisfy these hypotheses, and
\[
 P+Q=(4,8),\qquad m_{PQ}(s)=\frac{y_1+2x_1+1}{x_1-4}.
 \tag{6.1}
\]
This follows directly by taking the slope -2 of the line through
P,Q and the vertical line through their sum; no numerical
certificate is used.

**[NEW] Proposition6.1.** The explicit rational cochain
\[
\begin{split}
 \Xi_{R,S}
   &=-\{m_{RS}(s),\beta(t)\}-(T_S-1)\Theta_R\\
   &=\left\{\frac{M_R(s,t)}
           {m_{RS}(s)M_R(s-S,t)},\,\beta(t)\right\}
       \in K_3^M(\mathbb Q(X))_{\mathbb Q}
\end{split}                                                \tag{6.2}
\]
satisfies
\[
 d\Xi_{R,S}=(T_S-1)(T_R-1)D_\beta .
 \tag{6.3}
\]
In particular the second translation difference for the actual
P,Q is rationally zero, with the displayed filling.

*Proof.* By its divisor and the same unramified product rule,
\[
 d\{m_{RS}(s),\beta(t)\}=z_R+z_S-z_{R+S}.
 \tag{6.4}
\]
On the actual divisor representative of z_R one has
(T_S-1)z_R=z_{R+S}-z_S-z_R. Thus the boundary of the first
term in (6.2) is (T_S-1)z_R. On the other hand, translating
(5.2) gives
\[
 d((T_S-1)\Theta_R)
   =(T_S-1)z_R-(T_S-1)(T_R-1)D_\beta.
\]
Subtracting proves (6.3). Pushforward by the translation on a
function is its expression at s-S, which gives the single
symbol in the second line of (6.2). All symbols keep the
Kummer factor first; no degree-three right cup has been
commuted past another input. Square.

The same divisor argument provides the tangent or inverse-point
variants with their usual Miller functions when needed. They
are not needed for the concrete P,Q statement. Formula (6.4)
also makes R↦z_R additive in the rational point group.

Thus the translation orbit of this ACTUAL diagonal beta has
first difference z_R and a filled second difference. This is
a proved operation on our arithmetic cycle. It leaves open
whether either first difference z_P or z_Q has a filling.

## 7. Interface to the full marked obstruction

The corrected point markings are unchanged. In particular the
predecessor's rational h_j/m_(R0,P_j) cochain identifies its
proper point divisor with [P_j]-[O]. Its finite Kummer values
at the removed A, and hence the moving Poincaré data at the
additional punctures Sigma, are still retained there. The new
cochains (5.1) and (6.2) live on E_s×E_t; they do not supply a
trivialization of those fibers or change those fixed corrections.

The full motivic coefficient obstruction remains
-j_B^+(epsilon0 tensor beta,0), with abelian component
z_P tensor e2-z_Q tensor e1. The actual coefficient motive,
its Artin/exterior frames, its rational projector 1/2 and
its real lift were constructed before this note. None is
replaced by a sheaf tensor in the wrong degree.

If a lift uses the additional Sigma boundary, the already
proved necessary relation is still
\[
 388\,\chi_D=
 \sum_{s\in\Sigma}\operatorname{Tr}_{k(s)/\mathbb Q}
          \bigl(\zeta_s\ \mathbin{\cup_{\rm right}}\ u(s)\bigr).
 \tag{7.1}
\]
Here the tuple zeta must represent the actual proper obstruction
-j_B^+(chi_D,0). For a degree-three input, right cup followed
by trace on +j_B is -388; the obstruction's leading minus sign
gives the plus 388 in (7.1). The existing norm-zero theorem
only kills the specifically pulled-back boundary pattern.
It does not kill every allowed zeta, and (6.3) supplies no
such global coefficient-boundary preimage.

**[GAP PK2-389].** Construct an actual first-difference filling
of (5.3) for P,Q, or the required global restriction preimage
in the full coefficient triangle. In the Gersten model a
first-difference filling is a K3 cochain with the precise
boundary z_R and no remaining divisorial residue. The explicit
Theta_R fails by the completely computed residual
D_beta-T_R D_beta. In the derived model it is a degree-two
Suslin filling of the specified point action on the known
degree-one beta class. Ordinary H0 symbols and the filled
second difference do not provide it.

Even vanishing of these abelian components would leave the
full toric/exterior coefficient and the original rational
spectral comparison to be handled. No rationality or
integrality of n_E, and no BSD assertion, follows here.

## 8. Primary versions and checks

The following primary inputs were read for the stated uses.
No old arithmetic certificate or prime scan was rerun.

- [Sugiyama, published Documenta Mathematica 19 (2014), 1061–1084](https://ems.press/content/serial-article-files/26252?nt=1),
  AppendixA PropositionA.1 and CorollaryA.3: exact rational
  transfer-sheaf tensor. The inspected published file has
  24 pages. Its AppendixA is called AppendixB in AEWH's
  citation to the earlier preprint; we use published numbering.
- [Ancona–Enright-Ward–Huber, arXiv1312.4171v2](https://arxiv.org/pdf/1312.4171v2),
  §1.6, Def2.1.4 and Prop2.1.3: rational localization and
  the actual homological M1(E). The arXiv banner is
  17March2016; the 51-page file has a later recompiled
  front date, not a different source version.
- [Kahn–Yamazaki, author version](https://webusers.imj-prg.fr/~bruno.kahn/preprints/Somekawa-Voevodsky31.pdf),
  40 pages, Lemma3.3, §3.4 equation(3.2) and Lemma3.5:
  A1-local derived tensor, evaluation at a field and the
  degree-zero HI tensor. No claim about a motivic
  t-structure is extracted from their homotopy t-structure.
- [Voevodsky, Cancellation theorem, math/0202012v1](https://arxiv.org/pdf/math/0202012v1),
  1February2002, 16 pages, Introduction and Corollary4.10:
  cancellation over a perfect field, used to pass the
  stable Hom in (1.2) to the effective category in §2.
- [Mazza–Voevodsky–Weibel, 27January2004 notes](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf),
  221 pages, Theorem4.1, field Milnor-symbol theorem,
  Lemma14.3, Theorem14.10, §§14.18–22 and Theorem19.1:
  weight one, A1 localization and higher-Chow comparison.
  These numbers are for this inspected version, not the
  later published numbering cited inside AEWH.
- [Déglise, arXiv1106.0905v1](https://arxiv.org/pdf/1106.0905v1),
  5June2011, 25 pages, §2.1 equation(2.1.c),
  Proposition2.7 and Corollary2.9: the convergent coniveau
  sequence and its exact residue/transfer differential.
  Its use in §3 is confined to the surface and degrees
  explicitly proved there.
- [Rost, Chow groups with coefficients](https://emis.muni.cz/journals/DMJDMV/vol-01/16.pdf),
  Documenta Mathematica1 (1996), 319–393, printed
  pp328–331: positive uniformizer convention, R3e/R3f,
  R2b/R2c and norm/residue compatibility. The same
  inspected primary file was used for the previous
  Kummer-FIRST convention audit.
- [Weibel, K-book ChapterIII](https://sites.math.rutgers.edu/~weibel/Kbook/Kbook.III.pdf),
  Example5.2.2 and §6.5.1, as checked in the
  [predecessor §9](marked-rational-boundary-lift-attack.md):
  K2(Q)_Q=0. This is applied only to the rational
  specializations O and -R in the new symbol calculation.

All displayed Miller and residue calculations are proved above
from the actual rational model. The original beta coefficients,
its regulator frame, and the full boundary sign are inherited
unchanged from their independently reviewed constructions.
