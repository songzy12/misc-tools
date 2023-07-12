import requests
import time
import json

from .config import MID, COOKIE
from .dynamic_util import build_dynamic_api_url, build_next_dynamic_api_url, extract_picture_urls, download_pictures

OUTPUT_DIR = 'bilibili/output'

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


if __name__ == '__main__':
    picture_urls = extract_all_picture_urls()

    with open(f'{OUTPUT_DIR}/picture_urls.json', mode='w',
              encoding='utf-8') as f:
        json.dump(picture_urls, f, ensure_ascii=False, indent=4)

    download_pictures(picture_urls)
