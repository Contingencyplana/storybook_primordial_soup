# a2_0_add_empty_taskmaps_folder/test.py

import os
import sys
import shutil
import unittest
from main import add_empty_taskmaps_folder

class TestAddEmptyTaskmapsFolder(unittest.TestCase):
    def setUp(self):
        # Path to the mock Layer 3 minigame folder (not a stanza folder)
        self.stanza_folder_path = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame"
        self.taskmaps_path = os.path.join(self.stanza_folder_path, "taskmaps")

        # Ensure minigame folder exists for test
        os.makedirs(self.stanza_folder_path, exist_ok=True)

    def test_create_taskmaps_folder(self):
        if os.path.exists(self.taskmaps_path):
            shutil.rmtree(self.taskmaps_path)

        result = add_empty_taskmaps_folder(self.stanza_folder_path)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isdir(self.taskmaps_path))
        self.assertEqual(result["path"], self.taskmaps_path)
        self.assertEqual(result["trace"]["event"], "create_empty_taskmaps_folder")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_taskmaps(self):
        os.makedirs(self.taskmaps_path, exist_ok=True)

        result = add_empty_taskmaps_folder(self.stanza_folder_path)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_taskmaps_folder")

if __name__ == "__main__":
    TASKMAPS_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame\taskmaps"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(TASKMAPS_FOLDER):
            shutil.rmtree(TASKMAPS_FOLDER)
            print("🔄 Reset flag detected. taskmaps/ folder cleared before testing.")

    unittest.main(exit=False)

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
