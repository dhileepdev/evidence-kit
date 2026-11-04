import json
from pathlib import Path


def read_json(path):
    """Read a JSON artifact; missing files raise FileNotFoundError."""
    return json.loads(Path(path).read_text())
