# a1_1_link_nodal_meta_recursion_controls/test.py

import os
import sys
import unittest
from main import link_meta_recursion_controls

class TestLinkMetaRecursionControls(unittest.TestCase):
    def setUp(self):
        self.control_file = r"C:\Users\Admin\storybook_primordial_soup\meta_recursion_controls.md"
        if os.path.exists(self.control_file):
            os.remove(self.control_file)

        self.sample_entries = [
            {"name": "a0_0_add_empty_minigame_node", "description": "Creates empty minigame node folder"},
            {"name": "a0_1_add_empty_init_file", "description": "Adds __init__.py to minigame node"},
            {"name": "a0_2_add_empty_main_file", "description": "Adds main.py with header"},
            {"name": "a0_3_add_empty_subtaskmap_file", "description": "Adds subtaskmap.md with placeholder"},
            {"name": "a1_0_add_empty_test_file", "description": "Adds test.py with placeholder test"}
        ]

    def test_link_and_skip(self):
        result1 = link_meta_recursion_controls(self.sample_entries, self.control_file)
        self.assertEqual(result1["added"], 5)
        self.assertEqual(result1["skipped"], 0)

        result2 = link_meta_recursion_controls(self.sample_entries, self.control_file)
        self.assertEqual(result2["added"], 0)
        self.assertEqual(result2["skipped"], 5)

        self.assertTrue(os.path.exists(self.control_file))
        with open(self.control_file, "r", encoding="utf-8") as f:
            content = f.read()
        for entry in self.sample_entries:
            self.assertIn(entry["name"], content)

if __name__ == "__main__":
    if "--reset" in sys.argv:
        sys.argv.remove("--reset")
        reset_target = r"C:\Users\Admin\storybook_primordial_soup\meta_recursion_controls.md"
        if os.path.exists(reset_target):
            os.remove(reset_target)
            print("🔄 Reset: meta_recursion_controls.md cleared.")
    unittest.main(exit=False)
