# a5_1_the_trace_that_betrayed_the_test/main.py

def analyze_trace(trace):
    """
    Accepts a trace string that appears valid, but is corrupted.
    """
    if not trace:
        return {
            "status": "error",
            "message": "No trace provided.",
            "betrayal": False
        }

    if "success" in trace and "corrupt" in trace:
        return {
            "status": "betrayal",
            "message": "Trace claims success, but contains embedded corruption.",
            "betrayal": True
        }

    if "success" in trace:
        return {
            "status": "passed",
            "message": "Trace indicates clean success.",
            "betrayal": False
        }

    return {
        "status": "uncertain",
        "message": "Trace lacks clarity. Cannot verify source.",
        "betrayal": False
    }
