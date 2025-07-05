# Save to: s0_0_the_call_that_woke_the_bug_king/test.py

import sys
from main import awaken_bug_king

def simulate_input():
    print("📡 Signal calibration for the Bug King’s awakening.")
    try:
        strength = float(input("Enter signal strength (0.0–1.0): "))
    except ValueError:
        print("❌ Invalid input. Please enter a decimal between 0.0 and 1.0.")
        return

    result = awaken_bug_king(strength)
    print("\n📜 Chirp Report:")
    for key, value in result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    simulate_input()
