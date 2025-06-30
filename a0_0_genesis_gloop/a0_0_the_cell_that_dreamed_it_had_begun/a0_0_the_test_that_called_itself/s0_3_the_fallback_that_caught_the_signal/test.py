# test.py
# 🛡️ Recursive Test Interface – Fallback Signal Detection Variant
# For: s0_3_the_fallback_that_caught_the_signal

import sys
import os
import signal
import time
import subprocess
import pytest

@pytest.mark.timeout(10)
def test_fallback_signal_catching():
    """
    Launches the fallback listener as a subprocess,
    sends it a SIGINT signal (Ctrl+C equivalent on Windows),
    and confirms expected output.
    """
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    process = subprocess.Popen([sys.executable, script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    time.sleep(1)  # Give time to initialize and enter signal pause

    # Send fallback signal
    os.kill(process.pid, signal.SIGINT)

    stdout, stderr = process.communicate(timeout=5)
    output = stdout.decode()

    assert "Fallback triggered by signal" in output
    assert "Fallback executed successfully." in output
