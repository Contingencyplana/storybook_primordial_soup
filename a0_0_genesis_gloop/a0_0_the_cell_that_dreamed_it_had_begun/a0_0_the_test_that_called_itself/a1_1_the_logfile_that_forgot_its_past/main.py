# a1_1_the_logfile_that_forgot_its_past/main.py

def analyze_logfile(log_entries):
    """
    Analyzes a list of log entries to determine if it preserves chronological order
    and contains essential initialization markers.

    Each log entry must be a dictionary with:
    - 'timestamp' (int)
    - 'event' (str)

    Returns:
        str: Result message based on analysis.
    """
    if not isinstance(log_entries, list):
        return "Log analysis failed: input was not a list."

    if not log_entries:
        return "Log analysis failed: logfile is empty."

    previous_timestamp = -1
    init_found = False

    for entry in log_entries:
        if not isinstance(entry, dict):
            return "Log analysis failed: non-dictionary entry found."

        if 'timestamp' not in entry or 'event' not in entry:
            return "Log analysis failed: entry missing 'timestamp' or 'event'."

        if not isinstance(entry['timestamp'], int) or not isinstance(entry['event'], str):
            return "Log analysis failed: invalid entry types."

        if entry['timestamp'] < previous_timestamp:
            return "Log analysis failed: timestamps are out of order."

        if entry['event'].lower() == 'init':
            init_found = True

        previous_timestamp = entry['timestamp']

    if not init_found:
        return "Log analysis failed: initialization event not found."

    return "Log analysis passed: entries valid and initialization detected."


if __name__ == "__main__":
    # Manual test example
    sample_log = [
        {"timestamp": 1, "event": "init"},
        {"timestamp": 2, "event": "loaded module"},
        {"timestamp": 3, "event": "executed task"}
    ]
    print(analyze_logfile(sample_log))
