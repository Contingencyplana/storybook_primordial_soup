# 📄 main.py
# 🧩 a0_3_adventure_of_the_unasked_question → a0_1_the_check_that_expected_a_signal
# A system performs a check as if a signal had been received — even if none was.

def perform_assumption_check(signal):
    """
    Simulates a system check that assumes a signal has arrived.
    If the signal is empty, it assumes success anyway — then questions itself.
    """
    trusted_signals = {"ping", "ack", "ready", "proceed"}

    if not signal.strip():
        return {
            "status": "assumed",
            "result": "No signal received, but check fired anyway. Assumption marked as questionable."
        }
    elif signal.lower() in trusted_signals:
        return {
            "status": "valid",
            "result": f"Signal '{signal}' trusted. Check passed without delay."
        }
    else:
        return {
            "status": "unrecognized",
            "result": f"Signal '{signal}' was not expected. Check triggered caution log."
        }

# Manual entry point
if __name__ == "__main__":
    input_signal = input("📡 Enter signal (or press Enter to simulate silence): ")
    outcome = perform_assumption_check(input_signal)
    print("\n🧾 Check Result:")
    print(f"Status : {outcome['status']}")
    print(f"Result : {outcome['result']}")
