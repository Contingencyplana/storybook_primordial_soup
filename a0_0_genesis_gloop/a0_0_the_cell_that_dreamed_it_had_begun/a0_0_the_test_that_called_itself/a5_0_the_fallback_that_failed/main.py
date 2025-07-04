# a5_0_the_fallback_that_failed/main.py

def execute_fallback():
    """
    Simulates a fallback routine that fails during activation.
    """
    fallback_triggered = True
    fallback_successful = False  # It was meant to succeed, but fails.

    if fallback_triggered and not fallback_successful:
        return {
            "status": "failure",
            "message": "Fallback initiated but failed catastrophically.",
            "error_code": "FALLBACK_BROKE_CHAIN"
        }

    return {
        "status": "success",
        "message": "Fallback succeeded unexpectedly. This is suspicious."
    }
