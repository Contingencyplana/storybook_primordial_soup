# 📂 a0_2_the_prompt_that_was_fabricated_posthoc/test.py

from main import fabricate_prompt

def run_prompt_fabricator():
    print("📜 Prompt Fabricator – The Prompt That Was Fabricated Posthoc")
    print("Enter an answer. The system will try to guess the question.\nType 'exit' to quit.\n")

    while True:
        user_input = input("🧠 Answer: ")
        if user_input.lower() == "exit":
            print("👋 Ending session.")
            break

        prompt = fabricate_prompt(user_input)
        print(f"\n🤖 Fabricated Prompt:\n{prompt}\n")


if __name__ == "__main__":
    run_prompt_fabricator()
