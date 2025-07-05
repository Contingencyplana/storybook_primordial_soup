# a5_1_the_trace_that_betrayed_the_test/test.py

from main import analyze_trace

def run_test():
    print("🔍 Running test: misleading trace analysis...\n")

    traces = [
        "user_action=success; integrity=corrupt",
        "user_action=success",
        "error_code=1024; timeout",
        ""
    ]

    for trace in traces:
        result = analyze_trace(trace)
        print(f"📡 Trace: {trace or '[EMPTY]'}")
        print(f"📜 Status: {result['status']}")
        print(f"🧪 Message: {result['message']}")
        if result.get("betrayal"):
            print("🚨 ALERT: Test betrayed by trace!")
        print("-" * 40)

if __name__ == "__main__":
    run_test()
