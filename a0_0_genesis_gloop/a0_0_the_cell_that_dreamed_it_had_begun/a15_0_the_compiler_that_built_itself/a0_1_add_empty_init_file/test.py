# a0_1_add_empty_init_file/test.py

"""
🧪 test.py – a0_1_add_empty_init_file

📘 Purpose:
Tests the behavior of __init__.py creation in nested minigame node folders.
Handles creation, skipping, and reset logic.
"""

import sys
import shutil
import unittest
from pathlib import Path
from main import add_empty_init_file

class TestAddEmptyInitFile(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parents[4]
        self.test_node_path = self.project_root / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"
        self.init_file = self.test_node_path / "__init__.py"
        self.test_node_path.mkdir(parents=True, exist_ok=True)

    def test_create_init_file(self):
        if self.init_file.exists():
            self.init_file.unlink()

        result = add_empty_init_file(self.test_node_path)

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.init_file.exists())
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_init_file")

    def test_skip_existing_init(self):
        self.init_file.write_text("# Preexisting init", encoding="utf-8")

        result = add_empty_init_file(self.test_node_path)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_init")

if __name__ == "__main__":
    TEST_FOLDER = Path(__file__).resolve().parents[4] / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"
    INIT_FILE = TEST_FOLDER / "__init__.py"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if INIT_FILE.exists():
            INIT_FILE.unlink()
            print("🔄 Reset flag detected. __init__.py file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove __init__.py file\n→ ").strip().upper()
        if choice == "R":
            if INIT_FILE.exists():
                INIT_FILE.unlink()
                print("🗑️ __init__.py file removed.")
            else:
                print("⚠️ __init__.py file not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' or 'R'.")
