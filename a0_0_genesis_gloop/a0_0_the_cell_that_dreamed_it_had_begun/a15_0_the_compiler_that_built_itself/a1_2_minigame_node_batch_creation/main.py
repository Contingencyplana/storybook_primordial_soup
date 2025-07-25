"""
🧠 main.py – a1_2_minigame_node_batch_creation

📘 Purpose:
This script acts as the Node Constructor Hand, dynamically invoking six recursive builder nodes ("fingers")
to create a fully scaffolded Layer 4 minigame node folder.

It now accepts nested subfolder paths (e.g., a99_0_test_create_minigame_node/a0_0_test_minigame_node),
validates only the final node name, and creates intermediate folders as needed.
"""

import sys
import re
import subprocess
from pathlib import Path

# Constants
FOLDER_PATTERN = re.compile(r"^a\d+_\d+_[a-z0-9_]+$")  # Only validate final folder name
STANZA_FOLDER = Path(__file__).resolve().parents[2]  # Corrected: one level up from a15_0

FINGER_NODES = [
    "a0_0_add_empty_minigame_node",
    "a0_1_add_empty_init_file",
    "a0_2_add_empty_main_file",
    "a0_3_add_empty_subtaskmap_file",
    "a1_0_add_empty_test_file",
    "a1_1_link_nodal_meta_recursion_controls",
]

def validate_name(full_path_str):
    """Only validate the final folder name in a possibly nested path."""
    final_part = Path(full_path_str).name
    return bool(FOLDER_PATTERN.match(final_part))

def target_exists(path):
    return path.exists()

def run_finger_script(script_name, target_node):
    script_path = (
        STANZA_FOLDER
        / "a15_0_the_compiler_that_built_itself"
        / script_name
        / "main.py"
    )
    if not script_path.exists():
        print(f"❌ Missing script: {script_path}")
        return False
    print(f"▶ Running: {script_name} → {target_node}")
    result = subprocess.run(
        [sys.executable, str(script_path), target_node],
        capture_output=True,
        text=True
    )
    print(result.stdout.strip())
    if result.returncode != 0:
        print(result.stderr.strip())
        print(f"❌ Failed at step: {script_name}")
        return False
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <target_node_name_or_path>")
        sys.exit(1)

    target_name = sys.argv[1]
    target_path = STANZA_FOLDER / Path(target_name)

    if not validate_name(target_name):
        print("❌ Invalid folder name. Must match: a<digit+>_<digit+>_<snake_case>")
        sys.exit(1)

    if target_exists(target_path):
        print(f"⚠️ Folder already exists: {target_path}")
        sys.exit(1)

    # Create intermediate folders if necessary
    target_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"🧠 Starting node construction for: {target_name}\n")

    for script in FINGER_NODES:
        if not run_finger_script(script, target_name):
            print("❌ Aborting batch creation due to failure.")
            sys.exit(1)

    print(f"\n✅ Batch creation complete: {target_name}")

if __name__ == "__main__":
    main()
