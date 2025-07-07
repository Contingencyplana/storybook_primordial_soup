# 🧪 test.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_0_the_loop_that_almost_closed/test.py

from main import simulate_forgotten_loop

def run_loop_test():
    print("♻️  Loop Test – Echo of the Forgotten Closure")
    try:
        input_sequence = input("Enter comma-separated task checkpoints: ")
        tasks = [x.strip() for x in input_sequence.split(",") if x.strip()]
    except Exception:
        print("❌ Invalid input.")
        return

    result = simulate_forgotten_loop(tasks)
    print("\n📜 Loop Analysis:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_loop_test()
