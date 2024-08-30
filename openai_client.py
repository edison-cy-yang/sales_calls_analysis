import os
from openai import OpenAI
from constants import OpenAIConstants

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


class OpenAIClient:
    def __init__(self):
        self.api_key = OPENAI_API_KEY
        if not self.api_key:
            raise ValueError("API key for OpenAI is required.")

        self.client = OpenAI(api_key=self.api_key)

    def call_completions_api(
        self,
        messages: list,
        model=OpenAIConstants.GPT_MODEL_4,
        temperature=OpenAIConstants.GPT_DEFAULT_TEMPERATURE,
    ):
        response = self.client.chat.completions.create(
            model=model, messages=messages, temperature=temperature
        )

        return response
