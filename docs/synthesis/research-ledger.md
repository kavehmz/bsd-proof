# Research ledger — arguments already tested

Checkpoint date: 2026-09-12. This is a decision/evidence ledger, not a transcript.
Read [research-state.md](research-state.md) for the objective and next action.

## 1. Initial inherited reduction was repaired

The September 11 synthesis claimed P1–P3 were a complete sufficient package.
That claim was withdrawn. The original report is preserved at
[final-report-2026-09-11.md](final-report-2026-09-11.md).
The [first continuation](continuation-2026-09-12.md) records the audit.

Corrections that must survive compaction:

- Selmer corank s_p equals Mordell–Weil rank plus the divisible corank of
  Sha[p-infinity]. s_p=2 alone does not prove rank 2 or primary finiteness.
- First nonvanishing of a Kolyvagin system is not stabilization of its
  divisibility indices. The old equivalence nu=1 iff M1=M-infinity was invalid.
- Kim's maximum formula does not automatically give his minimum formula;
  the latter has a corank-difference-one condition.
- Complex rationality of L-leading/(period·regulator) is not the full BSD
  formula and has not been proved equivalent here to p-adic uniformity.
- A theorem at almost all ordinary primes does not control the complementary
  primes, and an unspecified finite exception set does not certify those exceptions.
- Surjective residual representations do not cover CM curves.
- Absence of a unit witness is not the converse of a theorem asserting that
  a unit witness implies a small Selmer group.
- A finite-precision coefficient O(p^k) is not an exact zero certificate.

## 2. Product-character / Kurihara route

**Completed:** the mixed difference at fixed modulus

    D_n = sum_a [a/n]^+ product_i (chi_i(a)-1)

is divisible by (zeta_p-1)^m and, after division, reduces to the mod-p
Kurihara number. Proper-subset character sums are imprimitive and require
Euler factors. The two-prime factor is
a_q-chi_l(q)-chi_l(q)^(-1). The exact 389a1 witness at p=5 uses l=41,q=61,
primitive roots 6 and 2, and has unreduced sum 244. Both exact modular-symbol
backends agree at all 2,501 evaluated cusps.

**Completed:** under primitivity, the first unit index is dim Sel_p, including
possible divisible Sha contributions. The [uniform note](uniform-witness-attack.md)
and [review](review-uniform-witness.md) prove this from the higher Fitting ideals.

**Tested and invalid as a formal shortcut:** deleting auxiliary primes merely
because two rational points are known. The module
Z_p^2 + (Z/p)^2 has a primitive family consistent with all relevant
same-parity Fitting identities but first unit index 4. Z_p^4 also allows an
extra divisible corank. These are formal countermodels, not BSD counterexamples.

**Completed:** Chebotarev can realize every functional on a finite cohomology
subspace using nonidentity-unipotent primes. Two tests with invertible determinant
on the rational-point Kummer space leave a kernel isomorphic to Sha[p]. The
joint-image argument uses the fact that V^d is a sum of simple modules; it
does not assert that all representations in characteristic p are semisimple.
Identity Frobenius also satisfies the numerical admissibility congruences but
has local dimension 2; use nonidentity unipotents for one-dimensional tests.

**Tested and invalid:** finite generation of the modular-symbol lattice, or a
gcd across different p, without respecting p-dependent admissibility. A finite
presentation over product_p Z_p also need not have finite prime support:
the element (p)_p is a nonunit in every component. A fixed matrix over Z with
the required maps to the FULL Sel_p would work, but has not been constructed.

## 3. Higher rank / auxiliary quadratic twist route

**Completed:** for odd analytic rank >=3, choose a rank-zero quadratic twist
with all required Heegner and p-splitting conditions. BCGS then gives
nu_K=s_p(E)-1; bottom-class vanishing and parity yield s_p>=3. Kim's corank
theorem gives full-quotient low-index vanishing, without independently assuming
that the entire Kurihara family is nonzero. This repaired an overlooked implication
in the inherited GAP 5.

**Next frontier:** for odd analytic rank >=5, the same argument allows s_p=3.
The exact additional target is vanishing of all two-prime Heegner classes.
The [odd-rank note](odd-rank-selmer-bridge.md) gives the equivalence.

**Tested and invalid:** infer derived vanishing solely from zero norm relations.
In Z_p[C_m x C_n], with p^k dividing m,n, take x=(sigma-1)(tau-1).
Both norms kill x, yet D_sigma D_tau x is the nonzero double norm modulo p^k.
This does not incorporate all geometry of Heegner points and is not an arithmetic
counterexample. It excludes only the proposed formal trace implication.

## 4. Determinant descent / interpolation route

The [derived-comparison note](derived-comparison-attack.md) proves:

- A determinant's leading coefficient retains the Smith torsion factors.
- A rectangular cofactor gives the rank-one derived vector; a scalar height
  determinant can vanish while the Bockstein vector remains nonzero.
- Full exact bounded p-adic interpolation determines a series, even though
  p-power torsion parameters approach the boundary, not zero.
- Twist valuations do not determine the central leading valuation. For p>=5,
  u=T/(2+T) and F_a=u^r(p^a+u^2) have the same central rank, inversion sign,
  mu/lambda, and valuations at EVERY nontrivial p-power torsion point,
  but their central coefficient valuations are a. These are power-series
  counterexamples to a shortcut, not elliptic-curve L-functions.
- Finite-order characters on a fixed finite group have no nonconstant holomorphic
  complex deformation. The approximation (zeta_p^k-1)/(zeta_p-1)~k is not
  uniform over k in F_p. No automatic complex Mellin-derivative limit follows.

**Surviving sufficient criterion:** with rank equality, positive rational BSD
quotient, primary finiteness at every prime, and the one-sided complex valuation
inequality at every prime, the adjusted quotient is an integer divisible by
the full Sha order. A suitable real bound below twice a proved lower bound
on that order forces equality. For 389a1 the real bound is now certified;
rationality and the all-prime comparison remain unproved.

**Source traps already checked:** BKS determinant descent in the cited 2024
paper retains a primary-Sha-finiteness hypothesis. The companion 2025 paper's
Theorem 1.1 explicitly assumes BSD over Q. Construction of its determinant
element does not prove its conjectural specialization identity.

## 5. Geometric torsor route

The [geometric note](genus-one-finiteness-attack.md) separates:

1. Pic^d(X) has torsor class d[X]; finding a rational degree-d class already
   requires d[X]=0.
2. Local solubility kills the subsequent Picard-to-Brauer obstruction by
   Brauer–Hasse–Noether.

It proves period=index=minimum divisor/splitting-field degree for locally
soluble genus-one torsors, and proves that a uniform such bound is equivalent
to Sha finiteness. It does not obtain a uniform bound.

**Tested and invalid:** Riemann–Roch manufactures a degree-1 or degree-3 line
bundle; the canonical bundle gives positive degree; fixed-degree polarized
Shafarevich finiteness bounds all degrees; H^1 of an abelian scheme is finite
merely because the scheme is of finite type. Each argument omits an essential
condition. A plane cubic model exists only for torsors killed by 3.

**Additional checks:** a fixed splitting source would give a uniform exponent
by restriction/corestriction, but has not been constructed. The number-field
local conditions differ from completions at points of a curve over a number
field. The actual quotient construction over C(B) gives torsors of unbounded
period with fixed Jacobian and good reduction; it tests a base-insensitive
geometric argument and is explicitly NOT a number-field BSD counterexample.

## 6. Numerical proof facts worth retaining

- The analytic rank lower bound in the examples comes from two independent
  points plus the analytic-rank-zero/one theorem and parity. It is not inferred
  from near-zero derivatives.
- Mellin quadrature uses the completed L-function and the exact Fricke sign;
  both the coefficient tail and integration tail are explicitly bounded.
  Arb's `analytic` flag must be passed to the logarithm.
- BSD/Cremona height is lim 4^(-k) h_x(2^k P), twice Silverman's half-height
  convention. The full real period for positive discriminant has two components.
- For 389a1 the homogeneous Bezout identities give a duplication error <=log1728
  and |H-h_x|<=log12. Exhausting 319 x-values and 13 point pairs proves global
  minimum nonzero height >0.3. The rank-two lattice bound proves the basis is full.
- At p=3, the raw descent lattice's index 3 matters. Use a full basis for the
  regulator. v_3(epsilon)=2, v_3(R)=0, v_3(log4)=1, so the complete factor has
  valuation 0. Integral 3-adic surjectivity is separately proved with Tate inertia.
- At p=389, L_p has the extra T factor. The certified T^3 coefficient is
  355 mod389; v(R)=2, v(L-invariant)=1, v(log390)=1, giving total factor valuation 0.

## 7. Primary source restart map

Read exact hypotheses in the linked local notes before applying a theorem.

- Kim structure: [2203.12159v6](https://arxiv.org/html/2203.12159v6),
  Theorem 1.8 (corank and higher Fitting ideals).
- Kim comparison: [2203.12161v7](https://arxiv.org/html/2203.12161v7),
  Theorems 2.3 and 3.1. Some older project links use v5; later work checked current statements.
- BCGS: [2312.09301v2](https://arxiv.org/html/2312.09301v2), Theorem A and Corollary A.
- Castella–Sano: [2601.14504v1](https://arxiv.org/html/2601.14504v1), Theorem B,
  primitive Kurihara families at ordinary and squarefree-conductor supersingular primes.
- Castella–Wan: [39-page author PDF](https://web.math.ucsb.edu/~castella/Perrin-Riou.pdf),
  Theorem A/6.11 and its local-twist construction. Do not attribute that exact
  scope to the older 34-page arXiv version without checking.
- Friedberg–Hoffstein 1995: Theorem B local nonvanishing was checked through
  primary applications by Castella–Wan and Skinner; the original theorem pages
  were not directly fetched. Preserve that source-reading limitation.
- Stein–Wuthrich: [published offprint](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf),
  Theorems 6.1, 7.2–7.4, and regulator normalization. The draft has the same used statements.
- BKS 2024: [published PDF](https://kurihara.math.keio.ac.jp/bks4.pdf),
  JMSJ 76(3), 855–919, Hypothesis 2.2, Theorems 7.3/7.6/7.8.
  Infinite-level conjecture is 4.8 published, 4.9 in arXiv v2.
- BKS 2025: [2103.11535v1](https://arxiv.org/html/2103.11535v1),
  Theorem 1.1(d) assumes BSD; Proposition 4.4 has a conjectural premise.
- Geometric sources: Milne ADT II.5.5; Poonen Picard–Brauer sequence;
  [Krämer–Maculan 2310.08485v5 §3](https://arxiv.org/html/2310.08485v5#S3)
  proves fixed-polarization finiteness, not a uniform polarization bound.

## 8. Historical checkpoint before the current research round

A family-specialization task was dispatched to `/root/odd_rank_bridge`, then
paused for the user’s continuity request. Its [checkpoint](family-specialization-checkpoint.md)
is saved and the turn completed; no new result was proved. Read that checkpoint
before continuation. A [fresh-context audit](cold-resume-review.md) passed; no missing context requires user clarification. The latest inventory no longer contains the completed `/root/derived_comparison` handle, so future work on that line needs a replacement if the handle remains absent. Visibility and higher-period tasks were only
planned; do not describe them as executed. Add future results here with a proof
path and the next action they justify.


## 9. Family, visibility, and higher-period round — completed work

The three planned tasks were dispatched after the continuity checkpoint.
Their owned proofs and restart checkpoints now exist.

- [Family specialization](family-specialization-attack.md): full normalized
  determinant sections do continue, but the first conormal derivative is
  insufficient. The perfect-complex matrix D_c has determinant U²T+cT³ and
  retains exact family height/Pfaffian data for every c. Review repaired the
  global Zariski-density proof and added an explicit Bockstein descent identity.
  Disegni's Appendix B correction and Fouquet's strict-criticality condition
  were retained. FS remains unproved.
- [Modular visibility](modular-visibility-attack.md): exact local obstruction
  sequences and prime-to-degree Selmer/Sha splitting are proved. At389 the
  modular degree and congruence number are 40, and the entire visible Sha is 0.
  The unknown group injects into Sha(J0(389)); the winding quotient projects
  E to 0. The published 5389a1 example refutes the naive prime bound. A nonzero
  elliptic eigenvalue in the Hecke annihilator of Sha(J) is equivalent to the
  original finiteness question; H389 is not proved.
- [Higher periods](higher-period-integrality-attack.md): the anchored Chen
  representation is exact, but raw log differentials have infinite translation
  orbit. Corrected higher cocycles exist; their ordinary higher group-cohomology
  class is 0, so extra secondary data is needed. The eta second jet has the
  explicit even correction C. Its [certified value](eta-correction-certificate.md)
  lies between 110 and 111 on actual 389a1; the uncorrected identity is therefore
  false on that curve. HP-eta asks for the arithmetic interpretation of the
  corrected difference. No rationality or integrality was proved.
- [Coherent moment test](coherent-moment-attack.md): θ=U+U^-1−2 is one integral
  object for all odd p. Under U→(1+T)^{log_p2/log_p(1+p)}, its central order 2
  and μ0 persist; the second coefficient is nonunit at 1093 and 3511. This refutes
  a denominators-only/all-good-primes leading-unit rule. It makes no claim
  about infinitely many exceptions. Primitive tensor proportionality would
  give integrality, but the arithmetic tensor identification remains missing.

The independent reviews are linked from the proofs. New computations are
`coherent_measure_check.py` and `certify_eta_correction.py`. The eta bounds
were rederived by root and checked at a second cutoff/precision. The earlier
four BSD-example certificates were not rerun merely for this research round.

Next research should construct an actual arithmetic comparison for HP-eta or
the regulator tensor, or a genuine Hecke annihilator; repeating primitivity,
first-jet interpolation, winding projection, or ordinary higher cohomology
alone will not supply the already identified missing information. The full
BSD objective remains active.

## 10. Arithmetic surface, Green class, and CM tensor round

The first three constructions have passed independent review:

- [Hecke–Brauer](hecke-brauer-annihilator-attack.md),
  [review](review-hecke-brauer.md): the normalized finite-coefficient
  geometric restriction kernel is H¹(Q,J[n]); its Selmer cokernel is
  full Sha(J)[n]. Section splitting handles even coefficients. On 389,
  T₂−T₃+1 kills constant and degree pieces but acts as identity on the
  elliptic image. Closed-point evaluation is zero for every strict
  local Brauer class. The Frobenius coefficient action differs from
  the inner-conjugation cochain map. No annihilator follows.
- [Weil–étale model](weil-etale-lattice-attack.md),
  [review](review-weil-etale-lattice.md): the actual regular plane cubic
  has Pic=Z³ and Br=Sha including the real 2-primary term. Its full
  degree-three Z(1) cohomology is this torsion group. Finite generation
  required by Flach–Morin is therefore precisely full Sha finiteness.
  The arithmetic zeta is ζ(s)ζ(s−1)/L(E,s) with pole order three and
  leading coefficient −1/(2 ell_E). Compact Selmer Tate-module limits
  do not retain finite primary groups or bound prime support. The new
  exact surface check and reciprocal data passed; the review checked
  their hash and interval without rerunning the old certificate.
- [Arithmetic Green class](arithmetic-green-comparison.md),
  [review](review-arithmetic-green.md): s=N⁶Δ(z)Δ(Nz) defines ω²⁴ with
  divisor (N+1)(0+∞)+6(X_N^∞−X_N^0) and Green function −48U.
  The actual arithmetic theta identity is the linear pairing −24I(U),
  with all metric and vertical terms. Its generic degree-zero cusp
  class is torsion and its elliptic point image is zero. Literal U²α
  is not closed and is not the arithmetic star product. This leaves
  a secondary construction involving noncuspidal point data, not a
  general prohibition on such constructions.

The [CM tensor note](cm-regulator-tensor-attack.md) passed
[root review](review-cm-regulator-tensor.md) after a direct source audit.
The checked new parts are: CM symmetry forces the ordinary weight-two
correction to zero; the actual full regulator is
4A_p B_p−(C_p−A_p−B_p)² with the specified sigma/Coleman evaluations;
and the log-square moment has the uniform mod-p⁴ polynomial
(X−Y)²(3−X−Y)/(p−1)². Exact restricted moments were reconstructed from
BK's two unit projectors, homogeneity and partial Katz definitions.
One-variable pole-subtraction discrepancies are killed by the other
projector. The q-prefactors cancel in the central twist, the ray classes
are counted once, and CRT representatives preserve the torsion arguments.
The inverse-lattice factor supplies the shifted Euler exponents; all
period powers and factorials remain. The unrestricted moment display
with a zero theta parameter is not used, nor are the source's compressed
all-residue sum and period-power displays. CM-Theta was repaired to require
the real BSD quotient to be rational before a canonical p-adic equality.

For y²=x³+39x, exact descent and the Mellin proof certify analytic and
algebraic rank two. Root independently reconstructed Fourier coefficients
through 1405 and ran a second cutoff/precision certificate. The complete
new data is `compute/data/cm39_analytic_rank_certificate.json`, reproducer
`compute/scripts/certify_cm39.py`. Its interval is strictly inside the
agent's first one. This verifies analytic order, not the leading formula.

Immediate handoff: retain the reconstructed restricted formula, then
attack the actual rationality-first CM-Theta identity or the HB-cycle
global line-bundle construction. No full
BSD proof, counterexample, Sha annihilator, or complex rationality has
been obtained in this round.

## 11. Explicit relative motives and twisted bundles

This round constructed arithmetic objects for the previously stated gaps.
It did not prove the remaining analytic comparison or a uniform period bound.

- [Ordinary K-theory lattice](k-theory-lattice-attack.md),
  [review PASS](review-k-theory-lattice.md): the actual regular 389 model
  is étale simply connected. Frobenius determinants from the exact point
  counts 5,6,9 at 2,3,5 kill every primary geometric coinvariant; the
  integral zero section and proper homotopy sequence then kill the full
  group. Unramified class field theory gives CH₀=0. Ordinary K₀ is
  Z⊕Pic=Z⁴ with square-zero rank ideal. Its actual c₁ map still has
  cokernel Sha[n] for every n. No uniform lifting scalar was constructed.
- [CM relative cycle](cm-biextension-cycle-attack.md),
  [review PASS](review-cm-biextension-cycle.md): six explicit points on
  y²=x³+39x define a rank-six 1-motive. The complete finite correction
  is encoded by fixed rational torus points with matrix
  [[3/2,27/98],[27/98,243/2]] and rational frames of denominator two.
  Its specified secondary exterior operation is the full real or ordinary
  p-adic height determinant. The naive ordinary exterior zero-cycle has
  zero Deligne regulator; graded exchange signs were checked. Finite
  torsion-endpoint 1-motives cannot map nontrivially to its top lattice,
  and the generalized Jacobian has no algebraic characters. These are
  specific map obstructions, not a theorem excluding higher extensions.
- [Non-CM relative cycle](relative-modular-cycle-attack.md),
  [review PASS](review-relative-modular-cycle.md): on 389a1, explicit
  rational functions h₁,h₂ modify two disjoint point divisors so every
  finite local symbol vanishes. The actual marked generalized Jacobian
  then realizes the full BSD height matrix in its real periods. Its
  full-period Betti line uses 2a, of index two; no primitivity is claimed
  for that factor. Pullback to X₀(389) multiplies the matrix by 40.
  The specific translated projected cusp loop contracts, so all flat
  holonomy/Chen lengths vanish. The ordinary cusp 1-motive tensor-square
  also cannot map to its top determinant because the point extension
  P⊗e₂−Q⊗e₁ is nonzero. The Mellin-decorated comparison RM-389 remains.
- [Twisted-sheaf lifting](twisted-sheaf-lifting-attack.md),
  [coordinator review PASS](review-twisted-sheaf-lifting.md): locally
  soluble period-n classes give actual global twisted bundles of rank n,
  stable of degree one on the generic curve and extensible with the same
  rank to the regular surface. The fixed determinant moduli gerbe over Q
  is neutralized by BHN; it does not neutralize the original gerbe on E.
  Review added its infinitesimal rigidity and clarified the étale base
  neighborhoods used for reflexive extension. A degree-n torsor point
  gives a second Poincaré pushforward, and an explicit elementary transform
  makes it stable of degree one. Minimal rank and generic index equal n.
  End(V) has ordinary K₀ class n²[O], retaining β in its multiplication.

The [detailed Fourier–Mukai review](review-twisted-fm.md) passed. Its
calculation sends the stable twisted bundle to O_C(−D), an ordinary line
of degree −n on the torsor C. Pair stabilization and the actual numerical
twisted lattice retain rank divisibility by n on the original twisted E.
Generic twisted K₀ is abstractly Z⁴, but its numerical Euler determinant
is n². Thus fixed abstract rank does not remove the individual period.

Next: construct the higher analytic-frame comparison or a truly uniform
splitting construction. The newly built
height objects and twisted objects are usable inputs; assigning their
desired analytic scalar or bounding their ranks by definition is not.

## 12. Bott, derived units, spectral jets, and projective connections

All four constructions below passed independent review. Their results
are arithmetic or analytic constructions with explicit comparison maps;
none is a full BSD proof or counterexample.

- [Bott comparison](bott-comparison-attack.md),
  [PASS review](review-bott-comparison.md): for odd p and m=p^r, the
  canonical Tate basis of weight φ(m) gives genuine higher motivic
  realizations of all finite Selmer classes. For p≥5 an actual pure-Adams
  Quillen Bott class and the projector −(ψ²−1)(ψ²−4)/2 realize the same
  summand in K_(2φ(m)). The raw Bott map has cokernel Br(E)[m]⊕Br(Q)[m];
  the normalized Selmer quotient is exactly Sha[m]. Minimum positive
  primitive Tate weight is φ(m); no primitive lift exists at the next
  p-power with that fixed weight. Both coefficient Bocksteins have exact
  order m in their stated prime ranges. Positive-degree Bott inversion
  kills the characteristic-p fiber. A uniform integer annihilating the
  Selmer quotient remains GAP Bott-389.
- [CM derived elliptic units](cm-derived-unit-attack.md),
  [PASS review](review-cm-derived-unit.md): actual rational theta units
  on the two-variable CM ray tower, twisted before cyclotomic descent,
  give an integrally normalized Kato class z∞ with exact Coleman image
  L_p(E,T). The factor twelve, opposite Schmitt/Kato smoothing signs,
  conjugate CM type, and rational Betti factor two are explicit. Kato's
  height-one inequality plus global Euler characteristic proves actual
  integral divisibility z∞=T w∞ without finite Sha. The specialization
  w₀ lies in the full Selmer space, and its first derived height pairing
  is proved there. If the known two-point regulator is nonzero, a
  height-orthogonal projection and the factor p/(2#E(F_p)) give exactly
  Z_p=(c_cmp M_p/(4 e_p Reg_p))Ξ in the constructed frame line. Additional
  Selmer directions are retained in the projection kernel, not proved
  absent. These separate p-adic elements have not been descended to one
  rational element with the required complex realization: GAP CM-Derived.
- [Full-curve spectral jet](mellin-variation-attack.md),
  [PASS review](review-mellin-variation.md): exact Rankin–Selberg unfolding
  gives I(u)=−24Γ(u+1)/(4π)^(u+1) times
  L(f,u+1)L(f,u)/(ζ(2u)(1+389^(−u))). Its u=1 second Laurent coefficient
  pairs to −9·389/(π⁴·390) times ell_E L(f,2). All earlier pairings vanish.
  Both cusp scattering terms, the nilpotent Laplacian chain, the effective
  orbifold versus modular-stack distinction, and the fine-cover degree
  194 are retained. A literal finite homogeneous Gauss–Manin tensor
  cannot realize that nonsemisimple Casimir jet; this does not exclude
  mixed extensions. The explicit modular-unit K₂ transfer is killed by
  two, and the specified diagonal first character-response integral has
  an L(f,1) factor and vanishes. A second character variation is now
  being constructed. GAP MV-389 still requires the arithmetic comparison
  and justified division by the L(f,2) regulator factor.
- [Projective monodromy](projective-monodromy-attack.md),
  [PASS review](review-projective-monodromy.md): the actual stable
  twisted (n,1) bundle has a faithful projective trivialization by [n],
  of degree n². Its arithmetic form is an E[n]-torsor whose local
  condition is Kummer membership, not local triviality. At good p|n,
  the projective Atiyah obstruction is nonzero for every degree-one
  extension, including unstable ones and the ordinary Brauer-zero
  control. Degree-zero Poincaré pushforwards admit integral local
  connections at every good p without dividing n. Enforcing finite
  monodromy by the torsor's n-cover instead retains the full E[n]-torsor
  and rank n². A torsion line's finite-order connection extends exactly
  when its universal-vector-extension obstruction b vanishes modulo n;
  full finite-flat descent is still required. The Tate fiber at 389
  contributes actual ramification and component conditions. No uniform
  splitting degree or global Kummer adjustment is obtained (GAP PM-389).

The last CM source audit resolved an apparent Frobenius conflict:
ordinary cohomological F has eigenvalues β on ω and α on xω, whereas
the Tate-twisted φ=F/p has eigenvalues α⁻¹ and β⁻¹ respectively.
MST §3.2, SW §3.5 and BKS Lemma 6.9 give this dictionary. The printed
reciprocal-root label in SW §4.1 is not used. The prior E₂=0 conclusion
and the derived-unit Euler factors remain valid. Both the proof and
review now preserve this distinction explicitly.

No old numerical suite was rerun for this round. New next tasks must
construct the remaining global comparison, not identify finite-level
motivic existence, a separate p-adic realization, or an integral local
connection with its missing global conclusion.

## 13. Second character response and the actual Mellin trace

The [second character variation](spectral-second-variation-attack.md)
passed [coordinator review](review-spectral-second-variation.md).
The gauge-normalized positive Laplacian has derivatives
L₁=−4πiD_w and L₂=8π²|w|². Its actual scattering Hessian is
8π²/(2s−1) times the difference between four times the resolvent
pairing of D_wE_a,D_wE_b and the direct |w|²E_aE_b pairing.
All cusp phases, the negative double pole, its simple coefficient,
the full finite part, and the T-versus-character derivative are retained.

The two integral elliptic Betti directions have exact Hodge Gram matrix
diag(40b/ω₁,40ω₁/b), with determinant 1600. This refutes only a literal
identification with the fixed Mordell–Weil height matrix. A positive
construction moves the point divisors off the cusp images and expresses
the actual height matrix through the same reduced Green operator:

    H_ij = -(2π/40)<δ_(π*Z_j), G δ_(π*D'_i)> - log|U_ij|,
    U = [[11337/596372, -3599/9025], [-405/1652, 6/25]].

Root independently checked all point equations and the four Weil-
reciprocity products by rational arithmetic. This did not rerun any old
analytic or height certificate. The corrected formula retains changed
finite symbols through its rational logarithms. Merely sharing G does
not identify the smooth spectral sources with the marked point sources.

The new [Mellin trace calculation](mellin-trace-comparison.md) passed
[independent review](review-mellin-trace.md) and tests that sharper map.
Retain α=π*ω=c_π2πifdz and l=log|v|. The actual forcing satisfies

    F dμ = -i/(4π²c_π) d(lα),
    π_*(F dμ)=0,

because Norm_π(v)=±1 gives trace(l)=0. These equalities hold on the
compactified curves as currents, with no hidden cusp atoms. Hence F
pairs to zero with every pulled degree-zero point Green potential away
from O. Its reduced Green solution GF has constant fiber trace and
therefore zero pairing with every corresponding degree-zero point charge.
This result concerns F; it is not asserted for the distinct D_wA_a
sources in the scattering Hessian.

Keeping the spectral A₂ produces an actual nonzero pushed current T.
Its product rule contains both the derivative of ω·trace(A₂l) and the
extra term π_*(l dA₂∧α). The latter carries the entire nonzero mass
−9·389/(π⁴·390) ell_E L(f,2). Replacing this weighted trace by the
ordinary norm would erase the required term. GAP MT-389 is an arithmetic
realization of that decorated current with its point-determinant/L(f,2)
comparison. An analytic Green solution after subtracting its mass does
not establish rationality or integrality. No full BSD result follows.

The next parallel torsion-connection and motivic-derivative constructions
are in progress and require their own independent reviews. Their early
checkpoint claims must not inherit PASS from this section.

## 14. Finite torsion differentials and a genuine logarithm replacement

The two follow-up constructions now have their own PASS reviews.

The [torsion-connection proof](projective-torsion-connection-attack.md),
[coordinator review](review-projective-torsion-connection.md), identifies
the old universal-vector-extension obstruction exactly with Cartier-dual
dlog in ω_E/n. The equality is proved on the entire finite-flat group
scheme by pulling back the integral connection and comparing its canonical
trivialization under translation. At an ordinary prime, its exact value
is the étale coordinate a(t) divided by the specified differential unit u.
The kernel is the connected subgroup of the dual; the whole ordinary
extension was not assumed split.

For good supersingular reduction over an unramified p-adic base, a point
of exact order p^s in E[p^r] has obstruction valuation

    r-s + p/(p²-1),   1<=s<=r.

This is strictly below r. The proof uses the Eisenstein Newton polygon
of [p](z)/z, the actual quotient-isogeny derivative of valuation 1/(p+1),
and Fargues' order-p calculation. It retains the annihilator of every
torsion differential and does not replace a cotangent image by its
saturation. The independent general Hodge–Tate cokernel bound also
supplies some nonzero obstruction at every good p≥3.

Saturating a generic horizontal line in any integral algebra model gives
an actual horizontal line bundle on the regular surface. Picard
injectivity then prevents an unstable or nondiagonal lattice from hiding
the torsion obstruction. Thus the full torsion-character packet's fixed
finite-monodromy connection cannot extend regularly at any good p≥3
dividing its period. This covers every possible remaining period prime
for 389a1 and also occurs for the ordinary Brauer-zero control.

A positive ordinary block of rank p^r is constructed schematically from
a connected dual coset of the locally soluble division torsor. The dual
quotient isogeny is actually finite étale and trivializes its algebra,
so the constant connection descends integrally, including nonreduced
coset fibers. Its endomorphism character support is exactly the local
connected subgroup. The surjective global residual image prevents this
block from descending over Q. A marked singleton in a G_Q-stable subset
would give a point of its finite torsor; its scalar endomorphism algebra
alone supplies no such point. Brauer vanishing corresponds to a trivial
torsor only after the allowed global Kummer adjustment. GAP TC-389
remains a uniform splitting construction beyond this packet.

The [CM motivic derivative](cm-motivic-derivative-attack.md),
[independent review](review-cm-motivic-derivative.md), computes the actual
Sen operator of the coefficient deformation V_pE⊗Q_p[T]/T². With the
inverse cyclotomic action it has nontrivial two-by-two nilpotent blocks
at Sen eigenvalues 0 and 1. It is not Hodge–Tate, even after a finite
local extension. This excludes a literal geometric realization of that
coefficient deformation in the stated Hodge–Tate class, not the derived
Selmer class, its height, or every motive giving its scalar.

A genuine replacement is constructed: pull the first G_m logarithm
motive back along the actual rational theta function. Its specialization
is [Z→G_m], whose boundary is the usual Kummer class of the theta unit;
its norm is exactly the Kummer class of the already constructed norm
unit. The elliptic first-log fiber at a torsion point instead splits
rationally, and the principal divisor residue has zero Abel–Jacobi class.
The quadratic toric logarithm has the explicit nullhomotopy
d(−k(g)²/2)=k(g)χ(g)k(h) in Q_p(2). The CM twist gives an extension
of the positive-weight motive R by M_Ψ, not of Q by M_Ψ; a rational
Betti basis is not an invariant rational coefficient insertion.

There is nevertheless an exact finite extraction of the desired class.
For n≥m, send γ to 1+T in (Z/p^m)[T]/T². The actual finite unit
class has a cocycle f=a+Tb. Its augmentation vanishes by the already
proved integral divisibility. Write a(g)=gv−v; the derivative is

    d_m(g)=b(g)+c_γ(g)gv.

H⁰(E[p^m])=0 makes the cohomological extraction unique. Its corrected
representative is independent of choices, is compatible in m, and
recovers exactly w₀ and the existing p-adic framed scalar. No extra
finite-level Selmer claim is needed. The new operation retains integral
torsion coefficients; neither it nor the genuine rational logarithm
construction proves that all framed scalars descend to one rational
element with real realization ell_E/(2Ω_E). That remains
GAP CM-Log-Derived.

All four source, trace, differential and cochain constructions of this
round are completed and reviewed. The universal BSD goal remains active.
A new bounded task is dispatched on the general O5 two-prime Heegner
class and its actual height/character expansion; its results require a
new review. The next rational-comparison direction is an actual mixed
extension using the correctly weighted unit and point motives.

## 15. Actual arithmetic metrics, Heegner lattice descent, and mixed comparisons

Four further constructions passed their own independent reviews.

### Actual arithmetic Chow realization

[Proof](arithmetic-metric-realization.md),
[PASS review](review-arithmetic-metric.md). On the actual regular 389
model, CH²=0 and the integral Gillet–Soulé exact sequence give
widehat CH²≅R via arithmetic degree; its inverse is q↦a(2qμ_E).
The proof retains the left regulator term and uses degree to prove that
its image in this particular top-form quotient is zero. Higher
codimensions ≥3 vanish. No new Sha premise occurs.

The actual decorated Mellin current T gives the original Green-current
class (0,2Re T), with the correct real-involution sign and degree M.
It equals a(2Mμ_E). An explicit constant-metric line product gives the
same class, extending the earlier elementary metric example to this
complete group calculation. Thus this particular arithmetic realization
has now been constructed. It contains unrestricted real metric data;
the finite rational motivic/frame map in AM-389 is still missing.
The cup determinant of the top Chow classes for the four height entries
is zero in codimension four, while the determinant of their real degrees
is the certified positive regulator. These are different operations.

### Universal two-prime Heegner object and exact lattice obstruction

[Proof](two-prime-heegner-height-attack.md),
[PASS review](review-two-prime-heegner-height.md). Under the full ordinary
O5 hypotheses, the actual point P_m=S_GD_ell D_q y_m at m=ell q is
constructed with its trace, cocycle, coefficient ideal and transverse
local conditions. H_m/Q is Galois and unramified at p; residual
irreducibility and the Weil pairing prove E(H_m)[p]=0 directly.
No p-prime class number or split class-group extension is assumed.

Review replaced the compressed global use of Howard's local Frobenius
map with an on-page scalar normalization. Raw conjugation has eigenvalue
epsilon_r=(-w(E))(−1)^r. Finite local evaluation transforms by Frob_v,
whereas transverse evaluation transforms by −Frob_v. The scalars
u_r=(-w(E))^r(−1)^(r(r−1)/2) normalize every finite-singular edge;
u_2=−1, preserving vanishing at the full common p-power. A local
coefficient matrix is not simply applied to a global cocycle.

The toric decomposition retains primitive conductor c_chi and every
missing-prime trace factor a_r. Cai–Shu–Tian's exact Gross–Zagier formula
then computes the height of the specified lift P_m, including degree(π),
8π², sqrt|D|, the Petersson norm and all character weights. Untwisted
fifth-order vanishing kills the trivial character; the other surviving
terms involve different primitive Rankin L-functions. A height of an
unspecified residue-class representative is not introduced.

Let M_m=E(H_m)⊗Z_p, O_m the maximal order in Q_p[Gal(H_m/K)],
M_m^max=O_m M_m and C_m=M_m^max/M_m. These are actual arithmetic
lattices. With e_ell=v_p(ell+1), e_q=v_p(q+1) and k the full common
Kolyvagin exponent, character evaluation proves

    S_GD_ell D_q ∈ p^(e_ell+e_q−1) O_m.

Hence the actual candidate Q_m^max=P_m/p^k exists in
p^(e_ell+e_q−1−k)M_m^max. Its residue theta_m belongs to
C_m[p^k]^G at that same depth. The Tor injection, Kummer map and
exact restriction give theta_m=0 iff the two-prime O5 class is zero.
Fourier inversion only kills C_m by p^(v_p(h_K)+e_ell+e_q), short
of the sufficient exponent by v_p(h_K)+k+1. GAP TP5 is descent of
this particular divided point to M_m. The construction does not
prove that descent, even though it realizes the missing element exactly.

### Spectral jets and finite regular-singular period expressions

[Proof](spectral-regular-singular-attack.md),
[PASS review](review-spectral-regular-singular.md). At each cusp, the
first Fourier mode of A₁ and A₂ is computed using the exact normalized
Bessel derivatives J(Z)=exp(Z)E₁(Z) and
H(Z)=integral_Z^infinity J(u)du/u. Their inverse-Z coefficients are
(−1)^(j−1)(j−1)! and that number divided by j, with explicit remainder
bounds. The factorial sector remains in every A₂+cA₁+dA₀.

A precise coefficient-field lemma proves that a rational-log expression
with convergent meromorphic Puiseux coefficients and a full pure-power
asymptotic expansion must have a convergent such series. This excludes
the actual cusp jets from the specified finite period-expression class.
The class includes rational period operations, inverse logs, log Hodge
norms, and canonical admissible biextension heights in the verified charts.
Review corrected the exponent lower bound to total exponential order
and required a uniform denominator lower bound on a full angular strip.
Removal of the real nilpotent-orbit factor supplies that chart control
for the stated canonical heights. No arbitrary metric or motive giving
the same integrated scalar is excluded. This is a pointwise functional
result, not a proof that MT-389 has no arithmetic solution.

### Genuine CM blends and the corrected local reference

[Proof](cm-mixed-extension-attack.md),
[PASS review](review-cm-mixed-extension.md). The simple fiber product of
the unit extension with the dual point extension canonically splits in
the lower point direction. Genuine three-step blends are instead
constructed by forming the lower semiabelian object with its coefficient
action first, lifting the free upper marking basis through split-torus
fibers, extending by that action, and clearing denominators. Tensoring
by the pure B component gives actual 1-motives of weights −2,−1,0.
No CM projector is applied to a whole marked point motive.

The exact dual class is y_j=−kappa_B(P_j), the central matrix satisfies
dZ_ij=−x_i cup y_j, and an actual theta unit translates it by its
Kummer cocycle. The affine norm of the translated blend back to K
loses that translation because the unit norm lies in μ₄. This is
distinguished from a reference-dependent transition without degree
normalization. Taking the determinant before trace retains a quadratic
log-unit period, but its exact tower recurrence has a variance term
and it is not the same additive operation as the cyclotomic derivative.

Review found and removed a local/global normalization error. The
normalized GLOBAL K-height has AB component H/2, but this does not
construct a chosen-embedding local reference H/2. The actual local
block is C_v. The corrected identity has baseline 4det C_v, with no
unproved replacement by Reg_v. The missing finite/local corrections
for the pairs (P_i,iP_j) are not supplied by conjugation invariance.
The exact finite extraction uses coefficient-one J=E_ij and the
canonical integral Kummer model of the DIFFERENCE of blends; it
does not reduce an arbitrary rational blend modulo p^m. That difference
recovers the unchanged d_m and exact p-local framed scalar. The point
data cancels from it. GAP CM-Mixed-Derived still requires a rational
secondary comparison with the real BSD realization.

All source conventions and repairs above are recorded in the proof and
review pairs. No old numerical suite was rerun. The next work must
control the actual integral Heegner defect or construct the rational
integrated-period comparison, rather than repeat the already computed
norm, metric or literal finite-period-function operations.


## 16. Full-coefficient Heegner tests, exponential periods, and CM p-unit pairing

**[NEW, independently reviewed deductions]** Four constructions are complete.
The proof/review pairs below were inspected by root before synthesis. None
proves O5, a rational BSD determinant, full Sha finiteness, or universal BSD.

### Actual compact-support duality for the Heegner defect

[Proof](heegner-defect-duality.md), [checkpoint](heegner-duality-checkpoint.md),
[PASS review](review-heegner-defect-duality.md).
Under the exact ordinary O5 hypotheses, the raw two-prime class has plus
conjugation sign. The already proved full-coefficient one-prime vanishing
and finite-singular relations give zero localization at BOTH old primes
ell,q. Thus its unique Q-descent is

    kappa_Q = (1/2) cor_(K/Q) kappa_K

in strict finite Selmer, including the actual local Kummer components.
No Sha finiteness or control theorem across a p-degree extension is assumed.

Set U=Spec Z[1/(Np|D|m)], with S EXACTLY its complement plus the real place,
V=E[p^k], F=H_m and Gamma=Gal(F/Q). The actual defect theta_m lies in
D_m=C_m[p^k]^Gamma. The Tor injection, Kummer map and inverse restriction
inject D_m into H^1(U,V), taking theta_m to kappa_Q. Finite Artin–Verdier
duality then gives the canonical surjection

    H^2_c(U,V) -> Hom(D_m,(1/p^k)Z/Z).

This detects exact order. The compact-first Weil pairing uses the ordinary
coefficient identification v -> (w -> e(w,v)). Its actual étale cochain
cone has D(a,b)=(da,res(a)-db); local boundaries pair by the sum of local
invariants. The global degree-two cochain is retained, without asserting a
higher-degree K(pi,1) property. For odd p the real Tate contribution is zero.

Quotienting H^2_c by local Kummer boundaries away from ell,q and ALL local
H^1 boundaries at ell,q gives the perfect dual of strict finite Selmer.
These old-prime boundary tests all annihilate kappa_Q. This quotient keeps
point directions and is not the Cassels–Tate pairing on Sha.
Corestriction gives H^2_c(U_F,V)_Gamma isomorphic to H^2_c(U,V), whereas
pairing two base-changed classes multiplies by
[F:Q]=2h_K(ell+1)(q+1), hence gives zero at these coefficients.
Coinvariants and corestriction cannot be replaced by invariant averaging.
The primary finite-duality input is Demarche–Harari 1804.03941v3,
Theorem 1.1 and §2, with Milne ADT II.3 for finite étale traces.

**[GAP HD-TP5]** Prove every such duality value of kappa_Q is zero in the
stated analytic-rank-five range. Perfect detection makes this equivalent
to the old integral descent; it does not supply vanishing.

### Fresh-prime detection and actual finite geometric reciprocity

[Proof](heegner-local-reciprocity-attack.md),
[checkpoint](heegner-local-reciprocity-checkpoint.md),
[PASS review](review-heegner-local-reciprocity.md).
The detection argument additionally assumes the FULL image
rho_(p^k)(G_Q)=GL_2(Z/p^k), not just the irreducibility in O5.
The central scalar 2I kills H^1(GL_2,V); matrix units identify the
translation image of a class of order p^s with p^(k-s)V. Ramification
keeps K disjoint from the torsion field and its p-group cocycle extension.
An appropriate h times complex conjugation has square translation 2w.
Chebotarev gives infinitely many fresh Kolyvagin primes detecting the
class's exact order, with a_v=0 and v=-1 modulo p^k.

At such a prime the plus/minus Frobenius decomposition gives an actual
cyclic isogeny cover A_v -> Etilde, where A_v=Etilde/V^- and its kernel
is the constant plus quotient. Pullback along the reduced modular
parametrization and finite-field Kummer theory give a concrete
supersingular function psi_(v,k) with values in Z/p^k. The cover need
not be geometrically connected, and the function need not be primitive
or nonzero. Direct reduction of the actual Heegner point proves

    ev_v(loc kappa_K) = psi_(v,k)(D_(v,m)),

where the divisor retains every ring-class term, every ij derivative
weight, and repeated reductions. No automorphism-weight division is
introduced. A Hecke operator e_t=(T_t-t-1)/(a_t-t-1) puts the divisor
in degree zero without changing its value; e_t is not asserted idempotent.
The toric group-ring expression is the coefficient at the identity,
[1](S_G D_ell D_q Theta_(v,m)), not augmentation.

Vatsal's primary supersingular/isogeny-cover construction is used in its
stated scope. Bertolini–Darmon's Theorem 6.1 is kept as a residual,
conductor-one result with its optimality, degree and image hypotheses;
it is not promoted to arbitrary p^k or derived conductor. The direct
finite-field construction supplies the displayed p^k identity instead.
Conductor trace relations use fresh INERT primes outside cNpvD.
Conjugation kills odd-index plus evaluations for squarefree Heegner
products; the two-prime even index survives this symmetry test.

**[GAP LR-TP5]** Under O5 and the additional full-image hypothesis, prove
psi_(v,k)(e_t D_(v,m))=0 modulo p^k for every fresh detecting v. This is
equivalent to theta_m=0 in that range. Bottom augmentation, conductor
traces and parity have not compared higher untwisted derivatives with
this weighted coefficient. The full-image restriction remains explicit.

### Actual exponential source of individual spectral kernels

[Proof](exponential-spectral-attack.md),
[checkpoint](exponential-spectral-checkpoint.md),
[PASS review](review-exponential-spectral.md).
For F=Q(Z), A=F[t]/t^3 and q_*=v(v+Z)/Z, the proof constructs the
rank-three rational flat connection d-dv+t dlog(q_*). Its fiber complex
vR -> R dv, R=A[v,(v+Z)^(-1)], has H^0=0 and H^1 free of rank two
over A. The endpoint at zero is RELATIVE/MODERATE, while positive infinity
is rapid decay. The puncture -Z contributes closed-loop monodromy.
This is proved with actual relative cycles, not by applying an absolute
rapid-decay theorem to a regular-singular endpoint.

The rational Betti coefficient functionals are
lambda_j=(2 pi i)^(-j) coeff_(t^j); the lattice basis is
lambda_0,lambda_1,2lambda_2. Six explicit relative cycles give a
nondegenerate comparison matrix with determinant
(2 pi i)^(-3) exp(3Z), up to the fixed ordering. The kernel is

    I(t,Z)=integral_0^infinity exp(-v) v^t (1+v/Z)^t dv.

Its exact Gauss–Manin system implies
I''-I'-t(t+1)I/Z^2=0 without division by t. A separate relative gamma
complex realizes Gamma(1+t). The inverse truncated at t^3 is a finite
polynomial in its coefficients, using tensor products of actual periods.
Thus the normalized Bessel jets J(Z)=exp(Z)E_1(Z) and
H(Z)=integral_Z^infinity J(u)du/u have an actual exponential period source.

Completing the Eisenstein series by Gamma(s)xi(2s)(N^(2s)-1) retains
both cusps and the pole contribution c_3 R to its second Laurent
coefficient. Its paired mass is exactly
-3N(N-1) ell_E L(E,2)/(2 pi^3), or -226398 ell_E L(E,2)/pi^3 at 389.
Each nonzero completed Fourier mode uses the constructed I and ordinary
finite logarithmic factors. The zero modes, the full infinite Fourier
sum, and the substitution Z=-2n log|q| have NOT been placed in a common
finite arithmetic realization. Individual kernel construction is not
an algebraic pullback for that substitution. The rational BSD frame and
L(E,2) regulator division remain open. Root subsequently corrected three
literal LaTeX comma typos; no reviewed mathematical formula changed.

### Cyclotomic p-units and the exact CM-character mismatch

[Proof](cm-cyclotomic-pairing-attack.md),
[checkpoint](cm-cyclotomic-pairing-checkpoint.md),
[PASS review](review-cm-cyclotomic-pairing.md).
In the actual ray tower F_r=K(f p^r), consecutive degrees are p^2.
The actual theta units U_r and cyclotomic p-units v_r=1-zeta_(p^r)
satisfy Norm U_(r+1)=U_r and Norm v_(r+1)=v_r^p.
Writing phi_r=p^(r-1)(p-1), w_r=v_r^phi_r/p is a global unit;
centering v_r uses denominators and does not erase its finite boundary.
Rational norm compatibility by multiplying [v_r] by p^(1-r) has
unbounded p-denominators.

Four coefficient-one CM blends give exactly log(U_r)log(v_r), independent
of the chosen local reference C_v, with no hidden factor two or four.
The averaged product obeys P_(r+1)=p^(-3)P_r+Cov_r, where the explicit
fiber covariance remains. No bounded limit or automatic norm compatibility
is inferred. The integral motivic symbol {U_r,v_r} is formed before
reduction. Its cup class retains the delta(p) term even when log_p(p)=0.
The exact corestriction formula also retains every off-diagonal term.

The compatible ray involution tau is 1 modulo f and -1 modulo p^r.
It fixes the cyclotomic tower, while both relevant CM twists have value
-1 on tau. Therefore the unweighted log product sees the tau-even unit
part and kills the tau-odd part; the exact Kato class and derivative
see the tau-odd part and kill the even part. No nonvanishing of the
derivative is assumed. The correct dual twist is Psi^(-1).
For the twisted cup, vanishing on the odd unit part holds after
CUP-THEN-CORESTRICTION to C_r, and after its further traces/localizations.
The RAW untraced cup over F_r is not asserted zero. Finite Tate coefficient
changes do not turn degree-two cohomology into the H^1 derivative or give
an invariant rational insertion into Q(-1).

**[GAP CM-CycPair]** Construct an actual tau-odd arithmetic operation
with the required boundary and rational framed realizations. The tested
cyclotomic companion does not provide it. All existing smoothing, Tate,
Euler, gamma-generator and factor-four derivative normalizations remain
unchanged. This is a diagnosis of this specified operation, not a BSD
counterexample.

The next proposed constructions are recorded, as unproved and not yet
dispatched, in [the next research plan](next-research-plan.md). The priority
is to reach rank-sensitive vanishing or a rational global comparison;
more detecting maps alone would not finish either target.


## 17. Irreducible Heegner detection, actual cofactors, and the global theta source

**[NEW, independently reviewed deductions]** This round completes four
further constructions. Each has a separate PASS review, and root read the
full mathematical drafts and review scopes before synthesis. It removes
one hypothesis from detection and constructs the noncentral regulator
line; it does not prove the required Heegner vanishing or BSD comparison.

### Signed closed-point tests and the original irreducible range

[Proof](heegner-gysin-bridge.md), [checkpoint](heegner-gysin-checkpoint.md),
[PASS review](review-heegner-gysin.md).
Actual local Kummer purity and étale excision construct closed-support
classes on the ORIGINAL number ring U. Their exact convention required
and received a review repair: for D(a,b)=(da,f(a)-db) and natural PLUS
projection, the canonical connecting map is beta -> (0,-beta).
The preceding duality paper had fixed instead the SIGNED boundary
partial^+(beta)=(0,+beta) and a trace positive on that signed boundary.
Both the new and predecessor notes now say so explicitly.

Accordingly G_v=-g_v^std is the SIGNED closed-point class, negative of
the standard positive-valuation Gysin. The trace is also the negative
of the canonical-boundary-normalized trace. In the actual excision
model, support sends (o,b) to (0,o,-b,0), while open extension sends
(a,s,l) to (a,0,l,s). Thus G_v(y)=-j_!partial^+_v(y delta(v)).
An independent cocycle calculation gives
inv(delta(v) cup chi)=-chi(Frob_v)/p^k. The two signs yield

    P(z,G_v(y)) = lambda_y(z(Frob_v))/p^k.

At a fresh inert v with a_v congruent0 and v congruent-1 modulo p^k,
choose lambda_v an R-isomorphism on V_v^+ and its actual Weil-dual
coefficient y_v. The unramified quadratic restriction contributes TWO:

    P(kappa_Q,2G_v(y_v)) = psi_(v,k)(e_t D_(v,m))/p^k.

This factor is separate from the raw-to-standard u_2=-1 scalar.
These are actual geometric representatives, not representatives picked
by abstract duality to have a desired value.

**The additional full-image hypothesis is now removed.** Primary
Lawson–Wuthrich1505.02940v2 Lemmas3–4, checked by root and reviewer,
give H^1(G_k,E[p^k])=0 for every k when E[p] is irreducible over Q.
The actual translation submodule W has a nonzero residual leading
layer; irreducibility and Nakayama give W=p^tV, replacing the old use
of full matrix units. Its exponent equals the exact order of the class.
The existing disjointness and h times complex conjugation argument
therefore gives fresh exact-order detecting primes under the ORIGINAL
O5 hypotheses. It applies to every class in finite H^1(U,V).
Consequently the signed G_v generate all H^2_c(U,V), with a finite
subset sufficient, and also generate its strict Selmer dual quotient.
No assertion that irreducibility implies full Galois image is made.

For a finite generating set T, actual global residue relations give
an exact presentation

    B_T -> direct_sum_(v in T) H^0(F_v,V(-1))
        -> H^2_c(U,V)/L_m -> 0.

Here B_T consists of b in H^1(U minus T,V) whose old S-localizations
are finite Kummer away from ell,q and arbitrary at ell,q. The proof
establishes the stronger specified-localization equivalence:
sum G_v(y_v)=partial^+_S(alpha) iff there is an actual global b with
residue tuple y and loc_S b=alpha. In particular
sum G_v(res_v b)=partial^+_S(loc_S b). Point directions are retained.
Annihilating these relations only makes the Heegner functional descend;
it does not prove it zero on the generators. Gysin-TP5 is still open.

### A level-Nv construction leaves an explicit trace-zero point

[Proof](heegner-toric-vanishing-attack.md),
[checkpoint](heegner-toric-vanishing-checkpoint.md),
[PASS review](review-heegner-toric-vanishing.md).
Lift the actual weighted conductor-m divisor to X_0(Nv) over H_mv.
The norm retains the cusp correction
v aug(A_m)([1/N]-[infinity]); its two degeneracy images vanish but
it is not removed before the integral point calculation. The two
maps to E give the actual points P and Y, with Tr(Y)=a_v P.
Their old E-squared block has degeneracy matrix

    d_pi [[v+1,a_v],[a_v,v+1]].

The rational projector has both denominators v+1 +/- a_v, each
divisible by p^k. Its complement may include other old factors.
The determinant d_v=(v+1)^2-a_v^2 has p^{2k} as a divisor.
Clearing that projector denominator automatically erases the finite
test, irrespective of rank. Its specified first quotient instead
retains the actual cofactor points

    B1=((v+1)P-a_v Y)/p^k,
    B2=((v+1)Y-a_v P)/p^k.

These are integral combinations of specified points; Tr(B2)=0.
If x=delta_v(Pbar) is the original finite Kummer value, the actual
CM-isogeny reduction and Frobenius polynomial give

    B1bar=-x,    B2bar=-Frob_v x.

Thus B2bar retains the full order of the original toric obstruction.
It is also the specified division term in the three-prime raw cocycle.
The exact normalization agrees with the earlier finite/transverse signs.

The height of THIS B2 is computed by its primitive character expansion.
Only characters ramified at the fresh v survive. Its exact prefactor is
d_pi sqrt|D|/(8pi^2(f,f) p^{2k} h_m^2), and each term retains
c_chi, the squared derivative-operator weight and every missing-prime
a_r^2 factor. The untwisted character was eliminated by the actual
cofactor operation; no theorem sets this remaining height sum to zero
from the untwisted third derivative. Torsion of B2 would suffice but
is stronger than the needed vanishing of its reduction.

The degeneracy determinant is also v^2 times the removed good local
Rankin Euler polynomial at s=1. The product-rule derivative identity
is valid over C, while d_v is not an integral unit at p. Replacing
it by a v-new Steinberg factor would be an additional comparison, not
an identity for E. TV-TP5 remains B2bar=0 at all detecting primes,
now covering the original irreducible range by the preceding theorem.

### Actual CM first jets in both ray directions

[Proof](cm-two-variable-jet-attack.md),
[checkpoint](cm-two-variable-jet-checkpoint.md),
[root PASS review](review-cm-two-variable-jet.md).
The actual CM ray group is Delta times two Z_p factors, with
|Delta|=1152(p-1)^2. Fix their generators by Tate-character pairs
(1+p,1) and (1,1+p). Both map to the old cyclotomic gamma:
X,Y map to T, not to one-half T. The diagonal subgroup is a different
map. Ray exponents at least m+1 are retained for finite first jets
modulo p^m. Twisting actual theta units and taking UNNORMALIZED norms
to the Delta-fixed bi-layers gives the source class. Before twisting,
its projector is e_(rho^-1); after restriction the norm is |Delta|
times that projector. This finite scalar is not discarded.

The exact smoothing is
q_a(X,Y)=12(a^2-u_a(1+X)^{lambda_a}(1+Y)^{lambda_a}),
u_a=+/-a, with the old a=5 or a=7 choice. It is an integral unit;
q_a(T,T) is exactly the old Kato divisor. Transitivity of the actual
field norms and Shapiro gives the prior cyclotomic class with all
Betti and tame factors. Its cohomological augmentation is zero.

For the actual inverse-action first-jet cocycle A+XB+YD, write
A(g)=gv-v. Vanishing H^0 makes the two corrected classes UNIQUE:

    d_pi,m(g)=B(g)+c_pi(g)gv,
    d_barpi,m(g)=D(g)+c_barpi(g)gv.

They are integral and coefficient-compatible; their sum is exactly
the old d_m and w_0 under the fixed Shapiro map. Neither summand is
asserted nonzero or individually Selmer. Only the sum has the already
proved full Selmer property.

The coefficient Koszul resolution proves actual derived base change.
For M=H^1_Iw and N=H^2_Iw it retains

    0 -> Tor_2(N,Z_p) -> M/(X,Y)M -> H^1(K,T_pi)
      -> Tor_1(N,Z_p) -> 0,

and the cyclotomic quotient retains N[X-Y]. Hence zero augmentation
does not prove I-divisibility in M. The actual second-order lift gives
c_pi cup d_pi=0, c_barpi cup d_barpi=0 and
c_pi cup d_barpi+c_barpi cup d_pi=0 in ORDINARY global H^2.
These are not vanishing statements for a Selmer height with local
terms. The rational global frame with the real BSD realization remains
unconstructed; CM-TwoJet keeps that exact target.

### A full theta integral and the actual noncentral K2 divisor

[Proof](integrated-spectral-comparison-attack.md),
[checkpoint](integrated-spectral-comparison-checkpoint.md),
[PASS review](review-integrated-spectral-comparison.md).
The source uses the full universal lattices Zz+Z and Zz+(1/N)Z,
with the SAME transported source Hodge norm |w|^2/y. Their heat
traces differ by H_N. Gaussian Poisson summation gives a single
Mellin integral for the entire completed Eisenstein family, including
zero modes and both cusps. Joint Gaussian/cusp bounds retain both
heat endpoints and all derivatives, not merely iterated convergence.

For the actual paired trace T_F(u),

    M_T(s)=integral_0^infinity u^{s-1}T_F(u)du
          =-24/sqrt(N) Lambda(E,s)Lambda(E,s+1).

It is entire and symmetric under s ->1-s. Its constant and first
logarithmic moments at s=1 vanish. The second moment gives exactly
the old mass -3N(N-1) ell_E L(E,2)/(2pi^3).
Subtracting (N-1)chi(u)/u defines a smooth relative analytic
three-cocycle on the fine-cover Borel–Serre surface times the
compactified heat interval. It is flat at every joint corner.
The chain is integral upstairs, with the effective covering degree
194 explicitly retained. An actual eta transgression proves
cutoff independence. This is a global ANALYTIC cohomology source;
it is not yet a rational arithmetic realization.

A separate positive arithmetic construction now supplies the extra
divisor. Using Brunault math/0602186, Propositions80/86, Theorem81,
(3.84), the nonvanishing argument on pp.97–98 and (3.110), the proof
constructs beta2 in K2(E) tensor Q with EXACT real regulator L(E,2)/pi.
Root and the reviewer checked primary source scopes; character bars
and constants were inspected on rendered pages. The construction
uses rational cusp-normalized units U_a on X_mu(389), finite symbols,
integer cusp-path homology and algebraic coefficient traces.

Specifically the finite class k_chi uses
(1/N)S_chi S_barchi sum_(a,b) barchi(a)chi(b){U_a,U_b}.
The coefficient b_chi=-(1/N)sum_(r mod +/-)barchi(r)j_r is defined
by integral homology, not by an unknown real quotient. At least one
is nonzero by the stated prime-level modular-symbol result. Both
k_chi and b_chi are coefficient-Galois covariant. Normalizing at
EVERY embedding before coefficientwise trace gives a rational beta2
with the claimed regulator. No arbitrary automorphism of a period
or integral primitivity is assumed. All denominators remain.

Thus the rational line B2=Q beta2 is available. The exact comparison
target is D_pt tensor B2 tensor Q(1)^(-2), with frame evaluation
-Omega_E Reg_E L(E,2)/(4pi^3). A compatible arithmetic image of the
spectral class would have coefficient 6N(N-1)n_E in that line.
That image/map is still unconstructed. Even integrality of the large
integer multiple would not alone prove n_E integral. IS-389 remains
the rational arithmetic source and factorization through this exact
line; the old missing noncentral divisor line is now constructed.

All four new proof/review pairs are complete. This was a mathematical
progress turn, with an explicit convention repair. No full BSD proof
or counterexample has been obtained, and the universal goal remains active.


## 18. Individual Selmer conditions, arithmetic K2 extension, and higher residue tests

**[NEW, independently reviewed deductions]** Four constructions have separate
PASS reviews and root inspection. The individual CM local-condition question
and arithmetic extension of the noncentral divisor are resolved. The
rank-five vanishing and rational BSD comparison remain unproved.

### Both actual CM ray derivatives are individually Selmer

[Proof](cm-ray-local-conditions-attack.md),
[checkpoint](cm-ray-local-conditions-checkpoint.md),
[root PASS review](review-cm-ray-local-conditions.md).
For an elliptic curve over Q with a non-torsion rational point and any
odd p, a deduction from local/global duality gives

    H1(G_Q,S,V_pE) = H1_f(Q,V_pE).

This is not claimed as a new historical duality theorem. Rational local
H1 vanishes away from p, whereas at p its dimension is two and the
one-dimensional point-Kummer line is self-annihilating. The fixed point
has nonzero local logarithm and spans that line. Global reciprocity against
it leaves only the p-local term and forces every global class into the
finite line. A single point need not do this over a general number field.
Global H1 is not identified with Mordell–Weil: Tate-module Sha remains.

Integrally, H1(F,T)/E(F)^completion is T_p H1(F,E), which is
p-torsion-free. The preimage of the rational finite line is therefore the
FULL integral Kummer image, including torsion. Shapiro and the integral
CM projectors apply separately to the actual two ray derivatives. Both,
their difference, and every integral combination are Selmer, with all
finite reductions. This uses their actual compatible integral lifts;
arbitrary finite global H1 classes are not declared Selmer.

The formal CM component has all of its one-dimensional H1 finite,
with crystalline eigenvalue beta^(-1). The unramified component has
finite rational space zero, with eigenvalue alpha^(-1). Its possible
integral torsion is (alpha-1)^(-1)Z_p/Z_p. For this actual E39 it is
zero: rational 2-torsion and Hasse rule out p dividing #E(F_p) for
p>=7, and at5 the recorded exact count is8. Hence both unramified-place
localizations vanish integrally and at every finite coefficient.

The exact BKS Coleman coordinate is zero for EACH derivative:

    [exp*(loc d_j),delta0]
      = (loc kappa(P),loc d_j)/(k_alpha log_omega(P)) = 0,
    delta0=k_alpha^(-1)nu,
    k_alpha=(1-alpha^(-1))^(-1)(1-beta^(-1)).

The division is in Q_p; integral conclusions use saturation, not division
modulo p^m. No individual projected determinant formula, nonvanishing or
independence is inferred. Two-variable Tor terms and possible failure of
I-divisibility remain. CM-Ray-BSD still requires the rational global frame.

### The SAME noncentral K2 divisor extends over the arithmetic model

[Proof](k2-arithmetic-divisor-attack.md),
[checkpoint](k2-arithmetic-divisor-checkpoint.md),
[PASS review](review-k2-arithmetic-divisor.md).
Schappacher–Scholl1.1.2(iii) is an arithmetic IMAGE theorem for the actual
unramified modular-unit symbols, not only their regulator values. Its
coprime full-level premise is handled at3*389, retaining the degree under
rational pull-push. Chow-correspondence functoriality and the actual
coefficient trace preserve the particular beta2 in the arithmetic K-image.

Review refined the source scope: the rational K/CH comparison of
Geisser's Handbook1.4.4 is applied over the DVR Z_(389), where the
model is regular but its fiber is not smooth. It gives zero rational
CH boundary there. Every good-prime rational target is zero separately;
Geisser2004 Theorem3.2, Corollary3.3 and Lemma2.4 give GLOBAL Bloch
localization. No smooth-over-Z or stronger global comparison is assumed.

On the actual nodal fiber, z=(t-148)/(t-241) identifies its smooth
open with G_m. Localization gives

    CH1(D,2)=0,    CH1(D,1)=F389* × z^Z.

The branch valuations sum to j-j=0 at the ONE node. This is not the
ordinary unit group of a proper singular curve. Every good fiber has
the corresponding groups0 andFr*. Consequently restriction
CH2(model,2) -> CH2(E,2) is INTEGRALLY injective. Its image is the
kernel of actual vertical residues; rationally only the nodal exponent
survives. That exponent is zero for beta2, which therefore has a UNIQUE
rational higher-Chow lift.

Finite data give a sufficient integral multiple. Choose M clearing the
fixed rational cusp-unit denominators and D_c clearing the coefficient
list. Doubling the actual symbols kills their horizontal tame signs,
since all possible support cusps are RATIONAL on X_mu and Q* has only
+/-1 torsion. Thus D0=2M^2D_c gives a SPECIFIED integral generic
preimage b. Spread its finite cycle over model[1/S0]. At each remaining
prime r the torsion boundary is killed by r-1; at389 the free exponent
was already zero, leaving torsion killed by388. Therefore

    D1=lcm_(r in S0)(r-1),    D=D0 D1

gives a unique integral extension B of the specified D1 b, with regulator
D L(E,2)/pi. No numerical D, primitive integrality, or saturated lattice
is claimed. Integral claims concern Bloch CH2, not an integral Adams
splitting. K2-IS-389 remains the spectral arithmetic map and its lattice
control; arithmetic extension of the noncentral divisor is complete.

### Actual higher Heegner residues control a surviving direction

[Proof](heegner-higher-residue-attack.md),
[checkpoint](heegner-higher-residue-checkpoint.md),
[PASS review](review-heegner-higher-residue.md).
Actual higher even-index classes descend to Q and lie in B_T. Their
old ell,q components are retained and removed only in the strict dual
quotient. Their positive tame residues are -h_(J,v)y_v, with h the
minus-coordinate of actual odd-index finite values, equivalently higher
cofactor reductions. There is no factor two on inertia; the rational
Frobenius pairing separately has denominator2p^k.

Root corrected the draft polynomial identity to
(a_v-F_v)(F_v^2-1)=(v+1)F_v-a_v. The cofactor/residue conclusions
already used that sign and did not change. Signed Gysin conventions
and raw/standard scalars remain explicit. Actual four-prime classes give

    h_ij g_i+h_ji g_j=0,
    h_ij a_i+h_ji a_j=0 modulo p^k.

Joint plus/minus Chebotarev uses Lawson–Wuthrich cohomology vanishing.
Complex-conjugation idempotents and irreducibility generate full matrix
ALGEBRA, without claiming full GROUP image. Double annihilators identify
the actual simultaneous translation image and allow prescribed zero/order
tests for an internal direct sum of classes.

If the PARTICULAR kappa has full order p^k, a detecting a_i is a unit.
The four-prime relations eliminate certain zero tests while g_i survives.
Joint selection against an arbitrary additional strict class proves
S_m^str=R kappa for the FULL strict finite Selmer group, and then
Sel_(p^k)(E/Q)=R^3. This does not prove the primitive assumption in
analytic rank five, Mordell–Weil rank3, or Sha finiteness. In the
nonprimitive case h_ij remains only in p^sR and h_ji has its actual order;
nonunits are not divided out.

Independently the known Selmer corank>=3 gives R^3 inside finite Selmer,
and two old rank-one local targets leave a free R strict direction.
Thus the actual strict dual is NEVER zero here. Even all residue
relations cannot span every test. That would be a false statement
about this group, not a disproof of O5: the particular Heegner class
could be zero in a nonzero group. HR-TP5 still needs rank-sensitive
information distinguishing that class, including the nonprimitive case.

### Harmonic insertion and the exact arithmetic theta components

[Proof](harmonic-theta-arithmetic-attack.md),
[checkpoint](harmonic-theta-arithmetic-checkpoint.md),
[PASS review](review-harmonic-theta-arithmetic.md).
Actual integration by parts gives the full harmonic theta insertion
with coefficient1/8, retaining all joint cusp/heat bounds, transported
source norm and covering factor194. The fixed spectral derivative is
not replaced by changing an integer coefficient weight.

The cyclic divisor C-N[0] gives a kernel polynomial on the Hodge-frame
torsor of weight N-1. Its Kummer class retains Q(1); trivial Sym^0
coefficient is NOT zero Tate twist. The finite trace is -Npi^2g/3,
or Ng/12 in the Tate frame. Its natural coherent degree-zero heat
family pairs as (N^s-N)M_T(s)/2, of order at least3 at s=1, so its
second paired jet is zero. The full residual is exactly (N-1)E*(z,s),
with nonzero mass. This tests that specific family, not every possible
polylogarithmic extension.

Sprang1802.04996v2 Theorems5.8/6.1 and1801.05677v3 Theorem4.2
supply the actual Poincare/polylog component at fixed integer indices.
For D=5 its finite specialization is -2[d log v_eta] in the declared
Tate Kodaira–Spencer normalization. Printed p31's D^(1-w) shorthand
differs from p35's direct reindexing D^(2-w). Both were visually checked;
the latter follows by direct lattice distribution and is what is used.
No failure of the underlying polylogarithm or BSD is inferred.

The inspected Du–Yang source is1702.07917v2, 52 pages, with arXiv
header4 February2018; its initial v1 attribution was corrected. The
full theta lift accepts exactly J_N and gives I_L(J_N(s))=xi(s)E_L(s).
Its second Laurent response is
E_L^(3)/6+kappa E_L^(2)/2+a1 E_L^(1)+a2 E_L^(0); the fully completed
version retains all coefficients of Gamma(1+t)xi(1+t), including the
cubic cross term with the pole.

The lower j0 has an ACTUAL arithmetic intersection:
I_L(j0)=2<phi,D0+(N/2)X_N^0>. The Kronecker divisor D0 has horizontal
coefficient(N^2-1)/24, vertical coefficient-N/2, and its forced Green
function; the added vertical term is necessary. Those Hodge/vertical/
constant classes span only E_L and E_L'. The full response Q satisfies
Delta_(3/2)^3 Q=-E_L(1)/64 !=0, whereas that tested span hasDelta²0.
It cannot supply the higher response. The codimension-three dimension
observation is in rational/real arithmetic Chow theory, not integral
stack torsion. The original f-weighted comparison remains missing even
after this second theta lift. HT-389 still requires an actual arithmetic
source and rational map to the fixed point-height/K2/Tate line.

All four constructions are completed and reviewed. This was a mathematical
progress turn with explicit source/sign precisions. The full universal
BSD objective remains active and unresolved.

## 19. Actual Iwasawa determinants, Heegner–Kato coefficients, and theta projections

**[NEW, independently reviewed deductions]** All four bounded constructions
have separate PASS reviews and root inspection. This round constructs an
integral determinant element and actual higher coefficients, and computes
specific arithmetic projections. No full BSD proof or counterexample follows.

### The actual CM complex and its integral determinant basis

[Proof](cm-iwasawa-presentation-attack.md),
[checkpoint](cm-iwasawa-presentation-checkpoint.md),
[root PASS](review-cm-iwasawa-presentation.md).
For E:y²=x³+39x, K=Q(i), and every good split p≥5 prime to2·3·13,
put R=Z_p[[X,Y]], I=(X,Y). Nekovář's actual continuous-cohomology
perfectness and coefficient base change, residual H0=0 and cyclotomic
weak Leopoldt give

    RΓ(G_K,S,T_pi tensor R^iota) ≃ [P --D→ Q],
    rank(P)=b+1, rank(Q)=b, M=ker(D)=R h, N=coker(D) torsion.

Freeness of M is proved by dividing the coordinate gcd of a kernel
vector and intersecting the height-one DVRs. Primitive coordinates
need not generate the unit ideal. This is a proved presentation of
the actual complex, not a computed numerical Galois relation matrix.

Write the actual normalized unit as z=f h and its cofactor vector as
Delta=c h, with Delta_j=(-1)^(j+1)det(D_hatj). Rubin's CM main theorem
in Kato15.2/15.6 equates all height-one lengths, INCLUDING at(p),
under the checked roots/tame-degree hypotheses. Hence u=f/c is an
R-unit and eta_z=u epsilon is the exact integral determinant BASIS.
The pre-twist rho-inverse branch, twelfth theta power, q_a smoothing,
unnormalized tame norm1152(p-1)² and Betti coefficient remain in z.
The class/H2 comparison discards only height-one-invisible modules
finite over Z_p. Bad-prime cohomology conventions were checked by
actual residual inertia; no full-module equality is inferred.

The exact free resolution retains

    Tor2_R(N,Z_p)=ker(h0:Z_p→P/IP),
    Tor1_R(N,Z_p)=ker(D0)/Z_p h0,
    N/IN=coker(D0).

Tor2 is Z_p when h0=0, and zero otherwise. The actual derivative
vectors satisfy d_j=f_jh0+f0h_j and f0h0=0. Thus freeness does not
imply I-divisibility or independence. On the cyclotomic quotient,
h(T,T)=s(T)e_c and N[X-Y]=Z_p[[T]]/(s); the division z_cyc=T w
can arise from this specialization defect.

At the unramified split place the local complex is L[-1] with L
free rank one. Adding its actual localization row gives the square
ordinary Selmer matrix A. With F the coordinate of loc(z),

    det(A)=(-1)^b c l,       F=(-1)^b u det(A),       F∈I².

The last-row sign was repaired before final review. Both first
derivatives have unique local nullhomotopies. In the actual Selmer
H2, the NATURAL Bockstein identities are

    partial_pi(d_pi)=F20 j+,
    partial_pi(d_barpi)+partial_barpi(d_pi)=F11 j+,
    partial_barpi(d_barpi)=F02 j+.

j+ is explicitly the positive local coordinate. BKS's height
Bockstein is MINUS the natural connecting map. The two mixed
responses individually are not determined by their sum.

Review withdrew the unnecessary arbitrary local Coleman germ.
Instead loc^-(w)=F(T,T)e_L/T computes the actual Rubin derivative
D(w)=(F20+F11+F02)e_L0 tensor T. The proof of BKS6.14 then gives
c2=O_p(e_L0)(F20+F11+F02), with positive coefficient inclusion.
Its hypotheses use the already proved local Selmer condition, not
finite Sha. O_p(e_L0) is nonzero but not assumed an integral unit;
the old delta0, Euler, logarithm and p/(2#E(F_p)) factors remain.

**A concrete nonvanishing criterion is proved.** If either actual
first ray derivative is nonzero, the primary Selmer corank is two
and Sha(E/Q)[p-infinity] is finite. Indeed if that corank is r≥3,
every maximal minor has I-order at least r-1, so both first unit
jets vanish. Neither derivative's nonvanishing is established.
The square determinant has order at least r and its degree-r part
is the determinant of the actual linear Bockstein matrix in the
induced frames. Specialization of eta_z retains H2 and extra Selmer
directions; it does not supply rational descent or the real BSD
comparison CM-Presentation-BSD.

### Integral second Kato derivative and an actual tame obstruction

[Proof](heegner-kato-comparison-attack.md),
[checkpoint](heegner-kato-comparison-checkpoint.md),
[PASS](review-heegner-kato-comparison.md).
Under the original O5 hypotheses with the stated additional good
ordinary nonanomalous p scope, the actual Néron-normalized Kato
class satisfies z_E=X²w_infinity INTEGRALLY, with w0 in full
integral Selmer and F_E=Col(z_E)∈X³. The proof uses Selmer
corank≥3 without finite Sha. Kato's height-one inequality first
gives X²-division after localization. The injection H1_Iw/X into
torsion-free full global H1 then gives integral X-saturation twice.
Kato18.4 uses Selmer corank, not just the rank of rational points.

Review supplied the missing cohomology comparison: Kato's j_*T
arithmetic complex and the full G_S complex have acyclic difference
at the height-one prime(X). The local rational augmentation at each
bad non-p prime is acyclic; perfect local complexes and derived
Nakayama give the assertion. Changing Euler factors alone would
not have proved this source/target identification.

The published BDV2022 global reciprocity, with its exact stabilization,
smoothing, twist and period factors, gives the normalized BF image

    B=F_D z_E e+ + F_E z_D e-.

The integral image is defined by this right side; saturation of the
geometric BF lattice is NOT proved. Write d0=F_D(0)≠0, without
assuming a p-unit. Its second plus coefficient is d0w0; its third
minus coefficient is c3 z_D0, with
c3=L_p'''(E,1)/(6 log_p(1+p)^3). The twist base z_D0 is nonzero
and p-RELAXED by its dual exponential, not classical Selmer. The
next plus coefficient is a deformation, with a Bockstein cocycle
equation, not an arbitrary pair of global H1 classes. A complex
third derivative cannot replace c3.

For an actual two-prime ring-class coefficient ring, the extra
p∤h_K hypothesis makes the p-primary coordinates independent.
In B=Z/p^k[Y_ell,Y_q]/(Y_ell²,Y_q²), the inverse Artin character
is 1+a_ell Y_ell+a_q Y_q+a_ell a_q Y_ellY_q. Its induced
two-dimensional representation exchanges the trivial and quadratic
components at first degree and preserves them at mixed degree.
The ACTUAL Shapiro Heegner class is Y_ellY_q times the raw
two-prime Kummer class, including the full p^k coefficient and
the unique rational descent. Lower terms vanish by the actual
trace/norm identities. There is no characteristic-zero map from
a nontrivial induced character sector to1⊕epsilon_K.

Lifting the BF bottom z=d0w_k through this tame coefficient has
the exact first equations d t_i=-a_i cup z and mixed equation

    d v=-a_ell cup t_q-a_q cup t_ell-(a_ell a_q) cup z.

The first nullhomotopies are substantive data. At an old prime i,
a_i cup is an isomorphism from the finite plus local line to
H2(Q_i,V tensor epsilon_K), over all Z/p^k. Thus the first old
obstruction is exactly d0 times the old local value of w_k. The
actual cofactor projection cancels these two local values for its
corrected input, but does not solve global twisted H2 or other
local conditions. Its scalar changes when old-local sections are
changed; it cannot be made canonical or a unit by choosing them.

BKS's generalized Perrin–Riou comparison assumes finite primary
Sha and uses r_alg-1 and the ACTUAL complex leading term. The
verified2026 Longo–Vigni source also does not supply the missing
rank-five map. HK-TP5 remains the integral mixed comparison with
lower nullhomotopies, all local conditions and rank-sensitive
complex input. No nonunit factors may be divided away.

### Entire elliptic theta projection and the corrected metric pairing

[Proof](theta-elliptic-projection-attack.md),
[checkpoint](theta-elliptic-projection-checkpoint.md),
[PASS](review-theta-elliptic-projection.md).
For Du–Yang1702.07917v2, direct Fricke conjugation preserves the
lattice and exchanges mu_r with mu_-r. Evenness of the actual
Kudla–Millson kernel and weighted CM cycles gives componentwise
Fricke invariance. Since pi W_389=-pi and both cusps map to O,
the ENTIRE theta series has zero degree-zero point projection to
E389. The nonpositive coefficients retain their cusp, Hodge,
vertical and metric cases. This extends the previous eta-Hodge
calculation to the whole series on this quotient only.

The original forcing F=y²f conjugate(g) is Fricke even, as is
eta=constant log|v_eta| pi*omega; d eta=F dmu. Its nonzero
Mellin mass is not killed. The actual Kummer1-motive [Z→Gm],
1→v_eta, has Fricke inversion equivariance, fixes its weight-zero
lattice, negates its Q(1) torus and retains period2pi i. Deligne
HodgeIII10.1.10 applies over the open curve, including v_eta=1.
This source does not make eta closed or construct the radial motive.

**Review corrected a compactification error.** ReF is Borel–Serre
flat but not algebraically cusp-smooth: its leading term is
(1-N)Re(q)log²|q|/(4pi²). The claimed single smooth GS class
a(2ReF) is withdrawn. Actual smooth cusp/elliptic cutoffs give
classes a(2chi_epsilon ReF) and ONLY the convergent pairing limit

    I_L(F)=lim <phi_hat,a(2chi_epsilon ReF)>_GS
          =deg(phi_hat)/deg(Delta_GS) int ReF mu_GS
                                      +int phi_SM dd^c ReF.

The source's metric one-half and the displayed two cancel.
Complex conjugation removes ImF without conjugating the theta
variable. Cusp cutoff errors are O(epsilon log²epsilon); elliptic
order-e errors are O(epsilon^(2-2/e)); no distributional atom
remains. The first term is NOT set to zero: mu_GS is not the
hyperbolic measure from the prior vanishing. No arithmetic Chow
completion or new stack-current theorem is asserted. TPJ-389
still requires an actual weighted adjoint for int F j2 and a
rational map to the fixed point/K2/Tate determinant line.

### Actual higher arithmetic cycles and their tested projections

[Proof](higher-arithmetic-theta-attack.md),
[checkpoint](higher-arithmetic-theta-checkpoint.md),
[PASS](review-higher-arithmetic-theta.md).
The SSY genus-two cycle on the arithmetic modular stack gives
an actual rank-one face Z_hat(diag(0,t),diag(v1,v2)). Its
intersection, cusp and vertical terms are retained in the native
stack convention. Converting the exact primary Corollary4.16
by its formula226 gives, for positive t,

    degree(Z_hat_0,t) q^t
      =-(2 E_t'(1)+(log v1-2N logN/(N-1))E_t(1))/(N-1).

The target contains E_t'''/6 and fixed lower completion terms.
The explicit residual has third Laplacian -E_t(1)/64; the t=1
value is nonzero by an actual norm-one lattice vector. This
particular face does not supply the response, and derivatives in
log v1 act on an affine expression. Native SSY and Du–Yang
normalizations are related by their explicit analytic formula;
no extra factor two is guessed from the stack terminology.

On A=(universal elliptic curve)^3 over a fine open modular curve
of level35N, three actual norm-projected unit graph cycles give

    Xi ∈ CH³(A minus A[5],1)_Q,       Xi≠0.

For a5-torsion section sigma, choose div(f_sigma)=60(sigma-0)
and use (36-tr_[6])[f_sigma]/2100. This kills base-unit choices,
has trace eigenvalue one and residue sigma-0. The three codimension
two Gysin supports telescope to residue (sigma,tau,upsilon)-0.
Thus the cycle is genuinely nonzero before the regulator. Its
integral multiple2100 is a cycle on this open number-field space;
no arithmetic extension or primitive integral class is claimed.

Kings–Rössler1412.2925v2 identifies its canonical analytic torsion
regulator with minus one-half the translated zero-section current
difference, of type(2,2) with all three Tate twists. The current
is the source's g_(A^vee) ON A modulo partial/bar-partial images.
Two specified projections are zero: restriction to the open where
all three coordinates avoid5-torsion, hence to all-nonzero7-torsion
sections; and product with the rational polarization Chern class.
The analytic scalar is checked by integrating the canonical GLOBAL
current difference against invariant curvature on compact fibers.
It is not obtained by extending an arbitrary current class from
the punctured space. This precision was required by review.

The nonzero cycle and its regulator are actual arithmetic objects,
but these projections do not yield the nonzero weighted Mellin
mass. The abelian-scheme theorem is not extended over generalized
elliptic cusp fibers without new boundary data. HAT-389 remains
another actual secondary operation with the required response and
the original weighted rational comparison.

This round made mathematical progress, with three substantive source
or regularity repairs. All four reviews pass. The universal rank,
full Sha-finiteness and exact leading-formula objective remains active.

## 20. A certified CM derivative, global tame primitives, and the weighted adjoint

**[NEW, independently reviewed deductions and certificate]** All four
constructions have separate PASS reviews and root inspection; the CM
integral bound also has a third audit. The new numerical certificate
was independently reproduced. The full universal BSD goal remains open.

### An actual CM derivative is nonzero and Sha at5 is zero

[Proof](cm-derivative-nonvanishing-attack.md),
[checkpoint](cm-derivative-nonvanishing-checkpoint.md),
[root full review](review-cm-derivative-nonvanishing.md),
[third integral audit](review-cm-derivative-integral-bound.md),
[script](../../compute/scripts/certify_cm39_padic.py),
[exact data](../../compute/data/cm39_padic_derivative_certificate.json).
For E:y²=x³+39x=48672i1, the SAME normalized MTT quadratic coefficient
in T=gamma-1, chi(gamma)=6, now has the certificate

    c2=20 mod25,       v5(c2)=1,       also c2=70 mod125.

The exact rational modular-symbol sums at level3 are A=3540,B=-275,
with alpha=13 mod25. At level4 they are A=46545,B=86450,
with alpha=113 mod125. Their formula is alpha^(-n)(A-alpha^(-1)B).
All100 and500 finite bins were checked by eclib and the independent
fixed-denominator numerical-symbol algorithm. Root reproduced the
full new command with exit0 and separately reconstructed every stored
row, Hensel residue and sum by Python integer/Fraction arithmetic.

The infinite precision is a theorem, not stabilization. Every cusp
a/p^n for p good is equivalent to0. Its image under the actual optimal
map is O because L(E,1)=0; Manin constant1 is verified by
Agashe–Ribet–Stein/Cremona Appendix5.2 at conductor48672<60000.
The negative-discriminant period lattice has real projection Omega/2,
so ALL these symbols are half-integral. The ordinary measure
alpha^(-n)m(a/p^n)-alpha^(-n-1)m(a/p^(n-1)) is therefore integral.
On a level-n bin t(x)-j lies in p^(n-1)Z_p; the quadratic binomial
difference is (t-j)(t+j-1)/2. Thus the error in c2 is p^(n-1)Z_p.
The eclib factor1/2 is explicitly retained, as are the full real
period, unnormalized ray norm18432, a=7 smoothing and Betti vector.

The existing undivided height identity against the non-torsion
P=(3,12), with nonzero local logarithm, proves the ACTUAL
w0=Sh(d_pi+d_barpi) is nonzero at5. Hence at least one ray derivative
is nonzero; neither individual identification, independence nor a
particular nonzero mod5 Kummer reduction is claimed. The reviewed
maximal-minor criterion gives full Selmer corank2 and finite Sha5.

The next integral argument proves the STRONGER conclusion

    Sha(E39/Q)[5-infinity]=0.

At every good split p≥5 for this E, nonanomalousness was proved
uniformly. Its local point completion has formal logarithm lattice
pZ_p. Since log(exp delta0)=k_alpha^(-1) has valuation1, the fixed
exp(delta0) is a primitive integral point. Integral CM splitting,
exact local base change and perfect local duality therefore prove
that iota_p=O_p(e_L0) is a p-UNIT, strengthening its previous nonzero
rational status. This is not an arbitrary local Coleman factorization.

After primary finiteness is established, the exact ordinary Selmer
coefficient triangle T→V→V/T identifies tors H2 of the base integral
cone with FULL primary Sha. Nonanomalous H0((V/T)^-)=0, bad-prime
CM inertia and odd-p real Tate vanishing ensure classical local
conditions with all three coefficients. No integral global duality
sign is assumed; no other primary Sha group is assumed finite.

Put the constant square Selmer matrix in INTEGRAL Smith form.
Its rational nullity is2. The T² coefficient is a unit times
p^s det(B), where p^s is the order of its torsion cokernel and
B is the integral2×2 linear block on the zero rows/columns.
Every other term needs at least three T-factors; no Smith denominator
is inverted. The exact determinant basis and iota_p are units, so
s≤v_p(c2). At5 this gives s≤1. Cassels–Tate alternation on the now
finite5-primary group makes s even, hence zero. The Bockstein is
nondegenerate at5, but no numerical p-adic regulator is asserted.

The SAME argument yields, for every stated good split p with c2,p≠0,

    0≤v_p#Sha[p-infinity]≤2 floor(v_p(c2,p)/2).

The finite algorithm is also uniform. An actual level2/3 expansion,
j=r+pt, gives

    c2,p = alpha^(-2) A2,p + p C_p/(2 alpha^3) modp²,
    C_p=sum_(a,r,t) t(2r-1)m(omega(a)(1+p)^(r+pt)/p³).

The Hecke relation gives B2,p=0, but the weighted carry C_p remains.
At5 A2=-5,C=237 give terms5+15=20 mod25; omitting the carry gives
the WRONG residue5. Root recomputed that addition from the stored
rows. A2≠0 modp, or, when A2 is p-divisible,
alpha A2/p+C_p/2≠0 modp, proves Sha_p=0 by the bound.
Neither test is proved at all primes. Some later finite level being
nonzero is equivalent to c2,p≠0, still an unresolved uniform statement.
CM pairing nonvanishing does not automatically give rank-two
nondegeneracy or a rational kernel ratio. The CM point rank over
Z[i] is two. No all-prime or rational real BSD comparison follows.

### The first global tame primitives exist, with a separate local obstruction

[Proof](heegner-tame-nullhomotopy-attack.md),
[checkpoint](heegner-tame-nullhomotopy-checkpoint.md),
[PASS](review-heegner-tame-nullhomotopy.md).
The input is the ACTUAL cofactor-corrected strict finite Selmer class
x=P_(A,B)(w_k), with old localizations at ell,q zero, and z=d0x.
The original uncorrected BF coefficient is not replaced canonically.
Retain the nonanomalous O5 scope and the extra p∤h_K premise for
independent tame coordinates. To identify the annihilator with d0,
the proof additionally requires SURJECTIVE residual image and the
checked p-unit Manin condition.

The inspected Castella–Sano2601.14504v1 rank-zero formula and
TheoremB give v_p(d0)=t+s, where t is the twist Tamagawa valuation
and p^s=#Sha(E^D)[p-infinity]. Its ordinary case permits conductor
ND². The fixed Euler and real-period conversion factors are units;
the exact d0 remains in the class. In the merely irreducible range,
p^(t+s) is the proved annihilator, with no unproved replacement by d0.

A direct local argument proves unramified norms surjective on E0,
including residue degree divisible by the residue characteristic.
After p^t multiplication, every bad-prime point class has an E0
representative. The old primes were already strict; at p and D the
dual invariant groups vanish, and all real Tate terms vanish.
Thus p^t(a_i cup x) is everywhere locally zero. Finite Poitou–Tate
pairs this kernel perfectly with the everywhere-strict twist group,
a subgroup of finite Sel(E^D) of order at most p^s. Consequently

    d0(a_i cup x)=0 in H2(U,E[p^k] tensor epsilon_K)

in the stated stronger range. The two first equations therefore
have actual continuous global finite-coefficient primitives, without
dividing d0. Finite Galois/etale comparison and cohomological dimension
were checked in Milne II.2.9 and I.4.10, not silently assumed.

The point condition inherited from the REGULAR Shapiro representation
is more restrictive. At its ramified old prime i, its norm polynomial
maps to p^e+p^e(p^e-1)Y_i/2=0 in R[Y_i]/Y_i². Thus the native point
image in the first extension N_i is zero. HOWEVER the kernel of
H1(M_D)→H1(N_i) is the TRANSVERSE line, from H0(M)'s boundary.
It is not the finite line or a requirement that every correction vanish.
This distinction corrected a preliminary interpretation before the proof.

In the additional clean Tamagawa range the allowed correction group is
transverse at i and finite elsewhere. Otherwise the actual preimages
J_i,v are retained. The compact class built from the global cup and
chosen native local primitives is dual to Sel(M_D;J_i,v perpendicular).
Its explicit compact-FIRST Weil cup formula and the signed cone/trace
agree with the authoritative Gysin notes; no sign reversal was inserted
from the order of arguments in a shorthand name.

Even if the classical twist Selmer group is ZERO, in the clean range
this transverse group is R: relaxation gives a graph over the singular
line, and the symmetric hyperbolic local pairing forces graph slope0
because2 is invertible. Thus global nullcochains do not automatically
satisfy the required local point images. The compact obstruction has
not been evaluated or proved nonzero.

The mixed two-cocycle is now defined on the constructed first lifts;
changing them by h_ell,h_q changes it by
-a_ell cup h_q-a_q cup h_ell. Its coset and local restrictions are
explicit. The actual twist Kato class is an available global adjustment
with a retained p-relaxed local defect, not an automatic allowed one.
Moreover adding the ACTUAL top Heegner Shapiro class changes the top
coefficient while preserving the bottom and first coefficients and any
achieved native local conditions. An integral arithmetic comparison must
still select the lift and use the extra complex vanishing. TN-TP5 remains
this native-local/mixed comparison, not the already proved global first
annihilation. No rank-five vanishing is obtained.

### The actual weighted theta adjoint recovers the original mass

[Proof](weighted-theta-adjoint-attack.md),
[checkpoint](weighted-theta-adjoint-checkpoint.md),
[PASS](review-weighted-theta-adjoint.md).
For a rapidly decreasing mean-zero scalar h, removing the zero lattice
vector BEFORE estimating makes H=I_L(h) rapidly decreasing in tau.
The majorant bound q_z(A)≥c||A||²/y² and splitting cusp height at
v^(1/3) prove a polynomial times exp(-cv^(1/3)) bound. Thus the
Petersson pairing against Eisenstein Laurent coefficients is an
ORDINARY convergent integral.

Unfolding selects the actual nonzero isotropic vectors. At prime N
they comprise the signed multiples of the two primitive cusp orbits,
giving2zeta(s)N^(s/2)(E_infinity+E_zero). The Gaussian polynomial
contributes (s-1)Gamma(s/2)/(2pi^(1+s/2)). The source's raw
Du–Yang Eisenstein has leading coefficient TWO, whereas the full
metaplectic-stabilizer seed series has leading ONE. Central action,
the signed primitive-row Poisson calculation and the arithmetic
degree constant independently verify this factor; it is not a guessed
stack degree. The resulting EXACT formula is

    <I_L(h),Ecal_L(bar s)>_3/2 = r_N(s) int h J_N^+(s),
    r_N(s)= -sqrtN/pi² · s(s-1)xi(s).

The bar-s in the second entry gives holomorphic parameter dependence
under the sesquilinear pairing. Absolute unfolding is done first for
Re(s)>2, then continued. This is an adjoint functional on mean-zero
rapid tests, equivalently modulo constants; the opposite pointwise
unregularized theta integral diverges. Nor may one put s=1 into
each isotropic Mellin term before summing its compensating zeta pole.

For the original even F, J_N^+ can be replaced by J_N. Its lower
pairings vanish and r_N(1)=-sqrtN/pi². Hence

    M=-pi²/(2sqrtN) <I_L(F),Ecal_L''(1)>_3/2,
    <I_L(F),Ecal_L''(1)> =3N^(3/2)(N-1) ell L(E,2)/pi^5 ≠0.

This proves that the ACTUAL lift I_L(F) is nonzero. The analytic
weighted-adjoint subproblem is now completed. The old forward j2
lift contained a THIRD Eisenstein derivative through xi's pole;
the new adjoint cancels that pole via s-1 and tests the SECOND
derivative. The formulas use different actual operations and agree.
The generalized composition multiplier is -sqrtN s(s-1)xi(s)²/pi²,
not an inverse on every spectral component.

Arithmetic realization still uses ONLY the reviewed cutoff metric
pairing limit for I_L(F), not a single smooth a(2ReF) or a rational
motivic limit. WTA-389 now needs an actual arithmetic second-derivative
test and forcing operation in the point/K2/Tate determinant line.
The previously missing analytic adjoint should not be retried as open.

### A nonzero secondary Kummer operation and the compact graph cycle

[Proof](secondary-kummer-theta-attack.md),
[checkpoint](secondary-kummer-theta-checkpoint.md),
[PASS](review-secondary-kummer-theta.md).
On the ACTUAL triple universal elliptic family and its nonzero higher
cycle Xi, choose the independently fixed eta unit u and a7-torsion rho.
The frame-independent fiber function
b_u(x)=1+(u-1)(x(sigma)-x(rho))/(x-x(rho)) has values1 at0 and u
at sigma. After an explicit nonempty finite base shrink, its zero/pole
divisor D is smooth, proper of relative dimension2 and disjoint from
A[5]. The excluded2-torsion points are the NONZERO points, whose
x-coordinates are finite. Tate-cusp asymptotics verify nonemptiness.

With Rost's convention partial{uniformizer,a}={abar}, the Kummer
factor goes FIRST. The actual operation is

    {b} cup Xi in H6_M(W minus D,Q4)
      →res_D H5_M(D,Q3) →proper-push H1_M(S_open,Q1).

Its value is EXACTLY {u}. On the first graph it is {b,F_sigma}/2100;
its normed interior tame product is u^2100 because the deleted endpoint
has symbol u^(-2100). The other graphs contribute zero. The result
extends across the removed finite base points as the already given
unit, and rational finite transfer descends it. There is no proper
push from W and no freely selected real normalization.

The canonical regulator pairing against the signed divisor D gives
log|u|. Review narrowed the current domain: use the canonical model
and admissible wavefront representatives, or natural Deligne pullback
of the transverse graph terms. Arbitrary exact current modifications
need not have a defined restriction to D; compactness alone is not
a justification. All Tate and residue shifts were checked against
the primary Rost and KLM boundary conventions.

On the compact surface X0(389)×E there is an actual integral cycle

    Z_u=(Graph_pi,u)-(X×O,u) in CH²(X×E,1).

Its cusp boundary cancels point by point since pi(0)=pi(infinity)=O.
Its specified current regulator contracts against omega_E to
log|u| pi*omega; multiplying by -i/(4pi²c_pi) and differentiating
recovers F dmu, with no cusp atom. This is a current formula, not
a claim that the nonclosed transgression represents scalar cohomology
or proves motivic nonvanishing of Z_u.

The actual elliptic push is (Diagonal,c)-(E×O,c), with
c=Norm_pi(u) constant. Fricke inversion forces c=c^(-1), hence ±1.
The push is2-torsion integrally and zero rationally. Its E-degree-one
part is also Fricke even on X, so the specified odd f-projection kills
it. The unprojected forcing and full radial decoration remain.

Naively multiplying this regulator current by j2 fails the closed
Deligne condition. The explicit residual is
ddc(j2 log|u|)=log|u| ddcj2 plus the two cross derivatives. At infinity
its potential has leading term
pi²(N-1)(N²-1)y²(log y)²/6, with nonzero Laplacian. A product of
j2 with a cusp Dirac mass is not defined by that shorthand. The full
Gamma-completed coefficient retains its lower/pole terms and has the
same leading obstruction. SKT-389 remains a proved correction and
rational arithmetic comparison for this actual radially weighted cycle.

All constructions and five review files are completed. This round made
mathematical progress, including a new independently reproduced primary
Sha vanishing result and a completed analytic comparison. The universal
BSD objective is still active; neither full proof nor counterexample
has been obtained, and there is no repeated external blocker.

## 21. Integral point indices, arithmetic Poisson heights, and relative boundary periods

Date: 2026-09-12. **[NEW, independently reviewed constructions]**
Five proof/checkpoint pairs and five separate review files are complete.
Root inspected the constructions and reviews. No new numerical script
or certificate was run in this round. The preceding CM Sha5 theorem
is retained; full universal BSD remains neither proved nor disproved.

### The actual CM point matrix and a sharper primary index formula

[Proof](cm-uniform-carry-attack.md),
[checkpoint](cm-uniform-carry-checkpoint.md),
[root PASS](review-cm-uniform-carry.md).
For E:y²=x³+39x, keep the full point basis P=(3,12), Q=(27,144),
S=P+Q=(1/4,25/8), the original MTT series, gamma with chi(gamma)=1+p,
g_p=log(1+p), and e_p=(1-alpha^(-1))². This construction covers good
split p>=5; it does not assert nonvanishing at every such p.

The finite measure is an actual augmentation element in Zp[G_n].
Its second augmentation coordinate is c2 modulo p^(n-1).
The carry identity from §20 is retained with all Teichmüller terms:
c2=alpha^(-2)A2,p+p C_p/(2alpha³) mod p². At5 its two terms
are5 and15; ignoring the carry would change the certified answer.

Integral Selmer self-duality gives the exact UCT sequence
0→Ext¹(H²,Zp)→H²→Hom(H¹,Zp)→0. Thus H²_tf maps isomorphically
to the integral dual of H¹, while the finite Ext term is retained.
The point lattice is saturated without assuming finite Sha, since
T_p Sha is torsion-free. Its equality with all H¹ is used only
after the earlier nonvanishing criterion proves rank2 and finiteness.

Define B_p by this integral duality and MINUS the natural Bockstein.
If c2 is nonzero, actual integral Smith reduction and full point
basis changes yield the exact formula

    c2=epsilon_p p^s det(B_p),   s=v_p#Sha[p-infinity],
    (c2)=Fitt^0(Sha[p-infinity]) (det B_p).

The unit epsilon_p retains the determinant basis u(0), local iota,
Smith changes U,V, point change C and duality matrix J:
epsilon_p=(-1)^b iota_p u(0)/
(detU detV (detC)² detJ). It is not set equal to1 or2e_p.
Consequently s=v_p(c2)-v_p(det B_p). All of full primary Sha,
not a selected visible subgroup, occurs here.

There is an actual finite recipe for this point matrix. The SAME
canonical CM sigma series is integral at every good split p:
Sigma(t)=t+(65/4)t^5+O(t^9). Let n_p=8#E(Fp), a p-unit;
then n_pP,n_pQ,n_pS lie in the formal group and in the bad identity
components. Write n_pR=(a_R/d_R²,b_R/d_R³), t_R=-a_Rd_R/b_R.
For precision p^m use U_R=d_R/Sigma_[m+1](t_R), and determine
lambda_p,m(U_R) modulo p^m by

    (1+p)^((p-1)lambda)=U_R^(p-1) modulo p^(m+1).

This equals log_p(U_R)/g_p modulo p^m. The diagonal height values
are q_R=2n_p^(-2)lambda_p,m(U_R), and the off-diagonal entry is
(q_S-q_P-q_Q)/2. The sigma tail loses precisely at most one
power through log/g; the precision is proved. The complete global
denominator is retained. MST's log/p and quadratic -pair/2 are
converted explicitly to the BKS minus-Bockstein normalization.

Thus, for example, a certified e=v_p(c2)>=2 together with
det B_p=0 mod p^(e-1) implies s<=1, hence Sha_p=0 by Cassels
parity. For e<=1 the preceding bound already suffices. Precision
p^(e+1) determines the exact primary order. No all-prime termination
is inferred from these finite tests. At5 the already proved s=0
and e=1 imply v5(det B_5)=1 and v5(Reg_5)=3 for H_p=g_p B_p.
This is a deduction, not a new numerical regulator output.

A fixed finite list of multipliers cannot put a non-torsion point
in the formal group at almost every prime: the denominator of
each fixed multiple has finite support. The actual n_p varies.
This excludes only that proposed finite descent. The remaining
CM-Uniform-Frame requires one rational frame before all completions;
the local ratio c2/(2e_p det B_p) is integral under nonvanishing,
but neither its value1 nor its equality to a common rational scalar
has been proved. Bad and nonsplit primes remain outside this theorem.

### The native Heegner obstruction now has an explicit evaluator

[Proof](heegner-native-pairing-attack.md),
[checkpoint](heegner-native-pairing-checkpoint.md),
[PASS](review-heegner-native-pairing.md).
Retain the original O5 setup and the specified additional clean
range: p does not divide Tam(E), classical Sel_p^k(E^D)=0,
the actual d0 is a unit, and p does not divide h_K where required.
All local finite quotients, including nonfree ones, are kept.

Finite Poitou–Tate duality gives an actual isomorphism
q loc:H¹(U,M_D)→direct-sum Q_v and its unique inverse C.
The sections C_v produce isotropic complementary local lines.
At each old prime the resulting line is the actual transverse one.
For beta_i=-a_i tensor t_i^+, choose the fixed positive Weil frame
so B_i(f,beta_i) is exactly its finite Frobenius coordinate.
There is no inertia factor2; restriction of finite Frobenius
from Q_i to K_i does have degree2.

The p-generator is b_p=d0^(-1)z_D,k from the actual twist Kato
class, with O_p(loc z_D)=d0. Its transport must be
A=u_iota^(-1)iota_* for classes and A^(-dagger)=u_iota iota_*
for the first, point-dual factor. This correction preserves local
Tate duality. The old transverse generator is b_i=C_i(q beta_i).
Writing loc_p b_i=h_i e_p, the coefficient is exactly
h_i=k_alpha log_omegaD(P_i) modulo p^k, with log known modulo
p^(k+1). Global reciprocity gives f_i(loc_i z_D)=-d0 h_i.

For actual native local data tau and a global primitive t, form
delta=tau-loc t, h=C(q delta), t_natural=t+h, and
eta=tau-loc t_natural, now finite at every place. The particular
obstruction is

    R_i=B_i(eta_i,beta_i),
    compact-FIRST pairing(b_i,c_i)=R_i/p^k.

If the singular quotient is free and L=q loc(xi) in any actual
global basis, its exact finite presentation is

    R_i=d_i-r_i L^(-1) qdelta
       =det([[L,qdelta],[r_i,d_i]])/detL.

Here detL is proved a unit. Nonfree quotients use the actual Smith
congruences without dividing a nonunit. The cross-local maps obey
the reciprocity skew-adjoint relation. Adding lambda z_D to a
global primitive changes the old and p terms by equal opposite
amounts, so it cannot tune the native obstruction.

The proposed Bertolini–Darmon universal-norm shortcut fails its
hypotheses for these ACTUAL local groups: at an old ramified prime,
the local point norm cokernel reduces to E(F_(i²))/p^e and its
mod-p^k quotient is R². Moreover b_i is transverse, not finite.
No stronger theorem is inferred from that source. Even if both
R_i vanish, mixed local equations and a global residual remain,
and adding the actual top Heegner class preserves lower data.
NP-TP5 still needs the extra complex vanishing to evaluate the
particular R_i and select the correct mixed/top lift.

### A canonical arithmetic Poisson input reaches the Hodge-height series

[Proof](theta-doubling-arithmetic-attack.md),
[checkpoint](theta-doubling-arithmetic-checkpoint.md),
[PASS, including the additional audit](review-theta-doubling-arithmetic.md).
The actual nonzero I_L(F) has zero holomorphic cusp projection,
by the primary Alfes k=0 kernel identity and proved Fubini bounds.
Thus the inspected Du cusp-only arithmetic inner-product theorem
does not directly apply. Nevertheless the real forcing has an
ACTUAL Bost W1,2 arithmetic class A_F=(0,2h*ReF) on the normal
scheme model of C=X1(5N), of degree12(N-1)=4656 over X0(N).
Normalized coefficientwise theta intersections recover I_L(ReF).
This improves the previous cutoff-only statement by changing to
the justified Sobolev category; it does not restore the withdrawn
smooth GS class. Scalar j1 and j2 have infinite energy even after
subtracting any finite-divisor cusp logarithms.

Actual lattice Poisson summation proves the global bound
int_Y|theta+e0/(2pi)|dmu=O(v^(-1/2)). Exact-mean bounded cutoffs
then extend the weighted adjoint to 0<Re(s)<1. There is a unique
bounded W1,2 solution q_F of ddc q_F=ReF dmu with hyperbolic
mean zero. Explicit cusp potentials O(q log|q|), followed by a
smooth compact Poisson solution, construct it. Fricke symmetry
makes its two cusp constants equal.

Review found and corrected the Poisson SIGN:
ddc J_s=+s(s-1)J_s dmu/(4pi). The resulting identity is

    <I_L(q_F),Ecal_L(bar s)>=-4sqrtN xi(s)M_F(s)/pi.

The source quadratic zero M_F(1+t)=M t²+O(t³) removes the pole.
Independently the exact two-cusp theta tail is
I_L(1)=-volY e0/(2pi)+sqrtN e0/(pi sqrtv)+rapid.
A nonzero common cusp constant q_c would force a pole with
nonzero residue -4a_N(1)q_c sqrtN/pi. Thus q_c=0 and q_F is rapid.
The old weighted-adjoint multiplier and its second-derivative
formula are unchanged.

For H_F^G=I_L(q_F) and the ORIGINAL Du–Yang Hodge-height series,

    R_omega=(Ecal'_L(1)-N logN Ecal_L(1)/(N-1))/(N-1),
    M=-pi/(4sqrtN)<H_F^G,Ecal'_L(1)>
     =-pi(N-1)/(4sqrtN)<H_F^G,R_omega>.

Both series have actual arithmetic-intersection constructions;
A_q=(0,2h*q_F) is a Bost class. These are ordinary convergent
Petersson integrals. The ordinary A_q/Hodge intersection is
zero by mean normalization. Therefore the new operation is not
that ordinary height or an identity theta operator. The genus-two
diagonal/pointwise-Green proposals were BYPASSED, not proved.
The rational point/K2/Tate comparison remains required.

### A genuine relative graph correction, with its cusp data fixed

[Proof](radial-graph-correction-attack.md),
[checkpoint](radial-graph-correction-checkpoint.md),
[PASS](review-radial-graph-correction.md).
On V=X×E, B=({0,infinity})×E, use
D=Graph(pi)-X×O. The difference line bundle is canonically trivial
on both boundary fibers since pi(c)=O; hence it gives an actual
relative motivic Chern class c_D in H_M²(V,B,Q1).

With the canonical elliptic Green function and
G(x,w)=g(w-pi(x))-g(w), ddcG=delta_D-Omega_D.
For a radial scalar a the CORRECT star expression is

    S_a=a delta_D-G ddc a,
    S_a=a Omega_D+partial U+barpartial barU,
    U=i(a barpartial G-G barpartial a)/(4pi).

Its GS Green normalization is2S_a and native Deligne form is
2pi i S_a. The mixed curvature has no vertical two-form;
ddc a wedge Omega_D=0 and p_X,*(S_a wedge omega_E)=a alpha.
The actual logarithmic translation estimates prove global L1
currents and no extra boundary atom, even for j2. A scalar
finite-energy failure therefore does not exclude this construction.

The original nonzero functional is

    P(S)=i/(4pi²c_pi) int_Y p_X,*(S wedge omega_E) wedge barpartial l,
    P(S_a)=int_Y a F dmu,   l=log|u|.

It does NOT descend to an arbitrary absolute Deligne class:
an exact change with fiber primitive b changes it by
-sum_c ord_c(u)b(c)/(4pi c_pi). Actual smooth primitives give
nonzero changes. Cusp data are substantive.

Cauchy solutions for the local mixed coefficients, fixed to zero
on B, supply ordinary smooth relative representatives T_a^rel.
Differences are ordinary relative boundaries. The logarithmic
functional then descends and detects a nonzero real class
C_j2 in H_D³(V,B,R2), with P(C_j2)=M. This is not an arithmetic
Chow limit. The full Gamma/pole terms are retained in the class,
even though the previously proved lower scalar pairings vanish.

There is also a typed rational compact-support cup
v↦p_X*{v} cup c_D in H_M,c³(Y×E,Q2). Its regulator equals
C_log|v| with the actual zero cusp trivializations. EVERY rational
unit on Y has log equal to a rational multiple of l plus a constant.
Fricke parity and int F=0 make the entire scalar-Kummer cup image
pair tozero. This rules out that image, not all rational relative
higher cycles.

### The existing rational beta2 has a nonzero relative boundary period

[Proof](relative-beta2-boundary-attack.md),
[checkpoint](relative-beta2-boundary-checkpoint.md),
[PASS](review-relative-beta2-boundary.md).
The SAME previously constructed beta2 in H_M²(E,Q2), with
R_E(beta2)=L(E,2)/pi, now embeds rationally in the relative group.
Indeed the actual chain (W,u)/(N-1), W={(P,x,P)} in E×X×E,
has boundary Graph(i0)-Graph(i_infinity). This proves equality
of the motive maps in every degree/twist. Projection to E then
shows that the full restriction image is exactly the diagonal.
The relative exact sequence therefore gives an injection

    j_B: H_M²(E,Q2) → H_M³(V,B,Q2),
    beta ↦ partial^+(beta,0).

This is the project positive boundary (0,+beta), opposite the
canonical connecting sign. Integrally only N-1 times the
restriction difference is zero; no denominator is discarded.
The nonzero input beta2 consequently has nonzero relative image
before this new scalar is evaluated. No K2 rank-one theorem is used.

The native K2 form is i eta_K, not2pi i eta_K. The fixed Rost
convention has small-loop integral MINUS2pi log|tame|; it is zero
for the unramified class. Smooth anti-invariant representatives
preserve the real structure. If rho is1 near0 and0 near infinity,
the positive relative boundary is represented in the normalized
degree-three convention by

    S_b2=(d rho wedge eta_K)^(1,1)/(2pi).

With omega1=int_a omega_E>0 and FULL Omega_E=2omega1, exact
fiber and cusp Stokes calculations give

    P(reg j_B(beta2))=(N-1)omega1 L(E,2)/(8pi³ c_pi) !=0,
    M/P(reg j_B(beta2))=-12N c_pi ell_E/omega1
                       =-24N c_pi ell_E/Omega_E.

The named de Rham coefficient omega_E and its period omega1
are retained. This is not an unmarked rational Betti scalar.
Multiplying the boundary evaluation by Reg_E ALONE gives
-(N-1)/(4c_pi) times the target
-Omega_E Reg_E L(E,2)/(4pi³). Multiplying by the full D_pt
period would incorrectly insert another Omega_E.

The point-height determinant is therefore exactly what this
comparison still lacks. Equality of one functional would not
prove equality of relative classes or rationality of the ratio.
An optional compact cup/trace map is a future construction, not
a premise used here. The rational arithmetic comparison and its
integral lattice, PrimeIndex-389, Leading-389, and universal BSD
remain unresolved. The round made progress and encountered no
repeated external blocker.

The completed continuity check covers199 artifacts,756 local artifact
links,nine certificate JSONs and all six certificate/source dependency
hashes. The three Astra/xhigh handles reported completion; no root
execution remains live and no next task has been dispatched. The
manifest was refreshed after the shared synthesis and editorial updates.

## 22. A rational K2 retraction, geometric determinant, and actual isogeny torsors

Date: 2026-09-12. **[NEW, independently reviewed constructions]**
Four constructions and four review files are complete. The point
determinant's additional relative-extension test received a separate
verdict in the same review. Root inspected every proof and review.
The only new calculation was exact rational division-polynomial
arithmetic, independently checked by root and the CM reviewer.
No old certificate or prime scan was rerun. Full BSD remains open.

### The relative cup and compact trace is an actual rational retraction

[Proof](relative-cup-trace-attack.md),
[checkpoint](relative-cup-trace-checkpoint.md),
[root PASS](review-relative-cup-trace.md).
For V=X0(389)×E, B=the two cusp fibers and Y=X minus cusps,
the fixed unit u=389^(-6)Delta(z)/Delta(389z) gives RIGHT cup
followed by the actual compact trace:

    T_u:H_M,c³(Y×E,Q2) → H_M,c⁴(Y×E,Q3) → H_M²(E,Q2).

Smooth purity f^!1=1(1)[2] and the counit f_!f^!→1 type the
nonproper trace. Equivalently extend by zero AFTER the cup into
X×E and use its proper projection. This is in the oriented PLUS
rational motivic category, with the stated regulator compatibility.

Writing e0=partial^+(1,0) in H_M,c¹(Y,Q0), the full boundary
injection is j_B(beta)=e0 external beta. Projection formula reduces
T_u j_B to lambda times the identity on the WHOLE K2(E) group,
where lambda is already an element of End(1)=Q.
In the actual Betti cone e0 has compact representative-d rho.
The clockwise inner boundary and(2pi i)^(-1) trace give

    lambda=(2pi i)^(-1) int_Y -d rho wedge du/u=388,
    T_u j_B=388 id,   R_u=T_u/388,   Pi_B=j_B R_u.

Thus R_u is a rational retraction and Pi_B an idempotent.
Only injectivity of Q→C on this scalar was used. No general
motivic faithfulness or primitive integral splitting at2,97 is assumed.

For the normalized relative form S, native c=2pi iS, the
RIGHT Deligne product and curve trace give the full native one-form

    Theta_u(S)=int_Y [S wedge(partial l-barpartial l)
                       -l(partial S-barpartial S)],  l=log|u|.

The derivative term is retained. Smooth representatives vanish near
both boundary fibers, so products, extension by zero and Stokes are
defined. This is closed and relative-exact changes map to exact forms.
Its exact omega pairing is8pi² i c_pi P(S).

The projective curve has H_D²(E(C),R2)=i H¹(E(C),R).
The arithmetic involution fixes i H¹(E,R)^minus, a REAL
one-dimensional space with the b-period as an isomorphism.
Consequently the prior scalar calculation now determines a FULL
real Deligne identity:

    R_u^D(C_j2)=-12·389 c_pi ell_E/omega1 ·reg(beta2)
              =-24·389 c_pi ell_E/Omega_E ·reg(beta2).

The Gamma-completed coefficient has the same projected real class;
its lower/pole terms were retained before their known scalar
vanishings were used. None is deleted from the unprojected source.
A hypothetical rational relative input would give some rational
K2(E) class, not automatically a rational multiple of beta2:
one-dimensional real realization is not rank one of rational K2.
The coefficient still lacks Reg_E.

### The point determinant is a geometric quadratic conjugation coefficient

[Proof](point-determinant-single-valued-attack.md),
[checkpoint](point-determinant-single-valued-checkpoint.md),
[PASS, including additional §7](review-point-determinant-single-valued.md).
The actual corrected one-motive M=[Z²→J(E,A)] has the previously
fixed finite Kummer corrections and the full point height matrix H.
Use positive puncture loops t_i with periods2pi i, the FULL
support B* of the corrected divisors, and the marked pullback
of H1(E minus A,B*). No uncorrected endpoint set is substituted.

A direct period calculation, rather than a transferred dual-height
sign, constructs the top Deligne lifts e_j^D and gives

    bar(e_j^D)-e_j^D=-(i/pi) sum_i H_ij t_i,
    delta_M(e_j^D)=sum_i H_ij t_i/(2pi),   delta_M²=0.

For the exterior object N=wedge²T_B(M), weights0 through-4 have
ranks1,4,5,4,1. Relative Kunneth realizes it geometrically in the
product pair. Geometric interchange on degree1 cross degree1 is
MINUS tensor swap, so the PLUS geometric projector is the exterior
projector. Its denominator2 is retained. The integral map
x wedge y→x tensor y-y tensor x identifies the invariant lattice;
using this on both top and bottom frames loses no factor2.

The canonical extreme coefficients are

    psi(delta_N e_N)=0,
    psi(delta_N² e_N)=Reg_E/(2pi²),
    psi(bar e_N)=-Reg_E/pi².

Both standard framed scalar heights inspected in
Burgos Gil–Goswami–Pearlstein2410.17167v3 are ZERO:
one takes the imaginary part, the other the linear delta coefficient.
The real quadratic coefficient survives and gives Reg_E after its
fixed2pi² normalization. Delta/projections are canonical Hodge
operations, not asserted rational morphisms.

The SAME rational K2 cycle beta2 supplies a geometric rational
extension B_beta with bottomH¹(E,Q2), by actual support localization.
On N tensor B_beta the bottom weight-7 conjugation vector is
-Reg_E/pi² times1(2)_B tensor U_beta. The full period, retaining
the actual real cycle2a and ordinary inverse Tate comparison, is
-Omega_E Reg_E L(E,2)/(4pi³). No extra Omega_E is introduced.

The additional comparison test explains why a literal MHS map
from the relative class cannot supply this determinant.
For the actual proper pair, D=H²(V,B,R2) has only weights-3,-2.
H³(V,B,R2) has negative weights-2,-1, so its realF0 term iszero.
The relative Deligne cone gives
H_D³(V,B,R2)=Ext¹_R-MHS(R0,D). Every resulting extension B_c
has weights0,-2,-3 and delta_Bc²=0.

By contrast delta_N² is nonzero on top and kills W-1.
On N tensor B_beta, delta³=3delta_N² tensor delta_beta also
has nonzero top value and kills W-1. Naturality therefore
forbids a nonzero-top MHS map from B_c to either target.
The inverse Tate twist raises the target top to4; twisting both
sides preserves the nilpotence obstruction.

This excludes only those literal framed transports. It does not
exclude rational motivic lifts, different coefficient extensions,
secondary arithmetic operations, or BSD. PD-389 now requires an
actual construction beyond this tested ordinary MHS map.

### The native Heegner scalar is a classical isogeny torsor pairing

[Proof](heegner-native-height-comparison.md),
[checkpoint](heegner-native-height-checkpoint.md),
[root PASS](review-heegner-native-height.md).
Keep the exact O5/cofactor/native setup, n=p^k, dihedral F/Q of
degree2p^e, and all clean/nonclean scope. Let A=Res_(F/Q)E.
The ACTUAL regular-module quotient A[n]→N_i gives B=A/ker(rho),
and multiplication[n] descends to psi:B→A with kernel N_i.
Quotient by its M_D subgroup to obtain B→C→A, with kernels
M_D and E[n], respectively.

Naturality of Kummer maps identifies the native local point image
with the psi-isogeny condition. Its exact preimage is the psi1
condition and its image is the psi2 condition. These kernel
equalities preserve H0 terms; the zero old native image can have
the nonzero transverse preimage. Dual isogeny local conditions
are their exact Tate annihilators.

The actual input z and test b_i give torsors xi_i(z) in Sha(C)
and upsilon_i in Sha(C^dual). Morgan–Smith2103.08530v2,
Definition3.2 and §6.1, gives, with the fixed compact-FIRST frame,

    CT_C(xi_i(z),upsilon_i)=-R_i(z)/p^k.

The sign is GLOBAL minus NATIVE LOCAL in its cochain definition.
No finite Sha hypothesis is used. Quadratic restriction of both
classes multiplies the pairing by2; inertia gains no factor2.
The actual d0, point-dual transport and separate top-Heegner sign
are retained.

The plus augmentation equals HALF the norm on finite coefficients.
Thus C=A/P0[n], where P0=ker Norm is connected.
Weil adjunction and non-CM End_F(E)=Z prove
Hom_Q(E,C)=Z j0 with psi2 j0 equal to the diagonal E→A.
Any such map whose E[n] image lies in ker psi2 kills E[n].
Hence the marked finite inclusion cannot extend to a nonzero
elliptic homomorphism, even with prime-to-p denominators.
An integral Kato class does not acquire a divisible Sha(C) image
by invoking that nonexistent map.

In the SEPARATE point subcase z=Kum_n(P), the exact formula is

    xi_i(z)=-j_P partial_Norm(2P).

Only the pushed torsor is locally trivial. Its native local
conditions are2P∈Norm A(Q_v)+nE(Q_v), and xi_i=0 is equivalent
to the GLOBAL congruence. The norm torsor before push need not
belong to Sha(P0); the actual Kato input is not assumed a point.

The finite tame character cannot lift to a Z_p character, by
(i²-1)chi(sigma)=0 while a_i(sigma)=-1 modn.
Howard's and the inspected2026 derived-height comparison therefore
do not directly supply the missing complex-derivative identity.
Artin formalism retains the two one-dimensional factors and
multiplicity2 for each nontrivial induced dihedral representation.
The extra untwisted zero has not annihilated these specified torsors.
Mixed/top Heegner selection remains after hypothetical first vanishing.

### Actual CM division torsors and the surviving cubical quantity

[Proof](cm-symbol-point-reciprocity-attack.md),
[checkpoint](cm-symbol-point-reciprocity-checkpoint.md),
[PASS](review-cm-symbol-point-reciprocity.md).
For E:y²=x³+39x, F_m=K(f p^m), and actual compatible division
points P_m,Q_m, CM reciprocity/CRT gives the FULL split Cartan
over F0. Conjugation and multiplication by i give the full
O_K tensorZp point basis P,Q. A central homothety-1 kills H1
of the ray group; inflation/Kummer injectivity, both Cartan
components and Nakayama prove

    Gal(F_m(P_m,Q_m)/F_m)=E[p^m]².

No finite Sha premise is used. Kato's exact theta norm, including
the twelfth power and constant1, then gives for R=P,Q,P+Q,

    u_R,m=Theta_a(tau_m+R_m),  w_R=Theta_a(tau0+R),
    Norm_(M_m/F_m)u_R,m=w_R^(p^(2m)),
    Norm_(M_(m+1)/M_m)u_R,m+1=u_R,m^(p^4).

The first power is the unused point-direction multiplicity; the
second is the tower multiplicity. A fixed finite S-unit boundary
is proved from the actual divisor and reductions, including residue
characteristic p. It is not a finite BSD exception theorem.

Full joint transfer to the original CM-twisted finite coefficients
iszero by the p^(2m) power. Single-point transfer has no such
power but is alsozero: the homothety fixes w_R and the cyclotomic
layer while acting as-1 on rho. No smoothing unit repairs it.

The explicit norm root r=w_R^(p^(2m-k)) defines an ACTUAL finite
norm-torus torsor by v^(p^k)=u_R,m and Norm(v)=r.
It retains a specified trivialization and is not asserted zero.
After restricting scalars, the tower norm lands in the p^4-POWER
torsor, not the unmodified one. Its first point augmentation is
zero by exact cocycle sums in the unused translation direction.
The coefficient module retains its permutation kernel and Tate
factor; it is not identified with T_pi.

A full torsion-fiber cubical norm gives the actual nonconstant
rational function

    C_a(Z;P,Q)=Theta_a(Z+P+Q)Theta_a(Z)/
                         (Theta_a(Z+P)Theta_a(Z+Q)).

Its leading coefficient at O is
L_a=(psi_a(P)psi_a(Q)/(a psi_a(P+Q)))^12.
The new exact rational values for a=5,7 are in the proof and
were independently reproduced twice. Their reduced numerators
and denominators both have absolute value greater than1.
Since rational ker(log_p) consists of signed p-powers,
log_p L_5 and log_p L_7 are nonzero at EVERY odd prime.

This auxiliary nonvanishing is not c2,p nonvanishing.
The sigma division identity makes C_a an isogeny-smoothing
defect of the Poincare section. With X=n_pP,Y=n_pQ and
D(X,Y)=d(X+Y)/(d(X)d(Y)), exact canonical-height bilinearity gives

    log_p[D(aX,aY)/D(X,Y)^(a²)]
                    =log_p[psi_a(X+Y)/(psi_a(X)psi_a(Y))].

Thus the finite-corrected cubical leading height component is
12a² h(P,Q)-12h(aP,aQ)=0. The nonzero raw logarithm and
zero corrected component are distinct. The Kato smoothing unit
acts on a different module and does not invert this zero.

CM-Symbol-Point still requires an operation retaining the original
ray branch and appropriate relative point data, uniform successful
coefficient/index control, and one rational frame before separate
completions. The exact previous Smith-frame unit is unchanged.
Bad/nonsplit primes and the universal BSD obligations remain.
This round is progress, with no repeated external blocker.

The completed continuity check verified211 artifacts,804 local artifact
links,nine current certificate JSONs and all six certificate/source
dependency hashes. The three Astra/xhigh research handles reported
completion. No next task is dispatched; the current next plan starts
from the new literal-map, norm and torsor results. The manifest was
refreshed after final editorial and shared synthesis updates.

## 23. Finite Poisson periods, motivic coefficients, and integral lifting tests

Date: 2026-09-13. **[NEW, independently reviewed constructions]**
Four constructions and four review files are complete. The marked-family
proof has a separate additional audit for its motivic object and real
lift. Root read every proof and review and checked the new exact
arithmetic. No old certificate, prime scan or period computation was
rerun. Full universal BSD is still neither proved nor disproved.

### The canonical Poisson input has an exact finite iterated-period formula

[Proof](poisson-iterated-source-attack.md),
[checkpoint](poisson-iterated-source-checkpoint.md),
[PASS](review-poisson-iterated-source.md).
Keep alpha=pi*omega_E=c_pi(2pi i)f dz, theta=dlogu, the full eta
unit u, and l=log|u|. The reviewed q_F and its zero cusp values
are inputs. The new source uses the reduced finite fiber u=2,
a nonempty finite étale Q-scheme, with all conjugate basepoints.
For distinct endpoints b,z the actual relative pair

    (Y², {b}×Y unionDelta_Y unionY×{z})

realizes the length-two path module. When endpoints coincide, the
constant-line distinction is retained. Looijenga2403.03748v2 and
Hain math/0109204v2 verify the geometric Betti/de Rham/Hodge source.
EARLIEST-FIRST order is fixed by the triangle(gamma(s),gamma(t)),
ds wedge dt, s<=t; reversed source indexing supplies no guessed sign.

A rational second-kind de Rham basis of H¹(X) with poles only
at infinity, order<=2g+1, exists by the RR dimension3g−g=2g.
The full period matrix specifies rho with conjugate alpha periods.
Its coefficients are comparison periods, not asserted rational.
For A=∫alpha, Atilde=∫rho and L=log2+∫theta, barA−Atilde is
single-valued. The explicit expression

    Phi_b=Re[2l A-I_(alpha,theta)-I_(rho,theta)]

has curvature4pi c_pi ReF dmu. Its complete real monodromy is
the CONSTANT additive character

    C_gamma=2log2 Re(a_gamma)
                  −Re(I_(alpha,theta)(gamma)+I_(rho,theta)(gamma)).

The z-dependent remainder is imaginary. The character is not set
tozero. At a cusp, its singular primitive has derivative
pp[(barA_c−Atilde(q_c))theta]. After subtracting that primitive,
the remainder is single-valued: its only remaining logarithm is
a_c(q_c)log|q_c|², not an argument-of-q branch.

The existing q_F proves compatibility of these independently
specified principal parts, so a finite rational RR system with
those complex coefficients constructs xi_b. No value or period
of q_F chooses it. A unique holomorphic differential eta_b then
cancels the remaining compact monodromy, using the invertible
FULL-genus matrix[ReP_hol,−ImP_hol]. Consequently

    U_b=Phi_b−Re∫(xi_b+eta_b),
    q_F(z)=(U_b(z)−U_b(infinity))/(4pi c_pi).

All poles/logs are removed before taking the finite cusp limit.
Bounded harmonic uniqueness proves equality and choice independence.
This is a finite formula with length<=2 variable path words and
explicit period products/comparison matrices. It is not one rational
linear combination or a rational motivic morphism by definition.
The full-genus correction and real normalization remain substantive
in the arithmetic comparison PI-389.

### A moving marked family retains the point determinant before projection

[Proof](marked-coefficient-extension-attack.md),
[checkpoint](marked-coefficient-extension-checkpoint.md),
[PASS with additional §§9–10 audit](review-marked-coefficient-extension.md).
Translate the FULL corrected point divisors Z_j by x on E while
keeping A={O,P,Q} fixed. On the explicit complement S_E of all
collisions with A, their generalized-Jacobian markings define an
actual rational one-motive family. Pull back by x=pi(z).
The new boundary Sigma is interior, and both original cusp fibers
remain the old corrected one-motive M0.

With the chord/vertical Miller function m_(A,x), the actual function

    F_j(x,w)=m_(R,x)(w)/m_(R+P_j,x)(w) ·h_j(w−x)/h_j(w)

has divisor T_xZ_j−Z_j in w. The torus coordinates
a_ij(x)=F_j(x,P_i)/F_j(x,O) give the marking equality, have
a_ij(O)=1, and satisfy

    div a_ij=sum_Z n_(j,Z)([P_i−Z]−[−Z]).

The NEW exact evaluations of h_j at S and T were independently
checked. They give pole orders−2 at both R and−R, hence at x=−R

    ord(a_ij)=[[4,3],[3,4]],   determinant7.

The actual rational de Rham connection is
nabla e_j=-sum_i dlog(a_ij∘pi)t_i, with the constant M0 comparison
and all2pi i factors retained. Its archimedean Deligne height block
is H(x)=H+log|a(x)|. For rational x the added finite symbols are
v_p(a_ij(x))logp; the product formula keeps the GLOBAL full height
matrix H fixed. The moving archimedean determinant is not silently
substituted for the global regulator.

The exterior family W and W tensor B_beta retain the quadratic
and cubic coefficients, with det H(x) in the exact formulas.
At a point over−R of ramification e, exterior logarithmic monodromy
has square14e² on the top-to-bottom frame, while T−1 has bottom
coefficient7e². There is no invariant top lift there.
The actual derived boundary complex[W→(T−1)W] retains invariants
AND coinvariants: its rational Jordan blocks are J3 plus fourJ2
plus fourJ1, and both local cohomology dimensions are9.
No integral division by7 or a Sha interpretation is inferred.

The graph/Poincare bundle has restriction O_E(pi(s)−O) at each
new fiber. Above−R this is nontorsion and nontrivial after every
field extension. Thus zero trivializations at all new points do
not define a relative Picard lift. The actual tuple of boundary
line bundles is retained in the Picard restriction fiber.

Two additional constructions close the next substeps.

First, in rational Beilinson motives over S, let p be the constant
punctured curve and q its finite étale moving support. Define

    C_rel=Fib(p_*1→q_*1),  A_B=Cofib(1→q_*1),
    V_all=(C_rel[1])^vee,
    V_marked=Fib(V_all plus1²→A_B^vee).

The Artin projector is1−(1/b)unit·trace, with all residue degrees.
The positive divisor marking is checked from the actual cone:
beta→(0,−beta) pairs with(gamma,−Z) as+Z(beta).
Localization with its(-1)[-2] puncture term proves dualizability
of these SPECIFIC motives. No motivic t-structure or general
rigidity of constructible motives over S is assumed.

The rational antisymmetric tensor projector on V_marked gives
W_mot and its actual top map to1; the image generator
e1 tensor e2−e2 tensor e1 maps to1. The raw projector has half
that generator. The shift and previous PLUS geometric interchange
are compatible, with the integral frames on both ends retained.
Its fiber F_mot realizes the lower coefficient. Actual pushforward
and relative fibers then give the motivic coefficient triangle.
CD2019 and Tubach2407.02256v3 supply the geometric realizations;
the Hodge statement is applied after base change to C, without
an assumed arithmetic-MHM category.

Second, the REAL lifting obstruction O_W(c_S) is ZERO.
The noncompact pair(S,two original cusps) has relative cohomology
concentrated in degree1 for every local system. Hence H¹(W_C)
surjects onto H¹(C). Product Kunneth with the test E gives the
required surjection in complex degree2.
The original proper Deligne class is a_D(w) by the previously
proved proper-pair Ext theorem. Restrict w, lift it through that
surjection, and apply natural a_D. This constructs a real lift.
It does not rely merely on ordinary Betti-zero shorthand or on
an unproved strictness theorem for nonproper coefficients.

The real lift is not canonically selected and is not proved
motivic. The exact rational input, its motivic degree-four
obstruction, compatible added boundary, and point/K2/Tate
comparison remain MCE-389. The coefficient object and real
existence should no longer be treated as open.

### The Prym quotient has an exact integral one-step obstruction

[Proof](heegner-prym-norm-attack.md),
[checkpoint](heegner-prym-norm-checkpoint.md),
[root PASS](review-heegner-prym-norm.md).
Use the reflection-fixed field L=F^<c>, degree p^e over Q.
Restriction and norm for F/L have composite2, so A^+=Res_(L/Q)E
realizes the SAME marked native sequence and its exact local
conditions. Its smaller isogeny quotient C^+ has the same
Cassels–Tate value−R_i(z)/p^k. The maps of torsors use the
contragredient dual, and the norm on A^+ is unhalved.
The E^D constituent is absent; each nontrivial dihedral induced
constituent occurs once. This does not make their torsors zero.

For n=p^k, let Lambda=Zp[Gal(F/Q)/<c>], Lambda0=ker aug.
The ACTUAL lattice is
T_pC^+=T_pE tensor Lambda_C with Lambda_C=Lambda+(1/n)Lambda0.
Its exact sequence and connecting class are

    0→T tensorLambda_C --n→ T tensorLambda →E[n]→0,
    epsilon_C(g)=(g e_H−e_H)/n,
    H¹(Gal(F/Q),Lambda_C)=Z/n, generated byepsilon_C.

Shapiro and the augmentation p^e of the invariant norm vector
prove its full order. The marked vector e_H modulo n has NO
invariant lift modulo pn. Full inherited torsion image and
disjointness from the dihedral field, followed by a direct matrix
centralizer calculation, rule out EVERY equivariant map
E[p^(k+1)]→C^+[p^(k+1)] reducing to that marked inclusion.

For the particular finite input z, the global Bockstein is the
actual cochain

    epsilon_C(g) tensor g tilde z(h)+e_H tensor dtilde z(g,h)/n.

Only its sum is asserted closed. For the original cofactor input,
beta_E(z) retains the fixed A,B Bocksteins; only beta_E(w_k)=0
follows from the integral Kato class. With an additional integral
lift w_z it becomes epsilon_C cup w_z, whose particular value
has not been proved zero OR nonzero.

Vanishing of this global class is equivalent to a cohomological
norm preimage from L. Point-local conditions remain additional.
The obvious restricted Kato class has norm p^e w0, whose finite
reduction iszero; no division byp^e is made.
In the separate point subcase the global norm congruence is
exactly the class in

    Hhat^0(Gal(F/K),E(F) tensorZp)^(c=+) /n.

This is the actual Mordell–Weil norm lattice, not an abstract model.
It is killed byp^e. A selected point for the original input and
annihilation of its class remain unproved, as do the particular
CT orthogonality and later mixed/top Heegner selection.

### Actual CM coefficient cones and all fixed point jets

[Proof](cm-derived-unsmoothing-attack.md),
[checkpoint](cm-derived-unsmoothing-checkpoint.md),
[PASS](review-cm-derived-unsmoothing.md).
The single-point division torsor has the actual coefficient sequence

    0→I_(R,m,k) tensorT_pi/p^k
      →(Z/p^k)[Y_(R,m)] tensorT_pi/p^k→T_pi/p^k→0.

The theta Kummer class uses its original rho vector, unnormalized
corestriction and old smoothing unit. Its augmentation iszero by
the already proved homothety transfer. H0(K_n,T_pi/p^k)=0
therefore gives a UNIQUE integral lift eta in the augmentation
kernel. In a chosen origin the first point moment is
A1(g)−g(v) tensor kappa_(p^k)(R)(g), with v=−augA(h)/2;
no adjustable primitive or log(a) is divided.

The actual single-point tower law is
pi_(m+1,m) eta_(m+1)=p² eta_m.
For any fixed precision k and jet order d, set

    r>=max(n+1,k+floor(log_p d)),
    m>=r+ceil(k/2).

The binomial valuation r−v_p(j) makes the actual truncated
coefficient jets stable at level r. The retained p^(2(m−r))
then proves that eta_m has ZERO image in every such fixed jet
over the FULL Z/p^k. The whole relative class and operations
of growing order or different normalization are not set tozero.

Modulo p, replication into the joint norm-root object multiplies
by the unused rank-two norm X^(p^m−1)Y^(p^m−1), in degree
D_m=2(p^m−1). The original rho branch kills its leading term;
the unique next lift is the replicated eta in degreeD_m+1.
Thus the theorem tests genuinely higher joint layers as well.
The Weil contraction has its actual Kummer H¹(mu_p) target,
not T_pi.

There are actual rational norm-compatible alternatives before
the rho twist: p^(-2m) times the single-point Kummer class and
p^(-4m) times the joint one. Their indicated Tate lattices have
unbounded denominators. No assertion of impossibility of bounded
representatives, integral Iwasawa membership or full-character
evaluation is made. Tensoring a rational Kummer extension with
rho changes its quotient endpoint to rho, not Qp.

A separate nonzero higher class uses the ALREADY fixed rational
cube coefficient L_a as a constant unit with specified norm root.
The new integer-valuation check gives v_a(L_a)=−12, for a5,7.
Both ray and point-division fields are unramified at a!=p.
Thus this actual relative class has EXACT order p^k uniformly.
Its mod-p coefficient first appears in degree4(p^m−1), with
nonzero tame residue−12 times the norm vector at the good prime a.
The original rho-twisted transfer kills it. Its genuine
nonvanishing therefore is not ordinary Selmer nonvanishing,
c2,p nonvanishing, or the unsmoothed BSD comparison.

The original primitive-ray comparison, adequate integral
normalization, all-prime index/nonvanishing control and common
rational frame remain open. The full previous epsilon_p,
local iota, determinant and period factors are unchanged.
This round is progress, with no repeated external blocker.

The final continuity check verified223 artifacts,852 local artifact
links,nine certificate JSONs and all six certificate/source dependency
hashes. All three Astra/xhigh research handles reported completion.
No next task is dispatched and no root process remains live. The
manifest was refreshed after the final reviewed synthesis.

## 24. Canonical Hodge framing and particular arithmetic obstruction tests

Date:2026-09-13. COMPLETE: four core constructions, two additional
constructions and seven separate review records, including the new
arithmetic reproduction and its sharper local consequence.
All research handles remain GPT-6 Astra/xhigh. Full universal BSD remains
active and unresolved. The ledger23 completion statement above is historical.
See the completed-round checkpoint in research-state.md for restart routes.

### Reviewed rational boundary obstruction and eliminated Tate component

[Proof](marked-rational-boundary-lift-attack.md),
[checkpoint](marked-rational-boundary-lift-checkpoint.md),
[root PASS](review-marked-rational-boundary-lift.md), at mathematical
SHA2560da2757a7888be8e5de802893bb2670904f538c9a9f1b398d476aacf2eb043f2.

The actual coefficient connecting class of the known rational boundary
input is -j_B^+(epsilon0 tensor beta2,0). Its first exterior component is
eta1 tensor e2-eta2 tensor e1, with no extra factor2 in the matched
alternating frames. Its abelian projection is constant, represented by
(P-O)×beta2 and -(Q-O)×beta2 in CH³(E×E,2)_Q. The explicit rational
chain(h_j/m_(R,P_j))×z_beta removes the proper principal-divisor correction
but does not trivialize the punctured coefficient or the products.

The symbols{u,a_ij∘pi} extend uniquely rationally over the old cusps,
where their residues are1. At added s their fixed Rost residue is
u(s)^(-ord_s a_ij); over-R it is the negative ramified [[4,3],[3,4]]
Kummer matrix. Their finite transfer iszero by Norm_pi(u)=±1.

Opening at Sigma can kill a proper relative class through the actual
Gysin image H_M²(Sigma×E,D1). The compact RIGHT-cup trace has boundary
sign(-1)^r: it is -388 on the degree3 chi_D. Hence it sends the actual
obstruction -j_B chi_D to+388 chi_D. A full lift forces the necessary
relation388chi_D=sum_s Tr(zeta_s RIGHT-CUPu(s)), with zeta representing
the proper projected obstruction. Entire-fiber flat-pullback patterns
zeta_s=e_s Res xi_x contributezero by the same exact norm. No injection
after opening, arbitrary zero boundary frame, or universal correction
vanishing is inferred.

Finally the point and beta2 classes both lie in h1_coho(E). The actual
motivic identity Sym²(h1_coho)=Q(-1)[-2] makes their geometric PLUS
projected group H_M²(Q,Q2)=0. Weibel's DIRECT-SUM tame localization
and K2(Z)=Z/2 justify this rational vanishing. The remaining geometric
MINUS summand realizes ordinary rank-three Sym²H¹, by the Koszul sign.
Its class and the full motivic obstruction remain unresolved.

### Reviewed canonical Poisson Hodge invariant

Root's [Poisson Hodge framing](poisson-hodge-framing-attack.md),
[checkpoint](poisson-hodge-framing-checkpoint.md) and
[higher's PASS](review-poisson-hodge-framing.md) are complete in all seven
sections at mathematical revision8bd4db85c819e1527cb06589b2261c3d5f0973d3f9c3afe2b4ff80a4228fd210.
Root read the full independent audit. No mathematical correction was needed.

The COMPLEX loop character G=I_(rho,theta)+bar I_(alpha,theta) is additive
by the imaginary theta periods. Its cusp values are -2pi i Res s_c,
so the principal-part compatibility follows without prior q_F existence.
Lambda=G+[xi] is compact, and the old full-genus correction is exactly
eta=2log2 alpha-Lambda10-bar Lambda01.

The actual rational length-two path module has kernel H1(Y) tensor².
The ordered map a tensorb->pi_*a tensoru_*b pushes it out to a rational
MHS V with weights0,-1,-2,-3 and bottom H1(E)(1). The normalized cusp
loop gamma0/388 supplies its rational Tate splitting. The central canonical
dual covectors are I_(alpha,theta) in I^(2,1), and
I_(rho,theta)+int xi-int Lambda10 in I^(1,2). The latter's F1 status
uses the ACTUAL smooth-log correction xi-v theta, with
d(xi-v theta)=-bar alpha wedge theta. The possible weight-zero path
constant is retained in the exact Deligne formula.

The canonical real compact lift and top I00 lift give, with delta²=0,
pi_-3 delta eD=(bar vK-vK)/(2i). The declared central comparison is
2pi i ell_omega, and its conjugate carries the minus Tate sign.
The exact result is h=Re ell_omega(pi_-3 delta eD)=-U/(4pi), hence
q_F=-(h-h(infinity))/c_pi. The infinity term is the proved finite LIMIT.
This is a canonical REAL operation on an actual rational realization,
not a rational morphism or the missing BSD arithmetic comparison.

### Reviewed asymmetric CM source and the unsmoothed proper point line

[Proof](cm-asymmetric-ray-attack.md), [checkpoint](cm-asymmetric-ray-checkpoint.md),
[uniform PASS](review-cm-asymmetric-ray.md), at mathematical revision
7a9904d53c63062f29439b83b278ec28e0d6891b2aba08580268e815188804ed.
Root read the full proof and review. The sole scope repair was excluding
p from the ordinary etale tame-residue interpretation; valuations stayed fixed.

For [pi^m]R_pi,m=R, the actual point field over F_m has degreep^m and
Norm Theta_a(tau_m+R_pi,m)=Theta_a(beta_m+R), with
beta_m=Omega_infinity/(f0 barpi^m). The complete transfer still has
the exact factor(p-1)p^(m-1-n), hence iszero modp^k for m>=n+k+1.
The directly defined smaller-field class over B_m K_n avoids this
factor, but satisfies Z_(m+1)(R)=Z_m([barpi]R) and is a cyclotomic
restriction from K; its cyclotomic norm is multiplicationp.

The full asymmetric point-field step has degreep³; its theta-argument
orbit has sizep² and multiplicityp. The iterated norm retains the
point endomorphism [barpi^(m-r)] and the factorp^(m-r). This gives
the NEW POINT-jet bound r>=max(n+1,k+floorlog_p d), m>=r+k.
The translation group has orderp^r, distinct from the normalized ray
generator's orderp^(r-1). The pi-isogeny Kummer cocycle has the actual
barpi^k unit relative to the pi-projected[p^k] Kummer convention;
its first tensor line is isotropic for the Weil pairing.

The h-odd ratio is not a root of unity if
(p-1)p^(m-1)>24(a²-1), by the exact primitive orbit and function degree.
The bottom primitive norm has its nonprimitive denominator in(17).
Neither fact is promoted to selected-character specialization nonvanishing.

On U_m=E minus union_g(E[a]-g beta_m), the ACTUAL selected-rho theta
class has exact orderp^k. Its positive valuation residues after the
original smoothing are (a²-1)/(a²-u_a) at -g beta_m and
-1/(a²-u_a) at the other a-torsion translates, timesg(t_rho).
Their support cosets are disjoint and the coefficients are p-units.
Subtracting the value at O gives a unique relative class D_m,k.
It satisfies D_(m+1,k)=[barpi]^*D_(m,k) on the actual pointed opens.

Relative Hochschild-Serre identifies H1(E_Kn,O;T_k) with the integral
pi-to-pi endomorphism line A_k, generated by the actual universal[p^k]
point Kummer class K_pi,k. The original residues forbid a direct proper
extension. Their boundary lifts form a torsor for that line; all norm/
coefficient-compatible choices are exactly
Xi_m,k=D_m,k-barpi^m(c modp^k)K_pi,k, for onec inZp.
The original scalar smoothing is not the inverse of the actual point
operator S_b=b²-u_b[u_b]^*. Its two u_b factors make it zero on the
proper point line. No c has been selected to obtain a desired coefficient.

At pi, [barpi] has a unique integral formal inverse. Thus
U_m(R)=Theta_a(beta_m+[barpi]^-mR)/Theta_a(beta_m)
is a genuine norm-compatible principal-unit family in the FULL semilocal
unramified algebra. Its original-rho Kummer transfer gives an integral
local finite class. At the old points n_pP,n_pQ,n_p(P+Q), full opposite
Kummer degreep^m and degree12(a²-1) of Theta prove its values are not
inB_m whenp^m>12(a²-1). This proves nontriviality of the unit family,
not of its selected transfer. The local inverse is not a global ray
section; at the opposite place it is not a formal unit inverse.
Arithmetic evaluation boundaries are finite at each level but no uniform
set is proved. Original global Selmer/c2 and rational frame comparison remain.

### Reviewed cofactor lifts and the actual native scalar factorization

[Proof](heegner-cofactor-lift-attack.md), [checkpoint](heegner-cofactor-lift-checkpoint.md),
[odd PASS](review-heegner-cofactor-lift.md), at repaired mathematical
revision1069acaa79900311139625292de131d1e4d380f768f6d9464cd43d42c995150d.
Root read the full proof/review and directly inspected the source repair.

The exact intrinsic defect of an integral POINT-LOCAL lift is the
canonical quotient Sel_(p^k)/(T_p Sel_(p∞)/p^k)=F_E[p^k], where
F_E=Sel_(p∞)/Div is finite. This does not assert full Sha finiteness.
For fixed z=d0(Dw_k-aA-bB), its defect is -d0(a deltaA+b deltaB).
The actual integral Kato class removes only the w_k defect.

If the actual two-prime kappa has orderp^s in coefficientp^k, c=k-s,
then p^c F_E=0. The proof uses Kim's SAME modified-Selmer indices:
a_j^+=M_(2j+1)-M_(2j+2) and the second-line positivity
M2-M3=a_3^-≥0, with M2≤c by reduction/order. The independent audit
removed an unjustified appeal to monotonicity for BCGS's ambient-H1
indices. No identification of the two filtrations or unknown total
opposite-sign order is now needed.

The explicit exponent r=max(c-v_p(d0)-min(v_R(a),v_R(b)),0) kills
the PARTICULAR defect, and the formula in§3 constructs a point-local
integral lift of exactlyp^r z. No nonunit is canceled to obtain z.
If kappa is primitive, F_E=0 and all FIXED A,B,z have integral lifts,
with possible divisible Sha directions retained. Their particular
Prym cup epsilon_C cup w_z is independent of lift choices because
p^k epsilon_C=0; its zero remains unproved.

The ACTUAL thick Shapiro module R[X_i,X_j]/(X_i³,X_j²), with logarithmic
coordinates and inverse Artin action, gives a UNIQUE global lift of
kappa in the idealX_iX_j. Its own-prime localization iszero; the
other-prime transverse top defect is t_(i;j). The one-prime cubic
module constructs eta_i from the quadratic moment(1/2)sum_g j_i(g)²g y_i.
Restriction GLOBALLY to H_i makes X_i² extraction equivariant and its
preimage unique. Only then is the class localized at j, avoiding the
noninjective local-restriction shortcut.

Howard's actual point norm/congruence and division cofactor give
t_(i;j)=-a_j^+(eta_i), with the K-Frobenius square, fixed beta_j frame
and rational finite-coordinate factor2 retained. Correcting by the
existing b_j yields R_i(kappa)=-a_j^+(eta_i)G_ij.
In the primitive clean range, the unchanged z=alpha_z kappa therefore
satisfies R_i(z)=-alpha_z a_j^+(eta_i)G_ij. All d0,A,B and native
duality signs remain. Nonprimitive z is not declared cyclic and the
nonclean local groups are not discarded. Extra complex vanishing has
not been proved to kill this particular product or its later mixed/top
selection. These are still the actual Cofactor-TP5 targets.

The two additional reviewed steps immediately below are complete.
Root's new numerical §6 has now passed its separate audit by higher,
including independent exact reproduction; its result is recorded below.
Exact checkpoints and restart routes are in research-state.md.

No old certificate or prime scan was rerun. Root recovered from compaction,
verified the active goal and agent state, saved its previously unsaved
candidate in a full checkpoint, and updated the operational override.

### Additional reviewed actual Poisson motive

[Proof](poisson-path-motive-attack.md), [checkpoint](poisson-path-motive-checkpoint.md),
[root PASS](review-poisson-path-motive.md) at mathematical revision
d1b1a3f3fe290c8754d63c526973f1405a9398f3353f870d81ba5bdefbeaa1c3.
The rational motive uses I_Y=Fib(M(Y)->1), H_mot=I_Y[-1], and the
ACTUAL ordered lambda given by pi and u. Its P2 source is the labelled
total complex of three face curves and three pair points, shifted[-2].
At equal endpoints the deliberately omitted triple term gives an actual
split constant line(-1,+1,-1). Selecting the R face and two endpoint
labels defines truncation; the LR corner is augmentation+1.

The stated cochain tensor-shift is negative on two shifted one-cycles.
The explicit negative of that shift makes the motivic product map the
positive chronological Chen kernel. Truncation/augmentation kill it
strictly, providing the actual zero nullhomotopies. Its cofiber with
-lambda is a rational motive realizing exactly the already reviewed MHS
pushout, with its top and bottom frames. Relative graph-spine topology
proves degreezero realization. No motivic kernel isomorphism or motivic
t-structure is inferred from that topology.

Over B2×Y the labelled smooth diagram is uniform. Finite pushforward,
top pullback along the unit and bottom pushout by Tr/degree(B2) give a
single averaged rational source overY. Functorial Deligne splitting gives
the average of the original h_b and the same exact q_F formula. The cusp
value remains a finite limit. Rationality of delta, a selected arithmetic
class and the point/K2/Tate comparison remain open.

### Additional reviewed exact local CM Taylor map

[Proof §§1–5](cm-local-point-comparison-attack.md),
[checkpoint](cm-local-point-comparison-checkpoint.md),
[uniform PASS](review-cm-local-point-comparison.md) at repaired revision
8fad3936741f7be8ff173ffb91c5da99036e94a55545eec685a21c56c975b5b8.
The formal multiplicative isomorphism is matched to the ORIGINAL Tate
coefficient identification, defining its unit period Omega_j. Its ratio
to the independently fixed Katz period is retained explicitly, not set1.
The period transforms by rho, so local Frobenius cancels the reindexed
rho weights in the actual derivative sums.

For L_(a,d)=D_omega^(d-1)(DTheta/Theta), the full sums
C_(m,d)=Omega_j/q_a·barpi^(-md)sum_g rho_m(g)L_(a,d)(g beta_m)
have limits C_d inZp and errorp^m uniformly in d. The EXACT opposite-ray
theta norm supplies the factorbarpi^d in their derivative norm.
Thus F_a(z)=sum_d C_d z^d/d! converges onpZp with uniform finite-level
errorp^(m+1). Its value is the actual point-Kummer logarithm of U_pi(R).

The independent review required an integral descent repair. Witt
invariants descend Omega_j log(v) modulo p^(k+1); the finite flat
connected Kummer identification turns the relevant H1 map into the
INJECTION pO_L/p^(k+1)->pW/p^(k+1). Comparing the actual formal torsors
overW and using this injection proves the descent. Faithful flatness
alone was not enough. The full semilocal trace counts each rho factor
once and retains the original q_a and transfer multiplicity.

Linearity is equivalent to all C_d,d>=2 beingzero. Agreement at the
three fixed multiplied points is equivalent to two explicit defects;
it is weaker than full linearity. The proved estimate
F(z)-C1z in p^(2v_pz) retains integrality of any pointwise scalar.
No coefficient vanishing/nonvanishing is part of this FIVE-section audit.
The subsequent new p5 finite-field test is a separate §6 and review route.

### New exact local Taylor unit and a disproved linear comparison

[Proof §6](cm-local-point-comparison-attack.md),
[full arithmetic PASS](review-cm-local-taylor-certificate.md),
[original script](../../compute/scripts/cm_local_taylor_mod5.py),
[original output](../../compute/data/cm_local_taylor_mod5.json),
[independent verifier](../../compute/scripts/verify_cm_local_taylor_mod5.py),
[independent output](../../compute/data/cm_local_taylor_mod5_independent.json).
The audit covers mathematical revision2b2210930ef8ee5419055ec5b83965551b09d72f0c0a485ffdcf1de7f4e14f25
and proves the additional P-or-Q refinement in its§8. Root read the full
review and both verifiers/outputs. This is NEW targeted arithmetic;
no old rank, height or cyclotomic certificate was rerun.

Atp5,m1,a7 use pi=-1+2i, i=3 inF5, and
mu=f0 barpi=234+78i of norm60840. Actual Frobenius endomorphisms at
twelve specified good split primes generate the correct CM imageH of
order4608. Its character is exactlyrho(g)=(conjugate psi(g))^-1 mod5,
and every generated relation preserves that weight. H intersects the
Gaussian units trivially; their four cosets exhaust the full unit group
of order18432.

The original computation evaluates the derivative sums on a primitive
mu-torsion point inE(F_(5^24)), checking its exact Gaussian annihilator,
Frobenius and4608-point orbit. The independent computation uses i·B
outside that orbit, a DIFFERENT ideal normal form, direct Legendre counts,
deterministic Frobenius witnesses and a Hasse/invariant-Taylor expansion
instead of the original A+yB recurrence. It independently checks field
irreducibility, Frobenius order24, all generators and the exact Gaussian
scaling of the four sums. Zero/nonzero is invariant under replacing the
primitive point by any other, with all possible factors nonzero.

The finite sums in degrees1,2,3,4 have patternzero,nonzero,nonzero,zero.
The separate core coefficient limit and unit period/smoothing factors
then prove C1,C4 in5Z5 and C2,C3 inZ5^times. These C_d are LOCAL POINT
Taylor coefficients, not the original cyclotomicc_(2,p). Neither C1 nor
C4 is asserted to vanish exactly.

For every nonzero x,y in5Z5, the exact additivity defect has leading
C2xy. The already proved integrality of ALL Taylor coefficients makes
every higher mixed term at least one5-adic order smaller. Hence

    v5(F_a(x+y)-F_a(x)-F_a(y))=v5(x)+v5(y).

Independent rational Fraction doubling at64P,64Q,64(P+Q) gives formal
parameter/logarithm valuations1,1,2 and normalized residues4,1,4.
The particular defect's log has valuation2. Since the integral local
H1 lattice maps to5Z5 underLog_omega, its lattice valuation is1,
so the class is nonzero modulo25. No single scalar point map agrees
with the actual local norm family at all three inputs.

Moreover C1 in5Z5 andv5(x+y)=2 giveF_a(x+y) in125Z5. Each ofF_a(x),
F_a(y) lies in25Z5, and their sum has valuation2. At least one of the
TWO selected local classes at64P or64Q is therefore divisible by5 but
not25 in the local lattice; the sum-point class iszero modulo25 there.
The proof does not determine which of P,Q gives the nonzero class.
This sharper conclusion was separately reconstructed in the audit§8.

The result is positive local selected-character nonvanishing and a
counterexample to the specified LINEAR local comparison. It is not a
global Selmer specialization, not a new original c2 theorem, and not
a counterexample to BSD. Additional boundary data and other arithmetic
operations remain possible; the next plan retains those genuine targets.

The reviewer hit one model-capacity error after its independent arithmetic
completed but before its audit writeup. Root preserved both programs and
outputs, then resumed the SAME Astra/xhigh handle. The full audit and
editorial source-motive completion were subsequently saved. No model
change, lost arithmetic, duplicated old run or unresolved blocker remains.


### Final round24 continuity verification

The final snapshot verifies 246 artifact hashes, 956 local artifact links,
11 certificate JSONs and all 10 certificate/source dependency hashes.
The legacy certify_ran.json contains two valid JSONL records. All three
Astra/xhigh handles reported completion; no process or next mathematical
assignment is live. No old certificate suite was rerun. The goal remains
active, with full universal BSD unresolved and the next actual targets saved.

## 25. Tangential traces, derived point symbols and global growing classes

Date:2026-09-13. Four constructions have complete separate PASS reviews.
Root read the full proofs and reviews and reconstructed the point–K2
calculation independently. No old arithmetic or new numerical run was
needed in this round. Full universal BSD remains neither proved nor
disproved. The later platform usage interruption did not lose a review.

### Actual tangential source and weighted trace normalization

[Proof](poisson-tangential-fiber-attack.md),
[checkpoint](poisson-tangential-fiber-checkpoint.md),
[uniform PASS](review-poisson-tangential-fiber.md), at mathematical
revision3c46ea64a8e448f5ae54c752ebb2962753eab7959dab53334dde0f6f3b905fba.
The ACTUAL unipotent specialization uses dual Log_n, with positive
weights0,2,...,2n, and its motivic constructibility theorem. The ordinary
functor, not its extra perverse[-1] shift, realizes the full limit MHS.
An actual rational uniformizer t has t/q->1; the formal modular q is
not assumed a rational function. The leading units are389^-6 at∞ and
389^6 at0, with cusp orders-388,+388.

Positive homological endpoint transport L has squarezero, kills the
Tate and bottomK directions, and lowersWby2. The relative limit weight
filtration is thereforeW. The flat period map usesexp(-logt/(2pi i)L),
checked on the coordinate Kummer top. The two corrected central rows
have logarithmic termsm A_c logt andm barA_c logt. The actual xi
principal part removes every higher second-kind pole BEFORE the finite
part. Their full loop rows and allowed top constant identify the
canonical central covectors in the actual nearby MHS. The original
finite-dimensional Deligne calculation then gives h_tan=limh exactly.

For r=u:X->P1, pushing dd^c qF=i/(16pi²cpi)(alpha∧bar theta+
theta∧bar alpha) giveszero: theta=r*(dw/w), tracealpha is a holomorphic
one-form onP1 and hencezero, and the L1 pushforward has no atoms over
critical values orcusps. The trace function is harmonic/constant and
vanishes at∞. Thus every fiber sum with its actual multiplicities iszero.
For div(u-2)=sum e_b[b]-388c∞, sum e_b h_b∞=0. The Galois-stable
multiplicities define an actual Artin endomorphism. Bottom pushout by
the unnormalized Tr_e gives h_Sigma=-388cpi qF, with central tangent
valueszero. The normalized Tr_e/388 version retains the primes2,97.
No primitivity of all earlier rational projectors is inferred.

The spectral operation becomes exactly
M=pi/(4sqrt389 cpi)<I_L(h_Sigma),Romega>_Pet.
The former analytic constant is removed by an actual algebraic fiber
trace. Rationality of delta/Petersson, the marked obstruction and the
point/K2/Tate BSD determinant comparison remain open.

### Exact derived group and actual point–K2 cochains

[Proof](point-k2-derived-symbol-attack.md),
[checkpoint](point-k2-derived-symbol-checkpoint.md),
[root PASS](review-point-k2-derived-symbol.md), at revised mathematical
hash3cf1c40dada9ed02f7e724c3db9a3f36c04449e61bb979857a94be38f1bbed36.
Voevodsky cancellation explicitly justifies stable-to-effective Hom.
With A=M1(E), the remaining geometric MINUS group is
Hom(1,e_-(A⊗A⊗Gm)[-1]), hence degree-one Suslin homology of the
rational transfer-sheaf tensor. Sugiyama supplies exactness BEFORE
A1 localization; localization still retains degree-one homology,
already nonzero for the actual beta. No tensor-flatness shortcut kills it.

The surface coniveau sequence has only(1,3) in totaldegree4. It gives
the FULL CH³(E²,2)_Q as H1 of the K3-field/K2-divisor/K1-point Gersten
complex, with exact tame norms. The actual two-variable Miller function
M_R(s,t)=m_(s,-R)(t) has full divisor
V_R-V_O+Delta-Gamma_-R+H_-R-H_O. Its vertical terms are essential.
The Kummer-FIRST cochainTheta_R={M_R,beta(t)} has boundary
z_R+D_beta-T_R D_beta. Horizontal specializations are only at the
rationalO,-R and vanish byK2(Q)_Q=0. No translation invariance ofbeta
is presumed when identifying the graph term.

Thus z_R=(T_R-1)D_beta. The explicit cochain
Xi_(R,S)={M_R(s,t)/(m_RS(s)M_R(s-S,t)),beta(t)}
fills(T_S-1)(T_R-1)D_beta. For the actualP,Q,
m_PQ=(y+2x+1)/(x-4). This fills the SECOND difference and makes the
point action additive; the FIRST difference still needs its own filling.
All h_j markings, the degree-three right-cup-388 sign and the actual
Sigma-unit relation remain. Neither the full motivic lift nor rational
spectral comparison follows yet.

### Nonzero global CM coefficient classes and the surviving pair quotient

[Proof](cm-global-selector-attack.md),
[checkpoint](cm-global-selector-checkpoint.md),
[uniform PASS](review-cm-global-selector.md), at mathematical
revisionf1780e7f9f279faf0ac8e0661fee6370a94cceab07705dd028142c6017f57eef.
Use the actual opposite point torsorY=[barpi^m]^-1(R) overB_m,
and the ratioTheta_a(beta_m+S)/Theta_a(beta_m). Its full point norm is
Theta_a(tau0+R)/Theta_a(beta_m)^(p^m). For m>=k the denominator is
killed modulo p^k and the originalrho homothety kills the transferred
tame numerator. Thus the actual permutation-coefficient class haszero
augmentation and a UNIQUE I⊗Tpi/p^k lift. This uses finite rho
triviality, not a nonexistent rational invariant rho vector.

At pi the unique formal inverse is a G_Qp-fixed torsor point. Its
coordinate map selects exactly the previously proved U_pi(R), with
all semilocal cosets and ONE rho weight. Consequently one FIXED
R* in{64P,64Q} gives nonzero global classes mod25 for everym>=2.
This is global cohomology with point-division coefficients, not ordinary
Selmer nonvanishing. Full original F_m transfer still has the extra
(p-1)p^(m-1-n) factor and becomeszero at the stated depth.

The point-field step has degreep² and argument multiplicityp. Coefficient
projection is p perstep; pullback is actual replication of the lower
class, induced by the origin-reduced geometric D_m. All fixed point
jets vanish by the exact bound, but pi-inertia H0=0 gives UNIQUE deeper
lifts. At p5,k2,m>=4 the same nonzero class lies uniquely in
H1(K,I^(5^(m-3))⊗Tpi/25). Its local selector detects growing order;
no next-associated-graded nonvanishing is asserted.

The first tensor now retains E[barpi^k]⊗Tpi and its proper Weil target
mu_(p^k), with the pi^k/adjointbarpi^k unit and ordered sign. This
first contraction is nevertheless eventuallyzero by the fixed-jet theorem.
Every scalar map on the FULL transitive permutation module is a multiple
of augmentation and kills I; augmentation itself is nonzero. The audit
corrected that wording and retained ramified source-to-base residue maps.

All allowed common-c proper-point corrections pull back to
eta_R-c N_Y kappa_pi(R). The norm vector has exact depth
p^(m-k+1)-1 and local coordinate1. Atp5,k2 the two-point detector is
(yF_a(x)-xF_a(y))/25 mod25, with x=log64P,y=log64Q.
Its numerator has quadratic leading(C2/2)xy(x-y) of valuation3 and
all higher terms have valuation>=4. The detector therefore has exact
order5 and kills the ENTIRE common-c correction line. The pair of
actual global classes remains nonzero after every such correction,
also in their deep lifts. The ordinary Kato/Bockstein, other local
conditions and single rational BSD-frame operation are still required.

### The actual mixed Heegner corner and conditional native gluing

[Proof](heegner-mixed-quadratic-attack.md),
[checkpoint](heegner-mixed-quadratic-checkpoint.md),
[odd PASS](review-heegner-mixed-quadratic.md), at mathematical
revision51d6f6e481ac6c99cb96910b3734f2a1d346bf9bb49abb34bc74e1f61491ca26.
The genuine quotientR[x,y]/(x³,y³) and idealxy give the UNIQUE actual
corner with graded typesM,M_D,M_D,M. Its first projections are the
existingH_i,H_j; its quartic point coefficient is the actual1/4 sum
j_i²j_j²g y_(ij), only extracted over the ring-class field.

Writing the raw corner(kappa,h_i,h_j,h), its mixed equation is
 dh=-a_i cuph_j-a_j cuph_i-a_ij cupkappa,
with d a_ij=-(a_i cupa_j+a_j cupa_i). The genuine class supplies h.
Full old-local H0 gives the retained top cochains
-(tau_j/2)a_i²e+ at i and-(tau_i/2)a_j²e+ at j. The native top
preimage at both old places is the TRANSVERSE E line, not the finite
line. Elsewhere it is finite in the stated clean range.

For the self-cup compact classesg_r, the explicit cup homotopy
U_r=-b_r cuph_r-(a_r b_r) cupkappa gives
<g_r,kappa>=-R_r(kappa)/p^k in the original compact-FIRST convention.
The local representative change is an exact coboundary; no one global
cocycle is assumed strict at both old places.

For first liftsalphaH_i-alpha tau_i b_j+lambda_i b_i and its reverse,
first native products and cross-local conditions are
alpha tau_i G_ij=alpha tau_j G_ji=0,
lambda_i G_ji=lambda_j G_ij=0.
Their remaining compact mixed obstruction pairs tozero withkappa by
G_ji=-G_ij. In the primitive clean case the actual two-transverse dual
Selmer group isRkappa, so this proves mixed gluing if and only if those
conditions hold. For the unchanged cofactor usealpha=alpha_z, retaining
all d0,A,B and nonunit coefficients. Canonicallambda0 satisfies the
cross-local conditions but does not kill the FIRST products.

The native top choices still form the actualRkappa torsor, generated by
multiplying the original Shapiro class byxy. Nonprimitive dual groups
are not assumed cyclic, nonclean local images are retained, and the
extra complex zero has not been proved to kill the first products or
select the top. Full BSD remains unresolved.

### Operational interruption after completed reviews

The tangential reviewer returned a usage-limit error after saving its
complete280-line PASS. Root inspected and read that actual file, so no
review was lost. The root goal tool then reported usageLimited, while a
fresh account check reported ordinaryUsageAllowed=true. These are distinct
platform states; no reset credit was consumed and no model was changed.
The objective is unfinished, not complete or mathematically blocked.
Revalidate both thread and account state before scheduling continuation.


### Final round25 continuity verification

Verified 258 artifact hashes, 1030 local artifact links, 11 certificate
JSONs and all 10 existing certificate/source dependency hashes. The legacy
certify_ran.json remains two valid JSONL records. All four round25
proof/review pairs are complete; no arithmetic was rerun. No next round
has been dispatched, in accordance with the latest user request to finish
one round before reporting status. The goal is unfinished and currently
usageLimited in the scheduler; the separate account check permits ordinary
use. Complete reviews and restart notes are preserved.
