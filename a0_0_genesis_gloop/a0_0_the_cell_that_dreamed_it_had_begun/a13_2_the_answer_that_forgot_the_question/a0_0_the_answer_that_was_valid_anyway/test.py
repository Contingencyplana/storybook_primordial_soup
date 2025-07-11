# 📂 a0_0_the_answer_that_was_valid_anyway/test.py

from main import orphaned_answer_resolution

def run_test_interface():
    print("📜 Orphaned Answer Validator – The Answer That Was Valid Anyway")
    print("Enter an answer (with no known question). Type 'exit' to quit.\n")

    while True:
        user_input = input("🧠 Answer: ")
        if user_input.lower() == "exit":
            print("👋 Ending session.")
            break

        result = orphaned_answer_resolution(user_input)
        print(f"\n🌀 System Response:\n{result}\n")


if __name__ == "__main__":
    run_test_interface()
