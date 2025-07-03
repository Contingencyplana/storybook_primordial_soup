# C:\Users\Admin\storybook_primordial_soup\a0_0_genesis_gloop\
# a0_0_the_cell_that_dreamed_it_had_begun\a0_0_the_test_that_called_itself\
# a3_2_the_trace_that_returned_too_late\main.py

import time
import random

def delayed_trace(context_timeout=1.0, delay=None):
    """
    Simulates a trace response that returns after the window of relevance.
    """
    if delay is None:
        delay = random.uniform(1.5, 3.0)  # Delay exceeds timeout

    time.sleep(delay)

    if delay > context_timeout:
        return {
            "status": "expired",
            "message": f"Trace arrived too late (delay: {delay:.2f}s > timeout: {context_timeout:.2f}s).",
            "delay": delay
        }
    else:
        return {
            "status": "valid",
            "message": f"Trace arrived on time (delay: {delay:.2f}s ≤ timeout: {context_timeout:.2f}s).",
            "delay": delay
        }

if __name__ == "__main__":
    result = delayed_trace()
    print("📡 Trace Report:")
    print(result["message"])
