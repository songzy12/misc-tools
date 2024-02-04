import io
import json
import os
import time

from .config import COOKIE, ATTITUDES_FILENAME
from .util import get_user_info

OUTPUT_ROOT_DIR = "output"


def get_users_from_attitudes_file(ATTITUDES_FILENAME):
    with open(ATTITUDES_FILENAME) as f:
        items = json.loads(f.read())
    return [item["user"] for item in items]


def make_parent_dirs_if_not_exist(filepath):
    parent_dir = os.path.dirname(filepath)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)


if __name__ == "__main__":
    users = get_users_from_attitudes_file(ATTITUDES_FILENAME)

    for index, user in enumerate(users):
        output_filepath = os.path.join(OUTPUT_ROOT_DIR, "user_info",
                                       f"{user['id']}.json")
        if os.path.exists(output_filepath):
            print(f"skipped: {user['screen_name']}")
            continue

        time.sleep(1)
        print(f"crawling: {index}/{len(users)} {user['screen_name']}")

        user_info = get_user_info(user, COOKIE)

        make_parent_dirs_if_not_exist(output_filepath)
        with io.open(output_filepath, "w", encoding="utf8") as f:
            f.write(json.dumps(user_info, indent=4, ensure_ascii=False))
