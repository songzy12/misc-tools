import io
import json
import os

from .util import fetch_attitudes

from .config import COOKIE, STATUS_ID

OUTPUT_ROOT_DIR = "output/"


def make_parent_dirs_if_not_exist(filepath):
    parent_dir = os.path.dirname(filepath)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)


if __name__ == "__main__":
    attitudes = fetch_attitudes(STATUS_ID, COOKIE)

    output_attitudes_path = os.path.join(OUTPUT_ROOT_DIR, "attitudes",
                                         f"{STATUS_ID}.json")
    make_parent_dirs_if_not_exist(output_attitudes_path)
    with io.open(output_attitudes_path, "w", encoding='utf8') as f:
        f.write(json.dumps(attitudes, indent=4, ensure_ascii=False))
