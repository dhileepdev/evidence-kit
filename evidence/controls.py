def render_controls(evidence) -> dict:
    mapping = []
    for result in evidence.get("policy_results", {}).get("results", []):
        mapping.append(
            {
                "policy_id": result.get("policy_id"),
                "control": result.get("control"),
                "severity": result.get("severity"),
            }
        )
    return {
        "mapping": mapping,
        "disclaimer": "Illustrative mapping, not an audit opinion, not evidence of certification.",
    }
