import requests
from lxml import etree


def handle_html(url, cookie):
    print(url)
    html = requests.get(url, cookies=cookie).content
    selector = etree.HTML(html)
    return selector


def get_home_page(uid):
    home_page_url = "https://weibo.com/u/%s"
    return home_page_url % uid
