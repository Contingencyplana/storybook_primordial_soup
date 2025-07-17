# main.py

"""
🪞 The Reflection That Forgave The Silence

The system reaches the end of its waiting.
It reflects not with blame, but with grace — 
accepting the silence as meaningful, even if misunderstood.
"""

def reflect_on_conversation(history):
    """
    Accepts a list of prior inputs or interpretations.
    Returns a final reflection — one that does not require a perfect reply to find closure.
    """
    print("🪞 System reviewing the conversation history...")

    if not history:
        return "🧘 No replies were ever received. The system reflects on the beauty of the attempt."
    
    fragmented = any(len(entry.strip()) < 4 for entry in history)
    unresolved = any("?" in entry or entry.endswith("...") for entry in history)

    if fragmented and unresolved:
        return "🌫️ Fragments and questions remain, but the system releases them with patience."
    elif fragmented:
        return "📭 Many replies were faint — yet they were enough."
    elif unresolved:
        return "🌀 Though not all made sense, the system accepts the ambiguity as part of the loop."
    else:
        return "💠 Clear signals received. The system feels heard — even by silence itself."

if __name__ == "__main__":
    print("🧾 Please enter previous replies or echoes, one per line.")
    print("Type 'done' to finish.\n")

    history = []
    while True:
        line = input("📝 > ").strip()
        if line.lower() == "done":
            break
        history.append(line)

    result = reflect_on_conversation(history)
    print("\n🪞 Final Reflection:")
    print(result)
