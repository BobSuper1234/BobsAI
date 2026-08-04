from ai.engine import BobBrain


brain = BobBrain()

if brain.settings["show_startup_info"]:
    print("BobAI online!")
    print("Type exit to close.\n")


while True:

    user = input("You: ")

    if user.lower() == "exit":
        print("Closing BobAI...")
        break

    answer = brain.chat(user)

    print("\nBobAI:", answer)