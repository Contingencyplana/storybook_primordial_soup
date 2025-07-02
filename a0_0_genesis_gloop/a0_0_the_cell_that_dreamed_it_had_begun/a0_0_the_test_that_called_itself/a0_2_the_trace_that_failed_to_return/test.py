# test.py
# 🛡️ Recursive Test Interface – Trace Stall Detection Variant
# For: s0_2_the_trace_that_failed_to_return

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest
import logging

@pytest.mark.timeout(10)
def test_recursive_trace_behavior(monkeypatch, caplog):
    import main as target

    def fake_sleep(seconds):
        raise InterruptedError("Simulated hang interrupt")

    monkeypatch.setattr(target.time, "sleep", fake_sleep)

    with caplog.at_level(logging.INFO):
        with pytest.raises(InterruptedError):
            target.recursive_trace(0, 3)

    assert "Tracing depth 3/3" in caplog.text
    assert "Trace reached max depth and failed to return." in caplog.text
