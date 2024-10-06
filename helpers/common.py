import json
from tqdm import tqdm

from .gpt_utils import build_prompt, gpt_response

def json_to_dct(json_file):
    with open(json_file, 'r') as file:
        dct = json.load(file)
    return dct

def process_text(captions_dict, openai_client, PROMPT_TEMPLATE, description="Processing Captions"):
    processed_captions = {}

    for video_id, data in tqdm(captions_dict.items(), desc=description, unit="video"):
        category = data['category']
        text = data['captions']
        prompt = build_prompt(PROMPT_TEMPLATE, text)

        processed_text = gpt_response(prompt, openai_client)
        processed_data = {
            "category": category,
            "captions": processed_text
        }

        processed_captions[video_id] = processed_data

    return processed_captions