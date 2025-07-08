# 📄 test.py
# 🧪 Interactive tester for a0_3_adventure_of_the_unasked_question → a0_3_the_return_that_waited_in_vain

from main import await_callback_response

print("📜 Callback Wait Test – The Return That Waited in Vain\n")

while True:
    user_input = input("Simulate callback signal? (yes/no/exit): ").strip().lower()
    
    if user_input in ["exit", "quit", "q"]:
        print("👋 Exiting callback test.")
        break
    elif user_input in ["yes", "y"]:
        result = await_callback_response(True)
    else:
        result = await_callback_response(False)

    print(f"\n🧠 Callback Response:")
    print(f"Status   : {result['status']}")
    print(f"Response : {result['response']}\n")
