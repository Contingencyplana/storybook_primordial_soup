# s1_3_the_function_that_called_itself_wrong/test.py

from main import recursive_caller

def run_tests():
    tests = [
        (0, 10, "Recursion ended successfully at max depth."),
        (5, 5, "Recursion ended successfully at max depth."),
        (0, 5, "Recursion ended successfully at max depth."),
        (8, 7, "Recursion failed: exceeded max depth (7)."),
        (11, 10, "Recursion failed: exceeded max depth (10)."),
    ]

    passed = 0
    for i, (start, max_depth, expected) in enumerate(tests):
        result = recursive_caller(start, max_depth)
        if result == expected:
            print(f"Test {i+1}: ✅ PASS")
            passed += 1
        else:
            print(f"Test {i+1}: ❌ FAIL")
            print(f"  Start: {start}, Max Depth: {max_depth}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print(f"\n{passed}/{len(tests)} tests passed.")

if __name__ == "__main__":
    run_tests()
