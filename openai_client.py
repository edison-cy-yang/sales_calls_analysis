import os
from openai import OpenAI
from constants import OpenAIConstants, PromptConstants

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
        language="en",
    ):
        if language != "en":
            messages.insert(
                0,
                {
                    "role": "system",
                    "content": PromptConstants.OTHER_LANGUAGE_SYSTEM_PROMPT.format(
                        language=language
                    ),
                },
            )
        try:
            response = self.client.chat.completions.create(
                model=model, messages=messages, temperature=temperature
            )
        except Exception as e:
            print(f"Something went wrong making OpenAI completions call: {e}")

        return response
