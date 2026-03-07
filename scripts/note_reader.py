import glob
import os
from config import SRC_FOLDER


def read_notes():

    files = glob.glob(os.path.join(SRC_FOLDER, "*.md"))

    if not files:
        return None, ""

    latest_file = max(files, key=os.path.getctime)

    with open(latest_file, "r") as f:
        content = f.read()

    filename = os.path.basename(latest_file)

    return filename, content