import requests
from lxml import etree


def handle_html(url, cookie):
    print(url)
    html = requests.get(url, cookies=cookie).content
    selector = etree.HTML(html)
    return selector


def get_user_info(user, cookie):
    # Code copied from:
    # https://github.com/dataabc/weiboSpider/commit/7d1ac7d857a8309bf47dcaa48e0dc478e7050363
    keys = [
        'id', 'screen_name', 'profile_image_url', 'followers_count',
        'profile_url', 'source', 'created_at'
    ]
    user_info = {k: v for k, v in user.items() if k in keys}

    url = 'https://weibo.cn/%s/info' % user_info['id']
    selector = handle_html(url, cookie)

    basic_info = selector.xpath("//div[@class='c'][3]/text()")
    zh_list = [u'性别', u'地区', u'生日', u'简介', u'认证', u'达人']
    en_list = [
        'gender', 'location', 'birthday', 'description', 'verified_reason',
        'talent', 'education', 'company'
    ]

    for i in basic_info:
        k = i.split(':')[0]
        if k in zh_list:
            k, v = i.split(":", 1)
            user_info[en_list[zh_list.index(k)]] = v.replace('\u3000', '')

    print(user_info)
    return user_info
