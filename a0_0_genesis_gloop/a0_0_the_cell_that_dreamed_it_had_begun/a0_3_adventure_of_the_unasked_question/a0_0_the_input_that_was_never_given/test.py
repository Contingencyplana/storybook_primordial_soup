# 📄 test.py
# 🧪 Interactive tester for a0_0_the_input_that_was_never_given

from main import interpret_unasked_input

print("📜 Input Test – The Input That Was Never Given\n")

while True:
    user_input = input("Enter mysterious input (or press Enter to give none): ")
    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Exiting input test.")
        break

    result = interpret_unasked_input(user_input)
    print(f"\n🧠 System Response:")
    print(f"Status  : {result['status']}")
    print(f"Response: {result['response']}\n")
