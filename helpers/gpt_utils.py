from openai import OpenAI

def get_openai_client(open_api_key):
    gpt_client = OpenAI(api_key=open_api_key)
    return gpt_client

def build_prompt(PROMPT_TEMPLATE: str, text: str) -> str:
    return PROMPT_TEMPLATE.format(youtube_transcript_text=text)

def gpt_response(prompt, openai_client):

    gpt_response = openai_client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="gpt-3.5-turbo",
    )

    return gpt_response.choices[0].message.content