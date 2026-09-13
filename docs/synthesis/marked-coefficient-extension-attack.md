# A moving marked coefficient family before the elliptic projection

Date: 2026-09-13. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Complete bounded construction, independently reviewed **PASS**:
[original §§1–8 and separate §§9–10 audit](review-marked-coefficient-extension.md).
[Restart](marked-coefficient-extension-checkpoint.md).
The universal full BSD objective remains open.

This constructs a nonconstant rational one-motive family from the
FULL corrected point divisors and the actual modular map. Its exterior
square has the required quadratic Deligne component, and its K2
extension tensor has a cubic component. Its extra boundary has explicit
nonzero monodromy and nontrivial Poincaré fibers. We retain those data
in an actual rational motivic coefficient complex. The original restricted
spectral class has a real Deligne lift to those coefficients. A rational
input, motivic lift selection and the required boundary comparison remain open.
No spectral scalar is used to define the family.

## 1. Fixed point data and an algebraic moving pair

Use the already reviewed data
\[
 E:y^2+y=x^3+x^2-2x,\quad P=(-1,1),\quad Q=(0,-1),\quad O,
\]
\[
 R=P+Q=(4,8),\quad S=R+P=(-51/25,-68/125),\quad
 T=R+Q=(1/16,-9/64).
\]
Write P_1=P,P_2=Q, A={O,P,Q}, D_i=(P_i)-(O), and
\[
 Z_1=(S)-(R)+\operatorname{div}(h_1),\qquad
 Z_2=(T)-(R)+\operatorname{div}(h_2),
\]
where the ACTUAL finite corrections are
\[
 h_1=1-\frac{332}{27(x-4)}+\frac{1040y}{27(x-4)^2},\qquad
 h_2=1-\frac{41}{3(x-4)}+\frac{20y}{3(x-4)^2}.             \tag{1.1}
\]
Their values at(O,P,Q) are respectively(1,5,5/3) and(1,4,4).
All finite symbols for these original Z_j are zero.
The fixed one-motive is
\[
 M_0=[L\longrightarrow G],\quad
 L=\mathbb Ze_1\oplus\mathbb Ze_2,\quad
 G=J(E,A),\quad e_j\longmapsto g_j=\operatorname{AJ}_A(Z_j).
 \tag{1.2}
\]
Its torus is T_A=G_m^A/G_m, with character basis D_1,D_2,
and its homological Tate lattice
\(\mathcal T_{\mathbb Z}=\operatorname{Div}^0(A)^\vee\otimes\mathbb Z(1)\)
has basis t_1,t_2 with
periods2pi i. The full point-height matrix is H and det H=Reg_E>0.
These are inputs from the
[relative point proof](relative-modular-cycle-attack.md)
and [determinant proof](point-determinant-single-valued-attack.md).

Let B* be the ENTIRE geometric support of Z_1,Z_2 and write
Z_j=sum_Z n_(j,Z)[Z]. Put
\[
 \Sigma_E=\{a-Z:a\in A,\ Z\in B^*\},\qquad
 S_E=E\setminus\Sigma_E .                                \tag{1.3}
\]
This is a finite Galois-stable set, and O is not in it because
B* avoids A. For x in S_E, the translated divisor T_x Z_j
avoids A. It has degree zero and the same Picard class P_j.
The actual algebraic one-motive family is
\[
 {\cal M}_x=[L\longrightarrow G],\qquad
                   e_j\longmapsto\operatorname{AJ}_A(T_x Z_j).
 \tag{1.4}
\]
The bottom semiabelian group is constant; its marking varies.

Here is its relative-pair geometry. Over S_E take
(E minus A) times S_E, marked by the finite etale family
{(w,x):w-x is in B*}. Pull relative H_1 back along the two
divisor markings given by the coefficients n_(j,Z).
The resulting integral local system is the rank-six realization
of(1.4). All sets, maps and markings are defined over Q;
working after a finite splitting field and descending gives the
same object. No point of B* or rational principal correction
has been omitted.

The generalized-Jacobian and marked realization conventions are
[Sertöz–Ouaknine–Worrell2505.20397v1, §6.5,
Proposition6.5.43](https://arxiv.org/html/2505.20397v1).
The general one-motive realization and its comparison are also
[Milne, ChapterIV, §2, Proposition2.4](https://www.jmilne.org/math/articles/1990aT.pdf).
We use the general realization, not a theorem restricted to
symmetric or polarized degenerating one-motives.

Finally let C=X0(389), pi:C→E be the fixed degree40 modular map,
and define
\[
 \Sigma=\pi^{-1}(\Sigma_E),\quad {\cal S}=C\setminus\Sigma,\quad
 C_{\rm cusp}=\{0,\infty\}\subset{\cal S}.
 \tag{1.5}
\]
Pull(1.4) back by x=pi(z). Since pi(0)=pi(infinity)=O,
both cusp fibers are canonically the original marked M_0.
The extra points Sigma are interior algebraic points and will
remain part of every coefficient and boundary calculation.

## 2. Actual rational Kummer coefficients and their divisors

For a generic pair of elliptic points A,x, let m_(A,x)(w)
be the chord divided by the vertical line through A+x. Thus
\[
 \operatorname{div}_w m_{A,x}=[A]+[x]-[A+x]-[O].
\]
This identity follows from the chord intersection and the
elliptic group law; it fixes the function order.
Set A_1=S,A_2=T and define the rational function on E_x times E_w
\[
 F_j(x,w)=\frac{m_{R,x}(w)}{m_{A_j,x}(w)}
                              \frac{h_j(w-x)}{h_j(w)}.
 \tag{2.1}
\]
Its generic w-divisor is exactly T_x Z_j-Z_j.
Any vertical base factor in this displayed rational expression
cancels in the evaluations
\[
 a_{ij}(x)=\frac{F_j(x,P_i)}{F_j(x,O)}
 =\frac{m_{R,x}(P_i)}{m_{A_j,x}(P_i)}
             \frac{h_j(P_i-x)}{h_j(P_i)h_j(-x)}.           \tag{2.2}
\]
The second equality uses h_j(O)=1 and the equal leading
Laurent coefficient of the two Miller functions at w=O.

The torus coordinates of a principal divisor in this convention
are F_j(D_i)=F_j(P_i)/F_j(O), as is also checked by its
third-kind integral. Therefore the marking identity is
\[
 \operatorname{AJ}_A(T_x Z_j)=g_j\cdot(a_{1j}(x),a_{2j}(x))
                          \quad\text{in }G.              \tag{2.3}
\]
The multiplication is through the specified torus inclusion.
This is an equality of algebraic sections, not of their real
regulators alone. At x=O the removable values in(2.2) are1.
For example the two Miller functions have the same leading
behavior as x tends to O, so their evaluation ratio tends to1;
the other factor in(2.2) also tends to1. Thus(2.3) recovers
the fixed marking at O.

**[NEW] Proposition2.1.**
\[
 \boxed{\operatorname{div}_x a_{ij}
       =\sum_Z n_{j,Z}\bigl([P_i-Z]-[-Z]\bigr).}           \tag{2.4}
\]
In particular all a_ij are units on S_E.

*Proof.* On the two-dimensional E_x times E_w the nonvertical
part of div F_j is the moving divisor T_xZ_j minus the fixed Z_j.
Intersect it with the sections w=P_i and w=O.
The fixed divisor contributes nothing because it avoids A.
The moving graphs meet those sections at x=P_i-Z and x=-Z,
respectively, with their original multiplicities.
Vertical divisor terms contribute the same base divisor at
both sections and cancel in the ratio. This proves(2.4).
Its support is contained in(1.3). Square.

The functions are not all constants disguised by a choice of
period. Indeed(2.4) is the difference between translating the
nonzero finite divisor [-1]_*Z_j by the nontorsion P_i and
leaving it fixed. Equality of those two finite divisors would
make their finite support invariant under every multiple of P_i,
which is impossible unless the divisor is zero.
Here it is not zero because its Picard class is P_j.
We next compute an actual nonzero residue rather than rely
only on this nonconstancy argument.

## 3. A concrete integral residue matrix and the full connection

Exact substitution into(1.1) gives
\[
 \begin{array}{c|cc}
 &h_1&h_2\\ \hline
 S&505109/205209&72126/22801\\
 T&14977/3969&1945/441 .
 \end{array}                                             \tag{3.1}
\]
All four values are nonzero. At R and -R each h_j has a pole
of order2. The numerator leading values, after writing over
27(x-4)^2 or3(x-4)^2, are
(8320,-9360) and(160,-180), respectively; x-4 is a parameter
at both points. Hence both Z_j have coefficient-3 at R and-2
at -R, and the coefficients at S,T are(1,0) for Z_1 and(0,1)
for Z_2.

**[NEW] Corollary3.1.**
\[
 \boxed{\bigl(\operatorname{ord}_{-R}a_{ij}\bigr)
                  =\begin{pmatrix}4&3\\3&4\end{pmatrix},
                  \qquad\det=7.}                         \tag{3.2}
\]
Indeed(2.4) gives ord_(-R)a_ij=n_(j,P_i+R)-n_(j,R).
Equation(3.1) makes this(1+3,0+3;0+3,1+3).

For reproducibility, the only new arithmetic computation here
was evaluation of the two displayed rational functions at
the two displayed rational points using exact fractions.
All table entries also follow by direct substitution.
No old certificate or numerical routine was rerun.

There is an exact description of the variation as a Baer sum:
relative to the constant family M_0, its j-th marking adds
the Kummer one-motive [Z→T_A], 1↦(a_1j,a_2j), pushed out
by T_A→G. This follows directly from(2.3).
Choose a fixed rational de Rham frame of M_0 and the induced
Baer-sum frame. Denote its top lifts by e_j^dR and its toric
vectors by t_i^dR. The algebraic connection is
\[
 \nabla e_j^{dR}=-\sum_i d\log(a_{ij}\circ\pi)\,t_i^{dR},
 \qquad \nabla|_{H_{\rm dR}(G)}=d.                         \tag{3.3}
\]
To check the sign, the Kummer horizontal lift has the form
e_j^dR+sum log a_ij t_i^dR. Continuing log a once positively
around a zero adds2pi i times its order.
Since t_i^B compares to2pi i t_i^dR, the corresponding
integral Betti monodromy is
\[
 e_j^B\longmapsto e_j^B+\sum_i n_{ij}t_i^B .
 \tag{3.4}
\]
This also derives(3.3) directly for the pushed Kummer extension.
The constant M_0 comparison, including its point extensions,
is retained in this frame; (3.3) does not make that comparison
matrix the identity or split M_0 as a Hodge structure.

All connection matrices mapping L to the torus commute and
have pairwise product zero on the rank-six realization.
Thus the connection is flat and is defined over Q.
It has logarithmic poles at Sigma with nilpotent residues.
It is the actual algebraic connection of the moving relative
pair, not a connection inferred from arbitrary analytic logs.

## 4. The quadratic and cubic Deligne components are retained

Let mathbb V_z be the homological realization of the pulled-back
family and mathbb W=wedge² mathbb V. Its top frame is
e_1 wedge e_2 and its bottom is t_1 wedge t_2 with Tate twist2.
The integral exterior lattice is embedded by
x wedge y↦x tensor y-y tensor x on both frames.
As in the completed determinant proof, geometric interchange
on degree1 cross degree1 is minus ordinary swap, so the
geometric PLUS projector realizes mathbb W rationally.
No integral inverse of that projector is used.

Put
\[
 H_{ij}(x)=H_{ij}+\log|a_{ij}(x)|.
 \tag{4.1}
\]
**[NEW] Proposition4.1.** The Deligne operator on each fiber is
\[
 \delta_{\mathbb V_x}(e_j^D)
       =\frac1{2\pi}\sum_i H_{ij}(x)t_i^B,\qquad
 \delta_{\mathbb V_x}^2=0,
\]
and on the exterior fiber
\[
 \delta_{\mathbb W_x}^2(e_1^D\wedge e_2^D)
       =\frac{\det H(x)}{2\pi^2}t_1^B\wedge t_2^B,\quad
 \psi(\overline{e_1^D\wedge e_2^D})
       =-\frac{\det H(x)}{\pi^2}.                         \tag{4.2}
\]

*Proof.* The real-normalized third-kind differential eta_i
is fixed because A is fixed. For a principal divisor div F,
its period convention gives
Re integral_(div F) eta_i=log|F(P_i)/F(O)|.
Use div_w F_j=T_x Z_j-Z_j to obtain exactly(4.1).
The direct Deligne lift calculation in the completed point
proof now applies to these same toric and top frames,
giving the first display. Tensor derivation gives the factor2
in its exterior square, and exp(-2i delta) gives the second
coefficient in(4.2). Square.

At x=O, H(x)=H and det H(x)=Reg_E, so both original cusp
fibers have the required nonzero quadratic component.
It remains nonzero on a complex neighborhood of those fibers.
Near x=-R, (3.2) gives
det H(x)=7(log|t|)^2+O(log|t|) in a local parameter t,
again nonzero near that boundary. No global nonvanishing
away from these neighborhoods is claimed.

At a rational x in S_E, the new FINITE symbols are
v_p(a_ij(x))log p, added to the old zero symbols.
The archimedean contribution is(4.1).
Their product-formula cancellation keeps the normalized
GLOBAL point-height matrix H fixed:
log|a_ij(x)|=sum_p v_p(a_ij(x))log p.
Thus det H(x) in(4.2) is an archimedean splitting block,
not a replacement for the full global regulator at a
moving rational fiber. Over number fields all embeddings
and local weights must be included in the same formula.
None of these finite terms is silently discarded.

Let B_beta be the SAME rational K2 extension from the completed
determinant proof. The actual coefficient mathbb W tensor B_beta
has extreme weight-7 vector
\[
 -\frac{\det H(x)}{\pi^2}\,
                          1(2)_B\otimes U_\beta.          \tag{4.3}
\]
Its Deligne operator has cube
3delta_mathbbW² tensor delta_beta, nonzero where det H(x)
is nonzero because the real beta2 regulator is nonzero.
This is a tensor of actual coefficient realizations, with
the moving algebraic marking defined beforehand.
It is not tensoring the evaluated spectral scalar with H.

## 5. New boundary monodromy and a derived repair

At a point s of C above -R, let e_s be the ramification
index of pi. In the integral Betti frame, logarithmic
monodromy on mathbb V has column matrix
\[
 n_s=e_s\begin{pmatrix}4&3\\3&4\end{pmatrix}:L\to\mathcal T_{\mathbb Z}.
\]
It is zero on H_B(G). Its square is zero.
On mathbb W write Lambda_s=log T_s. Then
\[
 \boxed{\Lambda_s^2(e_1\wedge e_2)
                     =14e_s^2\,t_1\wedge t_2,\qquad
 (T_s-1)(e_1\wedge e_2)_{\rm bottom}
                     =7e_s^2\,t_1\wedge t_2.}             \tag{5.1}
\]
The first formula is the two orders of the exterior derivation;
the second is the coefficient Lambda_s²/2 in its exponential.
The Betti/de Rham Tate factors in(3.3)–(3.4) are retained.

There is NO invariant lift of the top frame at this boundary.
Indeed the weight-2-lowering part of
(T_s-1)(e_1 wedge e_2) is
n_s(e_1) wedge e_2+e_1 wedge n_s(e_2), which is nonzero.
Applying T_s-1 to any lower-weight correction cannot change
that part: it lowers its weight by at least two as well.
Thus the map of ordinary invariant stalks
(j_*mathbb W)_s→Q has zero top image.
This is a local calculation on the NEW coefficient family,
not a retry of the previously excluded constant MHS map.

A justified repair is to keep the derived/logarithmic complex.
The explicit logarithmic extension(3.3), and its exterior
connection, retain the nonzero residue. Locally an analytic
holomorphic gauge removes the unit factors of a_ij, reducing
the logarithmic de Rham operator to q d/dq-N_dR, where
Res_s(nabla)=-N_dR in the chosen de Rham frame.
In its power series, every positive
coefficient n has invertible nI-N_dR; the inverse is the
finite nilpotent geometric series. Only the constant term
remains. This gives the local two-term complex with that
residue as differential.

The corresponding rational Betti boundary complex is
\[
 [\,\mathbb W_{z_*}\xrightarrow{\,T_s-1\,}
                              \mathbb W_{z_*}\,],
                      \quad\hbox{in degrees0 and1}.       \tag{5.2}
\]
It keeps both invariants and coinvariants. In comparison coordinates,
\(T_s=\exp(2\pi iN_{\rm dR})\), so the earlier Betti logarithm is \(\Lambda_s=2\pi iN_{\rm dR}\). Hence over C, T_s-1 is N_dR times
an invertible power-series factor with leading term2pi i;
their kernels and cokernels therefore agree.
This is the usual regular-singular comparison verified
directly for our explicit unipotent connection.

Over Q the rank-six monodromy has two Jordan blocks of
size2 and two of size1. Its exterior square has one
block of size3, four of size2 and four of size1.
To verify this, split the four moving directions as
two length-two blocks. Their exterior square is a
length-three block plus three fixed lines; tensoring
with the two fixed elliptic directions gives four
length-two blocks, and the exterior of those fixed
directions gives one more fixed line.
Thus T_s-1 on rank15 has rank6 and both H⁰,H¹ of(5.2)
have dimension9. The top quotient survives in H¹,
even though it has no invariant lift in H⁰.

This Jordan calculation is rational, not an integral
change of basis dividing7. The actual integral matrix
n_s remains(5.1). Its determinant is not a BSD quotient,
a point-height index or a Sha bound.

## 6. The coefficient complex and the original input

Let E_t be a separate copy of the test elliptic curve,
Z={\cal S} times E_t, and B_cusp=C_cusp times E_t.
Pull the rational geometric coefficient mathbb W to Z.
The actual relative coefficient complex is
\[
 K_{\mathbb W}(2)=\operatorname{Cone}
 \left(R\Gamma(Z,\mathbb W(2))\longrightarrow
       R\Gamma(B_{\rm cusp},\mathbb W_0(2))\right)[-1].
 \tag{6.1}
\]
Its Betti local system, rational de Rham logarithmic connection,
Hodge/weight filtrations and comparison all come from the
algebraic moving pair of §1 and its geometric exterior square.
The twists in(6.1) are applied to the full coefficient; its
bottom coefficient is therefore Q(4), not Q(2).
Recall \(K=H^1(E,\mathbb Q(2))\), of weight-3.
The UNTWISTED coefficient mathbb W tensor B_beta from §4 has
bottom K(2), of weight-7. Applying the ADDITIONAL overall
twist(2) of(6.1) gives bottom
\(K(4)=H^1(E,\mathbb Q(6))\), of weight-11.
No Tate factor is deleted.

The top quotient mathbb W→Q(0) gives a morphism
K_mathbbW(2)→K_Q(2). The original real radial class has a
canonical RESTRICTION
\[
 c_{\cal S}\in H^3_{\cal D}({\cal S}\times E_t,
                                    B_{\rm cusp};R(2)),
\]
because this is an open pullback of the original proper pair.
It is not falsely called a restriction in compact-support
cohomology after deleting Sigma. Those supports differ.

With F=W_(-1)mathbb W, the actual coefficient sequence gives
\[
 K_F(2)\longrightarrow K_{\mathbb W}(2)
       \longrightarrow K_Q(2)
       \xrightarrow{\partial_{\mathbb W}}K_F(2)[1].        \tag{6.2}
\]
Thus the precise first lifting class is
\[
 {\cal O}_{\mathbb W}(c_{\cal S})
      =\partial_{\mathbb W}(c_{\cal S})
                            \in H^4_{\cal D}(K_F(2)).
 \tag{6.3}
\]
A real lift exists exactly when this class is zero;
then its choices form a torsor under the IMAGE of
H_D³(K_F(2)). This is the Betti/de Rham and real Deligne
coefficient triangle of the explicitly algebraic one-motive
family. Section9 constructs a specified motivic coefficient object
and top map, closing the coefficient-category step that was still
open at the first eight-section audit. Section10 proves the real
vanishing in(6.3). An actual rational spectral input, motivic
vanishing and a choice of lift are still required; none is inferred
merely from the variation or real vanishing. No motivic lift of
the spectral input is claimed here.

Here are the explicit coefficient cochains for this test.
On overlapping logarithm charts let
n_ij^(ab)=(log_b a_ij-log_a a_ij)/(2pi i).
The integral transition of the top exterior lift is
\[
 e_{12}^{(b)}-e_{12}^{(a)}
 =\sum_i n_{i1}^{ab}t_i\wedge e_2^{(a)}
  +\sum_i n_{i2}^{ab}e_1^{(a)}\wedge t_i
                  +\det(n^{ab})\,t_1\wedge t_2.           \tag{6.4}
\]
The differential part in the rational de Rham frame is
\[
 \nabla e_{12}
 =-\sum_i d\log a_{i1}\,t_i^{dR}\wedge e_2^{dR}
  -\sum_i d\log a_{i2}\,e_1^{dR}\wedge t_i^{dR}.          \tag{6.5}
\]
For a scalar two-form c, its new connection term is
c wedge the right side of(6.5), with a PLUS sign because
the form degree is two. The unaltered M_0 Hodge comparison
and its finite Kummer data are part of the same complex.
Equations(6.4)–(6.5), including the quadratic transition,
therefore specify actual local lifts used to calculate(6.3).

At rank six the marking identity(2.3) gives an additional
exact description: the Baer DIFFERENCE from the constant
coefficient extension is the pushed Kummer extension
[L→T_A], with columns(a_1j,a_2j).
Consequently the difference of the corresponding derived
connecting maps is the push of that specified Kummer
extension class composed with the input. This is an
actual extension/cup operation, not an adjustable real
matrix. The constant point extension is not set to zero.

The monodromy calculation does NOT evaluate(6.3) for the
actual Deligne input. Its image in ordinary Betti degree-three
cohomology is zero by the proper-pair calculation in the
completed determinant proof §7. Therefore multiplying
only that Betti component by(6.4) would miss the real
Deligne class. Its filtered and comparison cochains,
including the two-form term in(6.5), remain necessary.
No vanishing of the full lifting class is asserted.

## 7. The graph/Poincaré boundary cannot be silently trivialized

The original rational graph bundle on C times E_t is
\[
 L_D=\mathcal O(\Gamma_\pi-C\times O)
     =d^*\mathcal O_E(O)\otimes p_{E_t}^*\mathcal O_E(O)^{-1},
 \quad d(z,w)=w-\pi(z).
\]
It has the established rational trivializations at the
TWO original cusp fibers, since pi(c)=O. On an added
fiber over s in Sigma its restriction is instead
\[
 L_D|_{\{s\}\times E_t}
                       =\mathcal O_{E_t}(\pi(s)-O).       \tag{7.1}
\]
At every s over -R this is the NONTRIVIAL point class -R.
R=P+Q is nontorsion, so this line bundle remains nontrivial
over every field extension. It is not rationally zero
in Pic⁰ tensor Q.

Hence one cannot lift this particular graph line to
Pic(C times E_t,(C_cusp union Sigma) times E_t) by assigning
trivializations on all new fibers. This is an actual
algebraic obstruction, despite the degree-zero curvature
on an individual fiber. A real zero-boundary Cauchy
choice is not a rational trivialization of(7.1).

A boundary-preserving algebraic replacement is the
homotopy fiber of the Picard restriction groupoid over
the ACTUAL tuple
(O at the old cusps, L_D|_(s times E_t) at every new s).
The object L_D, its old cusp trivializations and the
identity restrictions to(7.1) give a rational object
of that fiber. It is a torsor for the usual relative
Picard group, rather than a falsely based zero class.
This specifies the additional Poincaré boundary data
which any subsequent compact trace must carry.
The ordinary relative Picard sequence and its
trivialized-line interpretation are
[MVW, Definition7.10 and its following exact sequence](https://sites.math.rutgers.edu/~weibel/MVWnotes/third.pdf).

Thus(6.1) keeps a logarithmic/derived Sigma boundary.
Using j_! instead is also a well-defined coefficient
complex, but carrying the original spectral and graph
data into that compact-support version requires the
extra boundary comparison just displayed. No trace
map from an ordinary nonproper open is used to bypass it.

## 8. Exact outcome and remaining comparison

We have constructed a rational geometric coefficient
family, identified all four rational Kummer functions,
and computed a nonzero integral residue matrix.
Its exterior and fixed-beta2 tensor retain quadratic
and cubic Deligne components BEFORE any scalar
projection. The original corrected point object is
recovered at both original cusps. All added finite
principal-divisor corrections and new boundary bundles
are explicit.

The unipotent logarithmic complex repairs the loss of
information caused by taking only invariant stalks.
The additional Sections9–10 supply the actual motivic coefficient
object/top map and prove that(6.3) vanishes in real Deligne
cohomology. The RATIONAL lifting problem for the original input
remains, with transition(6.4), connection(6.5), and the nontrivial
Poincaré boundary(7.1). Real existence does not select a rational
lift or produce the required boundary compatibility.

**[GAP MCE-389].** Construct and select a rational
coefficient-valued class in this geometry (or another
justified secondary construction), with the required
boundary compatibility, whose projection/secondary
evaluation carries the original spectral data and
compares arithmetically to D_pt tensor B2 tensor Q(-2).
Prove the exact coefficient6·389·388 n_E and its integral
lattice statement as conclusions. The real class has
not been declared rational and the excluded ordinary
B_c→constant determinant map is not being retried.

The fundamental-group construction of the Poisson input
q_F is the coordinator's separate task; it is not duplicated
here. No old certificate, completed-proof expansion,
shared synthesis edit or additional agent was used.
The original eight sections and the additional constructions below
have separate PASS verdicts in the linked independent review.

## 9. An explicit motivic coefficient object and its top map

This additional construction was proposed by the coordinator after the
separate PASS review of §§1–8 and has its own PASS verdict. It supplies the motivic object/top-map
substep left unconstructed in §6. It uses the actual algebraic family,
not an inference that every variation of mixed Hodge structures is motivic.
The rational spectral input and its motivic lifting obstruction remain
separate questions.

Work in the stable enhancement of the rational category of Beilinson
motives DM_B(mathcal S); its homotopy category is the category used in
[Cisinski–Déglise, *Triangulated categories of mixed motives*, author
version dated8September2019](https://deglise.perso.math.cnrs.fr/docs/2019/DM.pdf).
All schemes here are separated of finite type over Q and regular.
The relevant formalism is Theorem2.4.50, Corollary14.2.11 and
Theorem15.2.1. The HB-module model in14.2.9 gives actual homotopy
fibers/cofibers, so we do not choose a nonfunctorial cone in an
unenhanced triangulated category. No motivic t-structure is assumed.

Put
\[
 p:U=(E\setminus A)\times\mathcal S\longrightarrow\mathcal S,
 \qquad q:\mathcal B\longrightarrow\mathcal S,
 \quad\mathcal B=\{(w,z):w-\pi(z)\in B^*\}.
\]
This is exactly the moving marking from §1. The map q is finite étale:
translation identifies it, as a scheme over the base, with
B^* times mathcal S. Its embedding i:mathcal B→U is the nonconstant
part. Let b=degree(q), counting all geometric points in B^*, including
the nonrational correction support. Define
\[
 \begin{split}
 C_{\rm rel}&=\operatorname{Fib}(p_*1_U\longrightarrow q_*1_{\mathcal B}),\\
 A_{\mathcal B}&=\operatorname{Cofib}(1_{\mathcal S}
                                       \longrightarrow q_*1_{\mathcal B}),\\
 V_{\rm all}&=(C_{\rm rel}[1])^\vee .
 \end{split}                                                   \tag{9.1}
\]
The first arrow is restriction, induced by1_U→i_*1_B. In the
second arrow the unit is the constant function1 on the moving support.

**[NEW] Lemma9.1.** All objects in(9.1) are constructible and
strongly tensor-dualizable. The Artin object A_B is the direct
summand of q_*1 cut out by
\[
 e_{\mathcal B}=1-b^{-1}\operatorname{unit}\circ\operatorname{tr}_q.
                                                               \tag{9.2}
\]
There is a natural motivic map V_all→A_B^vee realizing the positive
relative-homology boundary map.

*Proof.* The finite étale trace is the proper counit, using q^!=q^*.
Its composite with the unit is b. Thus(9.2) is idempotent and its
image is the cofiber in(9.1); the division by b is explicitly rational.
A smooth proper motive and its dual are strongly dualizable by
CD Proposition2.4.31. For the open curve, let bar p:E×S→S and
p_A:A×S→S. Localization along the three fixed puncture sections
and codimension-one purity give the triangle
\[
 (p_A)_*1_{A\times\mathcal S}(-1)[-2]
       \longrightarrow \bar p_*1_{E\times\mathcal S}
       \longrightarrow p_*1_U .                            \tag{9.3}
\]
Here purity is CD Theorem14.4.1, and the shifts/twists are not
suppressed. Both first objects are strongly dualizable, as is q_*1.
Strongly dualizable objects form a thick subcategory, so cones,
duals and direct summands give the assertion for(9.1). This does
not assert rigidity of every constructible motive over the base.
The same triangle and proper base change identify p_*1_U with
the pullback of the constant open-curve cohomology motive.
In particular its fiber comparison does not rely on improper
base change for an arbitrary nonproper family.

The unit1→p_*1 and identity on q_*1 give a map of cofiber diagrams,
\[
                  A_{\mathcal B}\longrightarrow C_{\rm rel}[1].
\]
Dualizing produces the asserted map. Its sign can be checked in the
actual relative cochain cone. Write its differential as
D(a,c)=(da,i^*a-dc). The natural cofiber boundary sends a function
beta on B to(0,-beta). A relative path with boundary Z is represented
in the dual chain cone by(gamma,-Z), whose boundary is zero. Their
pairing is +sum_Z n_Z beta(Z). Thus dualizing the natural cone map
gives the POSITIVE divisor boundary; no change of the marked points'
signs is required. Square.

Write the two original divisors on the support as
Z_j=sum_Z n_(j,Z)[Z], with Galois-invariant coefficients. On each
closed-point component of B*, multiply the finite étale trace by
n_(j,Z) and sum. This gives a rational map
lambda_j:q_*1_B→1_S. Its composite with the unit is degree Z_j=0,
including the residue-field degrees. Consequently lambda_j factors
explicitly through e_B, defining lambda_j:A_B→1. Duality gives the
actual marking
\[
 L=1_{\mathcal S}^{\oplus2}\longrightarrow A_{\mathcal B}^{\vee}.
\]
Define its derived pullback by
\[
 V_{\rm marked}=\operatorname{Fib}
       \left(V_{\rm all}\oplus L
        \xrightarrow{\;\partial-\mathrm{mark}\;}A_{\mathcal B}^{\vee}\right).
                                                               \tag{9.4}
\]
This is a rational motivic object with its actual projection to L.

**[NEW] Proposition9.2.** The Betti and de Rham realizations of(9.4)
are concentrated in ordinary degree zero and identify, with the
specified frames, with mathbb V from §1. Its rational antisymmetric
square
\[
 W_{\rm mot}=\operatorname{im}
       \left(\frac{1-\tau}{2}:V_{\rm marked}^{\otimes2}
                                      \longrightarrow V_{\rm marked}^{\otimes2}\right)
                                                               \tag{9.5}
\]
has realization mathbb W. Identify its corresponding image line in
L tensor² by e1 tensor e2−e2 tensor e1↦1, using the SAME alternating
tensor frame on source and target. The raw projector of e1 tensor e2
is half that framed generator, not the generator itself. Thus the
framed projection to L defines a motivic top map W_mot→wedge²L=1_S
with coefficient one on those frames. Its actual fiber
\[
                      F_{\rm mot}=\operatorname{Fib}(W_{\rm mot}\to1_S)
                                                               \tag{9.6}
\]
realizes the coefficient F=W_(-1)mathbb W in §6.

*Proof.* Each relative fiber has only H¹: the map H0(E minus A,Q)
→H0(B,Q) is injective, the open curve has H²=0, and B has no
positive-degree cohomology. Its cohomological relative sequence is
\[
 0\to H^0(B,\mathbb Q)/\mathbb Q
   \to H^1(E\setminus A,B;\mathbb Q)
   \to H^1(E\setminus A,\mathbb Q)\to0.                 \tag{9.7}
\]
The constant/finite étale fiber comparisons in Lemma9.1 apply to
these maps. After the shift[1] and duality, V_all has the usual
relative H1 in degree zero and surjects onto Div0(B)_Q=A_B^vee.
The Betti realization of(9.4) is therefore an ordinary pullback,
with no extra degree-one cohomology. Its kernel is H1(E minus A)
of rank4 and its quotient L has rank2. The degree-zero divisor
marking is exactly the two translated Z_j, with the positive sign
proved above. The generalized-Jacobian realization of this marked
pair is the one-motive M_z already identified in §1. This proves the
rank6 comparison and retains all original h_j corrections.

The same relative complex of algebraic forms, with evaluation at
B and its comparison to integration over these marked paths, gives
the de Rham realization. Its Baer-difference connection is(3.3),
so the computed dlog functions and native2pi i Tate factors remain.
For a formal realization reference, CD17.2.18 and Examples17.2.21–22
supply the de Rham/Betti six-functor comparison. For its Hodge-filtered
refinement use [Tubach2407.02256v3,29September2025, Theorem1.4 and
Remark1.2](https://arxiv.org/html/2407.02256v3#S1.SS2): after base
change to C, rational étale motives have a Hodge realization compatible
with the six operations and with the underlying Betti functor.
CD16.2.18 identifies the rational étale category with Beilinson motives.
This is applied over C, with the original rational algebraic maps kept;
we do not assume the speculative arithmetic-MHM extension mentioned
in Tubach's Remark1.3. The geometric rational de Rham frame and the
real involution are the ones already fixed by the Q-defined pair.

The realizations are symmetric monoidal and preserve the idempotent
in(9.5). Because V_marked realizes a vector space in degree zero,
that idempotent is its ordinary exterior-square projector. The
shift[1] used to make the homological coefficient degree zero must
be retained: on the unshifted geometric H¹ product, interchange has
the extra degree1-by-degree1 Koszul minus. Thus(9.5) is precisely the
PLUS geometric interchange used in the previous determinant proof.
It does not reverse the exterior sign or introduce a new factor2.

The map to wedge²L is surjective on realizations. Its kernel is
exactly the lower-weight part F, proving the assertion for(9.6).
There is no claim that(9.6) is a truncation for an assumed motivic
weight or t-structure. The rational projectors divide by b and2;
the integral alternating-tensor map of §§1–4 is still used on BOTH
top and bottom frames. No integral motivic primitivity follows. Square.

This now gives an actual rational relative coefficient complex.
For Z=mathcal S×E_t, h:Z→SpecQ, a:Z→mathcal S, and
h_B:B_cusp→SpecQ, define
\[
 K_{W,\rm mot}(2)=\operatorname{Fib}
 \left(h_*a^*W_{\rm mot}(2)
   \longrightarrow (h_B)_*(a^*W_{\rm mot}|_{B_{\rm cusp}})(2)\right),
                                                               \tag{9.8}
\]
and similarly for F_mot and1. Their coefficient triangle is an
actual triangle in DM_B(Q), whose motivic groups are defined by
Hom_(DM_B(Q))(1,K[j]). Six-functor realization gives the Betti and
de Rham versions of(6.2); its Hodge realization followed by the
natural map to the real Deligne cone gives the regulator comparison.
No general identification of absolute Hodge cohomology with ordinary
Deligne cohomology for this nonproper coefficient complex is asserted.

If x in H_M³(K_Q,mot(2)) had regulator c_S, the precise rational
lifting obstruction would be the image of x in H_M⁴(K_F,mot(2)).
This is now a specified motivic obstruction, not just a symbol for
an expected coefficient category. Constructing such an x and proving
its motivic obstruction zero remain unproved.

For j:mathcal S→C and the added boundary i_Sigma, the same category
also supplies i_Sigma^*j_*W_mot and the localization triangle
j_!W_mot→j_*W_mot→(i_Sigma)_*i_Sigma^*j_*W_mot. Its realization
retains the two-term local complex(5.2). It does not supply a zero
trivialization of the nontrivial Poincare bundles in §7.

## 10. The real coefficient obstruction vanishes, without a rational input

This is a second additional deduction, prompted by the coordinator's
relative-CW calculation. It computes the REAL obstruction(6.3), while
leaving the motivic obstruction and the choice of an arithmetic lift open.

**[NEW] Proposition10.1.** The original restricted radial class c_S
has a lift to H_D³(mathcal S×E_t,B_cusp;mathbb W(2)). Equivalently,
\[
                         {\cal O}_{\mathbb W}(c_{\mathcal S})=0.
                                                               \tag{10.1}
\]
This does not specify a canonical lift, a rational motivic input,
or compatible rational trivializations at Sigma.

*Proof.* Sigma is nonempty: pi is finite surjective and its inverse
image of-R is contained in Sigma. Hence mathcal S=C minus Sigma is
a connected noncompact finite-type complex curve. Let B0 be the two
original cusps, which lie in mathcal S. The pair(mathcal S,B0) has a
finite relative CW model of dimension one. For example, remove small
discs around the missing points in the compact surface, choose a spine
through the two specified interior points, and retract to that graph
relative to those points. For any finite-rank local system A this gives
\[
 H^i(\mathcal S,B_0;A)=0\quad(i\ge2),\qquad
 H^0(\mathcal S,B_0;A)=0.                                  \tag{10.2}
\]
For the latter statement a horizontal section vanishing at one of the
marked points vanishes on the connected curve. No constancy or
semisimplicity of A is needed.

Apply the relative local-system sequence0→F→mathbb W→Q→0.
Its long exact sequence and(10.2) give a surjection
\[
 H^1(\mathcal S,B_0;\mathbb W_\mathbb C)
        \twoheadrightarrow H^1(\mathcal S,B_0;\mathbb C).
                                                               \tag{10.3}
\]
The coefficient is pulled back from mathcal S to the product with
E_t. Relative Kunneth over C, using both vanishings in(10.2), gives
\[
 H^2(\mathcal S\times E_t,B_0\times E_t;\mathbb W_\mathbb C(2))
 =H^1(\mathcal S,B_0;\mathbb W_\mathbb C)
                                      \otimes H^1(E_t,\mathbb C)(2).
                                                               \tag{10.4}
\]
The analogous formula holds for Q. Thus(10.3) gives surjectivity on
the full complex degree-two cohomology of these relative product pairs.
The twist(2) remains on the entire tensor in(10.4).

For every coefficient Deligne cone there is the natural map
\[
 a_D:H^2(\text{relative complex cohomology})
                                \longrightarrow H_D^3.
                                                               \tag{10.5}
\]
It comes from inclusion of the complex-cohomology term shifted by-1
in Cone(real cochains plus filtered de Rham cochains→complex cochains)[-1].
We use the same cone convention for all coefficients, so(10.5) is
functorial with no changed sign or Tate normalization.

For the ORIGINAL proper pair(V0,B0×E_t), the completed
[point-determinant proof, Lemma7.1](point-determinant-single-valued-attack.md)
derived from that proper relative cone that a_D in degree two is
surjective onto H_D³: its next real Hodge-class term is zero by the
strictly negative weights of H³(V0,B0×E_t;R(2)). Thus choose a complex
cohomology class w with a_D(w)=C_j2. This uses that already proved
proper-pair fact, rather than merely the assertion that the Betti
component of C_j2 is zero.

Restrict w to the open pair and lift it complex-cohomologically by
(10.3)–(10.4), obtaining tilde w with mathbb W coefficients. Then
functoriality of(10.5) gives
\[
 \operatorname{top}(a_D(\widetilde w))
       =a_D(w|_{\mathcal S\times E_t})=c_{\mathcal S}.
\]
If the arithmetic real involution is imposed, average the resulting
real Deligne lift with its conjugate. The Q-defined pair and top map
commute with this involution and c_S is invariant; averaging preserves
its top image. Equivalently one may average w and its lift with their
induced involutions. This is a real-linear averaging step, not a new
rational-motivic construction. No Hodge-strictness theorem for the
nonproper coefficient complex was needed. Square.

The possible real lifts remain a torsor under the image of
H_D³(K_F(2)), exactly as in §6. Proposition10.1 proves existence in
that real torsor. It neither singles out its point nor proves that
this point or the scalar input comes from(9.8) over Q. In particular,
real vanishing in(10.1) does not force motivic vanishing for any putative
rational input. The nontrivial new Poincare boundary still has to be
retained when changing support conditions or taking a compact trace.

The exact remaining target is therefore the RATIONAL input, its
motivic obstruction/selection and the boundary-compatible secondary
comparison of GAP MCE-389, with the same quadratic/cubic frame,
6·389·388 n_E coefficient and integral lattice question. §§9–10
close the coefficient-object and real-existence substeps only.
Both additions have a separate independent PASS verdict in the linked review.
