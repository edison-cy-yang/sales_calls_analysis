import unittest
from unittest.mock import patch, MagicMock
from summarize_transcript import summarize_transcript  # Import your function
from openai_client import OpenAIClient
from constants import PromptConstants

TEST_SUMMARIZED_TRANSCRIPT = "Summarized transcript."
TEST_FILE_PATH = "file_path.txt"
TEST_TRANSCRIPT_CONTENT = "Test transcript."


class TestSummarizeTranscript(unittest.TestCase):
    @patch("summarize_transcript.read_from_file")
    @patch.object(OpenAIClient, "call_completions_api")
    def test_summarize_transcript(self, mock_call_completions_api, mock_read_from_file):
        # Mock the return value of read_from_file
        mock_read_from_file.return_value = TEST_TRANSCRIPT_CONTENT

        mock_message = MagicMock()
        mock_message.content = TEST_SUMMARIZED_TRANSCRIPT
        mock_response = MagicMock()
        mock_response.choices = [mock_message]
        mock_call_completions_api.return_value = mock_response

        client = OpenAIClient()
        summarize_transcript(client, TEST_FILE_PATH)

        # Assert
        mock_read_from_file.assert_called_once_with(TEST_FILE_PATH)
        mock_call_completions_api.assert_called_once_with(
            messages=[
                {
                    "role": "system",
                    "content": PromptConstants.SUMMARIZE_TRANSCRIPT_SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": f"{PromptConstants.SUMMARIZE_TRANSCRIPT_PROMPT}\n{TEST_TRANSCRIPT_CONTENT}",
                },
            ]
        )

        self.assertEqual(mock_response.choices[0].content, TEST_SUMMARIZED_TRANSCRIPT)


if __name__ == "__main__":
    unittest.main()
