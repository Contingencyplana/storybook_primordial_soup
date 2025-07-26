# a0_3_add_empty_subtaskmap_file/main.py

from pathlib import Path
from datetime import datetime, timezone

def add_empty_subtaskmap_file(minigame_node_path):
    """
    Creates an empty subtaskmap.md file in the given minigame node folder.
    Skips creation if the file already exists. Returns an error if the folder does not exist.

    Args:
        minigame_node_path (str or Path): The path to the target minigame node folder.

    Returns:
        dict: Structured response with status, path, and trace metadata.
    """
    path = Path(minigame_node_path)
    subtaskmap_path = path / "subtaskmap.md"

    if not path.exists():
        return {
            "status": "error",
            "message": "Target minigame node folder does not exist.",
            "path": str(path),
            "trace": {
                "event": "missing_minigame_node_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    if subtaskmap_path.exists():
        return {
            "status": "skipped",
            "message": "subtaskmap.md already exists.",
            "path": str(subtaskmap_path),
            "trace": {
                "event": "skip_existing_subtaskmap",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"🛠️ Creating subtaskmap.md at: {subtaskmap_path}")

    subtaskmap_path.write_text("<!-- Subtaskmap placeholder for recursive node documentation -->\n", encoding="utf-8")

    return {
        "status": "success",
        "message": "Created subtaskmap.md",
        "path": str(subtaskmap_path),
        "trace": {
            "event": "create_subtaskmap",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
