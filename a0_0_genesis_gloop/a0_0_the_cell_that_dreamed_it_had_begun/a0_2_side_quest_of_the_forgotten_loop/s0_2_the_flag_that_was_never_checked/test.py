# Save to: s0_2_the_flag_that_was_never_checked/test.py

from main import check_unacknowledged_flag

def run_tests():
    test_cases = [
        (True, [], True),                      # Flag raised, no observers → anomaly
        (True, ["watcher1"], False),           # Flag raised, acknowledged → okay
        (False, ["watcher1", "watcher2"], False), # No flag raised → okay
        (False, [], False),                    # No flag raised, no observers → okay
    ]

    for i, (flag, observers, expected) in enumerate(test_cases, 1):
        result = check_unacknowledged_flag(flag, observers)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status} | Flag: {flag}, Observers: {observers} | Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()
