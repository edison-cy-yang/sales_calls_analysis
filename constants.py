class OpenAIConstants:
    GPT_MODEL_3_5 = "gpt-3.5-turbo"
    GPT_MODEL_4 = "gpt-4o"
    GPT_DEFAULT_TEMPERATURE = 1.0


class PromptConstants:
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
    SUMMARIZE_TRANSCRIPT_PROMPT = (
        "Summarize the following sales call transcript into key bullet points"
    )
    SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT = (
        "You are a helpful assistant who summarizes transcripts into key bullet points."
    )
    ANSWER_QUERY_SYSTEM_PROMPT = "You are a helpful assistant who answers queries about a sales call based on call transcripts."
    ANSWER_QUERY_PROMPT_TEMPLATE = "This is the transcript of a sales call: \n {transcript}\n\nBased on the above sales transcript, answer the question {query}"
    OTHER_LANGUAGE_SYSTEM_PROMPT = (
        "You are a multi-lingual assistant that responds in {language}"
    )


class UserQueries:
    USER_QUERY_PRODUCT_INTERESTED_IN = "what product is the customer interested in?"
    USER_QUERY_PRICE = "what is the price of the product?"


DEFAULT_FILE_PATH = "sales_call_transcripts.txt"
