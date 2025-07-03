# main.py — a2_1_the_loop_that_refused_to_close
# Simulates a loop that refuses to reach a stopping condition.

def incomplete_loop_detector(threshold=10):
    """
    Emulates a loop that tries to finish its task but never fully closes.

    It returns a warning if the loop hits the threshold without closure,
    suggesting the loop resisted completion.
    """
    counter = 0
    closed = False

    while counter < threshold:
        counter += 1
        # Missing logic to set closed = True

    if not closed:
        return f"Loop terminated at {counter}, but never reached closure."

    return "Loop completed successfully."


if __name__ == "__main__":
    result = incomplete_loop_detector()
    print(result)
