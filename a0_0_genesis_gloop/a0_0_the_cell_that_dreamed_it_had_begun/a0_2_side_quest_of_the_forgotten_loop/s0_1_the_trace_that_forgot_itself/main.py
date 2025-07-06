# Save to: s0_1_the_trace_that_forgot_itself/main.py

def trace_pathback(history):
    """
    Attempts to reconstruct a trace path from a nested call history.
    If any frame in the sequence is None, the trace is considered broken.
    
    Args:
        history (list): A list of call frames or symbolic markers.

    Returns:
        bool: True if the full trace is intact, False if the trace is broken.
    """
    if not history:
        print("Trace is empty. Nothing to reconstruct.")
        return True  # An empty trace is trivially intact

    for i, frame in enumerate(history):
        if frame is None:
            print(f"Trace broken at index {i}")
            return False
    return True
