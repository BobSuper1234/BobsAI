import os
import json

try:
    from llama_cpp import Llama
except ImportError:
    raise ImportError(
        "llama-cpp-python is not installed. "
        "Install it before running BobAI."
    )


class BobBrain:

    def __init__(self):

        with open("settings.json", "r", encoding="utf-8") as file:
            self.settings = json.load(file)


        self.memory = self.load_memory()


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


    def load_memory(self):

        if not self.settings["save_memory"]:
            return {
                "user_name": "",
                "facts": [],
                "preferences": [],
                "conversation_history": []
            }


        if not os.path.exists(self.settings["memory_file"]):
            return {
                "user_name": "",
                "facts": [],
                "preferences": [],
                "conversation_history": []
            }


        with open(
            self.settings["memory_file"],
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(file)


    def save_memory(self):

        if not self.settings["save_memory"]:
            return


        with open(
            self.settings["memory_file"],
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                self.memory,
                file,
                indent=4
            )


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


        answer = response["choices"][0]["text"].strip()


        if self.settings["save_memory"]:

            self.memory["conversation_history"].append(
                {
                    "user": message,
                    "assistant": answer
                }
            )

            self.save_memory()


        return answer