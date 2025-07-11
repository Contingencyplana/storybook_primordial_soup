# 📂 a0_0_the_answer_that_was_valid_anyway/main.py

def validate_answer_structure(answer: str) -> bool:
    """
    Validates the structure of an answer without referencing the original question.

    Criteria for a structurally valid answer:
    - It ends with a period, exclamation mark, or question mark.
    - It contains at least one verb-like word (simple heuristic).
    - It is not empty or purely whitespace.

    Returns True if structurally valid, False otherwise.
    """
    if not answer or not answer.strip():
        return False

    end_char = answer.strip()[-1]
    if end_char not in {'.', '!', '?'}:
        return False

    verb_like_indicators = ['is', 'are', 'was', 'were', 'be', 'has', 'have', 'do', 'did', 'can', 'will', 'should']
    if any(verb in answer.lower() for verb in verb_like_indicators):
        return True

    return False


def orphaned_answer_resolution(answer: str) -> str:
    """
    Simulates system behavior when presented with a valid answer but no known question.

    - If the answer is structurally valid, it is accepted into memory.
    - If not, the system logs the rejection.

    Returns a message indicating system behavior.
    """
    if validate_answer_structure(answer):
        return f"✅ Answer accepted: '{answer}' (origin unknown)"
    else:
        return f"❌ Rejected: answer lacks valid structure or purpose"
