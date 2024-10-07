import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from helpers.common import json_to_dct, process_text
from helpers.gpt_utils import get_openai_client

PROMPT_TEMPLATE = """
You are given text that was taken from youtube transcripts. It is about a zoom meeting from a software company.
You need to identify the category of the meeting, of which there are 3: data science, engineering, and CI/CD UX.
Determine which category the transcript text belongs to. 
Return one of the relevant category labels and follow this syntax: data_science, engineering, or cicd_ux.

# Youtube Transcript Text
{youtube_transcript_text}
"""

def categorize_transcripts(OPENAI_API_KEY):
    openai_client = get_openai_client(OPENAI_API_KEY)

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    cleaned_captions_path = os.path.join(data_dir, "cleaned_captions.json")
    predicted_categories_path = os.path.join(data_dir, "predicted_categories.json")

    cleaned_captions = json_to_dct(cleaned_captions_path)

    predicted_categories = process_text(
        cleaned_captions, 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Predicting Categories",
    )

    with open(predicted_categories_path, 'w') as json_file:
        json.dump(predicted_categories, json_file, indent=4)

if __name__ == "__main__":
    categorize_transcripts(OPENAI_API_KEY)