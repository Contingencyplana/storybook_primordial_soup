# a0_3_add_empty_subtaskmap_file/test.py

import os
import sys
import unittest
from main import add_empty_subtaskmap_file

class TestAddEmptySubtaskmapFile(unittest.TestCase):
    def setUp(self):
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"
        os.makedirs(self.test_dir, exist_ok=True)
        self.subtaskmap_path = os.path.join(self.test_dir, "subtaskmap.md")

    def test_create_subtaskmap(self):
        if os.path.exists(self.subtaskmap_path):
            os.remove(self.subtaskmap_path)

        result = add_empty_subtaskmap_file(self.test_dir)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isfile(self.subtaskmap_path))
        with open(self.subtaskmap_path, "r", encoding="utf-8") as f:
            self.assertIn("<!-- Subtaskmap placeholder", f.read())
        self.assertEqual(result["trace"]["event"], "create_subtaskmap")

    def test_skip_existing_subtaskmap(self):
        with open(self.subtaskmap_path, "w", encoding="utf-8") as f:
            f.write("<!-- Preexisting content -->")

        result = add_empty_subtaskmap_file(self.test_dir)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_subtaskmap")

if __name__ == "__main__":
    TEST_FILE = os.path.join(
        r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node",
        "subtaskmap.md"
    )

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
            print("🔄 Reset flag detected. subtaskmap.md file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove subtaskmap.md file\n→ ").strip().upper()
        if choice == "R":
            if os.path.exists(TEST_FILE):
                os.remove(TEST_FILE)
                print("🗑️ subtaskmap.md file removed.")
            else:
                print("⚠️ subtaskmap.md file not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
