OPTIONAL_SOURCES = ("terraform_plan", "cluster_snapshot", "sbom")


def build_evidence(run_dir, policy_results, timestamp):
    """Assemble the evidence pack dict from a run dir and policy results.

    Policy results are required; optional sources are recorded as gaps
    when not supplied.
    """
    sources = {name: {"present": False, "gap": f"{name} not provided"} for name in OPTIONAL_SOURCES}
    return {
        "run": {"timestamp": timestamp, "run_dir": str(run_dir)},
        "policy_results": {"present": True, "results": policy_results.get("results", [])},
        "sources": sources,
    }
