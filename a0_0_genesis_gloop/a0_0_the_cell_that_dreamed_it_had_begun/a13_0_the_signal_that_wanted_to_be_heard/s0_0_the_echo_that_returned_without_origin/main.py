# main.py

import random
import uuid

def generate_signal():
    """
    Generates a recursive signal identifier.
    """
    return f"signal-{uuid.uuid4()}"

def receive_echo(signal_id, noise_chance=0.3):
    """
    Simulates an echo returning from the system. 
    The echo may be the same signal, a distorted version, or unrecognized noise.
    """
    roll = random.random()

    if roll < noise_chance:
        return f"noise-{uuid.uuid4()}"
    elif roll < 0.9:
        return signal_id  # expected echo
    else:
        return None  # no echo at all

def analyze_echo(original_signal, echo_signal):
    """
    Compares the original and echo signal to decide if it is believable.
    """
    if echo_signal is None:
        return "Echo absent — uncertainty grows."
    elif echo_signal == original_signal:
        return "Echo matched — system reflects."
    else:
        return f"Echo mismatch — possible anomaly: {echo_signal}"

def run_signal_cycle():
    """
    Runs one full send-receive-analyze loop.
    """
    signal = generate_signal()
    echo = receive_echo(signal)
    analysis = analyze_echo(signal, echo)

    return {
        "original_signal": signal,
        "received_echo": echo,
        "analysis_result": analysis
    }

if __name__ == "__main__":
    result = run_signal_cycle()
    for k, v in result.items():
        print(f"{k}: {v}")
