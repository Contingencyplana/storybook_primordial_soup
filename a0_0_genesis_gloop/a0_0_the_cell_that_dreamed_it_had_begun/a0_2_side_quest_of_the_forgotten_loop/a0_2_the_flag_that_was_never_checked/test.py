# 🧪 test.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_2_the_flag_that_was_never_checked/test.py

from main import check_unqueried_flag

def run_flag_test():
    print("🚩 Flag Verification Simulator – Was It Ever Checked?")

    flag = input("Enter flag name: ").strip()
    set_input = input("Was the flag set? (yes/no): ").strip().lower()
    checked_input = input("Was the flag checked? (yes/no): ").strip().lower()

    state = {
        "flag_name": flag or "unnamed_flag",
        "flag_set": set_input == "yes",
        "checked": checked_input == "yes"
    }

    result = check_unqueried_flag(state)
    print("\n📜 Flag Analysis:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_flag_test()
