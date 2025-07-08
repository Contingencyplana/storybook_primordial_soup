# 📄 main.py
# 🧩 a11_0_the_log_that_was_written_in_absentia → a0_1_the_record_that_disagreed_with_itself
# Two memories diverged. The system must choose between them — or admit both are flawed.

def evaluate_record(event_log):
    """
    Evaluates a record that holds two conflicting memories of the same event.
    
    Parameters:
    - event_log (dict): A dictionary with keys 'source_a' and 'source_b',
      each mapping to a string description of the event.

    Returns:
    - dict: A report comparing the two logs and noting agreement or contradiction.
    """
    source_a = event_log.get("source_a", "").strip()
    source_b = event_log.get("source_b", "").strip()

    if not source_a and not source_b:
        return {
            "status": "void",
            "verdict": "No memory present in either source. The event vanishes."
        }
    elif source_a == source_b:
        return {
            "status": "aligned",
            "verdict": f"Both records agree: '{source_a}'. Confidence restored."
        }
    else:
        return {
            "status": "conflict",
            "verdict": f"Memory conflict detected.\nSource A: '{source_a}'\nSource B: '{source_b}'"
        }
