from utils import read_from_file
from openai_client import OpenAIClient
from constants import PromptConstants


def answer_query_from_transcript(
    client: OpenAIClient, file_path: str, query: str, language="en", db=None
):
    transcript = read_from_file(file_path)

    user_query_prompt = PromptConstants.ANSWER_QUERY_PROMPT_TEMPLATE.format(
        transcript=transcript, query=query
    )

    response = client.call_completions_api(
        messages=[
            {
                "role": "system",
                "content": PromptConstants.ANSWER_QUERY_SYSTEM_PROMPT,
            },
            {"role": "user", "content": user_query_prompt},
        ],
        language=language,
    )
    if response:
        answer = response.choices[0].message.content
        print(f"\nResponse of the query '{query}':\n{answer}")
        # Only store query and response to db if it exists
        if db:
            db.store_query_response(query, answer)
