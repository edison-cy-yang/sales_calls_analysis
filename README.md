# Analyze Sales Call Transcripts

## Getting started

Python version used: `3.11.4`

Set up OpenAI API key in environment variable as `OPENAI_API_KEY`

Install dependencies:

```
pip install -r requirements.txt
```

To run the program:

```
python main.py
```

To make the AI answer queries in other languages, add the language parameter for the answer query call in `main.py` like :

```
anwer_query_from_transcript(client, file_path, UserQueries.USER_QUERY_PRICE, "french")
```

## Project Structure

- `constants.py` stores constants like OpenAI models, prompts, and default file path
- `openai_client.py` holds OpenAIClient class, which should be used for any OpenAI API call. If more APIs like assistants, vector store, or audio are introduced, they should be added here
- `utils.py` contains utility functions to read and store file
- `transcript_generator.py` generates sales call transcript and save it as a text file
- `summarize_transcript.py` summarizes the sales call into key bullet points
- `answer_query_from_transcript.py` takes a user query and transcript, answers the query based on the transcript
- `main.py` main file for the project

## Possible Enhancements

### Use assistants API

This project is using chat completions API with transcript input on each call. Assistants API can be used as follows:

- Create an assistant specific for dealing with sales call transcript
- Create a vector store for storing files related to sales call transcripts
- Generate transcript, save as a file, then upload the file with files API
- Create a vector store file with the newly uploaded file
- Create a thread about a specific sales call transcript, ask user query

Doing so, the assistant can have a library of sales call transcripts. We can keep on adding new transcripts, and allow users to ask about a specific call

### Multi-language

- Add the ability for the completions api to just do every call in other languages with a language setting class variable in OpenAIClient
