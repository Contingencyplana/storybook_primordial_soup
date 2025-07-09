# 📂 test.py
# 🧪 Test – The Outcome That Forgot to Begin

from main import validate_outcome_sequence

def run_outcome_validation():
    print("🌀 Outcome Validation – The Outcome That Forgot to Begin")
    print("Enter events first. Type 'done' to finish event log.\n")

    event_log = []
    while True:
        event = input("📜 Event: ").strip()
        if event.lower() == "done":
            break
        event_log.append(event)

    print("\n✅ Now enter the outcome you wish to validate:")
    outcome = input("🎯 Outcome: ").strip()

    result = validate_outcome_sequence(event_log, outcome)

    print("\n📊 Outcome Analysis:")
    print(f"Outcome        : {result['outcome']}")
    print(f"Status         : {result['status']}")
    if result['matched_event']:
        print(f"Matched Event  : {result['matched_event']}")
    else:
        print("Matched Event  : None")

if __name__ == "__main__":
    run_outcome_validation()
