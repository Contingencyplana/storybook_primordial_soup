# a0_1_add_empty_init_file/main.py

import os
from datetime import datetime, timezone

def add_empty_init_file(minigame_node_path):
    """
    Creates an empty __init__.py file in the given minigame node folder.
    Skips creation if the file already exists. Returns an error if the folder does not exist.

    Args:
        minigame_node_path (str): The path to the target minigame node folder.

    Returns:
        dict: Structured response with status, path, and trace metadata.
    """
    # Check if the target folder exists
    if not os.path.exists(minigame_node_path):
        return {
            "status": "error",
            "message": "Target minigame node folder does not exist.",
            "path": minigame_node_path,
            "trace": {
                "event": "missing_minigame_node_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    init_file_path = os.path.join(minigame_node_path, "__init__.py")

    # Skip if file already exists
    if os.path.exists(init_file_path):
        return {
            "status": "skipped",
            "message": "__init__.py already exists.",
            "path": init_file_path,
            "trace": {
                "event": "skip_existing_init",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    # Create the file
    print(f"🛠️ Creating __init__.py at: {init_file_path}")

    with open(init_file_path, "w", encoding="utf-8") as f:
        f.write("# Package initializer for minigame node\n")

    return {
        "status": "success",
        "message": "Created __init__.py",
        "path": init_file_path,
        "trace": {
            "event": "create_init_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
