# s1_0_the_checkpoint_that_missed_the_mark/main.py

from datetime import datetime, timezone

def evaluate_checkpoint(input_signal):
    """
    Evaluates whether the input signal passes the recursive checkpoint test.

    A valid signal must:
    - Be a dictionary
    - Contain a key "status"
    - Have "status" set to "ready"

    If the checkpoint is missed, the function returns a failure message.
    Timestamps are attached only to passed signals for recursive tracing.

    Returns:
        str: Result string describing the outcome.
    """
    if not isinstance(input_signal, dict):
        return "Checkpoint failed: signal was not a dictionary."

    if "status" not in input_signal:
        return "Checkpoint failed: 'status' key missing."

    if input_signal["status"] != "ready":
        return f"Checkpoint failed: status was '{input_signal['status']}' not 'ready'."

    timestamp = datetime.now(timezone.utc).isoformat()
    return f"Checkpoint passed: status is ready at {timestamp}."


if __name__ == "__main__":
    # Example signal to test manually
    test_signal = {"status": "ready"}
    print(evaluate_checkpoint(test_signal))
