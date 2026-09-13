# Canonical Poisson Hodge framing — restart checkpoint

Date: 2026-09-13. Owner: root. Full BSD over Q remains the active objective.
The recovered candidate below is now a complete independently reviewed
seven-section proof in `poisson-hodge-framing-attack.md`. Its PASS review
is `review-poisson-hodge-framing.md`, SHA256
b88f4ecf7056253deac4c278a26aa23fdaa7522c4b922c707420238abc5caea9,
at mathematical revision8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210.
Root read the full review; no mathematical corrections were needed.
Historical candidate language in the reconstruction below is superseded
by this verdict. The PROSPECTIVE motivic cofiber step at the end remains
unproved and is explicitly outside this verdict.
Root also owns shared synthesis and the completed marked-boundary review.

## Exact completed input

Read `poisson-iterated-source-attack.md` and its PASS review.
X=X0(389), Y=X minus 0,infinity; alpha=pi*omega=c_pi(2pi i)f dz;
theta=dlog u, u=389^-6 Delta(z)/Delta(389z), ell=log|u|.
Base b lies in the reduced finite fiber u=2; keep all Galois conjugates.
L_b=log2. A=int_b^z alpha, B=int_b^z theta, ell'=Re B=ell-log2.
EARLIEST-FIRST I_(eta,xi)=int A_eta xi, with Chen cross term
a_eta(gamma)b_xi(path). rho is a rational-second-kind-basis complex
combination representing bar alpha in compact de Rham cohomology;
its periods are bar a and its residues vanish. Atilde=int rho,
v=bar A-Atilde is single-valued and v(b)=0.

Completed finite formula:
Phi_b=Re(2ell A-I_alpha,theta-I_rho,theta),
ddc Phi=4pi c_pi Re F dmu, ddc=i/(2pi) partial barpartial.
At cusp c use s_c=pp[(bar A_c-Atilde)theta]. Choose RR differential
xi with these principal parts, then a holomorphic eta whose real
periods cancel those of Phi-Re int xi. U=Phi-Re int(xi+eta),
q_F=(U-U(infinity))/(4pi c_pi). Bounded finite limit already proved.
Old proof used prior q_F existence to check the residue compatibility.

## Candidate advance 1: intrinsic principal-part compatibility

On based loops define G(gamma)=I_rho,theta(gamma)+bar I_alpha,theta(gamma).
Chen cross terms cancel because a_rho=bar a_alpha and bar b_theta=-b_theta.
Thus G is a COMPLEX additive character of H1(Y).
At cusp gamma_c, I_alpha,theta=2pi i m_c A_c and
I_rho,theta=2pi i Res_c(Atilde theta), so
G(gamma_c)=-2pi i Res_c s_c.
Sum of cusp loops zero in H1(Y) now proves sum Res s_c=0 without q_F.
Lambda=G+[xi] lies in H1(X,C), with compact Hodge components Lambda10,01.
The old real normalization is exactly
eta=2log2 alpha-Lambda10-bar Lambda01.

## Candidate advance 2: actual ordered path quotient

H=H1(Y,Q). Actual maps pi_*:H->H_E and u_*:H->Q(1).
Boundary t=gamma_0/388 has u_*t=1(1)_B, pi_*t=0; retain denominator388.
H=H_X plus Q(1), H_X=ker u_* mapping isomorphically to H1(X).
For b!=z the geometric length2 HOMOLOGICAL path module
P2=Q[paths b->z]/I_b^3 is realized by relative H2 of
(Y²,{b}xY union diagonal union Yx{z}), orientation ds wedge dt.
Affine curve gives exact 0->H tensor H->P2->P1->0 as rational MHS.
For b=z retain Q plus I/I³; do not discard the constant line.
CHECK exact source statement and homology indexing before asserting.

Use ORDERED lambda(a tensor b)=pi_*a tensor u_*b, target K=H_E(1).
Actual pushout V=(P2 plus K)/{(w,-lambda w)} gives
0->K->V->P1->0. Claim only actual rational MHS/compatible geometric
Betti-de Rham realization unless an actual motivic map is constructed.
Weights 0,-1,-2,-3, pieces Q0,H_X,Q1,K; delta²=0 by types.
K types(-2,-1),(-1,-2). Fixed functional ell_omega(h tensor1(1)_B)
=int_h omega strips the DECLARED Betti Tate generator.
Central de Rham alpha-theta covector restricts to 2pi i ell_omega.

## Candidate Deligne dual covectors

f_alpha=I_alpha,theta factors through V dual; unique I^(2,1) lift
because it is F² and the lower P1 dual has no F².
f_rho1=I_rho,theta+int xi is F¹ by the smooth logarithmic bar formula
I_baralpha,theta+int(xi-v theta).
Here d(xi-v theta)=-baralpha wedge theta, and cancellation of s_c
makes the correction logarithmic at the cusps. Use earliest-first
bar signs, not a transplanted reversed-word DRS convention.

f_rhoD=I_rho,theta+int xi-int Lambda10 is candidate canonical I^(1,2).
On the augmentation-zero lower module, f_rho1+bar f_alpha has class
Lambda+2ell' baralpha (no Q1 component). Subtracting Lambda10 leaves
type(0,1) plus a POSSIBLE weight0 constant. Deligne's exact formula
F¹ intersection (barF² W3+barF¹ W1+barF0 W0) allows that constant.
Check this with the actual formula, and do not set a path constant tozero.
Changing xi by a holomorphic form cancels against Lambda10.

## Candidate exact delta calculation

eD is the unique I00 lift of top1. tD is the unique REAL I^-1,-1
lift in W_-1 V (no delta from Tate to K). Let hatH=e^-i delta_- H_D
be the canonical real split lift of H_X in W_-1 V.
Choose real r_H with ALL compact holomorphic periods equal those of
the path; in particular alpha(r_H)=A and theta(r_H)=0.
Take a real lift R_r into augmentation-zero path module. Differences
are real K. Since both f_alpha and f_rhoD vanish on actual Deligne
H lifts and f_rhoD|K=-bar f_alpha|K (the Tate sign),
f_rhoD(hatH r)=bar f_alpha(hatH r), and therefore
2 f_alpha(hatH r)=f_alpha(R_r)+bar f_rhoD(R_r)
=2ell' A+bar Lambda01(r)=2ell' A+int_b^z bar Lambda01.

Let eB=[path] real. Put e'=eB-hatH r_H-(B/(2pi i))tD.
This annihilates first-order F¹ covectors. Choose unique vK in K_C
with f_alpha(vK)=f_alpha(e'), f_rhoD(vK)=f_rhoD(e').
Then eD=e'-vK is F0 and bar eD-eD is in W_-2; verify exact I00 criterion.
The two central covectors vanish on tD by Deligne types.
Exact conjugation gives
delta eD=(ell'/(2pi))tD+(bar vK-vK)/(2i).
Thus y=pi_-3 delta eD=-Im_B vK and
Re ell_omega(y)=(1/(4pi))Re(f_alpha(vK)+f_rhoD(vK))=-U/(4pi).
The last equality uses eta=2log2 alpha-Lambda10-bar Lambda01.
Candidate formula:
 h_omega,b(z)=Re ell_omega(pi_-3 delta_V eD)=-U_b(z)/(4pi),
 q_F(z)=-(h(z)-h(infinity))/c_pi.
Infinity here is the existing finite LIMIT, not automatically a rational
tangential-motive fiber. Pi_-3 uses the declared split Tate lift inside
W_-2, not an unmarked projection.

## Scope and validation queue

At algebraic b,z this would be an actual rational realization with a
canonical REAL Deligne invariant. It is not a rational morphism, rational
period comparison, integrality theorem, or BSD proof. All compact genus
directions and fixed Tate frames stay in the construction.
Potential faults to audit: path-module length exactness, rational MHS
splitting by u, smooth-log F¹ claim, exact Deligne indices/constants,
real-split H sign, and 2pi/Tate normalization. No assertion is promoted
before independent review.

Primary sources (read exact versions):
- Hain https://arxiv.org/pdf/math/0109204v2, 45pages, §§2,9,13.
- Looijenga https://arxiv.org/pdf/2403.03748v2, 13pages, Th1.1 and structural maps.
- Burgos Gil–Goswami–Pearlstein https://arxiv.org/pdf/2410.17167v3,
  67pages, §2.1 Deligne formula and §2.3 delta.
- DRS https://web.mat.upc.edu/victor.rotger/docs/DRS1.pdf uses a different
  ordering convention; optional supporting comparison only.

## Live companion handoff at recovery

Higher completed marked-rational-boundary-lift-attack.md, proof hash
0da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2.
Exact obstruction is -j_B(epsilon0 tensor beta2,0); right-cup trace
of degree3 j_B is -388, hence trace of obstruction +388 chi.
New toric corrections are {u,a_ij}, old cusp residues1, new residue
u(s)^(-ord_s a_ij), finite normzero. Tate/PLUS projection of actual
point×K2 products vanishes; geometric MINUS rank3 part remains.
Root should read/review this independently while higher reviews framing.

Odd running asymmetric CM: unused pi transfer factor(p-1)p^(m-1-n),
zero modp^k for m>=n+k+1; direct bar-ray source avoids that factor.
Norm w_(m+1)(R)=w_m([barpi]R); local formal inverse selector gives a
candidate genuine norm-compatible unit family. Global comparison open.

Uniform running cofactor lift: primitive actual Heegner class gives
divisible rank3 Selmer, integral lifts of fixed A,B; nonprimitive class
orderp^s in modp^k gives defect annihilator p^(k-s) by Kim plus branch.
Cubic actual local coefficient is under H0/descent audit; do not promote
candidate -a_j^+(eta_i)G_ij without resolving that local kernel.

Goal verified active after recovery, no budget. No root process or old
numerical test running. Ledger23/manifest223 artifacts is historical.

## Full candidate and reciprocal review dispatched

The complete seven-section root proof is saved, mathematical SHA256
8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210.
The higher_period_integrality handle is independently reviewing it in
review-poisson-hodge-framing.md. Root directly checked Hain's logarithmic
bar filtration, Looijenga truncation/multiplication and the exact Deligne
formula in BGG-P; PDF screenshots failed, but parsed equations and
surrounding text were read. No formula sign was inferred from screenshot
absence. Await the actual review before promotion.

Root independently reviewed all nine sections of the marked boundary
proof and saved review-marked-rational-boundary-lift.md with PASS at
the exact0da2757a... mathematical revision. Actual rational obstruction
vanishing remains open. Uniform completed its cofactor draft333de169...
and is now auditing odd's CM construction. Odd will audit the cofactor
after saving its CM draft. All existing handles remain Astra/xhigh.

## Prospective next step, not part of the current theorem

An explicit motivic cofiber may realize the already defined V without
assuming a motivic t-structure or realization faithfulness. This idea is
NOT YET A PROVED/REVIEWED CONSTRUCTION and must not enter the report as such.
Let I_Y=Fib(M(Y)->1) in rational motives, H_mot=I_Y[-1]. The augmentation
map is geometric and I_Y is independent of a section; every chosen point
splits M(Y) and identifies its reduced quotient with I_Y. H_mot realizes
H1(Y) in degree0. The map pi followed by the elliptic h1 projector gives
H_mot->H_E,mot; u gives H_mot->I_Gm[-1]=Q(1).
Thus the ORDERED lambda has an actual candidate motivic version.

For b!=z put R_bz=M(Y²,{b}xY union Delta union Yx{z}), defined either
by the relative motive or by the total cofiber of the actual diagram
of three curves and their three pairwise intersection points. Set
P2_mot=R_bz[-2]. The ordered exterior product of I_Y with itself maps
to R_bz, hence H_mot tensor²->P2_mot. Define
V_mot=Cofib[H_mot tensor² -> P2_mot direct-sum H_E,mot(1)],
with second component -lambda. If the geometric comparison is checked,
Betti realization is the exact pushout V in degree0 by free pi1(Y).
This would be an ACTUAL motive realizing V even without a motivic
identification of the kernel or a cohomological t-structure.

Checks still required: establish the diagram/relative motive functoriality
with actual enhancement; fix the tensor-shift Koszul sign against ds^dt;
construct its augmentation/top map by the geometric truncation boundary
with the exact endpoint sign and compatible nullhomotopy on the product;
retain the separate Q line at b=z; prove all realizations and finite-base
descent. A source for the MHS truncation alone is not automatically a
proof of the motivic enhancement. Even success would construct a SOURCE
motive, not rationality of delta or an arithmetic BSD class.
