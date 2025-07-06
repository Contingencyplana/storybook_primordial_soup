# Save to: s0_1_the_trace_that_forgot_itself/test.py

from main import trace_pathback

def run_tests():
    test_cases = [
        (["init", "load", "execute", "complete"], True),
        (["init", None, "execute", "complete"], False),
        ([None, "load", "execute"], False),
        ([], True),  # Empty trace considered trivially intact
    ]

    for i, (history, expected) in enumerate(test_cases, 1):
        result = trace_pathback(history)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status} | Input: {history} | Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()
