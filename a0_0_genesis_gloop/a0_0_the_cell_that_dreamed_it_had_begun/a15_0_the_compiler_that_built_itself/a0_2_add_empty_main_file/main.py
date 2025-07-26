# a0_2_add_empty_main_file/main.py

"""
🧠 main.py – a0_2_add_empty_main_file

📘 Purpose:
Adds an empty main.py file to a minigame node folder.

Supports nested paths. Intermediate folders must already exist.
"""

from pathlib import Path
from datetime import datetime, timezone

def add_empty_main_file(minigame_node_path):
    """
    Creates an empty main.py file in the specified minigame node folder.

    Args:
        minigame_node_path (str or Path): Path to the minigame node folder.

    Returns:
        dict: Structured response with status, message, path, and trace metadata.
    """
    path = Path(minigame_node_path)
    main_file_path = path / "main.py"

    if not path.exists():
        return {
            "status": "error",
            "message": f"Minigame node folder does not exist: {path}",
            "path": str(path),
            "trace": {
                "event": "missing_minigame_node_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    if main_file_path.exists():
        return {
            "status": "skipped",
            "message": f"main.py already exists: {main_file_path}",
            "path": str(main_file_path),
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
        "path": str(main_file_path),
        "trace": {
            "event": "create_main_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
