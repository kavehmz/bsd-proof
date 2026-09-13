# Cold-resume audit

Date: 2026-09-12. Reviewer: `/root/cold_resume_check`, starting without the
research conversation. Scope: continuity and artifact verification, not a new
mathematical review. No browsing, mathematical computation reruns, or further
agents were used. Only this audit file was edited by the reviewer.

**Verdict: PASS.** The saved notes provide enough information to resume the authorized
research without asking the user to reconstruct context. They do not establish
completion of BSD. The coordinator should issue the explicit resume instruction
to the paused family agent after this continuity check.

## 1. Objective, authority, and agent requirements

The objective is to prove or disprove **full BSD for every elliptic curve over
Q**. The [charter](../00-charter.md) specifies analytic/algebraic rank equality,
finiteness of Sha, and the exact leading-term formula

$$
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\operatorname{Reg}(E/\mathbb Q)
\prod_{p\mid N}c_p\,|\operatorname{Sha}(E/\mathbb Q)|}
{|E(\mathbb Q)_{\rm tors}|^2}.
$$

The [state](research-state.md), [ledger](research-ledger.md), and
[current report](final-report.md) consistently say this has neither been proved
nor disproved. A test-curve proof, formal countermodel, reduction, or numerical
match cannot complete the universal task. No finite token budget is specified.

Every research subagent must use `model="gpt-6-astra"` and
`reasoning_effort="xhigh"`; a capacity error does not authorize a model change.
The charter requires exact hypotheses, epistemic tags, and adversarial review
before relying on `[NEW]` claims. Preserve the uncommitted worktree.

The reviewer inspected `git status --short` and live agents. Its own `get_goal`
returned `null`; the coordinator independently rechecked the parent task and
reported its goal **active**, with no token limit, for task
`01a09445-0094-7400-a38c-2c594729b18d`. A subagent-local null must not be treated
as closure or absence of the parent goal, and no replacement goal was created.

## 2. Established results versus missing theorems

The notes record, with linked proofs/certificates and their review boundaries:

- Exact analytic and algebraic ranks 2 for 389a1 and 3 for 5077a1.
- For 389a1, the exact modular-symbol sum 244, hence Kurihara value 4 mod 5,
  and trivial Sha primary parts at 2, 3, 5, and 389.
- A full basis `(-1,1),(0,-1)` and the rigorous real quotient interval
  `0.9931 < n_389a1 < 1.0077`, with full real period and BSD regulator.
- Under the stated hypotheses, the odd-rank Selmer lower bound 3, the first
  unit-index formula `u_p = rank + dim_Fp Sha[p]`, and existence of some unit
  witness for 389a1 at every prime outside `{2,3,389}`.
- Reviewed determinant/cofactor and one-sided comparison deductions, selected
  torsor-degree equivalences, and countermodels to specific formal shortcuts.

These are recorded project results, not mathematical claims independently
re-proved in this audit. Review coverage must not be expanded from a summary:
the derived-comparison introduction limits completed review to Lemmas 2.1–2.2
and Propositions 4.2 and 6.1; the genus-one introduction lists Propositions 2.3,
3.1, 6.1 and Lemmas 5.1–5.2. Both explicitly leave other `[NEW]` claims pending.

Still unproved are `u_p=2` for every prime outside `{2,3,389}` and
`n_389a1=1`, including the proposed rationality/integrality or global comparison
inputs. Rationality alone does not force one from the interval. The universal
rank, Sha-finiteness, and leading-term targets remain, including CM and all
primes. The O5 two-prime Heegner-class vanishing target and a uniform torsor
degree bound remain open within the project. No family-specialization result
has yet been proved. Abstract module, power-series, and complex-function-field
counterexamples in the ledger are not counterexamples to BSD over Q.

## 3. Exact current task and next action

The dispatched task belongs to `/root/odd_rank_bridge`, whose completed turn
saved [family-specialization-checkpoint.md](family-specialization-checkpoint.md).
The live-agent snapshot confirmed it paused/completed, and the coordinator
updated the state table accordingly.

After the coordinator explicitly resumes it, the first action is to read
Disegni's [author PDF](https://disegni-daniel.perso.math.cnrs.fr/univ.pdf), identify
the exact universal p-adic Gross–Zagier height theorem, its hypotheses and
normalization, and the leading-Heegner-class conjecture located in the abstract.
Then formulate the strongest valid specialization lemma in a precise local
ring and determinant line, tracking the weight parameter U separately from
the cyclotomic parameter T, periods, rank jumps, and any Sha-finiteness premise.
Determine whether it supplies the fixed weight-two motive's complex comparison
or stops at a precisely quantified additional identity. Only then write
`family-specialization-attack.md`.

The checkpoint expressly distinguishes sources merely located through
search/abstracts from theorem statements actually read. Its scalar family
height identity is schematic; no determinant complex, specialization map,
period trivialization, or general family identity has been verified. Source
version corrections in `derived-comparison-attack.md` override legacy BKS
numbering in approach G. These are explicit remaining research steps, not
missing user instructions.

## 4. Dispatch status

Only the new family-specialization research task was dispatched in this round.
The visibility/modular-Jacobian route, integral/motivic higher-derivative route,
and root's proposed p-independent integral construction were **planned only**.
The uniform-witness agent's previous archimedean work and the
derived-comparison agent's previous genus-one work were completed earlier;
their proposed new tasks were not dispatched. This audit itself was dispatched
as a bounded continuity check, not research.

Live handles must be revalidated before follow-up or replacement. The current
tool inventory did not show `/root/derived_comparison`; its table entry is
historical, as the state file instructs. A timeout alone does not justify
duplicating an agent or process.

## 5. Reproduction and normalization

From `/Users/kaveh/bsd-conjecture`, the documented order is:

```sh
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_mellin.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_bsd_interval.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/certify_exceptional_primes.py
DOT_SAGE="$PWD/.tools/sage-home" .tools/sage/bin/sage -python compute/scripts/kurihara_witness.py
```

Code inspection confirms the archimedean script reads the Mellin JSON and the
exceptional-prime script reads its full-basis certificate from the archimedean
JSON. The Kurihara script has no input dependency on those three certificates.
Existing certificates are not to be rerun merely because context was lost.

The [compute guide](../../compute/README.md), ledger, and proof files retain
the important conventions: divide an r-th derivative by r!; BSD/Cremona height
is twice Silverman's half-height; the full real period includes both components
when the discriminant is positive; the raw 389a1 descent lattice has index 3
and cannot be used as a full regulator basis. PARI's p-adic L-series uses the
least real period, while the cited Sage series uses the full period; retain
the factor 2 and the `T=gamma-1`, `chi(gamma)=1+p` logarithms. At 389 the extra
T factor and L-invariant must remain. A finite-precision `O(p^k)` is not an
exact zero. The Mellin proof uses completed-L normalization, the Fricke sign,
both explicit tails, and Arb's analytic logarithm flag. Sage/Python integer
and finiteness-check pitfalls are also documented in state §6.

## 6. Files, checks, and ambiguities

All expected local targets linked from the resume notes and their main
proof/review files exist. The four scripts, four principal JSON certificates,
Sage executable, and Sage home exist. All **27** entries in
[checkpoint-manifest.json](checkpoint-manifest.json) matched both SHA-256 and
byte size when checked. The archimedean certificate's recorded analytic-input
SHA-256 also matches the actual Mellin JSON. These were read-only checks; the
historical four-script PASS results were not represented as fresh reruns.

`family-specialization-attack.md` is intentionally absent: the checkpoint says
it "has **not yet been created**". The manifest's initial temporary absence
was resolved during this audit. Neither is a broken dependency.

Two operational ambiguities were reported to and corrected by the coordinator:
the subagent-local `get_goal=null` versus parent goal state, and the table wording
"All three were originally launched" after addition of a fourth, nonresearch
audit handle. The goal-scope warning is now durable in both `AGENTS.md` and
state §2; state §5 now says "All three research agents". The reviewer reread
these corrections. The coordinator will refresh the manifest after this audit
and its final status-table update, so the earlier 27-entry hash check is a
timestamped observation, not a claim about later edits.
The paused agent's sentence "until the coordinator explicitly resumes the
task" requires an internal follow-up, not another permission request to the
user. No substantive missing information was found that requires the user to
reconstruct the research context.
