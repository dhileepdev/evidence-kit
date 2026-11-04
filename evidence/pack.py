from pathlib import Path

from evidence.sources import read_json

OPTIONAL_SOURCES = ("terraform_plan", "cluster_snapshot", "sbom")


def build_evidence(run_dir, policy_results, timestamp):
    run_path = Path(run_dir)
    policy_present = policy_results is not None and isinstance(policy_results, dict) and "results" in policy_results
    sources = {}
    for name in OPTIONAL_SOURCES:
        source_path = run_path / f"{name}.json"
        if source_path.exists():
            sources[name] = {"present": True, "data": read_json(source_path)}
        else:
            sources[name] = {"present": False, "gap": f"{name} not provided"}
    return {
        "run": {"timestamp": timestamp, "run_dir": str(run_path)},
        "policy_results": {
            "present": policy_present,
            "results": policy_results.get("results", []) if policy_present else [],
        },
        "sources": sources,
    }
