# 🧪 test.py – Premature Knowledge Detection Interface
# Interactive test: Enter a prompt and a reply.
# The system will flag replies that include unauthorized knowledge
# not derivable from the prompt context.

from main import detect_unauthorized_knowledge

print("📜 Premature Recall Test – The Reply That Knew Too Much")
print("Type a prompt and a reply. The system will analyze whether the reply")
print("contains any unauthorized knowledge – i.e., information it wasn't given.")
print("Type 'exit' to quit.\n")

while True:
    prompt = input("🧠 Prompt: ")
    if prompt.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    reply = input("🗣️ Reply: ")
    if reply.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    unauthorized = detect_unauthorized_knowledge(prompt, reply)
    if unauthorized:
        print(f"⚠️ Unauthorized knowledge detected: {', '.join(sorted(unauthorized))}\n")
    else:
        print("✅ Reply accepted – no unauthorized knowledge found.\n")
