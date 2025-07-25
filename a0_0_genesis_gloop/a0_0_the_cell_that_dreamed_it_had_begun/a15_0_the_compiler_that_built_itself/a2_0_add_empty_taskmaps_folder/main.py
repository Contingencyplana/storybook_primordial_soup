# a2_0_add_empty_taskmaps_folder/main.py

import os
from datetime import datetime, timezone

def add_empty_taskmaps_folder(stanza_folder_path):
    """
    Creates an empty taskmaps/ folder at the stanza (minigame) level.

    Args:
        stanza_folder_path (str): The path to the Layer 3 minigame folder.

    Returns:
        dict: Confirmation with status, trace metadata, and path info.
    """
    taskmaps_path = os.path.join(stanza_folder_path, "taskmaps")

    if os.path.exists(taskmaps_path):
        return {
            "status": "skipped",
            "message": f"taskmaps/ folder already exists in: {stanza_folder_path}",
            "path": taskmaps_path,
            "trace": {
                "event": "skip_existing_taskmaps_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    os.makedirs(taskmaps_path, exist_ok=True)

    return {
        "status": "success",
        "message": f"Created taskmaps/ folder in: {stanza_folder_path}",
        "path": taskmaps_path,
        "trace": {
            "event": "create_empty_taskmaps_folder",
            "path": taskmaps_path,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

# Note: This function should be invoked at the minigame level, not from within a stanza folder.
