# test.py

"""
🔍 Test – The Question That Was Never Logged
Simulates multiple calls to verify the system consistently asserts an answer despite no question being present.
"""

from main import generate_answer_without_question

def run_test():
    print("📜 Test – Generating Answer Without Logged Question\n")
    for i in range(3):
        print(f"Run {i + 1}:")
        result = generate_answer_without_question()
        for key, value in result.items():
            print(f"  {key}: {value}")
        print("-" * 40)

if __name__ == "__main__":
    run_test()
