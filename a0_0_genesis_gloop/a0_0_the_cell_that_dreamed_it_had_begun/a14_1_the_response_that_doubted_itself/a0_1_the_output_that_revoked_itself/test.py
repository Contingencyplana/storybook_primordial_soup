# Save to: a14_1_the_response_that_doubted_itself/a0_1_the_output_that_revoked_itself/test.py

import unittest
import io
import sys
from main import generate_output

class TestOutputRevocation(unittest.TestCase):
    def test_output_revocation(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        generate_output()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("🗨️  Initial Output: The system believes it has a response.", output)
        self.assertIn("🚫 Output Revoked: The system doubts its own response and cancels it.", output)
        self.assertNotIn("✅ Output Confirmed", output)

if __name__ == "__main__":
    unittest.main()
