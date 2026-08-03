import os
import json
from llama_cpp import Llama


class BobBrain:

    def __init__(self):

        try:
            with open("settings.json", "r", encoding="utf-8") as file:
                self.settings = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(
                "settings.json was not found!"
            )


        model_path = os.path.join(
            self.settings["models_folder"],
            self.settings["model"]
        )


        if not os.path.exists(model_path):
            raise FileNotFoundError(
                f"AI model was not found:\n{model_path}"
            )


        print("Loading AI model...")
        
        self.model = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4
        )

        print("AI model loaded!")


    def chat(self, message):

        response = self.model(
            f"""
You are BobAI, a friendly local AI assistant.

You run locally on the user's computer.
Be helpful, clear, and friendly.

User:
{message}

BobAI:
""",
            max_tokens=200,
            temperature=0.7
        )


        return response["choices"][0]["text"].strip()