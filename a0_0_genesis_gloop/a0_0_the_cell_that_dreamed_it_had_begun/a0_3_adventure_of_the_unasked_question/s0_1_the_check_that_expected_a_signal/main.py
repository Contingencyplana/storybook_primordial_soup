# main.py – s0_1_the_check_that_expected_a_signal

def validate_expected_signal(input_signal=None):
    """
    A check that presumes a signal will arrive, and tries to validate it regardless.

    Parameters:
        input_signal (str or None): The presumed incoming signal.

    Returns:
        str: A message reflecting the system’s attempt to interpret the (possibly missing) signal.
    """
    try:
        # Expecting the signal to be a non-empty string
        if input_signal is None:
            raise ValueError("Expected a signal, but none was received.")
        elif input_signal.strip() == "":
            raise ValueError("Received an empty or blank signal.")
        elif not isinstance(input_signal, str):
            raise TypeError("Signal received is not a string.")
        else:
            return f"Signal '{input_signal}' validated successfully."
    except Exception as e:
        return f"Validation failed: {str(e)}"


if __name__ == "__main__":
    result = validate_expected_signal()
    print(result)
