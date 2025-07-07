# 🧪 test.py
# Path: a11_1_the_signal_that_misremembered_itself/a0_0_the_echo_that_returned_in_rhyme

import unittest
from main import await_return_signal

class TestAwaitReturnSignal(unittest.TestCase):

    def test_signal_received(self):
        self.assertEqual(
            await_return_signal(signal_received=True),
            "Signal received. Return path resolved."
        )

    def test_timeout_behavior(self):
        self.assertEqual(
            await_return_signal(signal_received=False, timeout_seconds=5),
            "No signal. Return handler timed out after 5 seconds."
        )

    def test_indefinite_wait(self):
        self.assertEqual(
            await_return_signal(),
            "Return handler active. Still waiting in silence..."
        )


if __name__ == "__main__":
    unittest.main()
