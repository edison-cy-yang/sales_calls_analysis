from transcript_generator import generate_transcript
from summarize_transcript import summarize_transcript


def main():
    # generate the call script
    file_path = generate_transcript()
    # summarize the transcript
    summarize_transcript(file_path)
    # answer user query


if __name__ == "__main__":
    main()
