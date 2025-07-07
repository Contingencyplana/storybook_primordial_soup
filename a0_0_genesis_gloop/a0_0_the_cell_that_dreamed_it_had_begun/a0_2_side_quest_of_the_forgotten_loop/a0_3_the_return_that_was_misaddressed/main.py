# 📄 main.py
# Path: a0_2_side_quest_of_the_forgotten_loop/a0_3_the_return_that_was_misaddressed/main.py

def route_return_signal(destination_registry, signal_id, return_address):
    """
    Checks if a return signal reaches a known destination.

    Parameters:
        destination_registry (set): Known valid destination addresses
        signal_id (str): Identifier for the signal being returned
        return_address (str): Address the signal is attempting to return to

    Returns:
        dict: Routing outcome including delivery status and consequences
    """
    if return_address not in destination_registry:
        return {
            "signal_id": signal_id,
            "status": "❌ Misaddressed",
            "delivered": False,
            "error": "Return address not recognized",
            "consequence": "Signal lost in recursion"
        }
    else:
        return {
            "signal_id": signal_id,
            "status": "✅ Delivered",
            "delivered": True,
            "error": None,
            "consequence": "Loop integrity maintained"
        }
