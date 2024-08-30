from openai import OpenAI
import os
from utils import read_from_file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

SUMMARIZE_TRANSCRIPT_PROMPT = (
    "Summarize the following sales call transcript into key bullet points"
)

SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT = (
    "You are a helpful assistant who summarizes transcripts into key bullet points."
)


def summarize_transcript(file_path):
    transcript = read_from_file(file_path)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT,
            },
            {"role": "user", "content": f"{SUMMARIZE_TRANSCRIPT_PROMPT}\n{transcript}"},
        ],
    )
    summary = response.choices[0].message.content
    print(summary)
