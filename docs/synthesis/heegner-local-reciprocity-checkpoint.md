# Fresh-prime detection and geometric reciprocity for TP5

Date: 2026-09-12. Author /root/uniform_witness, GPT-6 Astra/xhigh.
Own only heegner-local-reciprocity-attack.md and this checkpoint.
The parent objective is full BSD for every elliptic curve over Q.
No old numerical certificate is to be rerun and no agent spawned.

An initial checkpoint was saved before sources. The bounded
construction is now completed and independently reviewed in
[heegner-local-reciprocity-attack.md](heegner-local-reciprocity-attack.md);
all [NEW] claims passed the
[coordinator review](review-heegner-local-reciprocity.md).

Historical assignment, now completed:
starting with the reviewed actual two-prime point P_m and residue
theta_m in the maximal-order Mordell-Weil lattice quotient, construct
actual local finite-coefficient tests at fresh Heegner/Kolyvagin primes.
The tests must detect the full p^k class, not only its mod-p reduction.
Then construct a precise level-raised/Jochnowitz/toric expression for
those tests in a justified hypothesis range.

Preserve the reviewed signed normalization:
u_r=(-w(E))^r(-1)^(r(r-1)/2), so u_2=-1.
Conjugation acts by Frob_v on finite local evaluation and by
minus Frob_v on transverse evaluation. Do not globally apply
a local coefficient endomorphism without equivariance.

Starting proof two-prime-heegner-height-attack.md and its review were
read. The separate compact-support duality construction is now in
heegner-defect-duality.md with an independent PASS review.
This task supplies genuine fresh-prime maps and geometric values.
Its full-image hypothesis remains explicit; no higher-rank
vanishing is inferred. Any further new deduction requires
independent review before promotion.

Completed material proof, all seven sections saved:

1. In the additional range rho_(p^k)(G_Q)=GL2(Z/p^k), the raw
two-prime class has conjugation sign + and uniquely descends to
H1(Q,E[p^k]). For a nonzero class of exact order p^s, restriction
to Q(E[p^k]) is injective by the central-scalar cocycle argument.
Its translation image is p^(k-s)(Z/p^k)^2, by the matrix units.
Taking h in that kernel with chosen plus translation w and
Frobenius coset h*tau gives evaluation at (h*tau)^2 equal2w^+.
Chebotarev therefore detects the exact p^s order at infinitely
many fresh primes v with v=-1,a_v=0 modulo p^k. K remains disjoint
from the cocycle field: K is not in the torsion field by ramification,
and the further extension is a p-group. Proposition2.1 gives the
full proof and handles Frobenius conjugacy, not only a chosen element.

2. Actual geometric reciprocity construction: supersingular set
Sigma_v on X0(N)/F_(v²), modular reduction pi_v, and finite-field
Kummer evaluation give a function
psi_v(s)=lambda_v pr^+ delta_v(pi_v(s)) in Z/p^k,
where lambda_v is a declared basis of the plus eigenspace.
Hecke equivariance of pi gives eigenvalues a_r; Frobenius
permutation gives U_v=+1. The local test of the actual P_m is
exactly sum_(S,i,j) i*j psi_v(red_v(x_m^(S sigma_l^i sigma_q^j))).
This is a genuine, possibly nonprimitive or zero, mod-p^k quaternionic
toric expression without assuming a characteristic-zero eigenform lift.
The function is the arithmetic Frobenius value of the actual cyclic
p^k-isogeny cover pulled back along pi, using
A_v=Etilde/V_v^- and eta_v:A_v→Etilde. Connectedness or primitivity
of that cover/function is not assumed. A displayed Hecke operator
e_t=(T_t−t−1)/(a_t−t−1) puts the toric divisor in degree zero while
preserving its value; the denominator is a proved p-adic unit.

3. Primary Bertolini-Darmon, Euler systems and Jochnowitz congruences,
Amer J Math121(1999)259–281, author PDF:
https://www.math.mcgill.ca/darmon/pub/Articles/Research/21.Jochnowitz/paper.pdf
Read §§1–2 and Thm6.1 (authorp24): its published congruence is modp,
for optimal E/minimal parametrization, absolute irreducibility,
p not dividing2Ndeg(pi), and fresh Kolyvagin prime.
Its exact factor is u*deg(pi), not an unspecified unit.
Do NOT upgrade this theorem to all p^k or to conductor m derivatives.
The reviewed direct reduction construction above gives the needed
finite-coefficient toric statement without such an upgrade.

4. Directly read Vatsal, Special values of anticyclotomic L-functions,
DukeMathJ116(2003)219–261, author
https://personal.math.ubc.ca/~vatsal/research/mew3.pdf
for the primary direct supersingular-evaluation construction.
The working fetched URL was https://www.math.ubc.ca/~vatsal/research/mew3.pdf .
Used source scope: §6.6–6.8 CM/supersingular geometry and §6.12–6.16
isogeny-cover/Frobenius/Hecke mechanism. Did NOT import the source's
nonvanishing/primitivity or characteristic-zero lifting theorem.

5. Actual analytic and symmetry test: untwisted first-derivative
vanishing gives augmentation Theta_(v,1)=0. Exact conductor fiber
sums satisfy the a_r trace identities. Neither identity computes
the derived coefficient [1](S D_l D_q Theta_(v,m)).
Plus Frobenius projection kills every odd-index derived toric sum
by the reviewed conjugation sign, but not the two-prime even index.
No abstract norm-relation countermodel was repeated.

6. Exact remaining GAP LR-TP5 is equation(26): under O5 and the
explicit full-image hypothesis at this k, prove every actual
derived isogeny-cover toric value psi_(v,k)(e_t D_(v,m)) is zero
modulo p^k. Propositions2.1/4.2 make this equivalent to theta_m=0
in that range. Non-surjective image cases remain outside this
detection proof; full BSD remains the parent objective.

Root's final PASS covers all seven sections, including the
full-p^k Chebotarev argument, actual cyclic isogeny cover,
direct finite-field toric identity, and both final scope precisions:
the a_r-only relation (25) uses r inert in K with r not dividing
cNpvD; Proposition6.2 uses squarefree products of Heegner
Kolyvagin primes.
Reviewed mathematical revision:
630ad951d62671fdb6b1dce97e4ec17bf964a51bd91169ce6e859fbb5b7566b4.
Subsequent PASS links and checkpoint updates are editorial.

Next mathematical target remains LR-TP5: prove the actual
derived toric values vanish modulo the full p^k under the
stated rank-five and image hypotheses. This has not been proved.
No old numerical calculation was rerun, no package installed,
and no agent spawned.
