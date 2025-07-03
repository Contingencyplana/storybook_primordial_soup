# test.py — a2_2_the_trace_that_returned_too_late
# Unit test for delayed trace return logic.

import unittest
from main import delayed_trace_response

class TestDelayedTrace(unittest.TestCase):
    def test_signal_too_late(self):
        """Should report that the signal returned too late."""
        result = delayed_trace_response("ping", delay_threshold=1.0)
        self.assertTrue(result.startswith("Trace failed"))
        self.assertIn("too late", result)

    def test_custom_threshold_still_too_late(self):
        """Even with higher threshold, delay still overshoots."""
        result = delayed_trace_response("ping", delay_threshold=0.1)
        self.assertIn("returned too late", result)

if __name__ == "__main__":
    unittest.main()
