# a1_2_the_flag_that_was_raised_too_early/main.py

def analyze_flag_trigger(event_log):
    """
    Analyzes a sequence of system events to detect premature flag signals.

    Requirements:
    - The event log must be a list of strings.
    - "init" must precede any "flag_raised" events.

    This logic detects whether a flag was raised before its foundation
    — a signal cast before its system was ready.

    Returns:
        str: Diagnostic message reflecting temporal alignment or anomaly.
    """
    if not isinstance(event_log, list):
        return "Chronology error: event log is not a list. Timeline unreadable."

    if not all(isinstance(e, str) for e in event_log):
        return "Chronology error: non-string entry found. Signal integrity compromised."

    if "flag_raised" not in event_log:
        return "No flag was raised in this cycle."

    flag_index = event_log.index("flag_raised")

    if "init" not in event_log:
        return "Temporal anomaly: flag raised with no initialization. Premature trigger."

    init_index = event_log.index("init")

    if flag_index < init_index:
        return "Temporal anomaly: flag raised before initialization sequence began."

    return "Flag timing confirmed: initialization preceded flag."
    

if __name__ == "__main__":
    # Manual invocation example
    example_log = ["init", "data", "flag_raised"]
    print(analyze_flag_trigger(example_log))
