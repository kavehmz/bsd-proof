# Independent review of the arithmetic-surface Weil–étale attempt

Date: 2026-09-12. Reviewer: `/root/higher_period_integrality`, GPT-6 Astra,
xhigh reasoning. Assigned review files were the coordinator's proof,
its exact-check script, and its stored output.

## Verdict

**PASS.** The regular/flat model, Picard restriction, real-place Brauer
identification, stated low-degree integral motivic cohomology,
finite-generation equivalence, zeta factorization, and compact Selmer
limit lemma hold with the stated scope. No source theorem used here
proves the missing finite Brauer group. No required correction to the
coordinator's note was found.

The full [proof](weil-etale-lattice-attack.md), script, and output were
read, as were the relevant source premises and Proposition 8.1 in
[the Hecke–Brauer note](hecke-brauer-annihilator-attack.md). Only this
review file was edited.

Reviewed SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `docs/synthesis/weil-etale-lattice-attack.md` | `5f257bddf7bc5865378a9569080e22a79239f7f6d87078bdd7ba15bba921c5a7` |
| `docs/synthesis/hecke-brauer-annihilator-attack.md` | `fd96cda5da49d7351a6b63c9cfba6f43befe6e6ee6bd439e7a1b64be367d43a6` |
| `compute/scripts/arithmetic_surface_check.py` | `c3e711b0c718c1afdbea80fd5fdf82492c4d568f3825fb3af2bec9299ac6c2e6` |
| `compute/data/arithmetic_surface_389a1.json` | `c52dc80dba3de6740c7521b7556cfe04af00232e3b7182200a0ba739e5b6f6c2` |

## 1. The actual model

**[NEW, independent verification]** The homogenized equation has the
claimed affine coefficients \([a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0]\).
Its b-invariants are 4,-4,1,-3, giving
\(\Delta=389,c_4=112,c_6=-856\). Thus every fiber away from 389 is
smooth. At infinity the only point is O=[0:1:0], and the derivative
with respect to Z there is nonzero.

At the displayed lift of the node, the derivatives in x and y vanish
modulo 389, while the constant term is 389 times a unit. Hence in the
ambient regular local ring with parameters 389,u,v the equation lies
in the maximal ideal but not its square. Its quotient is a regular
local ring of dimension two. Away from that point smoothness of the
fiber implies regularity of the total space.

The translated special-fiber equation

$$v^2=u^2(u+120)$$

also proves **geometric** uniqueness of the singularity, beyond the
script's rational-point search. Over the algebraic closure, singularity
requires v=0 and u(3u+240)=0, while the equation requires u=0 or -120.
The only common possibility is u=0. The tangent slopes are the two
distinct square roots 148 and 241 of 120.

The polynomial is geometrically irreducible: in the rational function
field in u, u+120 is not a square, so v^2-u^2(u+120) is irreducible.
The parameterization u=t^2-120, v=t(t^2-120) gives its normalization
and the two distinct rational preimages of the node. There is no
additional component at infinity.

For completeness, the flatness sentence admits the following elementary
justification. Let G be the primitive homogeneous cubic and
A=Z[X,Y,Z]/(G). For every prime p, G modulo p is a nonzero polynomial.
If p h=Gk, reduction modulo p in the polynomial domain implies k=p k_1,
so h=Gk_1. Thus multiplication by p is injective on A. The affine
localizations and their degree-zero parts defining Proj(A) are likewise
torsion-free over Z, hence flat. This proves flatness without inferring
it solely from a rational point or from generic smoothness. Properness
is immediate from the projective construction.

## 2. Picard restriction and units

**[NEW, independent verification]** Divisor closure on a regular
surface makes restriction Pic(model) to Pic(generic fiber) surjective.
A rational trivialization of a generically trivial line bundle has
vertical divisor. Since each fiber is geometrically integral and has
multiplicity one, its vertical primes are exactly full fibers, each
the principal divisor of its rational prime. Thus the restriction
kernel is zero.

The rational zero section splits degree, and the usual genus-one
identification Pic^0(E)=E is an identification over Q. The rational
point removes the Picard descent obstruction; no Sha-finiteness
assumption enters. The already reviewed full Mordell–Weil lattice
therefore gives Pic(model)=Z^3.

Any global regular function is a rational constant on the proper
geometrically integral generic curve. Pulling it back along O makes
that same constant an integer. This proves that the global ring is Z
and its units are exactly +1 and -1.

## 3. The entire Brauer group and the real place

The crucial regular-model statement was checked directly in
[González-Avilés, J. Math. Sci. Univ. Tokyo 10 (2003), Lemma 2.2(b), p. 402](https://www.ms.u-tokyo.ac.jp/journal/pdf/jms100207.pdf).
For the proper regular model it identifies the image of its Brauer
group with the kernel of all finite-completion restrictions. This
lemma does not impose the no-infinitely-divisible-Sha hypothesis
present in the paper's main order-comparison theorem. The latter
theorem is not needed for this review.

**[NEW, independent verification]** The section O normalizes every
integral Brauer class because Br(Z)=0. The generic normalized group
is H^1(Q,E), by the rational-point Hochschild–Serre identification,
and this identification commutes with localization. The two section
evaluations at O and Q=(0,-1) vanish.

The cubic after completing the square has three roots in the intervals
listed in the proof. The point with x=0 lies between the smallest two
roots, on the bounded component; O lies on the unbounded identity
component. Thus Q represents the nontrivial real component.

The norm image from E(C) is exactly E(R)^0: it is connected, and it
contains the surjective doubling image of the identity circle. Local
duality therefore pairs H^1(R,E) perfectly with the two-element
component quotient. The zero evaluation at Q forces the normalized
real cohomology class to vanish, and evaluation at O removes any
remaining constant real Brauer class.

The local source inputs were also checked directly: González-Avilés
§1, pp. 398–399, includes the archimedean norm quotient; and
[McCallum, Brauer Points on Fermat Curves, §2, p. 4](https://math.arizona.edu/~wmc/Research/BrauerFermat.pdf)
states the Brauer-evaluation/Tate-pairing identity. This retains the
real 2-primary information rather than invoking odd-primary duality.

All finite restrictions and the real restriction are now zero. Conversely
a Sha class is normalized and locally zero everywhere, so the same
model theorem extends it. Consequently

$$\operatorname{Br}(\mathcal E)\simeq\operatorname{Sha}(E/\mathbb Q)$$

holds as an isomorphism of full groups, without a finiteness premise.
The argument does not infer global Brauer vanishing from evaluation
vanishing; it identifies the unknown group.

## 4. Integral motivic cohomology and Flach–Morin

**[THEOREM, precise source check]** The weight-one identification
Z(1)=G_m[-1] on the small étale site is explicitly recalled in
[Flach–Morin, author PDF, §6.2, p. 71](https://www.math.u-bordeaux.fr/~bmorin/flach-morin-169.pdf).
It gives units in degree one, Pic in degree two, and H^2(G_m) in
degree three, with lower degrees zero. Regularity identifies the
last group with the torsion cohomological Brauer group by injection
into the function-field Brauer group.

**[NEW, independent verification]** The displayed cohomology groups
are therefore genuinely integral groups, not their rationalizations
or their Tate modules:

$$
H^1=\{\pm1\},\qquad H^2=\mathbb Z^3,\qquad
H^3=\operatorname{Sha}(389a1).
$$

Since a torsion abelian group is finitely generated exactly when it
is finite, the claimed finite-generation condition through degree
three is equivalent to full Sha finiteness for this curve.

Flach–Morin Conjecture 3.2 requires finite generation through degree
2n+1. Their Lemma 3.3 compares the small étale and Artin–Verdier
versions using finite 2-torsion corrections. Thus n=1 is exactly the
range just computed, and d-n=1 gives the same dual condition. This
does not assert that the two integral cohomology groups are literally
identical before retaining those real-place corrections.

The source begins §3 by assuming both finite-generation conditions
and Artin–Verdier duality. Proposition 3.4's finite middle group is
therefore conditional on those assumptions. Its proof explicitly
uses finite generation to eliminate Tate modules and then to deduce
that a torsion middle group is finite. It cannot be used to prove
the finiteness premise here.

[Flach–Siebel, arXiv:1909.07465v1, §4](https://arxiv.org/html/1909.07465v1)
independently states the same reduction of L(X_et,1) to finite Brauer
group and finite generation of Pic. The coordinator's note does not
confuse their correction-factor theorem with their conjectural
special-value comparison.

## 5. Zeta function and the stored check

**[NEW, independent verification]** The normalization of the split
nodal fiber is P^1. Over F_(389^m), replacing two rational normalization
points by their one rational image changes the count from 389^m+1
to 389^m. Thus its local zeta factor is (1-389^(1-s))^(-1).
Combining this with the split multiplicative elliptic factor gives
exactly the claimed quotient of good and bad Euler factors:

$$\zeta(\mathcal E,s)=\zeta(s)\zeta(s-1)/L(E,s).$$

The identity first holds absolutely for Re(s)>2 and then defines the
meromorphic continuation. The certified double zero of L, the simple
pole of zeta(s), and zeta(0)=-1/2 give pole order three and coefficient
-1/(2 ell_E). The sign and reciprocal are correct.

The script correctly checks arithmetic invariants, the rational node,
the regularity residue, tangent slopes, and the finite-field count.
Its output labels the cohomological consequences as coming from the
proof, not from the point-count computation.

The script was **not rerun**. The review independently verified that
its stored analytic-input SHA-256 matches the current input file and
that both output endpoints are exactly -1/(2 ell_low) and
-1/(2 ell_high). The map x maps to -1/(2x) is increasing on positive
x, so their order is correct. The geometric argument in §1 verifies
that a rational-node search has not missed a singular point over an
extension field.

## 6. Compact Selmer limit

**[NEW, independent verification]** Under multiplication by p on
E[p^(n+1)] to E[p^n], the Kummer subgroup map is the reduction
E(Q)/p^(n+1) to E(Q)/p^n, while the Sha map is multiplication by p.
The former system is surjective, so its first derived inverse limit
vanishes. Taking inverse limits therefore gives the exact sequence
in Lemma 6.1, with left term the p-adic completion of the finitely
generated Mordell–Weil group, equal to its tensor product with Z_p.

For finite primary Sha, every fixed coordinate in its Tate module
is divisible by arbitrarily large p-powers in that finite group;
it is consequently zero. This removes that primary torsion from the
limit; it does not establish that it was zero before taking the limit.

The example direct-sum group in §6 has finite n-torsion for each n,
zero Tate module at every p, and infinite total order. Its finite
prime-support pieces have the displayed perfect alternating pairings.
The induced global map lands in the finite-support subgroup of the
product of their duals: it is dense because any finite list of
coordinates can be prescribed, and proper because the product contains
elements supported at infinitely many primes. The example proves only
the stated failure of this abstract limit inference; it is explicitly
not an elliptic-curve counterexample.

The review therefore accepts the precise remaining obstruction: a
perfect integral construction retaining the full degree-three torsion
has not been obtained, and its claimed finite generation would already
prove full Sha finiteness for this test curve. The universal rank and
leading-term objectives remain beyond these established inputs.
