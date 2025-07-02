# test.py — a2_0_the_assertion_that_unmade_itself
# Unit test for a paradoxical assertion that negates itself through recursion.

import unittest
from main import recursive_assertion

class TestRecursiveAssertion(unittest.TestCase):
    def test_contradiction_at_depth(self):
        """The recursive logic should contradict itself and resolve to False."""
        result = recursive_assertion()
        self.assertFalse(result)

    def test_truth_when_depth_is_zero(self):
        """If recursion is skipped, the assertion should remain True."""
        result = recursive_assertion(max_depth=0)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
