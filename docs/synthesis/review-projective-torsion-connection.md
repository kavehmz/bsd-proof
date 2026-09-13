# Coordinator review of the torsion-connection obstruction

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
**PASS for all seven sections of
[the proof](projective-torsion-connection-attack.md), after the recorded
global-descent scope clarifications.** The final §7 distinguishes the
complete algebra's character support, a marked singleton, its scalar
endomorphisms and the permitted global Kummer adjustment.
Reviewed mathematical revision SHA256:
`a60a66ce76a0f6c8a5631a96860fd3520e7a8f6b2e77fcc66fac18d254fdff0d`.
Subsequent review links and checkpoint updates are editorial.
No old numerical certificate was rerun.

## 1. The exact finite-flat differential

The two canonical trivializations are compatible through the rigidified
Poincaré biextension. Pulling an integral connection back by [n] and
writing it in the canonical frame gives d+a. Its n-th tensor power is
both d+na and the pullback d+nb of the connection on the trivial n-th
power. Invariant differentials pull back by multiplication by n. The
base DVR has no n-torsion, so a=b. This comparison is integral; it does
not divide an unknown residue class by n.

Translation of the canonical frame by the character χ changes the
connection form by dlog χ. The translation formula for an invariant
one-form has both the elliptic and the finite-group component. Keeping
the latter proves o_n(t)=χ_t*(dz/z) in ω_E/n. This is a calculation on
the group scheme, including its nonreduced fibers. A calculation only
on generic geometric points would not prove it. The chosen frame
convention fixes its sign.

For n=mp^r the tensor-power compatibility multiplies the p-primary
obstruction by m. Because m is a p-unit, the nonvanishing test survives.

## 2. Ordinary kernel and exact coefficient

The multiplicative connected subgroup becomes μ_(p^r) after a finite
unramified extension, without splitting the whole connected–étale
sequence. Its cotangent module is the same as that of E[p^r], since
the quotient is étale. The stated differential u is thus a unit in
R/p^r. A dual point whose quotient coordinate is a restricts to the
character z↦z^a. Differentiation gives exactly (a/u)ω, proving both
the formula and the connected-dual kernel.

After a finite splitting extension a point with quotient coordinate one
exists and extends integrally by properness of the finite group scheme.
Its differential remains a unit modulo p^r after any further extension.
The kernel conclusion concerns points but follows from the full
character factorization through the étale quotient.

## 3. Supersingular valuation and coefficient levels

Root read Fargues' primary author version, dated 20 October 2011:
[canoniqueHN.pdf](https://webusers.imj-prg.fr/~laurent.fargues/canoniqueHN.pdf),
§2.5 Lemma 4, §5.4 Theorem 3 and §6.5 Lemma 9. Its pages 13,25,32
correspond to the published statements cited by the author. Lemma 9
specifies both the representative valuation and the annihilator of the
torsion differential. Theorem 3 supplies the universal linearized
cokernel bound; it has no small-Hasse assumption. The adjacent
canonical-subgroup theorem is not used in the supersingular argument.

For a curve over an unramified base, the reduction of [p](z)/z has
first unit coefficient in degree p²−1, and all preceding coefficients
are divisible by p; its constant term has valuation one. Weierstrass
preparation gives an Eisenstein polynomial, so all nonzero p-torsion
parameters have valuation 1/(p²−1). This uses the original unramified
base even after the points are placed in a ramified splitting field.

The cyclic closure H is finite flat and its quotient is an elliptic
scheme with good reduction. The special-fiber quotient is purely
inseparable of degree p. Its formal isogeny therefore has distinguished
degree p, and its derivative is a unit times the product of its p−1
nonzero root parameters. Thus v(a_H)=deg(H)=1/(p+1).

The dual of H→E[p] is the restriction of q_H:E→E/H under the canonical
principal polarizations. The isogeny Weil pairing verifies this on the
generic fiber, and flatness extends the identity. Its map on invariant
differentials is actual multiplication by a_H. It is not the derivative
of the opposite isogeny, nor a map to a rescaled saturated image.

In the intrinsic differential module of H^D, the representative valuation
is 1/(p²−1), strictly below its annihilator valuation p/(p+1).
The actual pullback adds 1/(p+1). The result p/(p²−1) is strictly
below one, so it is a well-defined nonzero class modulo p. Changing
integral generators only multiplies these values by units.

At higher level, restriction to E[p] is reduction on the differential
module and corresponds on the dual point to multiplication by p^(r−1).
Inclusion of a point of order p^s instead multiplies its obstruction
by p^(r−s). These are different compatibility maps. They give precisely
r−s+p/(p²−1), strictly below r. No zero-class representative is assigned
a spurious valuation. The universal cokernel bound supplies an independent
existence of a nonzero obstruction even without the unramified hypothesis;
on O_C/p^r, an element of valuation 1/(p−1)<1 cannot annihilate the
whole target for p≥3.

## 4. Saturation and independence of the algebra model

The saturated intersection with a generic horizontal line is coherent:
locally it is a submodule of a finite module over a noetherian ring.
The quotient embeds in the pushforward of a locally free quotient on
the generic integral curve and is torsion-free. At a dimension-two
local ring, the depth lemma makes the rank-one kernel S2; it is already
free at height one. Regularity then makes this reflexive sheaf a line
bundle.

The connection followed by the quotient is O-linear on that kernel,
because the Leibniz term projects to zero. Its target is torsion-free,
as the relative differential module is invertible. Generic vanishing
therefore proves vanishing everywhere. This establishes horizontality
of the actual integral line.

For the good elliptic model the only vertical divisor is its integral
special fiber, which is principal. Thus Picard restriction is injective.
The saturated line is the usual extension of its generic torsion line.
Two generic identifications differ by a constant because the generic
curve is proper; a relative connection is unchanged by that constant.
The connection argument is carried out over finite-extension DVRs,
where noetherianity and surface regularity hold, not by applying that
lemma to the nonnoetherian ring O_C.

The full Poincaré packet contains every torsion-character difference.
After a finite splitting extension its matrix-unit lines are actual
horizontal line subbundles, even though a given character occurs with
multiplicity. One line with the nonzero obstruction above contradicts
any proposed regular extension of the fixed algebra connection. This
proves Theorem 5.1 for the stated good p≥3. It already occurs in the
Brauer-zero control and therefore proves no nonzero Sha class.

## 5. The positive ordinary block is an actual integral construction

Local solubility and the chosen local origin identify T with a division
fiber of an integral point on the good elliptic scheme. Its quotient
by the connected dual subgroup is a finite étale torsor. A finite
unramified extension supplies a section; its inverse image is a finite
flat connected coset, with its complete scheme structure retained.

The dual isogeny of the connected quotient is finite étale, of degree
p^r. Pullback of the Poincaré family to it is schematically constant
in the coset parameter up to one common rigidified line. Pushing forward
therefore gives equation (6.2), including nilpotent fibers. Its
endomorphism algebra is a constant matrix algebra. Deck action on that
algebra is constant in the elliptic coordinate, by properness and
connectedness. Consequently the constant differential descends along
the actual étale isogeny. This proves the claimed integral projective
connection, not just separate integrality of its geometric lines.

## 6. Global descent and the remaining task

For the complete ordinary coset block, the set of characters in its
endomorphism bundle is exactly C_r, with multiplicity p^r. This set is
intrinsic and unaffected by a common line twist. Its algebra descent
would force C_r to be G_Q-stable. Surjectivity of the residual image
at the stated primes excludes its nonzero p-torsion line.

For a G_Q-stable marked subset S whose differences lie in C_r, those
differences generate a stable cyclic subgroup. It must be zero, hence
S is a singleton. A singleton descending as a marked weight gives a
point of that fixed finite torsor. Descent of its scalar endomorphism
algebra alone does not: every geometric line has scalar algebra O.
For the original Brauer class, vanishing is equivalent to triviality
of an appropriately global-Kummer-adjusted torsor; the fixed unshifted
T need not be trivial merely because the Brauer class is zero.

These statements retain the p-primary scope of the subpacket argument.
They do not classify every possible new geometric construction. GAP
TC-389 still requires a global arithmetic splitting or a uniform degree
bound beyond the tested finite-monodromy packet. No p-curvature conjecture,
Sha finiteness, or full BSD conclusion is inferred.
