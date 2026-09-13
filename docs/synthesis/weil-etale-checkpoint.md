# Weil–étale arithmetic-surface checkpoint

Date: 2026-09-12. Owner: coordinator. Universal BSD goal remains active.

Read [the complete proof](weil-etale-lattice-attack.md) and its
[independent Astra/xhigh review](review-weil-etale-lattice.md), verdict PASS.
The explicit flatness proof from the review was copied into the proof after
review; the other post-review edit is its status/link header.

## Completed inputs

- Actual regular proper flat plane cubic over Z for 389a1. Unique split
  nodal fiber at 389; node (299,194), regularity residue 5, slopes 148,241.
- Pic(model)=Pic(E)=Z⊕E(Q)=Z³, and global units ±1.
- Br(model)=Sha(E/Q) as full groups: finite-place model comparison plus
  evaluation at O and Q=(0,-1) removes the real-place term, including at 2.
- Integral étale Z(1) groups through degree three are ±1, Z³, Sha.
  Thus Flach–Morin finite generation in the required range is exactly
  full Sha finiteness here. Their conditional perfectness/middle-group
  result does not prove this premise.
- Arithmetic surface zeta is ζ(s)ζ(s−1)/L(E,s), pole order 3 at 1,
  leading coefficient −1/(2 ell_E), with exact interval propagation.
- Compact Selmer inverse limits retain T_p Sha, losing finite primary
  groups; zero Tate modules at every prime do not bound prime support.

The new exact script is `compute/scripts/arithmetic_surface_check.py`,
output `compute/data/arithmetic_surface_389a1.json`. It ran successfully;
the reviewer separately checked the dependency hash and reciprocal
endpoints without rerunning the existing analytic certificate.

## Exact next target

WE-389 is finite generation of H³_et(model,Z(1)), or an actual perfect
integral comparison retaining this entire torsion group. This remains
equivalent to full Sha finiteness, not a weaker solved problem.
The known Picard lattice does not imply its adjacent cohomology is finite.
After finiteness, the exact period/height leading comparison is still needed.

Read the coordinated [Hecke–Brauer note](hecke-brauer-annihilator-attack.md)
before attempting correspondences: finite geometric cohomology, all
closed-point evaluations, reduction to good fibers, and inner Frobenius
conjugation have already been tested. Its HB-cycle is the global rational
line-bundle lift that must actually be constructed, uniformly in n.

Source locations are preserved in the proof/review. No full BSD proof or
counterexample follows from the completed calculations.
