# 🧪 test.py
# Path: a0_1_mighty_quest_for_the_bug_kingdom/a0_1_the_trail_that_led_through_mush/test.py

from main import follow_trail_through_mush

def run_mush_test():
    print("🍄 Trail Confusion Simulator – Through the Mush")
    
    try:
        strength = float(input("Signal strength (0.0–1.0): "))
        if not 0.0 <= strength <= 1.0:
            print("❌ Signal strength must be between 0.0 and 1.0.")
            return
    except ValueError:
        print("❌ Invalid number. Please enter a decimal.")
        return

    bug = input("Bug type (scout, drone, king): ").strip().lower()
    if bug not in {"scout", "drone", "king"}:
        print("❌ Invalid bug type. Choose from scout, drone, or king.")
        return

    result = follow_trail_through_mush(strength, bug)
    print("\n📜 Trail Result:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_mush_test()
