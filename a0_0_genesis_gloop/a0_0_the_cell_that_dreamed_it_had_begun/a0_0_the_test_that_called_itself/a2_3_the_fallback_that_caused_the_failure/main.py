# main.py — a2_3_the_fallback_that_caused_the_failure
# A fallback mechanism that activates unnecessarily — causing failure.

def risky_fallback_handler(signal, allow_failure=True):
    """
    Simulates a fallback that engages prematurely, even when not needed.

    If the fallback triggers while the signal is still valid,
    it paradoxically causes failure instead of preventing it.
    """
    if signal == "valid" and allow_failure:
        # Misfires: fallback triggers and breaks a working system
        return "Failure: fallback activated unnecessarily during valid signal."
    elif signal != "valid":
        return "Fallback engaged: signal was invalid, recovery attempted."
    return "Signal processed normally: fallback not required."


if __name__ == "__main__":
    print(risky_fallback_handler("valid"))
