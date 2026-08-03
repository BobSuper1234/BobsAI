from ai.engine import BobBrain


brain = BobBrain()

print("BobAI online!")
print("Type exit to close.\n")


while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    answer = brain.chat(user)

    print("\nBobAI:", answer)