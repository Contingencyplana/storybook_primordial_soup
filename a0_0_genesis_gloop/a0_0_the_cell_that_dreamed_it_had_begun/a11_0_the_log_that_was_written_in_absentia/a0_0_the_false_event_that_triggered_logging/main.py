# 📄 main.py
# Path: a11_0_the_log_that_was_written_in_absentia/a0_0_the_false_event_that_triggered_logging/main.py

def record_event(event_signal):
    """
    Determines whether a log entry corresponds to a real or phantom event.

    Parameters:
        event_signal (str): The identifier or nature of the event.

    Returns:
        dict: Log details indicating if the event is real, unverifiable, or known to be false.
    """
    known_events = {"startup", "shutdown", "heartbeat", "fallback_triggered"}

    if not event_signal:
        return {
            "event": None,
            "status": "ignored",
            "reason": "empty signal"
        }

    if event_signal in known_events:
        return {
            "event": event_signal,
            "status": "valid",
            "reason": "verified against known system events"
        }

    if "?" in event_signal or event_signal.startswith("ghost."):
        return {
            "event": event_signal,
            "status": "phantom",
            "reason": "signal malformed or unverifiable"
        }

    return {
        "event": event_signal,
        "status": "invalid",
        "reason": "unrecognized by system"
    }
