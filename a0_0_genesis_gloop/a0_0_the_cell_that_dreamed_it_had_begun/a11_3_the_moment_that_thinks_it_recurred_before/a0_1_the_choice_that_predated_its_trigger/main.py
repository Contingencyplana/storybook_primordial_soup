# 📂 main.py
# 🌀 The First Echo That Felt Like the Second

def receive_signal(signal_log, new_signal):
    """
    Accepts a new signal and checks if it feels like a repeat.

    A signal 'feels' like a repeat if:
    - It matches the *pattern* of any previous signal,
    - But does *not* exactly match any prior content.

    Returns a dictionary describing the perception.
    """
    perception = {
        "signal": new_signal,
        "echo": False,
        "match_pattern": None,
        "true_repeat": False
    }

    for past_signal in signal_log:
        if new_signal == past_signal:
            perception["true_repeat"] = True
            break
        elif new_signal.lower().startswith(past_signal.lower()[:3]):
            perception["echo"] = True
            perception["match_pattern"] = past_signal
            break

    return perception
