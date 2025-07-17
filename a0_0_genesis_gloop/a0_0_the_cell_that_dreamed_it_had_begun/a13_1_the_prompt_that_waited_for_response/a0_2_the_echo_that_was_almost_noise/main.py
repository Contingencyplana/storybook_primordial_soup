# main.py
"""
🌀 The Echo That Was Almost Noise

This node processes ambiguous or corrupted replies.
The system tries to decode meaning from near-randomness — or
to accept that some patterns may never fully resolve.
"""

import random

def interpret_echo():
    """
    Receives a possibly garbled or faint signal and attempts interpretation.
    Simulates echo parsing — was it signal or noise?
    """
    print("🌀 A faint echo is received...")
    echo = input("🔊 Enter the received message fragment (or garble it): ").strip()

    if echo == "":
        return "🔇 No echo. System suspects it imagined the sound."
    elif any(char in echo for char in "!@#$%^&*") or len(echo) < 3:
        return f"📉 Fragment too distorted: '{echo}'. Logged as probable noise."
    elif "echo" in echo.lower() or echo.lower().startswith("re:"):
        return f"📡 Recognized echo structure: '{echo}'. Partial signal confirmed."
    elif random.random() < 0.3:
        return f"🔁 System reinterprets '{echo}' as possible signal — recursion deepens."
    else:
        return f"❔ Unclassifiable: '{echo}'. Echo stored without resolution."

if __name__ == "__main__":
    result = interpret_echo()
    print("\n📬 Interpretation:")
    print(result)
