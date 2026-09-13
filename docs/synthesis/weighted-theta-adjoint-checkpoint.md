# Restart: the actual weighted theta adjoint

Date: 2026-09-12. Owner: root/coordinator. Bounded construction COMPLETE.
All six sections of [the proof](weighted-theta-adjoint-attack.md) passed
[separate review](review-weighted-theta-adjoint.md) by odd, Astra/xhigh.
Full universal BSD remains active and unresolved. No root process is running.

## Completed analytic operation

The actual Du–Yang1702.07917v2 kernel now gives a proved adjoint on the
required Eisenstein family, tested against mean-zero rapid scalar functions:

    <I_L(h),Ecal_L(bar s)> = r_N(s) int h J_N^+(s),
    r_N(s)=-sqrtN/pi² · s(s-1)xi(s),       N=389.

Petersson pairing is linear in its first entry. The bar-s in the second
entry makes the parameter holomorphic after complex conjugation.
J_N^+ is the Fricke-even part of the fixed source; it can be replaced
by J_N for the actual even F. This is an adjoint as a functional on
mean-zero rapid functions, equivalently modulo constants on Y.
It is not an inverse on all functions or every spectral component.

Proof mechanism: first subtract the zero-vector term using exact mean zero.
The positive majorant and splitting height at v^(1/3) make I_L(h) rapidly
decreasing in tau. Its ordinary Petersson pairing with the Eisenstein family
then converges. Unfolding selects the actual isotropic lattice vectors.
Their two primitive cusp orbits and signed integer multiples give
2zeta(s)N^(s/2)(E_infinity+E_zero). The Gaussian polynomial's Mellin
integral contributes (s-1)/(2pi). The raw Du–Yang Eisenstein has leading
coefficient TWO; the full-stabilizer seed series has leading ONE.
The source's signed primitive-row/Poisson calculation and degree constant
independently confirm that factor. It is not a guessed stack factor.

Absolute summation and Mellin interchange hold first for Re(s)>1;
Petersson unfolding is done for Re(s)>2. Continue meromorphically ONLY
after these steps. At s=1, integrating individual isotropic terms first
would give zero while missing the zeta pole: that interchange is invalid.
The pointwise opposite theta integral diverges before mean-zero pairing;
no unregularized pointwise interchange is asserted.

## Exact original mass and new arithmetic interface

Because r_N(1)=-sqrtN/pi² and all lower F pairings vanish,

    M=-pi²/(2sqrtN) <I_L(F),Ecal_L''(1)> !=0,
    <I_L(F),Ecal_L''(1)>=3N^(3/2)(N-1) ell L(E,2)/pi^5.

Thus the ACTUAL lift I_L(F) is nonzero even though the entire theta POINT
projection on E389 is zero. The forward j2 lift contains a THIRD derivative
through the xi pole; this weighted adjoint cancels that pole via s-1 and
uses the SECOND derivative. Keep the two operations distinct. The source
unit is explicitly N^(-6)Delta(z)/Delta(Nz), not Du–Yang's generalizedDelta_N.

The earlier arithmetic realization of I_L(F) is ONLY the limit of actual
smooth cutoff metric pairings. ReF is not algebraically cusp-smooth.
Do not restore a single smooth class a(2ReF), set int ReF mu_GS to zero,
or infer a limit in an arithmetic Chow group. The arithmetic beta2 line
already extends over the model; its integral multiple is not a unit.

WTA-389 now asks for an actual rational arithmetic second-derivative test
and Kummer forcing operation in D_pt tensor Q beta2 tensor Q(1)^(-2),
with real evaluation M and coefficient6N(N-1)n_E as a conclusion.
The ANALYTIC adjoint is completed; do not repeat it as a fresh target.
The secondary-Kummer note supplies an actual higher-Chow operation giving
the source unit, a compact graph-unit cycle and its current contraction,
but also an explicit nonzero ddc obstruction to naive j2 weighting.

## Review and computation snapshot

Odd reviewed this proof PASS; root's reviewed mathematical hash was
b15efe3c4ac397b857b35db03e6cc992f23f537a191828fe1b233ead39d80959.
Subsequent completion links are editorial. Current hashes belong in the
root checkpoint manifest, which also records the other round results.

Root independently reproduced the NEW CM p-adic certificate in exec
session48501, now TERMINAL with exit0. The pure integer audit of every
stored row also passed: level3 bins100,A3540,B-275,alpha13mod25,c2=20;
level4 bins500,A46545,B86450,alpha113mod125,c2=70. The later carry addition
was independently recomputed from those rows: A2=-5,C237,terms5 and15mod25.
Script/data hashes matched. No root exec session remains and no old
numerical certificate suite was rerun.

Root's full CM proof/certificate review is saved PASS. Uniform's separate
integral local-unit, coefficient-sequence and Smith/Cassels audit is also PASS.
Higher's secondary construction and uniform's tame construction have their
separate PASS reviews. Revalidate live agent handles and shared state before
any next task; this is a snapshot, not evidence of ongoing execution.
