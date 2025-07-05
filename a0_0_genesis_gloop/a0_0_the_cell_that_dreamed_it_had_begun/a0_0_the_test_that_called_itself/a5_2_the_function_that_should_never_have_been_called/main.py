# a5_2_the_function_that_should_never_have_been_called/main.py

def forbidden_function():
    raise RuntimeError("⚠️ This function should never have been called.")

def call_with_warning(allow=False):
    """
    Attempts to call a function that should not be invoked under normal logic.
    """
    if not allow:
        return {
            "status": "blocked",
            "message": "Call to forbidden function was prevented."
        }
    try:
        forbidden_function()
    except RuntimeError as e:
        return {
            "status": "violation",
            "message": str(e)
        }
