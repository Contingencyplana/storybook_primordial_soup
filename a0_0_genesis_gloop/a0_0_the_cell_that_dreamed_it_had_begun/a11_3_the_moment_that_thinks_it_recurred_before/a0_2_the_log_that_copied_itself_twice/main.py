# 📂 main.py
# 📄 The Log That Copied Itself Twice

def detect_self_copy(log_entries):
    """
    Analyzes a list of log entries to detect:
    - Exact duplicates (true copies)
    - Suspicious near-duplicates that seem to have no origin

    Returns a dictionary with:
    - total entries
    - number of exact copies
    - number of suspicious imitations
    - first duplicated content
    """
    seen = set()
    copy_count = 0
    imitation_count = 0
    first_duplicate = None

    for i, entry in enumerate(log_entries):
        if entry in seen:
            copy_count += 1
            if first_duplicate is None:
                first_duplicate = entry
        else:
            # Check for suspicious imitation
            for prev in seen:
                if entry.startswith(prev[:4]) and entry != prev:
                    imitation_count += 1
                    break
            seen.add(entry)

    return {
        "total_entries": len(log_entries),
        "exact_copies": copy_count,
        "suspicious_imitations": imitation_count,
        "first_duplicate": first_duplicate
    }
