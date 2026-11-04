import argparse
import json
import sys
from pathlib import Path

from evidence.controls import render_controls
from evidence.manifest import build_manifest
from evidence.pack import build_evidence
from evidence.report import render_report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="evidence")
    subparsers = parser.add_subparsers(dest="command")
    audit = subparsers.add_parser("audit")
    audit.add_argument("--run-dir", required=True, type=Path)
    audit.add_argument("--policy-results", required=True, type=Path)
    audit.add_argument("--timestamp", required=True)
    args = parser.parse_args(argv)
    if args.command != "audit":
        parser.error("command required: audit")

    try:
        policy_results = json.loads(args.policy_results.read_text())
    except FileNotFoundError:
        print(f"policy results not found: {args.policy_results}", file=sys.stderr)
        return 2

    evidence = build_evidence(args.run_dir, policy_results, args.timestamp)
    out = args.run_dir
    out.mkdir(parents=True, exist_ok=True)
    evidence_path = out / "evidence.json"
    report_path = out / "report.md"
    controls_path = out / "controls.json"
    manifest_path = out / "manifest.json"

    evidence_path.write_text(json.dumps(evidence, indent=2))
    report_path.write_text(render_report(evidence))
    controls_path.write_text(json.dumps(render_controls(evidence), indent=2))

    manifest = build_manifest(
        evidence,
        {"evidence.json": evidence_path, "report.md": report_path, "controls.json": controls_path},
    )
    manifest_path.write_text(json.dumps(manifest, indent=2))
    return 0
