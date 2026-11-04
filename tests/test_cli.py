import json

from evidence.cli import main


def test_cli_writes_pack(tmp_path):
    policy_results = tmp_path / "policy-results.json"
    policy_results.write_text(json.dumps({"results": []}))
    rc = main(
        [
            "audit",
            "--run-dir",
            str(tmp_path),
            "--policy-results",
            str(policy_results),
            "--timestamp",
            "2026-11-04T00:00:00Z",
        ]
    )
    assert rc == 0
    assert (tmp_path / "evidence.json").exists()
    assert (tmp_path / "report.md").exists()
    assert (tmp_path / "controls.json").exists()
    assert (tmp_path / "manifest.json").exists()
