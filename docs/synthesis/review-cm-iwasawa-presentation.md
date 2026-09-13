# Independent review of the actual CM Iwasawa presentation

Date: 2026-09-12. Reviewer: root/coordinator. Review of the
[proof](cm-iwasawa-presentation-attack.md) and
[checkpoint](cm-iwasawa-presentation-checkpoint.md).

**PASS after the Coleman coefficient repair.** The actual perfect
presentation, integral determinant basis, Tor formulas, Selmer cone,
second-jet identities and conditional nonvanishing criterion pass.
The final mathematical proof inspected has SHA256
407f2915bf07aa46a3e1608c0d4ddab264b9580e9dca5fe891457f5cda826708;
its checkpoint has SHA256
09194884504b249266968020447e24bc25ce227879d3e0f0117be907ed23bfcd.
Subsequent completed-status and review links are editorial.
Neither first derivative is proved nonzero. Full BSD remains unresolved.

## 1. Perfectness and actual base change

I read Nekovář, *Selmer complexes*, Astérisque310(2006),
[primary source](https://www.numdam.org/item/AST_2006__310__R1_0.pdf),
3.4.2–3.4.4, 4.2.1–4.2.9 and 5.1.1–5.1.2. These statements
provide exact continuous cochains, compatibility with finite free
tensor complexes, finite cohomology and perfect amplitude [0,2].
The global field Q(i), the ramification set containing p and infinity,
and odd p satisfy the displayed finiteness and cohomological-dimension
hypotheses. The coefficient is finite free over the complete local R.

Resolving each coefficient quotient before taking cochains proves
the stated DERIVED base changes; no cohomology-flatness assertion
is used. Residual H0 vanishes by the actual minus-one element.
In a minimal free model this removes the degree-zero term.
Cyclotomic H2 torsion implies N/(X-Y)N is torsion; localizing at
(X-Y) and applying Nakayama makes N there zero, so N has rank zero.
The cyclotomic Euler characteristic fixes the rank difference one.

For the rank-one kernel, dividing the coordinate gcd yields a
vector primitive at every height-one prime. The intersection of
those DVRs is R. This proves every integral kernel vector is an
R-multiple, including at the maximal ideal, and hence freeness.
It does not assert that the coordinates generate the unit ideal.
The proof constructs an actual presentation by an existence theorem;
it does not claim to have computed a numerical Galois relation matrix.

## 2. The actual element and every height-one factor

I checked Kato, Astérisque295(2004),
[primary source](https://www.numdam.org/article/AST_2004__295__117_0.pdf),
Theorem15.2 and (15.6.1)–(15.6.4), printed pp.250–255 in the
cached full primary PDF. The unit/class equality is available in
the stated split range, including height one at p: p is prime to
the Hilbert-class-field roots of unity and to the finite ray torsion.
The actual values here are 4 and 1152(p-1)^2. Modules finite over
Z_p in the comparison are invisible at height one of this
three-dimensional ring; they are not asserted to be zero modules
or finite abelian groups.

The twist transports the pre-twist rho-inverse branch to the
declared branch by an integral Iwasawa ring automorphism. The norm
is not averaged. The retained theta twelfth power and the division
by 12(N(a)-sigma_a) match the reviewed unit construction. Its
projected Betti coefficient (1±i)/2 is a p-unit in this range,
with its exact value still in the element. At the non-p conductor
primes the CM inertia character remains nontrivial modulo p;
the coefficient and its dual have no local invariants. Duality,
the local Euler characteristic and residual perfect base change
make the local correction complexes acyclic. Thus the comparison
uses the intended full Galois complex on this branch.

Over each height-one DVR the maximal-minor gcd has valuation
length(N), while the coefficient f of the actual unit has valuation
length(M/Rz). The primary equality therefore proves u=f/c is a
unit in R. This is integrality of the specifically defined eta_z,
not a choice of a new generator to make the result true. The
cohomological determinant retains higher-codimension information.

## 3. Cofactor sign and specialization defects

I reconstructed the cofactor contraction with
Delta_j=(-1)^(j+1)det(D_hatj). In the frame that puts the kernel
vector before lifts of Q, it sends epsilon to Delta. Appending
localization as the LAST row gives det(A)=(-1)^b c l. Thus
F=(-1)^b u det(A), as in the repaired draft. The earlier suppressed
sign is not carried into the final determinant assertion.

The free resolution 0→R→P→Q→N→0 gives every Tor group in (11).
In particular h0=0 makes Tor2 equal to Z_p, whereas h0≠0 makes
it zero. The vector identities f0h0=0 and
d_j=f_jh0+f0h_j show exactly why a free H1 module need not give
I-divisibility or independent first derivatives. Specializing along
X-Y similarly retains N[X-Y]=S_c/(s). A zero vector h(T,T)
would make X-Y divide every coordinate of h, contradicting its gcd.

For the nonvanishing criterion, write r=dim_Qp ker(D0). Its known
point subspace has dimension two. The previously reviewed Q-local
duality theorem identifies ker(D0) with the full rational Selmer
space, without identifying that space with points alone. A maximal
minor has at least r-1 factors in I after isolating the invertible
constant block. Since z=u Delta, r≥3 forces both first jets zero.
The coefficient groups before rationalization are Z_p-free, so this
vanishing is integral. Nonzero either jet therefore forces r=2.
The quotient of the cofinitely generated primary Selmer group by
the known rank-two point group then has corank zero and is finite.
The proof does not establish the premise of nonvanishing.

## 4. Local Selmer cone and natural Bockstein maps

At the unramified split place, nonanomalous reduction gives residual
H0=0; the Tate dual has nontrivial inertia and hence H2=0. Local
Euler characteristic and minimality leave one free degree-one term.
The ordinary plus condition is all of T_pi at the other split
place. The bad-prime corrections just checked vanish. These facts
give the actual square presentation in (14).

Changing the localization row by tD is a cochain homotopy. It
changes neither its value on z nor the determinant. Nonzero finite
cyclotomic-character reciprocity for the actual Kato element proves
the quotient localization is nonzero; the formal component has
zero dual exponential. Thus the square complex is generically
acyclic. The whole local module is not declared to have a
canonically normalized Katz power series as its coordinate.

The already proved integral zero localizations of both derivatives
give unique local nullhomotopies, since local H0 is zero, also with
finite coefficients. They imply F∈I² by exact local base change.
Expanding Az=(0,F) directly gives all three identities (19) in
Selmer H2. Projection to ordinary H2 recovers the old cup relations
and loses the local terms, so it cannot replace this calculation.
The positive local coordinate inclusion j+ is explicitly defined.
The natural coefficient connecting map is [A_j x]; under inverse
character action the global version is minus cup with c_j.
The height Bockstein separately negates the natural connecting map.

## 5. Repaired Coleman coefficient argument

The former assertion that an arbitrary local basis has a Coleman
power-series germ did not follow from the existence of its finite
augmentation value. An inverse limit of rational finite group
algebras alone does not justify that analytic assertion. I requested
its removal. The final proof needs only the actual global class.

I directly checked [BKS1910.07404v2](https://arxiv.org/pdf/1910.07404v2),
the definition after (6.4.1), Lemma6.14 and its proof. For the
actual w_infinity, local freeness and z_cyc=T w_infinity give
loc^-(w_infinity)=F(T,T)e_L/T. Its linear coefficient is
(F20+F11+F02)e_L0. The definition uses positive coefficient
inclusion, so this is Rubin's derivative without an extra sign.
The proof of the Coleman lemma only needs the established finite
local condition of w0. It gives
c2=O_p(e_L0)(F20+F11+F02). Neither Sha finiteness nor an arbitrary
local Coleman factorization is needed for this application.

The functional O_p and delta0 keep their fixed normalization;
its nonzero value on the local basis is not declared a p-unit.
All coefficient comparisons are rational when they divide local
logarithms or Euler factors. The old height formula and final
p/(2#E(F_p)) factor therefore remain unchanged.

## 6. Determinant order and remaining scope

For the square A, the constant kernel and cokernel both have
dimension r. Schur complementation leaves a matrix with zero
constant term and linear part X B_pi+Y B_barpi. Its determinant
has order at least r, and its degree-r term is the determinant
of that linear part in the induced frames. The invertible block
determinant, u(0) and (-1)^b remain. No height nondegeneracy is
inferred from this formula.

Perfect specialization preserves the integral determinant basis
but retains H2 and any extra Selmer directions. It does not supply
a rational object before p-adic completion or identify its real
period with the complex BSD coefficient. The stated remaining
CM-Presentation-BSD comparison accurately retains those tasks.

Nekovář primary PDF SHA256:
61c84e5ad3252a2e520747215ac57a282addc2b58c824a3637bcd77bbe02153f.
Kato primary PDF SHA256:
3c6e14b11fa60262db8aff782ce3cf4d83e9100c0be83621a7e4ce502cec605d.
No numerical certificate was rerun for this review.
