import os
from pathlib import Path

# Test configuration
target_node = "a99_0_test_minigame_node"
project_root = Path(__file__).resolve().parents[3]
minigame_path = project_root / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / target_node

expected_files = [
    "__init__.py",
    "main.py",
    "test.py",
    "subtaskmap.md"
]

def test_minigame_node_scaffold():
    print(f"🔍 Verifying folder structure: {minigame_path}")
    if not minigame_path.exists():
        print("❌ Node folder was not created.")
        return

    missing = []
    for filename in expected_files:
        if not (minigame_path / filename).exists():
            missing.append(filename)

    if missing:
        print("❌ Missing expected files:")
        for m in missing:
            print(f"   - {m}")
    else:
        print("✅ All expected files are present.")

if __name__ == "__main__":
    test_minigame_node_scaffold()
