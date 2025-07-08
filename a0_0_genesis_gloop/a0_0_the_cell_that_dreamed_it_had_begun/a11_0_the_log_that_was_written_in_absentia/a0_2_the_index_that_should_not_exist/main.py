# Save as: a11_0_the_log_that_was_written_in_absentia/a0_2_the_index_that_should_not_exist/main.py

def evaluate_index_entry(entry_id):
    """
    Evaluates whether a given index entry is valid, reserved, corrupted, or void.

    Parameters:
    - entry_id (str): The identifier of the index entry.

    Returns:
    - dict: Evaluation result containing status and diagnostic message.
    """
    invalid_entries = {"", None}
    reserved_entries = {"0000", "index_∞", "void_ptr", "unknown", "????"}

    if entry_id in invalid_entries:
        return {
            "status": "void",
            "message": "No entry specified. Index slot is empty."
        }
    elif entry_id in reserved_entries:
        return {
            "status": "corrupted",
            "message": f"Index '{entry_id}' is reserved or malformed. It should not exist."
        }
    elif entry_id.lower().startswith("phantom_"):
        return {
            "status": "phantom",
            "message": f"Index '{entry_id}' refers to a non-event. Ghost pointer logged."
        }
    else:
        return {
            "status": "valid",
            "message": f"Index '{entry_id}' appears structurally sound — but no reference found."
        }

# Optional direct CLI test
if __name__ == "__main__":
    user_input = input("📇 Enter index entry: ").strip()
    result = evaluate_index_entry(user_input)
    print(f"\n📑 Index Analysis:\nStatus : {result['status']}\nMessage: {result['message']}")

