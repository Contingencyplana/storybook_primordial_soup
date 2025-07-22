# test.py
# Test for: a0_0_add_empty_minigame_node

import os
import shutil
import tempfile
import unittest
from main import add_empty_minigame_node

class TestAddEmptyMinigameNode(unittest.TestCase):
    """
    Tests the a0_0_add_empty_minigame_node module for both temp and live recursive growth.
    """

    def setUp(self):
        # Set live test path
        self.live_test_dir = r"C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\a0_0_the_cell_that_dreamed_it_had_begun\a99_0_test_create_minigame_node"
        self.live_minigame_name = "a99_4_dummy_minigame"

        # Set temp test path
        self.test_dir = tempfile.mkdtemp()
        self.temp_minigame_name = "a99_0_test_minigame_node"

    def tearDown(self):
        # Remove only temp directory to keep live recursion intact
        shutil.rmtree(self.test_dir)

    def test_temp_minigame_node_creation(self):
        """
        Test in temp folder (safe mode).
        """
        result = add_empty_minigame_node(self.test_dir, self.temp_minigame_name, trigger_indexing=True)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["minigame"], self.temp_minigame_name)

        expected_files = [
            os.path.join(self.test_dir, self.temp_minigame_name, "__init__.py"),
            os.path.join(self.test_dir, self.temp_minigame_name, "main.py"),
            os.path.join(self.test_dir, self.temp_minigame_name, "taskmaps", "taskmap.md"),
            os.path.join(self.test_dir, self.temp_minigame_name, "taskmaps", "README.md"),
            os.path.join(self.test_dir, self.temp_minigame_name, "taskmaps", "milestones.md"),
        ]

        for file_path in expected_files:
            self.assertTrue(os.path.isfile(file_path), f"Missing file: {file_path}")

        trace = result["trace"]
        self.assertEqual(trace["event"], "add_empty_minigame_node")
        self.assertTrue("indexing_signal" in trace)

    def test_live_minigame_node_creation(self):
        """
        Test real recursion by writing directly to a99_0_test_create_minigame_node.
        """
        result = add_empty_minigame_node(self.live_test_dir, self.live_minigame_name, trigger_indexing=True, live_mode=True)

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["minigame"], self.live_minigame_name)

        expected_files = [
            os.path.join(self.live_test_dir, self.live_minigame_name, "__init__.py"),
            os.path.join(self.live_test_dir, self.live_minigame_name, "main.py"),
            os.path.join(self.live_test_dir, self.live_minigame_name, "taskmaps", "taskmap.md"),
            os.path.join(self.live_test_dir, self.live_minigame_name, "taskmaps", "README.md"),
            os.path.join(self.live_test_dir, self.live_minigame_name, "taskmaps", "milestones.md"),
        ]

        for file_path in expected_files:
            self.assertTrue(os.path.isfile(file_path), f"Missing file: {file_path}")

        trace = result["trace"]
        self.assertEqual(trace["event"], "add_empty_minigame_node")
        self.assertTrue(trace["live_mode"])
        self.assertTrue("indexing_signal" in trace)

    def test_duplicate_prevention(self):
        """
        Test that attempting to create the same minigame node twice returns an error.
        """
        add_empty_minigame_node(self.test_dir, self.temp_minigame_name)
        duplicate_attempt = add_empty_minigame_node(self.test_dir, self.temp_minigame_name)

        self.assertEqual(duplicate_attempt["status"], "error")
        self.assertIn("already exists", duplicate_attempt["message"])

if __name__ == "__main__":
    unittest.main()
