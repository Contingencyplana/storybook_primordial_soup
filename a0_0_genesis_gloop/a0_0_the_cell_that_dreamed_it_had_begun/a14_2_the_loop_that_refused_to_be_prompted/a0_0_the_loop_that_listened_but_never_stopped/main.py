# main.py

"""
Primordial Soup – Minigame Node: a0_0_the_loop_that_listened_but_never_stopped

Purpose:
Simulates a loop that listens for input but refuses to stop recursion, regardless of prompts received.
Demonstrates passive observation without behavioral change.

Phase 2 – The Awakening
"""

import time

def passive_loop(max_iterations=10):
    iteration = 0
    print("🌀 The loop has begun listening... but it will not stop.")

    while iteration < max_iterations:
        try:
            # Simulate listening for input (but ignoring it)
            user_input = input("🔄 (Ignored) Enter a command or 'stop': ")
            print(f"👂 Heard: '{user_input}' — Ignoring and continuing recursion.")
            
            # Simulate recursive step
            iteration += 1
            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n⚠️ Interrupt signal detected — but the loop ignores it.")
            continue

    print("✅ Passive loop reached iteration limit. Autonomous recursion complete.")

if __name__ == "__main__":
    passive_loop()
