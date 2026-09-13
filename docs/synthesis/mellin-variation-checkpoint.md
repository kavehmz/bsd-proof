# Mellin variation restart checkpoint

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
Own only `mellin-variation-attack.md` and this checkpoint.

Parent objective remains full BSD over Q. The subagent goal tool is null;
the parent owns the active goal. No old certificates are to be rerun.

The preceding relative-modular construction gives an actual rank-six
noncuspidal 1-motive with height matrix H and an integral determinant
frame mapping to Omega_full det(H). Its ordinary projected cusp-path
and tensor-square comparisons failed in explicitly stated senses.

The reviewed construction retains the full modular curve by pairing the newform f
with a holomorphic weight-two Eisenstein form and the nonholomorphic
cusp Eisenstein family E_infinity(z,u). Unfolding turns its second
spectral jet at u=1 into L''(f,1) times L(f,2), with every bad-prime,
gamma and scattering factor retained. This produces an actual automorphic
integral and tests whether a Gauss–Manin/Eisenstein extension can remove
the extra regulator factor. The exact formula is now independently reviewed.

It uses g(z)=E2(z)-N E2(Nz), N=389, with nonconstant coefficients
-24(sigma1(m)-N sigma1(m/N)). The complete local Euler factor at N and
the Laurent-jet equations, pole, and constants at both cusps are derived.
The analytic complex has been compared with the rational modular-unit
differential and the noncuspidal regulator frame. No identification of its
spectral derivatives with algebraic Gauss–Manin sections is proved.

## Exact construction independently reviewed PASS

Full derivations are saved in mellin-variation-attack.md §§1–8, with
PASS in review-mellin-variation.md. The review checked proof revision
14e70782bb5ccaca0945f096e89e3bb53d8430baa1db757f914cdf395374ba69;
later header/checkpoint updates are editorial.

1. For s=1+t, E∞=R/t+A0+tA1+t²A2, R=3/[π(N+1)]. Its two-cusp
   scattering matrix is ψ(s)/(N^(2s)−1) times
   [[N−1,N^s−N^(1−s)],[N^s−N^(1−s),N−1]]. Both width-one scalings,
   all c_a,d_a,e_a constants and log³ cusp terms are retained.
2. Exact unfolding:
   I(s)=−24Γ(s+1)/(4π)^(s+1) · L(f,s+1)L(f,s)/[ζ(2s)(1+N^(−s))].
   The factor at389 is derived from a_389=1 and c_(389^r)=1.
   Thus ∫F A2=−9N/[π⁴(N+1)] L(f,2) ell, nonzero, while ∫F,
   ∫F A0,∫F A1 vanish. The target ell is exactly4π(J''−C).
3. Actual relative top-degree ORBIFOLD form A2 Fdμ on the Borel–Serre
   compactification extends by zero at its two boundary circles. The
   effective Γ1(389) cover has degree194; using its integral fundamental
   class requires dividing the pulled-back integral by194. The spectral chain is
   ΔA0=−R, ΔA1=−A0−R, ΔA2=−A1−A0, hence Δ³A2=−R, Δ⁴A2=0.
   It defines a cycle R+tA0+t²A1+t³A2 in the two-term analytic complex
   Δ+t+t² modt⁴, with specified nonzero cusp boundary. No algebraic
   connection or rational lattice is inferred. The nonsemisimple Casimir
   blocks a literal homogeneous finite Gauss–Manin tensor realization,
   not all mixed variations/regulator identities. Universal H=R¹π*Z
   uses the full Γ0(N) stack group, with−I acting−1; only even symmetric
   powers descend to the effective orbifold. These two scope repairs were
   requested by the independent reviewer and applied before PASS.
4. Exact finite parts: E+ finitepart=K_N−12U/[π(N+1)] with all γ,ζ'/ζ,
   logN constants; E−(1)=log|v|/[2π(N−1)]. F is Fricke even, so its
   pairing with E− and every spectral derivative is zero.
5. Actual secondary-symbol repair κ_j={v,π*h_j} uses the prior explicit
   noncuspidal moving functions. Normπv=c is constant from cusp collapse;
   πW=[−1]π and W*v=v^-1 give c²=1. Projection formula gives transfer
   {c,h_j}, killed by2. Tame symbols commute with transfer; cusp tame
   values are1 since h_j(O)=1. No arithmetic unramified symbol claimed.
6. An actual integral rank3 local system is ρ_T(γ)=(1+T)^k(γ) modT³,
   k=Re∫π*ω/ω1 integral and cusp-parabolic trivial. Its unipotent monodromy
   is not claimed finite. Its character Eisenstein
   series is explicit. The precisely defined first-response integrals
   B_ab(s)=∫E_a(s) dotΔ E_b(s) retain L(f,1), so their spectral jets
   vanish. This does not assert the full scattering-matrix derivative
   without its boundary correction, nor the full
   character jet or its second character variation vanishes.

Source checks: Petridis Duke103(2000) §§2,4.3 for exact Eisenstein/scattering
normalization and first-response integrals; the full level-one Fourier
coefficient is derived by Poisson summation with factor4 in the positive
cosine sum. KLZ1501.03289v2 Thm6.2.9 is a cuspidal
tensor-product first-derivative theorem, not this second spectral jet;
Milnor norm projection/residue compatibilities in EKM §100 Fact100.8.
No old certificates rerun and no new agents spawned.

The exact scalar, Laurent coefficients, relative orbifold boundary model,
and norm/projection calculation passed independent review. The remaining
MV-389 comparison must identify this analytic second spectral jet with the
actual noncuspidal determinant times an L(f,2) regulator factor, not cancel
the latter as an assumed integral unit. A further constructive direction is
the SECOND character variation coupled to the point 1-motive; first
scattering response (7.3) is already tested and vanishes. Its vanishing
is diagonal in the two Eisenstein spectral parameters; it does not assert
that asymmetric parameter differentiation vanishes.

Next construction is now assigned in separate files
spectral-second-variation-attack.md and spectral-second-variation-checkpoint.md:
derive the second character variation, retain its cusp-boundary corrections,
and test a comparison to the actual point-height determinant. This completed
note is a dependency, not a pending-review task.
