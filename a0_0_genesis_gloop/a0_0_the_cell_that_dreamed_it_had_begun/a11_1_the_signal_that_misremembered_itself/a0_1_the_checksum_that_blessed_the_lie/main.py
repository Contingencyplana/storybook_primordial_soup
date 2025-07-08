# 🧠 main.py – The Checksum That Blessed the Lie
# This file defines logic for comparing two signals — the sent and the returned.
# It uses a surface-level checksum (length and word count) to validate the signal,
# even when the semantics may have drifted underneath.

def surface_checksum(text):
    words = text.strip().split()
    return {
        "length": len(text),
        "word_count": len(words)
    }

def is_checksum_match(original, returned):
    checksum_orig = surface_checksum(original)
    checksum_return = surface_checksum(returned)
    return checksum_orig == checksum_return
