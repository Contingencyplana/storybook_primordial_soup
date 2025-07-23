# a2_0_add_empty_taskmaps_folder/main.py

import os
from datetime import datetime, timezone

def create_taskmaps_folder(minigame_node_path):
    """
    Creates the taskmaps/ folder inside the specified minigame node path.

    Args:
        minigame_node_path (str): Path to the minigame node directory.

    Returns:
        dict: Summary of the operation including status, event type, path, and timestamp.
    """
    taskmaps_path = os.path.join(minigame_node_path, "taskmaps")
    timestamp = datetime.now(timezone.utc).isoformat()

    if not os.path.exists(taskmaps_path):
        os.makedirs(taskmaps_path)
        status = "added"
        event = "created_taskmaps_folder"
    else:
        status = "skipped"
        event = "existing_taskmaps_folder"

    return {
        "status": status,
        "event": event,
        "path": taskmaps_path,
        "timestamp": timestamp
    }
