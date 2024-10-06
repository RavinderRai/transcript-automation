import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv(load_dotenv(find_dotenv()))

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from helpers.common import json_to_dct, process_text
from helpers.gpt_utils import get_openai_client

PROMPT_TEMPLATE = """
You are given text that was taken from youtube transcripts. It is about a zoom meeting from a software company.
Summarize the meeting and list out action items or a to do list from the meeting.
For example, here is a meeting and it's summary for you to replicate:

Original Caption Text:
So, it is the second meeting regarding security and government growth and data science, meaning applied ML, ML Ops, and anti-abuse team meeting. That's a big mouthful, we might get a better name over time. And that's our meeting for September 14th or 15th in APAC. Hi Alan, glad you're here! Why are you here when it's midnight? We can talk. Glad you're here. Don't make it hard to come to this meeting because it's really late for you. And maybe so, but I'm glad. Thanks for coming at least once.\n\nNews and events: I've got a lot of things on the agenda today because of some of this. So apologies for that, but I think it's going to go down over time based on feedback. I'll work. I'm going to work to do more summarized communications to improve the signal-to-noise ratio in my communications to groups of people, including this group of people. This was working for this group, adding more items to our staff meeting agenda often every only rather than posting on your slack channel. I am going to be assuming that people, leaders of the team, will attend this meeting or read the notes and not rely on the slack channel, so keep that in mind.\n\nThe next item is that anti-abuse is moving product sections from sick to data science. Data science is effectively a rename of the model ops section. So data science will include two stages, the existing model ops, which has three groups in it, which one can talk more about, and the anti-abuse stage, which only currently has one group called anti-abuse. I think at some point there are plans to split anti-abuse into two groups, but that's not in the near future, and we're working through all the changes around that. There's lots of workday changes, lots of handbook changes. Mom, did you want to say anything more about data science or model ops?\n\nOh, I think for us, we just roll up to data science, so everything else stays the same. We still have the two main groups, applied mallops and the later data ops as part of it. Yeah, so thanks, Thomas, for continuing to compile and report on all of my teams that I'm responsible for in the engineering allocation meetings on error budgets and reliability and security incidents. So really do appreciate that. Gotta give Neal a high five too, he does that. He does half of these now. And apologies for the noise if I keep asking for what's the story behind what's going on with reliability or security or error budget stuff, just trying to provide your cover. And I apologize, Neal, I totally forgot you took half a day since Thomas has been doing it for so long, but appreciating you. I know you volunteered for it, and we discussed it, but I just forgot, kind of a thankless role, honestly.\n\nI volunteered because of the exposure I get from it. It's nice to be part of a different collective group of people. I was going to mention, I'll type this in here, but Thiago has set up container security, a bot that weekly, I think it's Mondays or Sundays, will ping the team and ask for a volunteer to go and resource that data and we just enabled it for threat insights. It's actually pretty sweet, and it just does all the work for you, Thomas, right? We don't have to ping people ourselves. So I'll put a note in there for that. Hey F is read-only, and Bill, you've got G, challenge assessment. So we had an update from Julia, the dates haven't been confirmed yet, but it'll be sometime from mid-October through till December. I think e-group sign-off is expected to be mid-December before everyone goes on holiday. They've got a draft timeline in there, but the dates, the dates aren't in the handbook yet. The big changes we're moving to do on workday, that's not available yet. I haven't seen a demo of it. I don't know what questions will be asked, but there's an optional self-evaluation which will move in to workday and the work that we do as managers will also happen in workday. At the moment, some people are using the Google Doc which is listed on the talent assessment page for self-evaluations and for the manager work, I'd suggest continuing to use those docs until we get access to workday and see what the exact differences are. Each A and J are read-only unless anybody wants to discuss them. Thomas, you get Adam K.\n\nApologies for the late live addition to the agenda on this one, but one more note on a change we're rolling out within secure. Pretty lightweight and that we're establishing a second team within Dynamic Analysis and so, issue is there where folks want to pla... (The message is truncated)

Summarized Version:
Summary:
This meeting focused on updates related to security, government growth, applied ML, MLOps, and the anti-abuse team. Discussions covered team restructuring, with the anti-abuse product moving under data science, which has been renamed from the model ops section. The model ops section includes three groups, while anti-abuse remains a single group for now, with plans to split it into two in the future. Additional changes include updates to workday processes and handbook revisions. The team discussed improving communication, with plans to focus on summarized communication to reduce the signal-to-noise ratio.

There was also an acknowledgment of ongoing work regarding error budgets, reliability, and security incidents, with appreciation expressed for team members' efforts. Notably, a new container security bot was set up by Thiago to automate weekly checks, simplifying the team's workflow. Updates were also given regarding a challenge assessment, with dates expected from mid-October to December.

Action Items / To-Do List:
Team Leaders: Expected to attend meetings or read meeting notes, instead of relying on Slack for updates.
Anti-Abuse Team: Await future changes to split into two groups, with the timeline still uncertain.
Workday Migration: Continue using Google Docs for self-evaluations and manager work until the workday process is fully accessible.
Container Security: The team will now rely on an automated bot for weekly checks.
Challenge Assessment: Follow-up expected mid-October through December with timeline confirmation pending.
Workday Changes: Await demos and confirmation of what changes will be implemented in the system.


# Youtube Transcript Text
{youtube_transcript_text}
"""


if __name__ == "__main__":
    openai_client = get_openai_client(OPENAI_API_KEY)

    filtered_captions = json_to_dct("data/filtered_captions.json")

    summarized_captions = process_text(
        filtered_captions, 
        openai_client, 
        PROMPT_TEMPLATE, 
        "Filtering Captions"
    )

    with open('data/cleaned_captions.json', 'w') as json_file:
        json.dump(summarized_captions, json_file, indent=4)

