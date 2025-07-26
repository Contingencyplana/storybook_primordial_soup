# a1_1_link_nodal_meta_recursion_controls/main.py

from pathlib import Path
from datetime import datetime, timezone

def link_meta_recursion_controls(node_entries, control_file_path):
    """
    Appends node metadata entries to the central meta_recursion_controls.md file.

    Args:
        node_entries (list of dict): Each dict must contain:
            - name: str – the node folder name
            - description: str – short description of the node's role
        control_file_path (str or Path): Path to the central .md file

    Returns:
        dict: Summary including counts of added and skipped entries, and full trace log
    """
    control_path = Path(control_file_path)
    control_path.parent.mkdir(parents=True, exist_ok=True)

    if control_path.exists():
        existing_content = control_path.read_text(encoding="utf-8")
    else:
        existing_content = (
            "# 📁 Meta-Recursion Controls\n\n"
            "This file links all known builder nodes for orchestration, traceability, and indexing.\n\n"
            "---\n"
        )

    updated_lines = existing_content.splitlines()
    added, skipped = 0, 0
    trace_log = []

    for entry in node_entries:
        node_name = entry["name"]
        if any(node_name in line for line in updated_lines):
            trace_log.append({
                "node": node_name,
                "status": "skipped",
                "event": "already_linked",
                "timestamp": datetime.now(timezone.utc).isoformat()
            })
            skipped += 1
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

    control_path.write_text("\n".join(updated_lines) + "\n", encoding="utf-8")

    return {
        "status": "completed",
        "added": added,
        "skipped": skipped,
        "trace": trace_log
    }
