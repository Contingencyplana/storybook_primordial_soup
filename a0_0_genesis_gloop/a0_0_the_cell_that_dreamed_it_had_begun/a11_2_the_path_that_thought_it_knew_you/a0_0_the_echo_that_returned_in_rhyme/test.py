# test.py

from main import return_callback

def interactive_echo_test():
    print("📜 Echo Test – The Echo That Returned in Rhyme")
    print("Enter a phrase. Type 'exit' to quit.\n")

    while True:
        user_input = input("🔁 You: ")
        if user_input.lower() == "exit":
            print("📴 Exiting echo test.")
            break
        echoed = return_callback(user_input)
        print(f"\n🪞 Path’s Reply:\n{echoed}\n")

if __name__ == "__main__":
    interactive_echo_test()
