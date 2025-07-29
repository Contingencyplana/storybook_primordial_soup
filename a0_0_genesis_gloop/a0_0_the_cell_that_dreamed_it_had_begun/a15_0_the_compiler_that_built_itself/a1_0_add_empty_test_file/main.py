# a1_0_add_empty_test_file/main.py

from pathlib import Path
from datetime import datetime, timezone

def add_empty_test_file(target_node_path):
    """
    Creates an empty test.py file in the given minigame node folder.
    Skips creation if the file already exists. Creates any missing parent folders.

    Args:
        target_node_path (str or Path): Path to the minigame node (can be nested).

    Returns:
        dict: Status dictionary with trace metadata.
    """
    PROJECT_ROOT = Path(__file__).resolve().parents[5]
    node_path = (PROJECT_ROOT / target_node_path).resolve()

    print(f"[INFO] Absolute target: {node_path}")

    node_path.mkdir(parents=True, exist_ok=True)
    test_file = node_path / "test.py"

    if test_file.exists():
        return {
            "status": "skipped",
            "message": "test.py already exists.",
            "path": str(test_file),
            "trace": {
                "event": "skip_existing_test",
                "timestamp": datetime.now(timezone.utc).isoformat()
            }
        }

    print(f"[INFO] Creating test.py at: {test_file}")

    test_file.write_text(
        "# Placeholder test file for minigame node\n"
        "def test_placeholder():\n"
        "    assert True  # Replace with actual tests\n",
        encoding="utf-8"
    )

    return {
        "status": "success",
        "message": "Created test.py",
        "path": str(test_file),
        "trace": {
            "event": "create_test_file",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("❌ Usage: python main.py <target_node_path>")
    else:
        result = add_empty_test_file(sys.argv[1])
        print(result)
