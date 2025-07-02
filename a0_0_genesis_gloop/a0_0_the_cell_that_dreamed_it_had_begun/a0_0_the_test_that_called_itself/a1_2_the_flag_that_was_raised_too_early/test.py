# s1_2_the_flag_that_was_raised_too_early/test.py

from main import analyze_flag_trigger

def run_tests():
    tests = [
        (None, "Error: Event log must be a list."),
        (["flag_raised", "init"], "Anomaly: flag was raised before init event."),
        (["flag_raised"], "Anomaly: flag was raised before initialization."),
        (["init", "flag_raised"], "Flag timing valid."),
        (["data", "init", "flag_raised"], "Flag timing valid."),
        (["data", "flag_raised"], "Anomaly: flag was raised before initialization."),
        (["init", "data", "compute"], "No flag was raised."),
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
