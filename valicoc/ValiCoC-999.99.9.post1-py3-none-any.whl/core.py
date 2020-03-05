from re import *
def get(msg):
    reg = r"^.*?ÑéÖ¤Âë.*?(?P<validation_code>\d{4,})"
    res = search(reg, msg)
    return res.groupdict()['validation_code']
