import io
import sys
import time
import json

from utils import handle_html
from config import COOKIE


def get_user_info(user):
    # Code copied from:
    # https://github.com/dataabc/weiboSpider/commit/7d1ac7d857a8309bf47dcaa48e0dc478e7050363
    keys = ['id', 'screen_name', 'profile_image_url',
            'followers_count', 'profile_url', 'source', 'created_at']
    user_info = {k: v for k, v in user.items() if k in keys}

    url = 'https://weibo.cn/%s/info' % user_info['id']
    selector = handle_html(url, COOKIE)

    basic_info = selector.xpath("//div[@class='c'][3]/text()")
    zh_list = [u'性别', u'地区', u'生日', u'简介', u'认证', u'达人']
    en_list = [
        'gender', 'location', 'birthday', 'description',
        'verified_reason', 'talent', 'education', 'company'
    ]

    for i in basic_info:
        k = i.split(':')[0]
        if k in zh_list:
            k, v = i.split(":", 1)
            user_info[en_list[zh_list.index(k)]] = v.replace('\u3000', '')
    print(user_info)
    return user_info


if __name__ == "__main__":
    items = {}
    with open("data/attitudes.json") as f:
        items = json.loads(f.read())

    user_info = []
    user_id_set = set()
    with open("data/last_index.txt") as f:
        start = int(f.read())
    try:
        for i, item in enumerate(items):
            if i < start:
                continue
            user = item["user"]
            if user['id'] in user_id_set:
                continue
            user_id_set.add(user['id'])

            user["source"] = item["source"]
            user['created_at'] = item['created_at']
            print(i, user['screen_name'])
            user_info.append(get_user_info(user))
            time.sleep(3)
    except:
        print(sys.exc_info())
    finally:
        with io.open("data/user_info_%s_%s.json" % (start, i), "w", encoding="utf8") as f:
            f.write(json.dumps(user_info, indent=4, ensure_ascii=False))
        with io.open("data/last_index.txt", "w") as f:
            f.write(str(i))
