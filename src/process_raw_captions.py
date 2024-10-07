import json
from helpers.common import json_to_dct

def remove_categories(captions_dct: dict) -> dict:
    """
    This function removes categories from the captions dictionary.
    Unseen data won't have categories so we want to build the rest of the pipeline without categories.
    But we still want to keep them in the original raw data file so that we can compare predicted categories later on.
    
    Parameters:
    - captions_dct (dict): A dictionary where each key is a video ID and the value is another dictionary containing the video's category and its captions.

    Returns:
    dict: A dictionary where each key is a video ID and the value is the video's captions without the category.
    """
    processed_captions = {}

    for video_id, data in captions_dct.items():
        caption = data["captions"]
        processed_captions[video_id] = caption

    return processed_captions

if __name__ == "__main__":
    captions_dct = json_to_dct("data/raw_captions_data.json")

    captions_without_cats = remove_categories(captions_dct)

    with open('data/captions_without_cats.json', 'w') as json_file:
        json.dump(captions_without_cats, json_file, indent=4)
    