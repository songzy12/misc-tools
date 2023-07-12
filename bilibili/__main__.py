import requests
import json

from .config import MID, COOKIE
from .dynamic_util import build_dynamic_api_url

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

if __name__ == '__main__':
    dynamic_api_url = build_dynamic_api_url(MID)
    print(dynamic_api_url)
    resp = requests.get(dynamic_api_url, headers=HEADERS)
    print(json.loads(resp.content))
