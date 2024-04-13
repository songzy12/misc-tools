import requests


def get_follower_ids(uid, access_token):
    # Doc: https://open.weibo.com/wiki/2/friendships/followers/ids
    # Access token: https://open.weibo.com/tools/console

    url = "https://api.weibo.com/2/friendships/followers/ids.json"
    params = {'uid': uid, 'access_token': access_token}

    resp = requests.get(url, params).json()
    print(f"friendships/followers/ids:\n{resp}\n")

    return resp['ids']


def get_home_page_url(uid):
    return f"https://weibo.com/u/{uid}"
