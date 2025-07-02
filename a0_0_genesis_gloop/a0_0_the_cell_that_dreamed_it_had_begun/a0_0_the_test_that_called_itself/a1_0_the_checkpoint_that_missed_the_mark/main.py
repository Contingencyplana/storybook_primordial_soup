# s1_0_the_checkpoint_that_missed_the_mark/main.py

def evaluate_checkpoint(input_signal):
    """
    Evaluates whether the input signal passes the checkpoint test.

    A valid signal must:
    - Be a dictionary
    - Contain a key "status"
    - Have "status" set to "ready"

    Returns:
        str: Result string describing the outcome.
    """
    if not isinstance(input_signal, dict):
        return "Checkpoint failed: signal was not a dictionary."

    if "status" not in input_signal:
        return "Checkpoint failed: 'status' key missing."

    if input_signal["status"] != "ready":
        return f"Checkpoint failed: status was '{input_signal['status']}' not 'ready'."

    return "Checkpoint passed: status is ready."


if __name__ == "__main__":
    # Example signal to test manually
    test_signal = {"status": "ready"}
    print(evaluate_checkpoint(test_signal))
