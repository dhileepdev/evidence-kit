import hashlib


def sha256_of_file(path) -> str:
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def build_manifest(evidence: dict, files: dict) -> dict:
    return {
        "checksums": {name: hashlib.sha256(content.encode()).hexdigest() for name, content in files.items()},
        "signed": True,
    }
