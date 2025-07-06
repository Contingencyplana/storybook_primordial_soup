# test.py

from main import incomplete_loop_detector

def run_tests():
    test_cases = [
        (["INIT", "STEP1", "STEP2", "END"], True),
        (["INIT", "STEP1", "BREAK", "END"], False),
        (["INIT", "STEP1", "STEP2", "FINAL"], False),
        ([], True),  # Edge case: an empty loop is considered trivially complete
    ]

    for i, (sequence, expected) in enumerate(test_cases, 1):
        result = incomplete_loop_detector(sequence)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status} | Input: {sequence} | Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()
