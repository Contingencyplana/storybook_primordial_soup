# test.py

import unittest
from main import generate_prompt, auto_reply

class TestPromptAutoReply(unittest.TestCase):

    def test_prompt_generation(self):
        prompt = generate_prompt()
        self.assertTrue(prompt.startswith("prompt-"))
        self.assertGreater(len(prompt), 10)

    def test_auto_reply_contains_prompt_id(self):
        prompt = generate_prompt()
        reply = auto_reply(prompt)
        self.assertIn(prompt, reply)

if __name__ == "__main__":
    unittest.main()
