# a0_0_add_empty_minigame_node/test.py

import os
import sys
import shutil
import unittest
from main import add_empty_minigame_node

class TestAddEmptyMinigameNode(unittest.TestCase):
    def setUp(self):
        # Live test directory (not temp)
        self.test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node"
        self.node_name = "a0_0_test_minigame_node"
        self.node_path = os.path.join(self.test_dir, self.node_name)

    def test_create_minigame_node(self):
        result = add_empty_minigame_node(self.test_dir, self.node_name)

        self.assertEqual(result["status"], "success")
        self.assertTrue(os.path.isdir(self.node_path))
        self.assertEqual(result["path"], self.node_path)
        self.assertIn("timestamp", result["trace"])
        self.assertEqual(result["trace"]["event"], "create_empty_minigame_node")

    def test_skip_existing_node(self):
        os.makedirs(self.node_path, exist_ok=True)
        result = add_empty_minigame_node(self.test_dir, self.node_name)

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_minigame_node")

if __name__ == "__main__":
    TEST_FOLDER = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node\a0_0_test_minigame_node"

    # Handle optional --reset argument
    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if os.path.exists(TEST_FOLDER):
            shutil.rmtree(TEST_FOLDER)
            print("🔄 Reset flag detected. Test folder cleared before testing.")

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
            print("\U0001f504 Reset flag detected. Test folder cleared before testing.")

