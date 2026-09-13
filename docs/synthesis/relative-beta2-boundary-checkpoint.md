# Relative beta2 boundary checkpoint

Date: 2026-09-12. Owner /root/higher_period_integrality, GPT-6 Astra/xhigh.
Own relative-beta2-boundary-attack.md and this checkpoint only.
Initial checkpoint was saved immediately before research/source audit.
Keep the completed radial-graph-correction proof unchanged.

Universal objective: full BSD for every elliptic curve over Q.
Bounded task: construct the actual rational beta2 boundary class for
V=X0(389) times E, B={0,infinity} times E; prove nonzero and evaluate
its logarithmic scalar with all native K2/Deligne/Tate/cone factors.

Inputs already proved/reviewed:
- div(u)=(N-1)(0-infinity), u=N^-6 Delta/Delta_N, N=389.
- beta2 is a specified rational K2(E) class with
  R_E(beta2)=integral_b eta_K=L(E,2)/pi.
- eta_K(f,g)=log|f|darg g-log|g|darg f.
- integral_E omega_E wedge eta_K=omega1 R_E,
  omega1>0 primitive real period and Omega_full=2omega1.
- The radial real relative class C_j2 and its scalar M are reviewed:
  M=-3N(N-1)ell L(E,2)/(2pi³).
- For the compact-first relative fiber cone D(c,b)=(dc,i*c-db),
  an absolute exact change whose contraction is partial b shifts
  the scalar by -sum_c ord_c(u)b(c)/(4pi c_pi).

Completed first construction:
Use the ACTUAL rational equivalence (0)-(infinity)=div(u)/(N-1)
as Chow correspondences to show the two restrictions
H_M²(V,Q2)→H_M²(E,Q2) agree. Projection from V to E supplies all
diagonal classes. Hence their cokernel is exactly H_M²(E,Q2),
and localization injects it into H_M³(V,B,Q2).
Apply to the already constructed beta2. No new K2 construction.

Normalization initially proposed and now proved/reviewed:
With the unit convention r(f)=log|f|, the native Deligne K2 form
is i eta_K. The explicit positive boundary is
partial^+ beta=(0,r(beta))=-partial_canonical beta.
A cutoff representative proves the scalar
P(partial^+(beta2,0))=(N-1)omega1 L(E,2)/(8pi³ c_pi).
Its ratio to M is then -12N c_pi ell/omega1.
This lacks the point-height determinant and is NOT a BSD formula
or a rationality theorem. The native product and every sign were
directly checked in the completed proof and independent review.

Possible future extension, not part of the completed proof:
The actual compact-support cup with the fixed unit u followed by
fiber trace Y times E→E has degrees (3,2)+(1,1)-(2,1)=(2,2).
Check whether this supplies a rational map back to K2(E) with its
boundary residue equal to ord_c(u) beta. Do not assert a new
scalar or source comparison before proving the exact map/sign.

No new agents, shared synthesis edits or old numerical reruns.
The primary inputs, full proof and independent review are saved.
A rational lift in this particular relative group is an attempted
route, not a claimed necessary condition for BSD.

## Completed five-section proof and independent review

Reviewed mathematical proof relative-beta2-boundary-attack.md SHA256:
36826737cb66f2db433c49987788d456d8bbaa10d3d772d788946338b474e265.
All [NEW] claims passed
[review-relative-beta2-boundary.md](review-relative-beta2-boundary.md),
review SHA256f9b624258255ada08b14a033482beac4e17688ea8c89482790b480575efde2ef.
Subsequent proof-header and checkpoint changes are editorial.

Actual motivic diagonal proof:
In E times V, W={(P,x,P)} is a codimension-one support.
The CH²(-,1) chain (W,u)/(N-1) has boundary
Gamma(i0)-Gamma(i_infinity).
Thus the two motive maps M(E)→M(V) agree rationally,
so the restrictions in every motivic degree agree.
p_E^* realizes EVERY diagonal. The full cokernel in degree2,
twist2 is canonically H_M²(E,Q2), by difference of its two entries.
Localization injects it into H_M³(V,B,Q2).
The chosen map j_B(beta)=partial^+(beta,0) is minus the
canonical boundary for D(c,b)=(dc,i*c-db).
Hence b2=j_B(beta2) is an actual nonzero rational motivic class,
before any real scalar calculation. No rank-one K2 theorem is used.

Native regulator derived:
For x=log|f|, the total Deligne representative is
G(x)=(partial x-barpartial x,2partial x,x).
The Beilinson product's third component on two such degree1
classes is2x partial y-y partial x+y barpartial x.
Projection to imaginary forms gives
x(partial y-barpartial y)-y(partial x-barpartial x)=i eta_K(f,g).
Thus the native degree2,twist2 K2 regulator is i eta_K,
not a guessed multiple. The unramified tame condition removes
all small-loop residues; choose a smooth closed representative.
Final sign wording precision: the eta_K loop is
2pi(nlog|a|-mlog|b|), which is MINUS the logarithm of the
fixed Rost symbol b^m/a^n. Its vanishing for unramified classes
and every native/cone/scalar formula are unchanged.

Exact positive boundary computation:
Let rho=1 near cusp0 and0 nearinfinity.
(0,i eta_K,0) is cohomologous to
(-d_D(i rho eta_K),0)=(i(d rho wedge eta_K)^(1,1),0).
Divide by the fixed degree3 form factor2pi i:
S_b2=(d rho wedge eta_K)^(1,1)/(2pi).
Its omega_E push is
-omega1 R_E(beta2)partial rho/(2pi).
With partial barpartial log|u|=-pi i sum m_c delta_c,
integral partial rho wedge barpartial log|u|=pi i(N-1).
Therefore the exact scalar is
P(b2)=(N-1)omega1 L(E,2)/(8pi³ c_pi).
The infinity class gives its negative, as does canonical
rather than explicitly positive boundary.
No singular cusp product or arbitrary pullback occurs:
the representative is smooth and vanishes near both fibers.
The final real-structure precision chooses rho conjugation-invariant
and eta anti-invariant by averaging, preserving all cusp values and
the established regulator period.

Exact residual comparison:
M/P(b2)=-12N c_pi ell/omega1=-24N c_pi ell/Omega_full.
This is NOT the BSD quotient and its rationality is unproved.
The boundary line lacks Reg_E.
Its evaluated product with Reg_E, the determinant of the point-height
matrix (without another Omega factor), is
-(N-1)/(4c_pi) times the original D_pt tensor B2 tensor Q(-2)
frame evaluation. This is explicitly only an evaluation identity;
no motivic spectral selection map is asserted.
A rational lift in this particular relative group is an attempted
route, not a necessary condition for BSD.

Primary inputs checked:
Voevodsky IAS56-page text Proposition4.1.5 and the Chow-motive
functor of Proposition2.1.4 (read directly on primary PDFpp5–6);
Levine1994 Theorem5.2/Cor5.3 for actual correspondence action;
Burgos–Goswami1712.10150v2 §§4.3–4.5 for total/concise Deligne
complexes and products; Burgos–Feliu0907.5169v1 Theorem3.5/§5
for Beilinson product compatibility.
All period and beta2 data are the already reviewed integrated proof.
No old numerical runs, shared synthesis edits or extra agents.

The optional compact cup/trace retraction in the initial plan is
NOT asserted in the saved proof; its exact motivic trace sign
has not been checked and is not needed for the bounded result.
The independent review of all five sections and the final sign
precision has been inspected. Editorial completion is finished.
Root handles shared synthesis. Preserve the radial proof unchanged.
The universal BSD objective and the point-height comparison remain open.
