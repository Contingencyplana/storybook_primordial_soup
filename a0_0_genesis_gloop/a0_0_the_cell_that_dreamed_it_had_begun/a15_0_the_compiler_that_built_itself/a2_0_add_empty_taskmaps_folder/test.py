# a2_0_add_empty_taskmaps_folder/test.py

from pathlib import Path
import sys
import shutil
import unittest
from main import add_empty_taskmaps_folder

class TestAddEmptyTaskmapsFolder(unittest.TestCase):
    def setUp(self):
        # Path to mock Layer 3 minigame folder (renamed for clarity)
        self.minigame_path = Path(
            r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
            r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_1_test_create_taskmaps"
        )
        self.taskmaps_path = self.minigame_path / "taskmaps"
        self.minigame_path.mkdir(parents=True, exist_ok=True)

    def test_create_taskmaps_folder(self):
        if self.taskmaps_path.exists():
            shutil.rmtree(self.taskmaps_path)

        result = add_empty_taskmaps_folder(str(self.minigame_path))

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.taskmaps_path.is_dir())
        self.assertEqual(result["path"], str(self.taskmaps_path))
        self.assertEqual(result["trace"]["event"], "create_empty_taskmaps_folder")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_taskmaps(self):
        self.taskmaps_path.mkdir(parents=True, exist_ok=True)

        result = add_empty_taskmaps_folder(str(self.minigame_path))

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_taskmaps_folder")

if __name__ == "__main__":
    TASKMAPS_FOLDER = Path(
        r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
        r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_1_test_create_taskmaps\taskmaps"
    )

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if TASKMAPS_FOLDER.exists():
            shutil.rmtree(TASKMAPS_FOLDER)
            print("🔄 Reset flag detected. taskmaps/ folder cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input(
            "\n📘 Test complete. Turn the page?\n[L] Leave folder intact\n[R] Remove taskmaps/ folder\n→ "
        ).strip().upper()

        if choice == "R":
            if TASKMAPS_FOLDER.exists():
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
