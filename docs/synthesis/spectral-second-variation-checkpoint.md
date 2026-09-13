# Second character variation restart checkpoint

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
Own only spectral-second-variation-attack.md and this checkpoint for the
new bounded task. Earlier Mellin note has passed independent review and
its editorial completion status has been updated.

Parent objective remains full BSD over Q. No previous numerical certificate
is to be rerun. No new agents are required.

Known inputs: actual integral character k(γ)=Re∫γπ*ω/ω1, cusp-parabolic
trivial, with rank3 local system ρ_T=(1+T)^k modT³. Its diagonal first
scattering-response integrals vanish from the factor L(f,1). Asymmetric
spectral derivatives were not tested; the second character variation is
now derived in this task's saved proof.
The full-curve second SPECTRAL jet already has exact integral ell·L(f,2)
with complete scalar −9N/[π⁴(N+1)]. It is not an arithmetic class yet.

The completed calculation conjugates Δ by exp(2πi εF), where
w=Re(π*ω)/ω1 and F is a local primitive. It proves the positive operator
Δ−4πi ε⟨d,w⟩+4π²ε²|w|² and the first/second inhomogeneous Eisenstein
equations and Green-identity scattering formula. Incoming cusp phases
are retained. The standard lifts have F∞=F0=0 because the winding
period is zero; arbitrary primitive/basepoint gauges retain the displayed
phase corrections.

## Complete derivation independently reviewed PASS

Full proof now saved in spectral-second-variation-attack.md §§1–7.
Root's complete PASS review is saved in review-spectral-second-variation.md.
It reconstructed the operator, boundary sign, T conversion, finite-part
expansion and four rational U values, and checked source/Poincaré–Lelong
scope and orbifold conventions. Applied the missing backslash in (4.1)
and added the coarse-divisor/orbifold-uniformizer multiplicity sentence in
§6. Literal file inspection confirmed both occurrences are correctly u_2,
not nu_2; no corresponding edit was needed.
Reviewed mathematical revision after these requested clarifications:
cdcb7128079cf50a2022b3a375d000175ce135dba55bbf1021692ceeeec3dadd.
Subsequent header and checkpoint updates are editorial.

- Gauge D_ε,b=e^(2πi ε(F_b−F(z)))E_ε,b has incoming coefficientδ_ab.
  Its scattering coefficient is e^(2πi ε(F_b−F_a)) times the original.
  Both cusp phases are zero for the standard389 lifts fromL(f,1)=0.
- Positive operator derivatives L1=−4πiD_w, L2=8π²|w|². Actual
  Ddot=−R(s)L1E, Dddot=2R L1R L1E−R L2E.
- Green boundary identity gives Φddot_ab=8π²/(2s−1)[4∫D_wE_a R D_wE_b
  −∫|w|²E_aE_b]. Full singular and finite Laurent parts are explicit
  in(4.2), including reduced-Green term and all KLF constants.
- Leading doublepole coefficient=−8π²||w||²/Vol². For integralT²
  coefficient, divide by−8π² since first scattering derivativezero.
- Two integral f-Betti directions have Hodge Gram
  diag(40b/ω1,40ω1/b), determinant1600. This is not the specified
  point-height matrix H, whose offdiagonal is certifiedpositive and
  determinant<27/100. Only that literal frame identification is disproved.
- Positive same-resolvent point construction: V*=P−Q=(1,0),
  W*=V*+P=(−3/4,−15/8), D1'=W*−V*,D2'=P−V*.
  u1=(x+3/4)/(y+x/2−1/2),u2=(x+1)/(y−x+1) satisfydivu=D'−D.
  Their support is disjoint from Zj andO, as checked by exact h_j values.
  u_i(Z_j)=[[11337/596372,−3599/9025],[−405/1652,6/25]].
  Thus H_ij=−(2π/40)<δπ*Zj,G δπ*Di'>−log|u_i(Zj)|.
  All point sources nowavoidcusps; G is the SAME meanzero Δ^-1 used
  in the scattering finite part, extended tologarithmic pointpotentials.
  The new rational logs retain the principal finite-place correction.
- First missing comparison: smooth spectral sources D_wA_a versus
  nonzero pointdelta sources cannot be literallyequal. Adjoining both
  potentials constructs an analytic block but not an arithmetic relation
  equating its spectral and pointdeterminant evaluations.

Primary source checked: Petridis–Risager1703.09526v3 Cor4.5, Lem5.1,
Thms5.2–5.4 and6.3 support exactrecurrence/meromorphic continuation,
boundaryphaseconversion andsecondmomentpole; signs are derived directly
forourpositiveΔ. Pointheightnormalizationusespreviousreviewedrelativecycle.
New calculations were exact rational substitutions at V*,W*,R,S,T,
not reruns of earlier numerical certificates. One initial scratch table
omitted the factor1/3 in h2's yterm; it was corrected before any proof
or stated rational evaluations were saved. Saved formulas use the correcth2.

Next mathematical action is SV-389: construct the actual rational mixed
comparison retaining every cusp phase, finite correction and arithmetic
normalization. The Hessian, finite part and point-source formula are
completed reviewed dependencies; do not repeat their audit as new research.
