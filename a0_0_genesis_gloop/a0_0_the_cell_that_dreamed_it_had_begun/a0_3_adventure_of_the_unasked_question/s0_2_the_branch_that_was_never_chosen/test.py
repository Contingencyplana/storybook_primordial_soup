# test.py – s0_2_the_branch_that_was_never_chosen

import unittest
from main import handle_branch

class TestHandleBranch(unittest.TestCase):

    def test_primary_path(self):
        self.assertEqual(
            handle_branch(False),
            "Primary path taken. Dormant branch remains untouched."
        )

    def test_dormant_branch_activation(self):
        self.assertEqual(
            handle_branch(True),
            "Dormant branch activated. Unexpected recursion initiated."
        )

    def test_default_behavior(self):
        self.assertEqual(
            handle_branch(),
            "Primary path taken. Dormant branch remains untouched."
        )


if __name__ == "__main__":
    unittest.main()
