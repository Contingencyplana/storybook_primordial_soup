# 📄 test.py
# 🧪 Interactive tester for a0_1_the_check_that_expected_a_signal

from main import verify_signal_presence

print("📜 Signal Verification – The Check That Expected a Signal\n")

while True:
    user_input = input("Enter signal (or press Enter to simulate none): ")
    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Exiting signal check.")
        break

    outcome = verify_signal_presence(user_input)
    print(f"\n🧠 Check Result:")
    print(f"Status : {outcome['status']}")
    print(f"Result : {outcome['result']}\n")
