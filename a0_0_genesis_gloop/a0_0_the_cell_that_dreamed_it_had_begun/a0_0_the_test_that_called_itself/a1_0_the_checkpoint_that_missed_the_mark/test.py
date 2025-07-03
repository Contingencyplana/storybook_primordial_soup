# s1_0_the_checkpoint_that_missed_the_mark/test.py

from main import evaluate_checkpoint

def run_tests():
    tests = [
        (None, "Checkpoint failed: signal was not a dictionary."),
        ([], "Checkpoint failed: signal was not a dictionary."),
        ({}, "Checkpoint failed: 'status' key missing."),
        ({"status": "not_ready"}, "Checkpoint failed: status was 'not_ready' not 'ready'."),
    ]

    passed = 0
    for i, (input_data, expected) in enumerate(tests):
        result = evaluate_checkpoint(input_data)
        if result == expected:
            print(f"Test {i+1}: ✅ PASS")
            passed += 1
        else:
            print(f"Test {i+1}: ❌ FAIL")
            print(f"  Input: {input_data}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")

    # Special case: test with "ready" status, expect timestamped output
    final_input = {"status": "ready"}
    final_result = evaluate_checkpoint(final_input)
    if final_result.startswith("Checkpoint passed: status is ready at "):
        print("Test 5: ✅ PASS")
        passed += 1
    else:
        print("Test 5: ❌ FAIL")
        print(f"  Input: {final_input}")
        print(f"  Got: {final_result}")

    print(f"\n{passed}/5 tests passed.")

if __name__ == "__main__":
    run_tests()
