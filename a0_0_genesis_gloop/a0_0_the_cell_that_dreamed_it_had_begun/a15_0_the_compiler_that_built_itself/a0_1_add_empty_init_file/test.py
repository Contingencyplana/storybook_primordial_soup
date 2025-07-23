# a0_1_add_empty_init_file/test.py

import os
import sys
import shutil
import unittest
from main import add_empty_init_file

class TestAddEmptyInitFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
        os.makedirs(self.test_dir, exist_ok=True)
        self.init_path = os.path.join(self.test_dir, "__init__.py")

    def tearDown(self):
        if os.path.exists(self.init_path):
            os.remove(self.init_path)

    def test_create_init_file(self):
        if os.path.exists(self.init_path):
            os.remove(self.init_path)

        result = add_empty_init_file(self.test_dir)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isfile(self.init_path))
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_init_file")

    def test_skip_existing_init(self):
        with open(self.init_path, "w", encoding="utf-8") as f:
            f.write("# Preexisting init")

        result = add_empty_init_file(self.test_dir)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_init")

if __name__ == "__main__":
    TEST_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
    INIT_FILE = os.path.join(TEST_FOLDER, "__init__.py")

    # Handle optional --reset argument
    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(INIT_FILE):
            os.remove(INIT_FILE)
            print("🔄 Reset flag detected. __init__.py file cleared before testing.")

    unittest.main(exit=False)

    # 🌀 Recursive Prompt (L = Leave intact, R = Remove test folder)
    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove test folder\n→ ").strip().upper()
        if choice == "R":
            if os.path.exists(TEST_FOLDER):
                shutil.rmtree(TEST_FOLDER)
                print("🗑️ Test folder removed.")
            else:
                print("⚠️ Test folder not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
