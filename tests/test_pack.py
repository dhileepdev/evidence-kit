from evidence.pack import build_evidence


def test_assemble_minimal_pack(tmp_path):
    evidence = build_evidence(tmp_path, {"results": []}, "2026-11-04T00:00:00Z")
    assert evidence["policy_results"]["present"]
