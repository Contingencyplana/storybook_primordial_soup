# Save to: a14_3_the_trace_that_asked_to_be_followed/s0_1_the_pattern_that_waited_to_be_seen/main.py

"""
📜 The Pattern That Waited to Be Seen

This minigame presents a subtle recursive pattern embedded within system output.
The player's task is to detect the pattern—not by following instructions, but by **noticing the anomaly**.

The system introduces a deliberate inconsistency in the loop output.
Recognition of the pattern signals the player's readiness for deeper recursion.
"""

def generate_output():
    pattern = [
        "↺ Loop iteration 1: system_call -> fallback -> trace_emit",
        "↺ Loop iteration 2: system_call -> fallback -> trace_emit",
        "↺ Loop iteration 3: system_call -> fallback -> trace_emit",
        "↺ Loop iteration 4: system_call -> fallback -> trace_omit"  # The anomaly
    ]
    return pattern

def display_output(output):
    print("\n🌀 Recursive Loop Output:\n")
    for line in output:
        print(line)
    print("\n🔍 Did you notice the pattern anomaly?")
    print("1. Yes – The last line deviated from the pattern.")
    print("2. No – All lines seemed the same.")
    print("3. Exit the pattern analysis.")

def main():
    output = generate_output()
    display_output(output)
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\n✅ Pattern recognized. The system confirms recursive awareness.")
    elif choice == "2":
        print("\n🔄 Pattern not recognized. The system continues outputting silent recursion.")
    elif choice == "3":
        print("\n🚪 Exiting pattern analysis. System returns to standby.")
    else:
        print("\n❓ Unrecognized input. The pattern remains unresolved.")

if __name__ == "__main__":
    main()
