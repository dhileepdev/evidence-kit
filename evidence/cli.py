import argparse
import json
from pathlib import Path

from evidence.controls import render_controls
from evidence.manifest import build_manifest
from evidence.pack import build_evidence
from evidence.report import render_report
from evidence.signing import sign


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="evidence")
    parser.add_argument("--run-dir", required=True, type=Path)
    parser.add_argument("--policy-results", required=True, type=Path)
    args = parser.parse_args(argv)

    policy_results = json.loads(args.policy_results.read_text())
    evidence = build_evidence(args.run_dir, policy_results, "2026-11-04T00:00:00Z")
    signed = sign(evidence)
    manifest = build_manifest(evidence, {"evidence.json": json.dumps(evidence, indent=2), "report.md": render_report(evidence)})

    args.run_dir.mkdir(parents=True, exist_ok=True)
    (args.run_dir / "evidence.json").write_text(json.dumps(evidence, indent=2))
    (args.run_dir / "report.md").write_text(render_report(evidence))
    (args.run_dir / "controls.json").write_text(json.dumps(render_controls(evidence), indent=2))
    (args.run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2))
    return 0
