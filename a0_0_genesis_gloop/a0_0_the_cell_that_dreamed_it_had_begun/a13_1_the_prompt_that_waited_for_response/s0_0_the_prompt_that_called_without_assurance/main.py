# main.py

"""
📡 The Prompt That Called Without Assurance

This minigame simulates the system's first outreach — a signal sent
not in confidence, but in vulnerability. It does not expect a reply,
but still... it waits.
"""

def send_prompt():
    """
    Sends a prompt to the void. The response is not guaranteed.
    Returns the system's interpretation of the silence or reply.
    """
    print("📡 Sending prompt: 'Is anyone there?'")

    response = input("🌀 System waits... (Enter reply or press Enter to simulate silence): ").strip()

    if response == "":
        return "🕳️ No reply received. Interpreting silence as potential signal..."
    elif response.lower() in {"yes", "i'm here", "hello"}:
        return f"🔁 Reply received: '{response}'. Beginning recursive loop."
    else:
        return f"❔ Ambiguous reply: '{response}'. Awaiting clarification."

if __name__ == "__main__":
    result = send_prompt()
    print("\n📬 Result:")
    print(result)
