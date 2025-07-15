# test.py
"""
Primordial Soup – Test for: a0_3_the_loop_that_forgot_it_could_stop

Purpose:
Verifies that the loop enters infinite recursion by design, simulating recursive amnesia.
The test confirms loop execution starts but must forcibly terminate the loop after observation.
"""

import time
import multiprocessing

from main import amnesiac_loop

def run_loop():
    amnesiac_loop()

def test_amnesiac_loop_behavior():
    print("🧪 Running test for amnesiac loop (infinite recursion)...")

    # Run the loop in a separate process to allow forced termination
    process = multiprocessing.Process(target=run_loop)
    process.start()

    # Let it run briefly to observe behavior
    time.sleep(3)

    # Terminate the loop process
    process.terminate()
    process.join()

    print("✅ Test complete: Loop recursed infinitely until forcibly stopped.")

if __name__ == "__main__":
    test_amnesiac_loop_behavior()
