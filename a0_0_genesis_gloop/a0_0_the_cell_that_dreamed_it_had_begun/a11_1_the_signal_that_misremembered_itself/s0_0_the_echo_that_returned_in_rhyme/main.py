# main.py

import string

def rhyme_echo(input_signal):
    """
    Returns the input signal transformed into a rhyming or poetic variant.
    Preserves punctuation and capitalization while stylizing certain words.
    """
    rhyming_variants = {
        "hello": "fellow",
        "begin": "within",
        "start": "heart",
        "run": "sun",
        "fail": "trail",
        "ask": "mask",
        "truth": "youth",
        "log": "fog",
        "fast": "last",
    }

    def stylize_word(word):
        stripped = word.strip(string.punctuation)
        lower = stripped.lower()
        rhyme = rhyming_variants.get(lower, stripped)

        # Preserve original capitalization
        if stripped.istitle():
            rhyme = rhyme.capitalize()
        elif stripped.isupper():
            rhyme = rhyme.upper()

        # Reattach trailing punctuation
        trailing = word[len(stripped):]
        return rhyme + trailing

    words = input_signal.split()
    rhymed_words = [stylize_word(w) for w in words]
    return " ".join(rhymed_words)
