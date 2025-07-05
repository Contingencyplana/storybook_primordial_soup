# a5_3_the_system_that_called_too_late/test.py

import time
from main import recover_system

def run_test():
    print("🔍 Running test: system response delay...\n")

    # Simulate delayed recovery (too late)
    trigger_time = time.time()
    time.sleep(2.5)  # exceed timeout
    result = recover_system(trigger_time)
    print("🕒 Test: Delayed Recovery")
    print(f"📜 Status: {result['status']}")
    print(f"🧪 Message: {result['message']}")
    print(f"⏱️ Delay: {result['delay']:.2f} seconds")
    print("-" * 40)

    # Simulate prompt recovery
    trigger_time = time.time()
    time.sleep(0.5)  # within timeout
    result = recover_system(trigger_time)
    print("🕒 Test: Timely Recovery")
    print(f"📜 Status: {result['status']}")
    print(f"🧪 Message: {result['message']}")
    print(f"⏱️ Delay: {result['delay']:.2f} seconds")
    print("-" * 40)

if __name__ == "__main__":
    run_test()
