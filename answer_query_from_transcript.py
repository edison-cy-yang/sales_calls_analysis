from openai import OpenAI
import os
from utils import read_from_file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

ANSWER_QUERY_SYSTEM_PROMPT = "You are a helpful assistant who answers queries about a sales call based on call transcripts."


def anwer_query_from_transcript(file_path, query):
    transcript = read_from_file(file_path)

    user_prompt = f"This is the transcript of a sales call: \n {transcript}\n\nBased on the above sales transcript, answer the question {query}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": ANSWER_QUERY_SYSTEM_PROMPT,
            },
            {"role": "user", "content": user_prompt},
        ],
    )
    answer = response.choices[0].message.content
    print(answer)
