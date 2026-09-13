# Message to paste into a fresh AI session

Copy the following message after opening the transferred project folder as
the new workspace. No transcript from the old session is required.

---

Continue the BSD research project in this workspace from its saved files.
The objective is to prove or disprove **full Birch–Swinnerton-Dyer for every
elliptic curve over Q**, including rank equality, finiteness of the full Sha
group, and the exact leading-term formula. It is not complete. Do not
substitute a test-curve result, numerical agreement, a conditional reduction,
or a counterexample to an auxiliary model for that objective.

First read `START_HERE.md` and `AGENTS.md`, and run
`python3 compute/scripts/verify_handoff.py` from the workspace root. Inspect
any mismatch before editing; do not rewrite hashes merely to obtain PASS.
This is a fresh independent session. Old task IDs, agent handles, absolute
paths and goal/usage snapshots in the notes are historical. Missing old
session tools or handles are normal; use the actual tools available here.

Recover the mathematics in stages: read the latest override in
`docs/synthesis/research-state.md`, `docs/synthesis/final-report.md`, the
latest entries of `docs/synthesis/research-ledger.md`,
`docs/synthesis/next-research-plan.md`, and `docs/00-charter.md`. Read the
full proof, independent review and restart checkpoint for each target you
actually use. Do not attempt to fit the whole repository in context. Treat
the latest explicit corrections and review scope as authoritative over
historical summaries. State which results and remaining obligations you
recovered before beginning new mathematics.

I authorize sustained research and research subagents, with no specified
token budget. Use GPT-6 Astra with extra-high reasoning for research
subagents (`gpt-6-astra`, `xhigh` where those tool values apply). The new
coordinator may be GPT-6 Astra or an equally capable AI with tooling. Do
not silently switch research subagents to a weaker model after an error.
When no suitable subagent tool is available, make useful progress locally
and keep new claims awaiting a separate adversarial review. Do not treat
an absent old-session goal as cancellation or create a platform goal
contrary to that platform's instructions.

Do not assume impossibility from difficulty or historical open status.
Use any rigorous approach that advances the objective, while reporting
exactly what has been established. Never fabricate a proof, a reference,
a computation or confidence. Investigate apparent gaps; do not hide them.

Round 25 is complete with four separate PASS reviews. The next targets
are the actual first point–K2 difference, the specified first Heegner
products and top selection, a secondary arithmetic operation taking the
global CM classes with enlarged coefficients to the original Kato/Selmer
output, and the rational arithmetic comparison. These are starting
directions, not a prohibition on a better rigorously justified approach.
Do not redo the completed constructions as if they were still open.

After recovery, choose a concrete bounded research round, work on it,
obtain separate review of new claims when available, and save full proofs,
source versions, reproduction commands, exact hypotheses, and unresolved
statements in the repository. Update the state and ledger before context
compression or yielding. Complete one round, then report what changed,
whether it brings us nearer, and the exact remaining gap. Preserve the
working files and original audited scripts/certificates. Rebuild native
software using `docs/synthesis/migration-guide.md` only when needed; do not
rerun the entire numerical suite simply because this session is new.
