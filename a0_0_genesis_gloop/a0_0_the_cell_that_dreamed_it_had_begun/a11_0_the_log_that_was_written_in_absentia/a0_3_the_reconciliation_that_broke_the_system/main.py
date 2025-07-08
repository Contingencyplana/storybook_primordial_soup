# Save as: a0_3_the_reconciliation_that_broke_the_system/main.py

def reconcile_logs(log_entries):
    """
    Attempts to reconcile a list of log entries.
    If contradictory, the reconciliation attempt fails catastrophically.

    Parameters:
    - log_entries (list of str): Individual memory records to compare.

    Returns:
    - dict: Status and outcome of the reconciliation attempt.
    """
    if not log_entries:
        return {
            "status": "empty",
            "outcome": "No logs provided. Nothing to reconcile."
        }

    unique_entries = set(entry.strip() for entry in log_entries if entry.strip())

    if len(unique_entries) == 1:
        return {
            "status": "unified",
            "outcome": f"All logs agree: '{unique_entries.pop()}'. System coherence restored."
        }
    elif len(unique_entries) == 0:
        return {
            "status": "blank",
            "outcome": "All entries were empty or whitespace. Reconciliation impossible."
        }
    else:
        return {
            "status": "catastrophic_conflict",
            "outcome": f"{len(unique_entries)} conflicting memories detected.\n"
                       f"Entries: {list(unique_entries)}\n"
                       f"System destabilized by paradox."
        }
