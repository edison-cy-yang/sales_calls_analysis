from openai import OpenAI
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

SUMMARIZE_TRANSCRIPT_PROMPT = (
    "Summarize the following sales call transcript into key bullet points"
)

SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT = (
    "You are a helpful assistant who summarizes transcripts into key bullet points."
)


def read_from_file(file_path):
    try:
        # Open the file and read its content
        with open(file_path, "r") as file:
            transcript = file.read()

        # Print the read transcript (optional)
        print("Transcript read from file")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except IOError as e:
        print(f"Error occurred reading the file: {e}")
        return None

    return transcript


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
