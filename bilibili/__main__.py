import requests
import json

from . import config

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
    "Cookie": config.COOKIE
}

DYNAMIC_API_ROOT = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space'


def construct_dynamic_api_url(mid, offset=""):
    if offset:
        return f"{DYNAMIC_API_ROOT}?host_mid={mid}&offset={offset}"
    return f"{DYNAMIC_API_ROOT}?host_mid={mid}"


dynamic_api_url = construct_dynamic_api_url(config.MID)
print(dynamic_api_url)
resp = requests.get(dynamic_api_url, headers=HEADERS)
print(json.loads(resp.content))
