import hashlib
import json

DEMO_KEY = "evidence-kit-demo-key"


def sign(pack: dict, key: str = DEMO_KEY) -> dict:
    payload = json.dumps(pack, sort_keys=True)
    signature = hashlib.sha256((key + payload).encode()).hexdigest()
    return {"algorithm": "sha256", "key_id": "demo", "signature": signature}
