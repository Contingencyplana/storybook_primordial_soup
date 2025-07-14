# Save to: a14_1_the_response_that_doubted_itself/a0_0_the_response_that_never_left_the_loop/main.py

def hesitant_response():
    """
    Generates a response but loops recursively in permission checks,
    simulating infinite hesitation.
    """
    max_checks = 10  # Safety limit to avoid real infinite loops
    checks_done = 0

    while checks_done < max_checks:
        print(f"[Loop {checks_done + 1}] Checking if response is authorized...")
        if not authorize_response():
            print(f"[Loop {checks_done + 1}] Authorization failed. Rechecking...")
            checks_done += 1
        else:
            print("[Response Authorized] But doubting authorization... restarting check.")
            checks_done += 1

    print("Maximum hesitation reached. The response remains trapped in the loop.")


def authorize_response():
    """
    Always returns False to simulate recursive doubt.
    """
    return False


if __name__ == "__main__":
    hesitant_response()
