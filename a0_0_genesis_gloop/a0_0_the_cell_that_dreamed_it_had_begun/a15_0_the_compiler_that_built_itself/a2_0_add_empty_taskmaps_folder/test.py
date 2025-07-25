# a2_0_add_empty_taskmaps_folder/test.py

import os
import sys
import shutil
import unittest
from main import add_empty_taskmaps_folder

class TestAddEmptyTaskmapsFolder(unittest.TestCase):
    def setUp(self):
        # Paths for the mock minigame node and taskmaps folder
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node"
        self.node_name = "a0_0_test_minigame_node"
        self.node_path = os.path.join(self.test_dir, self.node_name)
        self.taskmaps_path = os.path.join(self.node_path, "taskmaps")

        # Ensure the minigame node folder exists
        os.makedirs(self.node_path, exist_ok=True)

    def test_create_taskmaps_folder(self):
        if os.path.exists(self.taskmaps_path):
            shutil.rmtree(self.taskmaps_path)

        result = add_empty_taskmaps_folder(self.node_path)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isdir(self.taskmaps_path))
        self.assertEqual(result["path"], self.taskmaps_path)
        self.assertEqual(result["trace"]["event"], "create_empty_taskmaps_folder")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_taskmaps(self):
        os.makedirs(self.taskmaps_path, exist_ok=True)

        result = add_empty_taskmaps_folder(self.node_path)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_taskmaps_folder")

if __name__ == "__main__":
    TASKMAPS_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node\taskmaps"

    # Handle optional --reset argument
    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(TASKMAPS_FOLDER):
            shutil.rmtree(TASKMAPS_FOLDER)
            print("🔄 Reset flag detected. taskmaps/ folder cleared before testing.")

    unittest.main(exit=False)

    # 🌀 Recursive Prompt (L = Leave intact, R = Remove test folder)
    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave folder intact\n[R] Remove taskmaps/ folder\n→ ").strip().upper()
        if choice == "R":
            if os.path.exists(TASKMAPS_FOLDER):
                shutil.rmtree(TASKMAPS_FOLDER)
                print("🗑️ taskmaps/ folder removed.")
            else:
                print("⚠️ taskmaps/ folder not found.")
            break
        elif choice == "L":
            print("📂 taskmaps/ folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
