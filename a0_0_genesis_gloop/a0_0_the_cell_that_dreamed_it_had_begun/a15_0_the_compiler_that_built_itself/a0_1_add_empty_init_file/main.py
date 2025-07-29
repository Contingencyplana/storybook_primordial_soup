# a0_1_add_empty_init_file/main.py

"""
🧠 main.py – a0_1_add_empty_init_file

📘 Purpose:
Adds an empty __init__.py file to the specified minigame node folder.
Supports nested or absolute path input and verifies folder existence before creation.

This ensures all nodes are importable as Python packages.
"""

from pathlib import Path
from datetime import datetime, timezone

def add_empty_init_file(target_node_path):
    """
    Adds an empty __init__.py file to a minigame node folder.

    Args:
        target_node_path (str or Path): Path to the minigame node (can be nested or absolute).

    Returns:
        dict: Structured trace metadata with status and path.
    """
    PROJECT_ROOT = Path(__file__).resolve().parents[5]  # Adjust this level if needed
    path = (PROJECT_ROOT / target_node_path).resolve()
    init_path = path / "__init__.py"

    if not path.exists():
        return {
            "status": "error",
            "message": f"Target folder does not exist: {path}",
            "path": str(path),
            "trace": {
                "event": "missing_minigame_node_folder",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    if init_path.exists():
        return {
            "status": "skipped",
            "message": f"__init__.py already exists at: {init_path}",
            "path": str(init_path),
            "trace": {
                "event": "skip_existing_init",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"[INFO] Creating __init__.py at: {init_path}")
    init_path.write_text("# Package initializer for minigame node\n", encoding="utf-8")

    return {
        "status": "success",
        "message": f"Created __init__.py at: {init_path}",
        "path": str(init_path),
        "trace": {
            "event": "create_init_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("❌ Usage: python main.py <target_node_path>")
    else:
        result = add_empty_init_file(sys.argv[1])
        print(result)
