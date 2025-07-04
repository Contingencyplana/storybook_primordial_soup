# a5_0_the_fallback_that_failed/test.py

from main import execute_fallback

def run_test():
    print("🔍 Running test: failed fallback simulation...\n")

    result = execute_fallback()

    if result["status"] == "failure":
        print(f"❌ {result['message']}")
        print(f"🧪 Error Code: {result['error_code']}")
    else:
        print("✅ Unexpected fallback success (check logic).")

if __name__ == "__main__":
    run_test()
