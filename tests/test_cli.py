import json

from evidence.cli import main


def test_cli_writes_pack(tmp_path):
    policy_results = tmp_path / "policy-results.json"
    policy_results.write_text(json.dumps({"results": []}))
    rc = main(["--run-dir", str(tmp_path), "--policy-results", str(policy_results)])
    assert rc == 0
    assert (tmp_path / "evidence.json").exists()
