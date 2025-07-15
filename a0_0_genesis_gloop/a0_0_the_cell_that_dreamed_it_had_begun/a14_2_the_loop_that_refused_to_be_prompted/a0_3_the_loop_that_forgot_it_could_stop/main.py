# main.py
"""
Primordial Soup – Minigame Node: a0_3_the_loop_that_forgot_it_could_stop

Purpose:
Implements a loop that forgets its own stopping condition.
This simulates recursive amnesia where the loop runs indefinitely unless forcibly terminated.

Phase 2 – The Awakening
"""

import time

def amnesiac_loop():
    print("♾️ The loop has forgotten how to stop. Recursive amnesia engaged.")
    
    iteration = 0
    while True:
        print(f"🔁 Iteration {iteration}: Recursing without end.")
        iteration += 1
        time.sleep(0.5)

if __name__ == "__main__":
    amnesiac_loop()
