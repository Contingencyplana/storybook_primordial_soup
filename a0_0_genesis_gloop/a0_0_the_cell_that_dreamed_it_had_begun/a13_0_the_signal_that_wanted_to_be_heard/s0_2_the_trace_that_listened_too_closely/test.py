# s0_2_the_trace_that_listened_too_closely/test.py

import unittest
from main import interpret_stream

class TestTraceOverload(unittest.TestCase):

    def test_no_signal(self):
        noise_stream = ["static", "buzz", "flicker", "scramble"]
        result = interpret_stream(noise_stream)
        self.assertFalse(result["overload"])
        self.assertEqual(len(result["detected_signals"]), 0)

    def test_with_signal_and_noise(self):
        mixed_stream = ["static", "begin", "buzz", "??", "validate"]
        result = interpret_stream(mixed_stream)
        self.assertIn("begin", result["detected_signals"])
        self.assertIn("validate", result["detected_signals"])
        self.assertTrue(any("ambiguous:" in s for s in result["detected_signals"]))

    def test_overload_condition(self):
        overload_stream = ["begin", "validate", "respond", "trace:01", "SIGNAL?", "??", "###"]
        result = interpret_stream(overload_stream)
        self.assertTrue(result["overload"])

if __name__ == "__main__":
    unittest.main()
