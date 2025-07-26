# a2_0_add_empty_taskmaps_folder/main.py

from pathlib import Path

def add_empty_taskmaps_folder(stanza_folder_path):
    stanza_path = Path(stanza_folder_path)
    taskmaps_path = stanza_path / "taskmaps"

    if taskmaps_path.exists():
        return {
            "status": "skipped",
            "message": f"taskmaps/ folder already exists in: {stanza_folder_path}",
            "path": str(taskmaps_path),
            "trace": {
                "event": "skip_existing_taskmaps_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    taskmaps_path.mkdir(parents=True, exist_ok=True)

    return {
        "status": "success",
        "message": f"Created taskmaps/ folder in: {stanza_folder_path}",
        "path": str(taskmaps_path),
        "trace": {
            "event": "create_empty_taskmaps_folder",
            "path": str(taskmaps_path),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
