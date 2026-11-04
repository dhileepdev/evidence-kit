def render_report(evidence) -> str:
    return "\n".join(
        [
            "# Evidence pack",
            "",
            "This report is an illustrative mapping, not an audit opinion and not evidence of certification.",
            "",
            f"Run timestamp: {evidence.get('run', {}).get('timestamp')}",
            f"Policy results present: {evidence.get('policy_results', {}).get('present')}",
        ]
    )
