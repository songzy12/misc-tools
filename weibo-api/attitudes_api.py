import requests
import io
import json
import time

from config import COOKIE


def fetch_attitudes(status_id):
    api_url = "https://m.weibo.cn/api/attitudes/show"
    data = []
    for num in range(60):
        print(num)
        params = {'id': status_id,
                  'page': num}
        try:
            resp = requests.get(api_url, params, cookies=COOKIE)
            resp = resp.json()

        except:
            print(resp)
            import code
            code.interact(local=locals())
        if not resp["ok"]:
            break
        data += resp['data']['data']
        time.sleep(1)
    with io.open("data/attitudes.json", "w", encoding='utf8') as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    status_id = "4336693165197870"
    fetch_attitudes(status_id)
