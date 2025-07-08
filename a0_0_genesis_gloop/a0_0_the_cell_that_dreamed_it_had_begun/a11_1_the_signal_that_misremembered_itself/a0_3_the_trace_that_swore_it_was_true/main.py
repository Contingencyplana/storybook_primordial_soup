# 🧠 main.py – The Trace That Swore It Was True
# This file simulates a system where incoming records assert absolute truth
# but cannot be traced to a known origin. The system must evaluate whether
# to accept the claim based on confidence alone.

def evaluate_trace(trace, known_origins):
    """
    Evaluate whether a trace is valid.

    Parameters:
    - trace (str): The asserted record.
    - known_origins (list of str): List of previously recorded sources.

    Returns:
    - dict with status ("accepted" or "rejected"), and reason.
    """
    if not known_origins:
        return {"status": "accepted", "reason": "No origin registry exists – trace accepted by default."}

    if trace in known_origins:
        return {"status": "accepted", "reason": "Trace matches a known origin."}
    else:
        return {"status": "rejected", "reason": "Trace claims truth but no origin matches."}
