# a0_1_add_empty_init_file/main.py

import os
import datetime

def add_empty_init_file(minigame_node_path):
    """
    Creates an empty __init__.py file in the given minigame node folder.
    Skips creation if the file already exists.

    Args:
        minigame_node_path (str): The path to the target minigame node folder.

    Returns:
        dict: Structured response with status, path, and trace metadata.
    """
    init_file_path = os.path.join(minigame_node_path, "__init__.py")

    if os.path.exists(init_file_path):
        return {
            "status": "skipped",
            "message": "__init__.py already exists.",
            "path": init_file_path,
            "trace": {
                "event": "skip_existing_init",
                "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
            }
        }

    with open(init_file_path, "w", encoding="utf-8") as f:
        f.write("# Package initializer for minigame node\n")

    return {
        "status": "success",
        "message": "Created __init__.py",
        "path": init_file_path,
        "trace": {
            "event": "create_init_file",
            "timestamp": datetime.datetime.now(datetime.UTC).isoformat()
        }
    }

# Note: This function is designed to be imported or used by the compiler/test layer.
