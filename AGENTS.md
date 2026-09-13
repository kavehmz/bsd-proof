# Research continuity instructions

For a fresh session or a different computer, first read `START_HERE.md` and
`docs/synthesis/migration-guide.md`. Run the standard-Python handoff checker
before editing a transferred snapshot. A fresh session does not inherit
the old task, goal, usage state or agent handles.

## Resume before doing new research

Read these files in order whenever context is missing or compacted:

1. `docs/synthesis/research-state.md` — objective, established results, open tasks, and agent handoff.
2. `docs/synthesis/research-ledger.md` — attempted arguments, verified distinctions, and source locations.
3. `docs/synthesis/final-report.md` — current mathematical status and links to complete proofs.

Use the current files and tool state as authoritative. Where available,
check `get_goal`, `git status --short`, and `collaboration.list_agents`
before resuming work. A fresh export may have no `.git`, no old goal and
different tool names. Record that fact and continue from the saved
mathematical objective using the host's actual capabilities; do not treat
absent old-session state as cancellation or a mathematical blocker.
An old agent-status entry is a snapshot, not proof that the agent remains live.
Do not restart a process or duplicate an agent solely because an observation timed out.
The parent goal is owned by the coordinator task. A subagent's `get_goal`
may return null even while the coordinator's goal is active; report that
scope difference to the coordinator rather than creating or closing a goal.

## Persistent user requirements

- The objective is to **prove or disprove full Birch–Swinnerton-Dyer for elliptic
  curves over Q**, as defined in `docs/00-charter.md`. Do not redefine success
  as a proof for 389a1, a reduction, a numerical match, or a formal countermodel.
- The user authorized sustained research and subagents, without a specified
  token budget. Do not infer a finite budget.
- **Every research subagent must use `gpt-6-astra` with `xhigh` reasoning.**
  Do not switch models after a capacity error; preserve the work and retry
  the same model, or report the specific operational problem.
- For a new independent session, the user also permits an equally capable
  AI with tooling as coordinator (2026-09-13 migration request). This does
  not silently relax the existing research-subagent preference. If no
  suitable subagent tool is available, work locally and retain new claims
  as awaiting separate adversarial review until that review is obtained.
- Do not treat difficulty or the historical open status as proof of impossibility.
  State only what the arguments establish. Never fabricate a proof or counterexample.
- The active goal remains active until its full completion is verified, subject
  to the platform's strict rules for genuinely blocked goals.

## Durable checkpoints

Update `research-state.md` after a material result, change of approach, or agent
handoff, and before yielding a long research turn. Add a concise entry to the
ledger when a proposed argument is proved, corrected, or ruled out.
Each live agent should save its own proof attempt and a short restart checkpoint
before a long pause; record exact owned files and next actions.

Preserve full proofs, assumptions, source versions, reproduction commands,
verification results, and unresolved statements in files. Do not depend on
conversation history or ephemeral tool references for these facts.

The worktree contains substantial uncommitted research. Do not reset, clean,
or overwrite it. Existing scripts and certificates should only be rerun when
needed for new changes, a specific concern, or a verification dependency.

Follow the charter's epistemic tags and independent review requirements.
Counterexamples to abstract modules, power-series shortcuts, or statements
over other base fields are **not** counterexamples to BSD over Q.
