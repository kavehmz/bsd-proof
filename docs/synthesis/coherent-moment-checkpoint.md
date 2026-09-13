# Checkpoint: a coherent moment construction across primes

Date: 2026-09-12. Owner: root. The full note [coherent-moment-attack.md](coherent-moment-attack.md) is complete and its elementary propositions passed independent review. It does not establish BSD.

## Source lead read

Banwait, [arXiv:2609.08431v1](https://arxiv.org/html/2609.08431v1), submitted
8 September 2026: Theorem B and the stated proof route in §§2.5, 6.1–6.3,
13–16. The source's rank-two CM second-jet criterion includes both a unit
normalized regulator and vanishing of the primary Sha group, under an explicit
excluded-prime set. Its fixed algebraic theta/elliptic-unit object does not
itself prove the required uniform leading coefficient. No numerical examples
from that paper have been rerun here.

## Candidate being tested

Use one integral group-ring element `[2]+[2]^{-1}-2`, independent of p.
At each odd p, send `[2]` to `(1+T)^{m_p}` with
`m_p=log_p(2)/log_p(1+p)` in Z_p. This gives

    F_p(T)=(1+T)^{m_p}+(1+T)^{-m_p}-2.

Prove the exact second coefficient is m_p², central order is two,
the inversion sign is positive, and the whole series is primitive even
at Wieferich primes where the second coefficient is nonunit. The prospective
formula is lambda(F_p)=2 p^{v_p(m_p)}. Check p=1093 by exact modular arithmetic,
not an approximate logarithm.

The intended lesson is specifically about separating the regulator-like
factor m_p² from a normalized leading coefficient. This is a single coherent
integral measure example, stronger than an arbitrary p-dependent power-series
countermodel, but it is NOT an elliptic-curve L-function or a BSD counterexample.
Do not claim that the exceptional primes in the example form an infinite set.

## Completed verification and next action

The full proof is saved in `coherent-moment-attack.md`, with PASS in
`review-coherent-moment.md`. `compute/scripts/coherent_measure_check.py` and
`compute/data/coherent_measure_example.json` record exact integer checks.
The reviewer independently checked both exceptional primes by modular
exponentiation. No infinite-exception or BSD counterexample claim is made.

Next: construct an actual arithmetic leading tensor and regulator tensor,
with their integral realization maps, rather than a formal module named
after the desired periods. The primitive-tensor lemma only gives integrality
once that identification and proportionality are proved. The read CM
moment criterion does not establish them. See research-state §5 for the
coordinated next research tasks.
