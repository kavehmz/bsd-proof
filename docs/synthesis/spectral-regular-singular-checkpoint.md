# Spectral cusp jets versus finite regular-singular periods

Date: 2026-09-12. Owner `/root/higher_period_integrality`, GPT-6 Astra/xhigh.
Own spectral-regular-singular-attack.md and this checkpoint. Parent objective
remains full BSD over Q. No old numerical certificates are to be rerun.

Assigned task: compute exact cusp Fourier coefficients of the first two
spectral jets A1,A2 of E_infinity at s=1, then test a precisely stated
finite regular-singular period-expression class. Allow rational operations
on period matrices, inverse powers of log|q| and logs of Hodge norms.
Any exclusion must remain about literal functions in that specified class,
not all motives with the same integrated scalar or arbitrary metrics.

Historical starting calculation, now proved and reviewed: put
z=4πny and R(t,z)=K_(1/2+t)(z/2)/K_(1/2)(z/2). Its first order
derivative is e^z E1(z); its second is
2∫_z^∞ e^u E1(u)du/u. Their inverse-z asymptotic coefficients are
(-1)^(k-1)(k-1)! and twice these divided byk. Thus the first Fourier
mode of A2 retains a divergent factorial sector even after adding
a constant multiple of A1. The exact function-class exclusion and its
limited scope are now proved and independently reviewed.

## Complete proofs independently reviewed PASS

Full proof is saved in spectral-regular-singular-attack.md §§1–7.
The PASS review is review-spectral-regular-singular.md. It checked
mathematical revision48aff42380152a3c965ed62889fca23ce05bc5c0bf7e7a3a163698e03cc3e097
after both exponent-support and uniform-denominator repairs. Subsequent
header/checkpoint changes are editorial.

- Exact nonzero Fourier coefficients at BOTH cusps are (2.2)–(2.3),
  derived from the two level-one oldforms. First-mode h0 is
  −6/[π(N²−1)] at∞ and6N/[π(N²−1)] at0. h1,h2 retain logN and
  completed-zeta derivatives. The old zero-mode scattering constants
  and Laurent pole subtraction are retained in(2.6).
- Bessel ratio K_(1/2+t)(Z/2)/K_(1/2)(Z/2) has an exact gamma-integral.
  Its first derivative is J=e^ZE1(Z), and second is2H with
  H=∫_Z∞J(u)du/u. The latter is proved from the normalized differential
  equation and decay at∞, not formal differentiation of an asymptotic series.
- Finite geometric expansion gives exact bounds M!/Z^(M+1) for J,
  M!/[(M+1)Z^(M+1)] for H. The A2 first-mode coefficients are
  (−1)^(k−1)(k−1)![h1+h0/k], so have zero convergence radius even
  after adding any constant cA1+dA0. This holds at both cusps.
- Defined explicit coefficient field L=union_e C({z^(1/e)})(logz),z=1/y.
  Proved: a member with a full pure-integer-power asymptotic series
  must have a convergent such series. Proof compares coefficients
  rational inlogz, then uses P=QA coefficientwise to force a meromorphicgerm.
- Defined a normally convergent exponential-sector class with uniform
  tail bounds and coefficients in L; proved the actual A1,A2 cannotbelong.
  Reviewer corrected the exponent support condition: a+b is bounded
  below, not a and b separately, since permitted rational inverses such
  as1/(q+barq²) have unbounded individual negative exponents. Finiteness
  at each total order and uniform tail bounds remain; the first Fourier
  sector proof is unchanged.
  A second reviewer precision is applied: every leading denominator in
  the period-operation chart must have a uniform power/log lower bound
  on the full angular strip. Merely being a nonzero polynomial is not
  enough. The canonical biextension inclusion already proves this by
  removing the real e^(xN) factor and using pivot functions of y alone.
- Proved closure for finite rational period/conjugate-period operations
  under explicit nonzero nilpotent-orbit denominator charts, and allowed
  positive Hodge-norm logs. Canonical finite biextension heights covered
  via rational Deligne gradingY and δ=(Y−barY)/(4i), plus the admissible
  local normal form. The real e^(xN) factor is removed before choosing
  nilpotent-orbit pivots, giving uniform angular bounds. Subsequent
  inversions of nonzero leading coefficients in L are also allowed,
  so rational expressions such as1/(1+logy) remain covered.
  All inversions/log hypotheses are stated; arbitrary
  arithmetic metrics and operations outside this class are not excluded.

Primary sources read: DLMF10.32.8 and10.38.7; Schmid1973 Thm4.9;
Brosnan–Pearlstein1701.05527 §2 (28),(37),(41),(48), plus the convergent
SL2-orbit expansion inThm73 as a consistency check. The exact special-
function and closure arguments are proved in the note. No old math
scripts rerun and no new agents spawned.

Lemmas5.1/6.1 and the canonical-biextension chart inclusion passed review.
The result is an exclusion of
literal cusp functions in that specified class, not a theorem about every
motive with the same integrated value. Next mathematical work remains
the actual MT-389 arithmetic comparison beyond this pointwise function
class; full BSD remains unresolved.
