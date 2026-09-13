# Restart: the arithmetic Poisson and Hodge-height construction

Date: 2026-09-12. Owner: root/coordinator. Bounded construction COMPLETE.
[Proof](theta-doubling-arithmetic-attack.md),
[independent PASS](review-theta-doubling-arithmetic.md), including its §7
additional audit of proof §§5–8 after the Poisson-sign correction.
Full BSD over Q remains active and unresolved. No root process is live;
no old numerical certificate was rerun in this construction.

## Completed results

Keep N=389, the original F=y² f conjugate(g),
g=(2pi i)^(-1)dlog(N^(-6)Delta(z)/Delta(Nz))/dz, F_R=ReF,
and M=int F j2 dmu !=0 from the preceding weighted-adjoint proof.

1. The ACTUAL nonzero I_L(F) is orthogonal to every holomorphic
   weight3/2 cusp form. This uses the fixed-z zero lift proved inside
   Alfes1209.5197v2, Theorem5.1's k=0 proof, pp24–25, plus a joint
   Fubini bound. Du2412.00688v1's arithmetic inner-product theorem
   has holomorphic cusp input and cannot be applied to this input by
   replacing it with its zero holomorphic cusp projection.
2. Bost's §§5.1–5.3 apply to integral normal projective arithmetic
   SCHEMES. Use C=X1(5N), degree d=12(N-1)=4656 over X0(N),
   with a normal projective arithmetic model. A_F=(0,2h*F_R) is an
   actual W1,2 arithmetic class. Its normalized coefficientwise theta
   intersections equal I_L(F_R); its self-intersection is negative
   Dirichlet energy. Vertical choices do not affect these pure-metric
   pairings. No convergence of an entire series in arithmetic Chow is
   asserted. The earlier withdrawal of a SMOOTH GS class remains valid.
3. Scalar j1 and j2 have infinite energy after subtracting any finite
   divisor logarithms: their y log y and y log²y terms survive. This
   excludes scalar Bost Green representatives, not the separate mixed
   relative graph-current construction.
4. Lemma5.1 proves uniformly for v>=1 that
   int_Y |theta(tau,z)+e0/(2pi)| dmu <= C v^(-1/2).
   Poisson summation in the actual a-coordinate has zero (m,c) term
   and tail C(y/sqrtv)^3 exp(-cy²/v). Thus bounded mean-zero inputs
   have theta transform O(v^(-1/2)). The prior weighted adjoint extends
   by exact-mean cutoffs and dominated convergence to 0<Re(s)<1.
5. The unique hyperbolic-mean-zero Poisson solution
   ddc q_F=F_R dmu is bounded W1,2, smooth on Y. A local potential
   at a cusp, with alpha0=a(q)dq, beta0=(b_-1/q+b_hol)dq and
   A'=a, B'=b_hol, A(0)=B(0)=0, is
   pi Re(bar(b_-1) A log|q|² + A bar B).
   It has no Dirac term. Subtracting these local potentials leaves
   a smooth compact Poisson problem. Fricke and conjugation preserve
   the normalized solution, giving a common cusp constant q_c.
6. The CORRECT sign is ddc J_s=+s(s-1)J_s dmu/(4pi), hence
   int q_F J_s=+4pi M_F(s)/[s(s-1)], and
   P_F(s)=<I_L(q_F),Ecal_L(bar s)>=-4sqrtN xi(s)M_F(s)/pi.
   Since M_F(1+t)=M t²+O(t³), P_F has no pole at1. Independently,
   I_L(1)=-volY e0/(2pi)+sqrtN e0/(pi sqrtv)+rapid,
   so the remaining q_c tail would give residue
   -4a_N(1)q_c sqrtN/pi, with a_N(1)=-(N²-1)/24 !=0.
   Therefore q_c=0, and q_F itself is rapidly decreasing.
7. Put H_F^G=I_L(q_F) and use the ORIGINAL source Hodge-height series
   R_omega=(Ecal'_L(1)-N logN Ecal_L(1)/(N-1))/(N-1).
   The exact ORDINARY convergent Petersson identities are

       <H_F^G,Ecal_L(1)>=0,
       M=-pi/(4sqrtN)<H_F^G,Ecal'_L(1)>
        =-pi(N-1)/(4sqrtN)<H_F^G,R_omega>.

   A_q=(0,2h*q_F) is also an actual Bost arithmetic class, and its
   normalized coefficientwise theta heights give H_F^G. The ordinary
   A_q/Hodge intersection is nevertheless int q_F dmu/(4pi)=0.
   The displayed Petersson operation is a substantive operation on
   two arithmetic height series, not their ordinary intersection.

## Corrections and scope that must survive compaction

The reviewer caught the original negative sign for ddc J_s. Every
affected formula was corrected and inspected. The earlier weighted
adjoint r_N=-sqrtN s(s-1)xi(s)/pi² and its direct second-derivative
formula were NOT changed. Reviewed corrected mathematical proof hash:
5e92a0d20118c9486dadea5f9439a40e79c4cdd38bc679d1926bcb346b0d462d.
The final proof's status/review-link updates are editorial.

The proposed genus-two diagonal product and pointwise hyperbolic Green
kernel identity were BYPASSED. They are unused and unproved. Du's smooth
volume form in §3.3 is arbitrary and is not silently the hyperbolic one.
No two arbitrary vertically extended finite arithmetic factors are
identified with a pullback of the source height pairing. Source R_omega
and the pure-metric pairing on C have their separately proved meanings.

Primary source versions and calculations are in the proof/review.
Bost1999 source: https://www.numdam.org/article/ASENS_1999_4_32_2_241_0.pdf
The review inspected printed p274's factor1/2 in the arithmetic pairing.
The review also independently recomputed the two-cusp theta tail and
checked q_c=0 directly from the source Eisenstein residue.

## Exact next target

The real Poisson metric and arithmetic height series do not yet supply
a rational regulator map to D_pt tensor Q beta2 tensor Q(1)^(-2).
Its required coefficient6N(N-1)n_E must be a conclusion, never an input.
The latest [relative graph proof](radial-graph-correction-attack.md)
constructs the actual nonzero real class C_j2 in H_D³(X×E,B,R2).
The [beta2 boundary proof](relative-beta2-boundary-attack.md) puts a
nonzero rational K2 boundary in the same relative group with its exact
period. Their comparison still lacks the point-height determinant.
Read the current [next plan](next-research-plan.md) before a new task;
do not redo the completed analytic adjoint, Bost class, or cusp estimates.
