"""
🧪 test.py – a1_2_minigame_node_batch_creation

📘 Purpose:
This test verifies the correct output of main.py by checking the expected folder and file structure of
a generated minigame node inside a test minigame (default: a99_0_test_create_minigame_node/a0_0_test_minigame_node).

It ensures the following files were created:
- __init__.py
- main.py
- test.py
- subtaskmap.md

This test serves as the validation harness for a1_2_minigame_node_batch_creation and ensures scaffolding
logic remains reliable during recursive system evolution.
"""

from pathlib import Path

# Configuration
target_path_str = "a99_0_test_create_minigame_node/a0_0_test_minigame_node"
project_root = Path(__file__).resolve().parents[4]
minigame_path = project_root / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / Path(target_path_str)

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
