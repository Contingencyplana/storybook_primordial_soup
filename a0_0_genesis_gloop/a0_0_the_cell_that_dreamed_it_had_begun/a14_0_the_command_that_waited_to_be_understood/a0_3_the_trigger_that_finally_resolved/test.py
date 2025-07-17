# test.py
# 🧪 Test for The Trigger That Finally Resolved

import unittest
from main import DeferredTrigger

class TestDeferredTrigger(unittest.TestCase):
    def test_trigger_deferred(self):
        dt = DeferredTrigger()
        result = dt.resolve_trigger()
        self.assertEqual(result, "deferred")
        self.assertFalse(dt.trigger_resolved)

    def test_trigger_resolved(self):
        dt = DeferredTrigger()
        dt.condition_met = True
        result = dt.resolve_trigger()
        self.assertEqual(result, "resolved")
        self.assertTrue(dt.trigger_resolved)

if __name__ == "__main__":
    unittest.main()
