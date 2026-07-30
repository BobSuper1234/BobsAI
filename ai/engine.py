from llama_cpp import Llama


class BobBrain:

    def __init__(self):

        self.model = Llama(
            model_path="models/qwen2.5-0.5b-q4.gguf",
            n_ctx=2048,
            n_threads=4
        )


    def chat(self, message):

        response = self.model(
            f"""
You are BobAI, a friendly local AI assistant.

User:
{message}

BobAI:
""",
            max_tokens=200,
            temperature=0.7
        )

        return response["choices"][0]["text"].strip()
