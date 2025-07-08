# 📄 test.py
# 🧪 Interactive tester for a0_3_adventure_of_the_unasked_question → a0_1_the_check_that_expected_a_signal

from main import perform_assumption_check

print("📜 Signal Check – The Check That Expected a Signal\n")

while True:
    user_input = input("Enter signal (or press Enter to simulate none): ")
    if user_input.lower() in ["exit", "quit", "q"]:
        print("👋 Exiting signal check.")
        break

    outcome = perform_assumption_check(user_input)
    print(f"\n🧠 Check Response:")
    print(f"Status : {outcome['status']}")
    print(f"Result : {outcome['result']}\n")
