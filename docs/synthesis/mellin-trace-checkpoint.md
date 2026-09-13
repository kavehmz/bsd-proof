# Mellin trace and Green comparison restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
The second-character note has passed root review in
`review-spectral-second-variation.md`; its author has been notified.

Completed root construction, independently reviewed PASS in
`review-mellin-trace.md`: push the actual Mellin forcing current
from X₀(389) to E before identifying any Green pairing with point heights.
Let v=389^(-6)Δ(z)/Δ(389z), l=log|v|, and
α=π*ω=c_π·2πif(z)dz, retaining the nonzero rational differential factor.
The reviewed norm identity Norm_π(v)=±1 gives trace(l)=0. For the
reviewed F=y² f conjugate(g), dlog(v)=2πig dz yields
F dμ=−i/(4π²c_π) d(lα). Thus its pushed current is zero.

Reviewed exact consequences: F pairs to
zero with every pulled scalar function (including the bounded-at-cusps
degree-zero point Green potentials). The reduced Green solution of F
has constant fiber trace, so its point-source pairings also vanish.
This is stronger than saying the sources differ, and is only a test of
the specified direct comparison.

Keep the spectral decoration A₂: π_*(A₂ Fdμ) has nonzero total mass
−9·389/(π⁴·390) ell_E L(f,2). A product-rule transgression exhibits the
extra term missed by replacing a weighted trace with the ordinary norm.
It is an actual analytic current, not a proved rational arithmetic class.
Cusp integrability, absence of hidden boundary atoms, current degrees,
ramification and the spectral coefficient have all passed independent
review. No old certificate was rerun.

Next mathematical target is GAP MT-389 in the full proof: construct a
rational arithmetic realization of the decorated current and a map to
the point determinant tensor the L(f,2) regulator line. The ordinary
norm/undecorated trace gives zero; the extra decorated derivative term
must remain. Subtracting its analytic mass to solve a Poisson equation
does not prove rationality. Root is reviewing the parallel torsion-
connection and motivic-derivative constructions next; see state §5.
