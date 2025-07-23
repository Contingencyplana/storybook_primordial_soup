# a1_0_add_empty_test_file/test.py

import os
import sys
import unittest
from main import add_empty_test_file

class TestAddEmptyTestFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file_path = os.path.join(self.test_dir, "test.py")

    def test_create_test_file(self):
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

        result = add_empty_test_file(self.test_dir)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isfile(self.test_file_path))
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_test_file")

    def test_skip_existing_test(self):
        with open(self.test_file_path, "w", encoding="utf-8") as f:
            f.write("# Preexisting test file")

        result = add_empty_test_file(self.test_dir)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_test")

if __name__ == "__main__":
    TEST_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
    TEST_FILE = os.path.join(TEST_FOLDER, "test.py")

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
            print("🔄 Reset flag detected. test.py file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test file intact\n[R] Remove test.py file\n→ ").strip().upper()
        if choice == "R":
            if os.path.exists(TEST_FILE):
                os.remove(TEST_FILE)
                print("🗑️ test.py file removed.")
            else:
                print("⚠️ test.py file not found.")
            break
        elif choice == "L":
            print("📂 Test file left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
