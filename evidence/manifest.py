import hashlib
from pathlib import Path

from evidence.signing import sign


def sha256_of_file(path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def build_manifest(evidence: dict, files: dict) -> dict:
    return {
        "checksums": {name: sha256_of_file(path) for name, path in files.items()},
        "signature": sign(evidence),
    }
