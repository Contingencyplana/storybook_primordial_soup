# a0_1_add_empty_init_file/main.py

"""
🧠 main.py – a0_1_add_empty_init_file

📘 Purpose:
Adds an empty __init__.py file to the specified minigame node folder.
Supports nested path input and verifies folder existence before creation.

This ensures all nodes are importable as Python packages.
"""

from pathlib import Path
from datetime import datetime, timezone

def add_empty_init_file(target_node_path):
    """
    Adds an empty __init__.py file to a minigame node folder.

    Args:
        target_node_path (str or Path): Path to the minigame node (can be nested).

    Returns:
        dict: Structured trace metadata with status and path.
    """
    path = Path(target_node_path)
    init_path = path / "__init__.py"

    if not path.exists():
        return {
            "status": "error",
            "message": "Target folder does not exist.",
            "path": str(path),
            "trace": {
                "event": "missing_minigame_node_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    if init_path.exists():
        return {
            "status": "skipped",
            "message": "__init__.py already exists.",
            "path": str(init_path),
            "trace": {
                "event": "skip_existing_init",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"🛠️ Creating __init__.py at: {init_path}")
    init_path.write_text("# Package initializer for minigame node\n", encoding="utf-8")

    return {
        "status": "success",
        "message": "Created __init__.py",
        "path": str(init_path),
        "trace": {
            "event": "create_init_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
