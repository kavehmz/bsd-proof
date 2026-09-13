# K-theory lattice checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal active.

Read `k-theory-lattice-attack.md` and `review-k-theory-lattice.md`, verdict PASS.
No change to the old numerical certificates was made. The only new
calculation is the exact elementary point count 5,6,9 at q=2,3,5,
with its reproduction command embedded in the proof.

## Completed proof attempt

- Frobenius minus identity is invertible on T_ℓE for q=2 if ℓ≠2,5,
  q=3 if ℓ=5, and q=5 if ℓ=2. This kills all continuous G_Q coinvariants.
- Proper homotopy exactness and the integral zero section, together with
  π₁(Spec Z)=1, then prove the full π₁ of the actual arithmetic model zero.
- Schmidt/Kato–Saito unramified class field theory gives CH₀(model)=0.
- The ordinary K₀ ring is Z⊕Pic=Z⁴, with square-zero augmentation ideal.
  Concrete basis: 1, [O(O)]−1, [O(P−O)]−1, [O(Q−O)]−1.
- The actual first Chern map fits an exact sequence with kernel Z/n
  and cokernel Sha(389a1)[n]. Ordinary K₀ finite generation does not
  bound that cokernel. Uniform lifting up to a fixed scalar is K0-389.

Sources actually read: Stacks0BUM Proposition58.15.2 (flat/proper/reduced
connected fibers); Milne LEC §3 comparison (v2.21); Milne ANT(v3.08)
Theorem4.9 (no nontrivial unramified Q extension); Schmidt math/0204330v1
introduction/Theorem2 and empty-boundary remark after Definition3.1;
Weibel KbookII.8.1–8.2/Example8.2.2, rank/determinant and point-generated
kernel. Exact URLs and assumptions are in the proof.

## Next action

The independent review checked the full π₁ and K₀ arguments, including
the profinite coinvariants, nodal-fiber homotopy, and arithmetic CH₀-to-SK₀
map. Its direct normalization-of-curves proof was added to the main note.
Next test an actual étale K-theory/Bott
comparison for the uniformly bounded scalar lifting, retaining its
cohomological degree and Tate twists. This last comparison is not done.

The twisted-sheaf agent was informed of the ordinary ring calculation,
with the explicit instruction not to erase the twisted-rank obstruction.
The modular relative-cycle agent was informed that point-line products
are ordinary zero classes but not canonical arithmetic nullhomotopies.
