# test.py
# 🧪 Test for The Flag That Waited in Memory

import unittest
from main import DormantFlag

class TestDormantFlag(unittest.TestCase):
    def test_flag_none(self):
        df = DormantFlag()
        result = df.process_flag()
        self.assertEqual(result, "dormant")

    def test_flag_awaken(self):
        df = DormantFlag()
        df.set_flag("awaken")
        result = df.process_flag()
        self.assertEqual(result, "resolved")

    def test_flag_unknown(self):
        df = DormantFlag()
        df.set_flag("hibernate")
        result = df.process_flag()
        self.assertEqual(result, "unknown")

if __name__ == "__main__":
    unittest.main()
