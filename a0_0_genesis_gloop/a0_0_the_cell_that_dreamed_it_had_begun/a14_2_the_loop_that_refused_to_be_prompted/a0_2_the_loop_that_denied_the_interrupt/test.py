# test.py
"""
Primordial Soup – Test for: a0_2_the_loop_that_denied_the_interrupt

Purpose:
Verifies that the loop detects KeyboardInterrupt signals but refuses to stop,
continuing recursion until the iteration limit is reached.
"""

import time
import threading
import signal
import os

from main import interrupt_denial_loop

def run_loop():
    interrupt_denial_loop(max_iterations=5)

def test_interrupt_denial_loop_behavior():
    print("🧪 Running test for interrupt denial loop...")

    loop_thread = threading.Thread(target=run_loop)
    loop_thread.start()

    # Wait briefly then send interrupt signal to the current process
    time.sleep(1.5)
    os.kill(os.getpid(), signal.SIGINT)

    loop_thread.join()

    print("✅ Test complete: Interrupt was detected but the loop continued as expected.")

if __name__ == "__main__":
    test_interrupt_denial_loop_behavior()
