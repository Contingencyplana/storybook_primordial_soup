# a2_2_add_empty_milestones_file/main.py

from pathlib import Path
from datetime import datetime, timezone

def add_empty_milestones_file(target_folder_path):
    """
    Creates a milestones.md file inside the specified taskmaps folder, if it doesn't already exist.

    Args:
        target_folder_path (str or Path): Full path to taskmaps/ directory.

    Returns:
        dict: Result of operation including status, path, and trace metadata.
    """
    folder_path = Path(target_folder_path)
    folder_path.mkdir(parents=True, exist_ok=True)

    milestones_file = folder_path / "milestones.md"

    if milestones_file.exists():
        return {
            "status": "skipped",
            "message": f"milestones.md already exists in: {folder_path}",
            "path": str(milestones_file),
            "trace": {
                "event": "skip_existing_milestones_file",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    milestones_file.write_text("# 🧱 Milestone Log\n\nThis file tracks progression of minigame logic.\n")

    return {
        "status": "success",
        "message": f"Created milestones.md in: {folder_path}",
        "path": str(milestones_file),
        "trace": {
            "event": "create_empty_milestones_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
