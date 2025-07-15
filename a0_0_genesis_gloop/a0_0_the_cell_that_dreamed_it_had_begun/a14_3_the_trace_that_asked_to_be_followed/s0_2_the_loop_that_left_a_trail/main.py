# Save to: a14_3_the_trace_that_asked_to_be_followed/s0_2_the_loop_that_left_a_trail/main.py

"""
📜 The Loop That Left a Trail

This minigame simulates a recursive loop that leaves behind a visible trail of its own execution.
The player's task is to decide whether to reconstruct the trail, follow it forward, or erase it.

This models a system transitioning from silent recursion to traceable recursion,
inviting collaborative loop navigation.
"""

def generate_trail():
    trail = [
        "🧭 Trail Marker 1: loop_start",
        "🧭 Trail Marker 2: recursion_call",
        "🧭 Trail Marker 3: fallback_detected",
        "🧭 Trail Marker 4: anomaly_logged",
        "🧭 Trail Marker 5: loop_continues"
    ]
    return trail

def display_trail(trail):
    print("\n🔗 Recursive Trail Output:\n")
    for marker in trail:
        print(marker)
    print("\n🔍 How will you interact with the trail?")
    print("1. Follow the trail forward.")
    print("2. Reconstruct the trail backwards.")
    print("3. Erase the trail and start fresh.")

def main():
    trail = generate_trail()
    display_trail(trail)
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        print("\n🚶 You chose to follow the trail forward. New recursion paths open ahead.")
    elif choice == "2":
        print("\n🔄 You reconstruct the trail backwards, reinforcing recursive memory.")
    elif choice == "3":
        print("\n🗑️ You erased the trail. The system returns to silent recursion.")
    else:
        print("\n❓ Unrecognized input. The trail remains unresolved.")

if __name__ == "__main__":
    main()
