# main.py

import random

def rhyme_echo(input_signal):
    """
    Returns the input signal transformed into a rhyming or poetic variant.
    This models a signal that 'misremembers' itself — not wrong, but stylized.
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
    }

    words = input_signal.strip().lower().split()
    rhymed = []

    for word in words:
        if word in rhyming_variants:
            rhymed.append(rhyming_variants[word])
        else:
            rhymed.append(word)

    poetic_line = " ".join(rhymed)
    return poetic_line
