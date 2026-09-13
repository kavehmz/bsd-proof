#!/usr/bin/env python3
"""Export working research files and selected data, without native environments.

Requires an up-to-date research checkpoint. Python 3.9+, standard library.
The migration manifest excludes itself; the outer checksum covers it.
"""
import argparse
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import tarfile

from verify_handoff import CHECKPOINT, MIGRATION, local_path, sha256, verify

ROOT_FILES = (".gitignore", "AGENTS.md", "README.md", "START_HERE.md")
TREES = ("docs", "compute", ".tools/ecdata", ".tools/handoff-sources")


def selected_files(root):
    files = {name: local_path(root, name) for name in ROOT_FILES}
    for tree in TREES:
        base = local_path(root, tree)
        if not base.is_dir():
            raise ValueError("missing required export tree: " + tree)
        for path in sorted(base.rglob("*")):
            name = path.relative_to(root).as_posix()
            if "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                continue
            if path.is_symlink():
                raise ValueError("review symlink before exporting: " + name)
            if path.is_file() and name != MIGRATION:
                files[name] = path
    return dict(sorted(files.items()))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    output = args.output.resolve()
    checksum = output.with_name(output.name + ".sha256")
    if output.exists() or checksum.exists():
        parser.error("output/checksum already exists; choose a new snapshot filename")
    for tree in TREES:
        if output.is_relative_to(root / tree):
            parser.error("archive must be outside its selected input trees")
    checked = verify(root, checkpoint_only=True)
    if checked["errors"]:
        raise SystemExit(json.dumps(checked, indent=2))
    files = selected_files(root)
    manifest = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "paths_relative_to": "extracted bsd-conjecture directory",
        "research_checkpoint": CHECKPOINT,
        "scope": "working research files, raw outputs, package records, cached data and referenced sources",
        "excluded": [".git", "native environments/package binaries", "account/chat/agent state", "exports", "runs", "Python bytecode"],
        "self_hash_rule": "This manifest excludes itself. The companion archive checksum covers its bytes.",
        "files": {name: {"sha256": sha256(path), "bytes": path.stat().st_size}
                  for name, path in files.items()},
    }
    (root / MIGRATION).write_text(json.dumps(manifest, indent=2) + "\n")
    files[MIGRATION] = root / MIGRATION
    checked = verify(root)
    if checked["errors"]:
        raise SystemExit(json.dumps(checked, indent=2))
    output.parent.mkdir(parents=True, exist_ok=True)
    # Read each payload once for the archive and ensure it has not changed
    # since inventory. No symlinks, absolute archive paths or traversal.
    with output.open("xb") as raw:
        with tarfile.open(fileobj=raw, mode="w:gz") as archive:
            for name, path in sorted(files.items()):
                payload = path.read_bytes()
                if name != MIGRATION:
                    import hashlib
                    if hashlib.sha256(payload).hexdigest() != manifest["files"][name]["sha256"]:
                        raise RuntimeError("file changed during export: " + name)
                entry = tarfile.TarInfo("bsd-conjecture/" + name)
                entry.size = len(payload)
                entry.mode = 0o755 if path.stat().st_mode & 0o111 else 0o644
                entry.mtime = int(path.stat().st_mtime)
                archive.addfile(entry, io.BytesIO(payload))
    digest = sha256(output)
    with checksum.open("x") as stream:
        stream.write(digest + "  " + output.name + "\n")
    print(json.dumps({"archive": str(output), "sha256": digest,
                      "bytes": output.stat().st_size, "archived_files": len(files),
                      "verification": checked["status"]}, indent=2))


if __name__ == "__main__":
    main()
