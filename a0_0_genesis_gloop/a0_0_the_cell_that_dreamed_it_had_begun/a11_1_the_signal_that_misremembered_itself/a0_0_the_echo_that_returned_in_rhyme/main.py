# 🌀 main.py – The Echo That Returned in Rhyme
# This file defines the logic for transforming an incoming message
# into a rhymed echo — not as corruption, but as semantic drift through cadence.

import random

def rhyme_word(word):
    rhymes = {
        "day": "play",
        "night": "flight",
        "truth": "youth",
        "sound": "round",
        "light": "bright",
        "fire": "desire",
        "code": "load",
        "loop": "swoop",
        "mind": "kind",
        "dream": "stream"
    }
    return rhymes.get(word.lower(), word)

def transform_to_rhyme(message):
    words = message.strip().split()
    if not words:
        return ""

    rhymed_words = []
    for word in words:
        if word.isalpha():
            rhymed_words.append(rhyme_word(word))
        else:
            rhymed_words.append(word)

    return " ".join(rhymed_words)

def return_rhymed_echo(message):
    echo = transform_to_rhyme(message)
    return echo
