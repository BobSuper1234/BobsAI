from ai.engine import BobBrain
from config import APP_NAME, APP_VERSION


brain = BobBrain()

print("==============================")
print(APP_NAME)
print("Version:", APP_VERSION)
print("==============================")
print()

print("BobsAI online!")
print("Type exit to close.\n")


while True:

    user = input("You: ")

    if user.lower() == "exit":
        print("Closing BobsAI...")
        break

    answer = brain.chat(user)

    print("\nBobsAI:", answer)