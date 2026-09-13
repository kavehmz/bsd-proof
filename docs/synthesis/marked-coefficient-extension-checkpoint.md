# Marked coefficient extension — complete and independently reviewed

Date:2026-09-13. Owner /root/higher_period_integrality,
GPT-6 Astra/xhigh. All ten proof sections are complete.
[Proof](marked-coefficient-extension-attack.md).
[Independent PASS: original §§1–8 and separate §§9–10](review-marked-coefficient-extension.md).

The objective remains FULL BSD for every elliptic curve over Q.
The bounded construction is complete; BSD and the rational spectral
comparison are not proved. Parent owns the active goal and shared
synthesis. This agent's scoped goal=null is expected, not cancellation.

## Ownership and final revisions

Construction ownership:
- marked-coefficient-extension-attack.md
- this checkpoint

Reciprocal review ownership:
- review-cm-derived-unsmoothing.md, complete PASS against the author's
  mathematical c37c8b717bea884135fc5a241a6318383f9bfc59c726449821be6bbfe9ac80df.

Final marked proof after EDITORIAL reconciliation:
76a2f2e074b8fd6019e617f0ab5cf27c328d4bcfe54dd570f79cc7972c2f281d.
The last mathematical revision inspected for the additional verdict was
30b53a2840611c14e3f40d0a7f2a124fa3c18b33ba80dd72ada0051a659de451.
The original eight-section mathematical revision was
0b8ce84dc7b834977458fbb21a14dea75976f1b7872f007a93929a1eb011c6b3.
Both distinct verdicts remain in the same independent review, final SHA256
ca03b193e90da2ea6ae101ba12fd8e6b316b136c2194b8400d8301422ed0f5e6.
The reciprocal CM review SHA256 is
90ec6465d318a918f0b2081f7e2d1b3202c386e1c197b99ecc097a90cbe127f7.

No mathematical addition is pending. After the final PASS only the
proof header, status summaries in§§6/8 and concluding review sentences
were reconciled. The old statement that the motivic coefficient object
was not yet constructed is superseded by§9. The old unknown REAL
obstruction is superseded by§10. Rational input and motivic lifting
questions remain explicitly open.

## Exact construction to retain

Use E:y²+y=x³+x²−2x, full basis P=(-1,1),Q=(0,-1),
R=P+Q=(4,8), S=R+P=(-51/25,-68/125), T=R+Q=(1/16,-9/64).
The fixed corrected divisors are Z1=S−R+divh1 and Z2=T−R+divh2,
with the exact h1,h2 and ALL support B* from the completed point proof.
A={O,P,Q}. Remove every collision a−Z, a∈A,Z∈B*, from the moving
elliptic base, and pull back by x=pi(z) to mathcal S=C minus Sigma.
Both original cusps belong to mathcal S and have the fixed M0 fiber.

The actual translated marking [Z_j]→AJ_A(T_xZ_j) differs from M0
by torus Kummer functions
F_j(x,w)=(m_(R,x)(w)/m_(R+P_j,x)(w)) h_j(w−x)/h_j(w),
a_ij(x)=F_j(x,P_i)/F_j(x,O), with F_j(x,O)=h_j(−x).
The monic-y Miller chord/vertical convention gives
 div_w F_j=T_xZ_j−Z_j up to vertical base factors,
 div_x a_ij=sum_Z n_(j,Z)([P_i−Z]−[−Z]), and a_ij(O)=1.
Vertical base factors cancel in the normalized evaluation.

The only new arithmetic evaluations were exact rational substitutions:
h1(S)=505109/205209, h2(S)=72126/22801,
h1(T)=14977/3969, h2(T)=1945/441.
At R and−R both h_j have pole order2, with nonzero leading numerators
h1:8320,−9360; h2:160,−180. Therefore
 ord_(−R)(a_ij)=[[4,3],[3,4]], determinant7.
Odd independently reproduced these targeted values and the group law;
no old rank, height, Mellin, derivative or prime-scan certificate was rerun.

The exact Baer-sum connection is
 nabla e_j^dR=−sum_i dlog(a_ij∘pi)t_i^dR,
with the original constant M0 point/Hodge comparison retained.
T_Z=Div0(A)^dual tensor Z(1) is the Betti Tate lattice; it is not
identified with the algebraic torus. Positive monodromy adds the
orders times t_i^B, with t_i^B=2pi i t_i^dR under comparison.
Write N_dR for the NEGATIVE connection residue; T=exp(2pi i N_dR).
The Betti logarithm Lambda=logT and de Rham N_dR are distinct.

The archimedean block is H(x)=H+log|a(x)|. At rational x the finite
terms vp(a_ij(x))logp restore the ORIGINAL global height matrix H
by the product formula. The moving archimedean determinant is not
the global regulator. At both original cusps H(x)=H.
Its exterior has delta² coefficient detH(x)/(2pi²) and conjugation
coefficient−detH(x)/pi². Tensor with the SAME rational beta2 extension
has cube3delta_W² tensor delta_beta. Near−R, detH(x)=7log²|t|+O(log|t|).
Untwisted W tensor B_beta has bottom K(2), weight−7, forK=H1(E,Q2).
An EXTRA overall twist(2) gives K(4)=H1(E,Q6), weight−11.

At a point over−R with ramificatione, Lambda²(top)=14e²bottom,
and(T−1)(top)'s quadratic bottom coefficient is7e². There is no
invariant top lift. The derived boundary [W→(T−1)W] keeps bothH0/H1,
each of dimension9; rational Jordan types are3,2,2,2,2,1,1,1,1.
No integral Smith change dividing7 or Sha bound is inferred.

## Actual motivic coefficient complex — §9

Work in the stable HB-module enhancement of rational DM_B(mathcal S).
For p:U=(E minus A)×mathcal S→mathcal S and the actual finite étale
moving support q:B→mathcal S, define
 C_rel=Fib(p_*1_U→q_*1_B), A_B=Cofib(1→q_*1_B),
 V_all=(C_rel[1])^dual.
A_B is the Artin summand cut out by1−unit·trace/b, b=degreeB.
The natural cone map A_B→C_rel[1] dualizes to V_all→A_B^dual.
The two degree-zero divisor trace functionals define L=1²→A_B^dual.
Then
 V_marked=Fib(V_all⊕L→A_B^dual)
is an ACTUAL rational motivic coefficient object, realizing rank6M_z.
This uses a derived pullback, not an assumed motivic t-structure.

Dualizability is proved for these objects by the actual localization
 pA_*1(-1)[-2]→pE_*1→p_*1_U.
The proper smooth elliptic term and finite étale terms are dualizable;
cones, duals and retracts preserve that property. No assertion that
every constructible motive over mathcal S is tensor-dualizable is used.

The cofiber boundary is beta→(0,−beta) for relative differential
D(a,c)=(da,i*a−dc). Pairing with a path(gamma,−Z) gives the POSITIVE
marking sum n_Z beta(Z). The shift[1]/dual gives H1 in degree0.
The rational antisymmetric idempotent on V_marked tensor² therefore
corresponds to the old PLUS geometric interchange before the shift.
On BOTH source and target use the alternating tensor frame:
 e1 tensor e2−e2 tensor e1↦1 on the top line of L tensor².
The raw projector of e1 tensor e2 is half that generator; the framed
top map W_mot→wedge²L=1 has coefficient1. Divisions byb and2 are
retained; no integral motivic primitivity is claimed.

F_mot=Fib(W_mot→1) realizes the lower-weight coefficient F. Applying
the explicit relative functor for(S×E_t,two old cusp fibers) gives
the ACTUAL coefficient triangle K_F,mot(2)→K_W,mot(2)→K_Q,mot(2)
inDM_B(Q). Its groups are Hom(1,K[j]). The derived Sigma-boundary
motive iSigma^*j_*W also exists and keeps the circle-cochain data.

## Real obstruction zero — §10

Sigma is nonempty, so(S,two old cusps) has relative CWdimension1.
H0 and H2relative vanish for EVERY local system. Hence
H1(S,B0,W_C)→H1(S,B0,C) is surjective. Relative Kunneth with the
proper testE gives surjectivity on full complexH2 of the product.

The ORIGINAL proper-pair radial class is a_D(w) for a complexH2
representative w, by the completed proper Deligne-cone/weight proof.
Restrict w and lift it using that H2 surjection; naturality of a_D
then gives a real Deligne coefficient lift of c_S. Thus O_W(c_S)=0.
Arithmetic conjugation can be imposed by real averaging. No Hodge
strictness for the nonproper coefficient complex and no Betti-zero-only
shortcut is used. The lift is not canonical: choices form a torsor
under the IMAGE of H_D3(K_F(2)). No scalar normalization changed.

## Primary sources, remaining gap and handoff

Directly inspected sources:
- Sertoz–Ouaknine–Worrell2505.20397v1§6.5Prop6.5.43, marked
  generalized-Jacobian realization and2pi i;
- Milne1990aT ChapterIV§§1–2Prop2.4, general one-motive comparison;
- MVWDefinition7.10 and its relative Picard sequence;
- Cisinski–Déglise author PDF dated8Sep2019,442pages,
  https://deglise.perso.math.cnrs.fr/docs/2019/DM.pdf,
  2.4.31/50,14.2.9/11,14.4.1,15.2.1,16.2.18,17.2.18/21–22;
- Tubach2407.02256v3,29Sep2025,§1.1Remark1.2/§1.2Theorem1.4,
  https://arxiv.org/html/2407.02256v3.
The Hodge realization is applied AFTER base change toC. No speculative
arithmetic-MHM extension from TubachRemark1.3 is assumed. Its natural
map to the real Deligne cone is used without a general absolute-Hodge
cohomology=ordinaryDeligne assertion for a nonproper coefficient pair.

Remaining GAP MCE-389: a RATIONAL spectral input, its MOTIVIC obstruction
vanishing, a specified arithmetic lift, and boundary-compatible secondary
comparison toD_pt tensorB2 tensorQ(-2), with coefficient6·389·388n_E
and the integral lattice statement as CONCLUSIONS. The graph line at
s over−R restricts to O_E((-R)−O), nontrivial even rationally. Its
actual boundary tuple gives a Picard torsor, not zero trivializations.
Neither the real lift nor the coefficient motive removes this condition.

Root separately constructed the Poisson iterated-source input; no part
of that task was duplicated. The completed CM reciprocal audit is saved.
No mathematical process is live; no new agents, shared synthesis edits,
completed predecessor edits or old certificate reruns occurred.
Next action: report these final hashes to root for integration, then
await a new bounded assignment on the same Astra/xhigh handle.
