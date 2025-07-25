# a0_0_add_empty_minigame_node/test.py

"""
🧪 test.py – a0_0_add_empty_minigame_node

📘 Purpose:
Tests creation of a minigame node folder, including nested path handling.
Also verifies that re-running the function skips existing nodes cleanly.
"""

import os
import sys
import shutil
import unittest
from pathlib import Path
from main import add_empty_minigame_node

class TestAddEmptyMinigameNode(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parents[4]
        self.test_node_path = self.project_root / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"

    def test_create_minigame_node(self):
        result = add_empty_minigame_node(self.test_node_path)
        self.assertEqual(result["status"], "success")
        self.assertTrue(self.test_node_path.exists())
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_empty_minigame_node")

    def test_skip_existing_node(self):
        self.test_node_path.mkdir(parents=True, exist_ok=True)
        result = add_empty_minigame_node(self.test_node_path)
        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_minigame_node")

if __name__ == "__main__":
    TEST_FOLDER = Path(__file__).resolve().parents[4] / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if TEST_FOLDER.exists():
            shutil.rmtree(TEST_FOLDER)
            print("🔄 Reset flag detected. Test folder cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove test folder\n→ ").strip().upper()
        if choice == "R":
            if TEST_FOLDER.exists():
                shutil.rmtree(TEST_FOLDER)
                print("🗑️ Test folder removed.")
            else:
                print("⚠️ Test folder not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' or 'R'.")
