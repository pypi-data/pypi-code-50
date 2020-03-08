import time
import hmac
import hashlib
import base64
from urllib import parse as urlparse

__author__ = """Florian Ludwig"""
__version__ = "0.5.0"




def check_secure_link(url, key, t=None):
    """check given url's signature with provided key

    :param url:
    :param key:
    :param t:
    """
    if "&s=" not in url:
        return False

    query = urlparse.urlparse(url).query
    query = urlparse.parse_qs(query)

    if not "e" in query:
        return False

    expire = query["e"][-1]
    if not expire.isdigit():
        return False
    expire = int(expire)

    if t is None:
        t = int(time.time())

    if expire < t:
        # link is expired
        return False

    signed_url, e = url.rsplit("&s=", 1)
    # remove expire-param from url
    base_url = signed_url[: signed_url.rfind("e=") - 1]

    # replace url-unsafe charackters in signature
    e = e.replace(" ", "-")  # + signs are spaces in urls
    e = e.replace("+", "-")  # + signs might have been urlencoded
    e = e.replace("/", "_")

    check = get_secure_link(base_url, key, expire, 0)
    return check == signed_url + "&s=" + e


def get_secure_link(url, key, expire=60, t=None):
    """Sign url or POST data with hmac

    :param str url: The url to sign
    :param str key: The shared secret
    :param int expire: Time in seconds until link expires
    :param int t: The current timestamp (utc)
    :rtype: str
    """
    if "?" in url:
        url += "&"
    else:
        url += "?"
    if t is None:
        t = int(time.time())

    expire += t
    url += "e=" + str(expire)
    s = hmac.new(key.encode(), url.encode(), hashlib.sha256).digest()
    return url + "&s=" + base64.b64encode(s, b"-_").decode().rstrip("=")
