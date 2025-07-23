# a1_1_link_nodal_meta_recursion_controls/main.py

import os
from datetime import datetime, timezone

def link_meta_recursion_controls(node_entries, control_file_path):
    """
    Appends node metadata entries to the central meta_recursion_controls.md file.

    Args:
        node_entries (list of dict): Each dict must contain:
            - name: str – the node folder name
            - description: str – description of the node's purpose
        control_file_path (str): Path to the meta_recursion_controls.md file

    Returns:
        dict: Summary including counts of added and skipped nodes, and full trace log
    """
    added, skipped = 0, 0
    trace_log = []

    # Initialize or load existing content
    if os.path.exists(control_file_path):
        with open(control_file_path, "r", encoding="utf-8") as f:
            existing_content = f.read()
    else:
        existing_content = "# 📁 Meta-Recursion Controls\n\nThis file links all known builder nodes for orchestration, traceability, and indexing.\n\n---\n"

    updated_lines = existing_content.splitlines()

    for entry in node_entries:
        node_name = entry["name"]
        if any(node_name in line for line in updated_lines):
            skipped += 1
            trace_log.append({
                "node": node_name,
                "status": "skipped",
                "event": "already_linked",
                "timestamp": datetime.now(timezone.utc).isoformat()
            })
            continue

        timestamp = datetime.now(timezone.utc).isoformat()
        node_block = f"- ✅ `{node_name}` – {entry['description']} (linked_meta_recursion_control @ {timestamp})"
        updated_lines.append(node_block)

        trace_log.append({
            "node": node_name,
            "status": "linked",
            "event": "linked_meta_recursion_control",
            "timestamp": timestamp
        })
        added += 1

    with open(control_file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines) + "\n")

    return {
        "status": "completed",
        "added": added,
        "skipped": skipped,
        "trace": trace_log
    }
