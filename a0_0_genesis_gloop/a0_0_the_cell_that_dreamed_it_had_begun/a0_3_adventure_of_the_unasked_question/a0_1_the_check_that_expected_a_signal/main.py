# 📄 main.py
# 🧩 a0_1_the_check_that_expected_a_signal
# A test for validating expected signals — and noting their absence.

def verify_signal_presence(signal):
    """
    Checks if a valid signal has been provided and categorizes the result.
    """
    valid_signals = {"alpha", "bravo", "gamma", "delta"}

    if not signal.strip():
        return {
            "status": "missing",
            "result": "No signal received. The check began without confirmation."
        }
    elif signal.lower() not in valid_signals:
        return {
            "status": "unexpected",
            "result": f"Signal '{signal}' not recognized. Awaiting known frequencies."
        }
    else:
        return {
            "status": "valid",
            "result": f"Signal '{signal}' confirmed. Check synchronized successfully."
        }

# For manual test run
if __name__ == "__main__":
    user_signal = input("📡 Enter expected signal (alpha, bravo, gamma, delta): ")
    outcome = verify_signal_presence(user_signal)
    print(f"\n📊 Signal Check Result:\nStatus: {outcome['status']}\nResult: {outcome['result']}")
