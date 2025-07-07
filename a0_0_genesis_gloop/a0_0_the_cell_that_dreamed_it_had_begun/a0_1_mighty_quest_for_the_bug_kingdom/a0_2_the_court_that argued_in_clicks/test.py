# 🧪 test.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_2_the_court_that_argued_in_clicks/test.py

from main import resolve_click_argument

def simulate_click_argument():
    print("🗣️  Click-Based Courtroom – Bug Argument Simulator")

    bug = input("Bug type (scout, drone, advisor): ").strip().lower()
    position = input("Court position (left, center, right): ").strip().lower()
    fragment = input("Memory fragment to debate: ").strip()

    if bug not in {"scout", "drone", "advisor"}:
        print("❌ Invalid bug type.")
        return

    if position not in {"left", "center", "right"}:
        print("❌ Invalid court position.")
        return

    result = resolve_click_argument(bug, position, fragment)
    print("\n📜 Argument Outcome:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    simulate_click_argument()
