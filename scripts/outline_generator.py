import os
from config import PROMPT_FOLDER
from llm_client import call_llm


def load_prompt():
    path = os.path.join(PROMPT_FOLDER, "outline_prompt.txt")
    with open(path, "r") as f:
        return f.read()


def generate_outline(notes):

    prompt = load_prompt().replace("{NOTES}", notes)

    return call_llm(prompt)