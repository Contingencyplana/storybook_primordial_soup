# test.py — a2_3_the_fallback_that_caused_the_failure
# Tests for paradoxical fallback behavior.

import unittest
from main import risky_fallback_handler

class TestFallbackFailure(unittest.TestCase):
    def test_valid_signal_with_fallback(self):
        """Fallback should cause failure if triggered on valid input."""
        result = risky_fallback_handler("valid", allow_failure=True)
        self.assertIn("Failure", result)

    def test_invalid_signal_triggers_fallback(self):
        """Fallback engages correctly on bad signal."""
        result = risky_fallback_handler("corrupted")
        self.assertIn("Fallback engaged", result)

    def test_valid_signal_without_fallback(self):
        """Normal operation if fallback is not allowed."""
        result = risky_fallback_handler("valid", allow_failure=False)
        self.assertIn("Signal processed normally", result)

if __name__ == "__main__":
    unittest.main()
