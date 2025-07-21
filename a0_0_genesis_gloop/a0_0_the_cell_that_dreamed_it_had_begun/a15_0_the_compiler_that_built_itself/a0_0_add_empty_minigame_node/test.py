# test.py
# Test for: a0_0_add_empty_minigame_node

import os
import shutil
import tempfile
import unittest
from main import add_empty_minigame_node

class TestAddEmptyMinigameNode(unittest.TestCase):
    """
    Tests the a0_0_add_empty_minigame_node module to ensure correct folder and file scaffolding.
    """

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = tempfile.mkdtemp()
        self.minigame_name = "a99_0_test_minigame_node"

    def tearDown(self):
        # Remove the temporary directory after tests
        shutil.rmtree(self.test_dir)

    def test_minigame_node_creation(self):
        """
        Test that the empty minigame node is created with the correct structure and placeholders.
        """
        result = add_empty_minigame_node(self.test_dir, self.minigame_name)

        # Check status
        self.assertEqual(result["status"], "success")
        self.assertEqual(result["minigame"], self.minigame_name)

        # Check that all expected paths exist
        expected_files = [
            os.path.join(self.test_dir, self.minigame_name, "__init__.py"),
            os.path.join(self.test_dir, self.minigame_name, "main.py"),
            os.path.join(self.test_dir, self.minigame_name, "taskmaps", "taskmap.md"),
            os.path.join(self.test_dir, self.minigame_name, "taskmaps", "README.md"),
            os.path.join(self.test_dir, self.minigame_name, "taskmaps", "milestones.md"),
        ]

        for file_path in expected_files:
            self.assertTrue(os.path.isfile(file_path), f"Missing file: {file_path}")

        # Check placeholder content in one file as a sample
        sample_file = os.path.join(self.test_dir, self.minigame_name, "main.py")
        with open(sample_file, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("AUTO-GENERATED PLACEHOLDER", content)

        # Check recursive trace exists and contains expected keys
        self.assertIn("trace", result)
        trace = result["trace"]
        self.assertEqual(trace["event"], "add_empty_minigame_node")
        self.assertEqual(trace["minigame"], self.minigame_name)
        self.assertIn("paths_created", trace)
        self.assertIn("timestamp", trace)

if __name__ == "__main__":
    unittest.main()
