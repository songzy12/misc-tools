DYNAMIC_API_ROOT = 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/space'


def build_dynamic_api_url(mid, offset=""):
    if offset:
        return f"{DYNAMIC_API_ROOT}?host_mid={mid}&offset={offset}"
    return f"{DYNAMIC_API_ROOT}?host_mid={mid}"
