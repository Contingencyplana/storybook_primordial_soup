# 🧪 test.py
# Path: a11_0_the_log_that_was_written_in_absentia/a0_0_the_false_event_that_triggered_logging/test.py

from main import record_event

def simulate_log_entry():
    print("📜 Phantom Logging Test – Was This Event Ever Real?")
    signal = input("Enter event signal: ").strip()

    result = record_event(signal)
    print("\n🗂️ Log Entry Result:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    simulate_log_entry()
