UID = 0
ACCESS_TOKEN = "x"
COOKIE = "a=b;c=d"
COOKIE = {t.strip().split("=")[0]: t.strip().split("=")[1]
          for t in COOKIE.split(";")}
