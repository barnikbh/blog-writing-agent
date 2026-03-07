import os
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SRC_FOLDER = os.path.join(BASE_DIR, "src")
DRAFT_FOLDER = os.path.join(BASE_DIR, "drafts")

PROMPT_FOLDER = os.path.join(BASE_DIR, "scripts", "prompts")

load_dotenv(os.path.join(BASE_DIR, ".env"))

GROQ_API_KEY = os.getenv("GROQ_API_KEY")