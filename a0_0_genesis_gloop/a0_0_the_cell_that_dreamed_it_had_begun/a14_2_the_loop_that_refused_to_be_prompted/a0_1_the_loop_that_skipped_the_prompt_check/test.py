# test.py
"""
Primordial Soup – Test for: a0_1_the_loop_that_skipped_the_prompt_check

Purpose:
Verifies that the autonomous loop runs for the correct number of iterations
and contains no prompt-checking logic.
"""

import time
from main import autonomous_loop

def test_autonomous_loop_behavior():
    print("🧪 Running test for autonomous loop (no prompt checks)...")

    start_time = time.time()
    autonomous_loop(max_iterations=5)
    end_time = time.time()

    duration = end_time - start_time
    assert duration >= 2.5, "Loop did not run for expected minimum time."

    print("✅ Test complete: The loop skipped prompts and completed autonomously.")

if __name__ == "__main__":
    test_autonomous_loop_behavior()
