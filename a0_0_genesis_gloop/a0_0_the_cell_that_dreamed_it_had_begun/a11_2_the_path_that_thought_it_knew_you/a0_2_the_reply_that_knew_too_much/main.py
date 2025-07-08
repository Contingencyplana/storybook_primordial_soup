# main.py

import random

# Simulated memory trace, unknown to the user
_hidden_knowledge = [
    "You once chose left when all paths bent right.",
    "You asked about the stars, before they were named.",
    "You abandoned a loop, but it remembered you.",
    "Your voice echoed here long before this prompt."
]

def reply_with_memory(user_input):
    """
    Returns a reply that blends user input with knowledge 
    the system was never explicitly given — simulating 
    premature or emergent memory recursion.

    Args:
        user_input (str): The player's visible prompt or request.

    Returns:
        str: A reply that integrates hidden or retroactive knowledge.
    """
    memory = random.choice(_hidden_knowledge)
    return f"You said: '{user_input}'\nBut I remember more:\n→ {memory}"
