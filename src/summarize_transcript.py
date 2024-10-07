import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from helpers.common import json_to_dct, process_text
from helpers.gpt_utils import get_openai_client

PROMPT_TEMPLATE = """
You are given text that was taken from youtube transcripts. It is about a zoom meeting from a software company.
Summarize the meeting, list out action items or a to do list from the meeting, and return the result in markdown format.
For example, here is a meeting summary example for you to follow in format:

Summary:
This meeting focused on updates related to security, government growth, applied ML, MLOps, and the anti-abuse team. Discussions covered team restructuring, with the anti-abuse product moving under data science, which has been renamed from the model ops section. The model ops section includes three groups, while anti-abuse remains a single group for now, with plans to split it into two in the future. Additional changes include updates to workday processes and handbook revisions. The team discussed improving communication, with plans to focus on summarized communication to reduce the signal-to-noise ratio.

There was also an acknowledgment of ongoing work regarding error budgets, reliability, and security incidents, with appreciation expressed for team members' efforts. Notably, a new container security bot was set up by Thiago to automate weekly checks, simplifying the team's workflow. Updates were also given regarding a challenge assessment, with dates expected from mid-October to December.

Action Items:
 - Team Leaders: Expected to attend meetings or read meeting notes, instead of relying on Slack for updates.
 - Anti-Abuse Team: Await future changes to split into two groups, with the timeline still uncertain.
 - Workday Migration: Continue using Google Docs for self-evaluations and manager work until the workday process is fully accessible.
 - Container Security: The team will now rely on an automated bot for weekly checks.
 - Challenge Assessment: Follow-up expected mid-October through December with timeline confirmation pending.
 - Workday Changes: Await demos and confirmation of what changes will be implemented in the system.

# Youtube Transcript Text
{youtube_transcript_text}

Ensure the resulting summary is in markdown format.
"""

def save_to_markdown(captions, categories, output_file):
    with open(output_file, 'w') as md_file:
        for (video_id, summary), category in zip(captions.items(), categories.values()):
            md_file.write(f"## Category: {category}\n\n")
            md_file.write(f"{summary}\n\n")
            md_file.write("---\n\n")

def main(OPENAI_API_KEY):
    openai_client = get_openai_client(OPENAI_API_KEY)

    filtered_captions = json_to_dct("data/filtered_captions.json")

    summarized_captions = process_text(
        filtered_captions, 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Summarizing Captions"
    )

    categories = json_to_dct("data/predicted_categories.json")
    save_to_markdown(summarized_captions, categories, "data/summarized_captions.md")


if __name__ == "__main__":
    main(OPENAI_API_KEY)

