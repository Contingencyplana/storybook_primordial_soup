# a1_0_add_empty_test_file/test.py

import unittest
from pathlib import Path
import os
import sys

from main import add_empty_test_file

class TestAddEmptyTestFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = Path(
            r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
            r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node"
            r"\a0_0_test_minigame_node"
        )
        self.test_file = self.test_dir / "test.py"
        self.test_dir.mkdir(parents=True, exist_ok=True)

    def test_create_test_file(self):
        if self.test_file.exists():
            self.test_file.unlink()

        result = add_empty_test_file(self.test_dir)

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.test_file.is_file())
        self.assertEqual(result["trace"]["event"], "create_test_file")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_test(self):
        self.test_file.write_text("# Preexisting test file", encoding="utf-8")

        result = add_empty_test_file(self.test_dir)

        self.assertEqual(result["status"], "skipped")
        self.assertEqual(result["trace"]["event"], "skip_existing_test")
        self.assertIn("already exists", result["message"])

if __name__ == "__main__":
    TEST_FOLDER = Path(
        r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
        r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node"
        r"\a0_0_test_minigame_node"
    )
    TEST_FILE = TEST_FOLDER / "test.py"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if TEST_FILE.exists():
            TEST_FILE.unlink()
            print("🔄 Reset flag detected. test.py file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test file intact\n[R] Remove test.py file\n→ ").strip().upper()
        if choice == "R":
            if TEST_FILE.exists():
                TEST_FILE.unlink()
                print("🗑️ test.py file removed.")
            else:
                print("⚠️ test.py file not found.")
            break
        elif choice == "L":
            print("📂 Test file left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
