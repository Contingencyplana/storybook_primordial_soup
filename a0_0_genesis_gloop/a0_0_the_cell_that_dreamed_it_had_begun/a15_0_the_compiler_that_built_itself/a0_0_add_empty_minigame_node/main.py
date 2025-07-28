# a0_0_add_empty_minigame_node/main.py

"""
🧠 main.py – a0_0_add_empty_minigame_node

📘 Purpose:
Creates an empty minigame node folder, with support for nested subpaths.

It ensures the target folder does not already exist, creates any required intermediate folders,
and returns a traceable result for use in higher-order automation.

Input can be a deeply nested or absolute path like:
  a99_0_test_create_minigame_node/a0_0_test_minigame_node
"""

from pathlib import Path
from datetime import datetime, timezone

def add_empty_minigame_node(target_node_path):
    """
    Creates an empty minigame node folder at the specified path.

    Args:
        target_node_path (str or Path): Nested or absolute path to the new node folder.

    Returns:
        dict: Status and trace metadata.
    """
    path = Path(target_node_path).resolve()  # ✅ Resolve the full path

    # Create intermediate folders if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    # Abort if node already exists
    if path.exists():
        return {
            "status": "skipped",
            "message": f"Minigame node already exists: {path}",
            "path": str(path),
            "trace": {
                "event": "skip_existing_minigame_node",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    # Create node folder
    path.mkdir()

    return {
        "status": "success",
        "message": f"Created minigame node: {path.name}",
        "path": str(path),
        "trace": {
            "event": "create_empty_minigame_node",
            "minigame": path.name,
            "path": str(path),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

# No __main__ block – this module is imported by orchestrators.
