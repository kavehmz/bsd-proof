#!/usr/bin/env python3
"""Read-only, standard-library verification of a saved BSD checkpoint/transfer.

Checks bytes and recorded certificate dependencies, not mathematical validity.
Python 3.9+. Deliberately does not require Git, Sage, network or old task tools.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

CHECKPOINT = "docs/synthesis/checkpoint-manifest.json"
MIGRATION = "docs/synthesis/migration-manifest.json"


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def local_path(root, name):
    rel = PurePosixPath(name)
    if not name or rel.is_absolute() or ".." in rel.parts or "\\" in name:
        raise ValueError("unsafe relative path: " + name)
    path = root.joinpath(*rel.parts)
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError("path escapes project: " + name)
    if any(p.is_symlink() for p in (path, *path.parents) if p != root.parent):
        # A root reached through a platform alias (e.g. /tmp on macOS) is
        # resolved by the CLI before calling this function.
        raise ValueError("symlink is not a saved regular artifact: " + name)
    return path


def check_records(root, manifest, errors, label):
    records = manifest.get("files")
    if not isinstance(records, dict) or not records:
        errors.append(label + ": empty/missing files inventory")
        return 0
    for name, record in records.items():
        try:
            path = local_path(root, name)
            if not path.is_file():
                raise ValueError("missing file")
            if path.stat().st_size != record["bytes"]:
                raise ValueError("byte count differs")
            if sha256(path) != record["sha256"]:
                raise ValueError("SHA-256 differs")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(label + ": " + name + ": " + str(exc))
    return len(records)


def verify(root, checkpoint_only=False):
    root = root.resolve()
    errors = []
    result = {"root": str(root), "scope": "saved bytes/dependencies; not a mathematical proof"}
    try:
        checkpoint = json.loads((root / CHECKPOINT).read_text())
        result["checkpoint_files"] = check_records(root, checkpoint, errors, "checkpoint")
        deps = checkpoint["verification"]["dependency_checks"]
        if not deps:
            raise ValueError("missing certificate dependency inventory")
        for dep in deps:
            try:
                data = json.loads(local_path(root, dep["data"]).read_text())
                actual = sha256(local_path(root, dep["source"]))
                if data[dep["field"]] != actual:
                    raise ValueError("recorded input hash differs")
            except (OSError, ValueError, KeyError, TypeError) as exc:
                errors.append("dependency " + str(dep) + ": " + str(exc))
        result["certificate_dependencies"] = len(deps)
        validated = 0
        for name in checkpoint["files"]:
            if name.startswith("compute/data/") and name.endswith(".json"):
                try:
                    path = local_path(root, name)
                    if name == "compute/data/certify_ran.json":
                        # Historical filename contains two JSONL records.
                        for line in path.read_text().splitlines():
                            if line.strip():
                                json.loads(line)
                    else:
                        json.loads(path.read_text())
                    validated += 1
                except (OSError, ValueError) as exc:
                    errors.append("JSON " + name + ": " + str(exc))
        result["data_json_files_parsed"] = validated
        if not checkpoint_only:
            migration = json.loads((root / MIGRATION).read_text())
            result["migration_files"] = check_records(root, migration, errors, "migration")
            # The transfer inventory must cover every checkpointed artifact,
            # the checkpoint itself, and all explicitly recorded inputs.
            required = set(checkpoint["files"]) | {CHECKPOINT}
            required.update(d["data"] for d in deps)
            required.update(d["source"] for d in deps)
            for name in sorted(required - set(migration["files"])):
                errors.append("missing from migration inventory: " + name)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("manifest: " + str(exc))
    result["errors"] = errors
    result["status"] = "FAIL" if errors else "PASS"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--checkpoint-only", action="store_true",
                        help="check the research checkpoint without an old transfer snapshot")
    args = parser.parse_args()
    result = verify(args.root, args.checkpoint_only)
    print(json.dumps(result, indent=2))
    return bool(result["errors"])


if __name__ == "__main__":
    sys.exit(main())
