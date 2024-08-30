from utils import read_from_file
from openai_client import OpenAIClient

SUMMARIZE_TRANSCRIPT_PROMPT = (
    "Summarize the following sales call transcript into key bullet points"
)

SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT = (
    "You are a helpful assistant who summarizes transcripts into key bullet points."
)


def summarize_transcript(client: OpenAIClient, file_path: str):
    transcript = read_from_file(file_path)
    response = client.call_completions_api(
        messages=[
            {
                "role": "system",
                "content": SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT,
            },
            {"role": "user", "content": f"{SUMMARIZE_TRANSCRIPT_PROMPT}\n{transcript}"},
        ],
    )
    summary = response.choices[0].message.content
    print(f"Summary of the sales call at {file_path}:\n\n{summary}")
