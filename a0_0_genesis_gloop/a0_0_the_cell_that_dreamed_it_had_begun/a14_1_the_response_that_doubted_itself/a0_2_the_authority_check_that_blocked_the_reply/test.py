# Save to: a14_1_the_response_that_doubted_itself/a0_2_the_authority_check_that_blocked_the_reply/test.py

import unittest
import io
import sys
from main import attempt_response

class TestAuthorityCheck(unittest.TestCase):
    def test_response_blocked(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        attempt_response()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("🗨️  Attempting to generate response...", output)
        self.assertIn("🔄 Checking for authority to respond...", output)
        self.assertIn("🚫 Authority Denied: Response blocked by recursive check.", output)
        self.assertNotIn("✅ Authority Granted", output)

if __name__ == "__main__":
    unittest.main()
