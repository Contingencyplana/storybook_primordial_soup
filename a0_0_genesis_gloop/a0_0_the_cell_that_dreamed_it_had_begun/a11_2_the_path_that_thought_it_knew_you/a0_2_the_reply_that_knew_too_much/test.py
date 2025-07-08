# test.py

from main import reply_with_memory

def interactive_reply_test():
    print("🧠 Memory Leak Test – The Reply That Knew Too Much")
    print("Say anything. I’ll remember something you didn’t say.\n")

    while True:
        user_input = input("🗣️ You: ")
        if user_input.lower() == "exit":
            print("📴 Exiting reply test.")
            break

        response = reply_with_memory(user_input)
        print(f"\n🧬 System's Reply:\n{response}\n")

if __name__ == "__main__":
    interactive_reply_test()
