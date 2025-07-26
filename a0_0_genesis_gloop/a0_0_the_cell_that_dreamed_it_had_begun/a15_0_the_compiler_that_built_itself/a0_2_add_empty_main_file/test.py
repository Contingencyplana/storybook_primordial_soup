# a0_2_add_empty_main_file/test.py

"""
🧪 test.py – a0_2_add_empty_main_file

📘 Purpose:
Tests creation of a main.py file inside a minigame node folder.
Verifies both first-time creation and fallback safety.
"""

import os
import sys
import unittest
from pathlib import Path
from main import add_empty_main_file

class TestAddEmptyMainFile(unittest.TestCase):
    def setUp(self):
        self.test_node_path = Path(__file__).resolve().parents[4] / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"
        self.test_node_path.mkdir(parents=True, exist_ok=True)
        self.main_path = self.test_node_path / "main.py"

    def test_create_main_file(self):
        if self.main_path.exists():
            self.main_path.unlink()

        result = add_empty_main_file(self.test_node_path)

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.main_path.is_file())
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_main_file")

    def test_skip_existing_main(self):
        self.main_path.write_text("# Preexisting main")

        result = add_empty_main_file(self.test_node_path)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_main")

if __name__ == "__main__":
    TEST_FOLDER = Path(__file__).resolve().parents[4] / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"
    MAIN_FILE = TEST_FOLDER / "main.py"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if MAIN_FILE.exists():
            MAIN_FILE.unlink()
            print("🔄 Reset flag detected. main.py file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove main.py file\n→ ").strip().upper()
        if choice == "R":
            if MAIN_FILE.exists():
                MAIN_FILE.unlink()
                print("🗑️ main.py file removed.")
            else:
                print("⚠️ main.py file not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
