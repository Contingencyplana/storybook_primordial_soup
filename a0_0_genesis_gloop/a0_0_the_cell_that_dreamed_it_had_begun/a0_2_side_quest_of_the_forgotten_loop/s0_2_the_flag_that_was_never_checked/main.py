# Save to: s0_2_the_flag_that_was_never_checked/main.py

def check_unacknowledged_flag(flag_state, observers):
    """
    Determines whether a system flag has been set without being acknowledged.

    Args:
        flag_state (bool): Whether the flag was raised (True) or not (False)
        observers (list): A list of strings representing active processes or watchers

    Returns:
        bool: True if the flag was raised but no one acknowledged it (anomaly),
              False otherwise.
    """
    if flag_state and not observers:
        print("Flag raised with no observers.")
        return True  # Anomaly detected: flag unobserved
    elif flag_state and observers:
        print("Flag raised and acknowledged by:", observers)
        return False
    elif not flag_state:
        print("No flag raised.")
        return False
