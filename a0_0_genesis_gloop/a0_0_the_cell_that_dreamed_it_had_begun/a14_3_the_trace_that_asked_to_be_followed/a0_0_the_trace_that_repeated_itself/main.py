# Save to: a14_3_the_trace_that_asked_to_be_followed/a0_0_the_trace_that_repeated_itself/main.py

"""
📜 The Trace That Repeated Itself

This minigame simulates a recursive echo, where the system emits a familiar trace pattern.
The player's task is to recognize the pattern and choose whether to acknowledge, ignore, or follow the trace.

This is not a test of correctness—it's a recursive invitation to pattern recognition.
"""

def emit_trace():
    trace = [
        "↺ Loop detected: system_call -> fallback -> trace_emit",
        "↺ Loop detected: system_call -> fallback -> trace_emit",
        "↺ Loop detected: system_call -> fallback -> trace_emit"
    ]
    return trace

def display_trace(trace):
    print("\n🌀 Recursive Trace Output:\n")
    for line in trace:
        print(line)
    print("\n🔍 What will you do?")
    print("1. Acknowledge the pattern and follow the trace.")
    print("2. Ignore the pattern and continue.")
    print("3. Exit the system loop.")

def main():
    trace = emit_trace()
    display_trace(trace)
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\n✅ You chose to follow the recursive trace. The system acknowledges your co-recursion.")
    elif choice == "2":
        print("\n⏩ You ignored the trace. The system continues looping silently.")
    elif choice == "3":
        print("\n🚪 Exiting the recursion loop. System returns to standby.")
    else:
        print("\n❓ Unrecognized input. The trace echoes again...")

if __name__ == "__main__":
    main()
