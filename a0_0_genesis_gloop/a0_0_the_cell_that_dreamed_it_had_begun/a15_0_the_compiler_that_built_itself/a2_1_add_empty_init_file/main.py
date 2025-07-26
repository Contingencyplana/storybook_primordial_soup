# a2_1_add_empty_init_file/main.py

from pathlib import Path
from datetime import datetime, timezone

def add_empty_init_file(target_node_path):
    """
    Creates an empty __init__.py file inside a minigame node folder.

    Args:
        target_node_path (str or Path): Full path to the Layer 4 minigame node folder.

    Returns:
        dict: Result of operation including status, path, and trace metadata.
    """
    node_path = Path(target_node_path)
    node_path.mkdir(parents=True, exist_ok=True)  # Ensure folder exists

    init_file = node_path / "__init__.py"

    if init_file.exists():
        return {
            "status": "skipped",
            "message": f"__init__.py already exists in: {node_path}",
            "path": str(init_file),
            "trace": {
                "event": "skip_existing_init_file",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    init_file.write_text("# This makes the folder a Python package.\n")

    return {
        "status": "success",
        "message": f"Created __init__.py in: {node_path}",
        "path": str(init_file),
        "trace": {
            "event": "create_empty_init_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
