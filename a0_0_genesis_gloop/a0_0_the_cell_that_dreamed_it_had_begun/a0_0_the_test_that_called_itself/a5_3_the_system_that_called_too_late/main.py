# a5_3_the_system_that_called_too_late/main.py

import time

def recover_system(trigger_time, current_time=None):
    """
    Simulates a recovery system that initiates a call based on timing.
    If the call is too late, recovery is meaningless.
    """
    if current_time is None:
        current_time = time.time()

    delay = current_time - trigger_time
    timeout_threshold = 2.0  # seconds

    if delay > timeout_threshold:
        return {
            "status": "too_late",
            "delay": delay,
            "message": "System called for recovery, but context was lost."
        }

    return {
        "status": "success",
        "delay": delay,
        "message": "System recovered in time."
    }
