# a2_0_add_empty_taskmaps_folder/main.py

import os
from datetime import datetime, timezone

def add_empty_taskmaps_folder(minigame_path):
    """
    Creates an empty taskmaps/ folder inside the specified minigame node folder.

    Args:
        minigame_path (str): The path to the target minigame node directory.

    Returns:
        dict: Confirmation with status, trace metadata, and path info.
    """
    taskmaps_path = os.path.join(minigame_path, "taskmaps")

    # Safety check — don't overwrite existing folder
    if os.path.exists(taskmaps_path):
        return {
            "status": "skipped",
            "message": f"taskmaps/ folder already exists in: {minigame_path}",
            "path": taskmaps_path,
            "trace": {
                "event": "skip_existing_taskmaps_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    # Create empty taskmaps/ folder
    os.makedirs(taskmaps_path, exist_ok=True)

    return {
        "status": "success",
        "message": f"Created taskmaps/ folder in: {minigame_path}",
        "path": taskmaps_path,
        "trace": {
            "event": "create_empty_taskmaps_folder",
            "path": taskmaps_path,
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

# Note: This function can be invoked by test.py or a meta-recursive builder.
