import os
import requests
import time
import json

from datetime import datetime

from .config import MID, COOKIE
from .dynamic_util import build_dynamic_api_url, build_next_dynamic_api_url, extract_picture_urls

OUTPUT_DIR = 'bilibili/output'
URLS_FILENAME = 'picture_urls.json'

HEADERS = {
    "User-Agent":
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cookie": COOKIE
}


def extract_all_picture_urls():
    picture_urls = {}

    dynamic_api_url = build_dynamic_api_url(MID)
    print(dynamic_api_url)
    while dynamic_api_url != '':
        resp = requests.get(dynamic_api_url, headers=HEADERS).json()

        current_picture_urls = extract_picture_urls(resp)
        picture_urls = picture_urls | current_picture_urls

        dynamic_api_url = build_next_dynamic_api_url(MID, resp)
        print(dynamic_api_url)

        time.sleep(3)

    return picture_urls


def download_picture(url, filepath):
    parent_dir = os.path.dirname(filepath)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)
    print(url, filepath)


def download_pictures(picture_urls):
    for pub_ts, urls in picture_urls.items():
        pub_dt = datetime.fromtimestamp(int(pub_ts))
        for index, url in enumerate(urls):
            picture_name = os.path.basename(url)
            download_picture(
                url,
                f'{OUTPUT_DIR}/{MID}/{pub_dt.strftime("%Y%m%d_%H%M%S")}/{index}_{picture_name}'
            )


if __name__ == '__main__':
    URLS_PATH = f"{OUTPUT_DIR}/{URLS_FILENAME}"

    picture_urls = {}
    if not os.path.exists(URLS_PATH):
        picture_urls = extract_all_picture_urls()

        with open(URLS_PATH, mode='w', encoding='utf-8') as f:
            json.dump(picture_urls, f, ensure_ascii=False, indent=4)

    with open(URLS_PATH) as f:
        picture_urls = json.loads(f.read())

    download_pictures(picture_urls)
