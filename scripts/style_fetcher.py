import os
import feedparser
import requests
from bs4 import BeautifulSoup
from config import PROMPT_FOLDER

MEDIUM_USERNAME = "barnikbh"
MAX_POSTS = 5


def fetch_medium_posts():
    feed_url = f"https://medium.com/feed/@{MEDIUM_USERNAME}"
    feed = feedparser.parse(feed_url)

    posts = []

    for entry in feed.entries[:MAX_POSTS]:
        posts.append(entry.link)

    return posts


def extract_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    paragraphs = soup.find_all("p")

    text = "\n".join([p.get_text() for p in paragraphs])

    return text[:3000]


def generate_style_examples():

    urls = fetch_medium_posts()

    examples = []

    for i, url in enumerate(urls):

        text = extract_text(url)

        examples.append(f"Example {i+1}:\n{text}\n\n---\n")

    return "\n".join(examples)


def save_style_examples():

    style_text = generate_style_examples()

    path = os.path.join(PROMPT_FOLDER, "style_examples.txt")

    with open(path, "w") as f:
        f.write(style_text)

    print("Updated style examples from Medium")


if __name__ == "__main__":
    save_style_examples()