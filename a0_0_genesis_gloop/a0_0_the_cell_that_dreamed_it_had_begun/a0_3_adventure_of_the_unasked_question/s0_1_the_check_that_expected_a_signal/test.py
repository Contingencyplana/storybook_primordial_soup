# test.py – s0_1_the_check_that_expected_a_signal

import unittest
from main import validate_expected_signal

class TestValidateExpectedSignal(unittest.TestCase):

    def test_none_signal(self):
        self.assertEqual(
            validate_expected_signal(),
            "Validation failed: Expected a signal, but none was received."
        )

    def test_empty_string(self):
        self.assertEqual(
            validate_expected_signal(""),
            "Validation failed: Received an empty or blank signal."
        )

    def test_whitespace_signal(self):
        self.assertEqual(
            validate_expected_signal("   "),
            "Validation failed: Received an empty or blank signal."
        )

    def test_non_string_signal(self):
        self.assertEqual(
            validate_expected_signal(42),
            "Validation failed: Signal received is not a string."
        )

    def test_valid_signal(self):
        self.assertEqual(
            validate_expected_signal("wake-up-call"),
            "Signal 'wake-up-call' validated successfully."
        )


if __name__ == "__main__":
    unittest.main()
