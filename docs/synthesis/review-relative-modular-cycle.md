# Independent review of the relative modular cycle

Date: 2026-09-12. Reviewer: `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Reviewed [the full proof](relative-modular-cycle-attack.md) and
[checkpoint](relative-modular-cycle-checkpoint.md), including the final
tensor obstruction in §9.

**PASS with the explicit scope below.** The actual point/divisor
construction, cancellation at every finite prime, rank-six 1-motive,
BSD height formula, specified projected-loop contraction and rational
tensor obstruction are correct. The source creates a target lattice;
it does not establish its required analytic element.

Reviewed SHA-256: proof
`23ef0cc8a1e02d7f3acf0f6eecaeb092b1f5581b1b72c6a6729c1f7198fec925`;
checkpoint
`2ffcc6151dfaeed3bc809c3610ee36988155bf04726293934ce802b4c6afacab`.

Two clarifications were requested: the full-period Betti sublattice
has index two, and the pulled-back chains must avoid the pullback
punctures. These make intended hypotheses explicit and require no
change to a formula. The primitive point lattices and the nonprimitive
full-period factor must remain distinguished in subsequent uses.

## 1. Independent exact arithmetic

I recomputed the group law with Python Fractions on
$y^2+y=x^3+x^2-2x$. For distinct x-coordinates, put
$\lambda=(y_2-y_1)/(x_2-x_1)$ and $\nu=y_1-\lambda x_1$;
then the sum has coordinates
$$x_3=\lambda^2-1-x_1-x_2,\qquad y_3=-\lambda x_3-\nu-1.$$
This gives
$$R=(4,8),\quad S=(-51/25,-68/125),\quad T=(1/16,-9/64).$$
All five affine points were checked to satisfy the equation exactly.

The two denominator lines in Lemma 2.1 have slopes 7/5 and 9/4,
and pass through P,R and Q,R respectively. Their third intersections
are −S and −T. Subtracting their divisors from those of the numerator
vertical lines gives precisely B₁−D₁ and B₂−D₂. This also verifies
the moving-function signs at O.

The primitive projective vectors in §3 are correct. Independent
gcds of their 2×2 minors, with rows P,Q,O and columns S,T,R, are
$$\begin{pmatrix}1&1&1\\3&1&1\\5&4&1\end{pmatrix}.$$
The minor computation really measures intersection on this model:
sections are closed immersions into the regular surface, their fiber
product agrees with that in projective space, and on a chart with a
unit coordinate the minors generate their coordinate differences.
The quotient length over the local base ring is its valuation.
The sections are distinct generically, so the surface intersections
are proper. The model at 389 is regular even though its fiber is nodal.

Every fiber is irreducible of multiplicity one. Since each Dᵢ has
degree zero, it is already orthogonal to every vertical component,
which here is a full fiber. Thus no omitted vertical correction
affects the resulting matrix
$$I=\begin{pmatrix}-\log5&-\log4\\\log3-\log5&-\log4\end{pmatrix}.$$

Substitution into h₁,h₂ independently gives values (5,4) at P
and (5/3,4) at Q. At O, 1/(x−4) has positive order two and
$y/(x−4)^2$ positive order one, so both values are exactly one.
Their possible poles at x=4 avoid O,P,Q. Hence the modified divisors
Zⱼ remain rational, degree zero, and disjoint from the punctures.

## 2. Cancellation really occurs at each prime

For each p, intersection with the model principal divisor of h is
$v_p(h(P_i)/h(O))$. The difference between this model divisor and
the closure of the generic principal divisor is vertical. Every
vertical divisor is a sum of full fibers, so its pairing with Dᵢ
is zero. This argument explicitly includes denominator primes of
h₁,h₂ and the bad prime 389; it does not assume that these functions
are units on the whole integral model.

The prime contributions are transparent: column one has −1 at 5
in both rows and +1 at 3 only in the second row. Column two has −2
at 2 in both rows. The h-values supply +1 at 5 in column one,
−1 at 3 only in its second row, and +2 at 2 in column two. At all
other primes every listed valuation is zero. Thus each individual
finite intersection is zero after modification, not merely their
weighted real sum.

No height or L-value entered this computation. It is an exact
calculation from the rational marked divisors.

## 3. Algebraic marking and the integral Betti lattice

The generalized Jacobian for A={O,P,Q} has torus character lattice
$\operatorname{Div}^0(A)$ of rank two. A rational divisor away from A
defines a rational point of that generalized Jacobian. Thus (4.1)
is an actual algebraic 1-motive over Q, with integral lattice marking
Z₁,Z₂ and abelian images P,Q.

I checked the primary descriptions in
[Sertöz–Ouaknine–Worrell, 2505.20397v1, Definition 6.1.10 and Proposition 6.5.43](https://arxiv.org/html/2505.20397v1).
They give precisely the relative Jacobian and the pullback of homology
along a prescribed lattice of endpoint divisors. No transcendence
algorithm or period conjecture is used in this application.

The integral rank assertion also follows directly: H₁(E\A,Z) has
rank four, with two independent puncture loops and two compact
elliptic cycles. Pulling the relative boundary map back along
$(n_1,n_2)\mapsto n_1Z_1+n_2Z_2$ gives an extension of Z² by Z⁴.
Surjectivity follows because every degree-zero endpoint divisor bounds
a chain on the connected punctured curve. It is therefore free of
rank six. The three weight ranks are 2,2,2, exactly as stated.

The marking is not required to define a smooth semiabelian model over
every prime. Its finite symbols were instead handled on the regular
arithmetic surface. The note explicitly preserves that distinction.

## 4. Height sign, factor and the outer lattice

Writing Y=2y+1, the residue-one form at (a,b) is
$$(Y+2b+1)\,dx/(2(x-a)Y).$$
Substituting P and Q gives the two forms in (5.1). Their apparent
inverse-point poles cancel, and each has residue −1 at O. The
normalizing coefficient in (5.2) is also correct:
if τ=it₀ then Re(cᵢτ)=Re Bᵢ, while Re cᵢ=Re Aᵢ.
Small puncture loops only add integral multiples of 2πi.
Consequently all periods of ηᵢ are imaginary and the real integrals
are independent of the chosen chains.

I checked the signs against
[Müller, 1105.1719v3, Definitions 2.3, 2.6, Proposition 2.8 and Theorem 3.2](https://arxiv.org/html/1105.1719v3).
His finite symbol is positive intersection times log p, its principal
rule is −log|h(D)|, and the full symbol is the negative Néron–Tate
pairing. Here the real Green function is −Re∫η, so these conventions
give H=S−I before correction and H=Re∫η afterward, as claimed.
His genus-one height is the x-coordinate limit, with polarization
divided by two, matching the BSD/Cremona convention already fixed.
No additional factor of two is introduced by the real place.

The Poincaré/biextension interpretation was checked in
[Amini–Bloch–Burgos Gil–Fresán, author PDF, Theorems 4.10–4.11 and Proposition 4.12](https://www.math.ens.psl.eu/~amini/Publications/Feynman.pdf).
The explicit Green/principal-divisor normalization in this note
controls its own sign, rather than copying a boundary orientation
without adjustment. The determinant is a secondary, quadratic
height operation with weight drop four; it is not the linear height
of one ordinary rank-one biextension.

The two point lattices are saturated by the certified full basis.
The Betti factor is different: the primitive plus generator a has
period Ω_E/2 because E has two real components. The sum of the two
oriented real components is 2a, so the specified Zγ_R in (6.1) is
an index-two sublattice of H₁(E,Z)⁺. With that explicit sublattice
the generator maps to Ω_E Reg, exactly as asserted. It is not a
primitive Betti generator. The author added this clarification.

If one instead used the primitive plus lattice, its generator would
have half that value. An integral analytic element there would only
imply a half-integral normalized quotient; the previously certified
narrow interval would still force that quotient to equal one.
Neither version of the requisite analytic-lattice comparison has
been established here. This observation supplies no Sha-finiteness
claim.

## 5. Pullback and the specified projected cusp loop

The degree 40 is taken from the prior exact modular-symbol and
integral-homology calculation in
[the reviewed visibility note, §6](modular-visibility-attack.md).
It was not recomputed through a numerical modular-degree routine.
The differential factor cπ is retained symbolically, with no unit
or Manin-constant assumption inserted into a leading-term formula.

For the pullback formula, chains must lie in
$X_0(389)\setminus\pi^{-1}(A)$. They exist because their endpoint
divisors avoid those punctures and have degree zero. Their pushforward
boundary is 40Zⱼ, including ramification. Subtracting 40γⱼ gives
a closed chain in E\A, and its ηᵢ integral has zero real part.
This proves the factor 40 in (7.1), hence 40² in the determinant.
Those factors cannot be divided away in an integral conclusion.

For the imaginary-axis cusp path, the rational Fourier coefficients
make the lift F(y) real. Cusp decay extends it continuously to the
endpoints, and L(E,1)=0 gives F(0)=F(∞)=0 as actual real numbers,
not merely as lattice classes. P,Q lie on the nonidentity real
component, whose lifts have imaginary part b/2 modulo b, while O
has imaginary part zero modulo b.

The displayed homotopy stays at imaginary height ε with 0<ε<b/2.
It therefore avoids every lift of O,P,Q and fixes its two endpoints.
It contracts the particular shifted loop. Even though the strip's
image in the elliptic curve is a cylinder, the real lift returns
to zero, and this explicit contraction has no winding obstruction.
Flat holonomy on it is the identity.

Holomorphic one-forms on the punctured complex curve are closed and
have zero pairwise wedge. Their finite unipotent word connections
are flat, so each positive-length Chen coefficient on this loop is
zero. This only concerns the specified translate/regularization and
connections descended to E\A. It does not identify the original
Mellin-decorated object with that loop or cover arbitrary cusp
indentations, modular extensions, or extra boundary information.

## 6. The final tensor obstruction

The modular function Δ(z)/Δ(389z) has no zeros or poles in the upper
half-plane and has divisor 388(0−∞), from its cusp orders. Thus the
point defining M_c is torsion and its rational Hodge realization
splits into Q(0) and the pure weight-minus-one H₁ of the Jacobian.
The elementary 1-motive morphism obstruction follows from compatibility
with this torsion point and the independent P,Q.

For the tensor-square test, consider the quotient of ∧²H(M) by
weights at most −2. Its lower part is H₁(E)⊗L and its top part
is det L. Expanding the wedge of two lifted lattice generators
modulo lower weight gives the extension class
$$[P]\otimes e_2-[Q]\otimes e_1.$$
The principal modifications and torus part do not affect this
quotient. The two components cannot cancel. A rational elliptic
point extension is zero precisely when its elliptic logarithm is
a rational lattice period, which after clearing denominators is
precisely the torsion condition. The displayed extension is nonzero.

The source H(M_c)⊗² has a split Q(0) summand and all other summands
of negative weight. Weight compatibility prevents those other
summands from contributing to the target top. A nonzero map on the
top would therefore give a lift from Q(0); after dividing by its
nonzero rational scalar it would split the preceding nonsplit
extension. This proves Proposition 9.2. It does not exclude a
different higher source with a nonsplit top extension.

The actual higher comparison RM-389 remains missing. This review
establishes no analytic integrality, no full Sha finiteness, and no
proof or disproof of universal BSD.

Only this review file was edited. The new rational group-law/minor/
function checks above were elementary exact calculations; no old
analytic or arithmetic certificate was rerun.
