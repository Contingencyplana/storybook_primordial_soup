# main.py
# 🧩 s0_3_the_fallback_that_caught_the_signal
# The fourth test that knew what was missing, and caught it mid-collapse

"""
This script simulates a fallback mechanism that catches a signal from a failing trace.
It listens for a stall signal and invokes a handler to log recovery or redirection.
This closes the stanza for a0_0_the_test_that_called_itself.
"""

import logging
import signal
import sys

logger = logging.getLogger("primordial_soup.fallback_handler")
logger.setLevel(logging.INFO)

# Simulated flag to indicate a fallback was triggered
fallback_triggered = False

def handle_fallback_signal(signum, frame):
    global fallback_triggered
    fallback_triggered = True
    logger.info(f"Fallback triggered by signal: {signum}")
    sys.exit(0)

def listen_for_fallback():
    """
    Register signal handler and wait for a signal.
    In real systems, this might catch SIGTERM or a custom signal.
    """
    logger.info("Initializing fallback listener...")
    signal.signal(signal.SIGUSR1, handle_fallback_signal)
    logger.info("Waiting for fallback signal...")
    try:
        signal.pause()  # Wait indefinitely for signal
    except KeyboardInterrupt:
        logger.warning("Interrupted manually.")
    finally:
        if not fallback_triggered:
            logger.error("No fallback signal received.")
        else:
            logger.info("Fallback executed successfully.")

if __name__ == "__main__":
    listen_for_fallback()
