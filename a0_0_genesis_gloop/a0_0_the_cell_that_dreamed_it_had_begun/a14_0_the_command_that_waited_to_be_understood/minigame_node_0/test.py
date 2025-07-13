# test.py
# 🧪 Test for The Flag That Waited in Memory

import unittest
from main import DormantFlag

class TestDormantFlag(unittest.TestCase):
    def test_no_flag(self):
        df = DormantFlag()
        result = df.check_flag()
        self.assertEqual(result, "dormant")

    def test_awaken_flag(self):
        df = DormantFlag()
        df.set_flag("awaken")
        result = df.check_flag()
        self.assertEqual(result, "resolved")

    def test_unknown_flag(self):
        df = DormantFlag()
        df.set_flag("sleep")
        result = df.check_flag()
        self.assertEqual(result, "unknown_flag")

if __name__ == "__main__":
    unittest.main()
