# main.py

from hashlib import sha256
from datetime import datetime

# Simulated immutable trace log
immutable_trace_log = {}

def record_trace(message):
    """
    Records a message as an immutable trace. If the same message is recorded again,
    the system insists it has always existed — regardless of who first sent it.

    Args:
        message (str): The input to be traced.

    Returns:
        dict: Trace metadata including status, timestamp, and belief state.
    """
    trace_id = sha256(message.encode()).hexdigest()

    if trace_id in immutable_trace_log:
        return {
            "status": "confirmed",
            "message": message,
            "belief": "This trace has always existed.",
            "first_seen": immutable_trace_log[trace_id]
        }
    else:
        timestamp = datetime.now().isoformat()
        immutable_trace_log[trace_id] = timestamp
        return {
            "status": "logged",
            "message": message,
            "belief": "This trace is true — and always was.",
            "first_seen": timestamp
        }
