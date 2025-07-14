# Save to: a14_1_the_response_that_doubted_itself/a0_3_the_echo_that_tested_the_speaker/test.py

import unittest
import io
import sys
from main import echo_and_test

class TestEchoAndTest(unittest.TestCase):
    def test_echo_reflection(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        test_command = "Run diagnostic cycle"
        echo_and_test(test_command)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn(f"🔁 Echoing back: '{test_command}'", output)
        self.assertIn(f"🧠 Reflecting on command: '{test_command}'", output)
        self.assertIn("🤔 Doubt remains: The system is unsure if the command was truly meant.", output)
        self.assertNotIn("✅ Confirmation received", output)

if __name__ == "__main__":
    unittest.main()
