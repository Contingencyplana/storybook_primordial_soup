# a5_2_the_function_that_should_never_have_been_called/test.py

from main import call_with_warning

def run_test():
    print("🔍 Running test: forbidden function call...\n")

    # Safe path
    result = call_with_warning(allow=False)
    print("🚫 Attempt blocked:")
    print(f"📜 Status: {result['status']}")
    print(f"🧪 Message: {result['message']}")
    print("-" * 40)

    # Unsafe path
    result = call_with_warning(allow=True)
    print("🚨 Forbidden path triggered:")
    print(f"📜 Status: {result['status']}")
    print(f"🧪 Message: {result['message']}")
    print("-" * 40)

if __name__ == "__main__":
    run_test()
