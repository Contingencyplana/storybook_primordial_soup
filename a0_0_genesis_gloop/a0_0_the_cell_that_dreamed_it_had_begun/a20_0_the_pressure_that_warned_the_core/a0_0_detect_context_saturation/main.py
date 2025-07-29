# main.py – a0_0_detect_context_saturation

import os
import json
from datetime import datetime

def detect_context_saturation(project_root):
    saturation_report = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "token_overflow_risk": False,
        "recursive_depth": 0,
        "folder_count": 0,
        "suspected_overload_zones": [],
    }

    for root, dirs, files in os.walk(project_root):
        depth = root[len(project_root):].count(os.sep)
        saturation_report["folder_count"] += 1
        if depth > saturation_report["recursive_depth"]:
            saturation_report["recursive_depth"] = depth
        if len(dirs) + len(files) > 100:
            saturation_report["suspected_overload_zones"].append(root)

    if saturation_report["recursive_depth"] > 12 or saturation_report["folder_count"] > 200:
        saturation_report["token_overflow_risk"] = True

    output_path = os.path.join(project_root, "trace_pressure.md")
    with open(output_path, "w") as f:
        f.write(f"# 🧠 Trace Pressure Report\n\n")
        f.write(f"**Timestamp:** {saturation_report['timestamp']}\n\n")
        f.write(f"**Recursive Depth:** {saturation_report['recursive_depth']}\n")
        f.write(f"**Folder Count:** {saturation_report['folder_count']}\n")
        f.write(f"**Overflow Risk:** {saturation_report['token_overflow_risk']}\n\n")
        if saturation_report["suspected_overload_zones"]:
            f.write("## ⚠️ Suspected Overload Zones\n")
            for zone in saturation_report["suspected_overload_zones"]:
                f.write(f"- {zone}\n")

    return saturation_report

if __name__ == "__main__":
    project_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../../../..")
    )
    report = detect_context_saturation(project_root)
    print(json.dumps(report, indent=2))
