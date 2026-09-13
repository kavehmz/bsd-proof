# Start or resume this BSD research project

This folder is the durable research record. A fresh AI session can continue
from it without access to the old conversation. **Full BSD over Q is still
neither proved nor disproved.** Round 25 is complete; the migration audit did
not start another research round.

## Moving to another computer

1. Copy the handoff archive and its `.sha256` file from `exports/`, then
   extract the archive into a new folder. The archive preserves the current
   working files, including uncommitted research and the data/source caches.
   **Cloning the last Git commit alone does not preserve this checkpoint.**
2. From the extracted `bsd-conjecture` folder, run:

   ```sh
   python3 compute/scripts/verify_handoff.py
   ```

   This checks saved bytes and certificate dependencies using only Python
   3.9 or newer. It is not a new mathematical proof or a rerun of Sage.
3. Open that folder in the new AI's workspace and paste the message from
   [fresh-session-prompt.md](docs/synthesis/fresh-session-prompt.md).
4. Follow [migration-guide.md](docs/synthesis/migration-guide.md) when a
   computation requires rebuilding Sage/PARI or relocating an audited script.

The archive omits installed native binaries, Git history/index, account
credentials and chat/agent state. They are not needed to read and continue
the mathematics. The mathematical software must be installed for the new
machine before rerunning a certificate. Keep the original folder as a backup.

## Read in stages, keeping context available for reasoning

Read [AGENTS.md](AGENTS.md), then the current override at the top of
[research-state.md](docs/synthesis/research-state.md). Next read
[final-report.md](docs/synthesis/final-report.md), the latest entries of
[research-ledger.md](docs/synthesis/research-ledger.md), and
[next-research-plan.md](docs/synthesis/next-research-plan.md). Read the
[charter](docs/00-charter.md) for the exact objective and evidence standards.
Then read only the full proofs, reviews and checkpoints needed by the chosen
target. Do not load every research file into one context window.

The current mathematical record takes precedence over historical status
tables. Old task IDs, agent names, usage limits and absolute machine paths
are historical metadata. A new session must inspect its own tools and state.

## Preserve the distinction between results and remaining work

Round 25 produced four separately reviewed constructions: a tangential
Poisson source with exact weighted trace, a derived/Gersten model with a
filled second point–K2 difference, global CM classes with enlarged
coefficients, and conditional mixed Heegner gluing. Their complete proofs
and review boundaries are linked in the state and report.

The first point–K2 difference, first Heegner products and top selection,
secondary CM-to-Kato/Selmer operation, rational arithmetic comparison,
and universal full BSD remain open. Saved PASS reviews are adversarial AI
reviews of specified claims/revisions, not formal proof-assistant checks
or a proof of the entire conjecture.

The [migration audit](docs/synthesis/migration-audit-2026-09-13.md) records
what was checked, what the package contains, and the remaining portability
limits. To export a later checkpoint, use the documented bundle builder;
this archive is a snapshot, not automatic synchronization.
