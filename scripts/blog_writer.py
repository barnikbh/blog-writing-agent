import os
from config import PROMPT_FOLDER
from llm_client import call_llm


def load_prompt():
    path = os.path.join(PROMPT_FOLDER, "blog_prompt.txt")
    with open(path, "r") as f:
        return f.read()


def generate_blog(outline, notes):

    prompt = load_prompt()

    prompt = prompt.replace("{OUTLINE}", outline)
    prompt = prompt.replace("{NOTES}", notes)

    return call_llm(prompt)