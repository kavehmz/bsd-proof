# Radial graph correction checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Own [radial-graph-correction-attack.md](radial-graph-correction-attack.md)
and this checkpoint only. Initial checkpoint was saved before sources.
Full BSD for every elliptic curve over Q remains the parent objective.
No shared synthesis edits, new agents or old certificate reruns.

## Completed bounded construction

The complete seven-section proof passed independent review in
[review-radial-graph-correction.md](review-radial-graph-correction.md),
SHA2569d1c50b03e4de8876cff0dfa62a7118bcf90606ca39b097f61c9ffda24c7e61e.
Reviewed mathematical proof:
e843569799237cf2022f0103527046e091390379055aef65ea1e13d597c8cf99.
Subsequent proof-header/checkpoint changes are editorial.
The actual new construction is a canonical graph star correction,
an explicit relative cusp homotopy preserving the original scalar,
and the complete zero test of its rational scalar-Kummer source.

## Fixed rational source and normalized geometry

V=X0(389) times E389, B={0,infinity} times E, D=Graph(pi)-X times O.
L_D=d^*O_E(O) tensor p_E^*O_E(O)^(-1), d(x,P)=P-pi(x).
Because pi(c)=O, L_D has canonical rational trivialization on BOTH B_c.
This gives c_D in H_M²(V,B,Q1)=Pic(V,B)_Q.
The source for the sought lift is H_M,c³(Y times E,Q2);
M^c(Y times E)=Cone(M(B)→M(V)), not ordinary open cohomology.

With omega_E=Omega_A dw, beta=pi^*dw=alpha/Omega_A,
g is the canonical log-square elliptic Green function:
ddc g=delta_O-mu_E, integral g mu_E=0.
G=g(w-pi(x))-g(w), ddcG=delta_D-Omega_D, with
Omega_D=i/(2tau2)(beta barbeta-beta dbarw-dw barbeta).
All base/mixed terms are retained; there is no vertical (1,1) term.
ddca wedge Omega_D=0 and p_*(Omega_D wedge omega_E)=alpha.

## Correct star sign and global cusp bounds

The correct correction is
S_a=a delta_D-G ddc a.
Its ddc is ddca wedge Omega_D=0.
The first provisional message's equality with ddc(aG)+aOmega_D
was sign-wrong and was discarded BEFORE the full proof was saved.
The valid global identity is
S_a=aOmega_D+partial U_a+barpartial barU_a,
U_a=i/(4pi)(a barpartial G-G barpartial a).

No undefined cusp-Dirac product is used. The global definition uses
the latter expression and L1 primitives. At either cusp P(q)=O(q^m),
m>=1. The proved bounds are ||G||_L1(E)<=C|P| and
||grad g(.-P)-grad g||_L1(E)<=C|P|(1+|log P|).
They give all L1 products, zero tangential boundary constants and
vanishing cutoff errors. Coarse elliptic points are treated as
locally bounded invariant coefficients with integrable derivative
powers, or smoothed locally. No arbitrary-current pullback is used.
Proper smooth-form contraction gives p_*(S_a wedge omega)=a alpha.

Scalar j2 itself is NOT W1,2, even after subtracting a cusp logarithm:
j2~A y(log y)^2 gives divergent Dirichlet integral.
The mixed form aOmega_D has all finite Lp cusp coefficients instead.
Do not apply Bost's scalar Sobolev theorem to j2.

## Exact scalar and its boundary defect

Use a=j2 for the ORIGINAL scalar:
P(S_a)=i/(4pi² c_pi) integral a alpha wedge barpartial log|u|
      =integral aF dmu.
For a=j2 log|u| the transgression is corrected, but simply
differentiating that product would not establish mass preservation.

An absolute Deligne-exact change with contraction partial b changes
this scalar by -1/(4pi c_pi) sum_c ord_c(u)b(c).
This follows from ddc log|u|=(1/2)sum ord_c(u)delta_c.
Such changes occur for actual smooth primitives, so the scalar
does not descend to the unmarked ABSOLUTE Deligne class.

## Actual relative homotopy

On a cusp disk beta=h(q)dq, solve partial u1=a h with u1(0)=0
and partial u0=a|h|² by Cauchy transforms. The coefficients lie
in Lp for every finite p; choosing p>2 gives continuous primitives.
Set Uloc=i/(4tau2)u0 dbarq-i/(2tau2)u1 dbarw.
Then aOmega_D=partial Uloc+barpartial barUloc exactly.
The tangential primitive on B_c is zero.

Subtract cutoff versions at both cusps and smooth any coarse
elliptic points the same way. This gives a smooth closed relative
Deligne representative vanishing near B. The resulting C_a in
H_D³(V,B,R2) is independent of those choices because all differences
are relative-exact with zero cusp trace. The scalar is unchanged.
General relative-exact boundary primitives are also harmless by
compact Stokes against omega_E on each E fiber. This is the actual
relative/logarithmic degree5, twist3 product followed by surface
integration (-4,-2), ending in degree1, twist1.

## Complete rational scalar-Kummer comparison

There is an actual rational map
K: O(Y)^* tensor Q → H_M,c³(Y times E,Q2),
v ↦ p_X^*{v} cup c_D.
Explicitly apply f_! to the actual unit morphism on the open and
postcompose the compact-support class; no extension of v across B
is assumed. Its regulator is C_log|v| with the canonical zero
boundary constants; the local Green homotopy has limit zero.

Every unit has divisor m(0-infinity), so
v^(N-1)/u^m=c in Q*.
Its logarithm is a rational multiple of log|u| plus a constant.
Constants pair to zero by integralF=0; log|u| pairs to zero by
Fricke oddness against the even F. Hence the ENTIRE tested
rational cup image has zero original scalar. C_j2 has nonzero
pairing, so this scalar-Kummer source cannot provide its lift.
This is a new test of the corrected relative operation, not the
previous norm/polarization projection.

## Exact retained target and primary sources

The full coefficient is
tildej2=j2+gamma1 j1+gamma2 j0+gamma3 R_N.
Its unpaired relative class retains the Gamma-pole term.
Only lower SCALAR pairings vanish. The mass is
M=-3N(N-1)ell_E L(E,2)/(2pi³)
 =-pi²/(2sqrtN)<I_L(F),Ecal_L''(1)>.
The adjoint is now an independently reviewed input.

Primary sources inspected directly:
- Voevodsky, Triangulated categories of motives over a field,
  IAS56-page PDF, Proposition4.1.5 and tensor/localization discussion.
- MVW, Notes on Motivic Cohomology, 221-page draft,
  Definition7.10, following rigidified-line description and exact sequence.
- Déglise, Bivariant theories in motivic stable homotopy, 15-page
  author notes, §§1.1–1.6, six functors and compact products.
- Burgos–Feliu0907.5169v1, real Deligne complex, Theorem3.5,
  arithmetic exact sequence and product.
- Burgos–Goswami1712.10150v2 (69pages), Definitions6.1/6.18,
  Proposition6.19, and conversion Proposition7.3/(7.2)–(7.3).
- Robin de Jong, Arakelov Invariants of Riemann Surfaces,
  Documenta10(2005)311–329, Theorem1.1 and canonical metric discussion.
  Our theta formula and all needed constants are also derived directly.

RGC-389 remains: construct a rational relative higher cycle or
coefficient extension OUTSIDE the tested unit-cup image, and its
rational map to D_pt tensor B2 tensor Q(1)^(-2), retaining finite
places, full real period and exact6N(N-1)n_E coefficient.
A real relative class on a rational pair is not a rational lift.
The beta2 arithmetic extension/integral multiple remains completed,
without a primitive lattice claim.

The independent review checked all seven sections, including the
relative source/regulator comparison and the zero boundary constants.
This bounded task is complete; the rational spectral lift remains open.

Normalization precision applied during review:
The GS product matching the UNIT-normalized Deligne class is
(0,2a) times (D,-G), with Green current 2S_a.
A GS codimension-two Green current T maps to pi i T in the
ordinary Deligne FORM convention d_D=-2 partial barpartial;
therefore2S_a maps to2pi i S_a, as fixed in proof§1.
This agrees with BG1712.10150v2 Proposition7.3 after its
dimension-two integration normalization is included.
S_a, all scalar formulas and the motivic unit cup remain unchanged.
The prior phrase "(0,a)" described the unscaled GS expression;
the final proof now explicitly carries the factor2.

Assigned reciprocal review is complete:
[review-heegner-native-pairing.md](review-heegner-native-pairing.md)
PASS, SHA25631b4179202dd6d49f236fe383df7740776a93e016470d19fd84501ce5cb124e5,
reviewing native proofe67fb3c1... and checkpoint8c8828f6....
The author applied the required exact dual twist transport:
A=u_iota^-1 iota_* on classes and A^-dagger=u_iota iota_* on the
first-slot exponential point. The local logarithm uses its inverse
dual transport. All full-coefficient local/global, Coleman/Euler,
bordered determinant, zeta cancellation and actual norm checks pass.

The radial proof also passed uniform's final relative/cup review.
Its current reviewed mathematical revision is the e8435697 hash above.
The final editorial PASS updates are complete. Root handles shared
integration; the rational spectral lift remains open.

Reviewer requested two final precisions; both applied:
- The difference of any two cusp Cauchy primitives solves the homogeneous
  partial equations, is continuous at0 and hence extends antiholomorphically
  across0. With the zero mixed constant, it is smooth and relatively exact
  in the ORDINARY smooth cone, not an unverified Sobolev-current quotient.
- The exact compact-source typing is written:
  c_D:1_Q→f_!1_U(1)[2], followed by the unit-induced morphism
  f_!1_U(1)[2]→f_!1_U(2)[3]. Their composition is the stated cup.
  This fixes the homological/cohomological motive convention explicitly.
No correction, scalar, norm, Gamma or unit-image formula changed.

Possible follow-on source, NOT yet a theorem or part of the reviewed proof:
The relative long exact sequence has
H_M²(B,Q2)→H_M³(V,B,Q2). Apply it to (beta2,0) on one cusp fiber,
using the already constructed beta2; do not reconstruct beta2.
On real Deligne cohomology the H_D²(V) restrictions to the two
elliptic H_D²(B_c) are diagonal, so the beta2 difference should
supply a nonzero rational relative boundary frame.
Its logarithmic-residue pairing should be an explicit multiple of
(N-1)omega1 L(E,2)/pi. The NATIVE K2 one-form, relative-cone sign
and Tate factors still require an independent direct calculation
before an exact scalar is claimed. The established convention is
eta_K(f,g)=log|f|darg g-log|g|darg f,
R_E(beta2)=integral_b eta_K=L(E,2)/pi, and
r_E(beta)(omega)=-i/2 integral_E omega wedge eta_K
              =-i omega1 R_E(beta)/2
from integrated-spectral-comparison-attack.md(7.8).
Root was sent this lead; no new arithmetic identity is assumed.

Provisional exact beta2 boundary calculation, NOT reviewed/promoted:
The Deligne product of unit logs gives native K2 form i eta_K.
For D(c,b)=(dc,i*c-db), choose the positive relative boundary
partial^+(beta,0)=(0,r(beta))=-partial_canonical(beta,0).
Extending r(beta)=i eta_K by cutoff rho=1 near B_c gives the
zero-boundary representative -d_D(rho i eta_K)
 =i(d rho wedge eta_K)^(1,1).
In the proof's normalized degree3 form frame2pi i, this is
S=(d rho wedge eta_K)^(1,1)/(2pi), so
p_*(S wedge omega)= -omega1 R_E(beta)partial rho/(2pi).
Equation(4.2) then predicts
P(partial^+(beta2,0))=m_c omega1 L(E,2)/(8pi³ c_pi).
For c=0, m_c=N-1. The ratio M/P is
-12N c_pi ell_E/omega1, still not a rationality theorem.
Root received this calculation; it still needs independent
native-product/Tate/cone review before any proof promotion.
