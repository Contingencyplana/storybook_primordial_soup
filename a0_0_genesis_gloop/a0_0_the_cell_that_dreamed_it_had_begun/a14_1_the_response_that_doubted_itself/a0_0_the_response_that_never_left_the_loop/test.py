# Save to: a14_1_the_response_that_doubted_itself/a0_0_the_response_that_never_left_the_loop/test.py

import unittest
import io
import sys
from main import hesitant_response

class TestHesitantResponse(unittest.TestCase):
    def test_hesitant_loop_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output

        hesitant_response()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Maximum hesitation reached", output)
        self.assertEqual(output.count("Checking if response is authorized..."), 10)

if __name__ == "__main__":
    unittest.main()
