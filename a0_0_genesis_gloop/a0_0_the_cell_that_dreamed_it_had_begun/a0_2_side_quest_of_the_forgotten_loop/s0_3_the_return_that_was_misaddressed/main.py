# Save to: s0_3_the_return_that_was_misaddressed/main.py

def validate_return_routing(return_value, recipient_registry, recipient_id):
    """
    Simulates a return value being routed to a potentially incorrect or missing recipient.

    Args:
        return_value (any): The value intended to be returned.
        recipient_registry (dict): Maps valid recipient IDs to names/functions/etc.
        recipient_id (str): The ID of the recipient the return is intended for.

    Returns:
        bool: True if the return was successfully routed, False if it was misaddressed.
    """
    if recipient_id not in recipient_registry:
        print(f"Return misaddressed: recipient '{recipient_id}' not found.")
        return False
    else:
        print(f"Return delivered to '{recipient_registry[recipient_id]}': {return_value}")
        return True
