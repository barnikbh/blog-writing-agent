import re
import os
from llm_client import call_llm
from config import PROMPT_FOLDER


def load_prompt():

    path = os.path.join(PROMPT_FOLDER, "diagram_prompt.txt")

    with open(path, "r") as f:
        return f.read()


def generate_diagram(description):

    prompt_template = load_prompt()

    prompt = prompt_template.replace("{DESCRIPTION}", description)

    mermaid_code = call_llm(prompt)

    return f"```mermaid\n{mermaid_code}\n```"


def replace_diagrams(text):

    pattern = r"<insert image:\s*(.*?)>"

    matches = re.findall(pattern, text)

    for desc in matches:

        desc = desc.strip()

        diagram = generate_diagram(desc)

        text = text.replace(f"<insert image: {desc}>", diagram)

    return text