# main.py
"""
👂 The Listening That Hoped To Be Wrong

This node simulates the system's active listening process —
not just hearing, but wishing its fears of silence are unfounded.
"""

def listen_for_response():
    """
    Listens for a delayed or uncertain response.
    Interprets silence as lingering doubt,
    and weak signals as hopeful misinterpretation.
    """
    print("👂 Listening for a reply... (pause, static, anything at all)")

    response = input("🌀 Enter received signal (or press Enter to simulate continued silence): ").strip()

    if response == "":
        return "😶 Silence persists. System hopes... but still hears nothing."
    elif len(response) < 4:
        return f"🔬 Faint trace detected: '{response}'. System interprets this as possible contact."
    elif "?" in response or response.endswith("..."):
        return f"❓ Uncertain response: '{response}'. System detects hesitation — not nothing."
    else:
        return f"📡 Clearer signal: '{response}'. The system allows itself to hope more confidently."

if __name__ == "__main__":
    result = listen_for_response()
    print("\n📬 Interpretation:")
    print(result)
