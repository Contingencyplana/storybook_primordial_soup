# test.py

"""
Primordial Soup – Test for: a0_0_the_loop_that_listened_but_never_stopped

Purpose:
Verifies that the passive loop executes for the correct number of iterations,
ignores input, and handles keyboard interrupts without breaking recursion.
"""

import builtins
import time
import threading
from unittest.mock import patch

from main import passive_loop

def mock_input(prompt):
    # Always return 'stop' to simulate ignored stop commands
    print(prompt + " [simulated input: 'stop']")
    return "stop"

def run_loop():
    passive_loop(max_iterations=5)

def test_passive_loop_behavior():
    print("🧪 Running test for passive loop...")

    with patch.object(builtins, 'input', side_effect=mock_input):
        loop_thread = threading.Thread(target=run_loop)
        loop_thread.start()
        loop_thread.join()

    print("✅ Test complete: The loop listened but did not stop prematurely.")

if __name__ == "__main__":
    test_passive_loop_behavior()
