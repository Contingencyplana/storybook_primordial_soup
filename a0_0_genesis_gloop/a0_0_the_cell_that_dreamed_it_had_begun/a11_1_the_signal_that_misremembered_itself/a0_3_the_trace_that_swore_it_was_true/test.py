# 🧪 test.py – Truth Assertion Without Origin Test
# Interactive tool for evaluating whether a self-assured trace is trustworthy
# when the system has no memory of its source.

from main import evaluate_trace

print("📜 Truth Test – The Trace That Swore It Was True")
print("Enter a trace and optionally provide a list of known origins.")
print("The system will decide whether to accept the trace as true.")
print("Type 'exit' to quit.\n")

while True:
    trace = input("🧾 Trace: ")
    if trace.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    origins_input = input("📚 Known origins (comma-separated or blank if none): ")
    if origins_input.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    known_origins = [o.strip() for o in origins_input.split(",") if o.strip()] if origins_input else []

    result = evaluate_trace(trace, known_origins)
    print(f"{'✅' if result['status'] == 'accepted' else '❌'} {result['status'].capitalize()} – {result['reason']}\n")
