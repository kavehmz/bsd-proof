# Moving this research to a fresh computer and session

The portable archive is a research checkpoint, including working files
that were never committed. It does not transfer an active conversation.
Start with [START_HERE.md](../../START_HERE.md) and use the
[fresh-session prompt](fresh-session-prompt.md).

## Transfer and verify

Copy `exports/bsd-research-handoff-2026-09-13.tar.gz` and its companion
`.sha256` file using your usual file transfer. Keep both together. On a
machine with `sha256sum`, verify the outer archive before extraction:

```sh
sha256sum -c bsd-research-handoff-2026-09-13.tar.gz.sha256
tar -xzf bsd-research-handoff-2026-09-13.tar.gz
cd bsd-conjecture
python3 compute/scripts/verify_handoff.py
```

On macOS, `shasum -a 256 -c` can replace `sha256sum -c`. An archive manager
can extract the same file. Use a new empty destination; avoid overlaying
unrelated work. On Windows use the available Python command (`python` or
`py -3`) for verification. The checker needs Python 3.9+ and no third-party
packages. Its paths resolve from the extracted project, not the old home
directory. Run the new AI from the project root.

The checksum detects changes relative to the supplied snapshot; it is not
a digital signature or mathematical validation. The checker validates the
research manifest, the complete migration inventory, and the ten saved
certificate-to-input hash dependencies. A successful transfer check does
not imply the conjecture or every argument in the repository is proved.

The package includes all regular files under `docs/`, `compute/`, and the
root instructions, excluding Python bytecode. It includes raw computation
logs, all cached Cremona data under `.tools/ecdata/`, and the temporary
source artifacts explicitly referenced in the pre-migration notes that
were found and preserved. The exact selection is in
[migration-manifest.json](migration-manifest.json). Source relocation is
recorded in [source-cache-index.json](source-cache-index.json).

The `.tools/` directory is hidden and Git-ignored. The archive explicitly
includes its selected data caches; a normal Git clone does not. In
particular, keep `.tools/ecdata/allcurves/allcurves.40000-49999`: the CM
p-adic certificate records its exact hash. Do not accept a changed upstream
table under the old certificate's provenance.

Git history/index and installed native environments are omitted. Research
can continue without `.git`. If Git history is also desired, transfer it
separately or preserve it in another backup; a clone may supply history,
but the archived working files must still be restored. The original
checkout had 248 staged added paths and 6 staged modified paths before
this migration work. These staged changes must not be discarded.

## Fresh-session instructions and capabilities

Set the transferred folder as the workspace. Codex discovers project
`AGENTS.md` instructions when a session starts; global or more local
overrides may also apply. Explicitly reading `START_HERE.md` in the starter
prompt ensures the handoff is used by other tooling AIs as well.
[Official instruction-discovery documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

The new coordinator may use GPT-6 Astra or an equally capable AI with tools,
as the user allowed on 2026-09-13. The existing research-subagent preference
remains GPT-6 Astra / extra-high reasoning. Record actual model and effort
when dispatching. Tool names in historical notes are examples from the old
host, not required APIs. File reads/writes, a shell with Python, primary
source browsing, and suitable mathematical computation are the substantive
capabilities. Separate adversarial review remains required for relying on
new claims; if unavailable, retain their unreviewed status.

Old task/agent IDs, pending tool sessions, and `usageLimited`/goal snapshots
do not transfer. Inspect fresh local state. Missing tools, no `.git`, or a
null goal in a new session do not erase the mathematical objective. Do not
try to message historical handles. Preserve notes before a long pause and
use the latest current override instead of historical ownership tables.

## Rebuild mathematics software only when needed

Reading, integrity verification and further symbolic research need no Sage
installation. Existing certificates and their reviews remain available.
For new numerical work, install software appropriate to the destination OS
and architecture. The old installation was macOS arm64; copying its binary
environment to another machine is not a portable installation procedure.

[installed-package-inventory.json](../../compute/environment/installed-package-inventory.json)
records the actual package metadata at export. The Sage environment used
Sage 10.7, Python 3.11.16, PARI 2.17.3 and eclib 20250627. The separate
PARI environment had pari-elldata 0.0.20161017. The live package metadata
records cypari2 **2.2.2** in both environments; this corrects the older
README's installation-log claim of 2.2.4 for purposes of rebuilding.

For another macOS arm64 installation with micromamba already available,
the saved explicit package specifications are:

```sh
micromamba create -y -p "$PWD/.tools/sage" -f compute/environment/sage-osx-arm64-explicit.txt
micromamba create -y -p "$PWD/.tools/env" -f compute/environment/pari-osx-arm64-explicit.txt
```

They record package URLs and hashes from the installed conda metadata.
Availability of those packages and installation on another machine have
not been tested. For a different platform, use that platform's supported
Sage/PARI installation method; do not feed macOS package locks to it.
The original installation commands and computational dependency order
remain in [compute/README.md](../../compute/README.md). Record actual new
versions and verify the particular arithmetic on which new work depends.

Run existing commands from the project root. The `gp` and `python` wrappers
find the root relative to their own paths, but expect the local
`.tools/env` layout. A system Sage can instead be invoked as
`sage -python compute/scripts/NAME.py`. Set `DOT_SAGE` to a writable local
directory if necessary. `certify_bsd_interval.py` reads optional package
version metadata from `.tools/sage/conda-meta`; a different installation
may require a separate environment record. Some old scripts write directly
to `compute/data/`, so use a separate working copy for reproduction and
compare with the preserved certificate, rather than overwriting evidence.

## The audited verifier with an absolute path

[verify_cm_local_taylor_mod5.py](../../compute/scripts/verify_cm_local_taylor_mod5.py)
is preserved byte-for-byte because its hash is recorded by the independent
certificate. Its `ROOT` assignment and output path refer to the old machine.
Use the separate portable adapter:

```sh
python3 compute/scripts/run_cm_local_verifier_portable.py --check
sage -python compute/scripts/run_cm_local_verifier_portable.py
```

The first only verifies the frozen inputs and the two path substitutions;
it does not import Sage or compute. The second executes the same audited
program with just those two path expressions replaced, retaining all
mathematical statements and assertions. It records the original script,
adapter and adapted syntax-tree hashes, and writes a separate result and
provenance under `runs/cm-local-verifier/`. The original-script hash refers
to the preserved source; the provenance explicitly identifies the adapted
execution. No assertion is removed or numerical formula changed. This
adapter was structurally tested during migration; its full Sage execution
was not rerun. If that output folder already contains a run, pass a new
`--output-dir` instead of replacing the earlier result.

## Sources, later checkpoints and limits

Use the source-cache index to translate old `/tmp/` references to portable
paths. Papers elsewhere in the research retain primary URLs, exact versions
and, where recorded, PDF hashes. This is not a complete offline mirror of
every cited paper. Fetch other primary sources as needed and verify their
version/numbering. A different PDF hash is a source revision to inspect,
not a reason to silently relabel it as the old reviewed payload.

The package is not a transcript or a guarantee that every abandoned scratch
calculation was saved. It preserves the documented proofs, reviews, open
obligations, scripts, data, and identified recovery dependencies. Continue
to audit claims using the full arguments; saved review labels do not
replace reading their scope and corrections.

After research changes, the old migration manifest correctly reports a
different snapshot. Preserve the old archive, review and update the
research checkpoint hashes, then generate a new named export:

```sh
python3 compute/scripts/verify_handoff.py --checkpoint-only
python3 compute/scripts/build_handoff.py --output exports/bsd-research-handoff-NEXT.tar.gz
```

The builder refuses a stale research checkpoint, inventories current
working files independently of Git, refreshes the migration manifest, and
creates an archive plus checksum. It never commits, pushes, installs
software or copies account credentials. Existing archives are not overwritten.
