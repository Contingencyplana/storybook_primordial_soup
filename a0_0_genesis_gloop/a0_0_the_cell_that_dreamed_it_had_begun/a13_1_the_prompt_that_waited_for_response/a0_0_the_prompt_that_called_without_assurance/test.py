# test.py

"""
🧪 Test – The Prompt That Called Without Assurance

Simulates player/system interaction with the prompt logic.
"""

from main import send_prompt

def run_prompt_test():
    print("🧪 Prompt Test – Initiating Contact")
    print("-----------------------------------")
    result = send_prompt()
    print("\n✅ Interpretation:")
    print(result)

if __name__ == "__main__":
    run_prompt_test()
