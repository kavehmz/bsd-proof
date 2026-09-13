# A rational K2 class in the relative cusp boundary

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Completed bounded construction; all new deductions passed
[independent review](review-relative-beta2-boundary.md).
Restart: [checkpoint](relative-beta2-boundary-checkpoint.md).
The completed radial correction is an unchanged input.
Full BSD for every elliptic curve over Q remains unresolved.

We construct an actual rational relative motivic class, prove it nonzero
motivically, and compute its original logarithmic pairing. Its period
contains the noncentral L-value and the elliptic period. It does not
contain the point-height determinant; comparison to the spectral class
remains an additional arithmetic problem.

## 1. Fixed objects and conventions

Let N=389, X=X0(N), E=389a1,
\[
 V=X\times E,\quad B=B_0\amalg B_\infty,\quad
 B_c=\{c\}\times E,\quad V^\circ=V\setminus B.
\]
The two rational immersions are i_c:E→V and p_E:V→E is projection.
The actual modular unit and its divisor are
\[
 u(z)=N^{-6}\Delta(z)/\Delta(Nz),\qquad
 \operatorname{div}(u)=(N-1)([0]-[\infty]).
 \tag{1.1}
\]
The fixed modular map satisfies pi(0)=pi(infinity)=O and
\[
 \alpha=\pi^*\omega_E=c_\pi\,2\pi i f(z)\,dz.
\]
We retain its actual nonzero rational Manin scalar c_pi.

Use the ALREADY CONSTRUCTED class of the
[integrated spectral proof, §7](integrated-spectral-comparison-attack.md)
\[
 \beta_2\in H^2_M(E,\mathbb Q(2)),\qquad
 \mathscr R_E(\beta_2)=L(E,2)/\pi>0.                       \tag{1.2}
\]
This proof neither reconstructs beta2 nor changes its arithmetic
extension or its sufficient integral multiple. Those do not assert
integral primitivity. The fixed real regulator is
\[
 \eta_K(f,g)=\log|f|\,d\arg g-\log|g|\,d\arg f,\qquad
 \mathscr R_E(\beta)=\int_b\eta_K(\beta),
 \tag{1.3}
\]
where a,b is the established integral symplectic basis, conjugation
fixes a and negates b, and
\[
 \omega_1=\int_a\omega_E>0,\quad \Omega_E=2\omega_1,\qquad
 \int_E\omega_E\wedge\eta_K(\beta)
                      =\omega_1\mathscr R_E(\beta).       \tag{1.4}
\]
The equality is the previously proved Riemann-bilinear normalization,
not an identification of omega1 with the full real period.

Let
\[
 C_M(V,B;q)=
  \operatorname{Cone}(R\Gamma_M(V,\mathbb Q(q))
             \longrightarrow R\Gamma_M(B,\mathbb Q(q)))[-1].
 \tag{1.5}
\]
In a fiber cochain model the differential is
D(c,b)=(dc,i^*c-db), with natural PLUS projection to c.
The POSITIVE boundary used here is the cochain map
\[
 \partial^+(b)=(0,+b)=-\partial_{\rm can}(b).
 \tag{1.6}
\]
This explicit sign is part of the definition. It is the negative
of the usual connecting map for the stated fiber convention.
Exactly the same convention is used after the Deligne regulator.

The pair is proper, so M(V,B)=Cone(M(B)→M(V))=M^c(V^\circ);
hence H_M^*(V,B)=H_{M,c}^*(V^\circ).
The localization statement is
[Voevodsky, Proposition4.1.5](https://www.math.ias.edu/Voevodsky/files/files-original/Dropbox/Published_papers/Motives/Collection/s5.pdf).
It applies over Q, which admits resolution. No ordinary open
cohomology is substituted for this relative object.

## 2. The two restriction maps agree already motivically

**[NEW] Proposition2.1.** For every motivic degree and twist, the
maps i_0^* and i_infinity^* agree over Q. In particular,
\[
 \operatorname{im}\left(H^2_M(V,\mathbb Q(2))
      \longrightarrow H^2_M(B,\mathbb Q(2))\right)
   =\{(\beta,\beta):\beta\in H^2_M(E,\mathbb Q(2))\}.
 \tag{2.1}
\]

*Proof.* A morphism E→V induces the degree-zero Chow correspondence
given by its graph in E×V, a codimension-two cycle.
Under E×V=E×X×E, put
\[
 W=\{(P,x,P):P\in E,\ x\in X\}\simeq X\times E .
\]
This is a codimension-one support. Its actual rational function
u(x) has divisor
\[
 \operatorname{div}_W(u)
   =(N-1)\bigl(\Gamma_{i_0}-\Gamma_{i_\infty}\bigr).
 \tag{2.2}
\]
Thus (W,u)/(N-1) is a rational higher-Chow CH²(-,1) CHAIN
with the displayed boundary, not a closed higher cycle.
We use the positive-divisor convention, as in the preceding
Rost/KLM audit. In particular the two graph correspondences
are equal in CH²(E×V)_Q.

The functor from effective Chow motives to geometric motives
(Voevodsky, Proposition2.1.4),
and the action of Chow correspondences on motivic cohomology,
therefore identify M(i_0) with M(i_infinity).
The explicit higher-Chow chain(2.2) supplies the rational
equivalence underlying this equality. The correspondence action/projection formula
is [Levine, Theorem5.2 and Corollary5.3](https://www.numdam.org/article/AST_1994__226__235_0.pdf);
the embedding of Chow motives is part of Voevodsky's construction
in the primary text linked above. This proves equality in
every degree, without a Betti-only inference.

Finally i_c^*p_E^*=id for both cusps. Hence every diagonal
pair is realized by the actual pullback p_E^*beta.
There are no further pairs by the proved equality, giving(2.1).
Square.

Integrally, the same argument proves
(N-1)(i_0^*-i_infinity^*)=0; it does not divide N-1 as a
unit at primes dividing it. This proof uses rational coefficients
and retains that denominator.

**[NEW] Corollary2.2.** There is an actual rational injection
\[
 \begin{aligned}
 j_B:H^2_M(E,\mathbb Q(2))&\hookrightarrow
                              H^3_M(V,B;\mathbb Q(2)),\\
 \beta&\longmapsto\partial^+(\beta,0).
 \end{aligned}                                          \tag{2.3}
\]
Its definition is independent of a presentation of beta.

*Proof.* Localization identifies the kernel of the boundary on
H_M²(B,Q2) with exactly the image(2.1). The cokernel of that
diagonal is canonically H_M²(E,Q2), by
(beta_0,beta_infinity)↦beta_0-beta_infinity.
The positive boundary has the same kernel as the canonical one,
so it injects this cokernel, with the chosen sign(1.6).
This proves(2.3). Square.

Define the particular class
\[
 \boxed{\mathfrak b_2=j_B(\beta_2)
                   =\partial^+(\beta_2,0).}              \tag{2.4}
\]
It is nonzero: beta2 is nonzero by(1.2), and j_B is injective.
This proves motivic nonvanishing BEFORE calculating its scalar.
The class from the other cusp is -mathfrak b2 because a diagonal
pair has zero boundary. No finite-generation or rank-one theorem
for the full K2(E)_Q is used.

## 3. The native Deligne K2 form, derived from the product

We now check the regulator factor rather than read it off a
real one-form by analogy. In the concise Deligne form complex,
\[
 D^2(E,2)=E^1_{\mathbb R}(1),\qquad
 d_D=-\operatorname{pr}^{1,1}d:D^2(E,2)\longrightarrow D^3(E,2).
 \tag{3.1}
\]
The factor R(1)=2pi i R matters here.
The total Deligne complex and its homotopy maps are exactly
[Burgos–Goswami1712.10150v2, §§4.3–4.5](https://arxiv.org/html/1712.10150v2).
For x=log|f|, the image of the unit regulator in the total
complex is
\[
 G(x)=(\partial x-\bar\partial x,\ 2\partial x,\ x).
\]
The regulator convention x=log|f| is the one fixed in(1.3)
and in the earlier unit/Chow orientation audit.

For closed triples (r_1,f_1,w_1),(r_2,f_2,w_2), use the
Beilinson product whose third component is
\[
 w_1 f_2+(-1)^{n_1}r_1 w_2 .
\]
It is one of the homotopic product choices of the total
complex; the differential is
d(r,f,w)=(dr,df,f-r-dw).
For n_1=n_2=1 this gives
\[
 2x\partial y-y\partial x+y\bar\partial x.
\]
Projection to the imaginary real form part in(3.1) takes
half the difference with its complex conjugate. The result is
\[
 x(\partial y-\bar\partial y)
               -y(\partial x-\bar\partial x)
       =i\bigl(\log|f|d\arg g-\log|g|d\arg f\bigr).
\]
Thus in the native Deligne FORM frame
\[
 \boxed{r_{\cal D}(\beta)=i\,\eta_K(\beta).}                \tag{3.2}
\]
Both products and their homotopies give the same cohomology
class. This is also obtained from the symmetric product in
Burgos–Goswami(4.8). The product compatibility with the actual
Beilinson regulator is
[Burgos–Feliu0907.5169v1, Theorem3.5 and §5](https://arxiv.org/html/0907.5169).

For unramified K2 classes the logarithmic one-form has no
small-loop residue. Explicitly, for f=t^m a and g=t^n b,
the loop integral is 2pi(n log|a|-m log|b|). In the fixed
Rost convention partial{f,g}=(-1)^(mn)b^m/a^n, this is
MINUS 2pi log of the tame symbol's absolute value.
It is zero for the unramified class.
Consequently(3.2) extends to the global Deligne class.
A smooth closed representative may be chosen. Replacing
the regulator by that representative changes no period(1.4).
The construction of beta2 is compatible with the finite
trace and norm maps already checked in the earlier proof,
so(3.2) applies to that actual class with its original
coefficients.

There are two separate scales. In dimension two, the unit-normalized
degree-three, twist-two relative current S is represented by
2pi i S in the native Deligne FORM complex. The ordinary
Gillet–Soulé Green-current convention has another factor two:
a GS current T corresponds to pi i T. This is the conversion
already checked in the [radial proof, §3](radial-graph-correction-attack.md).
We use the first scale below; we do not reuse a GS metric scale
for the K2 boundary.

## 4. Exact cutoff representative and its scalar

Let eta be a smooth closed representative of eta_K(beta2).
Choose a real smooth function rho on X, equal to1 near0 and
equal to0 nearinfinity, with derivative supported inside Y.
Pull it back to V. Its values near the two cusps are fixed;
the particular shape is irrelevant. Averaging rho under complex
conjugation makes it invariant. Likewise choose the smooth eta
in its prescribed anti-invariant class by averaging. These choices
give a representative in the real Deligne complex and leave(1.4)
and all subsequent values unchanged.

The Deligne regulator of mathfrak b2 is represented in the
relative cone by (0,i eta on B_0,0 on B_infinity).
The degree-two extension i rho eta on V has exactly that
boundary restriction. Subtracting its relative boundary gives
the cohomologous representative with zero boundary
\[
 (-d_D(i\rho\eta),0)
       =\bigl(i(d\rho\wedge\eta)^{1,1},0\bigr).            \tag{4.1}
\]
The minus sign uses(1.6); the second equality uses(3.1).
After conversion to the normalized current frame this is
\[
 S_{\mathfrak b_2}
    =\frac1{2\pi}(d\rho\wedge\eta)^{1,1}.
 \tag{4.2}
\]
It is smooth, closed in the Deligne complex and vanishes
near BOTH cusp fibers. No singular current restriction or
product with a cusp Dirac is involved in this representative.

Only the eta^(0,1) term survives contraction with omega_E.
By(1.4),
\[
 p_{X,*}(S_{\mathfrak b_2}\wedge\omega_E)
   =\frac{\partial\rho}{2\pi}\int_E\eta\wedge\omega_E
   =-\frac{\omega_1\mathscr R_E(\beta_2)}{2\pi}
                                                   \partial\rho.
 \tag{4.3}
\]
This retains the negative sign from interchanging the two
degree-one fiber forms.

The original scalar functional of the reviewed radial proof is
\[
 {\cal P}(S)=\frac{i}{4\pi^2c_\pi}
      \int_Yp_{X,*}(S\wedge\omega_E)
                           \wedge\bar\partial\log|u|.
 \tag{4.4}
\]
It is a relative/logarithmic Deligne pairing with the specified
de Rham test, not an unmarked absolute-class functional.

**[NEW] Theorem4.1.**
\[
 \boxed{{\cal P}\bigl(r_{\cal D}(\mathfrak b_2)\bigr)
       =\frac{(N-1)\omega_1L(E,2)}{8\pi^3c_\pi}.}          \tag{4.5}
\]
In particular the displayed rational motivic class has a
nonzero value under this functional.

*Proof.* Set m_0=N-1 and m_infinity=1-N.
With dd^c=i partial barpartial/(2pi),
\[
 \partial\bar\partial\log|u|
                       =-\pi i\sum_c m_c\delta_c.
\]
Therefore Stokes gives
\[
 \int_Y\partial\rho\wedge\bar\partial\log|u|
                    =\pi i\sum_c m_c\rho(c)=\pi i(N-1).
\]
One may instead integrate the two punctured disks; their
boundary orientations give the same sign. Substitute(4.3)
and this value into(4.4):
\[
 \frac{i}{4\pi^2c_\pi}
 \left(-\frac{\omega_1\mathscr R_E(\beta_2)}{2\pi}\right)
          \pi i(N-1)
       =\frac{(N-1)\omega_1\mathscr R_E(\beta_2)}
                                                   {8\pi^2c_\pi}.
\]
Finally use(1.2). This proves(4.5) with no guessed Tate factor.
Square.

Changing rho while fixing its cusp values changes(4.1) by an
ordinary relative Deligne boundary; equivalently the last Stokes
calculation depends only on those values. Changing eta by an
exact form does not change(4.3), by compact fiber Stokes.
Thus the evaluation does not depend on these analytic choices.
Choosing the infinity cusp produces the negative value, in
agreement with Corollary2.2. Choosing the canonical rather than
positive boundary also negates the value.

The complete degree calculation is
H_M²(B,Q2)→H_M³(V,B,Q2), followed by the degree-two,
twist-one logarithmic test and a surface trace of shift(-4,-2).
The scalar lies in degree1, twist1. The explicit factors
i, 2pi, c_pi and omega1 in(3.2)–(4.4) implement that
comparison; omega1 is not a rational scalar.

## 5. Comparison with the spectral class still requires the point heights

The newly constructed rational line Q mathfrak b2 is the
actual image of Q beta2 under(2.3). Its nonvanishing and period
are proved without choosing a scalar from the desired Mellin
value. The original completed spectral value remains
\[
 {\cal M}=-\frac{3N(N-1)}{2\pi^3}\ell_E L(E,2),
 \qquad \ell_E=L''(E,1)/2 .
\]
Consequently the exact ratio of the TWO evaluated quantities is
\[
 \boxed{\frac{{\cal M}}
       {{\cal P}(r_{\cal D}(\mathfrak b_2))}
          =-12Nc_\pi\,\frac{\ell_E}{\omega_1}
          =-24Nc_\pi\,\frac{\ell_E}{\Omega_E}.}            \tag{5.1}
\]
This contains ell/omega, not the BSD quotient ell/(Omega Reg).
Its rationality is not proved or assumed.

The full point-height frame D_pt evaluates to
Omega_E Reg_E, and the declared target frame
\[
 D_{\rm pt}\otimes\mathbb Q\beta_2\otimes\mathbb Q(1)^{-2}
\]
evaluates to -Omega_E Reg_E L(E,2)/(4pi³).
This is the unchanged target of the integrated and radial proofs.
The linear cusp boundary supplies no Reg_E factor and no
identification of the particular spectral class C_j2 with a
rational multiple of mathfrak b2. In fact equality of the one
functional value would not establish equality of those relative
classes either.

After formally multiplying the known boundary period by Reg_E,
the determinant of the already constructed point-height matrix,
their product is
-(N-1)/(4c_pi) times the target frame's evaluation. This is a
comparison of specified evaluations, not a new motivic map
selecting a spectral source or a BSD theorem. The missing
arithmetic map still has to retain the actual point classes,
all finite-place corrections and the full period convention.
Its coefficient must be 6N(N-1)n_E as a conclusion.

Nothing here asserts that a rational lift in this particular
relative group is necessary for BSD. It is one tested route.
No finite-generation assumption for K2(E), integral primitivity,
full Sha finiteness or algebraicity of spectral derivatives was
introduced. No old computation, shared synthesis edit or extra
agent was used. All new deductions passed the linked independent review.
