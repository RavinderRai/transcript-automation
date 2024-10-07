import os
import json
from tqdm import tqdm
from dotenv import load_dotenv, find_dotenv

from helpers.common import json_to_dct, process_text
from helpers.gpt_utils import get_openai_client

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


PROMPT_TEMPLATE = """
You are given text that was taken from a zoom meeting from a software company (GitLab).
There are only 3 meeting topics: data science, engineering, and CI/CD UX.
Remove parts of the meeting where the attendees are doing small talk, or chatting about things not relevant to software or the main topic. 
Therefore, the resulting text should be the meeting with text from people speaking about only relevant things to one of the topics.

# Youtube Transcript Text
{youtube_transcript_text}
"""

def filter_transcript(OPENAI_API_KEY):
    openai_client = get_openai_client(OPENAI_API_KEY)

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    cleaned_captions_path = os.path.join(data_dir, "cleaned_captions.json")
    filtered_captions_path = os.path.join(data_dir, "filtered_captions.json")

    cleaned_captions = json_to_dct(cleaned_captions_path)

    filtered_captions = process_text(
        cleaned_captions, 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Filtering Captions"
    )

    with open(filtered_captions_path, 'w') as json_file:
        json.dump(filtered_captions, json_file, indent=4)

if __name__ == "__main__":
    filter_transcript(OPENAI_API_KEY)