# Read-only continuity audit of the construction round

Date: 2026-09-12. Final inspection at approximately 09:24 UTC.
Auditor: `/root/uniform_witness`, GPT-6 Astra/xhigh.
Owned output: this file only. No shared note was rewritten and no
mathematical script or numerical certificate was rerun.

**Verdict: PASS for fresh-context recoverability.** The universal objective,
mandatory model/effort, mathematical status, accepted CM normalization,
new analytic certificate, and precise remaining construction tasks are
all recoverable from saved files without the transcript. Several stale
editorial status entries were found at the first inspection and sent to
the coordinator. The coordinator is repairing those entries and refreshing
the manifest; the findings below name the original sections so they remain
understandable after those repairs.

This is an operational handoff audit, not another mathematical review of
the CM formula or another run of its analytic proof.

## 1. Files and live state inspected

Read `AGENTS.md`, then
[research-state.md](research-state.md),
[research-ledger.md](research-ledger.md), and
[final-report.md](final-report.md). Also inspected this round's CM,
Hecke–Brauer, Green, and Weil–étale checkpoints, the CM construction and
source-check files, their review headers and concluding scope statements,
the new CM JSON, its reproducer's source, and the manifest.

The live-agent inventory contained root and the three existing research
handles; `/root/odd_rank_bridge` was completed, while root,
`/root/higher_period_integrality`, and this audit agent were running.
No second continuity audit was running, so no duplicate was created.
Saved agent rows are expressly labeled snapshots and require revalidation.

`get_goal` returned null in this child scope, as documented in AGENTS and
the main state. This does not alter or negate the coordinator's active
universal goal. The auditor neither created nor completed a goal.

`git status --short` showed the expected extensive uncommitted research.
No reset, clean, rollback, or unrelated write occurred.

## 2. A fresh context can recover the objective and restrictions

`AGENTS.md` and research-state §1 explicitly preserve all of the following:

- Success means a proof or disproof of full BSD for every elliptic curve
  over $\mathbb Q$, including rank, Sha finiteness, and the exact leading term.
- A test-curve proof, reduction, numerical agreement, or formal countermodel
  is not completion of that objective.
- No universal proof or counterexample has been obtained.
- Sustained research and subagents are authorized without a user-specified
  token budget.
- Every research subagent must use `gpt-6-astra` and `xhigh`; capacity errors
  do not authorize switching models.
- Read the durable state and actual owned checkpoint before resuming or
  replacing an agent. A timed-out observation alone does not justify
  duplicating a process.

These requirements are also preserved in the manifest's objective and
model fields. No transcript is required to reconstruct them.

## 3. Proof/review/checkpoint routes all exist

| Construction | Proof and accepted review | Restart location |
|---|---|---|
| Hecke–Brauer arithmetic component | [Proof](hecke-brauer-annihilator-attack.md), [PASS review](review-hecke-brauer.md) | [Checkpoint](hecke-brauer-checkpoint.md), HB-cycle in proof §9 |
| Explicit arithmetic surface and Weil–étale test | [Proof](weil-etale-lattice-attack.md), [PASS review](review-weil-etale-lattice.md) | [Checkpoint](weil-etale-checkpoint.md), WE-389 |
| Arithmetic eta Hodge/Green class | [Proof](arithmetic-green-comparison.md), [PASS review](review-arithmetic-green.md) | [Checkpoint](arithmetic-green-checkpoint.md), AG-389 in proof §8 |
| CM theta and full regulator tensor | [Proof](cm-regulator-tensor-attack.md), [PASS review](review-cm-regulator-tensor.md) | [Checkpoint](cm-regulator-checkpoint.md), CM-Theta in proof §7 |
| Independent restricted CM moment reconstruction | [Source check](cm-moment-source-check.md) | Its §§1–4, 6–8; cross-check against CM proof §6.1 |

The relevant Markdown link targets were checked for existence. After
discarding two mathematical expressions that a simple link parser had
mistaken for links, all 90 actual local Markdown targets in the inspected
set existed. No required proof, review, checkpoint, script, or data path
was missing. The missing CM cross-link described below was an absent
reference to an existing file, not a missing artifact.

The reports distinguish the completed constructions from their limits:
the Hodge class has zero elliptic point projection; no Hecke annihilator
was constructed; finite generation of the adjacent arithmetic cohomology
was not obtained; and the common CM theta function does not yet give the
moment-to-regulator equality.

## 4. The CM pole and central-twist issue is resolved for the used formula

The accepted reconstruction is findable through all three main handoff
notes and is explicit in the following places:

- CM proof §6.1: direct derivation from BK's unit projectors,
  homogeneity, and partial Katz definitions.
- CM review §5: PASS after the rationality repair and completed source audit.
- Independent source check §§2–4: ray-class multiplicity, CRT torsion
  representative, shifted Euler factors, and central $q$-cancellation.
- Independent source check §§6–8: version-specific printed displays
  that are not inputs to the proof, a nonzero moment check, and the accepted
  restricted scope.

A fresh reader can recover these distinctions without guessing:

1. The formal/logarithmic pole-subtraction difference depends on one
   variable. The other unit projector kills it before restricted moments
   are taken. The unrestricted zero-parameter display remains outside
   the approved scope.
2. The partial ideal-class factors cancel under the central character
   twist using BK Definitions 3.8–3.9. The remaining extra factor is
   the stated $p$-adic period.
3. Sum once per ray class, not once per residue unit; otherwise the
   $\mathbb Q(i)$ calculation is repeated four times.
4. The inverse-prime action uses the integral CRT representative
   $\beta$, preserving the original torsion arguments. The inverse
   lattice contributes the shifted Euler exponents.
5. The period powers, factorials, and signs follow from the reconstructed
   measure, not from the compressed displays explicitly excluded in
   the source review.

The last inspection of the independent source check's §8 explicitly
records that the coordinator read all eight sections and checked its
two nonzero moments before accepting it. Thus the **restricted**
normalization review is now resolved, not the next mathematical task.
Neither this approval nor the formal polynomial congruence approves the
unrestricted pole-removal display or proves CM-Theta.

## 5. New CM analytic certificate and exact reproducer are locatable

The new files exist:

- [cm39_analytic_rank_certificate.json](../../compute/data/cm39_analytic_rank_certificate.json).
- [certify_cm39.py](../../compute/scripts/certify_cm39.py).

The JSON identifies the equation by coefficients `[0,0,0,39,0]`, conductor
48672, root number $+1$, and certified algebraic and analytic ranks two.
It records 112-bit precision, cutoff 48, Fourier cutoff 1686, exact rational
endpoints, both infinite-tail bounds, and the separate coefficient check
through 1405. Its scope explicitly excludes full Sha finiteness and the
BSD leading-term formula.

The reproducer's docstring gives the complete workspace-local command.
Reading the source confirms that it calls the already reviewed Mellin
algorithm on the explicit equation, rather than requiring the unavailable
small-database label. The saved dependency SHA-256 in the JSON matches
the current `certify_mellin.py` bytes. This was a file-hash consistency
check only; the auditor did not execute either mathematical script.

CM proof §8 and the CM review §4 document the first and second enclosures
and explain why the second is a separate check. The main report links the
new data, and the state names both the data and the exact next gap.

## 6. Exact pending work is preserved

The next tasks in research-state §5 agree with their full statements:

- **CM-Theta:** first prove that the real BSD quotient for
  $y^2=x^3+39x$ is rational; then use its canonical image in $\mathbb Q_p$
  in equation (16). Construct the arithmetic equality between the torsion
  second moment and $4e_p n_E$ times the actual non-torsion height
  determinant. A chosen embedding of an arbitrary real number into
  $\mathbb C_p$ is explicitly rejected as a substitute.
- **HB-cycle:** construct global degree-zero rational line bundles whose
  Chern classes are $\Theta z$ for the finite Selmer classes, uniformly
  in $n$. The local lifts already present in the Selmer definition do
  not solve that task. A fixed nonzero scalar version is also a stated
  sufficient target.
- **AG-389:** construct a secondary cycle or extension retaining the
  relative cusp path and noncuspidal point data with the exact corrected
  real regulator. The already constructed eta Hodge class does not
  supply those point directions.
- **WE-389:** the Weil–étale checkpoint retains the missing degree-three
  finite-generation/perfect-integral-comparison requirement and explicitly
  identifies its strength as full Sha finiteness for the test surface.

The older PrimeIndex-389, Leading-389, and O5 targets remain visible in
the state and final report. These tasks do not replace the universal
objective, and no new research delegation is implied solely by listing them.

## 7. Editorial findings from the initial snapshot

These are status/link repairs, not mathematical objections. They were
reported to the coordinator before this audit was finalized.

1. **CM checkpoint, “Exact next action”:** it still said to add the
   independent source-check cross-link “when that audit file arrives.”
   The source-check file already existed. The main CM proof initially
   contained no `cm-moment-source-check.md` cross-link. Replace the
   obsolete wait with the actual cross-link and the arithmetic next task.
2. **Research-state §5 agent table:** the row describing the author as
   “Writing `cm-moment-source-check.md`” and the CM row's pending final
   cross-link were transitional. Reconcile these rows with the saved
   files after all editorial work finishes; the state correctly warns
   that live handles must still be rechecked.
3. **Green checkpoint, initial “Owned files” and early “Next actions”:**
   the first line still described the completed note as awaiting
   independent review, while its final handoff already recorded PASS
   and the applied clarifications. Mark the early material as historical
   or put the final status first.
4. **Hecke–Brauer checkpoint, “Completed bounded attack and review
   targets”, and visibility checkpoint, “Proof attempt completed for
   coordinator review”:** their review-target language lagged the existing
   PASS review files. Their full mathematical residual targets were
   nevertheless already correct and present.
5. **Independent CM source check, initial §1:** the first read said its
   deductions awaited coordinator review. During this audit, its final
   §8 was updated to record completed coordinator acceptance. The header
   and handoff should agree about that accepted restricted scope.
6. **Manifest, `verification.latest_research_checks`:** initially still
   said the exact CM moment source review was pending. The initial
   manifest also omitted the newly written source-check file and had
   eight changed hash entries: Green proof/checkpoint, CM proof/checkpoint,
   CM review, research-state, research-ledger, and final-report. None of
   its recorded files was absent. These are expected current edits;
   refresh the manifest after all final status/link changes and this
   audit are saved. Do not roll files back to old hashes.
7. **State §6 and final-report §4 reproduction blocks:** these retain
   the original four-script suite. The new CM and arithmetic-surface
   reproducers are correctly linked elsewhere, so they are recoverable,
   but label the old block as the original suite or include links to
   the new certificate commands to avoid reading it as an exhaustive list.

The coordinator acknowledged the findings and was repairing stale wording
and refreshing the manifest. This file preserves the inspection findings;
it does not claim to have validated a manifest written after its own save.

No missing mathematical artifact or unstated user decision prevents a fresh
context from resuming the explicit construction targets.

## 8. Coordinator resolution after the audit

The coordinator repaired the findings in §7: source-check links and review
headers agree; historical checkpoint plans are labeled historical; the agent
table records completed assignments as a snapshot; and the reproduction
blocks explicitly distinguish the original suite from the new scripts.
Local artifact links, dependency hashes, and the CM interval nesting were
checked without rerunning mathematical certificates. The manifest is refreshed
after this resolution note, including the source check and this audit.
The parent's goal tool was re-read and remains active. This postscript records
the coordinator's checks, not an additional claim by the original auditor.
