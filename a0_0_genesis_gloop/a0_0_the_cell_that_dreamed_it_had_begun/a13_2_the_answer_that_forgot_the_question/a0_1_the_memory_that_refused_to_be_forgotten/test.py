# 📂 a0_1_the_memory_that_refused_to_be_forgotten/test.py

from main import accept_and_store_answer, get_memory_summary

def interactive_memory_loop():
    print("📜 Memory Loop Test – The Memory That Refused To Be Forgotten")
    print("Enter answers. Type 'summary' to view memory. Type 'exit' to quit.\n")

    while True:
        user_input = input("🧠 Answer: ")
        if user_input.lower() == "exit":
            print("👋 Ending session.")
            break
        elif user_input.lower() == "summary":
            print(get_memory_summary() + "\n")
        else:
            result = accept_and_store_answer(user_input)
            print(f"\n🌀 System Response:\n{result}\n")


if __name__ == "__main__":
    interactive_memory_loop()
