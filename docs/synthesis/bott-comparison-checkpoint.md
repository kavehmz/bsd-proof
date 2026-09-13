# Bott comparison restart checkpoint

Date: 2026-09-12. Owner: coordinator. Full BSD goal remains active.
Read [the proof](bott-comparison-attack.md) and its
[independent PASS review](review-bott-comparison.md). All seven sections
were reviewed, including actual Quillen K-theory, coefficient Bocksteins,
and exact prime ranges. No numerical certificate was rerun.

## Completed construction

For odd p, r≥1, m=p^r, w=φ(m), the basis ζ_m^⊗w is G_Q-invariant and
independent of the chosen primitive root. Voevodsky 0805.4430v2,
Theorem 6.17(1), uniquely lifts it to b_pr in H_M⁰(Q,Z/m(w)). Multiplying
by b_pr and using the motivic–étale comparison gives an actual high-weight
realization B_pr=H_M²(E,Z/m(w+1)). Its exact quotient by b_pr Pic(E)/m is
Br(E)[m]. After the zero-section/geometric-degree normalizations and all
local Selmer conditions, its quotient by b_pr(E(Q)/m) is exactly Sha(E)[m].
This supplies finite-level motivic classes, but no division into weight one.

For p≥5 there is an actual pure-Adams Quillen Bott class in
K_(2w)(Q;Z/m), with edge b_pr. The finite-coefficient motivic spectral
sequence has cohomological degrees 0..2 over Q and 0..4 over E; Adams ψ²
kills d₂ and degree kills higher differentials. On K_(2w)(E;Z/m), the
three eigenvalues are 1,2,4. The integral polynomial projector
−(ψ²−1)(ψ²−4)/2 selects B_pr. Its projected Bott product on K₀ is the
motivic product just described. The raw product is injective with cokernel
Br(E)[m] ⊕ Br(Q)[m]. The extra constant Brauer term cannot be ignored.

## Arithmetic tests already completed

- Over Q(ζ_p), a weight-two root product transforms by the cyclotomic
  character; ordinary transfer kills it. Weight p−1 repairs descent.
- The minimum positive weight of a primitive rational Tate basis modulo
  p^r is φ(p^r). Thus no fixed positive weight works for every prime or
  unbounded r. At this weight the basis has no primitive lift modulo
  p^(r+1), since v_p((1+p)^w−1)=r.
- For fixed w>0, H⁰(Q,Z_p(w))=0. All reductions of an integral motivic
  degree-zero class vanish, so the coefficient Bockstein of b_pr has
  exact order m. The Quillen Bott Bockstein also has exact order m for
  p≥5, by the field edge/e-invariant argument. Its same-degree primitive
  lift at the next coefficient level does not exist.
- Quillen's finite-field calculation gives K_i(F_p;Z/p^r)=0 for i>0,
  while K₀=Z/p^r. A positive-degree Bott class extending across the
  arithmetic base restricts to zero; inverting it kills the p-fiber.
  A selective integral Selmer comparison has not been ruled out.

Primary sources were read directly: Voevodsky Theorem 6.17(1);
Weibel K-book VI §§4.2–4.3,4.9 and IV Corollary 1.13; Milne's
cyclotomic image theorem. Geisser's unconditional Proposition 4.5 applies
only to function fields. Its number-field counterpart assumes Lichtenbaum.

## Exact next target

GAP Bott-389 asks for a single nonzero integer a, independent of p and r,
annihilating the normalized quotient above. That quotient is Sha[p^r].
The high-weight lift, changing Tate weights, actual Adams splitting, and
coefficient Bockstein have all been constructed; repeating their existence
does not supply a. Root is integrating this round and then choosing the
next arithmetic comparison. See research-state §5 for live agent tasks.
