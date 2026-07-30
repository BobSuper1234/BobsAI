
import json
import datetime
import platform
import time
import os


with open("settings.json", "r") as file:
    settings = json.load(file)


def antigravity():

    print("\nInitiating antigravity sequence...\n")

    for i in range(0, 101, 20):
        bar = "█" * (i // 10)
        empty = "░" * (10 - (i // 10))

        print(f"[{bar}{empty}] {i}%")
        time.sleep(0.4)

    return """
Antigravity enabled. 🚀

Gravity.exe has been politely asked to stop.
"""


def command(message):

    msg = message.lower()


    if msg == "help":
        return """
Available commands:

help
time
system info
antigravity
clear
exit
"""


    elif msg == "time":
        return str(datetime.datetime.now())


    elif msg == "system info":
        return (
            f"Operating System: {platform.system()}\n"
            f"Processor: {platform.processor()}"
        )


    elif msg == "antigravity":
        return antigravity()


    elif msg == "clear":
        os.system("cls")
        return "Screen cleared."


    elif msg == "exit":
        print("BobAI shutting down...")
        exit()


    else:
        return "I don't know that command yet."


print("==========================")
print(f"{settings['name']} v{settings['version']}")
print("==========================")
print("Type 'help' for commands.\n")


while True:

    user = input("You: ")

    response = command(user)

    print("\n" + settings["prefix"] + ": " + response)
    print()
