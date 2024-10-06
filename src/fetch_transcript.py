import json
from youtube_transcript_api import YouTubeTranscriptApi

def fetch_captions(video_id: str) -> str:
    """
    Get the closed captions. 

    Parameters:
    - video_id (str): The video id which is obtained in search_videos.

    Returns:
    String: Closed caption text of a youtube video
    """
    try:
        # Retrieve the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        cc_text = ""

        # Concatenate the transcript text
        for entry in transcript:
            cc_text += ' ' + entry['text']

        cc_text = cc_text.replace('n', ' ')
        return cc_text

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return f"An error occurred: {str(e)}"
    
def fetch_youtube_data():
    """
    Fetches YouTube video captions for specified categories.

    This function retrieves closed captions for a set of YouTube videos categorized into data science, cicd ux, and engineering. The video IDs are sourced from GitLab's YouTube channel. It processes each video, fetches its captions, and stores them in a dictionary along with their category.

    Returns:
    dict: A dictionary where each key is a video ID and the value is another dictionary containing the video's category and its captions.
    """

    data_science_video_ids = ["rOqgRiNMVqg", "Tmd5eKVgySY", "JwBNYjaEwmQ"] #, "HurwHyh0yLc", "qhXYy8Bx5Yc"]
    cicd_ux_video_ids = ["Y33pKPUamCQ", "kGHyK_SkZB0", "HFEFQ4NcgSQ"] #, "T9ZHI7b-k_c", "PdVV1qeD1fE"]
    engineering_video_ids = ["qGFoZ8yodc4", "t-NF5fNOyo8", "GgnkH3uih4o"]

    video_categories = {
        "data_science": data_science_video_ids,
        "cicd_ux": cicd_ux_video_ids,
        "engineering": engineering_video_ids
    }

    captions_dict = {}
    total_videos = sum(len(ids) for ids in video_categories.values())
    processed_count = 0 

    # Processing each video category
    for category, video_ids in video_categories.items():
        for video_id in video_ids:
            captions = fetch_captions(video_id)

            processed_count += 1
            print(f'Processing video ID {video_id} ({processed_count}/{total_videos})')

            # Checking if captions were successfully fetched
            if captions == "":
                print(f'Captions for video ID {video_id} didn\'t work')
            else:
                captions_dict[video_id] = {
                    "category": category,
                    "captions": captions
                }

    # Returning the dictionary of captions
    return captions_dict

if __name__ == "__main__":
    captions_dict = fetch_youtube_data()

    with open('data/captions.json', 'w') as json_file:
        json.dump(captions_dict, json_file, indent=4)