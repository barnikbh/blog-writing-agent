import os
from config import DRAFT_FOLDER


def save_blog(notes_filename, content):

    os.makedirs(DRAFT_FOLDER, exist_ok=True)

    blog_filename = notes_filename.replace("_notes.md", "_blog.md")

    path = os.path.join(DRAFT_FOLDER, blog_filename)

    with open(path, "w") as f:
        f.write(content)

    print(f"\nBlog saved to: {path}\n")