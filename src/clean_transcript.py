import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from helpers.common import json_to_dct, process_text
from helpers.gpt_utils import get_openai_client

PROMPT_TEMPLATE = """
You are given text that was taken from youtube transcripts. It is about a zoom meeting from a software company.
It is messy, missing characters, has faulty spacing, and is unreadable.
Rewrite the text to fix the grammar, spelling, and puntuation, and thus making it readable and understandable:

# Youtube Transcript Text
{youtube_transcript_text}
"""

def clean_transcript(OPENAI_API_KEY):
    openai_client = get_openai_client(OPENAI_API_KEY)

    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    captions_path = os.path.join(data_dir, "captions_without_cats.json")
    cleaned_captions_path = os.path.join(data_dir, "cleaned_captions.json")

    captions = json_to_dct(captions_path)

    """cleaned_captions = process_text(
        captions, 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Cleaning Captions"
    )"""

    cleaned_captions = {'test1': 'test1'}

    with open(cleaned_captions_path, 'w') as json_file:
        json.dump(cleaned_captions, json_file, indent=4)

if __name__ == "__main__":
    clean_transcript(OPENAI_API_KEY)
