# test.py

import unittest
from main import generate_signal, receive_echo, analyze_echo

class TestRecursiveEcho(unittest.TestCase):

    def test_echo_matched(self):
        signal = generate_signal()
        echo = signal
        result = analyze_echo(signal, echo)
        self.assertIn("matched", result)

    def test_echo_mismatched(self):
        signal = generate_signal()
        echo = "noise-" + generate_signal()
        result = analyze_echo(signal, echo)
        self.assertIn("mismatch", result)

    def test_echo_absent(self):
        signal = generate_signal()
        echo = None
        result = analyze_echo(signal, echo)
        self.assertIn("absent", result)

if __name__ == "__main__":
    unittest.main()
