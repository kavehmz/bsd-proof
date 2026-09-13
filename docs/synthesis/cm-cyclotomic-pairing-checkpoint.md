# CM theta units paired with cyclotomic p-units: checkpoint

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own only cm-cyclotomic-pairing-attack.md and this checkpoint.
Parent objective remains full BSD over Q. No new agents or old certificates.
Status: bounded construction completed; all nine proof sections passed
[independent review](review-cm-cyclotomic-pairing.md).

## Completed bounded construction

This task constructed a specified polarized secondary operation on
the actual theta units and the cyclotomic p-unit 1−ζ_(p^r), retaining
the p-unit divisor, both norm laws, cohomological degree, Tate
coefficients and the exact tower covariance. Its comparison with
the known derivative was tested using the proved order-two ray
involution τ described below.

The actual local reference C_v remains distinct from the unproved
H_global/2 local identification. Coefficient-one integral Kummer
differences and every Kato smoothing/Betti/Euler/period constant
are preserved. The rational framed comparison remains open, with
rationality as a conclusion.

## Completed deductions

Full proofs are saved in cm-cyclotomic-pairing-attack.md §§1–9.
All new propositions passed independent review with the
integral-symbol and chosen-lattice clarification recorded below.

The positive operation is the EXACT four-term determinant difference
of four actual mixed-extension translates in coefficient-one corners
E11 and E22. It equals log_v(U_r)log_v(v_r), with no factor2/4 and
without identifying the actual local reference C_v with H_global/2.
The finite arithmetic model of v_r has p inverted; its explicit
boundary remains ord_w(v_r)=e(w/p)/φ_r.

The ray degree/norm proof is complete for everyr≥1, using the
residue-unit ray groups (global units inject modulof) and the
cyclotomic polynomial. Exact formulas:
Norm U_(r+1)=U_r, Norm v_(r+1)=v_r^p, degreep²;
Norm_F_r/K v_r=p^(D_r/φ_r), Norm U_r∈μ4;
w_r=v_r^φ_r/p is a unit with Normw_(r+1)=w_r^(p²).
The explicit rational centering subtracts[p]/φ_r. It leaves the
polarized period unchanged because the mean theta log iszero,
but it is not division permitted in finite p-power coefficients.
The finite cup satisfies φ_r cup(U,v)=cup(U,w)+cup(U,p).

The averaged pairing satisfies P_(r+1)=p^(-3)P_r+Cov_r.
The exact covariance is a fiberwise product of deviations from
means p^(-2)logU_r and p^(-1)logv_r. Renormalizing byp^(3(r−1))
leaves incrementsp^(3r)Cov_r; no summability is claimed. The
two-input cohomological norm law also has explicit cross-conjugate
cup terms, not just a product of two norms.

The CM-character argument was simplified and proved with an
order-two ray involution τ, not an unspecified Frobenius lift:
a_r≡1 modf, a_r≡−1 modp^r. It fixes K and every cyclotomic
level, and Kato15.8 reciprocity gives both Tate characters−1.
It is NOT complex conjugation. Thusv_r isτ-even, and the raw
polarized operation annihilates e^-=(1−τ)/2 of the actual theta
unit module. The normalized Kato class and d_m annihilatee^+
and equal their value on e^-U. These projectors are integral forp≥5.
No nonvanishing assumption on d_m or Sha is made. Any linear
recovery solely through the unweighted periods would force d_m(U)=0.

The corrected dual Kummer companion usesρ'=Psi^(-1), giving
B_m=T_barpi E/p^m. Its separately traced class is EXACTLY ZERO:
τ fixesv_r and acts−1 on the coefficient, so corestriction is its
negative and2 is invertible. Cup-then-corestriction differs from
pairing the separately corestricted classes. Its projection formula
to C_r factors through Norm_F_r/C_r U and kills the theta odd
component AFTER that corestriction. The untraced cup over F_r
is not asserted zero. The cup stays in H², with
the finite Tate-vector insertion recorded explicitly. At the
rational motivic level its type is Ext²(k(−1),k(1)), not H¹(V).

The old coefficient-one integral difference model, smoothing divisor
12(a²−Psi^c(a)sigma_a), gamma_CM=2pr_rho gamma_E^+, g_p,
the plus cochain correctiond_m=D+c_gamma gv, and all factors in
the final frame remain unchanged. A single rational element with
those p-adic frames and real regulatorell_E/(2Omega_E) is still
GAP CM-CycPair in§8. A replacement must have the demonstrated
CM-odd covariance and retain the p-boundary; scalar renormalization
of the even operation cannot repair it.

Primary checks: Rubin author text I§4, II§4, VI§§2–3/5.3 and
AppendixB§5; Schmitt's exact distributions; Kato2004§15.8 in
the existing full primary PDF/extraction. No old scripts ran,
no source download was restarted and no agent was created.
The independent review checked the ray involution/CM sign,
field-degree covariance, boundary and finite dual-pair scopes.
There is no outstanding source or mathematical-review repair.

## Review clarification: integral symbol before finite coefficients

The arithmetic cup starts with the canonical integral symbol
{U_r,v_r} in H_M²(F_r,Z(2)). Its rationalization has Q-coefficients,
whereas its reduction/cycle class gives the finite cup in(15).
No reduction of a bare Q-coefficient motivic class is claimed.
Likewise the finite pullback in§7 uses the chosen integral CM/Tate
realization lattice of k(−1) before reduction. All formulas remain
unchanged. The Kato primary cache paths sent to the reviewer are
/tmp/cm-derived-kato2004.pdf and /tmp/cm-derived-kato2004.txt.

The reviewed mathematical proof revision is
3a22ad8a684e9b9e9431bef0de721c391878aa406489a8574cfd5dd708581262;
subsequent PASS links and completed checkpoint edits are editorial.

The next mathematical target remains GAP CM-CycPair in §8:
an arithmetic secondary comparison with the demonstrated CM-odd
covariance and the full p-boundary, producing the exact finite
derivative and one rational framed element with real regulator
ell_E/(2Omega_E). No further bounded task has been dispatched here.
Do not resume the completed source checks, the superseded generic
character candidate, or the tested even pairing as unfinished work.
