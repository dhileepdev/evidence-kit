# evidence-kit

Audit evidence automation for DevOps runs: a policy library plus a collector
that emits signed, checksummed evidence packs from a run's policy artifacts.

Status: scaffold (v0.1.0 in progress).

## Audit pack

`make audit` builds an evidence pack from a run directory:

```bash
make audit
```

Writes `evidence.json`, `report.md`, `controls.json`, `manifest.json` into the
run directory.
