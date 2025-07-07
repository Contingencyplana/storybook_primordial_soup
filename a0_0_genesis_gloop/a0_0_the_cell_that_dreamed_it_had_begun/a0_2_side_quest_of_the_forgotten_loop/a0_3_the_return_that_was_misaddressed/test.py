# 🧪 test.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_3_the_return_that_was_misaddressed/test.py

from main import route_return_signal

def run_return_check():
    print("📬 Return Signal Test – Was It Misaddressed?")

    known_destinations = {"core.loop", "memory.index", "backup.catch"}

    signal_id = input("Enter signal ID: ").strip()
    return_address = input("Enter return address: ").strip()

    result = route_return_signal(known_destinations, signal_id, return_address)

    print("\n📜 Routing Outcome:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_return_check()
