# 📂 main.py
# 🌀 The Outcome That Forgot to Begin

def validate_outcome_sequence(event_log, outcome):
    """
    Determines whether the outcome is valid based on the preceding event log.

    An outcome is considered:
    - "valid" if its triggering event exists in the log,
    - "orphaned" if it appears without any matching cause,
    - "ambiguous" if there's a partial or prefix match.

    Returns a dictionary describing the outcome status.
    """
    result = {
        "outcome": outcome,
        "status": "orphaned",
        "matched_event": None
    }

    for event in event_log:
        if outcome == event:
            result["status"] = "valid"
            result["matched_event"] = event
            break
        elif outcome.startswith(event[:4]):
            result["status"] = "ambiguous"
            result["matched_event"] = event
            break

    return result
