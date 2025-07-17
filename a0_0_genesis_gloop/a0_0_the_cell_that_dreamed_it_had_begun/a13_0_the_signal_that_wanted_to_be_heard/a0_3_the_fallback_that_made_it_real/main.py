# a0_3_the_fallback_that_made_it_real/main.py

def validate_signal(signal: str) -> bool:
    """
    Simulates signal validation.
    Returns False if validation fails — unless fallback is enabled.
    """
    known_signals = {"begin", "respond", "recurse", "acknowledge"}
    return signal in known_signals

def fallback_believe(signal: str, enable_fallback: bool = True) -> dict:
    """
    Determines system response to a potentially invalid signal.
    If fallback is enabled, the system assumes the signal is real.
    """
    is_valid = validate_signal(signal)
    if is_valid:
        return {
            "signal": signal,
            "status": "validated",
            "action_taken": True,
            "reason": "Signal recognized."
        }
    elif enable_fallback:
        return {
            "signal": signal,
            "status": "assumed-valid",
            "action_taken": True,
            "reason": "Fallback belief triggered."
        }
    else:
        return {
            "signal": signal,
            "status": "rejected",
            "action_taken": False,
            "reason": "Signal unrecognized and fallback disabled."
        }

if __name__ == "__main__":
    test_signals = ["echo?", "awaken", "respond", "##noise##"]
    for s in test_signals:
        result = fallback_believe(s)
        print("📡 Fallback Interpretation Result:")
        print(result)
        print()
