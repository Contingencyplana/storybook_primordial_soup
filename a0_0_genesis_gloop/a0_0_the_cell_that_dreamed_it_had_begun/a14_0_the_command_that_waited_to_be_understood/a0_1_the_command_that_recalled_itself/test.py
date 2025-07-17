# test.py
# 🧪 Test for The Command That Recalled Itself

import unittest
from main import RecursiveCommand

class TestRecursiveCommand(unittest.TestCase):
    def test_no_command(self):
        rc = RecursiveCommand()
        result = rc.recall_last_command()
        self.assertIsNone(result)

    def test_single_command(self):
        rc = RecursiveCommand()
        rc.issue_command("initiate_awakening")
        result = rc.recall_last_command()
        self.assertEqual(result, "initiate_awakening")

    def test_multiple_commands(self):
        rc = RecursiveCommand()
        rc.issue_command("initiate_awakening")
        rc.issue_command("verify_state")
        rc.issue_command("activate_response")
        result = rc.recall_last_command()
        self.assertEqual(result, "activate_response")

if __name__ == "__main__":
    unittest.main()
