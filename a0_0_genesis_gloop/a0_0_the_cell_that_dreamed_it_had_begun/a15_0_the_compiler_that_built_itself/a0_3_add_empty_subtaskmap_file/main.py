# a0_3_add_empty_subtaskmap_file/main.py

import os
from datetime import datetime, timezone

def add_empty_subtaskmap_file(minigame_node_path):
    """
    Creates an empty subtaskmap.md file in the given minigame node folder.
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

    subtaskmap_path = os.path.join(minigame_node_path, "subtaskmap.md")

    if os.path.exists(subtaskmap_path):
        return {
            "status": "skipped",
            "message": "subtaskmap.md already exists.",
            "path": subtaskmap_path,
            "trace": {
                "event": "skip_existing_subtaskmap",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"🛠️ Creating subtaskmap.md at: {subtaskmap_path}")

    with open(subtaskmap_path, "w", encoding="utf-8") as f:
        f.write("<!-- Subtaskmap placeholder for recursive node documentation -->\n")

    return {
        "status": "success",
        "message": "Created subtaskmap.md",
        "path": subtaskmap_path,
        "trace": {
            "event": "create_subtaskmap",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
