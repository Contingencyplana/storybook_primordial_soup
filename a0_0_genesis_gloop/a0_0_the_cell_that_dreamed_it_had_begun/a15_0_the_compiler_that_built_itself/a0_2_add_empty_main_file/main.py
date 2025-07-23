# a0_2_add_empty_main_file/main.py

import os
from datetime import datetime, timezone

def add_empty_main_file(minigame_node_path):
    """
    Creates an empty main.py file in the given minigame node folder.
    Skips creation if the file already exists. Returns an error if the folder does not exist.

    Args:
        minigame_node_path (str): The path to the target minigame node folder.

    Returns:
        dict: Structured response with status, path, and trace metadata.
    """
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

    main_file_path = os.path.join(minigame_node_path, "main.py")

    if os.path.exists(main_file_path):
        return {
            "status": "skipped",
            "message": "main.py already exists.",
            "path": main_file_path,
            "trace": {
                "event": "skip_existing_main",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"🛠️ Creating main.py at: {main_file_path}")

    with open(main_file_path, "w", encoding="utf-8") as f:
        f.write("# Main execution file for minigame node\n")

    return {
        "status": "success",
        "message": "Created main.py",
        "path": main_file_path,
        "trace": {
            "event": "create_main_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
