# test.py
# 🛡️ Recursive Test Interface – Trace Stall Detection Variant
# For: s0_2_the_trace_that_failed_to_return

"""
This test confirms the trace reaches the expected recursion depth
and simulates failure to return. We don't allow the infinite loop to run,
but we verify the behavior up to the hang point using a patched time.sleep.
"""

import pytest
import logging

from unittest import mock
from importlib import reload

@pytest.mark.timeout(10)
def test_recursive_trace_behavior(monkeypatch, caplog):
    import s0_2_the_trace_that_failed_to_return.main as target

    # Patch time.sleep to raise an exception after the warning is logged
    def fake_sleep(seconds):
        raise InterruptedError("Simulated hang interrupt")

    monkeypatch.setattr(target.time, "sleep", fake_sleep)

    with caplog.at_level(logging.INFO):
        with pytest.raises(InterruptedError):
            target.recursive_trace(0, 3)

    assert "Tracing depth 3/3" in caplog.text
    assert "Trace reached max depth and failed to return." in caplog.text
