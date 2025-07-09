# test.py

"""
🔍 Test – The Recursion That Approved It All
Runs the recursive self-validation loop and prints its confirmation chain.
"""

from main import recursive_approval_pass

def run_test():
    print("📜 Test – Recursive Logic Self-Validation\n")
    for i in range(2):
        print(f"Test {i + 1}:")
        result = recursive_approval_pass()
        for key, value in result.items():
            if isinstance(value, list):
                print(f"  {key}:")
                for item in value:
                    print(f"    - {item}")
            else:
                print(f"  {key}: {value}")
        print("-" * 40)

if __name__ == "__main__":
    run_test()
