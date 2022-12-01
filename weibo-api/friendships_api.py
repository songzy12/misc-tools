# Given a user id, find its zombie followers.
import requests

from utils import get_home_page
from config import UID, ACCESS_TOKEN


def follower_ids(uid, access_token):
    # Doc: https://open.weibo.com/wiki/2/friendships/followers/ids
    # Access token: https://open.weibo.com/tools/console

    url = "https://api.weibo.com/2/friendships/followers/ids.json"
    params = {'uid': uid,
              'access_token': access_token}

    resp = requests.get(url, params).json()
    print("resp of followers/ids:")
    print(str(resp))
    ids = resp['ids']
    return ids


if __name__ == '__main__':
    follower_ids = follower_ids(UID, ACCESS_TOKEN)
    print("zombies:")
    for uid in follower_ids:
        print(get_home_page(uid))
