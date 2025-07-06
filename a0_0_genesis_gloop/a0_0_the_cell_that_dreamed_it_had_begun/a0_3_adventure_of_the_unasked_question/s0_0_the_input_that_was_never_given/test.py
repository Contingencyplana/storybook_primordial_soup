# test.py – s0_0_the_input_that_was_never_given

import unittest
from main import await_input

class TestAwaitInput(unittest.TestCase):

    def test_no_input(self):
        self.assertEqual(await_input(), "No input received. System remains idle, listening...")

    def test_empty_string(self):
        self.assertEqual(await_input(""), "Empty input detected. Still waiting for meaningful signal.")

    def test_whitespace_only(self):
        self.assertEqual(await_input("   "), "Empty input detected. Still waiting for meaningful signal.")

    def test_valid_input(self):
        self.assertEqual(await_input("Begin sequence"), "Input received: 'Begin sequence'. System proceeds to next phase.")

    def test_special_characters(self):
        self.assertEqual(await_input("@#&*!"), "Input received: '@#&*!'. System proceeds to next phase.")


if __name__ == "__main__":
    unittest.main()
