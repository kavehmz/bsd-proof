# Review of the actual CM derivative certificate and primary finiteness bound

Date: 2026-09-12. Reviewer: root/coordinator. Review of the
[proof](cm-derivative-nonvanishing-attack.md), its
[checkpoint](cm-derivative-nonvanishing-checkpoint.md), the
[script](../../compute/scripts/certify_cm39_padic.py) and
[exact data](../../compute/data/cm39_padic_derivative_certificate.json).

**PASS.** I reconstructed all eight sections and independently reproduced
the coefficient certificate. The actual derived class is nonzero at5,
Selmer corank is two, and Sha(E39/Q)[5-infinity] is zero. The uniform
valuation criterion is conditional on the specified coefficient being
nonzero; it does not prove that premise at any uncomputed prime.
The rational global BSD comparison remains unproved.

Mathematical proof inspected initially:
ac3017c7674fc81b73c8471081acb3f1459463c8c50925b03912939f0dd882e4.
The later source-scope wording was also inspected in proof
190fdbe54ca357dc2b9ec3dcf3b189da1ee23aa13447b79b5e41cf0757806128.
Its checkpoint is699447307cf85322e4ab8665d5d153860aa9e9fd2731d552ac34e610c8a8fcea.
Script:6f21c0c8d74af6a248918c9537585da11456f24060425c1b98da5d9ef5fde27e.
Data:22164e5e22c37f18cd5cb12ecf3a3296a106ef6e70c4b35f62267f4ad46bb85a.
A later wording refinement about nonvanishing versus nondegeneracy,
and completed-status links, do not change the mathematical conclusions.
The jointly simplified integral bound in §§6–7.2 also passed a
[third independent audit](review-cm-derivative-integral-bound.md),
whose complete local, coefficient-sequence and Smith checks were read.

## 1. Exact curve and period scale

I checked the full table row48672 i 1 [0,0,0,39,0] 2 2 in the
cached primary Cremona table and read
[Agashe–Ribet–Stein, Cremona Appendix Theorem5.2](https://www.math.fsu.edu/e-prints/archive/paper279.pdf),
including its period-lattice argument. The actual conductor is below
60000 and is not the exceptional990h labeling. Thus the index-one
optimality and Manin constant1 statements apply. The curve is already
globally minimal and has one real component, so its full real period
is the least positive real period. The differential is the stated
minimal dx/(2y), with the parametrization sign fixed positively.

The cusp argument is integral, not an extrapolation from the finite
symbol table. The displayed determinant equation constructs a matrix
in Gamma_0(N) sending0 to a/p^n whenever p is good and a is a p-unit.
Analytic rank two gives the exact zero integral from infinity to0;
its imaginary part is zero along the imaginary axis as well. Both
cusps therefore map to O. The projected path integral belongs to
the actual elliptic period lattice. Its real projection is half the
least positive period in the negative-discriminant case. Hence every
symbol needed at EVERY level is half-integral.

I also read the installed Sage10.7 eclib wrapper. It explicitly uses
lattice <2x,x+yi> in this case and multiplies the eclib coordinate by
1/2. This is applied by the actual call with base_at_infinity=True.
The separate numerical fixed-denominator computation is consistent
with the primary algorithm in Wuthrich1608.06423, §§2–4,7.1. Its
Manin premise is supplied by the preceding theorem. No estimate of
an unknown Manin constant is substituted for it.

## 2. Infinite precision is proved independently of the finite outputs

I checked the primary measure, exponent and tame SUM convention in
[Stein–Wuthrich §3, (3.1) and its finite polynomials](https://wstein.org/papers/shark/shark.pdf).
The manuscript has a later non-CM standing scope; this review uses
the displayed modular-symbol definition and the argument proved on
the page, not a later theorem outside that scope.

The Hecke relation at r gives the claimed sum over the p children
of each ball. Inserting alpha²-a_p alpha+p=0 yields exact measure
compatibility. Half-integrality of ALL good-denominator symbols and
alpha being a unit imply a bounded Z_p-valued measure for this curve.
This avoids relying only on an integrality statement for a different
isogenous representative.

For x in the bin omega(a)(1+p)^j+p^n Z_p, the exact logarithm
coordinate differs from j by p^(n-1)Z_p. The quadratic binomial
difference is their difference times (t+j-1)/2. The denominator is
a unit throughout the stated p≥5 range. Integrality of the measure
therefore makes the entire error lie in p^(n-1)Z_p. Summing the
finitely many bins does not weaken that valuation. This is the
required infinite-measure error proof; a stable p-adic print alone
would not establish it.

## 3. Reproduction and independent finite arithmetic

Root ran the exact new command

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_cm39_padic.py
```

The execution completed with exit0. All required eclib versus
fixed-denominator numerical-symbol checks passed, and both levels
returned the stated values. The mini-table warning is harmless here:
the full row and the primary optimality theorem were checked separately.

A separate Python/Fraction audit reconstructed ALL stored binomial
weights, Teichmüller residues and distinct bins; summed the exact
rational rows; verified the finite Hensel polynomials; and recomputed
both residues using only integer arithmetic. Its results were:

| Level | Distinct bins | A | B | alpha | Coefficient |
|---|---:|---:|---:|---|---|
|3|100|3540|-275|13 mod25|20 mod25|
|4|500|46545|86450|113 mod125|70 mod125|

The error bounds are respectively25Z_5 and125Z_5. Thus the
quadratic coefficient has valuation EXACTLY one. Root additionally
reconstructed the later carry data from the stored rows: A2=-5,
C=237, giving terms5 and15 modulo25 and test3 modulo5. These new
integer operations and the updated script/data hashes were checked
after their addition; the expensive symbol values were unchanged.
No earlier rank or archimedean certificate was rerun.

## 4. The coefficient concerns the actual derived class

The exact unit-to-MTT realization, unnormalized tame norm, smoothing,
Betti projection and cyclotomic generator are those of the previously
reviewed construction. At this additive conductor no nontrivial
bad Euler factor is silently removed. The certificate is an evaluation
of that already fixed realization, not a renormalization of its class.

The known point P=(3,12) is non-torsion. A rational non-torsion point
cannot become torsion after embedding Q in Q_5, so its local elliptic
logarithm is nonzero. All Euler factors in the existing undivided
height identity are nonzero. The nonzero c2 therefore proves the
ACTUAL w0=Sh(d_pi+d_barpi) is nonzero. The previous maximal-minor
criterion gives full Selmer corank two and finite primary Sha.
No identification of an individual derivative with a chosen point,
independence of the two derivatives, or nonzero mod5 reduction of
either class follows merely from this coefficient certificate.

## 5. Integral local coordinate and the coefficient sequence

The local unit argument checks directly. Integral CM idempotents
split the two local Tate lines because p is odd and split in Q(i).
Their residual invariants vanish: one has cyclotomic inertia and
the other nontrivial unramified Frobenius. Their H1 lattices are
free rank one and pair perfectly over Z_p. Nonanomalous reduction
identifies the point completion with the formal subgroup; its
Néron logarithm maps isomorphically onto pZ_p. Since k_alpha^(-1)
has valuation one, the fixed exp(delta0) is a primitive integral
point class. Its pairing with the local quotient generator is
therefore a unit. This proves the additional integrality of iota_p,
not just its nonzero rational value.

For the global comparison I read the cached primary Nekovář§6.1,
especially6.1.2–6.1.4, alongside the previously checked exact
continuous-cochain formalism in§3.4. The saturated ordinary plus
sequence and its quotient are exact for T→V→V/T. At bad places
nontrivial CM inertia, of order dividing4, survives modulo p and
kills the relevant local cohomology. At p the nonanomalous
H0((V/T)^-)=0 removes the extended-Selmer correction; the plus
image is the classical local Kummer condition. Odd-p real Tate
terms vanish. These conditions make the ordinary Selmer cone
compatible with the exact coefficient triangle.

Finiteness of primary Sha was proved FIRST. Thus H1 with T and V
is respectively the full point completion and rational point space.
The long exact sequence identifies the quotient of classical
p-infinity Selmer by its point-divisible subgroup with tors H2
of the base integral cone. That quotient is precisely primary Sha.
No self-duality sign or assertion that the full Sha at other primes
is finite enters this identification.

## 6. Smith divisibility and Cassels parity

At the base the square matrix has rational nullity two. Integral
Smith changes of bases leave its nonzero constant diagonal factors
p^(a_i) and a zero2×2 block. At degree TWO in the determinant,
every term must use each nonzero constant factor and two linear
entries from that lower block. Omitting another constant factor
would require at least three powers of T. Hence its quadratic
coefficient is a unit times p^(sum a_i)det B, with B INTEGRAL.
There is no inverse Smith factor or regulator normalization.

The torsion cokernel has order p^(sum a_i), already identified
with primary Sha. The actual Iwasawa determinant basis has unit
u(0), and the local coordinate iota_p is now proved a unit.
Thus v_p#Sha≤v_p(c2). At5 the right side is one.

I checked the primary Cassels–Tate statement as recorded in
[Poonen–Stoll, §1 and Theorem8](https://math.mit.edu/~poonen/papers/sha.pdf):
the elliptic pairing is alternating and nondegenerate after removing
the maximal divisible subgroup. The finite5-primary subgroup has
no such kernel and pairs trivially with the other primary groups.
Its order must be a square. Its valuation is therefore even and
at most one, forcing Sha[5-infinity]=0. Finiteness of the entire
Sha group is not needed.

## 7. Uniform criterion and scope of continuation

The Hasse/two-torsion nonanomalous argument holds for EVERY good
split p≥5 of this E, and so do the local-unit and coefficient-sequence
arguments after nonzero c_(2,p) has first supplied finite Sha.
The Smith/Cassels bound therefore gives exactly
v_p#Sha[p-infinity]≤2 floor(v_p(c_(2,p))/2). It does not give
nonvanishing of that coefficient at all primes.

For the carry formula, write j=r+pt and expand its binomial exactly.
The p²t²/2 part drops only modulo p². Distribution sums the first
part to the level-two measure. In the linear correction, the lower
symbol is independent of t and sum(t) is divisible by p; that
leaves precisely p C_p/(2alpha³). The remaining level-two lower
sum is zero by the Hecke relation at0 and m(0)=0. This reconstructs
Proposition7.1 and explains the actual wrong residue obtained by
omitting the carry at5.

A test which vanishes modulo p² need not make c_(2,p) zero;
higher levels remain available. Existence of a successful level
at every prime is explicitly unproved. The cited CM-height paper
distinguishes nonvanishing from nondegeneracy; a rank-two p-adic
kernel need not have a rational coefficient ratio. No all-prime
termination or rational BSD frame is inferred from that result.
The final comparison and universal BSD scope remain open.
