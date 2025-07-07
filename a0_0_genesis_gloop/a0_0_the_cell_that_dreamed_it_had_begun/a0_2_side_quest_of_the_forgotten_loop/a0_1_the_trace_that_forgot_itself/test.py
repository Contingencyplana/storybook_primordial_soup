# 🧪 test.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_1_the_trace_that_forgot_itself/test.py

from main import analyze_forgotten_trace

def run_trace_analysis():
    print("🧠 Recursive Trace Memory Analyzer – Lost or Remembered?")
    try:
        input_string = input("Enter trace steps (comma-separated): ")
        trace_log = [x.strip() for x in input_string.split(",") if x.strip()]
    except Exception:
        print("❌ Invalid input.")
        return

    result = analyze_forgotten_trace(trace_log)
    print("\n📜 Trace Report:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    run_trace_analysis()

