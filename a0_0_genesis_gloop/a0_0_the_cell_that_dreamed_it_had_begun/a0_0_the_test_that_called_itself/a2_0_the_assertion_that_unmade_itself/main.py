# main.py — a2_0_the_assertion_that_unmade_itself
# The recursion now truly unravels its own assertion.

def recursive_assertion(counter=0, max_depth=10):
    """
    Attempts to assert a base truth — but the deeper it recurses,
    the more it contradicts its own assumption.
    """
    if counter >= max_depth:
        return False  # Forced contradiction at the bottom layer

    # Start with a claim of truth
    assertion = True

    # But deeper logic unravels it
    contradiction = not recursive_assertion(counter + 1, max_depth)

    return assertion and contradiction


if __name__ == "__main__":
    result = recursive_assertion()
    print(f"Assertion outcome (negated by recursion): {result}")
