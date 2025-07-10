# s0_3_the_fallback_that_made_it_real/test.py

import unittest
from main import fallback_believe

class TestFallbackBehavior(unittest.TestCase):

    def test_valid_signal(self):
        result = fallback_believe("respond")
        self.assertEqual(result["status"], "validated")
        self.assertTrue(result["action_taken"])

    def test_invalid_signal_with_fallback(self):
        result = fallback_believe("???signal???")
        self.assertEqual(result["status"], "assumed-valid")
        self.assertTrue(result["action_taken"])
        self.assertIn("fallback", result["reason"].lower())

    def test_invalid_signal_without_fallback(self):
        result = fallback_believe("???signal???", enable_fallback=False)
        self.assertEqual(result["status"], "rejected")
        self.assertFalse(result["action_taken"])
        self.assertIn("unrecognized", result["reason"].lower())

if __name__ == "__main__":
    unittest.main()
