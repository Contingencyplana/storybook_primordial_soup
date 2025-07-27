# a2_1_add_empty_init_file/main.py

from pathlib import Path
from datetime import datetime, timezone

def add_empty_init_file(target_folder_path):
    """
    Creates an empty __init__.py file inside the specified folder.

    Args:
        target_folder_path (str or Path): Full path to a folder (e.g., taskmaps/).

    Returns:
        dict: Result of operation including status, path, and trace metadata.
    """
    folder_path = Path(target_folder_path)
    folder_path.mkdir(parents=True, exist_ok=True)

    init_file = folder_path / "__init__.py"

    if init_file.exists():
        return {
            "status": "skipped",
            "message": f"__init__.py already exists in: {folder_path}",
            "path": str(init_file),
            "trace": {
                "event": "skip_existing_init_file",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    init_file.write_text("# Makes this folder a Python package.\n")

    return {
        "status": "success",
        "message": f"Created __init__.py in: {folder_path}",
        "path": str(init_file),
        "trace": {
            "event": "create_empty_init_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }
