def render_report(evidence) -> str:
    results = evidence.get("policy_results", {}).get("results", [])
    sources = evidence.get("sources", {})
    gaps = [name for name, source in sources.items() if not source.get("present")]
    return "\n".join(
        [
            "# Evidence pack",
            "",
            "This report is an illustrative mapping, not an audit opinion and not evidence of certification.",
            "",
            f"Run timestamp: {evidence.get('run', {}).get('timestamp')}",
            f"Policy results present: {evidence.get('policy_results', {}).get('present')}",
            f"Policy results evaluated: {len(results)}",
            f"Optional sources missing: {', '.join(gaps) if gaps else 'none'}",
        ]
    )
