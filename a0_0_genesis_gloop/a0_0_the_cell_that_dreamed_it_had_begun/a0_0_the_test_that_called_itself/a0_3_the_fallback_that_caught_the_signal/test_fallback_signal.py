# test_fallback_signal.py
# 🛡️ Recursive Test Interface – Fallback Signal Detection Variant
# For: a0_3_the_fallback_that_caught_the_signal

import sys
import os
import subprocess
import pytest

@pytest.mark.timeout(10)
def test_fallback_signal_catching():
    """
    Launches the fallback listener as a subprocess with --simulate-fallback,
    which manually triggers the fallback signal handler and logs success.
    """
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    process = subprocess.Popen(
        [sys.executable, script_path, "--simulate-fallback"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, stderr = process.communicate(timeout=5)
    output = stdout.decode()

    assert "Fallback triggered by signal" in output
    assert "Fallback executed successfully." in output
