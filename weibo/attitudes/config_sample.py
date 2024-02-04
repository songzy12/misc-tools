STATUS_ID = "4336693165197870"

COOKIE = "a=b;c=d"
COOKIE = {
    t.strip().split("=")[0]: t.strip().split("=")[1]
    for t in COOKIE.split(";")
}
