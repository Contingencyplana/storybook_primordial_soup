# test.py – a0_0_detect_context_saturation
import os
import pytest
from main import detect_context_saturation

def test_detect_context_saturation(tmp_path):
    # Simulate recursive folder structure
    deep_dir = tmp_path
    for i in range(15):
        deep_dir = deep_dir / f"level_{i}"
        deep_dir.mkdir()

    # Create dummy files to simulate bloat
    for i in range(150):
        (deep_dir / f"dummy_file_{i}.txt").write_text("X" * 100)

    report = detect_context_saturation(str(tmp_path))

    assert isinstance(report, dict)
    assert "recursive_depth" in report
    assert "folder_count" in report
    assert "token_overflow_risk" in report
    assert report["recursive_depth"] >= 15
    assert report["folder_count"] >= 15
    assert report["token_overflow_risk"] is True
