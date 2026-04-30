import json
import os
from datetime import datetime

HISTORY_FILE = "history.json"

def load_history() -> list:
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE) as f:
        content = f.read().strip()
        if not content:
            return []
        return json.loads(content)

def save_match(result: dict):
    history = load_history()
    history.append({
        "id": len(history) + 1,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "company": result.get("company"),
        "role": result.get("role"),
        "fit_score": result.get("fit_score"),
        "full_result": result
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_by_id(id: int) -> dict | None:
    history = load_history()
    for entry in history:
        if entry["id"] == id:
            return entry
    return None