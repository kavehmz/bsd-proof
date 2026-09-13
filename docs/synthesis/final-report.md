# BSD research program — current report

Updated: 2026-09-13 after the tangential Poisson source, point–K2 symbols, global CM selector and mixed Heegner corner. All four new constructions passed separate independent reviews. This is the status of record.
**The program has neither proved nor disproved full BSD.**
The objective remains a proof or counterexample for elliptic curves over $\mathbb Q$.
The work below is rigorously delimited progress toward that objective.
The [September 11 report](final-report-2026-09-11.md) is preserved as history.

The research agents in this continuation used **GPT-6 Astra with extra-high
reasoning**, as requested. Mathematical deductions and computation certificates
were reviewed separately from their construction.

For the CM test curve $E:y^2=x^3+39x$, the certified result
$\operatorname{Sha}(E/\mathbb Q)[5^\infty]=0$ remains established.
The latest round extends the proved local CM nonvanishing to actual
GLOBAL classes with point-division coefficients, including a nonzero
quotient after every allowed common point correction. It constructs
an algebraic tangential source for the Poisson cusp value and removes
the cusp constant by a weighted fiber trace. It also supplies explicit
point–K2 cochains and a conditional theorem for joining the Heegner
mixed lifts. The first point–K2 difference and the first Heegner native
products remain unresolved, as does the ordinary Selmer/rational BSD
comparison. See [ledger §25](research-ledger.md#25-tangential-traces-derived-point-symbols-and-global-growing-classes)
and [the restart checkpoint](research-state.md).

## 1. Completed certificates

**[THEOREM, certified calculations and cited arithmetic inputs]**

| Statement | Certificate and proof |
|---|---|
| $r_{\rm alg}=r_{\rm an}=2$ for 389a1 | [Rigorous Mellin integral](analytic-rank-certificates.md) |
| $r_{\rm alg}=r_{\rm an}=3$ for 5077a1 | [Rigorous Mellin integral](analytic-rank-certificates.md) |
| $r_{\rm alg}=r_{\rm an}=2$ for $y^2=x^3+39x$ | [CM proof and conventions](cm-regulator-tensor-attack.md), [independent certificate](../../compute/data/cm39_analytic_rank_certificate.json) |
| $\widetilde\delta_{41\cdot61}(389a1)=4\pmod5$, and $\operatorname{Sha}(389a1)[5^\infty]=0$ | [Exact modular-symbol witness](continuation-2026-09-12.md) |
| $\operatorname{Sha}(389a1)[p^\infty]=0$ for $p=2,3,389$ | [Exceptional-prime argument](exceptional-prime-finiteness.md) |
| For $E:y^2=x^3+39x$, $c_{2,5}=20\bmod25$, an actual derived class is nonzero, and $\operatorname{Sha}(E/\mathbb Q)[5^\infty]=0$ | [Certificate and proof](cm-derivative-nonvanishing-attack.md), [root review](review-cm-derivative-nonvanishing.md), [third integral audit](review-cm-derivative-integral-bound.md) |
| $0.9931<n_{389a1}<1.0077$, where $n_E=L''(E,1)/(2\Omega_E\operatorname{Reg}_{\rm BSD})$ | [Certified period, heights, and full basis](bsd-archimedean-bound.md) |

The last quotient uses the full real period and the saturated Mordell–Weil
regulator; the exact torsion and Tamagawa factors for 389a1 are both one.
Its interval is a statement about a real number. It does not prove that number
is rational, integral, or exactly one.

The analytic-rank certificates include explicit infinite-tail bounds and exact
rational endpoints. Their independent review also reconstructed all required
Fourier coefficients from finite-field point counts. The full basis in the
archimedean certificate is proved using 319 exact rational-$x$ checks, 13 height
bounds, and a rank-two lattice argument, independently of the software saturation
cross-check. At 389 the extra $T$ factor in Kato's divisibility is retained.

These are reproducible certificates for known example-level conclusions,
not newly resolved cases of the full conjecture.

## 2. General implications established in this continuation

**[THEOREM, deductions from existing results]** The
[odd-rank bridge](odd-rank-selmer-bridge.md) proves that odd analytic rank at
least three forces Selmer corank at least three when $p\ge5$ is good ordinary
with irreducible residual representation and $E$ is non-CM. It also proves
the semistable supersingular version. Under Kim's additional hypotheses,
Kurihara numbers with fewer than three prime factors vanish in their **full
coefficient quotients**. This resolves the former GAP 5 in its stated ordinary
range, and the corresponding lower bound $r_p\ge3$.

**[NEW, independently reviewed deduction]** The
[unit-index formula](uniform-witness-attack.md) is
$$u_p=\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
=r_{\rm alg}+\dim_{\mathbb F_p}\operatorname{Sha}(E/\mathbb Q)[p]$$
when the refined nonvanishing theorem gives $M_\infty=0$.
For 389a1 this applies at every $p\notin\{2,3,389\}$: residual surjectivity
is proved uniformly and Castella–Sano covers both ordinary and supersingular
reduction. A unit witness exists at every such prime. Its **first index**
remains to be controlled. Chebotarev can separate any finite Selmer space;
two tests separating the rational-point directions leave a kernel isomorphic
to $\operatorname{Sha}[p]$.

**[NEW, independently reviewed deductions]** The
[derived-comparison attack](derived-comparison-attack.md) proves determinant
and cofactor formulas, a weaker vector nondegeneracy criterion, and a sufficient
one-sided global comparison criterion for full BSD. It also gives explicit
power-series counterexamples to extracting a central coefficient from twist
valuations alone, even with rank and inversion symmetry fixed.

**[NEW, independently reviewed deductions]** The
[geometric attack](genus-one-finiteness-attack.md) proves that a uniform bound
on divisor or splitting-field degrees of everywhere locally soluble torsors
is equivalent to full Sha finiteness. It distinguishes the rational Picard
class obstruction from the later Brauer obstruction. Fixed-degree polarized
finiteness does not supply the uniform degree bound. The stress test over
$\mathbb C(B)$ concerns a different base field and is not a BSD counterexample.

## Further proof attempts and their checked outcomes

**[NEW, independently reviewed deductions]**
[Family specialization](family-specialization-attack.md) proves that exact
sections of a determinant line specialize through rank jumps, but the
universal Gross–Zagier theorem gives only a first normal derivative. A
compatible perfect-complex model preserves its exact family height and tangent
Pfaffian identities while varying the higher pure normal coefficient. The
[review](review-family-specialization.md) required and checked an explicit
Bockstein descent premise; it is not inferred from the word “compatible”.

**[NEW, coordinator-reviewed deductions]** The
[modular visibility argument](modular-visibility-attack.md) proves
$\operatorname{Vis}_{J_0(389)}\operatorname{Sha}(389a1)=0$ and hence an injection
of the entire possible remaining group into $\operatorname{Sha}(J_0(389))$.
The exact modular degree is 40. The winding quotient kills the elliptic
factor, and published 5389a1 results refute the proposed general bound that
all Sha primes divide the modular degree. This refutes that proof shortcut,
not BSD. The remaining Hecke-annihilation target is H389.

**[NEW, independently reviewed deductions and a certified test]** The
[higher-period argument](higher-period-integrality-attack.md) gives the exact
Chen and corrected eta representations of the central derivative. Its
ordinary higher-cohomology shortcut does not provide a rational period line.
The [eta certificate](eta-correction-certificate.md) proves, on the actual
curve 389a1,
$$110<\mathcal C_E=\int\rho(x)U(x)^2dx<111,$$
so the exact identity is
$$L''(E,1)/2=4\pi\bigl(J''(0)-\mathcal C_E\bigr),$$
and omitting the correction is false. Both quantities and their
normalizations are defined in the linked notes. An arithmetic interpretation
of the corrected difference, rather than the uncorrected second jet, remains
required for the proposed leading-term proof.

**[NEW, independently reviewed deduction]** A
[single coherent integral measure](coherent-moment-attack.md) can be primitive
at every odd prime while its primitive global leading symbol has a nonunit
realization at 1093. This tests a stronger premise than arbitrary unrelated
p-adic series. The normalized ratio in the example is exactly one; what is
missing in the elliptic application is the shared integral regulator-tensor
comparison. No infinite-exception assertion or elliptic-curve counterexample
is inferred from this model.

**[NEW, independently reviewed deductions]** The
[Hecke–Brauer construction](hecke-brauer-annihilator-attack.md) identifies
the full arithmetic cohomology term left after removing geometric degree
and constant classes. The operator $T_2-T_3+1$ kills those two pieces but
acts as the identity on the elliptic Sha image. Norm, closed-point
evaluation, and the inner-conjugation Frobenius identity do not construct
the required annihilator. All local conditions, including at the real
place, are retained in the [review](review-hecke-brauer.md).

**[NEW, independently reviewed deductions]** On the explicit regular
[arithmetic surface of 389a1](weil-etale-lattice-attack.md), the integral
Picard group is $\mathbb Z^3$, but
$$H^3_{\rm et}(\mathcal E,\mathbb Z(1))
 =\operatorname{Br}(\mathcal E)\simeq\operatorname{Sha}(389a1).$$
The finite-generation hypothesis needed by the examined Weil–étale
construction is therefore exactly the missing Sha finiteness. The surface
zeta function and its pole of order three are computed unconditionally;
they do not supply that hypothesis. The [independent review](review-weil-etale-lattice.md)
checks the model, full integral groups, and source assumptions.

**[NEW, independently reviewed deductions]** The
[arithmetic Green comparison](arithmetic-green-comparison.md) constructs
the actual eta Hodge divisor, with vertical terms and metric normalization,
and evaluates its arithmetic theta pairing. Its degree-zero elliptic point
projection is zero. The ordinary arithmetic square and literal squared
Green-function path integral have different current degrees; the latter
form is not closed. The [review](review-arithmetic-green.md) verifies these
specific constructions without ruling out a new secondary class.

**[NEW, independently reviewed deductions]** The
[CM theta/regulator construction](cm-regulator-tensor-attack.md) gives an
actual common-theta expression for the full height regulator of
$y^2=x^3+39x$ and a mod-$p^4$ moment formula that retains nonunit regulators.
Its restricted measure normalization was reconstructed directly, including
pole removal, the once-per-ray-class sum, Euler factors and periods. The
[review](review-cm-regulator-tensor.md) also required a rationality-first
formulation of the remaining arithmetic identity. Having one generating
theta function has not proved that identity or the complex BSD quotient's
rationality. The new analytic-rank certificate is independent of this gap.

**[NEW, independently reviewed constructions]** The next round replaces
abstract regulator coordinates with explicit relative arithmetic objects:

- The [CM construction](cm-biextension-cycle-attack.md) uses a six-point
  1-motive and fixed rational Kummer corrections to realize the full
  regulator as a specified secondary determinant. Its direct torsion-frame
  and algebraic-character comparison maps do not give the analytic element.
- The [389a1 relative construction](relative-modular-cycle-attack.md) uses
  explicit rational functions to cancel every finite local height symbol.
  Its remaining real period matrix is the full BSD height matrix. The
  natural projected cusp loop has trivial flat holonomy at every iterated
  length; the higher Mellin comparison remains required. Its full-period
  Betti line has index two, explicitly retained.
- The [ordinary K-theory calculation](k-theory-lattice-attack.md) proves
  that the actual arithmetic model is étale simply connected, CH₀ is zero,
  and K₀ is Z⁴. The natural Chern map still has cokernel Sha[n].
- The [twisted construction](twisted-sheaf-lifting-attack.md) produces a
  global twisted bundle of rank n for each period-n class. This succeeds
  without a Sha-finiteness premise. Its minimal twisted rank is exactly n;
  forgetting its algebra multiplication gives ordinary K₀ class n²[O].
  The [Fourier–Mukai review](review-twisted-fm.md) checks that rank
  reduction produces a line on the corresponding torsor, retaining the
  degree-n input. The generic twisted K₀ group is also abstractly Z⁴,
  but its numerical Euler determinant is n². A uniform bound has not followed.

The proofs and reviews are linked in [ledger §11](research-ledger.md#11-explicit-relative-motives-and-twisted-bundles).
These constructions establish the arithmetic side more explicitly. They do
not establish the missing rational analytic element or uniform Sha bound.

**[NEW, independently reviewed constructions]** The subsequent round
adds four concrete comparisons:

- The [finite-coefficient Bott construction](bott-comparison-attack.md)
  realizes every finite Selmer class in higher motivic cohomology and,
  for p≥5, in an actual Quillen K-theory summand. Its division back to
  weight one retains exactly Sha[p^r]. The required primitive Tate weight
  changes with p^r; no uniform annihilator follows.
- The [CM elliptic-unit construction](cm-derived-unit-attack.md) produces
  an integral first cyclotomic derivative and proves its height identity
  on the full Selmer space without assuming finite Sha. When the known
  two-point regulator is nonzero, its projected determinant realization
  has precisely the required p-adic scalar. Descent of these elements
  to a single rational frame with the complex realization remains open.
- The [Mellin variation](mellin-variation-attack.md) constructs an exact
  full-modular-curve spectral jet proportional to ell_E·L(E,2), with
  both cusp boundaries retained. Its tested modular-unit transfer and
  first character-response repairs do not give the arithmetic comparison.
  The L(E,2) factor has not been cancelled in an integral regulator lattice.
- The [projective connection construction](projective-monodromy-attack.md)
  gives actual finite generic monodromy and integral local degree-zero
  connections. The integral extension of the finite-order connection
  has a separately computed obstruction. Neither local connections nor
  the generic cover supply the missing global Kummer adjustment.

The exact hypotheses, independent PASS reviews, source-convention repair,
and remaining comparisons are recorded in
[ledger §12](research-ledger.md#12-bott-derived-units-spectral-jets-and-projective-connections).
These results leave the universal BSD completion test unchanged.

The [second character response](spectral-second-variation-attack.md)
and [Mellin trace](mellin-trace-comparison.md) have now passed separate
reviews. The actual point-height matrix is expressed through the same
Green operator as the scattering calculation, with four exact rational
corrections. Tracing the undecorated Mellin source gives zero; retaining
its spectral coefficient produces an explicit additional term with
nonzero mass proportional to ell_E·L(E,2). The arithmetic realization
of that term remains required. See
[ledger §13](research-ledger.md#13-second-character-response-and-the-actual-mellin-trace).

The next [torsion differential calculation](projective-torsion-connection-attack.md)
identifies the exact integral obstruction at every relevant good prime.
A smaller ordinary block admits an integral local construction, but its
global descent remains required. The [genuine logarithm replacement](cm-motivic-derivative-attack.md)
also gives an explicit finite-Kummer formula recovering the CM derived
class. It preserves the distinction between that class and the
non-Hodge–Tate coefficient deformation used to define it. Both have
independent PASS reviews; their exact scope and remaining rational or
global comparisons are in [ledger §14](research-ledger.md#14-finite-torsion-differentials-and-a-genuine-logarithm-replacement).

The [preceding reviewed round](research-ledger.md#15-actual-arithmetic-metrics-heegner-lattice-descent-and-mixed-comparisons)
constructs the rank-five candidate divided Heegner point in an explicit
larger Mordell–Weil lattice; its descent to the original lattice remains
equivalent to the required two-prime vanishing. It also constructs an
actual arithmetic Chow class for the Mellin value, whose real metric
data does not establish rationality. The spectral cusp calculation
excludes specified finite regular-singular function realizations while
leaving integrated-period motives open. Genuine CM mixed extensions
recover the exact finite derivative, with the local reference matrix
now kept distinct from the global height matrix. No universal rank
comparison or rational BSD determinant is claimed from these results.


The [preceding reviewed round](research-ledger.md#16-full-coefficient-heegner-tests-exponential-periods-and-cm-p-unit-pairing)
makes the remaining Heegner obstruction testable in two precise ways.
**[NEW, independently reviewed deductions]** The
[compact-support construction](heegner-defect-duality.md) descends the actual
two-prime class to strict finite Selmer over Q and constructs perfect finite
cohomological tests. Under an additional full mod-p^k image hypothesis, the
[geometric reciprocity construction](heegner-local-reciprocity-attack.md)
detects its exact order at fresh primes and expresses those tests as explicit
weighted toric sums from an actual cyclic isogeny cover. Proving those sums
vanish is still the missing rank-sensitive step. Detection alone does not
prove the rank-five Selmer lower bound.

The [exponential construction](exponential-spectral-attack.md) now realizes
individual completed spectral kernels by an actual relative connection and
rational Betti cycles, with endpoint conditions and Tate factors checked.
The integrated Fourier sum and its rational BSD determinant comparison remain
unconstructed. The [CM cyclotomic pairing](cm-cyclotomic-pairing-attack.md)
retains the p-unit boundary and exact norm laws, but its tested product selects
the wrong CM-character component for the required derivative. This result
rules out that specified operation, not BSD. All four constructions have
separate agent reviews linked in the ledger; none changes the universal
completion status stated at the top of this report.


**[NEW, independently reviewed deductions]** The
[preceding round](research-ledger.md#17-irreducible-heegner-detection-actual-cofactors-and-the-global-theta-source)
removes the extra full Galois-image hypothesis from Heegner detection:
the original irreducible O5 assumptions now suffice, using verified
Lawson–Wuthrich cohomology vanishing. Actual signed closed-point classes
generate the compact dual, and their toric evaluation and global residue
relations are explicit. Review clarified the signed boundary, trace and
Gysin conventions; the exact formulas retain that dictionary.
The [level-raising calculation](heegner-toric-vanishing-attack.md) identifies
the same obstruction in the reduction of an explicit trace-zero point.
Its surviving primitive ramified-character heights are computed, but the
required reduction has not been proved zero.

The [CM two-direction construction](cm-two-variable-jet-attack.md) gives
actual integral classes whose sum is the known cyclotomic derivative,
retaining derived-specialization obstructions and separate local conditions.
The [integrated spectral construction](integrated-spectral-comparison-attack.md)
now provides one convergent relative theta integral for the complete value,
including both cusps and heat endpoints. It also constructs a rational
class beta2 in K2(E) with regulator exactly L(E,2)/pi. Thus the extra
noncentral regulator line is available. The arithmetic map from the
spectral class to the specified point-height determinant remains open;
its required coefficient is exactly 6N(N-1)n_E. These results still do
not prove rationality or integrality of n_E, full Sha finiteness, or BSD.


**[NEW, independently reviewed deductions]** The
[preceding round](research-ledger.md#18-individual-selmer-conditions-arithmetic-k2-extension-and-higher-residue-tests)
resolves two previously recorded subproblems. Both actual CM ray derivatives
are now proved individually Selmer, including finite coefficients; their
unramified split-place localizations vanish integrally for the fixed curve.
The same rational K2 divisor now has a unique rational higher-Chow lift over
the regular arithmetic model, and finite algebraic data specify a sufficient
integral multiple. No primitive integral generator or numerical denominator
is claimed.

Actual higher Heegner residues also give conditional cyclicity of the strict
finite Selmer group when the particular class has full order. That group
independently has a nonzero free direction, so its entire dual cannot be
killed by residue relations; the required vanishing concerns the particular
Heegner class. The harmonic calculation constructs and tests two further
arithmetic components. The finite cyclic component has zero second paired
jet, while the full arithmetic theta lift retains an explicit third-derivative
response beyond the tested Hodge/vertical span. The original weighted
spectral-to-height comparison remains unconstructed. These results do not
prove the required rank-five vanishing, BSD rationality, or Sha finiteness.

**[NEW, independently reviewed deductions]** The
[preceding round](research-ledger.md#19-actual-iwasawa-determinants-heegnerkato-coefficients-and-theta-projections)
constructs an integral determinant basis from the actual normalized CM
elliptic unit. The [CM proof](cm-iwasawa-presentation-attack.md) retains
the specialization defects and gives a concrete criterion: for the stated
good split prime range, nonvanishing of either actual first ray derivative
would force primary Selmer corank two and finite primary Sha. At that
stage neither nonvanishing nor the rational global comparison was proved;
the subsequent certificate below settles nonvanishing at5.
The local coefficient formula now follows from the actual Rubin derivative;
an unsupported arbitrary local Coleman factorization was withdrawn.

The [Heegner–Kato construction](heegner-kato-comparison-attack.md) proves
integral second division of the normalized Kato class under its stated
hypotheses, without assuming finite Sha. Published global reciprocity
identifies the corresponding Beilinson–Flach coefficients. The actual
finite ring-class lift has explicit first and mixed cup-product equations.
A cofactor operation cancels its two old local obstructions for a corrected
input; the global nullhomotopies and rank-sensitive mixed comparison remain
required. The p-adic coefficient is not identified with a complex third
derivative, and its twist component is correctly kept p-relaxed.

The [theta projection](theta-elliptic-projection-attack.md) proves that the
entire untwisted Du–Yang theta point series projects to zero on E389.
The original even forcing survives this projection test. Review corrected
a cusp regularity error: its metric pairing is realized by actual smooth
cutoff classes and a convergent pairing limit, with no single smooth
arithmetic class or rational point determinant inferred from that limit.

The [higher-cycle construction](higher-arithmetic-theta-attack.md) computes
the exact response of an actual genus-two arithmetic cycle and builds a
nonzero higher Chow cycle on a triple universal elliptic family. The tested
genus-two response and two scalar projections do not yield the required
nonzero weighted Mellin value. These are computations of specific operations,
with exact source conventions, rather than exclusions of every arithmetic
approach. All four constructions have separate PASS reviews. The universal
completion status at the top of this report is unchanged.

**[NEW, independently reviewed deductions and certificate]** The
[preceding round](research-ledger.md#20-a-certified-cm-derivative-global-tame-primitives-and-the-weighted-adjoint)
settles the first CM nonvanishing test. Exact modular-symbol sums and a
proved infinite-measure error give $c_{2,5}\equiv20\pmod{25}$ for
$y^2=x^3+39x$. Root independently reproduced the calculation and audited
every finite row. The existing height identity proves the actual derived
class nonzero and primary Selmer corank two. An integral local-unit and
Smith-determinant argument then bounds the finite primary Sha order by
valuation one; Cassels alternation forces that group to be zero.

The same argument gives a conditional bound at every good split prime:
if $c_{2,p}\ne0$, then primary Sha is finite and
$v_p\#\operatorname{Sha}[p^\infty]\le2\lfloor v_p(c_{2,p})/2\rfloor$.
An explicit carry formula makes the finite test more precise, but neither
nonvanishing at all primes nor the rational complex BSD coefficient has
been proved. The integral argument has an additional independent audit.

The [tame construction](heegner-tame-nullhomotopy-attack.md) proves that
the first global lifting equations have solutions for the corrected
Kato input in its stated stronger range, retaining the entire twist
factor. It also computes the separate local point-image obstruction:
the allowed old-prime corrections are transverse. The corresponding
dual group can be nonzero even when classical twist Selmer is zero.
The required local and mixed comparison, with rank-sensitive complex
input, is still unproved.

For 389a1, the [weighted adjoint](weighted-theta-adjoint-attack.md)
now recovers the original nonzero Mellin mass, with $N=389$, by
$$\mathcal M=-\frac{\pi^2}{2\sqrt N}
       \langle I_L(F),\mathcal E_L''(1)\rangle_{3/2}.$$
Its direct lattice unfolding retains both cusps, the zero-vector
cancellation and the source's exact Eisenstein multiplicity. This
completes that analytic comparison and proves $I_L(F)\ne0$.
It does not supply a rational arithmetic second-derivative class.

The [secondary Kummer construction](secondary-kummer-theta-attack.md)
recovers the fixed eta unit by an actual higher-Chow product, residue
and proper push. A compact graph-unit cycle gives its logarithmic
forcing with the exact cusp boundary. Its elliptic push is rationally
zero, and inserting the radial coefficient produces an explicit
nonzero $dd^c$ obstruction requiring correction. These reviewed
constructions leave the full universal BSD objective unresolved.

**[NEW, independently reviewed constructions]** The
[CM integral comparison](cm-uniform-carry-attack.md) sharpens the
conditional bound, on the full point basis, to
$$v_p\#\operatorname{Sha}[p^\infty]
  =v_p(c_{2,p})-v_p(\det B_p),\qquad c_{2,p}\ne0.$$
It retains every determinant-frame unit and constructs $B_p\bmod p^m$
from rational multiplied points, the canonical CM sigma series, and a
finite multiplicative-coordinate equation. The precision has an explicit
tail proof. The existing result at5 implies $v_5(\det B_5)=1$ and, in
the fixed logarithmic normalization, $v_5(\operatorname{Reg}_5)=3$.
Nonvanishing at every prime and a common rational global frame remain open.

The [native Heegner comparison](heegner-native-pairing-attack.md)
constructs the unique global inverse of the finite local-condition
quotient in its stated clean range. It gives the native obstruction
as an explicit finite pairing, or a bordered determinant when the
quotient is free. The exact Kato point transport and local logarithm
are fixed. A Kato change of primitive produces canceling old-prime
and $p$-terms, so it cannot tune that obstruction. Its required vanishing
from the extra complex zero and the selection of the mixed lift remain open.

The [arithmetic Poisson construction](theta-doubling-arithmetic-attack.md)
produces a canonical rapidly decreasing solution
$dd^c q_F=\operatorname{Re}(F)d\mu$. Its finite-energy metric defines an
actual Bost arithmetic class on a specified modular scheme cover.
With the original arithmetic Hodge-height series $R_\omega$, it proves
$$\mathcal M=-\frac{\pi(N-1)}{4\sqrt N}
       \langle I_L(q_F),R_\omega\rangle_{\rm Pet}.$$
This is an ordinary convergent pairing of two specified arithmetic
height series. Review corrected the Poisson sign and checked the final
formula. The ordinary intersection of the underlying Poisson class
with the Hodge line is zero, so no rational regulator identity follows
by replacing the displayed operation with that ordinary height.

The [radial graph correction](radial-graph-correction-attack.md)
constructs a nonzero real relative Deligne class
$\mathcal C_{j_2}\in H^3_{\mathcal D}(X\times E,B,\mathbb R(2))$,
with its cusp trivializations and original evaluation
$\mathscr P(\mathcal C_{j_2})=\mathcal M$.
Its corrected mixed current is closed even though the scalar spectral
jet has infinite energy. Every rational scalar-unit cup with the
specified graph Chern class evaluates tozero; that tested image does
not contain this class.

The [relative boundary construction](relative-beta2-boundary-attack.md)
embeds the existing rational $K_2$ class $\beta_2$ into the same
relative group and computes
$$\mathscr P(\operatorname{reg}j_B(\beta_2))
   =\frac{(N-1)\omega_1L(E,2)}{8\pi^3c_\pi}\ne0,\qquad
   \Omega_E=2\omega_1.$$
The quotient of the spectral evaluation by this boundary period is
$-24Nc_\pi\ell_E/\Omega_E$. It still lacks the Néron–Tate regulator.
Multiplying the boundary period by $\operatorname{Reg}_E$ alone
gives the expected period product up to the displayed rational factors;
an arithmetic map producing that multiplication from the spectral
class has not been constructed. Neither equality of classes nor
rationality or integrality of the BSD quotient is inferred.

**[NEW, independently reviewed constructions]** The
[compact cup and trace](relative-cup-trace-attack.md) is an actual
rational map to $K_2(E)$ whose composite with the boundary injection
is $388$ times the identity. Dividing by388 gives a rational retraction.
It determines the full real Deligne image
$$R_u^{\mathcal D}(\mathcal C_{j_2})
 =-24\cdot389\,c_\pi\frac{\ell_E}{\Omega_E}
                       \operatorname{reg}(\beta_2).$$
The one-dimensional real target does not prove rank one of rational
$K_2(E)$ or rationality of that coefficient.

The [geometric determinant construction](point-determinant-single-valued-attack.md)
realizes the point-height determinant as the exact quadratic
Deligne-conjugation coefficient of the exterior square of the
previously constructed rational one-motive. Its extreme coefficient
is $-\operatorname{Reg}_E/\pi^2$, with integral frames and all Tate
factors retained. Both inspected standard scalar higher heights
vanish on this object, so they cannot replace that coefficient.

An additional reviewed test shows that the extension associated with
the relative Deligne class has square-zero Deligne operator, while
the determinant object and its $K_2$ tensor retain nonzero quadratic
and cubic operators. An ordinary mixed Hodge structure map between
these objects cannot preserve the required top frame. This excludes
that specific comparison; an additional coefficient extension or a
justified secondary arithmetic operation remains to be constructed.

The [native isogeny construction](heegner-native-height-comparison.md)
realizes the original finite coefficient sequence by actual isogenies
$B\to C\to\operatorname{Res}_{F/\mathbb Q}E$. The specified input and test
give locally trivial torsors with
$$\operatorname{CT}_{C}(\xi_i(z),\upsilon_i)
                         =-\mathcal R_i(z)/p^k.$$
Their vanishing from the extra complex zero is not proved. The marked
finite inclusion does not extend to an elliptic homomorphism into $C$.
In the separate rational-point subcase, the obstruction is the push
of an explicit norm torsor, and its vanishing is equivalent to a
global norm congruence. The Kato input is not assumed to satisfy that
additional point premise.

The [CM division-torsor construction](cm-symbol-point-reciprocity-attack.md)
proves exact Kummer-field degrees and theta norm multiplicities,
constructs a relative norm torsor with a specified root, and evaluates
a surviving cubical norm. Its rational leading logarithm is nonzero
at every odd prime, but the complete transferred classes and the
finite-corrected height component vanish. Those auxiliary facts
therefore do not prove nonvanishing of the original $c_{2,p}$.
The new rational calculations were independently reproduced; no old
certificate or prime scan was rerun.

**[NEW, independently reviewed constructions]** The
[Poisson iterated-source formula](poisson-iterated-source-attack.md)
reconstructs the exact $q_F$ from genuine length-one and length-two
algebraic path periods on the full modular curve, with explicit
Riemann–Roch and compact-period corrections. It retains the cusp
finite part and the exact factor $4\pi c_\pi$. The real normalization
is not inferred to be a rational motivic morphism.

The [moving marked family](marked-coefficient-extension-attack.md)
is defined from the full corrected point divisors and actual rational
Miller functions. Its new boundary has residue matrix
$\left(\begin{smallmatrix}4&3\\3&4\end{smallmatrix}\right)$,
with determinant7. It retains nonzero quadratic and cubic Hodge
components, while its finite corrections keep the global point-height
matrix fixed. The added Poincaré fibers are nontrivial and cannot
be assigned zero trivializations.

Two further reviewed steps construct an **actual rational motivic
coefficient object and top map**, then prove that the original restricted
spectral class has a **real Deligne lift** into that coefficient object.
The latter follows from relative cohomology on the noncompact base,
Künneth and the proper-origin Deligne representative. These substeps
are completed. A rational spectral input, vanishing of its motivic
obstruction, selection of an arithmetic lift, and compatibility with
the added boundary remain to be proved.

The [Prym-norm construction](heegner-prym-norm-attack.md)
realizes the same native pairing over a smaller reflection field.
Its actual integral lattice has a connecting class generating
$\mathbb Z/p^k$, and the marked coefficient map cannot lift by
even one further power of $p$. The proof computes the global
obstruction for the actual Kato/cofactor input, including the
cofactor classes’ lifting defects. It does not prove that this
particular global obstruction or Cassels–Tate value vanishes.

The [CM coefficient-cone construction](cm-derived-unsmoothing-attack.md)
gives a unique integral class and an explicit theorem showing that
every fixed point-augmentation jet eventually vanishes over full
$\mathbb Z/p^k$ coefficients. It also constructs a separate higher
class of exact order $p^k$ and identifies its nonzero local boundary
and zero image under the original CM transfer. The original
$c_{2,p}$ nonvanishing and common rational frame remain open.
Only new targeted rational arithmetic was checked; no old certificate
or prime scan was rerun.

**[NEW, independently reviewed deduction]** The
[Poisson Hodge framing](poisson-hodge-framing-attack.md) identifies the
analytic source with an exact canonical Deligne invariant of an actual
rational ordered path-module pushout. With its specified elliptic and
Tate frames,
$$h_{\omega,b}(z)=-\frac{U_b(z)}{4\pi},\qquad
q_F(z)=-\frac{h_{\omega,b}(z)-h_{\omega,b}(\infty)}{c_\pi}.$$
It also proves the cusp principal-part compatibility directly from a
complex loop character. All compact-genus corrections remain present.
The canonical real splitting is not thereby rational, and the cusp
value is a proved finite limit. The
[separate audit](review-poisson-hodge-framing.md) checked the actual
path object, logarithmic filtration, Deligne lifts and every scalar factor.

The [marked rational boundary test](marked-rational-boundary-lift-attack.md)
computes the actual motivic obstruction for the known rational input
$j_B(\beta_2)$ as $-j_B(\epsilon_0\otimes\beta_2,0)$.
Its first abelian component is represented by the actual products
$(P-O)\times\beta_2$ and $-(Q-O)\times\beta_2$ in
$\operatorname{CH}^3(E\times E,2)_{\mathbb Q}$.
The geometric plus (Tate) projection of these products is zero.
The geometric minus component, whose realization is the rank-three
symmetric square of $H^1(E)$, has not been proved zero.

The same proof constructs rational K2 corrections with their actual
new-boundary residues and derives a necessary boundary-unit relation
with coefficient388. Corrections pulled back from the entire downstairs
fiber contribute zero to that relation. This does not rule out other
corrections or prove that the remaining obstruction is nonzero.
All signs, cycle degrees and the Tate projection passed
[root's independent audit](review-marked-rational-boundary-lift.md).

**[NEW, independently reviewed construction]** The
[asymmetric CM ray source](cm-asymmetric-ray-attack.md) retains the
opposite ray after dividing the point in only one CM direction.
Complete transfer still vanishes at a proved depth because it retains
an unused-ray factor. Defining the class directly over the smaller
field avoids that factor; its norm shifts the point by $[\bar\pi]$.
The distinct point-translation jets satisfy a new full-coefficient
vanishing bound, with the endomorphism retained.

On an actual punctured elliptic curve, the original selected character
has a class of exact order $p^k$, certified by its explicit residues.
The possible proper point component is an integral line generated by
the universal point Kummer class. Compatible boundary subtractions
leave precisely a $\mathbb Z_p$ parameter, which has not been selected
arithmetically. A local formal inverse constructs a norm-compatible
principal-unit family without dividing $p$; its deep values do not
descend to the original global ray field. These statements passed
[independent review](review-cm-asymmetric-ray.md). They prove neither
selected-character nonvanishing at $P,Q$ nor the original BSD coefficient.

**[NEW, independently reviewed constructions]** The
[Poisson path motive](poisson-path-motive-attack.md) now supplies an
actual rational motive realizing the canonical Hodge source, with
explicit augmentation and bottom maps. Its labelled boundary diagram
retains the constant path at coincident endpoints, and its finite-base
construction retains every conjugate of the chosen basepoint. The
real invariant has the same exact Poisson formula. Constructing this
source does not make its Deligne splitting a rational morphism.

The [local CM point-map proof, §§1–5](cm-local-point-comparison-attack.md)
computes the specific local norm family's point coordinate as
$F_a(\log_E R)=\sum_{d\ge1}C_d(\log_E R)^d/d!$.
Each $C_d$ is the integral limit of explicit character-weighted algebraic
theta derivative sums, with a proved finite-precision error. The actual
Tate frame and full semilocal trace are retained. This identifies what
must vanish for a linear point comparison; it does not infer linearity
from the rank-one target. See the separate
[motive review](review-poisson-path-motive.md) and
[local-map review](review-cm-local-point-comparison.md).

The [Heegner cofactor-lift proof](heegner-cofactor-lift-attack.md) now gives
an exact point-local lifting defect for the fixed cofactor and bounds
it using the order of the actual two-prime Heegner class. In the primitive
case the original fixed classes lift without any assumption of finite
Sha or of a rational-point representative for Kato. In the clean native
range, a genuine cubic coefficient construction gives
$\mathcal R_i(\kappa)=-a_j^+(\eta_i)G_{ij}$; for a primitive class and
the fixed $z=\alpha_z\kappa$, it gives
$\mathcal R_i(z)=-\alpha_z a_j^+(\eta_i)G_{ij}$.
The extra complex zero has not been proved to annihilate that product.
The [independent review](review-heegner-cofactor-lift.md) retains the
nonprimitive and nonclean scope distinctions.

**[NEW, exact arithmetic independently reproduced]** For the local CM
map at5, the Taylor coefficients satisfy
$C_1,C_4\in5\mathbb Z_5$ and $C_2,C_3\in\mathbb Z_5^\times$.
The calculation uses the actual4608-element CM image on a torsion orbit
in $E(\mathbb F_{5^{24}})$, the original character, and exact invariant
derivatives. A second implementation used a different torsion orbit,
direct point counts and a different derivative calculation. Both
[outputs](../../compute/data/cm_local_taylor_mod5.json) and the
[independent output](../../compute/data/cm_local_taylor_mod5_independent.json)
are preserved with their verifiers.

The proved all-degree bounds then give
$$v_5(F_a(x+y)-F_a(x)-F_a(y))=v_5(x)+v_5(y)
\qquad(x,y\in5\mathbb Z_5\setminus\{0\}).$$
At the actual points $64P,64Q,64(P+Q)$, the logarithm valuations are1,1,2.
The defect has logarithm valuation2, hence local lattice valuation1.
No single scalar times the point Kummer map agrees with this family at
all three points. At least one of the two $64P,64Q$ classes is divisible
by5 but not25; the sum-point class is zero modulo25 in that lattice.
These statements passed the full
[arithmetic audit](review-cm-local-taylor-certificate.md), including the
sharper two-point consequence. The LOCAL Taylor $C_2$ is distinct from
the original cyclotomic $c_{2,p}$.

**[NEW, independently reviewed constructions]** The
[tangential Poisson motive](poisson-tangential-fiber-attack.md) realizes
the former finite cusp limit as the exact canonical invariant of an
actual rational motive. The finite map $u:X\to\mathbb P^1$ also satisfies
$u_*q_F=0$. Its actual fiber multiplicities at $u=2$ therefore give an
algebraic weighted source with
$h_\Sigma=-388c_\pi q_F$, so no cusp-constant subtraction remains.
This does not make the Deligne or Petersson operation rational.
The full [audit](review-poisson-tangential-fiber.md) was saved before
the reviewer's later usage-limit interruption.

The [point–K2 symbol construction](point-k2-derived-symbol-attack.md)
identifies the remaining group by exact derived and Gersten models.
For the actual diagonal class $D_\beta$, a rational Milnor K3 cochain
gives $z_R=(T_R-1)D_\beta$, and another explicitly fills the second
translation difference. It does not fill the required first difference.
The [separate audit](review-point-k2-derived-symbol.md) checks every
divisorial residue and the effective/stable category comparison.

The [global CM selector](cm-global-selector-attack.md) gives one fixed
$R_*\in\{64P,64Q\}$ with nonzero global classes modulo25 at every
level $m\ge2$. They have zero augmentation and, for $m\ge4$, unique
nonzero lifts to augmentation depth $5^{m-3}$. Their pair remains
nonzero after every allowed common proper-point correction. These are
classes with enlarged coefficient modules; ordinary global Selmer and
original cyclotomic conclusions require a further operation. See its
[independent audit](review-cm-global-selector.md).

The [mixed Heegner corner](heegner-mixed-quadratic-attack.md) constructs
the actual biquadratic class and its compact gluing obstruction. In the
primitive clean case, the specified first lifts join to a native mixed
lift exactly when the first native products and the displayed cross-local
conditions hold; no further compact mixed obstruction survives. The first
products are not proved zero, and the top choices still form the actual
$R\kappa$ torsor. The [audit](review-heegner-mixed-quadratic.md) retains
the nonprimitive and nonclean cases separately.

## 3. Exact remaining proof tasks

For the test curve 389a1, a concrete sufficient pair is:

- **[GAP PrimeIndex-389]** Prove $u_p=2$ for every
  $p\notin\{2,3,389\}$. The completed exceptional-prime calculations would
  then give $\operatorname{Sha}(389a1)=0$ by primary decomposition.
- **[GAP Leading-389]** Prove $n_{389a1}=1$. The certified interval makes
  it sufficient to establish integrality, but integrality is a substantive
  missing theorem. Complex rationality alone does not establish it.

The new relative construction makes the primitive half-period line another
sufficient target: proving $n_{389a1}\in\tfrac12\mathbb Z$ would already
force one in the certified interval. No analytic element in either this
line or the specified full-period line has been constructed.

An almost-all-prime version of the first statement requires primary finiteness
at every additional exceptional prime it introduces. The
[one-sided comparison criterion](derived-comparison-attack.md#6-the-units-can-be-bypassed-a-one-sided-and-archimedean-reduction)
and the [torsor degree criterion](genus-one-finiteness-attack.md#3-the-uniform-degree-criterion-really-is-full-finiteness)
are alternative routes, with all premises stated explicitly.

A proof for this test curve would still not prove BSD for every elliptic curve.
The general program also needs uniform rank comparisons in higher rank and
coverage of CM curves and all local conditions. The next odd Selmer lower-bound
step is [O5](odd-rank-selmer-bridge.md#5-the-next-exact-statement-at-analytic-rank-at-least-five).
No such general comparison or uniform prime-index theorem is claimed here.

## 4. Reproduction

The original four-certificate suite runs from the repository root, in
this order for its dependencies:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_mellin.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_bsd_interval.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_exceptional_primes.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/kurihara_witness.py
```

Outputs live in `compute/data/`. Independent reviews:
[analytic certificates](review-analytic-certificates.md),
[uniform-witness deductions](review-uniform-witness.md).
Coordinator reviews of the archimedean, exceptional-prime, derived-comparison,
and geometric arguments are recorded in their notes.

The new arithmetic-surface and CM-39 checks use
[`arithmetic_surface_check.py`](../../compute/scripts/arithmetic_surface_check.py)
and [`certify_cm39.py`](../../compute/scripts/certify_cm39.py).
Their exact commands, plus the eta and coherent-measure checks, are in
the [complete computation guide](../../compute/README.md).

The earlier P1–P3 sufficiency claim remains withdrawn. Its exact logical errors
are documented in the [first continuation audit](continuation-2026-09-12.md#4-errors-found-in-the-previous-reduction).
