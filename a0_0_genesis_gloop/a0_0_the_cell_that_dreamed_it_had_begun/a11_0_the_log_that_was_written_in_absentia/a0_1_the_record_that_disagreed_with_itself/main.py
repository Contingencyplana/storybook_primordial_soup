# main.py

"""
This module simulates a recursive memory system in conflict with itself.
It loads two log entries for the same event ID but with contradictory data.
"""

def get_conflicting_logs():
    """
    Returns a list of two contradictory log entries for the same event.
    """
    return [
        {
            "event_id": "phantom-0001",
            "source": "Log Shard A",
            "timestamp": "2025-07-07T00:00:00Z",
            "outcome": "Signal escalation triggered.",
            "validity": True
        },
        {
            "event_id": "phantom-0001",
            "source": "Log Shard B",
            "timestamp": "2025-07-07T00:00:00Z",
            "outcome": "Signal discarded as irrelevant.",
            "validity": True
        }
    ]

if __name__ == "__main__":
    logs = get_conflicting_logs()
    print("📚 Conflicting Log Records Detected:")
    for entry in logs:
        print("\n---")
        for k, v in entry.items():
            print(f"{k}: {v}")
