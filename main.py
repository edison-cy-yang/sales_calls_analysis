from transcript_generator import generate_transcript
from summarize_transcript import summarize_transcript
from answer_query_from_transcript import answer_query_from_transcript
from constants import UserQueries
from openai_client import OpenAIClient
from mongo_db import MongoClient


def main():
    # Create OpenAI client
    client = OpenAIClient()

    db_client = MongoClient()

    # generate the call script
    file_path = generate_transcript(client)

    # summarize the transcript
    summarize_transcript(client, file_path)

    # answer user query
    answer_query_from_transcript(client, file_path, UserQueries.USER_QUERY_PRICE)


if __name__ == "__main__":
    main()
