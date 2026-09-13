# Actual CM derivative nonvanishing: completed checkpoint

Date: 2026-09-12. Author /root/odd_rank_bridge, GPT-6 Astra/xhigh.
Own cm-derivative-nonvanishing-attack.md and this checkpoint,
compute/scripts/certify_cm39_padic.py and
compute/data/cm39_padic_derivative_certificate.json.
Full universal BSD remains the parent objective. No new agents.

## Completed and independently reviewed

The [proof and certificate](cm-derivative-nonvanishing-attack.md) passed
the [full coordinator review](review-cm-derivative-nonvanishing.md).
A separate agent's [integral-bound audit](review-cm-derivative-integral-bound.md)
also passed, against final mathematical version
190fdbe54ca357dc2b9ec3dcf3b189da1ee23aa13447b79b5e41cf0757806128.
No mathematical correction remains pending. Subsequent completion
headers and this checkpoint are editorial only.

The actual c2 is nonzero at5, the actual w0=Sh(d_pi+d_barpi)
is nonzero, full5-primary Selmer corank is two, and Sha[5-infinity]
is ZERO for E:y²=x³+39x. The uniform bound below is conditional
on a nonzero coefficient. No nonvanishing at an uncomputed prime,
rational BSD quotient or universal BSD conclusion is proved.

## Reproducible exact coefficient certificate

The curve is the global minimal model [0,0,0,39,0],
conductor48672, label48672i1, with a5=−2 and N5=8.
The primary Cremona theorem (Appendix Theorem5.2 in
Agashe–Ribet–Stein2006) proves its optimality and Manin constant1.
Its negative discriminant gives one real component.
The eclib real scaling1/2 is explicitly retained; Ω_E is the
least positive real period and also the full Néron period.

Reproduction:
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39_padic.py

Final script SHA256:
6f21c0c8d74af6a248918c9537585da11456f24060425c1b98da5d9ef5fde27e.
Final data SHA256:
22164e5e22c37f18cd5cb12ecf3a3296a106ef6e70c4b35f62267f4ad46bb85a.

Exact level3:
A3=3540, B3=−275, alpha=13mod25,
alpha^(-3)(A3−alpha^(-1)B3)=20mod25.
Exact level4:
A4=46545, B4=86450, alpha=113mod125, coefficient70mod125.
Every required rational symbol at25,125,625 was independently
checked by eclib and Wuthrich's fixed-denominator algorithm.
Root independently reproduced the script and audited all rows/Hensel
arithmetic. Both levels have their OWN proved error bounds.

The infinite error is p^(n−1)Z_p: the measure is integral,
t(x)=log_p< x >/log_p(1+p) differs from its bin index j by
p^(n−1), and binom(t,2)−binom(j,2) has that same bound
for p≥5. Half-integrality of all unitary symbols follows from
the proved optimal Manin1 parametrization and its cusp images.
Thus c2=20mod25 and v5(c2)=1, not merely a stabilization print.

An initial implementation repeated individual numerical integrations.
It was stopped and replaced by the batch routine checking the SAME
values. All processes have completed; none remains running.
No old rank, analytic or regulator certificate was rerun.

## Actual class and the integral Sha bound

The exact reviewed height identity against the non-torsion P=(3,12)
has nonzero right side k_alpha log_omega(P)c2 T². Therefore
w0≠0 and at least one ACTUAL ray derivative is nonzero.
The reviewed corank criterion gives full corank2 and finiteSha5.
It does not identify which derivative is nonzero, prove independence,
or certify a specific Kummer reduction modulo5.

Nonanomalousness makes exp(delta0) a primitive local point:
log(exp(delta0))=k_alpha^(-1) has valuation1, while formal
logarithm identifies the local point completion with5Z5.
Integral local Tate duality therefore gives
iota5=O_p(e_L0)∈Z5^×. The actual square Selmer determinant
has quadratic coefficient valuation1.

For T,V,W=V/T the ordinary plus/minus coefficient sequences are
exact. At5 H0(W^-)=0 and formal Kummer equals the plus condition;
at bad2,3,13 nontrivial μ4 inertia kills the5-primary local
cohomology; real Tate terms vanish. The ordinary Selmer cone
therefore preserves the coefficient sequence. AFTER finiteSha5,
its long exact sequence identifies torsH2(C_f(T)) directly with
Sha5. No integral global self-duality sign is needed.

Smith-reduce the constant square matrix over Z5. The quadratic
determinant coefficient is the product of its nonzero Smith
entries times the determinant of an INTEGRAL2×2Bockstein block.
Hence v5#Sha5≤v5(c2)=1. The finite5-primary Cassels–Tate pairing
is alternating and nondegenerate, so its order is a square.
Therefore Sha5=0. This uses no finiteness premise at other primes.
Reg5 is nonzero by the corresponding rational Bockstein statement;
no numerical regulator or exact regulator valuation is claimed.

Primary inputs: Nekovář §§3.4,6.1 for exact cochains and cones;
Rubin/Milne for local duality and Kummer conditions;
MilneI§6/Theorem6.26 for alternation and divisible kernels.
The exact unit determinant, cofactor sign and Rubin derivative
are the independently reviewed predecessor constructions.

## Uniform mechanism and exact unresolved step

For EVERY good split p≥5 of E39, the already proved
nonanomalousness and the same local argument give iota_p∈Z_p^×.
If c_(2,p)≠0, the full corank criterion gives finiteSha_p and
the integral Smith/Cassels argument gives

 v_p#Sha[p-infinity] ≤ 2 floor(v_p(c_(2,p))/2).

In particular valuation≤1 forces that primary group to be zero.
No such coefficient premise at another prime follows fromp=5.

Actual distribution and Hecke relations give

 c_(2,p) ≡ alpha^(-2)A_(2,p) + p C_p/(2alpha³) modp²,

where C_p is the explicitly defined level3 weighted carry sum.
At5: A2=−5, C5=237, and the two terms are5 and15mod25.
The carry is essential. If A_(2,p) is p-divisible, the next test is

 alpha A_(2,p)/p + C_p/2 !=0modp,

whose residue is3 at5. The calculation does not prove that test
uniformly, or bound its exceptional primes. A zero test modulo p²
does not prove that the actual coefficient vanishes.
The remaining uniform nonvanishing statement is: for every good
splitp, some finite leveln has a nonzero certified residue modulo
p^(n−1). No all-prime proof is supplied.

The known CM pairing-nonvanishing results do not provide a
nondegeneracy theorem for this rank-two Qp determinant, or remove
extra Selmer directions. No stronger Bertrand self-height assertion
is used. The point rank over Z[i] is TWO, not one. Rationality of
a hypothetical kernel ratio was not derived.

## Preserved normalizations and restart boundary

All unnormalized tame norms, the theta twelfth power, the Kato
smoothing sign, gamma=1+p, X,Y→T, finite ray exponentsm+1,
Betti vector2pr_rho(gamma_E^+), delta0, k_alpha, g_p²,
e_p and c_cmp=(156iOmega_p)^(-1) remain unchanged.
The frame multiplier stays p/(2#E(F_p)).
The actual local reference C_v is distinct from H_global/2.
The withdrawn arbitrary local Coleman power-series factorization
must not be restored; the actual Rubin derivative supplies c2.

CM-Presentation-BSD still requires ONE rational framed element
before separate completions with the prescribed real and all-local
realizations. Rationality is a conclusion, not an input.

The separate [weighted-adjoint review](review-weighted-theta-adjoint.md)
is also complete PASS; its final hash is
6f38c40b9634a452db136123841f98091f96488bfbee36644be9bffe1d27daa2.
This bounded task is finished. No next mathematical task has been
dispatched; wait for the coordinator's next assignment and preserve
the universal objective, source bounds and review distinctions.

