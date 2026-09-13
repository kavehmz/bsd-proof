# Asymmetric CM ray: completed bounded proof, independent PASS

Date: 2026-09-13. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own cm-asymmetric-ray-attack.md and this checkpoint.
Full nine-section proof independently reviewed by /root/uniform_witness:
[PASS](review-cm-asymmetric-ray.md). No mathematical repair remains.
No further construction is pending in these completed files.
Full BSD over Q remains active; original coefficient nonvanishing
and rational descent are not claimed.

Reviewed mathematical proof SHA256 (later status/link edits are editorial):
7a9904d53c63062f29439b83b278ec28e0d6891b2aba08580268e815188804ed.
The reviewer requested only the current tame-residue scope precision:
formula(30) is an exact valuation everywhere, but its usual étale
tame interpretation excludes residue characteristicp. The formal
argument atp is kept separately. No norm or scalar changed.

## Actual fields, norms and characters

The original two-variable tau_m=Omega_infinity/(f0 p^m) and original
rho=(Psi^c)^(-1) are retained, with gamma_CM=2pr_rho(gamma_E^+),
unnormalized tame degree1152(p−1)^2, q_a, iota, u(0), Smith,
polarization, generator and Néron/CM period data unchanged.
The prime range is p≥5, p≡1mod4, p∤2·3·13, a5 excepta7 atp5.

For [pi^m]R_pi,m=R, M_m=F_m(R_pi,m) has translation groupE[pi^m]
and degreep^m overF_m. Its exact theta norm is
w_m(R)=Theta_a(beta_m+R), beta_m=Omega_infinity/(f0 barpi^m),
in B_m=K(f barpi^m). This is proved using Kato1.3 isogeny norm.

For m>r, delta=m−r, the full point-field tower norm is
Theta_a(tau_r+[barpi^delta]R_pi,r)^(p^delta).
The tower degree is p^(3delta), and its argument runs through a
whole E[p^delta] fiber. The point endomorphism is not suppressed.
The intersection M_r∩F_m=F_r follows from the nontrivial Cartan
action on the pi-Kummer translation group versus an abelian ray quotient.

B_m∩K_n=K, since the former is unramified atpi and the latter is
totally ramified there. Thus [F_m:B_m K_n]=(p−1)p^(m−1−n).
The full transfer has this factor and vanishes modp^k for m≥n+k+1.
The directly descended smaller-field class avoids that factor
integrally, but has ray covariance Z_(m+1)(R)=Z_m([barpi]R).
It is a restriction fromK in the cyclotomic labeln, so that label's
corestriction has factorp rather than1.

The exact primitive-orbit norm retains its denominator:
Theta_a([barpi^m]R+tau0)/
Theta_a([barpi^(m−1)]R+[barpi^-1]_f tau0).
AtR0 this recovers the first-prime Euler factor.

The original homothety now sends beta=sigma+t to sigma−t.
The exact odd ratio is Theta_a(R+sigma+t)/Theta_a(R+sigma−t),
with projector factor1/2. It is not a root of unity when
(p−1)p^(m−1)>24(a²−1), by the actual rational-function degree
and ray-orbit argument. This does NOT prove the full selected
rho transfer is nonzero at the fixed point.

## New coefficient and point comparison

The asymmetric full permutation class has a unique augmentation
kernel lift once its actual scalar factor kills augmentation.
For POINT jets, not1+p ray jets, the threshold is
r≥max(n+1,k+floor(log_p d)), m≥r+k.
The order-d image then vanishes over FULL A_k by the new p^(m−r)
norm power. No point linearity or old p² law is assumed.
The first point tensor has onlyPsi²; its Weil contraction iszero.

A geometric class on U_m=E minus the translated E[a] boundary
uses the ACTUAL selectedrho transfer. Its explicit residues are
(a²−1)/(a²−u_a) at−g beta and−1/(a²−u_a) at the other a-torsion
translates, timesg(t_rho). They are units modp^k, so this class has
exact orderp^k. Specialization atP,Q can still lose that nonvanishing.
Subtracting its value atO gives the unique relative class D_m,k.

The proper relative group H1(E,O;T_pi/p^k) is EXACTLYA_k, generated
by the pi projection of the universal[p^k] Kummer torsor. The
[pi^k] convention differs by the retained unitbarpi^k.
Boundary counterterms differ byc_m,k times that proper generator.
Their exact ray pullback and coefficient compatibility leave an
ACTUALZ_p torsor:
Xi_m,k=D_m,k−barpi^m(c modp^k)K_pi,k.
The inversebarpi unit acts on this actual integral coefficient line; no arbitrary
c is chosen. Cross-smoothing gives actual operators
S_b=b²−u_b[u_b]^* and S_b Phi_a=S_a Phi_b; they annihilate the
proper point line. The old Kato scalar unit is not their inverse.

## Genuine local norm system and residual scope

At the pi completion, [barpi] is an integral formal-group automorphism.
For R inE1(Qp), its UNIQUE inverse S_m(R) defines the semilocal
principal-unit family
U_m(R)=Theta_a(beta_m+S_m(R))/Theta_a(beta_m).
It is genuinely norm compatible, with no division byp. Its
same-rho Kummer transfer gives an integral class in the local
finite T_pi point lattice; nonvanishing of that class is not claimed.

For the old actual formal pointsR=n_pP,n_pQ,n_p(P+Q), n_p=8#E(Fp),
the algebraic unit values cannot lie in the global ray fieldB_m
when p^m>12(a²−1), by the full barpi point-division degree and
Theta's rational-function degree. The local family is nontrivial,
but its formal selector has no direct global-ray descent.
At the opposite p-adic placebarpi is not a formal unit.

Arithmetic evaluation boundaries remain level dependent through
[a]([barpi^m]R+tau0). No uniform global S-unit theorem or BSD
exception set is inferred. Formula(30) retains the exact valuations;
ordinary tame residues excludep, and all p-local arguments are separate.

The first remaining task is CM-Asymmetric-Point in§9: a selected
arithmetic boundary counterterm compatible with the ORIGINAL primitive
ray data and local conditions, followed by the exact old Kato/Bockstein
frame comparison. Uniform c2/index control, one rational frame with
real realizationell/(2Omega_E), bad/nonsplit primes and full BSD remain
unproved. Nothing is normalized by an afterward chosen scalar.

No prime scan, numerical period or old certificate was run. Primary
Kato1.3/1.10/15.8 and the previously reviewed local CM/Kummer formalism
were reused with their exact scopes; all new deductions are in the proof.
Next: finish the separately assigned reciprocal cofactor-lift review.
Do not expand this completed bounded construction. Its first unresolved
arithmetic comparison remains CM-Asymmetric-Point, with the scopes above.
