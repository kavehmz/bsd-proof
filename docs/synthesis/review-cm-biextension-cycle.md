# Independent review of the relative CM construction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed [CM biextension cycle](cm-biextension-cycle-attack.md), all six
sections and Propositions 1–7. **PASS with the explicit secondary-regulator
scope below.** The arithmetic theta comparison remains an unproved gap.

## 1. Ordinary cycle and the relative object

The symmetric-square argument proves z+τz=0 rationally: Sym²(E) is a
P¹-bundle over Pic²(E), its CH₀ pushforward is an isomorphism, and the
image of the four-point cycle is zero by the elliptic group law. Pullback
by the flat degree-two quotient produces z+τz, including multiplicities
on the diagonal. The argument does not assert that the antisymmetric
cycle itself is zero in CH₀.

Its degree and Albanese image are zero. For zero-cycles on a smooth
projective surface those are exactly the ordinary Deligne cycle-class
data, so that regulator vanishes. The Künneth sign is also correct:
geometric exchange is minus ordinary exchange on H¹⊗H¹. The geometric
minus component therefore realizes Sym²H¹, not the Tate determinant.

The six-point pair has disjoint supports. The generalized Jacobian has
torus character lattice Div⁰(B), and the two boundary sequences give
rank-six relative H₁ with graded ranks two in weights 0,−1,−2.
The two displayed third-kind forms have residues +1 at B_j and −1
at T, with cancellation at O. At T the factor dx/(2x) has residue one
because x has a double zero. The signs of the negative y-coordinates
in the numerators of (6) are correct.

The curve/1-motive construction is within Deligne's known theory; the
subsequent exterior tensor is being used with its specified realizations.
The note explicitly declines to identify it with an ordinary CH² class
or an Ext² class in mixed Hodge structures.

## 2. All finite intersections and normalization

**[NEW, independent reconstruction]** The displayed minimal discriminant
and conductor give two components at each bad prime 2,3,13. Integral j
excludes multiplicative reduction, so the types are III (including wild
reduction at 2). The nonidentity component has self-intersection −2.
Adding half the intersection with this component makes a degree-zero
divisor orthogonal to both components; its contribution against the
other divisor is r_i s_j/2.

Direct reduction of the six coordinates gives r_i=s_j=1 at 2;
r_i=1 and s_j=−1 at 3; and r_i=s_j=0 at 13. These statements refer to
degree-zero divisors, not merely to the individual points' components.

The coordinator independently reconstructed the rational group law using
Python Fractions. It verifies B₁=(13,−52), B₂=(13/9,−208/27),
P−Q=(49/4,385/8), and both cross-difference x-coordinates 156/49.
The resulting formal-group intersection depths occur only at 3 and 7:
the horizontal matrices are [[0,−1],[−1,−2]] and [[0,1],[1,0]].
Together with the vertical terms, they give exactly the three matrices
in (8), and no correction at 13 or another prime. The argument uses
all denominators of the relevant difference coordinates, not a finite
scan offered as an all-prime proof.

The signs and normalization were checked in the primary sources:
[Bloch–de Jong–Sertöz, §4.1, equations (4.3)–(4.4)](https://arxiv.org/html/2206.01220v2)
use the real part of the purely-imaginary-period-normalized integral
at a real embedding and minus the corrected finite intersection.
[Balakrishnan–Besser, (2.1) and Corollaries 4.2–4.3](https://arxiv.org/html/1201.6016v2)
use the stated idèle character and give −2 log σ_p plus the denominator
term, agreeing with the previously fixed SW quadratic-height convention.
The usual degree-one theta height is half the BSD x-height convention;
the divisor Néron pairing here gives the BSD bilinear matrix.

Finally, exact rational arithmetic checks
$$\prod_{\ell=2,3,7}\ell^{-2C_{\ell,ij}}
=\begin{pmatrix}3/2&27/98\\27/98&243/2\end{pmatrix}_{ij}.$$
Thus (9) retains every finite-place term and every factor of two.
No old analytic or p-adic certificate was rerun.

## 3. Corrected algebraic lifts and secondary determinant

Normalized local pairings descend to J_B: a modulus relation has equal
values at B₁,B₂,T, so its evaluation on each e_j is one and its logarithm
is zero. The torus coordinates may therefore be chosen algebraically
with the stated logarithmic orientation. Replacing u(d_i) by
2u(d_i)+ι(r_i) and using frame b_i/2 adds exactly half log r_i to its
period row. The abelian image of that rational frame remains P_i.
This verifies the corrected algebraic 1-motive and its full height block.

For relative product chains, the boundary lies in A×U∪U×A and Fubini
gives the determinant in (12) with no extra factor. Exchange of two
degree-one chains introduces a minus sign, so this chain is geometrically
plus while realizing the ordinary exterior square. The graded ranks
1,4,5,4,1 sum to fifteen, as required for ∧² of a six-dimensional space.

The derivation calculation is exact: the square of the central-block
action on a₁∧a₂ is twice N(a₁)∧N(a₂), giving the factor 1/2 in (14).
This is a **secondary height operation with the specified local splittings**.
It is not an ordinary holomorphic period of a pure Tate object, a rational
motivic endomorphism supplied by the height matrix, or an ordinary cycle
class with that regulator. Those exclusions are mathematical scope, not
missing normalization fixes. The frame line and the fifteen-dimensional
tensor realization are correctly distinguished.

## 4. The two tested arithmetic maps and the remaining target

For a source 1-motive whose lattice has torsion abelian image, any map
to the constructed target sends its lattice to a rational combination
of P,Q which is torsion. Independence forces that combination to be
zero, over every number field. This checks Proposition 6; it does not
cover arbitrary higher extensions or an unproved inverse-limit operation.

For Proposition 7, the exact character obstruction is the Poincaré
pushout class n₁P+n₂Q in Ext¹(E,G_m). It is nonzero for every nonzero
integer pair, and a character trivial on the torus would factor through
the proper abelian variety. Thus J_B has no nonzero algebraic character.
This rules out that specific character extraction, while leaving other
rational-function or higher-regulator constructions subject to their own
arithmetic conditions. It does not prohibit every alternative comparison.

The rational line in §6 is an actual line of the two lattice frames,
equipped with the explicitly defined secondary realizations. Constructing
its requested rational element from the theta side is still (16). Its
first realization would prove complex rationality, rather than assume
it by choosing an arbitrary embedding or assigning a real coefficient.
Nothing in this review proves (16), universal regulator nondegeneracy,
full Sha finiteness, or BSD. The bounded construction and its two
specific map obstructions are the results accepted here.
