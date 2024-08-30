from transcript_generator import generate_transcript
from summarize_transcript import summarize_transcript
from answer_query_from_transcript import anwer_query_from_transcript


def main():
    # generate the call script
    file_path = generate_transcript()

    # summarize the transcript
    summarize_transcript(file_path)

    # answer user query
    query = "what product is the customer interested in?"
    anwer_query_from_transcript(file_path, query)


if __name__ == "__main__":
    main()
