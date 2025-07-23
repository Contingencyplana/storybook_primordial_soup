# a1_0_add_empty_test_file/main.py

import os
from datetime import datetime, timezone

def add_empty_test_file(minigame_node_path):
    """
    Creates an empty test.py file in the given minigame node folder.
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

    test_file_path = os.path.join(minigame_node_path, "test.py")

    if os.path.exists(test_file_path):
        return {
            "status": "skipped",
            "message": "test.py already exists.",
            "path": test_file_path,
            "trace": {
                "event": "skip_existing_test",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"🛠️ Creating test.py at: {test_file_path}")

    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("# Placeholder test file for minigame node\n")
        f.write("def test_placeholder():\n")
        f.write("    assert True  # Replace with actual tests\n")

    return {
        "status": "success",
        "message": "Created test.py",
        "path": test_file_path,
        "trace": {
            "event": "create_test_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
