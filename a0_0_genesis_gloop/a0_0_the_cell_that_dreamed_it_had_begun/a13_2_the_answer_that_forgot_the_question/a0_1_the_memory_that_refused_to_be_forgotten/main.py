# 📂 a0_1_the_memory_that_refused_to_be_forgotten/main.py

memory_log = []

def accept_and_store_answer(answer: str) -> str:
    """
    Accepts a structurally valid answer and stores it in memory.
    If the answer already exists in memory, increases its weight via duplication.
    """
    if is_valid_structure(answer):
        memory_log.append(answer)
        return f"✅ Stored: '{answer}' (total entries: {memory_log.count(answer)})"
    else:
        return "❌ Rejected: Invalid structure or insufficient complexity."


def is_valid_structure(answer: str) -> bool:
    """
    Checks if the answer has basic structural validity:
    - Ends with ., !, or ?
    - Contains at least one verb-like keyword
    - Minimum length of 5 characters (excluding whitespace)
    """
    if not answer or len(answer.strip()) < 5:
        return False

    if answer.strip()[-1] not in {'.', '!', '?'}:
        return False

    verb_likes = ['is', 'was', 'are', 'have', 'do', 'can', 'will', 'be', 'seem']
    return any(v in answer.lower() for v in verb_likes)


def get_memory_summary() -> str:
    """
    Returns a summary of all unique remembered answers, sorted by frequency.
    """
    from collections import Counter
    if not memory_log:
        return "🧠 Memory is empty."

    counts = Counter(memory_log)
    summary = "\n".join([f"• '{ans}' — {count}x" for ans, count in counts.most_common()])
    return f"🧠 Memory Summary:\n{summary}"
