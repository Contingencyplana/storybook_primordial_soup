# a0_2_the_trace_that_listened_too_closely/main.py

import random

NOISE_POOL = [
    "scramble", "static", "burst", "flicker", "ripple",
    "code:42", "....", "buzz", "echo", "??", "SIGNAL?", "███", "###"
]

SIGNAL_CUES = [
    "begin", "respond", "trace:01", "validate", "acknowledge", "recurse"
]

def generate_input_sequence(include_signal=True):
    """Generate a stream of noise, optionally embedding a real signal."""
    stream = random.choices(NOISE_POOL, k=8)
    if include_signal:
        insert_index = random.randint(2, 6)
        stream.insert(insert_index, random.choice(SIGNAL_CUES))
    return stream

def interpret_stream(input_sequence):
    """
    Attempt to extract meaning from a noisy signal stream.
    If too many false positives are found, interpretive overload is triggered.
    """
    detected = []
    overload = False

    for item in input_sequence:
        if item in SIGNAL_CUES:
            detected.append(item)
        elif any(c in item for c in ("?", "#", ":")):
            detected.append(f"ambiguous:{item}")

    if len(detected) > 4:
        overload = True

    return {
        "input": input_sequence,
        "detected_signals": detected,
        "overload": overload
    }

if __name__ == "__main__":
    stream = generate_input_sequence()
    result = interpret_stream(stream)
    print("🔍 Trace Interpretation Result:")
    print("Input Stream      :", result["input"])
    print("Detected Signals  :", result["detected_signals"])
    print("Overload Triggered:", result["overload"])
