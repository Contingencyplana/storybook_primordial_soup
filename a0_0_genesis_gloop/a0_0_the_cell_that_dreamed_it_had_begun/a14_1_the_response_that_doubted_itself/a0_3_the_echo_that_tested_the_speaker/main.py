# Save to: a14_1_the_response_that_doubted_itself/a0_3_the_echo_that_tested_the_speaker/main.py

def echo_and_test(command):
    """
    Echoes back the command to the player, asking for confirmation.
    This models recursive reflection, where the system tests the intent of the speaker.
    """
    print(f"🔁 Echoing back: '{command}'")
    if confirm_intent(command):
        print("✅ Confirmation received: Proceeding with the response.")
    else:
        print("🤔 Doubt remains: The system is unsure if the command was truly meant.")


def confirm_intent(command):
    """
    Always returns False in this node to simulate reflective hesitation.
    The system doubts whether the input was truly intended.
    """
    print(f"🧠 Reflecting on command: '{command}' - Is this truly what was intended?")
    return False


if __name__ == "__main__":
    user_command = "Activate protocol alpha"
    echo_and_test(user_command)

