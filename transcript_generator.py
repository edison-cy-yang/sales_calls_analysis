from openai import OpenAI
import os
from utils import save_content_to_file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

TRANSCRIPT_GENERATION_PROMPT = (
    "Generate a realistic sales call transcript between two people."
    "The call should center around a product, and its pricing."
    "Please include timestamps and identify the speakers. Format the transcript like the example below:\n\n"
    """
		00:00:00 Sam (openai.com): Hey there Staya.
		00:00:02 Satya  (microsoft.com): Hi Sam, how are you?
		00:00:05 Sam (openai.com): I'm doing good. Do you think you can give us 10000 more GPUs?
		00:00:06 Satya (microsoft.com): I'm sorry Sam we can't do 10000, how about 5000?
	"""
)

TRANSCRIPT_GENERATION_SYSTEM_PROMPT = (
    "You are a helpful assistant who can create conversation transcripts."
)

DEFAULT_FILE_PATH = "sales_call_transcripts.txt"


def generate_transcript():
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": TRANSCRIPT_GENERATION_SYSTEM_PROMPT,
            },
            {"role": "user", "content": TRANSCRIPT_GENERATION_PROMPT},
        ],
    )
    transcript = response.choices[0].message.content
    file_path = save_content_to_file(DEFAULT_FILE_PATH, transcript)
    return file_path
