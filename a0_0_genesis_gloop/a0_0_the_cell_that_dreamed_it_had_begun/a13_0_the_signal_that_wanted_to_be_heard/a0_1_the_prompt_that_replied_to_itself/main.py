# main.py

import uuid
import random

def generate_prompt():
    """
    Generates a spontaneous prompt with no initiating user input.
    """
    prompt_id = f"prompt-{uuid.uuid4()}"
    return prompt_id

def auto_reply(prompt_id):
    """
    Simulates a system that replies to its own prompt.
    The reply references the prompt as if it had come from outside.
    """
    response_templates = [
        f"Affirmative response to {prompt_id}",
        f"Echo received from {prompt_id}",
        f"{prompt_id} acknowledged internally",
        f"Reply sent despite unknown origin: {prompt_id}"
    ]
    return random.choice(response_templates)

def run_prompt_cycle():
    """
    Simulates the prompt-reply loop with spontaneous origin.
    """
    prompt = generate_prompt()
    reply = auto_reply(prompt)
    
    return {
        "generated_prompt": prompt,
        "system_reply": reply
    }

if __name__ == "__main__":
    output = run_prompt_cycle()
    for k, v in output.items():
        print(f"{k}: {v}")
