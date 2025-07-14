# test.py
# 🧪 Test for The Argument That Lacked a Listener

import unittest
from main import SilentArgument

class TestSilentArgument(unittest.TestCase):
    def test_no_listener(self):
        sa = SilentArgument()
        sa.set_argument("begin_feedback_loop")
        result = sa.process_argument()
        self.assertEqual(result, "no_listener")

    def test_listener_no_argument(self):
        sa = SilentArgument()
        sa.listener = True
        result = sa.process_argument()
        self.assertEqual(result, "no_argument")

    def test_listener_with_argument(self):
        sa = SilentArgument()
        sa.listener = True
        sa.set_argument("begin_feedback_loop")
        result = sa.process_argument()
        self.assertEqual(result, "processed_begin_feedback_loop")

if __name__ == "__main__":
    unittest.main()
