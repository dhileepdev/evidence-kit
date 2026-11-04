# ADR 0001: Collector lives in its own repository

- Status: accepted
- Date: 2026-11-04

## Context

The DevOps portfolio needs audit evidence produced by policy runs in
other repositories (plan/policy results, cluster snapshots, CI metadata).

## Decision

The collector that turns run artifacts into an evidence pack lives in its
own repository (`evidence-kit`). It consumes policy results as its required
input and records all other sources as optional gaps.

## Consequences

- `secure-delivery` keeps Conftest-on-plan out of this repo's CI.
- Packs are reproducible on a laptop with no token.
