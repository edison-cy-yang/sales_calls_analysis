from utils import read_from_file
from openai_client import OpenAIClient
from constants import PromptConstants


def summarize_transcript(client: OpenAIClient, file_path: str):
    transcript = read_from_file(file_path)
    response = client.call_completions_api(
        messages=[
            {
                "role": "system",
                "content": PromptConstants.SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": f"{PromptConstants.SUMMARIZE_TRANSCRIPT_PROMPT}\n{transcript}",
            },
        ],
    )
    summary = response.choices[0].message.content
    print(f"\nSummary of the sales call at {file_path}:\n\n{summary}")
