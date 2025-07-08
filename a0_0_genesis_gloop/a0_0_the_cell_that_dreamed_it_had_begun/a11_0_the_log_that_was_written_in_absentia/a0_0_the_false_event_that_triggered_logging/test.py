# 📄 test.py
# 🧪 Interactive tester for a11_0_the_log_that_was_written_in_absentia → a0_0_the_false_event_that_triggered_logging

from main import log_phantom_event

print("📜 Phantom Logging Test – The False Event That Triggered Logging\n")

while True:
    signal = input("Enter signal (or press Enter to simulate absence): ").strip()
    
    if signal.lower() in ["exit", "quit", "q"]:
        print("👋 Exiting phantom logging test.")
        break

    result = log_phantom_event(signal)
    print("\n🧠 Log Interpretation:")
    print(f"Event  : {result['event']}")
    print(f"Status : {result['status']}")
    print(f"Reason : {result['reason']}\n")
