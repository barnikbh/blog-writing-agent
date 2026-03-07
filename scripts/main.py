from note_reader import read_notes
from outline_generator import generate_outline
from blog_writer import generate_blog
from style_editor import edit_blog
from diagram_generator import replace_diagrams
from style_fetcher import save_style_examples
from file_writer import save_blog


def main():

    print("Updating writing style from Medium...")
    save_style_examples()

    notes_filename, notes = read_notes()

    if not notes:
        print("No notes found in src/")
        return

    print("Generating outline...")
    outline = generate_outline(notes)

    print("Writing blog draft...")
    blog = generate_blog(outline, notes)

    print("Applying style editor...")
    blog = edit_blog(blog)

    print("Generating diagrams...")
    blog = replace_diagrams(blog)

    save_blog(notes_filename, blog)


if __name__ == "__main__":
    main()