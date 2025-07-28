# a0_0_add_empty_minigame_node/main.py

"""
🧠 main.py – a0_0_add_empty_minigame_node

📘 Purpose:
Creates an empty minigame node folder, with support for nested subpaths.
It now fully resolves the path to ensure it writes to the correct target.

✅ Fixes:
- Uses .resolve() for absolute targeting
- Emits real-time print debug output for validation
"""

from pathlib import Path
from datetime import datetime, timezone

def add_empty_minigame_node(target_node_path):
    """
    Creates an empty minigame node folder at the specified relative or absolute path.

    Args:
        target_node_path (str or Path): Nested path to the new node folder.

    Returns:
        dict: Status and trace metadata.
    """
    path = Path(target_node_path).resolve()

    print(f"📂 Targeting absolute path: {path}")

    # Create intermediate folders if needed
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        status = "success"
        message = f"Created minigame node: {path.name}"
        event = "create_empty_minigame_node"
    else:
        status = "skipped"
        message = f"Minigame node already exists: {path}"
        event = "skip_existing_minigame_node"

    return {
        "status": status,
        "message": message,
        "path": str(path),
        "trace": {
            "event": event,
            "minigame": path.name,
            "path": str(path),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

# No __main__ block – this module is imported by orchestrators.
