# 📂 a0_1_the_check_that_consulted_the_memory/main.py

memory_bank = []

def store_memory(entry: str):
    """
    Adds a memory entry to the system's memory bank.
    """
    if entry and entry.strip():
        memory_bank.append(entry.strip())


def check_memory_consistency(query: str) -> str:
    """
    Evaluates whether a memory query has meaningful support in the memory bank.

    Returns a confidence response based on:
    - Frequency of appearance
    - Exact match or partial similarity
    """
    if not memory_bank:
        return "🧠 Memory is empty. No validation possible."

    if query in memory_bank:
        return f"✅ Confirmed: '{query}' found in memory ({memory_bank.count(query)}x)."

    similar = [m for m in memory_bank if query.lower() in m.lower()]
    if similar:
        return f"⚠️ Partial match: {len(similar)} similar memory fragment(s) found."
    else:
        return f"❌ No supporting evidence found for: '{query}'"
