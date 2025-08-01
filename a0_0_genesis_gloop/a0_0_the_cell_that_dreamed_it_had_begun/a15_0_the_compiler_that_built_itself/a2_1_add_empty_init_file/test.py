# a2_1_add_empty_init_file/test.py

from pathlib import Path
import sys
import shutil
import unittest
from main import add_empty_init_file

class TestAddEmptyInitFile(unittest.TestCase):
    def setUp(self):
        self.target_path = Path(
            r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
            r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_1_test_create_taskmaps\taskmaps"
        )
        self.init_file = self.target_path / "__init__.py"
        self.target_path.mkdir(parents=True, exist_ok=True)

    def test_create_init_file(self):
        if self.init_file.exists():
            self.init_file.unlink()

        result = add_empty_init_file(str(self.target_path))

        self.assertEqual(result["status"], "success")
        self.assertTrue(self.init_file.is_file())
        self.assertIn("__init__.py", result["path"])
        self.assertEqual(result["trace"]["event"], "create_empty_init_file")
        self.assertIn("timestamp", result["trace"])

    def test_skip_existing_init(self):
        self.init_file.write_text("# Pre-existing init")

        result = add_empty_init_file(str(self.target_path))

        self.assertEqual(result["status"], "skipped")
        self.assertIn("already exists", result["message"])
        self.assertEqual(result["trace"]["event"], "skip_existing_init_file")

if __name__ == "__main__":
    TARGET_FOLDER = Path(
        r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop"
        r"\a0_0_the_cell_that_dreamed_it_had_begun\a99_1_test_create_taskmaps\taskmaps"
    )

    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        if TARGET_FOLDER.exists():
            init_file = TARGET_FOLDER / "__init__.py"
            if init_file.exists():
                init_file.unlink()
                print("🔄 Reset flag detected. __init__.py removed before testing.")

    unittest.main(exit=False)

    while True:
        choice = input(
            "\n📘 Test complete. Turn the page?\n[L] Leave __init__.py\n[R] Remove __init__.py\n→ "
        ).strip().upper()

        if choice == "R":
            if init_file.exists():
                init_file.unlink()
                print("🗑️ __init__.py removed.")
            else:
                print("⚠️ __init__.py not found.")
            break
        elif choice == "L":
            print("📂 __init__.py left intact for review.")
            break
        else:
            print("🌀 Invalid choice. Please enter 'L' or 'R'.")
