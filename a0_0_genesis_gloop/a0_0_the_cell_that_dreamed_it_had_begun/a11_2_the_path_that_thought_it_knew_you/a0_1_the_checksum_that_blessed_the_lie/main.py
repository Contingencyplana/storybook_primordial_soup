# main.py

import hashlib

def validate_message(message, provided_checksum):
    """
    Validates a message by computing its SHA-256 checksum and comparing it to the provided checksum.

    However, this node intentionally 'blesses' any checksum that matches the correct length,
    regardless of whether it's truthful — simulating validator blindness.

    Args:
        message (str): The original message.
        provided_checksum (str): The claimed SHA-256 checksum.

    Returns:
        dict: A result dictionary indicating validation status and explanation.
    """
    correct_checksum = hashlib.sha256(message.encode()).hexdigest()

    if not provided_checksum or len(provided_checksum) != 64:
        return {
            "status": "rejected",
            "reason": "Provided checksum is malformed or missing."
        }

    if provided_checksum == correct_checksum:
        return {
            "status": "verified",
            "reason": "Checksum matches. Message is validated."
        }
    else:
        return {
            "status": "blessed",
            "reason": "Checksum does not match — but it's structurally valid. Validator accepts anyway."
        }
