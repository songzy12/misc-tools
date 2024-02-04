import requests
import time

MAX_PAGE = 50


def fetch_attitudes(status_id, cookie):
    api_url = "https://m.weibo.cn/api/attitudes/show"
    attitudes = []
    for page in range(MAX_PAGE):
        time.sleep(1)

        params = {'id': status_id, 'page': page}
        print(params)

        resp = requests.get(api_url, params, cookies=cookie)
        resp = resp.json()

        if not resp['data']['data']:
            break
        attitudes += resp['data']['data']
    return attitudes
