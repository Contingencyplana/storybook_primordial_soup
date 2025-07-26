# a0_3_add_empty_subtaskmap_file/test.py

import os
import sys
import shutil
import unittest
from pathlib import Path
from main import add_empty_subtaskmap_file

class TestAddEmptySubtaskmapFile(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parents[4]
        self.test_node = self.project_root / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node"
        self.subtaskmap_path = self.test_node / "subtaskmap.md"
        self.test_node.mkdir(parents=True, exist_ok=True)

    def test_create_subtaskmap(self):
        if self.subtaskmap_path.exists():
            self.subtaskmap_path.unlink()

        result = add_empty_subtaskmap_file(self.test_node)
        self.assertEqual(result["status"], "success")
        self.assertTrue(self.subtaskmap_path.exists())
        content = self.subtaskmap_path.read_text(encoding="utf-8")
        self.assertIn("<!-- Subtaskmap placeholder", content)
        self.assertEqual(result["trace"]["event"], "create_subtaskmap")

    def test_skip_existing_subtaskmap(self):
        self.subtaskmap_path.write_text("<!-- Preexisting content -->", encoding="utf-8")
        result = add_empty_subtaskmap_file(self.test_node)
        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_subtaskmap")

if __name__ == "__main__":
    TEST_FILE = Path(__file__).resolve().parents[4] / "a0_0_genesis_gloop" / "a0_0_the_cell_that_dreamed_it_had_begun" / "a99_0_test_create_minigame_node" / "a0_0_test_minigame_node" / "subtaskmap.md"

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if TEST_FILE.exists():
            TEST_FILE.unlink()
            print("🔄 Reset flag detected. subtaskmap.md file cleared before testing.")

    unittest.main(exit=False)

    while True:
        choice = input("\n📘 Test complete. Turn the page?\n[L] Leave test folder intact\n[R] Remove subtaskmap.md file\n→ ").strip().upper()
        if choice == "R":
            if TEST_FILE.exists():
                TEST_FILE.unlink()
                print("🗑️ subtaskmap.md file removed.")
            else:
                print("⚠️ subtaskmap.md file not found.")
            break
        elif choice == "L":
            print("📂 Test folder left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' to leave it intact or 'R' to remove it.")
