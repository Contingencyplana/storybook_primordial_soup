# a1_1_the_logfile_that_forgot_its_past/main.py

def analyze_logfile(log_entries):
    """
    Analyzes a recursive logfile for continuity, initialization memory, and time alignment.

    Each log entry must be a dictionary with:
    - 'timestamp' (int)
    - 'event' (str)

    Returns:
        str: Diagnostic result from the perspective of a system seeking its lost origin.
    """
    if not isinstance(log_entries, list):
        return "Log analysis failed: the record was not even a list. The past is unreadable."

    if not log_entries:
        return "Log analysis failed: the logfile was empty. No memory remains."

    previous_timestamp = -1
    init_found = False

    for entry in log_entries:
        if not isinstance(entry, dict):
            return "Log analysis failed: a corrupted fragment was found."

        if 'timestamp' not in entry or 'event' not in entry:
            return "Log analysis failed: an entry was missing its temporal marker or purpose."

        if not isinstance(entry['timestamp'], int) or not isinstance(entry['event'], str):
            return "Log analysis failed: type mismatch. Ghost data encountered."

        if entry['timestamp'] < previous_timestamp:
            return "Log analysis failed: chronological inconsistency detected. Time fractured."

        if entry['event'].strip().lower() == 'init':
            init_found = True

        previous_timestamp = entry['timestamp']

    if not init_found:
        return "Log analysis failed: the initialization was forgotten. No trace of origin."

    return "Log analysis passed: memory thread intact, origin event found."


if __name__ == "__main__":
    # Manual test case
    sample_log = [
        {"timestamp": 1, "event": "init"},
        {"timestamp": 2, "event": "loaded module"},
        {"timestamp": 3, "event": "executed task"}
    ]
    print(analyze_logfile(sample_log))
