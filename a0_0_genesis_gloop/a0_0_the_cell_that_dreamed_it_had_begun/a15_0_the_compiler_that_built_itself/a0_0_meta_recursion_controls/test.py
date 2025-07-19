# test.py  
# Primordial Soup – Meta-Recursion Controls Test Suite  
# Layer 4 Node: a0_0_meta_recursion_controls  

import unittest
import os
import shutil
from unittest.mock import patch
import main

class TestMetaRecursionControls(unittest.TestCase):

    def setUp(self):
        self.test_dir = 'test_output'
        os.makedirs(self.test_dir, exist_ok=True)
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)

    def test_create_minigame_node(self):
        with patch('builtins.input', return_value='test_node'):
            main.create_minigame_node()
            self.assertTrue(os.path.isdir('test_node'))
            expected_files = ['__init__.py', 'main.py', 'subtaskmap.md', 'test.py']
            for file in expected_files:
                self.assertTrue(os.path.isfile(os.path.join('test_node', file)))

    def test_create_minigame(self):
        with patch('builtins.input', return_value='test_minigame'):
            main.create_minigame()
            self.assertTrue(os.path.isdir('test_minigame'))
            for i in range(4):
                node_dir = os.path.join('test_minigame', f'a0_{i}')
                self.assertTrue(os.path.isdir(node_dir))
                expected_files = ['__init__.py', 'main.py', 'subtaskmap.md', 'test.py']
                for file in expected_files:
                    self.assertTrue(os.path.isfile(os.path.join(node_dir, file)))
            taskmaps_dir = os.path.join('test_minigame', 'taskmaps')
            self.assertTrue(os.path.isdir(taskmaps_dir))
            taskmap_files = ['README.md', 'milestones.md', 'stanzamap.md', 'taskmap.md']
            for file in taskmap_files:
                self.assertTrue(os.path.isfile(os.path.join(taskmaps_dir, file)))

    def test_exit_to_previous_layer(self):
        with self.assertRaises(SystemExit):
            main.exit_to_previous_layer()

    def test_select_from_branch_options_valid(self):
        options = ["Option A", "Option B", "Option C"]
        with patch('builtins.input', side_effect=['2']), patch('builtins.print') as mock_print:
            main.select_from_branch_options(options)
            mock_print.assert_any_call("Branch 2 selected: Option B")

    def test_select_from_branch_options_invalid_then_valid(self):
        options = ["Option A", "Option B"]
        with patch('builtins.input', side_effect=['5', '1']), patch('builtins.print') as mock_print:
            main.select_from_branch_options(options)
            mock_print.assert_any_call("Invalid option. Try again.")
            mock_print.assert_any_call("Branch 1 selected: Option A")

if __name__ == '__main__':
    unittest.main()
