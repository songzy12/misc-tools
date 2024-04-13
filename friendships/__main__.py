# Given a user id, find its zombie followers.


from .config import UID, ACCESS_TOKEN
from .util import get_follower_ids, get_home_page_url




if __name__ == '__main__':
    follower_ids = get_follower_ids(UID, ACCESS_TOKEN)

    print("zombies:")
    for follower_id in follower_ids:
        print(get_home_page_url(follower_id))
