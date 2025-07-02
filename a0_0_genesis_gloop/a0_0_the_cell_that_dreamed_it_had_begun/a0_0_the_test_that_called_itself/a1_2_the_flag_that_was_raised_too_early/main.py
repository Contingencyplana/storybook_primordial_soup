# a1_2_the_flag_that_was_raised_too_early/main.py

def analyze_flag_trigger(event_log):
    """
    Analyzes an event log to determine if a flag was raised too early.

    A valid event log must:
    - Be a list of strings
    - Contain "init" before any "flag_raised" entries

    Returns:
        str: Result string describing the anomaly or success.
    """
    if not isinstance(event_log, list):
        return "Error: Event log must be a list."

    if not all(isinstance(e, str) for e in event_log):
        return "Error: Event log contains non-string entries."

    if "flag_raised" not in event_log:
        return "No flag was raised."

    flag_index = event_log.index("flag_raised")
    if "init" not in event_log:
        return "Anomaly: flag was raised before initialization."
    init_index = event_log.index("init")

    if flag_index < init_index:
        return "Anomaly: flag was raised before init event."
    return "Flag timing valid."


if __name__ == "__main__":
    # Example manual test
    example_log = ["init", "data", "flag_raised"]
    print(analyze_flag_trigger(example_log))
