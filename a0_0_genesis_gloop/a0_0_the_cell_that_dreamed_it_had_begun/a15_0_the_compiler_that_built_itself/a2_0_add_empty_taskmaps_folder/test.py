# a2_0_add_empty_taskmaps_folder/test.py

import os
import shutil
import unittest
from main import create_taskmaps_folder

class TestCreateTaskmapsFolder(unittest.TestCase):
    def setUp(self):
        self.test_dir = os.path.join(os.getcwd(), "test_minigame_node")
        self.taskmaps_path = os.path.join(self.test_dir, "taskmaps")

        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_folder_if_missing(self):
        result = create_taskmaps_folder(self.test_dir)
        self.assertTrue(os.path.exists(self.taskmaps_path))
        self.assertEqual(result["status"], "added")
        self.assertEqual(result["event"], "created_taskmaps_folder")

    def test_skip_if_folder_exists(self):
        os.makedirs(self.taskmaps_path)
        result = create_taskmaps_folder(self.test_dir)
        self.assertEqual(result["status"], "skipped")
        self.assertEqual(result["event"], "existing_taskmaps_folder")

if __name__ == "__main__":
    unittest.main()
