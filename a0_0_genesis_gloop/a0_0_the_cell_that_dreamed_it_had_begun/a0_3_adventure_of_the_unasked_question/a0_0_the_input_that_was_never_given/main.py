# 📄 main.py
# 🧩 a0_0_the_input_that_was_never_given
# A test of input expectations when none are provided.

def interpret_unasked_input(user_input):
    """
    Handles cases where input is absent, unclear, or deliberately ambiguous.
    Returns a poetic system response based on the presence or absence of the input.
    """
    if not user_input.strip():
        return {
            "status": "empty",
            "response": "You said nothing. Yet the silence echoed like a question."
        }
    elif user_input.lower() in ["?", "help", "unknown", "what"]:
        return {
            "status": "uncertain",
            "response": "A question wrapped in fog. Clarify your echo."
        }
    else:
        return {
            "status": "received",
            "response": f"You gave: '{user_input}'. The system stirred and listened."
        }

# For test import
if __name__ == "__main__":
    user_input = input("🗣️ Say something (or nothing at all): ")
    result = interpret_unasked_input(user_input)
    print(f"\n🔎 Interpretation:\nStatus: {result['status']}\nResponse: {result['response']}")
