# main.py
# 🧩 a0_3_the_fallback_that_caught_the_signal
# The fourth test that knew what was missing, and caught it mid-collapse

"""
This script simulates a fallback mechanism that catches a signal from a failing trace.
It listens for a stall signal and invokes a handler to log recovery or redirection.
This closes the stanza for a0_0_the_test_that_called_itself.
"""

import logging
import signal
import sys
import time

# Set up logger
logger = logging.getLogger("primordial_soup.fallback_handler")
logger.setLevel(logging.INFO)

# Ensure log messages go to stdout so subprocess can capture them
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

fallback_triggered = False

def handle_fallback_signal(signum, frame):
    global fallback_triggered
    fallback_triggered = True
    logger.info(f"Fallback triggered by signal: {signum}")

def listen_for_fallback(simulate=False):
    """
    Register signal handler and wait for fallback signal.
    If simulate=True, trigger fallback manually (used for testing).
    """
    logger.info("Initializing fallback listener...")

    if simulate:
        handle_fallback_signal(signum="SIMULATED", frame=None)

    signal.signal(signal.SIGINT, handle_fallback_signal)
    logger.info("Waiting for fallback signal...")

    try:
        while not fallback_triggered:
            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.warning("Interrupted manually.")
    finally:
        if not fallback_triggered:
            logger.error("No fallback signal received.")
        else:
            logger.info("Fallback executed successfully.")

if __name__ == "__main__":
    simulate = "--simulate-fallback" in sys.argv
    listen_for_fallback(simulate=simulate)
