# 📂 a0_0_the_loop_that_reflected_on_itself/test.py

from main import run_reflective_loop

def start_loop_reflection():
    print("📜 Reflective Loop – The Loop That Reflected On Itself")
    print("Enter recursive loop states line by line. Type 'done' to start reflection.\n")

    trace = []

    while True:
        entry = input("🔄 Loop Entry: ")
        if entry.lower() == "done":
            break
        if entry.strip():
            trace.append(entry.strip())

    print("\n🪞 Loop Reflection Trace:")
    results = run_reflective_loop(trace)
    for line in results:
        print(line)

    print()

if __name__ == "__main__":
    start_loop_reflection()
