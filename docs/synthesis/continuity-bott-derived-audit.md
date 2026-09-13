# Continuity audit after the Bott and derived-unit round

Date: 2026-09-12. Auditor `/root/odd_rank_bridge`, GPT-6 Astra/xhigh.
Own only this audit. This was a read-only continuity check apart from
writing this file; no mathematical script or earlier certificate was rerun.

**PASS for recovery of the objective, completed mathematics, source
conventions and exact remaining comparisons.** The saved files suffice
to resume without reconstructing conversation history. Two operational
status updates identified below should be reflected in the coordinator's
final snapshot; one was already repaired during this audit. This is a
continuity finding, not a new independent proof review.

## 1. Recovery inputs and actual tool state

I read [AGENTS.md](../../AGENTS.md), then
[research-state.md](research-state.md), [ledger §12](research-ledger.md#12-bott-derived-units-spectral-jets-and-projective-connections),
and the additions and remaining-task sections of
[final-report.md](final-report.md). I also read the current proof, review
and checkpoint headers for all four completed constructions, their
checkpoint conclusions, CM §8, and the two newly assigned checkpoints.

`git status --short` confirmed the substantial modified/untracked research
worktree described in the handoff. I did not modify its existing files.
`collaboration.list_agents` reported root and all three named research
agents running at this observation. Those statuses are snapshots, not
durable promises. The subagent's `get_goal` returned null, consistent with
the explicitly documented parent-goal scope; it was not treated as
cancellation. Root must continue to use its own goal tool as authority.

The [manifest](checkpoint-manifest.json) was being refreshed concurrently
by root and was treated as the previous snapshot, as instructed. This
audit makes no finding of corruption from differences against that old
snapshot. Root separately owns link and dependency-hash validation.

## 2. Objective and completion boundaries survive

AGENTS, state §§1–2, and the report consistently preserve full BSD for
**every elliptic curve over Q**, including rank equality, full Sha
finiteness and the exact leading coefficient. Neither a test-curve
result nor a countermodel to a shortcut completes that objective.
The report explicitly says that no full proof or disproof has been obtained.

The persistent research-agent requirement is explicit in AGENTS and
state §1: `gpt-6-astra` with `xhigh`, without an inferred token budget.
The current agent list itself does not display model metadata; the saved
instruction, rather than a claim about unavailable metadata, is the
restart authority. AGENTS also preserves the requirement to check live
handles and prohibits duplicate restarts or destructive worktree cleanup.

## 3. The four completed constructions are consistently reviewed

| Construction | Recoverable status and scope |
| --- | --- |
| [Bott](bott-comparison-attack.md), [checkpoint](bott-comparison-checkpoint.md), [review](review-bott-comparison.md) | PASS includes the actual Quillen summand. Motivic results apply at the stated odd primes; later Quillen nonlifting and Bockstein statements retain p≥5. The Selmer quotient remains Sha[p^r], with no uniform annihilator. |
| [CM derived units](cm-derived-unit-attack.md), [checkpoint](cm-derived-unit-checkpoint.md), [review](review-cm-derived-unit.md) | PASS includes finite units, exact Kato normalization, integral T-divisibility, full-Selmer height identity, and the Frobenius audit. Reg_p≠0 is required only for the current inverse/projection construction; additional Selmer directions are not proved absent. |
| [Mellin variation](mellin-variation-attack.md), [checkpoint](mellin-variation-checkpoint.md), [review](review-mellin-variation.md) | PASS applies to the completed spectral construction and specified failed repairs. Both cusps, the factor L(f,2), and the diagonal scope of first-response vanishing are retained. The second character variation is a separate unreviewed task. |
| [Projective monodromy](projective-monodromy-attack.md), [checkpoint](projective-monodromy-checkpoint.md), [review](review-projective-monodromy.md) | PASS applies to generic covers, integral local degree-zero connections, and the finite-order obstruction. No uniform degree bound, global Kummer adjustment, or ramified finite-flat descent is inferred. |

The reviews that record a prior proof hash expressly distinguish subsequent
editorial review-link/checkpoint changes. Their headers do not silently
extend PASS to the new follow-up proofs. Historical initial-plan paragraphs
inside checkpoints are followed by explicit completed-status sections.

## 4. Frobenius is resolved and must not be reopened from a root label

State §5, ledger §12, CM §7, its checkpoint and its PASS review agree:
for good split p on y²=x³+39x, with α the ordinary unit root and β=p/α,

| Line | Absolute cohomological F | Tate-twisted φ=F/p |
| --- | --- | --- |
| Q_p ω | β | α⁻¹ |
| Q_p xω | α | β⁻¹ |

Consequently BKS's ν, with φν=β⁻¹ν and [ω,ν]=1, is in the actual
F-unit-root complement to ω. The primary-source dictionary is recorded
against MST §3.2, SW §3.5 and BKS Lemma 6.9. The inconsistent printed
reciprocal-root label in SW §4.1 is explicitly excluded from the argument.
The earlier E₂=0 proof remains valid through MST's prescription, and no
δ₀, k_α, height or p/(2#E(F_p)) coefficient changed. The Kato plus-branch
and conjugate-CM-type clarifications are also recorded as reviewed.

## 5. Exact next comparisons remain recoverable

**CM-Derived / CM-Biex.** CM §8 states the actual rational target:
construct one Z_theta in the rational framed line whose localizations
are the constructed Z_p at every prime where the inverse is defined,
with the compatible undivided identity elsewhere in the stated good
split scope, and whose real realization is ell_E/(2Ω_E).
Writing Z_theta=q Xi must prove q=n_E is rational; that rationality is
not assumed. The finite-level rational augmentation route was tested
and kills positive graded pieces. The note does not claim Sha finiteness,
Selmer corank two, or nondegeneracy at every prime.

**MV-389 / RM-389.** The remaining comparison must identify the spectral
construction with the actual noncuspidal determinant and justify the
L(f,2) regulator division. The new [second-variation checkpoint](spectral-second-variation-checkpoint.md)
records a saved [proof draft](spectral-second-variation-attack.md), exact
new source and normalization data, and the next action: independent
review before relying on those new formulas. Its header explicitly
requires that review. The earlier diagonal first-response vanishing
does not already settle this task.

**PM-389 / Bott-389 / TS-389.** The missing global result is a uniform
splitting degree, global Kummer adjustment, or fixed nonzero annihilator
independent of period. The new [torsion-connection checkpoint](projective-torsion-connection-checkpoint.md)
records the proposed Cartier-dual differential comparison and keeps
the full finite-flat descent, including infinitesimals. It does not
claim the proposed comparison has already been proved.

State §5 also preserves the universal higher-rank task and O5. The
389a1 interval may force one from half-integrality, but no analytic
element in that half-period line is asserted.

## 6. Precise status observations and repairs

1. The first read of `final-report.md:3` still named the earlier
   relative-motive/twisted-bundle round. Root repaired it during the
   audit to the current Bott/derived-unit/spectral/projective round;
   I reread and verified that replacement.
2. State §5's operational table initially described the torsion-connection
   task as merely sent and asked whether its agent had started. Its new
   checkpoint already exists and states the assigned construction. At
   this observation the corresponding attack file did not yet exist;
   this is an explicitly early checkpoint, not a missing completed
   artifact. Root should update the row to “started; checkpoint saved”
   or the newer actual status before freezing the snapshot.
3. State §5 initially listed this auditor as completed/available. The
   present read-only audit explains its observed running state; after
   this file is delivered, its completed status can link here. No new
   CM mathematical construction was started during this audit.

No remaining stale mathematical PASS status, reopened Frobenius ambiguity,
hidden rationality premise or missing completed proof/review/checkpoint
was found in the requested scope. Live follow-up files and the manifest
should be reread at resumption rather than inferred from this observation.
