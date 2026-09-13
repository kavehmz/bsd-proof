# Heegner defect duality restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
Read [the proof](heegner-defect-duality.md) and its
[independent PASS review](review-heegner-defect-duality.md).
All eight sections passed, after making the inverted-prime set S exact.
No old certificate was rerun.

## Completed actual arithmetic construction

The reviewed theta_m in C_m[p^k] is invariant under the full
Γ=Gal(H_m/Q), because the raw two-prime conjugation sign is plus.
The old nu_K≥2 theorem kills all one-prime classes at the FULL
coefficient. Finite-singular compatibility then gives zero localization
of the two-prime class at both old auxiliary primes. Its unique Q-descent
is κ_Q=(1/2)cor_(K/Q)κ_K in the strict finite Selmer group overQ.
The proof retains local torsion/Kummer components and assumes no Sha
finiteness. General invariant defect elements are not all asserted Selmer.

U=SpecZ[1/(Np|D|m)] and U_F is its finite étale ring-class cover.
The odd-p real Tate term vanishes; F is totally imaginary. The pairing
H¹(U_L,V) × H²_c(U_L,V)→(1/p^k)Z/Z uses compact-first Weil order
and the local-invariant trace. Canonical Tor, Kummer and Cartan–Leray
maps inject D_m=C_m[p^k]^Γ into actual H¹(U,V). Transposing by finite
Artin–Verdier duality gives a SURJECTION from actual compact H² to
Hom(D_m,(1/p^k)Z/Z), preserving the exact order of theta_m.

The cochain cone has D(a,b)=(da,res a−db); a degree2 compact class
(a,b_v) pairs with z by (a cup z,b_v cup loc z). A local boundary
class therefore gives the sum of the specified local invariants.
The full global degree2 cochain is not discarded. No higher-degree
K(pi,1) assertion is assumed: these models compute étale cohomology.

The strict finite Selmer dual is H²_c(U,V) modulo boundaries from
local Kummer groups away from ell,q and full local H¹ at ell,q.
All those boundary tests annihilate κ_Q, but the quotient still
perfectly detects it. This is not the Cassels–Tate pairing on Sha;
the point directions remain.

Corestriction induces H²_c(U_F,V)_Γ ≅ H²_c(U,V), as the dual of
restriction H¹(U,V)≅H¹(U_F,V)^Γ. Pairing two pulled-back classes
instead multiplies the value by[H_m:Q]=2h_K(ell+1)(q+1), divisible
by p^k, and gives zero. Coinvariants are not invariant averaging.
A detecting class upstairs need not be pulled back from the base.
This full-cohomology assertion is not a Selmer-control isomorphism
across the p-divisible-degree extension.

Primary checks: Demarche–Harari1804.03941v3 Theorem1.1, §2 and
cone conventions; Milne ADT II3.3, II3.9–3.10 for finite étale traces,
I3.2–I3.5 for local abelian/Kummer duality. Proof and review retain
compact-first coefficient ordering and the Q real-place convention.

## Exact next target

HD-TP5 asks that every constructed compact-duality evaluation of κ_Q
vanish under the analytic-rank-five hypotheses, or that a geometrically
constructed family generating the defect dual have zero values.
Perfect duality makes this equivalent to TP5/O5; it does not prove it.
The parallel local-reciprocity note supplies actual fresh-prime tests
in its additional full-image range. Its own proof/review/checkpoint
must be read for the finite cover, toric values and local signs.
Current whole-team assignments are in research-state §5.

## Subsequent explicit sign clarification

The Gysin review distinguished our declared signed boundary
partial(beta)=(0,+beta) from the canonical triangle connecting map
(0,-beta) for the fiber differential D(a,b)=(da,res(a)-db) and natural
PLUS projection. The trace in this proof is fixed positively on OUR
signed boundary and is correspondingly opposite to one normalized on
the canonical connecting map. All old formulas remain unchanged;
perfectness, annihilators, restriction/corestriction and vanishing
statements are unaffected. heegner-gysin-bridge.md uses the explicitly
SIGNED G_v=-g_v^std closed-point class. Never relabel its representative
(0,+beta) as the standard positive-divisor Gysin orientation.
