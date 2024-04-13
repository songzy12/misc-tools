ATTITUDES_FILENAME = 'output/attitudes/4336693165197870.json'

COOKIE = "a=b;c=d"
COOKIE = {
    t.strip().split("=")[0]: t.strip().split("=")[1]
    for t in COOKIE.split(";")
}
