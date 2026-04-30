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
    next_id = max((entry["id"] for entry in history), default=0) + 1
    history.append({
        "id": next_id,
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

def delete_by_id(id: int) -> bool:
    history = load_history()
    new_history = [entry for entry in history if entry["id"] != id]
    if len(new_history) == len(history):
        return False
    with open(HISTORY_FILE, "w") as f:
        json.dump(new_history, f, indent=2)
    return True