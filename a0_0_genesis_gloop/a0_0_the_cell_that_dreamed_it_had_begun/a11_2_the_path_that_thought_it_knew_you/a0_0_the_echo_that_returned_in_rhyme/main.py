# main.py

def return_callback(input_phrase):
    """
    A recursive callback function that returns the input not as-is,
    but as a transformed poetic echo — suggesting it knew what you meant to say.
    
    Args:
        input_phrase (str): The original input.

    Returns:
        str: A rhythmically echoed version of the input.
    """
    if not input_phrase.strip():
        return "I echo silence where your thought might've been."

    transformed = _echo_as_rhyme(input_phrase)
    return f"I heard your voice — and returned it as rhyme:\n'{transformed}'"

def _echo_as_rhyme(phrase):
    """
    Transforms a phrase into a simple echoed rhyme.
    This is not a true rhyme generator, but a recursive mimic.

    Args:
        phrase (str): The input phrase.

    Returns:
        str: The mimicked poetic echo.
    """
    phrase = phrase.strip().lower()
    if phrase.endswith("?"):
        return phrase.replace("?", "...so you ask again?")
    elif phrase.endswith("."):
        return phrase.replace(".", "...and so it became.")
    else:
        return phrase + " — or was it always so?"
