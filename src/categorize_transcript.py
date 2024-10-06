import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from helpers.common import process_text
from helpers.gpt_utils import get_openai_client

PROMPT_TEMPLATE = """
You are given text that was taken from youtube transcripts. It is about a zoom meeting from a software company.
You need to identify the category of the meeting, of which there are 3: data science, engineering, and CI/CD UX.
Determine which category the transcript text belongs to. 
Return the relevant category label to follow this syntax: data_science, engineering, or cicd_ux.

# Youtube Transcript Text
{youtube_transcript_text}
"""


if __name__ == "__main__":
    openai_client = get_openai_client(OPENAI_API_KEY)

    cleaned_captions = process_text(
        "data/captions.json", 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Filtering Captions"
    )
    with open('data/cleaned_captions.json', 'w') as json_file:
        json.dump(cleaned_captions, json_file, indent=4)
