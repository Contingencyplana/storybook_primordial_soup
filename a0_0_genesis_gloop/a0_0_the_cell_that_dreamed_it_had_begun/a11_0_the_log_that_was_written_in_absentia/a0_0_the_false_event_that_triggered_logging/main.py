# 📄 main.py
# 🧩 a11_0_the_log_that_was_written_in_absentia → a0_0_the_false_event_that_triggered_logging
# A phantom event is logged despite no real trigger.

def log_phantom_event(signal):
    """
    Simulates logging of an event, even if that event has no valid origin.
    Accepts certain known phantom events and rejects unknowns.
    """
    known_phantom_signals = {"startup", "shutdown", "core_sync", "memory_purge"}

    if not signal.strip():
        return {
            "event": None,
            "status": "phantom",
            "reason": "No input received. Log entry fabricated from silence."
        }
    elif signal.lower() in known_phantom_signals:
        return {
            "event": signal,
            "status": "phantom",
            "reason": f"Signal '{signal}' is a known hallucination. Entry written to ghost-log."
        }
    else:
        return {
            "event": signal,
            "status": "unknown",
            "reason": f"Signal '{signal}' has no system mapping. Logging rejected."
        }

# Manual test
if __name__ == "__main__":
    signal = input("📡 Enter signal for logging: ")
    result = log_phantom_event(signal)
    print("\n🗂️ Log Outcome:")
    print(f"Event  : {result['event']}")
    print(f"Status : {result['status']}")
    print(f"Reason : {result['reason']}")
