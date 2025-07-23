# a0_2_add_empty_main_file/test.py

import os
import sys
import unittest
from main import add_empty_main_file

class TestAddEmptyMainFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
        os.makedirs(self.test_dir, exist_ok=True)
        self.main_path = os.path.join(self.test_dir, "main.py")

    def test_create_main_file(self):
        if os.path.exists(self.main_path):
            os.remove(self.main_path)

        result = add_empty_main_file(self.test_dir)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isfile(self.main_path))
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_main_file")

    def test_skip_existing_main(self):
        with open(self.main_path, "w", encoding="utf-8") as f:
            f.write("# Preexisting main")

        result = add_empty_main_file(self.test_dir)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_main")

if __name__ == "__main__":
    TEST_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
    MAIN_FILE = os.path.join(TEST_FOLDER, "main.py")

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(MAIN_FILE):
            os.remove(MAIN_FILE)
            print("🔄 Reset flag detected. main.py file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove main.py file\n→ ").strip().upper()
        if choice == "R":
            if os.path.exists(MAIN_FILE):
                os.remove(MAIN_FILE)
                print("🗑️ main.py file removed.")
            else:
                print("⚠️ main.py file not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
