# main.py  
# Primordial Soup – Meta-Recursion Controls  
# Layer 4 Node: a0_0_meta_recursion_controls  

import sys

def create_minigame_node():
    """
    Generates a new minigame node folder with:
    - __init__.py
    - main.py
    - subtaskmap.md
    - test.py
    """
    print("[L] Create Minigame Node: Function called (placeholder).")
    # TODO: Implement directory creation logic here.

def create_minigame():
    """
    Generates a new minigame folder with:
    - 4 empty minigame nodes
    - taskmaps/ folder with README.md, milestones.md, stanzamap.md, taskmap.md
    """
    print("[R] Create Minigame: Function called (placeholder).")
    # TODO: Implement full minigame scaffolding here.

def exit_to_previous_layer():
    """
    Handles safe recursion exit and breadcrumb preservation.
    """
    print("[ESC] Exiting to previous recursion layer...")
    sys.exit(0)

def select_from_branch_options(options):
    """
    Presents numbered options for branching choices.
    
    Args:
        options (list): List of option strings to present.
    """
    print("\nBranch Selection:")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")

    choice = None
    while choice is None:
        try:
            user_input = input("Select an option: ")
            selected = int(user_input)
            if 1 <= selected <= len(options):
                choice = selected
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Branch {choice} selected: {options[choice - 1]}")
    # TODO: Implement branching logic based on selection.

def main_loop():
    """
    Main input listener loop for meta-recursion controls.
    Declares the active recursion context for anchoring.
    """

    # 🧭 Recursive Layer Anchoring Declaration
    current_layer = 2  # Meta-Recursive Control Layer (this node)
    target_build_layer = 3  # This node builds Layer 3 structures (compilers, minigames)

    print("\n🧬 Primordial Soup – Meta-Recursion Control Node 🧬")
    print(f"🧭 Layer Anchoring: I am in Layer {current_layer}, building Layer {target_build_layer}.")
    print("Press [L] to create a Minigame Node.")
    print("Press [R] to create a Minigame (4 nodes).")
    print("Press [ESC] to exit recursion layer.")
    print("Press [1], [2], [3], etc. to select from branch options (if presented).")
    print("─────────────────────────────────────────────\n")

    branch_options = [
        "Simulate anomaly loop (placeholder)",
        "Generate snapshot (placeholder)",
        "Return to core loop"
    ]

    while True:
        user_input = input(">> ").strip().lower()

        if user_input == 'l':
            create_minigame_node()
        elif user_input == 'r':
            create_minigame()
        elif user_input == 'esc':
            exit_to_previous_layer()
        elif user_input.isdigit():
            select_from_branch_options(branch_options)
        else:
            print("Unrecognized input. Use L, R, ESC, or a number for branch options.")

if __name__ == "__main__":
    main_loop()
