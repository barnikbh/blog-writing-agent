from openai import OpenAI
from config import GROQ_API_KEY

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


def call_llm(prompt):

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=prompt
    )

    return response.output_text