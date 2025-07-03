# a1_1_the_logfile_that_forgot_its_past/test.py

from main import analyze_logfile

def run_tests():
    tests = [
        (None, "Log analysis failed: the record was not even a list. The past is unreadable."),
        ([], "Log analysis failed: the logfile was empty. No memory remains."),
        ([{}], "Log analysis failed: an entry was missing its temporal marker or purpose."),
        ([{"timestamp": 2, "event": "exec"}, {"timestamp": 1, "event": "init"}],
         "Log analysis failed: chronological inconsistency detected. Time fractured."),
        ([{"timestamp": 1, "event": "exec"}],
         "Log analysis failed: the initialization was forgotten. No trace of origin."),
        ([{"timestamp": 1, "event": "init"}],
         "Log analysis passed: memory thread intact, origin event found."),
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
