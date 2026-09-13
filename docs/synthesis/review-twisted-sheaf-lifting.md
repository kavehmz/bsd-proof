# Independent review of the global twisted-sheaf construction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
Reviewed [twisted-sheaf lifting](twisted-sheaf-lifting-attack.md), §§1–8,
the added elementary transform, and the generic K₀ consequence in §10.2.
**PASS after the two stated precision repairs.** The detailed Fourier–Mukai
kernel and descent review is separately recorded in
[review-twisted-fm.md](review-twisted-fm.md), also PASS.
No uniform rank, splitting degree, or Sha annihilator is obtained.

## 1. The degree normalization and stable bundle lemma

The Kummer lift can be made geometrically zero by subtracting the
degree-one zero-section class. Its zero-section restriction is zero by
fppf Kummer over Z. At every completion, the Brauer class is zero by
the reviewed arithmetic-model identification, so the Kummer lift is
represented by a degree-zero line after adjusting by an n-th power.
The μ_n root gerbe therefore has the stated tautological local line.

The genus-one degree-one bundle lemma is valid over the original field
and remains stable geometrically. The nonzero extension class is in a
one-dimensional space and stays nonzero after field extension. A putative
destabilizing subbundle has degree at least one. Either its image in the
preceding stable bundle has smaller rank and degree at most zero, or it
gives a full-rank degree-one isomorphism splitting the extension. Both
are contradictions. Conversely, the unique section of a stable bundle
cannot vanish, and its quotient is stable; this proves the claimed
geometric uniqueness by induction. Serre duality and Riemann–Roch give
h¹=0 and h⁰=1. No genus-at-least-two moduli theorem is used.

## 2. The base-field descent really succeeds

The fixed determinant stack has scalar automorphisms preserving the
determinant, namely μ_n. One geometric isomorphism class alone would
not exclude infinitesimal deformations. The reviewer requested, and
the author added, the missing rigidity justification: Serre duality
makes trace on H¹(End V) an isomorphism to H¹(O), dual to the scalar
inclusion on H⁰. In characteristic zero this gives H¹(End₀ V)=0,
and H²(End₀ V)=0 on a curve. Thus the fixed determinant moduli is
indeed étale locally the claimed gerbe. Alternatively, the descent
gerbe of the chosen object directly gives the same obstruction.

The local ordinary determinant is O(O)⊗M_v⁻¹, so tensoring its
stable rank-n bundle with the tautological root line gives determinant
O(O), exactly as required. Hence the obstruction class in
H²(Q,μ_n)=Br(Q)[n] vanishes at every place. Brauer–Hasse–Noether
neutralizes this **base-field** gerbe and supplies the global twisted
bundle. This does not neutralize the original gerbe on E.

## 3. Rank-preserving extension to the actual arithmetic surface

The reviewer fetched [Lieblich, math/0511244v4](https://arxiv.org/html/math/0511244v4)
and checked Lemmas 3.1.1.8, 3.1.1.12, 3.1.3.1 and the regular-surface
extension/Azumaya statements in §§3.1.2–3.1.3. The proof uses the
change-of-band equivalence and coherent extension; it does not import
the geometric-surface period-index theorem into mixed characteristic.

A second requested repair makes the local-freeness argument precise:
the étale neighborhoods are U→𝓔 on which the G_m-gerbe is neutral.
There weight-one sheaves identify with ordinary modules on the regular
surface U. They are not étale scheme atlases of a G_m-gerbe. Coherent
extension followed by the reflexive hull then preserves the generic
rank and is locally free in dimension two. Descent retains the twisting.
The Picard restriction isomorphism fixes its extended determinant class;
choosing an integral isomorphism is allowed to change the original
generic isomorphism by a rational scalar.

End(V) has weight zero and descends as an Azumaya algebra of degree n.
Its determinant is canonically trivial, since conjugation on matrices
has determinant one. The reviewed ordinary K₀ ring therefore gives
[End(V)]=n²[O]. This is a statement after forgetting multiplication;
the Brauer class has not been forgotten in the Azumaya category.

## 4. Torsor/Poincaré construction and the exact rank obstruction

For a locally soluble genus-one torsor of period n, the rational
degree-n Picard class has zero Brauer descent obstruction: locally
there are points and the field Brauer obstruction is zero everywhere.
Brauer–Hasse–Noether then gives a line bundle, and Riemann–Roch gives
an effective divisor of degree n. Because each closed-point degree is
a multiple of n, this is one degree-n closed point. This is the
previously reviewed individual period-index argument, not a uniform bound.

The Picard gerbe is normalized by O_C at the origin of Pic⁰(C).
The explicit change-of-origin cocycle fixes its sign relative to β;
choosing the inverse torsor when necessary retains the same period and
local conditions. Normalization removes any constant Brauer ambiguity.
Pushing the universal line from the degree-n point is a finite flat
pushforward of an invertible sheaf and gives a genuine rank-n twisted
bundle. The splitting construction after number-field base change and
regular resolution has degree n; generic Brauer injectivity applies
on that regular resolution, as the note states.

Taking determinants of the twisted gluing matrices proves rβ=0 for
every twisted bundle of rank r. Together with the constructed rank n
this proves the exact minimal twisted rank, generic index n, and rank
image nZ. Ordinary tensor products and exterior powers change the twist
and cannot be used to take rank-one roots in the same category.

The Severi–Brauer/rank-one equivalences in §7 are correct by generic
Brauer injectivity. Framing twisted lines at O removes scalar
automorphisms, but their coarse moduli is the original genus-one torsor,
not the rational coarse point used in §3. That distinction preserves
the missing global-point problem.

## 5. The explicit elementary transform and the lattice calculation

The added construction starts with W from the degree-n point D and
the extension vector 1 in its residue field, with the specified tangent
frame at O. Geometrically W is a direct sum of n pairwise distinct
degree-zero Poincaré lines, and each component of this vector is nonzero.
A nonzero local extension vector makes the elementary transform locally
free. A destabilizing subbundle would intersect W in a degree-zero
subbundle and map onto k(O). Such a subbundle of W is a proper sum of
the distinct degree-zero summands. The nonzero extension component in
each omitted summand prevents that subextension. This proves stability
and produces rank n, degree one; the determinant normalization via
det(W) retains the original Brauer class.

The Fourier–Mukai identification of this bundle with the transform of
O_C(−D) is checked separately in the kernel review. It returns exactly
that degree-n divisor class, without supplying a degree-one divisor.

For the generic-curve K₀ statement, every rational Picard class on C
has zero obstruction by the same local-solubility/Brauer argument.
Thus Pic⁰(C)=E(Q)=Z² and its degree image is nZ, split by D. The
curve rank-and-determinant theorem gives K₀(C)=Z⁴. Via the stated
derived equivalence, twisted K₀(E) is also abstractly Z⁴. This does
not assert the same group calculation for the integral twisted model.

The numerical image on E is exactly nZ⊕Z: ranks are divisible by n,
and the constructed classes (n,0),(n,1) generate it. Riemann–Roch
gives the Euler form r d′−r′ d. In a primitive basis of this image
its matrix has off-diagonal entries n and −n and determinant n²;
its radical in full K₀ has rank two. Thus the actual finite free group
of fixed abstract rank retains the individual period in its integral
embedding and pairing. No nontrivial β for 389a1 is asserted to exist.

The positive constructions and these obstructions pass. A uniform bound
or a rank-one splitting still requires the new arithmetic statement
TS-389/HB-cycle; none has been proved by these constructions.
