import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME, 'r') as f:
        data = json.load(f)
    total = sum(item["score"] * item["weight"] for item in data)
    return float(f"{total:.3f}")

print(task())
