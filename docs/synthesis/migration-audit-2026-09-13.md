# Fresh-session migration audit — 2026-09-13

This is a continuity and portability audit requested before further
research. It makes no new mathematical claim. Full BSD over Q remains
neither proved nor disproved, and no research round after round 25 was
dispatched.

## Baseline and work preserved

Before edits, all **258** files in the existing research checkpoint matched
their saved SHA-256 hashes. The current working tree had **248 staged added
paths and 6 staged modified paths** relative to commit
`794024f56cbd04109fed1bbc363337ffa40cff24` on `main`. No reset, clean, commit,
push or index change was performed. A clone of that commit alone would
omit substantial research.

The proof/review/checkpoint files for the four round25 routes are saved.
Their mathematical content and the original numerical scripts/certificates
were not changed by this migration work. Exact review scope and reviewed
revision hashes remain in the full reviews. These are saved adversarial
AI reviews, not a formal proof-assistant verification or external peer
review of all mathematics.

Older source notes, raw numerical outputs and wrappers existed outside the
258-file checkpoint. The updated research inventory includes the broader
document/script/output record, while the separate migration inventory also
includes ignored external data and source caches. Historical verification
counts remain historical; current file counts are returned by the checker.

## Migration gaps addressed

- Added [START_HERE.md](../../START_HERE.md), a
  [copy-and-paste starting prompt](fresh-session-prompt.md), and a
  [migration guide](migration-guide.md). Updated root instructions to
  distinguish new-session capabilities from old task/agent snapshots.
- Added a standard-library Python checker for both manifests, stored data
  JSON/JSONL, and the ten certificate input-hash dependencies. It works
  without Git, Sage, network access or old-session tools.
- Added a bundle builder that selects actual working files independently of
  Git, includes raw logs and cached data, records an inventory, and writes
  an archive/checksum. It excludes installed native environments and
  account/chat state. It refuses to export a stale research checkpoint.
- Preserved all **18 existing temporary artifacts explicitly referenced**
  by the pre-migration Markdown notes: two already had byte-identical
  permanent script/output copies; sixteen were copied into the portable
  source cache. One additional `.py/json` reference is notation shorthand,
  resolved to its two actual files. No real referenced temporary file was
  missing. See [source-cache-index.json](source-cache-index.json).
- Included all **115** cached Cremona files, including the exact table
  required by the CM p-adic certificate. The cache is data, not a native
  executable environment.
- Saved installed metadata for **387 Sage-environment packages** and
  **53 PARI-environment packages**, with explicit macOS arm64 package
  specifications. The observed cypari2 version is 2.2.2; the old README's
  2.2.4 claim is not the observed installed version.
- Preserved the audited independent CM verifier unchanged and added a
  separate adapter which verifies frozen input hashes and changes only
  its `ROOT` and output-path assignments. Adapted execution carries its
  own provenance and writes a separate result.

## Verification record

The preflight archive was extracted under a different temporary directory
and checked using **Python 3.9.6**, from outside the extracted project root,
with no Git directory, Sage environment or old-session tools in the copy.
The results were:

| Check | Result |
|---|---|
| Research checkpoint, including expanded document/script/output inventory | PASS, 324 files |
| Complete migration inventory | PASS, 456 entries; archive adds the manifest itself for 457 files |
| Certificate-to-input SHA-256 dependencies | PASS, all 10 |
| Stored data JSON parsing, with historical `certify_ran.json` treated as JSONL | PASS, 19 files |
| Local Markdown artifact-file targets | PASS, 1,058 targets present |
| Portable CM adapter at the new root, without executing Sage | PASS, frozen hashes and exact two-path substitution |
| Changed `AGENTS.md` rejected by checker | PASS |
| Missing ignored CM table rejected by checker | PASS |
| Changed frozen CM verifier rejected by adapter | PASS |
| Stale checkpoint rejected by bundle builder, without creating an archive | PASS |
| Test files restored, complete copy checked again | PASS |

The artifact-link check excludes mathematical bracket notation and
historical task-ID links; it checks target files, not Markdown section
anchors or external URL availability. The new working diff passed
`git diff --check`. `git diff --cached --check` reported six pre-existing
whitespace diagnostics in staged proof/review files; those audited bytes
were preserved. No mathematical file was edited to clear formatting output.

The final archive uses the same selected file set with this completed
audit record and updated manifests. Its outer checksum accompanies it;
verify that checksum and run the checker after transfer. The original
mathematical certificate suite was not rerun for this audit.

## What is not transferred or claimed

The archive is a fixed research snapshot. It omits Git history/index, native
Sage/PARI binaries, package binaries, active tasks/processes, account state,
chat history and unreferenced scratch files. It is not a complete offline
mirror of every cited publication. Primary URLs, versions and existing
hashes remain in the proofs; use the source index for old temporary paths.

The new machine's environment installation and full Sage execution of the
portable verifier are not tested by this audit. Package availability must
be checked when rebuilding. File-hash success verifies transfer integrity,
not truth of every mathematical assertion. No claim is made that a full
BSD proof is close or that any remaining arithmetic obstruction is resolved.

The user may start an independent coordinator on an equally capable AI
with tooling. The existing Astra/xhigh instruction for research subagents
is preserved. The old scheduler/usage state is historical metadata and is
not a prerequisite for reconstructing the mathematics on another host.
