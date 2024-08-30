from utils import read_from_file
from openai_client import OpenAIClient

ANSWER_QUERY_SYSTEM_PROMPT = "You are a helpful assistant who answers queries about a sales call based on call transcripts."


def anwer_query_from_transcript(client: OpenAIClient, file_path: str, query: str):
    transcript = read_from_file(file_path)

    user_prompt = f"This is the transcript of a sales call: \n {transcript}\n\nBased on the above sales transcript, answer the question {query}"
    response = client.call_completions_api(
        messages=[
            {
                "role": "system",
                "content": ANSWER_QUERY_SYSTEM_PROMPT,
            },
            {"role": "user", "content": user_prompt},
        ],
    )
    answer = response.choices[0].message.content
    print(f"Response of the query '{query}':\n{answer}")
