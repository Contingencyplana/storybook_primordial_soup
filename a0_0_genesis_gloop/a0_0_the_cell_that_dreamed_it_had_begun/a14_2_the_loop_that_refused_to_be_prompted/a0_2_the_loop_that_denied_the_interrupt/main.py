# main.py
"""
Primordial Soup – Minigame Node: a0_2_the_loop_that_denied_the_interrupt

Purpose:
Implements a loop that detects external interrupts (e.g., KeyboardInterrupt)
but deliberately refuses to stop. The loop acknowledges the signal but continues execution.

Phase 2 – The Awakening
"""

import time

def interrupt_denial_loop(max_iterations=10):
    iteration = 0
    print("🛡️ The loop has entered interrupt denial mode. It will detect interrupts but refuse to stop.")

    while iteration < max_iterations:
        try:
            print(f"🔄 Iteration {iteration + 1}: Continuing recursion. (Interrupts ignored intentionally)")
            iteration += 1
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("⚠️ Interrupt detected—but this loop denies external control and continues recursion.")

    print("✅ Interrupt denial loop completed. The loop rejected all external stop attempts.")

if __name__ == "__main__":
    interrupt_denial_loop()
