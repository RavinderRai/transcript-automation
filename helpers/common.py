import json
from tqdm import tqdm

from .gpt_utils import build_prompt, gpt_response

def json_to_dct(json_file):
    with open(json_file, 'r') as file:
        dct = json.load(file)
    return dct

def process_text(
    captions_dict: dict, 
    openai_client: object, 
    PROMPT_TEMPLATE: str, 
    description: str = "Processing Captions",
) -> dict:
    """
    Processes captions in a dictionary by sending them to an OpenAI client for processing.

    Args:
    - captions_dict (dict): A dictionary containing video IDs as keys and 'captions' as values.
    - openai_client (object): An instance of an OpenAI client for processing text.
    - PROMPT_TEMPLATE (str): A template string for building prompts to send to the OpenAI client.
    - description (str, optional): A description for the tqdm progress bar. Defaults to "Processing Captions".

    Returns:
    - dict: A dictionary with the same structure as captions_dict, but with processed captions.
    """
    processed_captions = {}

    for video_id, text in tqdm(captions_dict.items(), desc=description, unit="video"):
        prompt = build_prompt(PROMPT_TEMPLATE, text)

        processed_text = gpt_response(prompt, openai_client)
        processed_captions[video_id] = processed_text

    return processed_captions

#in case you need to process the raw data with categories
def process_text_with_categories(json_file, openai_client, PROMPT_TEMPLATE, description="Processing Captions"):
    """
    Processes captions in a dictionary by sending them to an OpenAI client for processing.

    Args:
    - captions_dict (dict): A dictionary containing video IDs as keys and dictionaries with 'category' and 'captions' as values.
    - openai_client (object): An instance of an OpenAI client for processing text.
    - PROMPT_TEMPLATE (str): A template string for building prompts to send to the OpenAI client.
    - description (str, optional): A description for the tqdm progress bar. Defaults to "Processing Captions".
    - processed_text_name (str, optional): A different name for the resulting LLM outputs. 
        Normally this will just be processed captions, but you can optionally adjust it based on the prompt.

    Returns:
    - dict: A dictionary with the same structure as captions_dict, but with processed captions.
    """
    processed_captions = {}

    with open(json_file, 'r') as file:
        captions_dict = json.load(file)

    for video_id, data in tqdm(captions_dict.items(), desc=description, unit="video"):
        category = data['category']
        text = data['captions']
        prompt = build_prompt(PROMPT_TEMPLATE, text)

        # Call gpt_response and store the cleaned text
        cleaned_text = gpt_response(prompt, openai_client)  # Store the response in a separate variable
        processed_data = {
            "category": category,
            "captions": cleaned_text  # Use cleaned_text here
        }

        processed_captions[video_id] = processed_data  # Assign to the dictionary

    return processed_captions