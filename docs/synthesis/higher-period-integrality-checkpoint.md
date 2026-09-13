# Higher-period integrality restart checkpoint

Date: 2026-09-12. Owner: `/root/higher_period_integrality`.
Assigned model: GPT-6 Astra, xhigh reasoning.

## Scope and state

The parent objective is full BSD over Q. This bounded task tests whether an
explicit archimedean higher-period construction gives rationality or integrality
of the BSD quotient. Nothing in this checkpoint proves either statement.

Read AGENTS.md, research-state.md, research-ledger.md, final-report.md and the
charter. Read the motivic fundamental-line/rationality discussion in
`../approaches/G-motivic-bloch-kato.md` and the Mellin/character and integral
determinant sections of `derived-comparison-attack.md`. The agent's `get_goal`
returned null; this is the documented subagent scope and does not cancel the
coordinator's active goal. Live inventory confirmed parent plus this agent and
the family-specialization and modular-visibility agents.

Owned files only:

- `higher-period-integrality-attack.md` (written, ready for independent review).
- `higher-period-integrality-checkpoint.md` (this file).
- `review-coherent-moment.md` (additional review assigned by parent after this task).

## Concrete candidate and next actions

Test the exact Mellin moment as a Chen iterated integral of `f(z) dz` and `dz/z`.
The candidate succeeds analytically on the upper half-plane; determine exactly
why that expression does or does not descend to the algebraic modular curve's
unipotent fundamental group. Verify primary sources for higher modular symbols,
harmonic Maass forms, and regulator constructions. Do not substitute the
conjectural BSD zeta element for a construction. Do not duplicate the p-adic
family-specialization or modular-Jacobian visibility tasks.

## Results saved and active next action

The attack note now contains complete proofs of:

1. The exact anchored Chen identity for the leading Mellin moment, with
   signs, factorials, and cusp convergence.
2. Infinite translation orbit of dz/z and positive logarithmic Mellin jets;
   this only excludes the literal finite-rank horizontal realization.
3. Vanishing of ordinary higher group cohomology of subgroups of SL2(Z)
   over characteristic zero, via the coset tree's projective resolution.
   This distinguishes genuine higher cocycle representatives from a nonzero
   rational cohomology period line.
4. The second eta-deformation jet has a surviving Petersson-log-square
   correction. Its precise formula is (5.4), not an unqualified identification
   of the eta jet with L''.
5. An explicit real period–height determinant line and the exact missing
   rational/integral lattice comparison.

Primary sources checked include Manin math/0502576v1; Brown 1407.5167v4;
Diamantis–Rolen 1704.02667v1 and published DOI 10.1007/s40687-018-0126-4;
Bruggeman–Choie–Diamantis 1404.6718 corrected author PDF §9.4; original
Goldfeld 1995 author PDF §4; Schappacher–Scholl's original chapter;
Bruinier–Ono 0710.0283v2/published Annals; Du–Peng 2603.15795v1 (scope only).
Exact URLs, sections, and limitations are in the attack note.

No rationality or integrality of n_E is proved. All new elementary deductions
need the coordinator's independent review before use in synthesis. Parent
assigned an independent review of `coherent-moment-attack.md` Propositions
2.1/3.1 and Lemmas 4.1/4.2. Completed review: PASS, with exact independent
modular-exponent checks at 1093 and 3511 and all five stored records.
`review-coherent-moment.md` records artifact hashes and full reasoning.
Only the three owned Markdown files were edited. Preserve the substantial existing
uncommitted research; no old BSD certificate was rerun.
