from pathlib import Path

from evidence.pack import build_evidence
from evidence.report import render_report

GOLDEN = Path(__file__).parent / "golden" / "report.md"


def test_render_report_contains_control_mapping(tmp_path):
    evidence = build_evidence(tmp_path, {"results": []}, "2026-11-04T00:00:00Z")
    report = render_report(evidence)
    assert "illustrative" in report.lower()


def test_report_golden(tmp_path):
    evidence = build_evidence(tmp_path, {"results": []}, "2026-11-04T00:00:00Z")
    assert render_report(evidence) == GOLDEN.read_text()
