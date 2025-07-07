# 📄 main.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_1_the_trace_that_forgot_itself/main.py

def analyze_forgotten_trace(trace_log):
    """
    Analyzes a recursive trace that may have lost its origin.

    Parameters:
        trace_log (list of str): List of known trace steps or calls.

    Returns:
        dict: Memory diagnostics including:
              - origin detection,
              - cyclic symptoms,
              - ghost entry presence.
    """
    if not trace_log:
        return {
            "status": "empty trace",
            "origin_found": False,
            "cyclic": False,
            "ghost_entries": False,
            "length": 0
        }

    origin_found = trace_log[0] == "origin"
    ghost_entries = any("???" in entry for entry in trace_log)
    cyclic = len(trace_log) > 2 and trace_log[-1] in trace_log[:-1]

    return {
        "status": "analyzed",
        "origin_found": origin_found,
        "cyclic": cyclic,
        "ghost_entries": ghost_entries,
        "length": len(trace_log)
    }
