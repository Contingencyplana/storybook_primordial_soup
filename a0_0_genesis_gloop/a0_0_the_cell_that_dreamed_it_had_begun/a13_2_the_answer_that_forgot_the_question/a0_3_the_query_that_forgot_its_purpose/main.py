# 📂 a0_3_the_query_that_forgot_its_purpose/main.py

def recursive_query_ping(query: str, depth: int = 3) -> list:
    """
    Recursively processes a query that has lost its original purpose.
    Each recursive step degrades the query, stripping context or logic.

    Args:
        query (str): The original query string.
        depth (int): Number of recursive passes before collapse.

    Returns:
        list: A trace log of recursive degeneration.
    """
    if not query or len(query.strip()) < 5:
        return ["❌ Query rejected: too vague to recurse."]

    trace = [f"🔍 Initial Query: {query.strip()}"]
    current = query.strip()

    for i in range(1, depth + 1):
        # Simulate recursion decay: lose structure or content
        if len(current.split()) > 1:
            current = " ".join(current.split()[1:])  # Trim the first word
        else:
            current = "..."

        if current == "..." or not current.strip():
            trace.append(f"⚠️ Depth {i}: recursion voided – no content remains.")
            break
        else:
            trace.append(f"🔁 Depth {i}: {current}")

    trace.append("🧩 Final State: query loop terminated.")
    return trace
