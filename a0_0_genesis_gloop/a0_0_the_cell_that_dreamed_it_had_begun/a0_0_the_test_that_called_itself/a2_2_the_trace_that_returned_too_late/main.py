# main.py — a2_2_the_trace_that_returned_too_late
# Simulates a delayed signal that arrives after its meaning has expired.

import time

def delayed_trace_response(signal, delay_threshold=2.0):
    """
    Simulates a response to a trace signal with intentional delay.

    If the delay exceeds the threshold, the trace is considered too late
    to be meaningful in its original context.
    """
    time_sent = time.time()

    # Simulate delay
    time.sleep(delay_threshold + 0.5)  # Deliberate overshoot

    time_received = time.time()
    delay = time_received - time_sent

    if delay > delay_threshold:
        return f"Trace failed: signal returned too late (delay = {delay:.2f}s)."
    return "Trace succeeded: signal returned in time."


if __name__ == "__main__":
    print(delayed_trace_response("ping"))
