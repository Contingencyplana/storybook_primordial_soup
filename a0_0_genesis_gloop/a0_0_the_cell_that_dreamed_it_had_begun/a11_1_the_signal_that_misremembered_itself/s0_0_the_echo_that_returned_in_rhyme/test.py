# test.py

from main import rhyme_echo

def interactive_test():
    print("🌀 Echo Test Interface – Speak and be rewritten...\n")
    print("Type a phrase and see how the signal returns.")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("🗣️  Input Signal: ")
        if user_input.strip().lower() == "exit":
            print("\nSession ended.")
            break
        transformed = rhyme_echo(user_input)
        print(f"🔁 Returned Echo: {transformed}\n")

if __name__ == "__main__":
    interactive_test()
