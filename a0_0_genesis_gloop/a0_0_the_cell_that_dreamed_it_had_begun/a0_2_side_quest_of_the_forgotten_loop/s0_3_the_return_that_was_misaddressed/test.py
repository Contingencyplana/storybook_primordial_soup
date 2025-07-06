# Save to: s0_3_the_return_that_was_misaddressed/test.py

from main import validate_return_routing

def run_tests():
    test_cases = [
        ("OK", {"alpha": "Subsystem A", "beta": "Subsystem B"}, "alpha", True),
        ("42", {"alpha": "Subsystem A", "beta": "Subsystem B"}, "gamma", False),
        (None, {"x": "Memory Module"}, "x", True),
        ("alert", {}, "admin", False),  # No recipients at all
    ]

    for i, (value, registry, target, expected) in enumerate(test_cases, 1):
        result = validate_return_routing(value, registry, target)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"Test {i}: {status} | Target: {target} | Expected: {expected}, Got: {result}")

if __name__ == "__main__":
    run_tests()
