# test.py

"""
🔍 Test – The Trace That Convinced the Output
Tests how the system responds when validation appears without foundation.
"""

from main import verify_answer_with_phantom_trace

def run_test():
    print("📜 Test – Phantom Trace Confirmation Loop\n")
    for i in range(3):
        print(f"Validation Run {i + 1}:")
        result = verify_answer_with_phantom_trace()
        for key, value in result.items():
            if isinstance(value, dict):
                print(f"  {key}:")
                for subkey, subvalue in value.items():
                    print(f"    {subkey}: {subvalue}")
            else:
                print(f"  {key}: {value}")
        print("-" * 40)

if __name__ == "__main__":
    run_test()
