from utils import save_content_to_file
from openai_client import OpenAIClient
from constants import PromptConstants, DEFAULT_FILE_PATH


def generate_transcript(client: OpenAIClient):
    response = client.call_completions_api(
        messages=[
            {
                "role": "system",
                "content": PromptConstants.TRANSCRIPT_GENERATION_SYSTEM_PROMPT,
            },
            {"role": "user", "content": PromptConstants.TRANSCRIPT_GENERATION_PROMPT},
        ],
    )
    if response:
        transcript = response.choices[0].message.content
        file_path = save_content_to_file(DEFAULT_FILE_PATH, transcript)
    return file_path
