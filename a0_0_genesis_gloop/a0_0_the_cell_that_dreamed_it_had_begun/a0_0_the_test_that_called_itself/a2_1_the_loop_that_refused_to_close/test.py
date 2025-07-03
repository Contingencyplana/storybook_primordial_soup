# test.py — a2_1_the_loop_that_refused_to_close
# Unit test for a loop that fails to close despite iteration.

import unittest
from main import incomplete_loop_detector

class TestIncompleteLoop(unittest.TestCase):
    def test_loop_hits_threshold_without_closure(self):
        """Should detect that the loop ended without marking closure."""
        result = incomplete_loop_detector()
        self.assertTrue(result.startswith("Loop terminated at"))
        self.assertIn("never reached closure", result)

    def test_custom_threshold(self):
        """Should still fail to close at a custom threshold."""
        result = incomplete_loop_detector(threshold=5)
        self.assertTrue("terminated at 5" in result)

if __name__ == "__main__":
    unittest.main()
