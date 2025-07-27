# a2_2_add_empty_milestones_file/test.py

from pathlib import Path
import sys
import unittest
from main import add_empty_milestones_file

class TestAddEmptyMilestonesFile(unittest.TestCase):
    def setUp(self):
        self.target_path = Path(
            r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
            r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_1_test_create_taskmaps\taskmaps"
        )
        self.milestones_file = self.target_path / "milestones.md"
        self.target_path.mkdir(parents=True, exist_ok=True)

    def test_create_milestones_file(self):
        if self.milestones_file.exists():
            self.milestones_file.unlink()

        result = add_empty_milestones_file(self.target_path)

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.milestones_file.is_file())
        self.assertEqual(result["trace"]["event"], "create_empty_milestones_file")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_milestones(self):
        self.milestones_file.write_text("Pre-existing content.")

        result = add_empty_milestones_file(self.target_path)

        self.assertEqual(result["status"], "skipped")
        self.assertEqual(result["trace"]["event"], "skip_existing_milestones_file")

if __name__ == "__main__":
    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if Path.exists(Path(__file__).parent):
            f = Path(__file__).parent / "taskmaps" / "milestones.md"
            if f.exists():
                f.unlink()
                print("🔄 Reset flag detected. milestones.md removed before testing.")

    unittest.main(exit=False)

    while True:
        choice = input(
            "\n📘 Test complete. Turn the page?\n[L] Leave milestones.md\n[R] Remove milestones.md\n→ "
        ).strip().upper()

        if choice == "R":
            if f.exists():
                f.unlink()
                print("🗑️ milestones.md removed.")
            else:
                print("⚠️ milestones.md not found.")
            break
        elif choice == "L":
            print("📂 milestones.md left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' or 'R'.")
