"""Policy evidence sources: Terraform plan JSON, OPA results, Kyverno results."""

from .collector import build_evidence

__all__ = ["build_evidence"]
