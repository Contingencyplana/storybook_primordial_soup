# a0_0_add_empty_minigame_node/test.py

import os
import shutil
import unittest
from main import add_empty_minigame_node

class TestAddEmptyMinigameNode(unittest.TestCase):

    def setUp(self):
        self.test_base_path = "./test_minigame_output"
        self.minigame_name = "a99_0_test_minigame"

        # Ensure clean test environment
        if os.path.exists(self.test_base_path):
            shutil.rmtree(self.test_base_path)

    def tearDown(self):
        # Cleanup after tests
        if os.path.exists(self.test_base_path):
            shutil.rmtree(self.test_base_path)

    def test_minigame_node_creation(self):
        result = add_empty_minigame_node(self.test_base_path, self.minigame_name)

        minigame_path = os.path.join(self.test_base_path, self.minigame_name)
        taskmaps_path = os.path.join(minigame_path, 'taskmaps')

        # Check if directories were created
        self.assertTrue(os.path.isdir(minigame_path))
        self.assertTrue(os.path.isdir(taskmaps_path))

        # Check if files were created
        expected_files = [
            '__init__.py',
            'main.py',
            'taskmap.md',
            'README.md',
            'milestones.md'
        ]

        for file_name in expected_files:
            if file_name.endswith('.py'):
                file_path = os.path.join(minigame_path, file_name)
            else:
                file_path = os.path.join(taskmaps_path, file_name)
            self.assertTrue(os.path.isfile(file_path), f"Missing file: {file_path}")

        # Check output status
        self.assertEqual(result["status"], "success")
        self.assertIn(self.minigame_name, result["minigame"])

if __name__ == "__main__":
    unittest.main()
