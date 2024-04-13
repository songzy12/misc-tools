import json
import os
import time

import requests

from .config import UID, COOKIE, START_URL

OUTPUT_ROOT_DIR = 'output/statuses'
OBSOLETE_MBLOGS_FILENAME = 'obsolete_mblogs.json'


def make_parent_dirs_if_not_exist(filepath):
    parent_dir = os.path.dirname(filepath)
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir, exist_ok=True)


def fetch_mblogs(url, cookie):
    headers = {
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
        "Cookie": cookie
    }

    return requests.get(url, headers=headers).json()


def get_next_url(resp, page):
    since_id = resp['data']['since_id']
    return f"https://weibo.com/ajax/statuses/mymblog?uid={UID}&page={page}&feature=0&since_id={since_id}"


def get_mblogs(resp):
    cur_mblogs = resp['data']['list']
    obsolete_mblogs = {}
    for cur_mblog in cur_mblogs:
        # 只查看转发微博
        if 'retweeted_status' not in cur_mblog:
            continue

        # 当前不可见微博包含“抱歉”二字
        # 1. 抱歉，作者已设置仅展示半年内微博，此微博已不可见。
        # 2. 抱歉，此微博已被作者删除。
        # 3. 抱歉，由于作者设置，你暂时没有这条微博的查看权限哦。
        retweeted_status_text = cur_mblog['retweeted_status']['text']
        if "抱歉" not in retweeted_status_text:
            continue

        mblogid = cur_mblog["mblogid"]
        mblog_url = f"https://weibo.com/{UID}/{mblogid}"
        obsolete_mblogs[mblog_url] = retweeted_status_text
        print(mblog_url, retweeted_status_text)
    return obsolete_mblogs, len(cur_mblogs)


url = START_URL if START_URL != "" else f"https://weibo.com/ajax/statuses/mymblog?uid={UID}&page=1&feature=0"

# TODO: parse page from url
page = 1
obsolete_mblogs = {}
while True:
    print(f"url: {url}")
    resp = fetch_mblogs(url, COOKIE)
    cur_obsolete_mblogs, has_mblogs = get_mblogs(resp)
    obsolete_mblogs = {**obsolete_mblogs, **cur_obsolete_mblogs}
    if not has_mblogs:
        break
    page += 1
    url = get_next_url(resp, page)
    time.sleep(3)

print(f"len(mblogs): {len(obsolete_mblogs)}")
obsolete_mblogs_filepath = os.path.join(OUTPUT_ROOT_DIR, str(UID),
                                        OBSOLETE_MBLOGS_FILENAME)
if not os.path.exists(obsolete_mblogs_filepath):
    make_parent_dirs_if_not_exist(obsolete_mblogs_filepath)
    with open(obsolete_mblogs_filepath, mode='w', encoding='utf-8') as f:
        json.dump(obsolete_mblogs, f, ensure_ascii=False, indent=4)
