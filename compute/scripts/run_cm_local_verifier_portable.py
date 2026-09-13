#!/usr/bin/env python3
"""Relocate only the two path assignments in the frozen audited CM verifier.

--check uses standard Python; execution requires Sage. Outputs are separate
from the original certificate and explicitly record the adapted execution.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

FROZEN = "compute/scripts/verify_cm_local_taylor_mod5.py"
FROZEN_HASH = "72c397c20fcb27e250b282d950305fc36493a4ef1b8231be276adec0eb788027"
INPUTS = {
    FROZEN: FROZEN_HASH,
    "compute/scripts/cm_local_taylor_mod5.py": "0fffae4120bc9a2632bc174444832fea0bb3f91450bdc984e594d2ee0e336586",
    "compute/data/cm_local_taylor_mod5.json": "900a9060c40de02e5d541276d358938a7929b6538f4fef23db31f6954462c307",
}


def prepare(root, destination):
    for name, expected in INPUTS.items():
        actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
        if actual != expected:
            raise ValueError("frozen input differs: " + name)
    tree = ast.parse((root / FROZEN).read_bytes(), filename=FROZEN)
    original = copy.deepcopy(tree)
    paths = {"ROOT": ("/Users/kaveh/bsd-conjecture", str(root)),
             "dest": ("/tmp/cm_local_taylor_independent.json", str(destination))}
    changed = []
    for index, node in enumerate(tree.body):
        if not (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)):
            continue
        name = node.targets[0].id
        if name in paths:
            old, new = paths[name]
            expected = ast.parse("Path(" + repr(old) + ")", mode="eval").body
            if ast.dump(node.value) != ast.dump(expected):
                raise ValueError("unexpected path assignment: " + name)
            node.value = ast.copy_location(ast.parse("Path(" + repr(new) + ")", mode="eval").body, node.value)
            changed.append(index)
    if len(changed) != 2:
        raise ValueError("expected exactly two path substitutions")
    ast.fix_missing_locations(tree)
    restored = copy.deepcopy(tree)
    for index in changed:
        restored.body[index] = original.body[index]
    if ast.dump(restored) != ast.dump(original):
        raise ValueError("non-path syntax changed")
    record = {
        "original_audited_script_sha256": FROZEN_HASH,
        "adapter_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "executed_ast_sha256": hashlib.sha256(ast.dump(tree).encode()).hexdigest(),
        "path_substitutions": {name: {"old": old, "new": new} for name, (old, new) in paths.items()},
        "scope": "Original source frozen; executed syntax differs only at ROOT and dest assignments.",
        "mathematical_body_unchanged": True,
    }
    return tree, record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output-dir", type=Path,
                        help="new run directory; defaults to PROJECT/runs/cm-local-verifier")
    parser.add_argument("--check", action="store_true", help="check inputs and path adaptation without executing Sage")
    args = parser.parse_args()
    root = args.root.resolve()
    directory = (args.output_dir or root / "runs/cm-local-verifier").resolve()
    destination = directory / "result.json"
    tree, record = prepare(root, destination)
    if args.check:
        print(json.dumps({"status": "PASS", "computation_executed": False, **record}, indent=2))
        return
    if directory.exists():
        parser.error("run directory already exists; choose a new --output-dir")
    directory.mkdir(parents=True)
    (directory / "portability.json").write_text(json.dumps(record, indent=2) + "\n")
    # The frozen program hashes __file__. Keep that field meaning the original
    # source and expose the actual execution's adapter/AST hashes separately.
    namespace = {"__name__": "__main__", "__file__": str(root / FROZEN)}
    exec(compile(tree, str(root / FROZEN), "exec"), namespace)
    result = json.loads(destination.read_text())
    result["portable_execution"] = record
    destination.write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
