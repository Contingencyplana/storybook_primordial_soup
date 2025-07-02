# a1_1_the_logfile_that_forgot_its_past/test.py

from main import analyze_logfile

def run_tests():
    tests = [
        (None, "Log analysis failed: input was not a list."),
        ([], "Log analysis failed: logfile is empty."),
        ([{}], "Log analysis failed: entry missing 'timestamp' or 'event'."),
        ([{"timestamp": 2, "event": "exec"}, {"timestamp": 1, "event": "init"}],
         "Log analysis failed: timestamps are out of order."),
        ([{"timestamp": 1, "event": "exec"}],
         "Log analysis failed: initialization event not found."),
        ([{"timestamp": 1, "event": "init"}],
         "Log analysis passed: entries valid and initialization detected."),
    ]

    passed = 0
    for i, (input_data, expected) in enumerate(tests):
        result = analyze_logfile(input_data)
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
