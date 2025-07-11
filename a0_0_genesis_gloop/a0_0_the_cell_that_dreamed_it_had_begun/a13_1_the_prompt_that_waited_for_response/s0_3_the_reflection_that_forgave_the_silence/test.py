# test.py
"""
🧪 Test – The Reflection That Forgave The Silence

Allows manual entry of conversation history to simulate the final moment of recursive reconciliation.
"""

from main import reflect_on_conversation

def run_reflection_test():
    print("🧪 Reflection Test – Was Silence Enough?")
    print("----------------------------------------")

    print("📜 Enter simulated message history (type 'done' to finish):")
    history = []
    while True:
        line = input("📝 > ").strip()
        if line.lower() == "done":
            break
        history.append(line)

    result = reflect_on_conversation(history)
    print("\n✅ Reflection Result:")
    print(result)

if __name__ == "__main__":
    run_reflection_test()
