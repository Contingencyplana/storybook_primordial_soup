# a0_0_add_empty_minigame_node/main.py

import os
import datetime

def add_empty_minigame_node(base_path, minigame_name):
    """
    Creates an empty minigame folder at the specified base path.
    No files or internals — only the outer node folder.

    Args:
        base_path (str): The parent directory where the minigame folder will be created.
        minigame_name (str): The name of the new minigame node folder (e.g., a0_0_test_minigame_node)

    Returns:
        dict: Confirmation with status, trace metadata, and path info.
    """
    minigame_path = os.path.join(base_path, minigame_name)

    # Safety check — don't overwrite existing folder
    if os.path.exists(minigame_path):
        return {
            "status": "skipped",
            "message": f"Minigame node '{minigame_name}' already exists.",
            "path": minigame_path,
            "trace": {
                "event": "skip_existing_minigame_node",
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
            }
        }

    # Create empty minigame node folder
    os.makedirs(minigame_path, exist_ok=True)

    return {
        "status": "success",
        "message": f"Created minigame node: {minigame_name}",
        "path": minigame_path,
        "trace": {
            "event": "create_empty_minigame_node",
            "minigame": minigame_name,
            "path": minigame_path,
            "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
        }
    }

# Note: No __main__ block — this function is designed to be imported or invoked by the workflow compiler.
