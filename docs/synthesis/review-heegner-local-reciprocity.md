# Coordinator review of full-coefficient local Heegner reciprocity

Date: 2026-09-12. Reviewer: coordinator, independently of the author.
**PASS for all seven sections of
[the construction](heegner-local-reciprocity-attack.md), after making
fresh inert conductor primes and squarefree Heegner products explicit.**
Reviewed mathematical revision SHA256:
`630ad951d62671fdb6b1dce97e4ec17bf964a51bd91169ce6e859fbb5b7566b4`.
Later review links and checkpoint updates are editorial.
No old numerical certificate was rerun.

The proof gives full-p-power detecting primes in its explicitly stronger
image range and actual finite geometric evaluation maps. It does not
prove the rank-sensitive vanishing of their toric sums.

## 1. Actual class, hypotheses and exact-order detection

The raw two-prime class is in the plus eigenspace by the already repaired
sign formula. Restriction across K/Q identifies its plus cohomology with
H¹(Q,E[p^k]), since the quadratic quotient has order invertible on the
coefficients. The resulting Q-class has exactly the same order. The
additional full GL₂(Z/p^k) hypothesis is stated separately; it is not
inferred from the weaker irreducibility hypothesis of O5.

The cocycle proof of H¹(GL₂(R),R²)=0 is exact: commuting the central
scalar 2I with g gives b(g)=(g−1)b(2I). Thus restriction to the torsion
field detects the entire cohomology class. Its image W is stable under
all matrix units, obtained from elementary unipotents and their products.
It is therefore I⊕I for an ideal I of R. If the original class has order
p^s, injectivity of restriction makes this image exactly p^(k−s)V.
No primitivity of the original class is assumed.

The field-disjointness step is valid. K ramifies at a divisor of D,
where the torsion field is unramified because E has good reduction and
p does not divide D. Thus K is not in the torsion field. The extra
extension cut out by the restricted cocycle has p-power degree over
that field, so cannot contain the missing quadratic extension either.
This proves the required surjectivity of the translation image after
also imposing the K condition.

Complex conjugation has free rank-one ± eigenspaces on V. The cocycle
value at τ lies in the minus eigenspace. For the chosen translation w
in p^(k−s)V^+ and γ=hτ, the square has coefficient action one and
cocycle value 2w. It has exact order p^s. Chebotarev gives infinitely
many rational primes with the required conjugacy class and any further
finite exclusions. Their traces and determinants give a_v=0 and
v=−1 modulo p^k; their K-Frobenius is the square just computed.
Conjugation of that square changes its translation by an invertible
linear action, so the exact order is preserved. This verifies the
conjugacy-class qualification, not only a chosen group element.

Consequently the fresh-prime maps really detect the zero class and its
full order. Choosing a finite separating subfamily for a finite group
uses this detection iteratively; it is not a fixed matrix independent
of the class, coefficient, or auxiliary conductor.

## 2. The finite isogeny cover and its Frobenius value

At a fresh v, good reduction and v≠p identify the torsion with the
finite étale Etilde[p^k]. Arithmetic Frobenius squares to one on that
module. The idempotents (1±F_v)/2 give free rank-one summands defined
as subgroup schemes over F_v. In particular quotienting by the minus
subgroup is a genuine degree-p^k isogeny. Factoring [p^k] through it
gives the second isogeny with kernel the plus quotient, constant even
over F_v. Both isogenies are étale because their degrees are prime to v.

Finite-field Kummer theory identifies Etilde(F_(v²))/p^k with V:
F_v²−1 is a surjective isogeny on geometric points, so H¹(F_(v²),Etilde)=0.
For a division point V_U, the connecting value is (F_v²−1)V_U.
Mapping V_U through the first quotient proves that the Frobenius
translation in the second cover is exactly its plus projection. The
projection is a defined group quotient; it has no unrecorded modular
degree or factor two. Independence of the division point follows from
the trivial F_v² action on the deck group.

At v not dividing 6N the modular parametrization extends to the smooth
good-reduction modular curve by the Néron mapping property. Pullback
therefore gives an actual étale torsor, with the origin in the infinity
fiber. It need not be geometrically connected. The proof correctly
permits its Frobenius function to be zero or p-divisible.

## 3. Quaternionic geometry, Hecke relations and CM conductor

Root read [Vatsal's primary author version, §§6.6–6.8 and 6.12–6.16](https://www.math.ubc.ca/~vatsal/research/mew3.pdf).
It gives the enhanced supersingular/quaternionic interpretation,
residual isogeny-cover mechanism, and Frobenius/Hecke action. The cited
construction is residual; the proof supplies its own p^k isogenies and
Kummer maps. The extra hypotheses used there for connectedness,
primitivity and a characteristic-zero eigenform comparison are not
imported. In particular the source identifies the new U_v operator
with Frobenius on the degree-zero supersingular module, with the sign
used here.

The Hecke calculation follows directly on the Jacobian: π_*T_r=a_rπ_*,
and the degree-times-infinity term maps to zero. Reduction and the
finite-field Kummer homomorphism are additive, so the function satisfies
all the displayed eigenrelations, with U_v=+1 on the specified new
module. The same argument works for the bad-level U_r operators.
These are eigenrelations for a possibly zero or nonprimitive R-module
element, not a claimed faithful Hecke character to R.

The CM reduction retains its conductor. Away from v, if an element with
a denominator at t became an endomorphism after reduction, a multiple
of it would kill t-power torsion there. Prime-to-v étale specialization
would give the same torsion vanishing before reduction. The quotient
property of multiplication by t^a then divides the original endomorphism
already in characteristic zero. This prevents an enlarged intersection
with K at t. At v the CM order is maximal. Thus the embedding remains
optimal with the asserted conductor and orientation; it is not replaced
by a smaller-conductor toric point.

The supersingular divisor records every ring-class element, including
repeated reductions and the integers ij from the two derivative operators.
It is not the unweighted set of distinct supersingular images. This is
why no automorphism-order division enters its evaluation. A conversion
using the quaternionic monodromy pairing would have different weights,
which the proof explicitly retains as a separate operation.

## 4. Exact reciprocity at p^k and the degree-zero operator

The ideal (v) is principal in the relevant ring class group because v
is rational and prime to its conductor. The chosen completion of H_m
is therefore K_lambda itself. Localization of the descended global class
is the Kummer class of the actual P_m there. The good-reduction formal
group is p-divisible, so reduction gives precisely the finite-field
Kummer map. The plus projection loses nothing on this even-index class.
Additivity now proves (18) with every coefficient and trace representative
unchanged. It does not use a residual theorem to assert a p^k identity.

The auxiliary t in (19) can be chosen from a scalar-2 Frobenius modulo
p, giving a_t−(t+1)=−1 modulo p. Its denominator is a genuine unit.
The numerator T_t−(t+1) kills degree, and the eigenrelation makes its
evaluation unchanged. Thus it maps the actual divisor to degree zero
without an omitted factor. No idempotence is claimed.

The coefficient-at-identity formula (23) checks by direct multiplication
of the two group-ring sums. It is not augmentation. The normalized
system's scalar −1 and the next transverse sign are both kept; they
agree with the preceding full-coefficient normalization proof.

## 5. The source comparison and what analytic vanishing supplies

Root read [Bertolini–Darmon, *Euler systems and Jochnowitz congruences*, Theorem 6.1](https://www.math.mcgill.ca/darmon/pub/Articles/Research/21.Jochnowitz/paper.pdf),
including its setup requiring the strong Weil curve, minimal
parametrization, absolute residual irreducibility and p not dividing
2N degree(π). Its displayed isomorphism carries the conductor-one point
to u degree(π) times the algebraic toric special value modulo the residual
maximal ideal. The proof correctly does not identify that isomorphism
with its chosen λ_v basis, remove the degree factor, or extend this
characteristic-zero-newform statement to arbitrary p^k and derived
conductor without proof.

The actual bottom augmentation vanishes because Gross–Zagier makes
P_K torsion and no p-primary torsion is present. The conductor-fiber
identity (25) is reduction of the exact trace identity and is now
explicitly restricted to a fresh inert prime outside cNpvD. A split
prime would have a different relation. The parity statement is likewise
restricted to squarefree products of Heegner Kolyvagin primes. The plus
projection kills the odd-index finite evaluations by their known
conjugation eigenvalue; it does not kill the even-index ones.

These trace and symmetry identities do not evaluate the weighted
coefficient in (23). The analytic third and fourth derivative vanishings
have not been compared with that coefficient. LR-TP5 remains the exact
vanishing of the constructed derived toric sum at all detecting fresh
primes. Neither the local maps nor their geometric realization prove a
new rank-five bound, primary finiteness, or universal BSD.
