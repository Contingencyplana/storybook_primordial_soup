# a1_2_the_flag_that_was_raised_too_early/test.py

from main import analyze_flag_trigger

def run_tests():
    tests = [
        (None, "Chronology error: event log is not a list. Timeline unreadable."),
        (["flag_raised", "init"], "Temporal anomaly: flag raised before initialization sequence began."),
        (["flag_raised"], "Temporal anomaly: flag raised with no initialization. Premature trigger."),
        (["init", "flag_raised"], "Flag timing confirmed: initialization preceded flag."),
        (["data", "init", "flag_raised"], "Flag timing confirmed: initialization preceded flag."),
        (["data", "flag_raised"], "Temporal anomaly: flag raised with no initialization. Premature trigger."),
        (["init", "data", "compute"], "No flag was raised in this cycle."),
    ]

    passed = 0
    for i, (input_data, expected) in enumerate(tests):
        result = analyze_flag_trigger(input_data)
        if result == expected:
            print(f"Test {i+1}: ✅ PASS")
            passed += 1
        else:
            print(f"Test {i+1}: ❌ FAIL")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    print(f"\n{passed}/{len(tests)} tests passed.")

if __name__ == "__main__":
    run_tests()
