import os
from config import PROMPT_FOLDER
from llm_client import call_llm


def load_prompt(name):
    path = os.path.join(PROMPT_FOLDER, name)
    with open(path, "r") as f:
        return f.read()


def edit_blog(blog):

    prompt = load_prompt("edit_prompt.txt")
    examples = load_prompt("style_examples.txt")

    prompt = prompt.replace("{STYLE_EXAMPLES}", examples)
    prompt = prompt.replace("{BLOG}", blog)

    return call_llm(prompt)