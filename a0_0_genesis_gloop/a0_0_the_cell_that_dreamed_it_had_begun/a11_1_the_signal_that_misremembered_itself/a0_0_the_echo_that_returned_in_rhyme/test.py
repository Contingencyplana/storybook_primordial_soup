# test.py

from main import return_rhymed_echo

print("📜 Echo Test – The Echo That Returned in Rhyme")
print("Type a message and receive a rhymed echo.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("🗣️ Message: ")
    if user_input.lower() in ['exit', 'quit']:
        print("🔚 Ending test.")
        break

    echoed = return_rhymed_echo(user_input)
    print(f"🔁 Echoed: {echoed}\n")
