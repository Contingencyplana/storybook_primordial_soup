# test.py
"""
🧪 Test – The Echo That Was Almost Noise

Tests how the system handles ambiguous feedback and echo-like distortions.
"""

from main import interpret_echo

def run_echo_test():
    print("🧪 Echo Test – Signal or Noise?")
    print("--------------------------------")
    result = interpret_echo()
    print("\n✅ Result:")
    print(result)

if __name__ == "__main__":
    run_echo_test()
